:encode
if .%1==. GOTO end
if /I %~x1 == .avi (
	D:/Mproject/graphic/post/tool/ffmpeg/ffmpeg.exe -y -i %1 -vcodec msmpeg4v2 -r 30 -s 720x404 -threads 0 -b:v 2048k -qscale 5 %~n1_cnv.avi
	D:/Mproject/graphic/post/tool/ffmpeg/ffmpeg.exe -y -i %~n1_cnv.avi -vcodec libx264 -r 30 -s 720x404 -threads 0 -b:v 2048k -qscale 5 %~n1_cnv.mp4
	DEL %~n1_cnv.avi
)

if /I %~x1 == .mov (
	D:/Mproject/graphic/post/tool/ffmpeg/ffmpeg.exe -y -i %1 -vcodec libx264 -r 30 -s 720x404 -threads 0 -b:v 2048k -qscale 5 %~n1_cnv.mp4
)

SHIFT
GOTO encode

:end





