# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_assetsUtil.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import os
import glob

import s2000_tools.MS_lib.MSG2_P4Lib as MSG2_P4Lib
reload(MSG2_P4Lib)

import s2000_tools.MSG2_atgiTools.MSG2_check_atgi_located as MSG2_check_atgi_located
reload(MSG2_check_atgi_located)


#JAMSetting
JAM_SET_PATH='D:/Projects/Gravite2/graphic/bg/jam/setting/'

#MB_path
MB_PATH='D:/Projects/Gravite2/graphic/bg/scenes/'

#JAM
JAM_THUMBNAIL='D:/Projects/Gravite2/graphic/bg/jam/thumbnail/'

#atgi_path
ATGI_PATH='D:/Projects/Gravite2/assets/bg/model/'

#anim_path
ANIM_PATH='D:/Projects/Gravite2/assets/bg/anim/'

#hkx_path
HKX_PATH='D:/Projects/Gravite2/assets/bg/collision/'

def searchPath(SEARCHPATH,searchFile='',searchExt='mb'):
	for (root,dir,files) in os.walk(SEARCHPATH):
		#発見時の処理
		for f in files:
			
			fname=f.split('.')[0]
			if (searchFile+'.'+searchExt) == f:
				root=root.replace('\\','/').replace('//','/')
				return root+'/'+f
	return False

def getPathes(ATGINAME=''):
	RET=[]
	RET.extend(glob.glob(JAM_SET_PATH+'*'+ATGINAME+'.xml'))
	RET.append(searchPath(MB_PATH,ATGINAME,'mb'))
	RET.extend(glob.glob(JAM_THUMBNAIL+'*'+ATGINAME+'.jpg'))
	RET.extend(glob.glob(ATGI_PATH+'*'+ATGINAME+'.atgi'))
	RET.extend(glob.glob(ANIM_PATH+'*'+ATGINAME+'.atgi'))
	RET.extend(glob.glob(HKX_PATH+'*'+ATGINAME+'.hkx'))
	return RET

# P4


def p4Button(PATH=''):
	CHECK=MSG2_P4Lib.P4Status(PATH)
	if CHECK=='checkout':return cmds.button(l='checkout',bgc=[0.6,0.8,0.6])
	if CHECK=='locked':return cmds.button(l='locked',bgc=[0.8,0.6,0.6])
	if CHECK=='notcheckout':return cmds.button(l='inDepo Delete?',bgc=[0.8,0.9,0.9],c=lambda *args:MSG2_P4Lib.P4DeleteMarking(PATH))
	if CHECK=='localFile':return cmds.button(l='localFile Delete?',c=lambda *args:deleteFile(PATH))

def deleteFile(PATH=''):
	os.remove(PATH)


def autoLabel(DATA=''):
	if not DATA:return cmds.text(l='none')
	if '.xml' in DATA:return cmds.text(l='XML',bgc=[0.6,0.8,0.6])
	if '_brk' in DATA:return cmds.text(l='BRK',bgc=[0.8,0.6,0.6])
	if '.mb' in DATA:return cmds.text(l='MB',bgc=[0.6,0.8,0.8])
	if '.jpg' in DATA:return cmds.text(l='JPG',bgc=[0.7,0.7,0.7])
	if '.atg' in DATA:return cmds.text(l='ATGI',bgc=[0.6,0.6,0.8])
	if '.hkx' in DATA:return cmds.text(l='HKX',bgc=[0.8,0.8,0.6])


def main(ATGINAME=''):
	def RET(dummy=''):
		if cmds.window('MSG2_assetsUtil_window',q=True,ex=True):
			cmds.deleteUI('MSG2_assetsUtil_window')
		cmds.window('MSG2_assetsUtil_window',rtf=True,s=True)
		
		p4CreateListLayout(ATGINAME)

		cmds.showWindow('MSG2_assetsUtil_window')
	return RET


def p4CreateListLayout(ATGINAME=''):
	cmds.columnLayout()
	LOG=MSG2_check_atgi_located.searchAtgiFromName([ATGINAME])

	#配置確認
	if int(LOG[1].split(',')[1])<1:
		cmds.text(l='notPlaced',bgc=[0.8,0.5,0.5])

	cmds.text(l=LOG[1])
	
	#レイアウト
	FILES=getPathes(ATGINAME)
	for each in FILES:
		cmds.rowLayout(nc=3,cw3=[40,500,150],cl3=['center','left','center'],columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)] )
		autoLabel(each)
		cmds.text(l=each)
		p4Button(each)
		cmds.setParent('..')
	cmds.setParent('..')



def assetsUtil_scrollLayout():
	cmds.columnLayout('MSG2_assetsUtil_scrollLayout_parent')
	cmds.scrollLayout('MSG2_assetsUtil_scrollLayout')
	cmds.setParent('..')
	cmds.setParent('..')



def LayoutA():
	cmds.columnLayout('MSG2_assetsUtil_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_assetsUtil.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MSG2_assetsUtil_window',q=True,ex=True):
		cmds.deleteUI('MSG2_assetsUtil_window')
	cmds.window('MSG2_assetsUtil_window',rtf=True,s=True)
	
	LayoutA()
	assetsUtil_scrollLayout()

	cmds.showWindow('MSG2_assetsUtil_window')
		