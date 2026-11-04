
@echo off

set FILE="D:\Projects\Gravite2\planning\datasheets\Placements.xlsx"
set EVS="D:\Projects\Gravite2\target\common\script\datasheets.evs"
set DEBDEF="D:\Projects\Gravite2\target\common\script\bg\debrisDefinition.evd"

rem Perforceチェックアウト

p4 sync -s %FILE%
p4 sync -s %FILE%/...
p4 sync -s %DEBDEF%
p4 sync -s %EVS%

p4 edit -c default %FILE%
p4 edit -c default %FILE%\...
p4 edit -c default %DEBDEF%
p4 edit -c default %EVS%

rem p4 lock %FILE%
rem p4 lock %FILE%\...

"C:\Program Files (x86)\Microsoft Office\Office14\EXCEL.EXE" %FILE%

call "D:\Projects\Gravite2\planning\datasheets\doit.bat"

