@echo off
setlocal enabledelayedexpansion

:: =========================
:: Settings
:: =========================
set SOURCE_FILE=main.py

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

:: Create folder
if not exist "%TARGET_DIR%" (
    mkdir "%TARGET_DIR%"
    echo Created folder "%TARGET_DIR%"
) else (
    echo [ERROR] Folder "%TARGET_DIR%" already exists.
    pause
    exit /b
)

:: Copy files A-G
for %%F in (A B C D E F G) do (
    copy "%SOURCE_FILE%" "%TARGET_DIR%\%%F.py" > nul
    echo Created "%TARGET_DIR%\%%F.py"
)

echo.
echo Done!
pause