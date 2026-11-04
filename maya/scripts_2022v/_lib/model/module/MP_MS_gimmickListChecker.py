# _*_coding:utf-8_*_
########################################
# ファイル名
#			MP_MS_gimmickListChecker
# 説明
#			
# 作成日\n#			
########################################

import maya.cmds as cmds
import os
import re
import MS_Lib
reload(MS_Lib)
	
TORO_DIR_PATH='d:/Mproject/mgamedata/models/character/gimmick'

FILE_LIST_PATH='d:/Mproject/mgamedata/db/filelist/122_list_gimmick.csv'

ENTITY_LOCATION_LIST='d:/Mproject/graphic/gimmick/doc/entity_location_list.csv'


EXPORT_PATH='d:/Mproject/graphic/gimmick/doc/list_in_db.csv'
EXPORT_PATH_B='d:/Mproject/graphic/gimmick/doc/list_no_used.csv'
EXPORT_PATH_C='d:/Mproject/graphic/gimmick/doc/list_no_located.csv'
	
def checkVailedFilename(NAME):
	if re.search('^st\d{2}_[a-d]_[a-z0-9]+\.toro$',NAME):#stageID
		return 'OK'
	else:
		return 'NG'
		
		
def locatedObjectsList():
	list_gimmick=MS_Lib.CSV_IMPORT(FILE_LIST_PATH)
	list_no_located=MS_Lib.CSV_IMPORT(ENTITY_LOCATION_LIST)
	
	list=[]
	for x in list_no_located:
		list.append(x[2])
	
	return list
	
def listInDB():
	list=MS_Lib.CSV_IMPORT(FILE_LIST_PATH)
	list_in_db=[]
	for each in list:
		if '.toro' in each[2]:
			list_in_db.append([each[0],each[1],each[2],each[3]])
	return list_in_db
	
def do():
	list_in_db=''
	list_no_located=''
	#
	list_in_db_list=listInDB()
	#
	files=os.listdir(TORO_DIR_PATH)
	#
	list_located=locatedObjectsList()
	
	for each in list_in_db_list:
		filename=each[2].split('/')[-1]
		# list_in_db
		
		list_in_db+=checkVailedFilename(filename)+','+','.join(each)+'\n'
		
		# list_no_used
		try:
			files.remove(filename)
		except:
			continue
		
		# list_no_located
		check=False
		for eachb in list_located:
			if each[1]==eachb:
				check=True
				break
		if not check:
			list_no_located+=','.join(each)+'\n'
		
		
	MS_Lib.SAVE(list_in_db,EXPORT_PATH)
	MS_Lib.SAVE('\n'.join(files),EXPORT_PATH_B)
	MS_Lib.SAVE(list_no_located,EXPORT_PATH_C)
	




def layoutA(
	LABEL='MP_MS_gimmickListChecker'
	,WIDTH=300
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	
	cmds.text(l=LABEL)
	cmds.text(l=u'Mプロのファイルのチェックリスト作成ツール')
	cmds.separator(w=300,h=10)
	cmds.text(l=u'ファイルリストの中にある.toroリスト=>%s'%EXPORT_PATH)
	cmds.text(l=u'未使用.toroリスト=>%s'%EXPORT_PATH_B)
	cmds.text(l=u'未配置.toroリスト=>%s'%EXPORT_PATH_C)
	cmds.separator(w=300,h=10)
	cmds.button(w=WIDTH-4,bgc=[0.6,0.8,0.6],l=u'gimmickListCheck',c=lambda *args:do())
	
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MP_MS_gimmickListChecker_main_window',q=True,ex=True):
		cmds.deleteUI('MP_MS_gimmickListChecker_main_window')
	cmds.window('MP_MS_gimmickListChecker_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MP_MS_gimmickListChecker_main_window')
	

