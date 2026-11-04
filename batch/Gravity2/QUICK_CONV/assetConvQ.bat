@echo off
setlocal

pushd "%GRAVITE2_ROOT_DIR%"

"build\imogen\bin\Imogen.exe" build assets\assets.targets win32s --jar=build\imogen\bin --ignoreFail --processPriority=lower
if not "%errorlevel%"=="0" goto ERROR_END

goto SUCCESS_END

:ERROR_END
pause

:SUCCESS_END
popd
endlocal
