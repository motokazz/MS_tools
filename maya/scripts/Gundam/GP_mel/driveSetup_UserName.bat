ECHO OFF
REM 
REM SetDrive_ForGP_20140403.bat
REM 
REM ネットワークドライブ、ルートドライブの設定
REM 
REM 
SETLOCAL




REM L ドライブ設定
IF EXIST L: (
	SUBST /D L: M:\Design
	)
SUBST M:\Design


ENDLOCAL
pause