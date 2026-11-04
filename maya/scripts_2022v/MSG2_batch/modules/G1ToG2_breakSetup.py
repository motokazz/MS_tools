# _*_coding:utf-8_*_
########################################
# ファイル名
#			g1setup
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

import s2000_tools.MSG2_breakTools.MSG2_breakModelEditor as MSG2_breakModelEditor
reload(MSG2_breakModelEditor)

def main(TARGET_NAME):
	LOG=''
	FN=cmds.file(q=True,sceneName=True,shortName=True).replace('_brk.mb','')
	if cmds.objExists('|root'):
		cmds.rename('|root','reserved_root')
	if cmds.objExists('|col'):
		cmds.rename('|col','reserved_col')

	#DB
	DB=cmds.ls('|bk_*',type='transform')
	if DB:
		cmds.select(cmds.listRelatives(DB,c=True,type='transform',f=True),r=True)
		MSG2_breakModelEditor.MS_copyToCollision('db')
		cmds.delete(DB)

	#BK
	BK=cmds.ls('|deb_*',type='transform')
	if BK:
		cmds.select(cmds.listRelatives(BK,c=True,type='transform',f=True),r=True)
		MSG2_breakModelEditor.MS_copyToCollision('bk')
		cmds.delete(BK)
	#DY
	DY=cmds.ls('|at_*',type='transform')
	if DY:
		cmds.select(cmds.listRelatives(DY,c=True,type='transform',f=True),r=True)
		MSG2_breakModelEditor.MS_copyToCollision('dy')
		cmds.delete(DY)

	#placemet
	if cmds.objExists('|top_db'):
		DBMODEL=FN+'_db'
	else:
		DBMODEL=''

	if cmds.objExists('|top_bk'):
		BKMODEL=FN+'_bk'
	else:
		BKMODEL=''

	if cmds.objExists('|top_dy'):
		DYMODEL=FN+'_dy'
		GRAB='TRUE'
		ATPOW='100'
	else:
		DYMODEL=''
		GRAB='FALSE'
		ATPOW=''

	LOG+=FN+',g1brk,20,'+GRAB+',FALSE,FALSE,0,0,,,'+BKMODEL+','+DBMODEL+',,,'+DYMODEL+',,,FALSE,,,,FALSE,,,'+ATPOW+',,,,'

	return LOG
