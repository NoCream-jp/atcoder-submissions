@echo off
setlocal enabledelayedexpansion

:: 1. add (1回目)
git add .
if %errorlevel% NEQ 0 exit /b %errorlevel%

:: 1. add (2回目)
git add .
if %errorlevel% NEQ 0 exit /b %errorlevel%

:: 日付と回数の計算
for /f "usebackq tokens=*" %%i in (`powershell -command "Get-Date -Format 'yyyyMMdd'"`) do set ymd=%%i
for /f "usebackq" %%i in (`git rev-list --count --since^="00:00:00" HEAD`) do set /a count=%%i + 1
if %count% LSS 10 (set num=0%count%) else (set num=%count%)

:: 2. commit
git commit -m "write: %ymd%-%num%"
if %errorlevel% NEQ 0 exit /b %errorlevel%

:: 3. push
git push origin main
if %errorlevel% NEQ 0 exit /b %errorlevel%