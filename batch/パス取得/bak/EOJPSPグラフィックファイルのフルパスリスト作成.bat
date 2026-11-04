
echo 画像ファイルのフルパスリスト　> "%~dp0画像ファイルのフルパスリスト.txt"

echo png________ >> "%~dp0画像ファイルのフルパスリスト.txt"
dir /b /a:-d /s %1\*.toro >> "%~dp0画像ファイルのフルパスリスト.txt"

echo psd________ >> "%~dp0画像ファイルのフルパスリスト.txt"
dir /b /a:-d /s %1\*.kuro >> "%~dp0画像ファイルのフルパスリスト.txt"

pause


