rem net stop TabletServiceWacom
echo タブレットがフリーズしたときにドライバを再起動するバッチです。

taskkill /f /im Wacom_TabletUser.exe
taskkill /f /im Wacom_Tablet.exe

rem sc stop "TabletServiceWacom" 
rem sc start "TabletServiceWacom" 

net start TabletServiceWacom

pause
