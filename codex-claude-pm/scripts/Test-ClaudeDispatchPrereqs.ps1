param(
    [string]$WorkingDirectory = (Get-Location).Path,
    [string]$ClaudeCommand = "claude",
    [switch]$SkipClaudeHelp,
    [switch]$Json
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function New-CheckResult {
    param(
        [string]$Name,
        [bool]$Pass,
        [string]$Detail,
        [string]$Remediation = ""
    )

    [pscustomobject]@{
        name = $Name
        pass = $Pass
        detail = $Detail
        remediation = $Remediation
    }
}

$results = New-Object System.Collections.Generic.List[object]

try {
    $resolvedWorkingDirectory = (Resolve-Path -LiteralPath $WorkingDirectory).Path
    $results.Add((New-CheckResult -Name "working-directory" -Pass $true -Detail $resolvedWorkingDirectory))
} catch {
    $results.Add((New-CheckResult -Name "working-directory" -Pass $false -Detail $_.Exception.Message -Remediation "Pass a valid -WorkingDirectory."))
    $resolvedWorkingDirectory = $WorkingDirectory
}

$claudeSource = $null
try {
    $commandInfo = Get-Command $ClaudeCommand -ErrorAction Stop
    $claudeSource = $commandInfo.Source
    if ([string]::IsNullOrWhiteSpace($claudeSource)) {
        $claudeSource = $commandInfo.Name
    }
    $results.Add((New-CheckResult -Name "claude-command" -Pass $true -Detail $claudeSource))
} catch {
    $results.Add((New-CheckResult -Name "claude-command" -Pass $false -Detail $_.Exception.Message -Remediation "Install Claude Code CLI or pass -ClaudeCommand with the executable path."))
}

if (-not $SkipClaudeHelp -and $null -ne $claudeSource) {
    try {
        $helpOutput = & $ClaudeCommand --help 2>&1 | Select-Object -First 5 | Out-String
        $hasPrintMode = $helpOutput -match "--print|-p"
        $results.Add((New-CheckResult -Name "claude-noninteractive-help" -Pass $hasPrintMode -Detail ($helpOutput.Trim()) -Remediation "Update Claude Code CLI if -p/--print is missing."))
    } catch {
        $results.Add((New-CheckResult -Name "claude-noninteractive-help" -Pass $false -Detail $_.Exception.Message -Remediation "Run Claude Code once manually and resolve install/auth issues."))
    }
}

try {
    Push-Location $resolvedWorkingDirectory
    try {
        $gitTop = git rev-parse --show-toplevel 2>$null
        if ($LASTEXITCODE -eq 0 -and -not [string]::IsNullOrWhiteSpace($gitTop)) {
            $status = git status --short 2>$null | Out-String
            $detail = if ([string]::IsNullOrWhiteSpace($status)) { "git repo clean or no short changes" } else { $status.Trim() }
            $results.Add((New-CheckResult -Name "git-status" -Pass $true -Detail $detail))
        } else {
            $results.Add((New-CheckResult -Name "git-status" -Pass $false -Detail "Not a git repository." -Remediation "Use a git worktree or be prepared to inspect file changes manually."))
        }
    } finally {
        Pop-Location
    }
} catch {
    $results.Add((New-CheckResult -Name "git-status" -Pass $false -Detail $_.Exception.Message -Remediation "Ensure git is installed and the working directory is accessible."))
}

$failed = @($results | Where-Object { -not $_.pass })
$summary = [pscustomobject]@{
    ok = ($failed.Count -eq 0)
    failed = $failed.Count
    checks = $results
}

if ($Json) {
    $summary | ConvertTo-Json -Depth 5
} else {
    foreach ($result in $results) {
        $mark = if ($result.pass) { "PASS" } else { "FAIL" }
        Write-Output "[$mark] $($result.name): $($result.detail)"
        if (-not $result.pass -and -not [string]::IsNullOrWhiteSpace($result.remediation)) {
            Write-Output "       fix: $($result.remediation)"
        }
    }
}

if ($failed.Count -gt 0) {
    exit 1
}

exit 0
