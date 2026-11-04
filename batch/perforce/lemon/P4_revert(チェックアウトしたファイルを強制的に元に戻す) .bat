@echo off
echo チェックアウトしたファイルを強制的に元に戻す。

for %%a in (%*) do (call :REVERT %%a)

pause
exit

:REVERT
p4 revert -k %1/...
p4 revert -k %1

exit /b



