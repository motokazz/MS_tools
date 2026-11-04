
@echo off

set FILE="D:\Projects\Gravite2\planning\datasheets\Placements.xlsx"
set EVS="D:\Projects\Gravite2\target\common\script\datasheets.evs"
set DEBDEF="D:\Projects\Gravite2\target\common\script\bg\debrisDefinition.evd"

echo;
echo --- Placements.xlsx ---
p4 opened -a %FILE%
echo;
echo;

echo --- datasheets.evs ---
p4 opened -a %EVS%
echo;
echo;

echo --- debrisDefinition.evd ---
p4 opened -a %DEBDEF%
echo;
echo;

pause
