@echo off
:: Unified launcher wrapper for Windows cmd / PowerShell
:: Usage: kickoff filename.genz   (or)   kickoff            (starts REPL)
:: This batch file simply calls the Python launcher located next to it.

python "%~dp0kickoff.py" %*
@echo off
REM kickoff.bat - convenient wrapper to run GenZLang examples
SET SCRIPT_DIR=%~dp0
IF "%~1"=="" (
  python "%SCRIPT_DIR%run_genz.py"
  GOTO :EOF
)

REM If the user passed a full path or relative path that exists, use it
IF EXIST "%~1" (
  python "%SCRIPT_DIR%run_genz.py" "%~1"
  GOTO :EOF
)

REM If the file exists in the examples folder, use it
IF EXIST "%SCRIPT_DIR%examples\%~1" (
  python "%SCRIPT_DIR%run_genz.py" "%SCRIPT_DIR%examples\%~1"
  GOTO :EOF
)

REM If the argument does not contain a path separator, try examples\<file>
echo %~1 | findstr /C:"\" >nul
IF ERRORLEVEL 1 (
  IF EXIST "%SCRIPT_DIR%examples\%~1" (
    python "%SCRIPT_DIR%run_genz.py" "%SCRIPT_DIR%examples\%~1"
    GOTO :EOF
  )
)

REM Fallback: try passing the argument as-is to the runner
python "%SCRIPT_DIR%run_genz.py" "%~1"
