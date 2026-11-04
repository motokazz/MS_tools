
echo 画像ファイルのフルパスリスト　> "%~dp0画像ファイルのフルパスリスト.txt"

echo png________ >> "%~dp0画像ファイルのフルパスリスト.txt"
dir /b /a:-d /s %1\*.png >> "%~dp0画像ファイルのフルパスリスト.txt"

echo psd________ >> "%~dp0画像ファイルのフルパスリスト.txt"
dir /b /a:-d /s %1\*.psd >> "%~dp0画像ファイルのフルパスリスト.txt"

echo dds________ >> "%~dp0画像ファイルのフルパスリスト.txt"
dir /b /a:-d /s %1\*.dds >> "%~dp0画像ファイルのフルパスリスト.txt"

echo torox______ >> "%~dp0画像ファイルのフルパスリスト.txt"
dir /b /a:-d /s %1\*.torox >> "%~dp0画像ファイルのフルパスリスト.txt"

echo tim2_______ >> "%~dp0画像ファイルのフルパスリスト.txt"
dir /b /a:-d /s %1\*.tm2 >> "%~dp0画像ファイルのフルパスリスト.txt"

pause


