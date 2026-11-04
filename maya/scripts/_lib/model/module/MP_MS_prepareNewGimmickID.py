# _*_coding:utf-8_*_
########################################
# ファイル名
#			MP_MS_prepareNewGimmickID
# 説明
#			
# 作成日\n#			
########################################

import maya.cmds as cmds
import maya.mel as mel

import os
import shutil
import glob
import codecs

import MS_CSVImportDict
reload (MS_CSVImportDict)
	
##### ファイルセーブ #####
def SAVE(ROW,FILE_PATH):
	f=open(FILE_PATH,'w')#'r'読み込み：'w'書き込み：'a'追記：'+'読み書き両方' 't'テキストモード：'b'バイナリーモード
	f.write(ROW)
	f.close()
	
##### ファイルロード #####
def LOAD(FILE_PATH):
	f=codecs.open(FILE_PATH,'r','shift_jis')
	DATA=[]
	for ROW in f:
		DATA.append(ROW)
	f.close()
	return DATA
	
def do():
	print 'do'
	srcID=cmds.textField('MP_MS_prepareNewGimmickID_srcID',q=True,tx=True)
	srcList=ditectGimmickPathFromID(srcID)
	
	dstID=cmds.textField('MP_MS_prepareNewGimmickID_dstID',q=True,tx=True)
	name=cmds.textField('MP_MS_prepareNewGimmickID_name',q=True,tx=True)
	dstList=createGimmickPathFromID(dstID,name)
	
	MODMB=dstList[1]+dstList[0]+'_model.mb'
	MOTMB=dstList[1]+dstList[0]+'_motion.mb'
	
	
	#MB
	if not os.path.exists(dstList[1]):
		os.makedirs(dstList[1])
	shutil.copyfile(srcList[1]+srcList[0]+'_model.mb',MODMB)
	shutil.copyfile(srcList[1]+srcList[0]+'_motion.mb',MOTMB)
	
	#MDATA
	
	SRC_CHARA_PROJECT=srcList[2]+srcList[0]+'.csv'
	DST_CHARA_PROJECT=dstList[2]+dstList[0]+'.csv'
	
	
	#modifyCharaProject
	if os.path.exists(SRC_CHARA_PROJECT):
		ROW=LOAD(SRC_CHARA_PROJECT)
		#FINAL_TORO_PATH=DICT['#export'][0][0].replace('\\','/')
		#
		data=''
		for each in ROW:
			temp_a=each.replace(srcList[0],dstList[0])
			temp_b=temp_a.replace(srcList[0][5:],dstList[0][5:])
			data+=temp_b
		
		if not os.path.exists(dstList[2]):
			os.makedirs(dstList[2])
		SAVE(data,DST_CHARA_PROJECT)
		
	#copytoro
	shutil.copyfile(srcList[2]+srcList[0]+'_model.toro',dstList[2]+dstList[0]+'_model.toro')
	shutil.copyfile(srcList[2]+srcList[0]+'_motion.toro',dstList[2]+dstList[0]+'_motion.toro')
		
		
		
	#copyEvents
	files=glob.glob(srcList[2]+'event*.csv')
	for each in files:
		shutil.copy(each,dstList[2])
	
	#modify reference
	mel.eval('file -f -options "v=0"  -ignoreVersion  -typ "mayaBinary" -o "%s";addRecentFile("%s", "mayaBinary");'%(MOTMB,MOTMB))
	mel.eval('file -loadReference "refRN" -type "mayaBinary" -options "v=0" "%s";'%MODMB)
	mel.eval('file -force -save -options "v=0";')
	
	
	'''
	#modify gimmick.csv
	gimmick_csv_path='D:/Mproject/mgamedata/db/gimmick.csv'
	gimmick_csv_temp_path='D:/Mproject/mgamedata/db/gimmick_temp.csv'
	ROW=LOAD(gimmick_csv_path)
	data=''
	buf=''
	inserted=False
	for each in  ROW:
		print each
		if srcID in each:
			buf=each
		if each[0:4]==dstID:
			inserted=True
		
		try:
			LID=int(each[0:4])
		except:
			LID=0
		
		if LID>int(dstID) and not inserted:
			
			buflist=buf.split(',')
			buflist[0]=dstID
			buflist[1]='newGimmick'
			buflist[2]=dstList[0][5:]
			data+=','.join(buflist)
			inserted=True
		data+=each
	SAVE(data,gimmick_csv_temp_path)
	'''
	
	
	
	
	
	
	
	
	
	
	
##### ギミックIDからパス検索
	
def ditectGimmickPathFromID(ID=0):
	
	ID_FOLDER=str(ID)[0:2]+'00/'
	
	#MBAPTH
	GIMMICK_MB_PATH='D:/Mproject/graphic/fg/character/gimmick/'
	MB_ID_PATH=GIMMICK_MB_PATH+ID_FOLDER
	MBLIST = os.listdir(MB_ID_PATH)
	GIMMICK_NAME=''
	for EACH in MBLIST:
		if str(ID) in EACH:
			GIMMICK_NAME=EACH
			break
			
	if not GIMMICK_NAME:
		MB_GIMMICK_PATH='nothing'
	else:
		MB_GIMMICK_PATH=MB_ID_PATH+GIMMICK_NAME+'/'
	
	#TOROPATH
	GIMMICK_TORO_PATH='D:/Mproject/mdata/character/gimmick/'
	TORO_ID_PATH=GIMMICK_TORO_PATH+ID_FOLDER
	TORO_GIMMICK_PATH=TORO_ID_PATH+GIMMICK_NAME+'/'
	
	if not os.path.exists(TORO_GIMMICK_PATH):
		TORO_GIMMICK_PATH='nothing'
	
	
	#finalToroFile
	CHARA_PROJECT=TORO_GIMMICK_PATH+GIMMICK_NAME+'.csv'
	if os.path.exists(CHARA_PROJECT):
		DICT=MS_CSVImportDict.indexColumn(CHARA_PROJECT)
		FINAL_TORO_PATH=DICT['#export'][0][0].replace('\\','/')
		if os.path.exists(FINAL_TORO_PATH):
			FINAL_TORO_PATH=FINAL_TORO_PATH.lower()
			FINAL_TORO_PATH=FINAL_TORO_PATH.replace('d:/mproject','D:/Mproject')
		else:
			FINAL_TORO_PATH='nothing'
			
	#gimmickPathList
	LIST=[]
	LIST.append('%s' % GIMMICK_NAME)
	LIST.append('%s' % MB_GIMMICK_PATH)
	LIST.append('%s'  % TORO_GIMMICK_PATH)
	LIST.append('%s'  % FINAL_TORO_PATH)
	
	print LIST
	return LIST

def createGimmickPathFromID(ID=0,FINAL_NAME=''):
	
	ID_FOLDER=str(ID)[0:2]+'00/'
	
	#GIMMICK_NAME
	GIMMICK_NAME=ID+'_'+FINAL_NAME
	
	#MBAPTH
	GIMMICK_MB_PATH='D:/Mproject/graphic/fg/character/gimmick/'
	MB_ID_PATH=GIMMICK_MB_PATH+ID_FOLDER
	
	if not GIMMICK_NAME:
		MB_GIMMICK_PATH='nothing'
	else:
		MB_GIMMICK_PATH=MB_ID_PATH+GIMMICK_NAME+'/'
	
	#TOROPATH
	GIMMICK_TORO_PATH='D:/Mproject/mdata/character/gimmick/'
	TORO_ID_PATH=GIMMICK_TORO_PATH+ID_FOLDER
	TORO_GIMMICK_PATH=TORO_ID_PATH+GIMMICK_NAME+'/'
	
	#CHARA_PROJECT
	
	CHARA_PROJECT=TORO_GIMMICK_PATH+GIMMICK_NAME+'.csv'
	
	#finalToroFile
	REL_PATH='models/character/gimmick/'
	FINAL_TORO_PATH='d:/Mproject/mgamedata/'+REL_PATH+GIMMICK_NAME+'.toro'
	
	#gimmickPathList
	LIST=[]
	LIST.append('%s' % GIMMICK_NAME)
	LIST.append('%s' % MB_GIMMICK_PATH)
	LIST.append('%s' % TORO_GIMMICK_PATH)
	LIST.append('%s' % FINAL_TORO_PATH)
	
	print LIST
	return LIST
	
def layoutA(
	LABEL='MP_MS_prepareNewGimmickID'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	
	cmds.text(l=LABEL)
	cmds.textField('MP_MS_prepareNewGimmickID_srcID',w=WIDTH-4,tx='9252')
	cmds.textField('MP_MS_prepareNewGimmickID_dstID',w=WIDTH-4,tx='9254')
	cmds.textField('MP_MS_prepareNewGimmickID_name',w=WIDTH-4,tx='st09_a_secretdoor1')
	
	
	cmds.button(w=WIDTH-4,l=u'do',c=lambda *args:do())
	
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MP_MS_prepareNewGimmickID_main_window',q=True,ex=True):
		cmds.deleteUI('MP_MS_prepareNewGimmickID_main_window')
	cmds.window('MP_MS_prepareNewGimmickID_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MP_MS_prepareNewGimmickID_main_window')
	

