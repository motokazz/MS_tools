
@echo off
echo =======================================================
echo フルパスリスト作成バッチ（サブディレクトリ込み）
echo   １・ディレクトリをドラッグアンドドロップ
echo   ２・検索したい拡張子を入力
echo　=======================================================
echo;

IF "%1"=="" goto END

set /p XXX="拡張子をピリオド無しで入力（入力無しで全部検索） > "
set FX=%XXX%
IF "%XXX%"=="" set XXX=*

dir /b /a:-d /s /o:d %1\*.%XXX% > "%~dp0%FX%ファイルのフルパスリスト.txt"


echo;
echo;
echo;
echo [ %~dp0%FX%ファイルのフルパスリスト.txt ]を作成しました。
echo;
echo;
echo;



:END
pause


