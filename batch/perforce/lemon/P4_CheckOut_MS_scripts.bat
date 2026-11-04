@echo off
rem Perforceチェックアウト

for %%a in (%*) do (call :CHECKOUT %%a)

pause
exit

:CHECKOUT
p4 sync -s %1
p4 sync -s %1/...

p4 edit -c 187146 %1
p4 edit -c 187146 %1\...

p4 lock %1
p4 lock %1\...

exit /b






