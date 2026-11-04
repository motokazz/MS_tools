# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_assetExport_easy
# 説明
#			
#			
# 作成日
#			
########################################


import maya.cmds as cmds

def assetExport(TGT='',EXPORT_PATH='D:/work/gravitydaze2_work/'):
	#EXPORT

	#TGT='go_parliament_a'
	cmds.select(TGT,r=True)
	cmds.duplicate()
	DUPED=cmds.ls(sl=True,l=True)
	#pre
	print(DUPED[0])
	#delete construction history
	cmds.delete(DUPED[0],ch=True)

	#assign lambert1
	cmds.select(DUPED[0],r=True)
	cmds.hyperShade(a='lambert1')

	#reset transform
	cmds.xform(t=[0,0,0],ro=[0,0,0],ws=True)
	cmds.xform(s=[1,1,1],ws=True)

	#parent to newroot
	EG=cmds.group(em=True,n='root')
	cmds.parent(DUPED[0],EG)

	#export
	FILENAME=TGT.split('|')[-1]
	cmds.select(EG,r=True)
	cmds.file(
		(EXPORT_PATH+FILENAME+'.mb')
		,f=True
		,type='mayaBinary'
		,es=True
		)

	cmds.delete(EG)




def main():
	#rename root
	ROOTEXISTS=False
	if cmds.objExists('|root'):
		ROOTEXISTS=True

	if ROOTEXISTS:
		cmds.rename('|root','temproot')

	SEL=cmds.ls(sl=True,l=True)
	for each in SEL:
		assetExport(each)

	#post
	if ROOTEXISTS:
		cmds.rename('temproot','root')



def LayoutA():
	cmds.columnLayout('MSG2_assetExport_easy_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_assetExport_easy',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	
