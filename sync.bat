@echo off
cd /d %~dp0

git add .
if errorlevel 1 exit /b %errorlevel%

git commit -m "test"
if errorlevel 1 exit /b %errorlevel%

git push origin main
if errorlevel 1 exit /b %errorlevel%

echo OK
pause