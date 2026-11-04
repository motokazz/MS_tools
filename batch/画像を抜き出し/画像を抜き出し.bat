
c:
cd %~dp0

dir /b /a:-d /s %1\*.png > "%~dp0画像ファイルのフルパスリスト.txt"

dir /b /a:-d /s %1\*.psd >> "%~dp0画像ファイルのフルパスリスト.txt"

dir /b /a:-d /s %1\*.dds >> "%~dp0画像ファイルのフルパスリスト.txt"

dir /b /a:-d /s %1\*.torox >> "%~dp0画像ファイルのフルパスリスト.txt"

dir /b /a:-d /s %1\*.tm2 >> "%~dp0画像ファイルのフルパスリスト.txt"

dir /b /a:-d /s %1\*.bmp >> "%~dp0画像ファイルのフルパスリスト.txt"

dir /b /a:-d /s %1\*.tga >> "%~dp0画像ファイルのフルパスリスト.txt"

dir /b /a:-d /s %1\*.tif >> "%~dp0画像ファイルのフルパスリスト.txt"

dir /b /a:-d /s %1\*.iff >> "%~dp0画像ファイルのフルパスリスト.txt"

dir /b /a:-d /s %1\*.eps >> "%~dp0画像ファイルのフルパスリスト.txt"

dir /b /a:-d /s %1\*.eps >> "%~dp0画像ファイルのフルパスリスト.txt"


copy 画像ファイルのフルパスリスト.txt full_path_list.bat


mfind  /w "/C:/copy \"C:/" full_path_list.bat

mfind  /w "/D:/copy \"D:/" full_path_list.bat

mfind  /w "/\\\\Fs03/copy \"\\\\Fs03/" full_path_list.bat

mfind  /w "/.dds/.dds\"/" full_path_list.bat

mfind  /w "/.png/.png\"/" full_path_list.bat

mfind  /w "/.psd/.psd\"/" full_path_list.bat

mfind  /w "/.torox/.torox\"/" full_path_list.bat

mfind  /w "/.tm2/.tm2\"/" full_path_list.bat

mfind  /w "/.bmp/.bmp\"/" full_path_list.bat

mfind  /w "/.tga/.tga\"/" full_path_list.bat

mfind  /w "/.tif/.tif\"/" full_path_list.bat

mfind  /w "/.iff/.iff\"/" full_path_list.bat

mfind  /w "/.eps/.eps\"/" full_path_list.bat

call full_path_list.bat

del full_path_list.bat

