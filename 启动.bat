@echo off
chcp 65001 >nul
cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 goto try_py

python "%~dp0server.py"
goto end

:try_py
where py >nul 2>nul
if errorlevel 1 (
    echo Python not found. Please install Python, then run this file again.
    pause
    exit /b 1
)
py "%~dp0server.py"

:end
if errorlevel 1 pause
