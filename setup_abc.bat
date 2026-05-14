@echo off
setlocal enabledelayedexpansion

:: ========================================
:: 設定エリア：ここを書き換えるだけでOK
:: ========================================
set TARGET_DIR=ABC300
:: ========================================

:: フォルダ名の設定 (例: ABC452)
set SOURCE_FILE=main.py

:: main.pyが存在するかチェック
if not exist "%SOURCE_FILE%" (
    echo [ERROR] %SOURCE_FILE% is not found.
    pause
    exit /b
)

:: フォルダの作成と存在チェック
if not exist "%TARGET_DIR%" (
    mkdir "%TARGET_DIR%"
    echo folder %TARGET_DIR% was created.
) else (
    echo [ERROR] folder %TARGET_DIR% is exist and prosess stopped.
    pause
    exit /b
)

:: A.py から G.py までをコピー
for %%F in (A B C D E F G) do (
    copy "%SOURCE_FILE%" "%TARGET_DIR%\%%F.py" > nul
    echo    -^> %TARGET_DIR%\%%F.py was created.
)

echo.
echo all file copied !
pause