# _*_coding:utf-8_*_
########################################
# ファイル名
#			checkMBExists.py
# 説明
#			
#			
# 作成日
#			
########################################
import os
import s2000_tools.MS_lib.MSG2_P4Lib as MSG2_P4Lib
reload(MSG2_P4Lib)

def searchPath(SEARCHPATH,searchFile='',searchExt='mb'):
	for (root,dir,files) in os.walk(SEARCHPATH):
		#発見時の処理
		for f in files:
			
			fname=f.split('.')[0]
			if (searchFile+'.'+searchExt) == f:
				root=root.replace('\\','/').replace('//','/')
				return root+'/'+f
	return False

def nameFilter(NAME=''):
	RET=''
	FILTERS=['_low','_occ','_brk_bk','_brk_db','_brk_md01','_brk_md02','_brk_md03','_brk_md04','_brk_md05','_brk_md06','_brk_md07','_brk_md08','_brk_md09','_brk_md10']
	for each in  FILTERS:
		if each in NAME:
			RET=NAME.replace(each,'')
			if '_brk_' in NAME:
				RET+='_brk'
	if RET:
		return RET
	else:
		return NAME




def main(TARGET_NAME):
	P4_STAT=''
	TARGET_NAME=nameFilter(TARGET_NAME)
	#forQuery
	if not TARGET_NAME:return False
	MB_PATH=searchPath('D:/Projects/Gravite2/graphic/bg/scenes',TARGET_NAME)
	if not MB_PATH:
		MB_PATH='FALSE'
	else:
		P4_STAT=MSG2_P4Lib.P4Status(PATH=MB_PATH)
		if not P4_STAT:
			P4_STAT='FALSE'
	return MB_PATH+','+P4_STAT
