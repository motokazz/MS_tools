@echo off

rem PerforceCheckStatus

echo P4CheckStatus>p4checkstatus.txt

for %%a in (%*) do (call :FILELOG %%a)

p4checkstatus.txt

rem pause

exit


:FILELOG
rem p4 sync -n %1
rem p4 describe %1
p4 opened -a %1 >> p4checkstatus.txt
p4 changes -s submitted -l -m 100 %1 >> p4checkstatus.txt
exit /b

