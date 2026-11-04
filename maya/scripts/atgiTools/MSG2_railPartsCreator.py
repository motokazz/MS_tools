# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_railPartsCreator.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel
DICT={
	'ma':[4000,0.784883,270]
	,'mb':[4000,0.784883,225]
	,'mc':[4000,0.784883,180]
	,'md':[4000,0.784883,135]
	,'me':[4000,0.784883,90]
	,'mf':[4000,0.784883,45]
	,'mg':[4000,0.784883,0]
	,'mh':[4000,0.784883,315]
	,'la':[8000,1.569878,270]
	,'lb':[8000,1.569878,225]
	,'lc':[8000,1.569878,180]
	,'ld':[8000,1.569878,135]
	,'le':[8000,1.569878,90]
	,'lf':[8000,1.569878,45]
	,'lg':[8000,1.569878,0]
	,'lh':[8000,1.569878,315]
}

def createSamplePipe():
	cmds.polyPipe(ax=[0,0,1],r=1200,sh=10, h=8000 ,sc=0,t=200)
	cmds.setAttr('.tz',2000)
	cmds.makeIdentity(a=True,t=True)
	cmds.xform(piv=[0,0,0],ws=True)





def main(KEY='_ma'):
	
	SEL=cmds.ls(sl=True)

	#オブジェクト名
	NAME=cmds.textField('MSG2_railTools_baseRailPartsName',q=True,tx=True)
	
	#複製したものを使用
	DUPED=cmds.duplicate()

	#辞書にキーがなかったらグループ化するだけ
	if not KEY in DICT.keys():
		cmds.group(DUPED[0:len(SEL)],n=NAME+'_'+KEY)
		cmds.select(SEL,r=True)
		return

	#createCircle
	CIRCLE=cmds.circle(ch=True,o=True,nr=[0,1,0],r=DICT[KEY][0])
	cmds.setAttr(CIRCLE[0]+".rotateY",90)
	cmds.makeIdentity(CIRCLE[0],a=True,t=True)

	#################
	# パスアニメーションとデフォーマー
	#################
	cmds.select(DUPED[0:len(SEL)],r=True)
	cmds.select(CIRCLE[0],add=True)
	cmds.pathAnimation(fractionMode=True,follow=True,followAxis='z',upAxis='y',worldUpType='vector',worldUpVector=[0,1,0],inverseUp=False,inverseFront=False,bank=False)
	CAGE=cmds.flow(DUPED[0:len(SEL)],divisions=[2,2,60],objectCentered=0,localCompute=1,localDivisions=[2,2,2])

	#普通に作ったケージだと形が壊れるので、ベースを拡大
	i=0
	CHECK=True
	while(CHECK):
		try:
			cmds.select(CAGE[3+i],r=True)
		except:
			break
		SX=cmds.getAttr(CAGE[3+i]+'.scaleX')
		cmds.setAttr(CAGE[3+i]+'.scaleX',SX*10)
		
		SY=cmds.getAttr(CAGE[3+i]+'.scaleY')
		cmds.setAttr(CAGE[3+i]+'.scaleY',SY*10)

		SZ=cmds.getAttr(CAGE[3+i]+'.scaleZ')
		cmds.setAttr(CAGE[3+i]+'.scaleZ',SZ*10)

		i+=4

	#45度のサイズにぴったり合わせるためのリスケール
	for each in DUPED[0:len(SEL)]:
		cmds.setAttr(each+'.scaleZ',DICT[KEY][1])

	#################
	# 任意の回転でパーツ化
	#################
	cmds.setAttr(CIRCLE[0]+".rotateZ",DICT[KEY][2])

	#作業用のデータを削除
	cmds.delete(DUPED[0:len(SEL)],ch=True)
	cmds.select(DUPED[0:len(SEL)],r=True)
	mel.eval('DeleteMotionPaths')
	cmds.delete(CIRCLE)

	#移動値をフリーズ
	for each in DUPED[0:len(SEL)]:
		cmds.makeIdentity(each,a=True,r=True,s=True)
		cmds.xform(each,t=[0,0,0],ws=True)
		#cmds.rename(each,each+'_'+KEY)

	#リネームとグループ化の処理
	#if len(SEL)>1:
	cmds.group(DUPED[0:len(SEL)],n=NAME+'_'+KEY)

	cmds.select(SEL,r=True)

#################
# Store Recall
#################
def store():
	PREFIX='MSG2_railTools'
	CONTROLNAME='MSG2_railTools_baseRailPartsName'
	NAME=PREFIX+CONTROLNAME
	if cmds.control(CONTROLNAME,ex=True):
		cmds.optionVar(stringValue=[NAME,cmds.textField(CONTROLNAME,q=True,tx=True)])

def recall():
	PREFIX='MSG2_railTools'
	CONTROLNAME='MSG2_railTools_baseRailPartsName'
	NAME=PREFIX+CONTROLNAME
	if cmds.optionVar(exists=NAME):
		cmds.textField(CONTROLNAME,e=True,tx=cmds.optionVar(q=NAME))

###############
# UI
###############

def LayoutButtons():
	cmds.gridLayout(nc=5)
	#
	cmds.button(l='lf',c=lambda *args:main('lf'))
	cmds.text(l='')
	cmds.button(l='le',c=lambda *args:main('le'))
	cmds.text(l='')
	cmds.button(l='ld',c=lambda *args:main('ld'))
	#
	cmds.text(l='')
	cmds.button(l='mf',c=lambda *args:main('mf'))
	cmds.button(l='me',c=lambda *args:main('me'))
	cmds.button(l='md',c=lambda *args:main('md'))
	cmds.text(l='')
	#
	cmds.button(l='lg',c=lambda *args:main('lg'))
	cmds.button(l='mg',c=lambda *args:main('mg'))
	cmds.button(l='a',c=lambda *args:main('a'))
	cmds.button(l='mc',c=lambda *args:main('mc'))
	cmds.button(l='lc',c=lambda *args:main('lc'))
	#
	cmds.text(l='')
	cmds.button(l='mh',c=lambda *args:main('mh'))
	cmds.button(l='ma',c=lambda *args:main('ma'))
	cmds.button(l='mb',c=lambda *args:main('mb'))
	cmds.text(l='')
	#
	cmds.button(l='lh',c=lambda *args:main('lh'))
	cmds.text(l='')
	cmds.button(l='la',c=lambda *args:main('la'))
	cmds.text(l='')
	cmds.button(l='lb',c=lambda *args:main('lb'))
	#
	cmds.setParent('..')

def LayoutA():
	cmds.columnLayout('MSG2_railPartsCreator_mainLayout',adj=True,bgc=[0.3,0.3,0.35])
	cmds.separator()
	cmds.text(l='railPartsCreator',bgc=[0.8,0.8,0.9],fn='boldLabelFont')
	cmds.text(l='baseRailPartsName')
	cmds.textField('MSG2_railTools_baseRailPartsName',tx='az6_pipe',cc=lambda *args:store())
	LayoutButtons()
	cmds.button(l='createSamplePipe',c=lambda *args:createSamplePipe())
	cmds.separator()
	cmds.setParent('..')
	recall()

def UI():
	if cmds.window('MSG2_railTools_window',q=True,ex=True):
		cmds.deleteUI('MSG2_railTools_window')
	cmds.window('MSG2_railTools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MSG2_railTools_window')

	recall()