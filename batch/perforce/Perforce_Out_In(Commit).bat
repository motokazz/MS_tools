echo Perforceコミット（チェックアウト＆イン）
@echo off
for %%a in (%*) do (call :OUTIN %%a)
pause
exit


:OUTIN
echo チェックアウト

p4 lock %1
p4 edit -c default %1

echo チェックイン

p4 sync %1
p4 unlock %1
p4 submit -f submitunchanged -d "バッチからサブミット" %1

exit /b


