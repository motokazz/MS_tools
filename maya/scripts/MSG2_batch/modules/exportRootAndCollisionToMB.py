# _*_coding:utf-8_*_
########################################
# ファイル名
#			exportRootAndCollision.py
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds
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
				print root+'/'+f
				return root+'/'+f
	return ''

def searchAndOpenMB(MBNAME):
	LOG=[]
	#BGMBRoot
	FPATH=searchPath('D:/Projects/Gravite2/graphic/bg/scenes',MBNAME)
	LOG.append(MSG2_P4Lib.P4CheckOut([FPATH]))
	cmds.file(FPATH,o=True,options='v=0',f=True)
	return LOG

def main(TARGET_NAME):
	print 'exportRootAndCollision'
	LOG=[]
	LOG.extend(searchAndOpenMB(TARGET_NAME))
	
	if not cmds.objExists('|root'):
		return
	cmds.select('|root',r=True)

	if cmds.objExists('|col'):
		cmds.select('|col',add=True)
	try:
		FN=cmds.file(q=True,sn=True)
		cmds.file(FN,force=True,options="v=0;",typ="mayaBinary",es=True)
		LOG.append('Success : Export !')
	except:
		LOG.append('Error : Export Failure !')
	#LOG
	return LOG




