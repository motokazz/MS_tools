rem 下記MS_melの部分を書き換えると、その名前で、フォルダ内の.melファイルをまとめます。
set xxx=MS_.mel

echo off> MSMELWORK

del %xxx%

type .\*.txt >> MSMELWORK

type "C:\Documents and Settings\s002000\デスクトップ\My_mel\__LIB\MS_selectTime.mel" >> MSMELWORK
type "C:\Documents and Settings\s002000\デスクトップ\My_mel\__LIB\MS_setEmitter.mel" >> MSMELWORK

type .\*.mel >> MSMELWORK

ren MSMELWORK %xxx%

copy %xxx% "C:\Documents and Settings\s002000\My Documents\maya\7.0\scripts\"
copy %xxx% "../"

set xxx=

pause