@echo off
setlocal enabledelayedexpansion

:: ========================================
:: 設定エリア：ここを書き換えるだけでOK
:: ========================================
set TARGET_DIR=ABC454
:: ========================================

:: フォルダ名の設定 (例: ABC452)
set SOURCE_FILE=main.py

:: main.pyが存在するかチェック
if not exist %SOURCE_FILE% (
    echo [ERROR] %SOURCE_FILE% が見つかりません。
    pause
    exit /b
)

:: フォルダの作成
if not exist %TARGET_DIR% (
    mkdir %TARGET_DIR%
    echo フォルダ %TARGET_DIR% を作成しました。
) else (
    echo [INFO] %TARGET_DIR% は既に存在します。
)

:: A.py から G.py までをコピー
for %%F in (A B C D E F G) do (
    copy "%SOURCE_FILE%" "%TARGET_DIR%\%%F.py" > nul
    echo   -^> %TARGET_DIR%\%%F.py を作成しました。
)

echo.
echo 全てのファイルのコピーが完了しました！
pause