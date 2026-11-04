echo off> MSMELWORK

set xxx=MS_VFAUI.mel

del %xxx%

type "..\..\__LIB\MS_selectTime.mel" >> MSMELWORK
type "..\..\__LIB\MS_setEmitter.mel" >> MSMELWORK

type .\*.mel >> MSMELWORK

ren MSMELWORK %xxx%

copy %xxx% "../"
copy %xxx% "../../"

set xxx=

pause