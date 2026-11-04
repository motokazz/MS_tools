@echo off
echo 自分が開いているファイルの確認

rem p4  -p ssl:54.250.7.52:1666 -u motokazu.sakai opened
rem p4  -p ssl:54.250.7.52:1666 -u motokazu.sakai opened -a //Lemon/Master/ProjectSettings/*.*
p4  -u motokazu.sakai opened -a //Lemon/Master/ProjectSettings/*.*
pause
exit


