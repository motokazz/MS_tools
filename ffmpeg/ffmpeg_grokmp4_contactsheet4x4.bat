
"D:\freeware\ffmpeg\bin\ffmpeg.exe" -i "%1" -vf "crop=320:320" output.mp4
"D:\freeware\ffmpeg\bin\ffmpeg.exe" -i output.mp4 -vf "select='not(mod(n,9))',scale=320:-1,tile=4x4" -frames:v 1 output.png

pause

