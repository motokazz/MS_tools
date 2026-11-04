# -*- coding: utf-8 -*-
'''
とりあえずバージョン
かなりつくりかけ

'''

import maya.cmds as cmds
import maya.mel as mel

def MS_selectTime():
	'''
	タイムスライダーから時間を取得
	スライダーで範囲選択がある場合はその範囲内を
	そうでない場合は現在のタイムスライダーの範囲を返す
	'''
	#グローバル宣言しないとプロシージャ内でタイムスライダーを特定できない。
	aPlayBackSliderPython = mel.eval('$tmpVar=$gPlayBackSlider')
	tc=cmds.timeControl(aPlayBackSliderPython,q=1,rng=1,gt=1)
	
	buf=tc.replace('"','').split(':')
	
	if((int(buf[1])-int(buf[0]))<=1):
		buf[0]=cmds.playbackOptions(q=1,min=1)
		buf[1]=cmds.playbackOptions(q=1,max=1)
	return [buf[0],buf[1]]


def MS_currentSceneShortName():
	filename=cmds.file(q=1,sn=1)
	fnsp=filename.split('/')[-1].split('.')
	return fnsp[0]

def MS_saver():
	cmds.file( save=True, de=False, type='mayaBinary' )

def UDK_animBuffer():
	sceneName=MS_currentSceneShortName()
	arange=MS_selectTime()
	#commands=('axexecute -path "d:/data/udk/" -skinfile "gum" -sequence '+sceneName+' -range '+str(arange[0])+' '+str(arange[1])+' -rate 30 -saveanim -animfile "gum"')
	commands=('axexecute -sequence '+sceneName+' -range '+str(int(arange[0]))+'-'+str(int(arange[1]))+' -rate 60')
	print commands
	mel.eval(commands)

def UDK_animBufferBatch(WORLDSPACE):
	scenefiles=cmds.getFileList (folder=WORLDSPACE,filespec='*.mb')
	print scenefiles
	for each in scenefiles:
		cmds.file(f=1,new=1)
		cmds.file(each,o=1)
		#MS_saver()
		UDK_animBuffer()

	
#WORLDSPACE=cmds.internalVar(userWorkspaceDir=True)
WORLDSPACE=('D:/DATA/udk/scenes/')
#UDK_animBufferBatch(WORLDSPACE)
UDK_animBuffer()



