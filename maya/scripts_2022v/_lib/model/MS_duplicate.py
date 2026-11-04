# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_duplicate.py
# 説明
#			ショートカットに登録して使うツール
#
#			import model.MS_duplicate as MS_duplicate
#			reload(MS_duplicate)
#			MS_duplicate.main()
#			
# 作成日
#			
########################################
import maya.cmds as cmds
import maya.mel as mel

def duplicateComponent(comp=[]):
	face = cmds.polyListComponentConversion(comp,tf=True)
	OBJ = face[0].split('.')[0]
	DUPED = cmds.duplicate(OBJ,rc=True)

	if len(DUPED)>1:
		DUPED=cmds.polyUnite(DUPED,o=True)

	ncomp=[]
	for i in comp:
		a,b=i.split('.')
		ncomp.append(DUPED[0]+'.'+b)

	cmds.select(ncomp,r=True)
	temptrn=cmds.xform(ncomp,q=True,t=True,ws=True)
	mel.eval('InvertSelection;')
	cmds.delete()
	return DUPED
	
def main():
	DUPED=[]
	comp = cmds.filterExpand(sm=[31,32,34,70])
	obj=cmds.ls(sl=True,type='transform')
	if comp:
		DUPED=duplicateComponent(comp)
	elif obj:
		DUPED=cmds.duplicate(obj,rc=True)
	else:
		return
	cmds.select(DUPED,r=True)







