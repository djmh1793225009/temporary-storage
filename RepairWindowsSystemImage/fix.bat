@echo off

net session >nul 2>&1
if %errorlevel% == 0 (
	echo 正在扫描系统镜像并修复...
	echo.
) else (
	echo 请按任意键关闭窗口并右键单击脚本以管理员身份运行。
	pause >nul
	exit /b
)

echo 正在执行 DISM.exe /Online /Cleanup-image /Scanhealth
DISM.exe /Online /Cleanup-image /Scanhealth
echo.
echo 正在执行 DISM.exe /Online /Cleanup-image /CheckHealth
DISM.exe /Online /Cleanup-Image /CheckHealth
echo.
echo 正在执行 DISM.exe /Online /Cleanup-image /Restorehealth
DISM.exe /Online /Cleanup-image /Restorehealth
echo.
echo 正在执行 sfc /scannow
sfc /scannow
echo.
echo 修复程序结束，按任意键关闭
pause >nul
exit /b
