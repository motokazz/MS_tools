

rem 変換したい文字列をセット
set before=%1

rem リネーム処理
set file1=%before:D:\MProject\=%
set filepath=%file1:\=/%


\\fs03\js-sd\M_PROJECT\toro_tools\AssetoroCmd -i %filepath%


pause
