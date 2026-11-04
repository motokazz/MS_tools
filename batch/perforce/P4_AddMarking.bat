@echo off
rem Perforce’Ç‰Á

for %%a in (%*) do (call :ADD %%a)
pause
exit


:ADD
p4 add -d -f default %1
rem p4 submit -c "add_from_batch" -d "add" %1
exit /b

