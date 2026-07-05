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
    [switch]$NoSessionPersistence,
    [switch]$DryRun,
    [switch]$PassThru
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Write-TextFile {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)][string]$Content
    )

    $parent = Split-Path -Parent $Path
    if ($parent -and -not (Test-Path -LiteralPath $parent)) {
        New-Item -ItemType Directory -Path $parent | Out-Null
    }

    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $Content, $utf8NoBom)
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

if ([string]::IsNullOrWhiteSpace($LogDirectory)) {
    $timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $LogDirectory = Join-Path $resolvedWorkingDirectory ".codex-claude-pm\runs\$timestamp"
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
}

Write-TextFile -Path $metadataPath -Content ($metadata | ConvertTo-Json -Depth 6)

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
    Write-Output $preview
    if ($PassThru) {
        [pscustomobject]@{
            ExitCode = 0
            LogDirectory = $LogDirectory
            StdoutPath = $stdoutPath
            StderrPath = $stderrPath
            MetadataPath = $metadataPath
        }
    }
    exit 0
}

$stderrTemp = Join-Path $LogDirectory "stderr.tmp"
Push-Location $resolvedWorkingDirectory
try {
    $output = $prompt | & $ClaudeCommand @claudeArgs 2> $stderrTemp
    $exitCode = if ($null -eq $LASTEXITCODE) { 0 } else { $LASTEXITCODE }
} finally {
    Pop-Location
}

$stdoutText = ($output | Out-String)
$stderrText = if (Test-Path -LiteralPath $stderrTemp) {
    [System.IO.File]::ReadAllText($stderrTemp)
} else {
    ""
}

Write-TextFile -Path $stdoutPath -Content $stdoutText
Write-TextFile -Path $stderrPath -Content $stderrText

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
    }
}

exit $exitCode
