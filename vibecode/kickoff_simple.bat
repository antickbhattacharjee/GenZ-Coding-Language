@echo off
REM Simple wrapper intended to be run from inside the `vibecode` folder in VSCode
IF "%~1"=="" (
  python "%~dp0..\run_genz.py"
  GOTO :EOF
)
IF EXIST "%~dp0..\examples\%~1" (
  python "%~dp0..\run_genz.py" "%~dp0..\examples\%~1"
  GOTO :EOF
)
python "%~dp0..\run_genz.py" "%~1"
