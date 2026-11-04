rem 下記MS_melの部分を書き換えると、その名前で、フォルダ内の.melファイルをまとめます。
set xxx=MS_MFCUI.mel

echo off> MSMELWORK

echo on

del %xxx%

type .\*.txt >> MSMELWORK

type "..\..\__LIB\MS_globalScale.mel"  >> MSMELWORK
type "..\..\__LIB\MS_selectTime.mel" >> MSMELWORK

type .\*.mel >> MSMELWORK

ren MSMELWORK %xxx%

copy %xxx% "..\..\"
copy %xxx% "..\"

set xxx=

pause