@echo off
rem Perforceチェックイン

for %%a in (%*) do (call :CHECKIN %%a)
pause
exit


:CHECKIN
p4 unlock %1
p4 submit -f submitunchanged -d "チェックイン" %1
exit /b

