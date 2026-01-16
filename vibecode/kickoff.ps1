param(
    [string]$file
)
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$parent = Split-Path -Parent $scriptDir

# Change to parent directory so relative paths (examples\...) resolve correctly
Push-Location $parent

if (-not $file) {
    python "run_genz.py"
    Pop-Location
    return
}

if (Test-Path $file) {
    python "run_genz.py" $file
    Pop-Location
    return
}

$examplesPath = Join-Path $parent "examples\$file"
if (Test-Path $examplesPath) {
    python "run_genz.py" $examplesPath
    Pop-Location
    return
}

python "run_genz.py" $file
Pop-Location
