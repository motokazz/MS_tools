@echo off
setlocal

rem ############################
rem 使用するするカスタムエリアディフィニション
rem ############################
set CUSTOM_AREA_DIFINITION=%1


set BACK= "%~dp0TEMP\areaDefinition.evd.bak"
rem set TEMP="D:\MS_tools\batch\Gravity2\QUICK_CONV\TEMP\"
set TEMP="%~dp0TEMP\"

set AREA_DEFINITION="D:\Projects\Gravite2\target\common\script\area\areaDefinition.evd"
set SCRIPT_AREA="D:\Projects\Gravite2\target\common\script\area\"

rem オリジナルコピー　ドラッグしたやつもコピー

copy %AREA_DEFINITION% %BACK%
attrib -R %AREA_DEFINITION%
copy %CUSTOM_AREA_DIFINITION% %AREA_DEFINITION%

rem evb複製

copy %SCRIPT_AREA%*.evb %TEMP%

rem ###############################################################################################

pushd "%GRAVITE2_ROOT_DIR%"

rem "build\imogen\bin\Imogen.exe" build assets\assets.targets win32s --jar=build\imogen\bin --ignoreFail --processPriority=lower
rem if not "%errorlevel%"=="0" goto ERROR_END

call "tools\GraviteAreaGenerator\GraviteAreaGenerator.bat"

rem ###############################################################################################

rem オリジナルを元に戻す

copy %BACK% %AREA_DEFINITION%

attrib -R %AREA_DEFINITION%

xcopy /C /D /Y %TEMP%*.evb %SCRIPT_AREA%

del %BACK%

del %TEMP%*.evb

goto SUCCESS_END

:ERROR_END
pause

:SUCCESS_END
popd
endlocal
