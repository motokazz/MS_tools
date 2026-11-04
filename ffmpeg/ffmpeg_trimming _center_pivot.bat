SET /P SizeX=
SET /P SizeY=

"D:\freeware\ffmpeg\bin\ffmpeg.exe" -i "%1" -vf "crop=%SizeX%:%SizeY%" output.mp4
pause

