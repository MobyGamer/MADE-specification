@echo off
:: SPDX-License-Identifier: CC0-1.0
:: Double-click to manually regenerate index.html after revising MADE-SPECIFICATION.md.
:: Any command-line flags (such as --check or --watch) are forwarded to sync_spec.py.
setlocal EnableExtensions EnableDelayedExpansion

where python >nul 2>nul
if not errorlevel 1 (
    python "%~dp0sync_spec.py" %*
) else (
    where py >nul 2>nul
    if not errorlevel 1 (
        py -3 "%~dp0sync_spec.py" %*
    ) else (
        echo ERROR: Neither 'python' nor 'py' launcher was found in PATH.
        pause
        exit /b 1
    )
)

set "EXIT_CODE=%ERRORLEVEL%"
if not "%EXIT_CODE%"=="0" (
    echo.
    echo Synchronization failed with exit code %EXIT_CODE%.
    set "_CMD=!CMDCMDLINE!"
    if not "!_CMD:/c=!"=="!_CMD!" pause
)
exit /b %EXIT_CODE%
