# -*- coding: sjis -*-
'''
mov info checker
'''
import re
import subprocess 
import os
import time
from stat import *
import math

userhome = os.path.expanduser('~')
DTsub = userhome.replace('Documents','')
DTsub = DTsub.replace('Desktop/','')
csvFile = DTsub +'/Desktop/mov_file_info.csv'
log = ''

#srcDir = "Z:\graphic\igc\mov\Movie\_movie\\"
defDir = (r'D:\Mproject\graphic\igc\cuts\reviewmovie\\')

canOpen = False
while not canOpen:
    try:
        f = open(csvFile, 'wb')
        f.close()
        canOpen = True
    except:
        raw_input('結果出力ファイルが開かれている気がします\n閉じて下さい(hit enter key)')
    
inputDir = ''
while not inputDir:
    inputDir = raw_input('ディレクトリを指定して下さい\n例:D:\Mproject\graphic\igc\cuts\\reviewmovie\n未入力の場合デフォルトディレクトリ(reviewmovie)を調査します\n >> ')
    if inputDir:
        if not os.path.isdir(inputDir):
            print '指定したディレクトリは存在しません'
            inputDir = ''
        else:
            print '調査を開始します\n'
    else:
        print 'デフォルトディレクトリを調査します'
        inputDir = defDir

for (root, dirs, files) in os.walk(inputDir):
    for oneFile in files:
        movPath = os.path.join(root, oneFile)
        if oneFile.split('.')[-1] == 'mov':
            conv = subprocess.Popen(r'D:/Mproject/graphic/post/tool/ffmpeg/ffmpeg.exe -i %s' % movPath, stderr= subprocess.PIPE).communicate()
            #print conv
            
            #継続時間
            durHead = str(conv).split('Duration: ')[-1]
            durTime = durHead.split(', ')[0]
            if not re.match('^[0-9][0-9]', durTime):
                durTimeA = 'no info'
                durFrame = 'no info'
            else:
                hms = durTime.split(':')
                hour = int(hms[0])
                minutes = int(hms[1])
                sec = int(hms[2].split('.')[0])
                msec = int(hms[2].split('.')[1])
                durTimeA = durTime
                durFrame = round(msec*0.3) + sec*30 + minutes*1800 + hour*108000
 
 
            #コーデック
            encHead = str(conv).split('Video: ')[-1]
            encType = encHead.split(' ')[0]
            if encType not in ('h264','dnxhd','rawvideo','mjpeg'):
                encType = 'no info'

            #解像度チェック
            try:
                encSize = encHead.split(',')[2] 
                encSize = encSize.split(' ')[1] 
            except:
                encSize = 'no info'             

            #作成日時  
            timeget = os.stat(movPath)
            time_ctime = time.ctime(timeget[ST_MTIME])
            output_fmt = '%Y/%m/%d %H:%M:%S'
            time_fmt = time.strftime(output_fmt,time.localtime(timeget[ST_MTIME]))

            #movPath
            movPathLink = '"=HYPERLINK(""%s"",""%s"")",'%(movPath, movPath)

            
            #まとめ
            #print oneFile + ',' + durTimeA + ',' + str(durFrame) + ',' + encType + ',' + encSize + ',' + time_fmt + ',' + movPath
            log += oneFile + ',' + durTimeA + ',' + str(durFrame) + ',' + encType + ',' + encSize + ',' + time_fmt + ',' + movPathLink  + '\n'   
            
f = open(csvFile, 'wb')
f.writelines('file name,duration time,duration frame,encode type,resolution,creation date,path\n')
f.writelines(log)
f.close()

print '結果出力 >>', csvFile
raw_input('調査を終了します(hit enter key)')
