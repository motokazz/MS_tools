# -*- coding: sjis -*-
"""
convertPNG2Mov
"""

import os
import re
import sys
import subprocess 
import dircache


def convert2Mov(inputFile, firstNum):
    fourDigit = inputFile.split('_')[-1]
    targetName = inputFile.replace(fourDigit, '%4d.png')
    outputName = inputFile.replace('_' + fourDigit, '.mov')
    conv = subprocess.Popen(r'D:/Mproject/graphic/post/tool/ffmpeg/ffmpeg.exe -start_number %s -i %s -pix_fmt yuv420p -r 30 -s 1280x720 %s' % (firstNum, targetName, outputName))
    conv.wait()    


movDir = raw_input('D&D folder plz... >> ')
allFiles = dircache.listdir(movDir)
for oneFile in allFiles:
    if re.match('.*.[png|PNG]', oneFile):
        print 'PNGファイルが見つかりました。\nコンバートします。'
        firstNum = (oneFile.split('_')[-1]).split('.')[0]
        convert2Mov(str(movDir) + '\\' +  str(oneFile), firstNum)
        raw_input('コンバートを終了します。')
        sys.exit()

raw_input('>>')


# -pass 2 -acodec libfaac -vcodec libx264 -b 384k -vpre
#D:/Mproject/graphic/post/tool/ffmpeg/ffmpeg.exe -y -i Z:\users\iida\tiff_anim/conbo_metar_rend_01.%3d.tif -r 30 -s 720x404 -qscale 5 d:avi2.avi