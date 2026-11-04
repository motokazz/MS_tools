echo ファイル名から日本語取り去ってコピー

for %%a in (%*) do (call :CPNOJP %%a)

exit


:CPNOJP
copy "%1" "%~dpn1_org%~x1"
exit /b




