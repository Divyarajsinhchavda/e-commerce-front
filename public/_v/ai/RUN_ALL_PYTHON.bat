@echo off
chcp 65001 >nul
cd /d "%~dp0"
for %%i in (01 02 03 04 05 06 07 08 09) do (
  echo ================ Practical_%%i ================
  python Practical_%%i.py
  echo.
)
pause
