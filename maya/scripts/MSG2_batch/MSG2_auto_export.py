# _*_coding:utf-8_*_
########################################
# ファイル名
#			g2export.py
# 説明
#			
#			
# 作成日
#			
########################################


import maya.cmds as cmds
import gravite_cmd
import sys
import shutil

import s2000_tools.MS_lib.MSG2_P4Lib as MSG2_P4Lib
reload(MSG2_P4Lib)

#
SYS_PATH = r'D:\\Projects\\Gravite2\\tools\\\GravitePythonLibs\\maya'
if not SYS_PATH in sys.path:
	sys.path.append(SYS_PATH)

#
ATGI_NAME_LIST=['']

MB_ROOT_PATH = 'D:/Projects/Gravite2/graphic/bg/scenes'

#PATH DEFINE
ATGI_ASSET_PATH = 'D:/Projects/Gravite2/assets/bg/model'
HKX_ASSET_PATH = 'D:/Projects/Gravite2/assets/bg/collision'
TIF_ASSET_PATH = 'D:/Projects/Gravite2/assets/common/texture'

ASSET_LOCAL_PATH = 'D:/Projects/Gravite2/assets_local'
ATGI_ASSET_LOCAL_PATH = '/bg/model'
HKX_ASSET_LOCAL_PATH = '/bg/collision'
TIF_ASSET_LOCAL_PATH = '/common/texture'


#正規データとしてAssetフォルダにコピーする
def copyLocalToAsset(SRC,DST):
	LOG=[]
	LOG.append(DST)
	MSG2_P4Lib.ENABLE_DIALOG=False
	MSG2_P4Lib.P4CheckOut([DST],ENABLE_DIALOG=False)
	LOG.append(SRC+' COPY---> '+DST)

	try:
		shutil.copy(SRC,DST)
		LOG.append('COPY SUCCESS! : '+DST)
	except:
		LOG.append('ERROR! : COPY Failure! : '+DST)
	#
	if not MSG2_P4Lib.P4headRev(DST):
		if MSG2_P4Lib.P4AddMarking(DST):
			LOG.append('ADD SUCCESS!'+DST+'\n')
		else:
			LOG.append('ADD FAILURE!'+DST+'\n')

	return LOG

def  copyREG(ATGI_NAME,FILENAME):
	LOG=[]
	#################
	#正規フォルダにコピー
	#################
	#copy_Assets_Local_To_Assets
	
	#atgi
	ATGI_LOCAL_PATH = ASSET_LOCAL_PATH+'/'+ATGI_NAME+ATGI_ASSET_LOCAL_PATH+'/'+FILENAME+'.atgi'
	ATGI_PATH=ATGI_ASSET_PATH+'/'+FILENAME+'.atgi'
	LOG.extend(copyLocalToAsset(ATGI_LOCAL_PATH,ATGI_PATH))

	#collision
	HKX_LOCAL_PATH=ASSET_LOCAL_PATH+'/'+ATGI_NAME+HKX_ASSET_LOCAL_PATH+'/'+FILENAME+'.hkx'
	HKX_PATH=HKX_ASSET_PATH+'/'+FILENAME+'.hkx'
	LOG.extend(copyLocalToAsset(HKX_LOCAL_PATH,HKX_PATH))
	
	return '\n'.join(LOG)

def auto():
	TARGET_NAME=cmds.file(q=True,sn=True).split('/')[-1].strip('.mb')
	main(TARGET_NAME)

def main(TARGET_NAME):

	print 'g2export'
	LOG=''

	#オリジナルルート関連リネーム
	ORGRT=''
	ORGCL=''

	CHECK=False

	if cmds.objExists('|root'):
		gravite_cmd.do_export(export_template='bg',export_target='model',EXPORT_NAME=TARGET_NAME)
		ORGRT=cmds.rename('|root','|MS_org_root')
		CHECK=True

	if cmds.objExists('|col'):
		gravite_cmd.do_export(export_template='bg',export_target='collision',EXPORT_NAME=TARGET_NAME)
		ORGCL=cmds.rename('|col','|MS_org_col')
		CHECK=True

	if CHECK:
		LOG+= copyREG(TARGET_NAME,TARGET_NAME)


	NODES=cmds.ls(['top_db','top_bk','top_dy','top_md*'],l=True)

	#壊れ物設定名処理
	RT=cmds.ls('root',l=True)
	i=0
	for each in RT:
		cmds.rename(each,'MS_root'+str(i))
		i+=1

	RT=cmds.ls('col',l=True)
	i=0
	for each in RT:
		cmds.rename(each,'MS_col'+str(i))
		i+=1

	for each in NODES:
		CHILDS=cmds.listRelatives(each,c=True,f=True)
		EXNAME=cmds.getAttr(CHILDS[0]+'.export_name')

		#子供を親に出す
		TEMP=cmds.parent(CHILDS,w=True)
		for eachTEMP in TEMP:
			if 'root' in eachTEMP:cmds.rename(eachTEMP,'root')
			if 'col' in eachTEMP:cmds.rename(eachTEMP,'col')
	
		#
		if cmds.objExists('|root'):
			gravite_cmd.do_export(export_template='bg_brk',export_target='model',EXPORT_NAME=EXNAME)
			REN=cmds.rename('|root','|MS_root')
			cmds.parent(REN,each)
			
			
		if cmds.objExists('|col'):
			gravite_cmd.do_export(export_template='bg_brk',export_target='collision',EXPORT_NAME=EXNAME)
			REN=cmds.rename('|col','|MS_col')
			cmds.parent(REN,each)

		LOG+= copyREG(TARGET_NAME,EXNAME)
							
	RT=cmds.ls('MS_root*',l=True)
	for each in RT:
		cmds.rename(each,'root')
	CL=cmds.ls('MS_col*',l=True)
	for each in CL:
		cmds.rename(each,'col')
	
	#オリジナルルート関連を元に戻す
	if cmds.objExists('|MS_org_root'):
		ORGRT=cmds.rename('|MS_org_root','|root')
	if cmds.objExists('|MS_org_col'):
		ORGCL=cmds.rename('|MS_org_col','|col')


	return LOG




