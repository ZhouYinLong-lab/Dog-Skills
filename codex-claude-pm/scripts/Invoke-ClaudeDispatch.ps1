param(
    [string]$TaskPackagePath,
    [string]$TaskPackage,
    [string]$WorkingDirectory = (Get-Location).Path,
    [string]$ClaudeCommand = "claude",
    [ValidateSet("acceptEdits", "auto", "bypassPermissions", "manual", "dontAsk", "plan")]
    [string]$PermissionMode = "acceptEdits",
    [ValidateSet("text", "json", "stream-json")]
    [string]$OutputFormat = "text",
    [string]$Model,
    [string]$Agent,
    [string]$Name,
    [string]$MaxBudgetUsd,
    [string[]]$AllowedTools,
    [string[]]$DisallowedTools,
    [string[]]$AddDir,
    [string[]]$AdditionalArgs = @(),
    [string]$LogDirectory,
    [string]$JobId,
    [switch]$NoSessionPersistence,
    [switch]$DryRun,
    [switch]$Background,
    [switch]$PassThru
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Write-TextFile {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [AllowEmptyString()][string]$Content
    )

    $parent = Split-Path -Parent $Path
    if ($parent -and -not (Test-Path -LiteralPath $parent)) {
        New-Item -ItemType Directory -Path $parent | Out-Null
    }

    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $Content, $utf8NoBom)
}

function Write-JsonFile {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)]$Value
    )

    Write-TextFile -Path $Path -Content ($Value | ConvertTo-Json -Depth 10)
}

function Write-RunStatus {
    param(
        [Parameter(Mandatory = $true)][string]$Status,
        [hashtable]$Extra = @{}
    )

    $payload = [ordered]@{
        jobId = $JobId
        status = $Status
        updatedAt = (Get-Date).ToString("o")
        workingDirectory = $resolvedWorkingDirectory
        logDirectory = $LogDirectory
        stdoutPath = $stdoutPath
        stderrPath = $stderrPath
        metadataPath = $metadataPath
    }

    foreach ($key in $Extra.Keys) {
        $payload[$key] = $Extra[$key]
    }

    Write-JsonFile -Path $statusPath -Value $payload
}

if ([string]::IsNullOrWhiteSpace($TaskPackagePath) -and [string]::IsNullOrWhiteSpace($TaskPackage)) {
    throw "Provide either -TaskPackagePath or -TaskPackage."
}

$resolvedWorkingDirectory = (Resolve-Path -LiteralPath $WorkingDirectory).Path

if (-not [string]::IsNullOrWhiteSpace($TaskPackagePath)) {
    $resolvedTaskPackagePath = (Resolve-Path -LiteralPath $TaskPackagePath).Path
    $prompt = [System.IO.File]::ReadAllText($resolvedTaskPackagePath)
} else {
    $resolvedTaskPackagePath = $null
    $prompt = $TaskPackage
}

if ([string]::IsNullOrWhiteSpace($prompt)) {
    throw "Task package is empty."
}

if ([string]::IsNullOrWhiteSpace($JobId)) {
    $JobId = "cc-" + (Get-Date -Format "yyyyMMdd-HHmmss") + "-" + ([guid]::NewGuid().ToString("N").Substring(0, 6))
}

if ([string]::IsNullOrWhiteSpace($LogDirectory)) {
    $LogDirectory = Join-Path $resolvedWorkingDirectory ".codex-claude-pm\runs\$JobId"
}

if (-not (Test-Path -LiteralPath $LogDirectory)) {
    New-Item -ItemType Directory -Path $LogDirectory | Out-Null
}

$claudeArgs = @(
    "-p",
    "--permission-mode", $PermissionMode,
    "--output-format", $OutputFormat
)

if (-not [string]::IsNullOrWhiteSpace($Model)) {
    $claudeArgs += @("--model", $Model)
}
if (-not [string]::IsNullOrWhiteSpace($Agent)) {
    $claudeArgs += @("--agent", $Agent)
}
if (-not [string]::IsNullOrWhiteSpace($Name)) {
    $claudeArgs += @("--name", $Name)
}
if (-not [string]::IsNullOrWhiteSpace($MaxBudgetUsd)) {
    $claudeArgs += @("--max-budget-usd", $MaxBudgetUsd)
}
if ($NoSessionPersistence) {
    $claudeArgs += "--no-session-persistence"
}
if ($AllowedTools -and $AllowedTools.Count -gt 0) {
    $claudeArgs += @("--allowedTools", ($AllowedTools -join ","))
}
if ($DisallowedTools -and $DisallowedTools.Count -gt 0) {
    $claudeArgs += @("--disallowedTools", ($DisallowedTools -join ","))
}
if ($AddDir -and $AddDir.Count -gt 0) {
    foreach ($dir in $AddDir) {
        $claudeArgs += @("--add-dir", $dir)
    }
}
if ($AdditionalArgs -and $AdditionalArgs.Count -gt 0) {
    $claudeArgs += $AdditionalArgs
}

$taskCopyPath = Join-Path $LogDirectory "task-package.md"
$stdoutPath = Join-Path $LogDirectory "stdout.txt"
$stderrPath = Join-Path $LogDirectory "stderr.txt"
$metadataPath = Join-Path $LogDirectory "metadata.json"
$statusPath = Join-Path $LogDirectory "status.json"

Write-TextFile -Path $taskCopyPath -Content $prompt

$metadata = [ordered]@{
    timestamp = (Get-Date).ToString("o")
    workingDirectory = $resolvedWorkingDirectory
    taskPackagePath = $resolvedTaskPackagePath
    claudeCommand = $ClaudeCommand
    args = $claudeArgs
    permissionMode = $PermissionMode
    outputFormat = $OutputFormat
    dryRun = [bool]$DryRun
    background = [bool]$Background
    jobId = $JobId
}

Write-JsonFile -Path $metadataPath -Value $metadata

if ($DryRun) {
    $preview = @"
Dry run only. Claude Code was not invoked.

Working directory:
$resolvedWorkingDirectory

Command:
$ClaudeCommand $($claudeArgs -join ' ')

Task package copy:
$taskCopyPath

Run metadata:
$metadataPath
"@
    Write-TextFile -Path $stdoutPath -Content $preview
    Write-RunStatus -Status "dry-run" -Extra @{
        exitCode = 0
        completedAt = (Get-Date).ToString("o")
    }
    Write-Output $preview
    if ($PassThru) {
        [pscustomobject]@{
            ExitCode = 0
            LogDirectory = $LogDirectory
            StdoutPath = $stdoutPath
            StderrPath = $stderrPath
            MetadataPath = $metadataPath
            StatusPath = $statusPath
        }
    }
    exit 0
}

if ($Background) {
    $powershellExe = (Get-Process -Id $PID).Path
    if ([string]::IsNullOrWhiteSpace($powershellExe)) {
        $powershellExe = "powershell"
    }

    $childArgs = @(
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-File", $PSCommandPath,
        "-TaskPackagePath", $taskCopyPath,
        "-WorkingDirectory", $resolvedWorkingDirectory,
        "-ClaudeCommand", $ClaudeCommand,
        "-PermissionMode", $PermissionMode,
        "-OutputFormat", $OutputFormat,
        "-LogDirectory", $LogDirectory,
        "-JobId", $JobId
    )

    if (-not [string]::IsNullOrWhiteSpace($Model)) {
        $childArgs += @("-Model", $Model)
    }
    if (-not [string]::IsNullOrWhiteSpace($Agent)) {
        $childArgs += @("-Agent", $Agent)
    }
    if (-not [string]::IsNullOrWhiteSpace($Name)) {
        $childArgs += @("-Name", $Name)
    }
    if (-not [string]::IsNullOrWhiteSpace($MaxBudgetUsd)) {
        $childArgs += @("-MaxBudgetUsd", $MaxBudgetUsd)
    }
    if ($AllowedTools -and $AllowedTools.Count -gt 0) {
        $childArgs += "-AllowedTools"
        $childArgs += $AllowedTools
    }
    if ($DisallowedTools -and $DisallowedTools.Count -gt 0) {
        $childArgs += "-DisallowedTools"
        $childArgs += $DisallowedTools
    }
    if ($AddDir -and $AddDir.Count -gt 0) {
        $childArgs += "-AddDir"
        $childArgs += $AddDir
    }
    if ($AdditionalArgs -and $AdditionalArgs.Count -gt 0) {
        $childArgs += "-AdditionalArgs"
        $childArgs += $AdditionalArgs
    }
    if ($NoSessionPersistence) {
        $childArgs += "-NoSessionPersistence"
    }

    Write-RunStatus -Status "queued" -Extra @{
        pid = $null
        startedAt = $null
        queuedAt = (Get-Date).ToString("o")
    }

    $process = Start-Process -FilePath $powershellExe -ArgumentList $childArgs -WorkingDirectory $resolvedWorkingDirectory -WindowStyle Hidden -PassThru

    $currentStatus = $null
    if (Test-Path -LiteralPath $statusPath) {
        try {
            $currentStatus = (Get-Content -Raw -LiteralPath $statusPath | ConvertFrom-Json).status
        } catch {
            $currentStatus = $null
        }
    }
    if ($currentStatus -eq "queued" -or [string]::IsNullOrWhiteSpace($currentStatus)) {
        Write-RunStatus -Status "queued" -Extra @{
            pid = $process.Id
            startedAt = $null
            queuedAt = (Get-Date).ToString("o")
        }
    }

    $message = @"
Claude Code dispatch started in the background.

Job ID:
$JobId

Status:
$statusPath

Result:
$stdoutPath

Use:
powershell -ExecutionPolicy Bypass -File .\codex-claude-pm\scripts\Get-ClaudeDispatchRun.ps1 -WorkingDirectory . -JobId $JobId
"@
    Write-TextFile -Path $stdoutPath -Content $message
    Write-Output $message

    if ($PassThru) {
        [pscustomobject]@{
            JobId = $JobId
            Pid = $process.Id
            LogDirectory = $LogDirectory
            StdoutPath = $stdoutPath
            StderrPath = $stderrPath
            MetadataPath = $metadataPath
            StatusPath = $statusPath
        }
    }
    exit 0
}

$stderrTemp = Join-Path $LogDirectory "stderr.tmp"
Write-RunStatus -Status "running" -Extra @{
    pid = $PID
    startedAt = (Get-Date).ToString("o")
}
$commandError = $null
Push-Location $resolvedWorkingDirectory
try {
    try {
        $output = $prompt | & $ClaudeCommand @claudeArgs 2> $stderrTemp
        $exitCode = if ($null -eq $LASTEXITCODE) { 0 } else { $LASTEXITCODE }
    } catch {
        $commandError = $_
        $output = @()
        $exitCode = 1
    }
} finally {
    Pop-Location
}

$stdoutText = ($output | Out-String)
$stderrText = if (Test-Path -LiteralPath $stderrTemp) {
    [System.IO.File]::ReadAllText($stderrTemp)
} else {
    ""
}
if ($null -ne $commandError) {
    $stderrText = ($stderrText.TrimEnd() + "`n" + $commandError.ToString()).TrimStart()
}

Write-TextFile -Path $stdoutPath -Content $stdoutText
Write-TextFile -Path $stderrPath -Content $stderrText
Write-RunStatus -Status $(if ($exitCode -eq 0) { "completed" } else { "failed" }) -Extra @{
    pid = $null
    exitCode = $exitCode
    completedAt = (Get-Date).ToString("o")
}

if (Test-Path -LiteralPath $stderrTemp) {
    Remove-Item -LiteralPath $stderrTemp -Force
}

if (-not [string]::IsNullOrWhiteSpace($stdoutText)) {
    Write-Output $stdoutText
}
if (-not [string]::IsNullOrWhiteSpace($stderrText)) {
    [Console]::Error.WriteLine($stderrText)
}

if ($PassThru) {
    [pscustomobject]@{
        ExitCode = $exitCode
        LogDirectory = $LogDirectory
        StdoutPath = $stdoutPath
        StderrPath = $stderrPath
        MetadataPath = $metadataPath
        StatusPath = $statusPath
    }
}

exit $exitCode
