# _*_coding:utf-8_*_
########################################
# ファイル名
#			checkAtgiExists.py
# 説明
#			MBファイルに対応したAtgiがあるかどうか調べる
#			
# 作成日
#			
########################################

import os

def main(FILEPATH,*args,**kwargs):
	ATGI_PATH = 'D:/Projects/Gravite2/assets/bg/model/'
	FILEPATH=FILEPATH.replace('\\','/')
	FILENAME=FILEPATH.split('/')[-1]
	EX=os.path.exists(ATGI_PATH+FILENAME+'.atgi')

	return FILEPATH+','+str(EX)







