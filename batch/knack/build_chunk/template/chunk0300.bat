@echo off
setlocal
set output_dir=D:\Mproject\mdata\character\player\0300
set charaproj_dir=%output_dir%

set callee_path=D:\Mproject\gtools\batch\build_chunk\create_bone_and_chara_output.bat
set input_path=%~dpn0.toro
set output_path=%output_dir%\%~n0.toro
set charaproj_path=%charaproj_dir%\%~n0_000.charaproj

call %callee_path% %input_path% %output_path% %charaproj_path%

pause
