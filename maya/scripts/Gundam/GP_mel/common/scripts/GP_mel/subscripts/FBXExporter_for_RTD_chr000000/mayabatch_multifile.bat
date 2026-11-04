cd /d %~dp0
@echo off

for %%f in (%*) do (
	echo %%f
	call mayabatch.exe %~dp0 %%f
	call logging %%f
)
pause
