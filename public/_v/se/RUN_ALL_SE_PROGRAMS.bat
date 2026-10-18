@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ================ Practical 9 ================
cd Practical_09_Coverage_Complexity
python practical9_coverage.py
cd ..
echo.
echo ================ Practical 10 ================
cd Practical_10_Test_Suite
python test_suite.py
cd ..
echo.
echo ================ Practical 11 ================
cd Practical_11_OAuth_Login_Tests
python test_auth.py
cd ..
echo.
pause
