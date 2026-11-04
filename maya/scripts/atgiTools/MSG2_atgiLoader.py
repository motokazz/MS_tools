# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_atgiLoader.py
# 説明
#			
#			
# 作成日
#			
########################################


import maya.cmds as cmds


def main(ATGINAME,ATGIPATH='D:/Projects/Gravite2/assets/bg/model'):
	SEL=cmds.ls(sl=True,tr=True,l=True)
	NEWATGI=''
	if not SEL:
		#選択無し
		SEL=[createAtgiNode()]
	for EACHSEL in SEL:
		mods = cmds.getModifiers()
		
		if (mods & 1) > 0:
			#Shiftキーを押しながらで強制ATGI新規作成モード
			NODE=createAtgiNode(EACHSEL)
			ATGINODE = cmds.listRelatives(ad=True,type='GraviteAtgiLocatorNode')[0]

		elif cmds.nodeType(EACHSEL) == 'GraviteAtgiLocatorNode':
			#Atgi生選択中
			ATGINODE = EACHSEL

		elif cmds.nodeType(cmds.listRelatives(EACHSEL,s=True,f=True)) == 'GraviteAtgiLocatorNode':
			#子供がAtgi選択中
			ATGINODE = cmds.listRelatives(EACHSEL,ad=True,type='GraviteAtgiLocatorNode',f=True)[0]

		elif not cmds.nodeType(cmds.listRelatives(EACHSEL,s=True,f=True)) == 'GraviteAtgiLocatorNode':
			#Atgi以外を選択中
			NODE=createAtgiNode(EACHSEL)
			ATGINODE = cmds.listRelatives(ad=True,type='GraviteAtgiLocatorNode')[0]
		else:
			#全てに引っかからない
			continue

		ATGIFILEPATH = ATGIPATH+'/'+ATGINAME+'.atgi'
		cmds.setAttr(ATGINODE + '.atgiFilename',ATGIFILEPATH,type='string')

		#ワイヤーフレームカラー
		cmds.color(ATGINODE,ud=2)

		#リネーム処理
		PNODE=cmds.listRelatives(ATGINODE,p=True,f=True)
		NEWATGI=cmds.rename(PNODE,ATGINAME+'_01')
		NEWATGI=cmds.ls(NEWATGI,l=True)

		#ctrlキーが押されているときの処理
		if NEWATGI:
			mods = cmds.getModifiers()
			if (mods & 4) > 0:#+ctrl
				PAR=cmds.listRelatives(EACHSEL,ap=True,f=True)
				cmds.parent(NEWATGI,PAR[0])
				cmds.delete(EACHSEL)
