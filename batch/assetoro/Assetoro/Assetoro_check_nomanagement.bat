

rem 変換したい文字列をセット
set before=%1

rem リネーム処理
set file1=%before:D:\MProject\=%
set filepath=%file1:\=/%


set INFO=\\fs03\js-sd\M_PROJECT\toro_tools\AssetoroCmd -i %filepath%
for %%a in %INFO% 
if "ServerVersion:3" in %INFO% (call:SUB %1)


:SUB
no repositry
echo %1



pause
