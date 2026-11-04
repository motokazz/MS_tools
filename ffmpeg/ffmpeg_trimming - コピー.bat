
"D:\freeware\ffmpeg\bin\ffmpeg.exe" -i "%1" -filter:v "minterpolate='mi_mode=mci:mc_mode=aobmc:vsbmc=1:fps=60'" -c:v libx264 -crf 20 "%~n1_output.mp4"
pause

