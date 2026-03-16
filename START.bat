@echo off
REM Property Management — Windows Launcher
REM Double-click this file to start the server and open the dashboard.

cd /d "%~dp0"

echo ============================================
echo   Property Management — Starting...
echo ============================================
echo.

REM Check if port 8000 is already in use
netstat -an | findstr ":8000.*LISTENING" >nul 2>&1
if %errorlevel% equ 0 (
    echo Server is already running on port 8000.
    echo Opening browser...
    start http://localhost:8000
    exit /b 0
)

REM Find Python 3.11+
set PYTHON=
where python >nul 2>&1
if %errorlevel% equ 0 (
    for /f "tokens=*" %%v in ('python -c "import sys; print(sys.version_info.minor)"') do set PYVER=%%v
    if %PYVER% geq 11 set PYTHON=python
)

if "%PYTHON%"=="" (
    where py >nul 2>&1
    if %errorlevel% equ 0 (
        for /f "tokens=*" %%v in ('py -3 -c "import sys; print(sys.version_info.minor)"') do set PYVER=%%v
        if %PYVER% geq 11 set PYTHON=py -3
    )
)

if "%PYTHON%"=="" (
    echo.
    echo ERROR: Python 3.11 or later is required.
    echo.
    echo Install Python from: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo Using: %PYTHON%

REM Create virtual environment if needed
if not exist "webapp\.venv" (
    echo Creating virtual environment...
    %PYTHON% -m venv webapp\.venv
)

REM Activate venv
call webapp\.venv\Scripts\activate.bat

REM Install/update dependencies
echo Checking dependencies...
pip install -q -r webapp\requirements.txt

REM Start the server
echo.
echo Starting server...
cd webapp
python -m app
