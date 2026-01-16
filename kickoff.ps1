param(
    [string]$file
)
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
if (-not $file) {
    python "$scriptDir\run_genz.py"
    return
}

# If provided path exists, use it; else try examples\<file>
if (Test-Path $file) {
    python "$scriptDir\run_genz.py" $file
    return
}

$examplesPath = Join-Path $scriptDir "examples\$file"
if (Test-Path $examplesPath) {
    python "$scriptDir\run_genz.py" $examplesPath
    return
}

# fallback: pass the argument as-is
python "$scriptDir\run_genz.py" $file
