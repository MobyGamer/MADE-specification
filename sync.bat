@echo off
setlocal
python "%~dp0sync_spec.py" %*
set "EXIT_CODE=%ERRORLEVEL%"
if not "%EXIT_CODE%"=="0" (
    echo.
    echo Synchronization failed with exit code %EXIT_CODE%.
    echo %CMDCMDLINE% | find /i "%~0" >nul
    if not errorlevel 1 pause
)
exit /b %EXIT_CODE%
