@echo off
setlocal enabledelayedexpansion

:: =========================
:: Settings
:: =========================
set SOURCE_FILE=main.py
set BASE_DIR=contests

:: Input contest name
set /p TARGET_DIR=Enter contest name (e.g. ABC149): 

:: Check empty input
if "%TARGET_DIR%"=="" (
    echo [ERROR] No folder name provided.
    pause
    exit /b
)

:: Check source file
if not exist "%SOURCE_FILE%" (
    echo [ERROR] "%SOURCE_FILE%" not found.
    pause
    exit /b
)

:: Create base folder if it doesn't exist
if not exist "%BASE_DIR%" (
    mkdir "%BASE_DIR%"
)

:: Set full target path
set FULL_TARGET_DIR=%BASE_DIR%\%TARGET_DIR%

:: Create target folder
if not exist "%FULL_TARGET_DIR%" (
    mkdir "%FULL_TARGET_DIR%"
    echo Created folder "%FULL_TARGET_DIR%"
) else (
    echo [ERROR] Folder "%FULL_TARGET_DIR%" already exists.
    pause
    exit /b
)

:: Copy files A-G
for %%F in (A B C D E F G) do (
    copy "%SOURCE_FILE%" "%FULL_TARGET_DIR%\%%F.py" > nul
    echo Created "%FULL_TARGET_DIR%\%%F.py"
)

echo.
echo Done!
pause