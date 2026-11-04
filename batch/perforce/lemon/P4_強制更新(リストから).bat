echo 更新（強制更新）
@echo off
rem setlocal

rem set PATH=%PATH%;C:\cygwin\bin;D:\p4works\bin

cd d:\Mproject
d:
rem set P4CHARSET=none
rem set P4COMMANDCHARSET=none
rem set P4CLIENT=Motokazu_Sakai
rem set P4PORT=43.9.1.107:1668
rem set P4USER=Motokazu_Sakai
rem p4 login -a < d:\mel\jstapass.txt

p4 -x - sync -f < C:\Users\s002000\Desktop\commitbatch\p4synclist.txt

pause

rem svn update
rem endlocal
