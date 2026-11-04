# _*_coding:utf-8_*_
########################################
# ファイル名
#			hkxFixer.py
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

def main(TARGET_NAME):
	LOG=''

	NAME=cmds.file(q=True,sn=True)
	BRK=NAME.replace('.mb','_brk.mb')

	if os.path.exists(BRK):
		return 'path exists : '+BRK

	DIR='D:/work/gravitydaze2_work/brk_org/'

	SFN=NAME.split('/')[-1]
	SFN=SFN.replace('g1_','')

	#読み込み
	ErrorFlag=0
	try:
		cmds.file(DIR+'bk_'+SFN,i=True,type='mayaBinary',ra=True,mergeNamespacesOnClash=True)
	except:
		ErrorFlag+=1
		
	try:
		cmds.file(DIR+'deb_'+SFN,i=True,type='mayaBinary',ra=True,mergeNamespacesOnClash=True)
	except:
		ErrorFlag+=1
		
	try:
		cmds.file(DIR+'at_'+SFN,i=True,type='mayaBinary',ra=True,mergeNamespacesOnClash=True)
	except:
		ErrorFlag+=1

	if ErrorFlag==3:
		return 'not exists all: '+BRK

	#削除
	try:
		cmds.delete('|*_hkx_*')
	except:
		print 'hkx not exists'

	cmds.select('|root',r=True)
	if cmds.objExists('|col'):
		cmds.select('|col',add=True)

	cmds.select('|*_top*',add=True)

	#保存


	cmds.file(BRK,force=True,options="v=0",typ="mayaBinary",de=1,pr=True,es=True,ch=0,chn=0,con=0,exp=0)
	#cmds.file(BRK,o=True,f=True)

	MSG2_P4Lib.P4AddMarking(BRK)


	return LOG

