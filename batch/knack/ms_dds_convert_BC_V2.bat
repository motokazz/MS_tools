
rem ddsconvert.exe フルパスファイル名 -o 出力先フォルダ

rem -c BC6、BC7に変換するためのオプション
rem -win32 コマンドプロンプトに出力させるオプション　
rem コンバート規則は　D:\MProject\torotool_config\texconvrule.csv

set TEMP_PATH=D:\Mproject\graphic\
set OUTPUT_PATH=D:\Mproject\mgamedata\models\edit\bg\texture\

for %%a in (%*) do (
call :conv %%a
)
pause
exit

:conv
"D:\MProject\GTools\bin\tiff_to_dds.exe" -in %1 -out %TEMP_PATH%%~n1.dds -target RGBA

set FILE_NAME=%~n1
if "%FILE_NAME:~-2,2%"=="_c" (call :DXT1 %1) else (call :BCX %1)

del %TEMP_PATH%%~n1.dds
exit/b


:DXT1
echo DXT1
"D:\MProject\GTools\bin\texconvex2.exe" %TEMP_PATH%%~n1.dds -f BC1_UNORM -ft dds -o %OUTPUT_PATH%
rem "D:\MProject\GTools\bin\ddsconvert.exe" %TEMP_PATH%%~n1.dds -o %OUTPUT_PATH%
exit/b


:BCX
echo BCX
"D:\MProject\GTools\bin\ddsconvert.exe" %TEMP_PATH%%~n1.dds -c -o %OUTPUT_PATH%
exit/b