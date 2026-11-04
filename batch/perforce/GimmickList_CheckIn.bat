rem リストギミックチェックアウト

call :CHECKIN "D:\Mproject\mdata\db\filelist\122_list_gimmick.xlsm"
call :CHECKIN "D:\Mproject\mgamedata\db\filelist\122_list_gimmick.csv"

pause
exit


:CHECKIN
p4 unlock %1
p4 submit -f submitunchanged -d "チェックイン" %1
exit /b






