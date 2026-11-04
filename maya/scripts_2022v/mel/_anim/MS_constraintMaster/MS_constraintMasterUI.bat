echo off> MSMELWORK

set xxx=MS_constraintMasterUI.mel

del %xxx%

type "..\..\__LIB\MS_distance.mel">> MSMELWORK
type "..\..\__LIB\MS_spaceLocatorBySceneName.mel">> MSMELWORK

type .\*.mel >> MSMELWORK

ren MSMELWORK %xxx%
echo on

copy %xxx% "..\..\"

set xxx=

pause