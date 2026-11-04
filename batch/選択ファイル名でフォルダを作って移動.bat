@echo on
rem 選択ファイル名でフォルダを作って移動

set asdfqwer=%~dp1%~n1

echo %asdfqwer%

mkdir %asdfqwer%

for %%a in (%*) do (call :CP %%a)

exit

:CP
move %1 %asdfqwer%\%~nx1
exit /b
