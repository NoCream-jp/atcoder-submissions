@echo off
:: ↓この1行を追加する（文字コードをUTF-8にするコマンド）
chcp 65001 > nul

setlocal enabledelayedexpansion

:: ========================================
:: 設定エリア
:: ========================================
set SOURCE_FILE=main.py

:: 実行時にフォルダ名を入力させる
set /p TARGET_DIR="作成するコンテスト名を入力してください (例: ABC149): "

:: (以下略)

:: 空白のままEnterを押された場合の処理
if "%TARGET_DIR%"=="" (
    echo [ERROR] フォルダ名が入力されていません。
    pause
    exit /b
)

:: ========================================

:: main.pyが存在するかチェック
if not exist "%SOURCE_FILE%" (
    echo [ERROR] "%SOURCE_FILE%" が見つかりません。
    pause
    exit /b
)

:: フォルダの作成と存在チェック
if not exist "%TARGET_DIR%" (
    mkdir "%TARGET_DIR%"
    echo フォルダ "%TARGET_DIR%" を作成しました。
) else (
    echo [ERROR] フォルダ "%TARGET_DIR%" は既に存在するため、処理を中止します。
    pause
    exit /b
)

:: A.py から G.py までをコピー
for %%F in (A B C D E F G) do (
    copy "%SOURCE_FILE%" "%TARGET_DIR%\%%F.py" > nul
    echo    -^> "%TARGET_DIR%\%%F.py" を作成しました。
)

echo.
echo すべてのファイルのコピーが完了しました！
pause