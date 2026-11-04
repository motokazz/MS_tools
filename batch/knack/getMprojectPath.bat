
@echo off

echo ///////////////////////////////////////////////////////////////
echo // ファイル名
echo //			getMprojectPath.bat
echo // 説明
echo //			MP_MS_getREG.exeを利用したレジストリ取得のサンプル
echo // 作成日
echo //			2012/07/26	坂井元一
echo ///////////////////////////////////////////////////////////////


rem ####################################################
rem for /f "usebackq"を使わないといけない。
rem ####################################################

for /f "usebackq" %%A in (`D:\MProject\GTools\bin\MP_MS_getREG.exe`) do ( set MPROJECT_PATH=%%A)

echo MPROJECT_PATH = %MPROJECT_PATH%



pause
