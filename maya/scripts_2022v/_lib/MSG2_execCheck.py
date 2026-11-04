# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_execCheck.py
# 説明
#			起動確認リスト作成
#使用方法
#下記コマンドを各スクリプトの先頭に記述
'''
#execCheckList
import s2000_tools.MS_lib.MSG2_execCheck as MSG2_execCheck
reload(MSG2_execCheck)
MSG2_execCheck.execCheckSafe('scriptName')#execCheckList

'''
#			
########################################

import os
import datetime

EXPORT_DIR='//Fs03/gravity2$/users/sakai/scriptCheckList'

def SAVE(ROW,FILE_PATH):
	f=open(FILE_PATH,'w')#'r'読み込み：'w'書き込み：'a'追記：'+'読み書き両方' 't'テキストモード：'b'バイナリーモード
	f.write(ROW)
	f.close()
	return True
	
##### ファイルロード #####
def LOAD(FILE_PATH):
	DATA=[]
	if not os.path.exists(FILE_PATH):
		return DATA#空のリストを返す
	try:
		f=open(FILE_PATH)
		for ROW in f:
			DATA.append(ROW)
		f.close()
		return DATA
	except:
		return DATA


def execCheckSafe(scriptName):
	#エラーで止まらないセーフモード。
	try:
		execCheckList(scriptName)
	except:
		print 'warnning:MS_execCheck error'

def execCheckList(scriptName,exportDir=EXPORT_DIR):
	#初回起動確認
	FIRSTCHECK=True
	
	#ファイル名
	FILENAME='checkList_'+scriptName+'.csv'
	FILEPATH=exportDir+'/'+FILENAME
	
	#ユーザー名取得
	USERNAME=os.environ.get('USERNAME')
	
	if USERNAME=='0300002000':#自分排除
		return False
	
	#起動日時
	TIME=str(datetime.datetime.now())
	REPLACELIST=[[' ','_'],['-','/']]
	for EACH in REPLACELIST:
		TIME=TIME.replace(EACH[0],EACH[1])
	#起動回数初期設定
	QUANTITY=''
	#
	if os.path.isdir(exportDir):
		NEWDATA=''
		NEWDATA2=[]
		DATA=LOAD(FILEPATH)
		for EACHDATA in DATA:
			DATA2=EACHDATA.replace('/n','').split(',')
			#print DATA2
			if DATA2[0]=='':
				continue
			if USERNAME in DATA2[0]:
				#起動回数
				#print DATA2[2]
				try:
					PREQ=int(DATA2[2])+1
				except:
					PREQ=1
				QUANTITY=str(PREQ)
				FIRSTCHECK=False
				NEWDATA+=DATA2[0]+','+TIME+','+QUANTITY+',\n'
			else:
				NEWDATA+=EACHDATA
			
		if FIRSTCHECK:
			NEWDATA2=[USERNAME,TIME,'1']
			NEWDATA+=(','.join(NEWDATA2)+'\n')
		
		SAVE(NEWDATA,FILEPATH)
		
		
	else:
		#print 'not found directry = '+EXPORT_DIR
		return False
		
		
	
