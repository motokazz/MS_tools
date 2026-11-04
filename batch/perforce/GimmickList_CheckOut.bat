rem リストギミックチェックアウト

call :CHECKOUT "D:\Mproject\mdata\db\filelist\122_list_gimmick.xlsm"
call :CHECKOUT "D:\Mproject\mgamedata\db\filelist\122_list_gimmick.csv"

pause
exit

:CHECKOUT
p4 lock %1
p4 edit -c default %1
exit /b






