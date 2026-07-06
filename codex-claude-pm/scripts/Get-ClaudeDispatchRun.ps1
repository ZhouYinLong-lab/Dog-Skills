param(
    [string]$WorkingDirectory = (Get-Location).Path,
    [string]$LogDirectory,
    [string]$JobId,
    [switch]$All,
    [switch]$Result,
    [switch]$Json
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Read-JsonFile {
    param([Parameter(Mandatory = $true)][string]$Path)
    Get-Content -Raw -LiteralPath $Path | ConvertFrom-Json
}

function Get-RunsRoot {
    param([Parameter(Mandatory = $true)][string]$Cwd)
    Join-Path $Cwd ".codex-claude-pm\runs"
}

function Get-ObjectValue {
    param(
        $Object,
        [Parameter(Mandatory = $true)][string]$Name,
        $Default = $null
    )
    if ($null -eq $Object) {
        return $Default
    }
    $property = $Object.PSObject.Properties[$Name]
    if ($null -eq $property) {
        return $Default
    }
    return $property.Value
}

function Get-RunRecords {
    param([Parameter(Mandatory = $true)][string]$RunsRoot)
    if (-not (Test-Path -LiteralPath $RunsRoot)) {
        return @()
    }

    $runDirs = if (Test-Path -LiteralPath (Join-Path $RunsRoot "status.json")) {
        @(Get-Item -LiteralPath $RunsRoot)
    } else {
        @(Get-ChildItem -LiteralPath $RunsRoot -Directory)
    }

    $runDirs | ForEach-Object {
        $statusPath = Join-Path $_.FullName "status.json"
        $metadataPath = Join-Path $_.FullName "metadata.json"
        $status = if (Test-Path -LiteralPath $statusPath) { Read-JsonFile -Path $statusPath } else { $null }
        $metadata = if (Test-Path -LiteralPath $metadataPath) { Read-JsonFile -Path $metadataPath } else { $null }
        [pscustomobject]@{
            JobId = if (Get-ObjectValue $status "jobId") { Get-ObjectValue $status "jobId" } elseif (Get-ObjectValue $metadata "jobId") { Get-ObjectValue $metadata "jobId" } else { $_.Name }
            Status = if (Get-ObjectValue $status "status") { Get-ObjectValue $status "status" } else { "unknown" }
            UpdatedAt = Get-ObjectValue $status "updatedAt"
            ExitCode = Get-ObjectValue $status "exitCode"
            Pid = Get-ObjectValue $status "pid"
            LogDirectory = $_.FullName
            Summary = if (Get-ObjectValue $metadata "taskPackagePath") { Get-ObjectValue $metadata "taskPackagePath" } else { "" }
            StdoutPath = Join-Path $_.FullName "stdout.txt"
            StderrPath = Join-Path $_.FullName "stderr.txt"
            MetadataPath = $metadataPath
            StatusPath = $statusPath
        }
    } | Sort-Object UpdatedAt -Descending
}

$resolvedWorkingDirectory = (Resolve-Path -LiteralPath $WorkingDirectory).Path
$runsRoot = if ([string]::IsNullOrWhiteSpace($LogDirectory)) {
    Get-RunsRoot -Cwd $resolvedWorkingDirectory
} else {
    (Resolve-Path -LiteralPath $LogDirectory).Path
}
$records = @(Get-RunRecords -RunsRoot $runsRoot)

if (-not $All -and [string]::IsNullOrWhiteSpace($JobId)) {
    $records = @($records | Select-Object -First 10)
}

if (-not [string]::IsNullOrWhiteSpace($JobId)) {
    $records = @($records | Where-Object { $_.JobId -eq $JobId -or (Split-Path -Leaf $_.LogDirectory) -eq $JobId })
    if ($records.Count -eq 0) {
        throw "No Claude dispatch run found for JobId: $JobId"
    }
}

if ($Result) {
    foreach ($record in $records) {
        if (Test-Path -LiteralPath $record.StdoutPath) {
            Get-Content -Raw -LiteralPath $record.StdoutPath
        } else {
            Write-Output "No stdout captured for $($record.JobId)."
        }
    }
    exit 0
}

if ($Json) {
    $records | ConvertTo-Json -Depth 8
    exit 0
}

if ($records.Count -eq 0) {
    Write-Output "No Claude Code dispatch runs found."
    exit 0
}

$records | Select-Object JobId,Status,ExitCode,Pid,UpdatedAt,LogDirectory | Format-Table -AutoSize
