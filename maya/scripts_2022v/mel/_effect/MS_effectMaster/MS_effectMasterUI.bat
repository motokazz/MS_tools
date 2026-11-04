rem 下記MS_melの部分を書き換えると、その名前で、フォルダ内の.melファイルをまとめます。
set xxx=MS_effectMasterUI.mel

echo off> MSMELWORK

del %xxx%
rem type "C:\Documents and Settings\s002000\デスクトップ\My_mel\__LIB\MS_cgfxMount.mel" >> MSMELWORK
type "C:\Documents and Settings\s002000\デスクトップ\My_mel\__LIB\MS_selectTime.mel" >> MSMELWORK
type "C:\Documents and Settings\s002000\デスクトップ\My_mel\__LIB\MS_duplicateFace.mel" >> MSMELWORK
type "C:\Documents and Settings\s002000\デスクトップ\My_mel\__LIB\MS_constraint.mel" >> MSMELWORK
type "C:\Documents and Settings\s002000\デスクトップ\My_mel\__LIB\MS_ditectCenter.mel" >> MSMELWORK

type .\*.mel >> MSMELWORK

ren MSMELWORK %xxx%

copy %xxx% "C:\Documents and Settings\s002000\My Documents\maya\7.0\scripts\"
copy %xxx% "../"

set xxx=

pause