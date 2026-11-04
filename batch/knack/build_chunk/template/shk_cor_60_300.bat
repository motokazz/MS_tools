@echo off
setlocal
set output_dir=D:\Mproject\mgamedata\models\character\player\cor

set callee_path=D:\Mproject\gtools\batch\build_chunk\make_shrink_model.bat
set input_path=%~dpn0.toro
set output_path=%output_dir%\%~n0.toro

call %callee_path% %input_path% %output_path%

pause
