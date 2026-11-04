echo off> MSMELWORK

set xxx=MS_trailUI.mel

del %xxx%

type "..\..\__LIB\MS_selectTime.mel" >> MSMELWORK
type "..\..\__LIB\MS_setEmitter.mel" >> MSMELWORK
type "..\..\__LIB\MS_constraint.mel" >> MSMELWORK

type .\*.mel >> MSMELWORK

ren MSMELWORK %xxx%

copy %xxx% "..\..\"
copy %xxx% "..\"

set xxx=

pause