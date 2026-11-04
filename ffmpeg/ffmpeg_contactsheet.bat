SET /P TILE_COUNT_X=
SET /P TILE_COUNT_Y=
SET /P FRAME_INTERVAL=


"D:\freeware\ffmpeg\bin\ffmpeg.exe" -i "%1" -vf "select='not(mod(n,%FRAME_INTERVAL%))',scale=320:-1,tile=%TILE_COUNT_X%x%TILE_COUNT_Y%" -frames:v 1 output.png
pause


