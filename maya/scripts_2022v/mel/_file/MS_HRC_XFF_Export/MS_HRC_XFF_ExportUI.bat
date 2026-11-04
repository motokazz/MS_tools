
rem 下記MS_melの部分を書き換えると、その名前で、フォルダ内の.melファイルをまとめます。
set xxx=MS_HRC_XFF_ExportUI.mel

echo off> MSMELWORK

del %xxx%

type .\*.txt >> MSMELWORK

type .\*.mel >> MSMELWORK

ren MSMELWORK %xxx%

copy %xxx% "../"
copy %xxx% "../../"

set xxx=

pause