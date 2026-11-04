
setlocal

set P4="C:\Program Files\Perforce\p4.exe"
echo PerforceでGravity2ディポを全更新します
%P4% sync -s //Gravity2/...
