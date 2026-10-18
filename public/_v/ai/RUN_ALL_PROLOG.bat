@echo off
cd /d "%~dp0"
for %%i in (10 11 12) do (
  echo ================ Practical_%%i ================
  swipl -q Practical_%%i.pl < nul
  echo.
)
pause
