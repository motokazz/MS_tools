@echo off
echo 更新（強制更新）

for %%a in (%*) do (call :FORCEUPDATE %%a)
pause
exit


:FORCEUPDATE
rem p4 sync -s %1
rem p4 edit -c default %1
p4 delete %1
rem p4 submit -f submitunchanged -d "未使用削除" %1
exit /b

