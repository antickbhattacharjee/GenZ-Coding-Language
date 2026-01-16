@echo off
REM kickoff.bat for vibecode subfolder — forwards to parent repo runner
SET SCRIPT_DIR=%~dp0
SET FILEARG=%1
REM Change directory to parent (repo root) so relative example paths resolve correctly
PUSHD "%SCRIPT_DIR%.."
SET REPO=%CD%
IF "%FILEARG%"=="" (
  python run_genz.py
  POPD
  GOTO :EOF
)
IF EXIST "%FILEARG%" (
  python "%REPO%\run_genz.py" "%FILEARG%"
  POPD
  GOTO :EOF
)
IF EXIST "%REPO%\examples\%FILEARG%" (
  python "%REPO%\run_genz.py" "%REPO%\examples\%FILEARG%"
  POPD
  GOTO :EOF
)
python "%REPO%\run_genz.py" "%FILEARG%"
POPD
