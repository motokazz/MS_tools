# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_bool.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

BOOL_OPERATION = 1

def compairCenterPivot(A,B):	#ピボット位置を比較して、同じかどうか判断する
	cmds.xform(A,cp=True)
	PIVA=cmds.xform(A,q=True,piv=True,ws=True)
	cmds.xform(B,cp=True)
	PIVB=cmds.xform(B,q=True,piv=True,ws=True)
	if PIVA==PIVB:
		return True
	else:
		return False

def boolDouble(A,B):
	#A
	OA=cmds.duplicate(A)
	BSA=cmds.duplicate(B)
		
	#コンストラクションヒストリー削除
	cmds.delete(OA,ch=True)
	cmds.delete(BSA,ch=True)

	#bool
	RESA=cmds.polyBoolOp(OA,BSA,op=BOOL_OPERATION,ch=0,preserveColor=0,caching=True)

	#ブーリアン失敗したら失敗してるやつを消す
	
	if compairCenterPivot(RESA[0],A) or cmds.polyEvaluate(RESA,v=True)<3:
		cmds.delete(RESA)
		if cmds.objExists(BSA[0]):
			cmds.delete(BSA)
		print 'failed :'+RESA[0]+':'+OA[0]+':'+BSA[0]
		return False

	#B
	OB=cmds.duplicate(A)
	BSB=cmds.duplicate(B)
	cmds.polyNormal(BSB,normalMode=0,userNormalMode=0,ch=0)

	#コンストラクションヒストリー削除
	cmds.delete(OB,ch=True)
	cmds.delete(BSB,ch=True)
					
	#bool
	RESB=cmds.polyBoolOp(OB,BSB,op=BOOL_OPERATION,ch=0,preserveColor=0,caching=True)

	return RESA[0],RESB[0]


def main(OP=1):
	
	global BOOL_OPERATION
	BOOL_OPERATION=OP

	BSS=cmds.textField('MS_bool_boolSeeds',q=True,tx=True).split(';')
	ORG=cmds.ls(sl=True,l=True)

	#オリジナルを保持
	if cmds.checkBox('MS_bool_keepOriginal',q=True,v=True):
		ORG=cmds.duplicate(ORG)

	for eachBS in BSS:
		
		NORG=[]

		for eachORG in ORG:
			#cmds.confirmDialog(m=eachORG+';'+eachBS)

			BD=boolDouble(eachORG,eachBS)

			if BD:
				NORG.extend(BD)
			else:
				DUP=cmds.duplicate(eachORG)
				if cmds.listRelatives(DUP,p=True):
					DUP=cmds.parent(DUP,w=True)
				NORG.extend(DUP)

		cmds.delete(ORG)

		ORG=NORG


def registBoolSeeds():
	OBJ=cmds.ls(sl=True,l=True)
	cmds.textField('MS_bool_boolSeeds',e=True,tx=';'.join(OBJ))

def LayoutA():
	cmds.columnLayout('MS_bool _mainLayout',adj=True)
	cmds.separator()

	cmds.text(l='MS_bool',bgc=[0.9,0.9,0.9],fn='boldLabelFont')


	cmds.rowLayout(nc=2,cw2=[200,100])
	cmds.textField('MS_bool_boolSeeds',tx='',en=False)
	cmds.button(l='registBoolSeeds',c=lambda *args:registBoolSeeds())
	cmds.setParent('..')

	cmds.checkBox('MS_bool_keepOriginal',l='keepOriginal',v=True)
	
	cmds.gridLayout(nc=3,cw=100)
	cmds.button(l='Union',c=lambda *args:main(1))
	cmds.button(l='Difference',c=lambda *args:main(2))
	cmds.button(l='Intersect',c=lambda *args:main(3))
	cmds.setParent('..')

	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_boolset_window',q=True,ex=True):
		cmds.deleteUI('MS_boolset_window')
	cmds.window('MS_boolset_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_boolset_window')
	