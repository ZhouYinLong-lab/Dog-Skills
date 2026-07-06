param(
    [string]$WorkingDirectory = (Get-Location).Path,
    [string]$LogDirectory,
    [Parameter(Mandatory = $true)][string]$JobId
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Write-TextFile {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [AllowEmptyString()][string]$Content
    )
    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $Content, $utf8NoBom)
}

function Read-JsonFile {
    param([Parameter(Mandatory = $true)][string]$Path)
    Get-Content -Raw -LiteralPath $Path | ConvertFrom-Json
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

$resolvedWorkingDirectory = (Resolve-Path -LiteralPath $WorkingDirectory).Path
$runsRoot = if ([string]::IsNullOrWhiteSpace($LogDirectory)) {
    Join-Path $resolvedWorkingDirectory ".codex-claude-pm\runs"
} else {
    (Resolve-Path -LiteralPath $LogDirectory).Path
}
if (-not (Test-Path -LiteralPath $runsRoot)) {
    throw "No dispatch runs directory found: $runsRoot"
}

$candidateRunDirs = if (Test-Path -LiteralPath (Join-Path $runsRoot "status.json")) {
    @(Get-Item -LiteralPath $runsRoot)
} else {
    @(Get-ChildItem -LiteralPath $runsRoot -Directory)
}

$runDir = $candidateRunDirs | Where-Object {
    $_.Name -eq $JobId -or ((Test-Path -LiteralPath (Join-Path $_.FullName "status.json")) -and ((Get-ObjectValue (Read-JsonFile -Path (Join-Path $_.FullName "status.json")) "jobId") -eq $JobId))
} | Select-Object -First 1

if (-not $runDir) {
    throw "No Claude dispatch run found for JobId: $JobId"
}

$statusPath = Join-Path $runDir.FullName "status.json"
$stderrPath = Join-Path $runDir.FullName "stderr.txt"
$status = Read-JsonFile -Path $statusPath
$pidValue = Get-ObjectValue $status "pid"
if (-not $pidValue) {
    Write-Output "Run $JobId has no active pid. Current status: $(Get-ObjectValue $status "status" "unknown")"
    exit 0
}

$process = Get-Process -Id ([int]$pidValue) -ErrorAction SilentlyContinue
if (-not $process) {
    $status.status = "cancelled"
    $status.pid = $null
    $status.updatedAt = (Get-Date).ToString("o")
    $status.cancelledAt = $status.updatedAt
    Write-TextFile -Path $statusPath -Content ($status | ConvertTo-Json -Depth 10)
    Write-Output "Run $JobId process was already gone; marked cancelled."
    exit 0
}

Stop-Process -Id $process.Id -Force
$status.status = "cancelled"
$status.pid = $null
$status.updatedAt = (Get-Date).ToString("o")
$status.cancelledAt = $status.updatedAt
Write-TextFile -Path $statusPath -Content ($status | ConvertTo-Json -Depth 10)
if (-not (Test-Path -LiteralPath $stderrPath)) {
    Write-TextFile -Path $stderrPath -Content ""
}
Add-Content -LiteralPath $stderrPath -Value "[cancelled $(Get-Date -Format o)] Cancelled by user."
Write-Output "Cancelled Claude dispatch run $JobId."
