@echo off
rem DIRLIST
echo dirlist>%~dp0\dir_list_filename.txt
for %%a in (%*) do (call :DIRLIST %%a)
%~dp0\dir_list_filename.txt
exit


:DIRLIST
echo %~n1>>%~dp0\dir_list_filename.txt
exit /b

