:encode
if .%1==. GOTO end
if /I %~x1 == .avi (
	D:/Mproject/graphic/post/tool/ffmpeg/ffmpeg.exe -y -i %1 -vcodec msmpeg4v2 -r 30 -s 1920x1080 -threads 0 -b:v 4096k -qscale 5 %~n1_cnv.avi
	D:/Mproject/graphic/post/tool/ffmpeg/ffmpeg.exe -y -i %~n1_cnv.avi -vcodec libx264 -r 30 -s 1920x1080 -ar 48000 -acodec pcm_s24le -ac 2 %~n1_cnv.mov
	DEL %~n1_cnv.avi
)

if /I %~x1 == .mov (
	D:/Mproject/graphic/post/tool/ffmpeg/ffmpeg.exe -y -i %1 -vcodec libx264 -threads 0 -b:v 4096k -r 30 -s 1920x1080 -qscale 5 -ar 48000 -acodec pcm_s24le -ac 2 %~n1_cnv.mov
)

SHIFT
GOTO encode

:end





