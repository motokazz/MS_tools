@echo off
echo 更新（安全な同期）

for %%a in (%*) do (call :UPDATE %%a)
pause
exit


:UPDATE
p4 sync -s %1/...
p4 sync -s %1
exit /b


