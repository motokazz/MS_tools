SET /P SizeX=
SET /P SizeY=
SET /P PivotX=
SET /P PivotY=

"D:\freeware\ffmpeg\bin\ffmpeg.exe" -i "%1" -vf "crop=%SizeX%:%SizeY%:%PivotX%:%PivotY%" output.mp4
pause

