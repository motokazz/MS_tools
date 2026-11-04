@echo on
echo filename >filelist.csv
rem 選択ファイル名リスト作成

for %%a in (%*) do (call :CP %%a)

exit

:CP
echo %~n1>>filelist.csv
exit /b
