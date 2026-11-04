
cd d:/Mproject/gtools/batch/
d:
setlocal

set P4CHARSET=none
set P4COMMANDCHARSET=none
set P4PORT=perforce1.ship.scea.com:1666
set P4USER=??SHIPユーザー名??
p4 login -a ??パスワード??
set P4CLIENT=??クライアント名??
rem p4 client -o

set INPUT=D:\Mproject\gtools\batch\update_batch\download_igc_pathlist_local.txt

rem >d:/Mproject/gtools/batch/update_batch/log.txt
for /f %%a in ( %INPUT% ) do (p4 sync -f %%a...#head >d:/Mproject/gtools/batch/update_batch/log.txt)

set P4CHARSET=none
set P4COMMANDCHARSET=none
set P4PORT=43.9.1.107:1668
set P4USER=??ユーザー名??
p4 login -a ??パスワード??
set P4CLIENT=??クライアント名??
rem p4 client -o


pause
