@echo off
rem DIRLIST

type nul>%~dp0\dir_list_filename.txt

for %%a in (%*) do (call :DIRLIST %%a)
clip < %~dp0\dir_list_filename.txt
exit


:DIRLIST
echo %1>>%~dp0\dir_list_filename.txt
exit /b

