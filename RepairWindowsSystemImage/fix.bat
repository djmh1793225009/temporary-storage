@echo off

net session >nul 2>&1
if %errorlevel% == 0 (
	echo ����ɨ��ϵͳ�����޸�...
	echo.
) else (
	echo �밴������رմ��ڲ��Ҽ������ű��Թ���Ա������С�
	pause >nul
	exit /b
)

echo ����ִ�� DISM.exe /Online /Cleanup-image /Scanhealth
DISM.exe /Online /Cleanup-image /Scanhealth
echo.
echo ����ִ�� DISM.exe /Online /Cleanup-image /CheckHealth
DISM.exe /Online /Cleanup-Image /CheckHealth
echo.
echo ����ִ�� DISM.exe /Online /Cleanup-image /Restorehealth
DISM.exe /Online /Cleanup-image /Restorehealth
echo.
echo ����ִ�� sfc /scannow
sfc /scannow
echo.
echo �޸������������������ر�
pause >nul
exit /b
