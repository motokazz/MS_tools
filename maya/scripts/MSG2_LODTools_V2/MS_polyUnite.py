# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_polyUnite.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel
import time

MPDA=['wireframe','wireframe','wireframe','wireframe']

#プログレスバー
class MS_Progress:
	def __init__(self):
		pass

	def create(self,MAXVALUE=10):
		if MAXVALUE<1:
			MAXVALUE=1
		#プログレスウィンドウ
		if cmds.window('MS_ProgressWindow',ex=True):
			cmds.deleteUI('MS_ProgressWindow')
		if cmds.windowPref('MS_ProgressWindow',ex=True):
			cmds.windowPref('MS_ProgressWindow',r=True)
		cmds.window('MS_ProgressWindow',wh=[248,70],tlc=[414,516],tlb=True,s=True,t='Calculating')
		cmds.columnLayout()
		cmds.progressBar('MS_progress',minValue=0,maxValue=MAXVALUE,width=246)
		cmds.setParent ('..')
		cmds.showWindow ('MS_ProgressWindow')

	def add(self):
		cmds.progressBar('MS_progress',edit=True,s=1)

	def delete(self):
		cmds.deleteUI('MS_ProgressWindow')

def MS_polyChipOff():
	#複数選択したオブジェクトのフェースをチップオフする
	SEL=cmds.ls(hl=True)
	DUPED=cmds.duplicate(SEL)
	POLY=cmds.filterExpand(sm=34)
	if not POLY:
		return False
	ARR=[]
	i=0
	for each in SEL:
		for eachPoly in POLY:
			if each in eachPoly:
				ARR.append(eachPoly.replace(each,DUPED[i]))
		i+=1
	cmds.select(ARR,r=True)
	cmds.InvertSelection()
	cmds.delete()
	return DUPED

def MS_polyUnite():
	obj_name=cmds.ls(l=True,sl=True) 
	SHORT_NAME=cmds.ls(obj_name[0])
	parent=cmds.listRelatives(obj_name[0],p=True)
	
	UNITED=cmds.polyUnite(obj_name,ch=False)

	NEW_NAME=cmds.rename(UNITED[0],SHORT_NAME[0])

	if cmds.objExists(parent[0]):
		cmds.parent(NEW_NAME,parent[0])

	return cmds.ls(sl=True,l=True)

def polyCountGrouping(SEL,MAXCOUNT=2000):
	##プログレス
	MPR=MS_Progress()
	MPR.create(len(SEL))
	POLYCOUNT=0
	GPQ=0
	GP=[[]]
	while(SEL):
		MPR.add()#プログレス
		NOW=SEL.pop(0)
		try:
			POLYCOUNT+=cmds.polyEvaluate(NOW,v=True)
			GP[GPQ].append(NOW)
		except:
			pass
		if POLYCOUNT>MAXCOUNT:
			POLYCOUNT=0
			GP.append([])
			GPQ+=1

	MPR.delete()#プログレス
	return GP

def MS_superPolyUnite(CONSIDER_PARENTS=True):
	#
	SEL=cmds.ls(sl=True,tr=True,dag=True,l=True)
	if len(SEL)<2:
		return SEL
	cmds.delete(SEL,ch=True)

	SHORT_NAME=cmds.ls(SEL[0])

	PARENT=cmds.listRelatives(SEL[0],p=True,f=True)
	GP=polyCountGrouping(SEL,MAXCOUNT=2000)
	
	##プログレス
	MPR=MS_Progress()
	MPR.create(len(GP))

	UNITED_OBJECTS=[]
	for EACH in GP:
		MPR.add()#プログレス
		if len(EACH)>1:
			UNITED=cmds.polyUnite(EACH,ch=True)
			UNITED_OBJECTS.append(UNITED[0])
		else:
			if len(EACH)==1:
				UNITED_OBJECTS.append(EACH[0])
			

	MPR.delete()#プログレス

	#2000以下UNITEのモデルが複数あったら、２００００超えるまでUNITE
	if len(UNITED_OBJECTS)>1:
		GP=polyCountGrouping(UNITED_OBJECTS,MAXCOUNT=20000)
		UNITED_OBJECTS=[]
		MPR.create(len(GP))#プログレス
		for EACH in GP:
			MPR.add()#プログレス
			if len(EACH)>1:
				UNITED=cmds.polyUnite(EACH,ch=True)
				UNITED=cmds.rename(UNITED[0],SHORT_NAME[0])
				UNITED_OBJECTS.append(UNITED)
			else:
				if len(EACH)==1:
					UNITED_OBJECTS.append(EACH[0])
		MPR.delete()#プログレス


	if PARENT and CONSIDER_PARENTS:
		UNITED_OBJECTS = cmds.parent(UNITED_OBJECTS,PARENT[0])
		UNITED_OBJECTS = cmds.ls(sl=True,l=True)

	cmds.delete(UNITED_OBJECTS,ch=True)

	return UNITED_OBJECTS

def MS_polySeparate():
	RET=[]
	
	comp = cmds.filterExpand(sm=34,ex=True)
	if comp:
		cmds.polyChipOff(ch=1,kft=1,dup=False,off=0)
		return

	SEL=cmds.ls(sl=True,tr=True,dag=True,l=True)
	if SEL:
		cmds.delete(SEL,ch=True)

	##プログレス
	MPR=MS_Progress()
	MPR.create(len(SEL))

	for each in SEL:
		MPR.add()
		try:
			PARENT=cmds.listRelatives(each,p=True,f=True)
			SEPARATED=cmds.polySeparate(each,ch=False)
			if PARENT:
				SEPARATED = cmds.parent(SEPARATED,PARENT[0])
				SEPARATED = cmds.ls(sl=True,l=True)
				try:
					cmds.delete(each)
				except:
					pass
			RET.extend(SEPARATED)
		except:
			RET.append(each)

	MPR.delete()
	
	return RET

def configModelPanel(MODE='store'):
	global MPDA
	if MODE=='store':
		MPDA[0] = cmds.modelEditor('modelPanel1',q=True,displayAppearance=True)
		MPDA[1] = cmds.modelEditor('modelPanel2',q=True,displayAppearance=True)
		MPDA[2] = cmds.modelEditor('modelPanel3',q=True,displayAppearance=True)
		MPDA[3] = cmds.modelEditor('modelPanel4',q=True,displayAppearance=True)
		cmds.modelEditor('modelPanel1',e=True,displayAppearance='wireframe')
		cmds.modelEditor('modelPanel2',e=True,displayAppearance='wireframe')
		cmds.modelEditor('modelPanel3',e=True,displayAppearance='wireframe')
		cmds.modelEditor('modelPanel4',e=True,displayAppearance='wireframe')

	if MODE=='recall':
		cmds.modelEditor('modelPanel1',e=True,displayAppearance=MPDA[0])
		cmds.modelEditor('modelPanel2',e=True,displayAppearance=MPDA[1])
		cmds.modelEditor('modelPanel3',e=True,displayAppearance=MPDA[2])
		cmds.modelEditor('modelPanel4',e=True,displayAppearance=MPDA[3])

def main(COMMAND,UNDO_CUT=True):
	TM = time.time()

	#UNDO削除、設定をきる
	if UNDO_CUT:
		cmds.flushUndo()
		CURRENT_UNDO_INFO=cmds.undoInfo(q=True,st=True)
		cmds.undoInfo(st=False)
		
	#処理を早めるためにワイヤーフレーム表示
	configModelPanel(MODE='store')

	RET=[]
	try:
		RET=COMMAND()
	except Exception as e:
		print 'ERROR:'
		print 'type:' + str(type(e))
		print 'args:' + str(e.args)
		print 'message:' + e.message
		print str(e)
	#ワイヤーフレーム表示を元に戻す
	configModelPanel(MODE='recall')
	#UNDO設定を元に戻す
	if UNDO_CUT:
		cmds.undoInfo(st=CURRENT_UNDO_INFO)
	print RET
	print time.time()-TM
	return RET

def LayoutA():
	cmds.columnLayout('MS_polyUnite.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_polyUnite.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='MS_polyUnite',c=lambda *args:main(MS_superPolyUnite))
	cmds.button(l='MS_polySeparate',c=lambda *args:main(MS_polySeparate))
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	