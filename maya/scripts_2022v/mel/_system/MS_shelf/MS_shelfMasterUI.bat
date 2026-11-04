echo off> MSMELWORK

set xxx=MS_shelfMasterUI.mel

del %xxx%

type .\*.mel >> MSMELWORK

ren MSMELWORK %xxx%

rem copy %xxx% "C:\Documents and Settings\s002000\My Documents\maya\7.0\scripts\"

copy %xxx% "../"

set xxx=

pause