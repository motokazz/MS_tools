@echo off
echo 更新（強制更新）

for %%a in (%*) do (call :FORCEUPDATE %%a)
pause
exit


:FORCEUPDATE
p4 revert -k %1
p4 sync -f %1
exit /b

