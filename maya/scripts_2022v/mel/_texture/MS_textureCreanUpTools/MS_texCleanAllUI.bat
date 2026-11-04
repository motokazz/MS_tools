echo off> MSMELWORK

set xxx=MS_texCleanUI.mel

del %xxx%

type .\*.mel >> MSMELWORK

ren MSMELWORK %xxx%

copy %xxx% "C:\Documents and Settings\s002000\My Documents\maya\7.0\scripts\"
copy %xxx% "../"
set xxx=

pause