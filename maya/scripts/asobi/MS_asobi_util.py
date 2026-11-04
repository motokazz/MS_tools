# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_asobi_util
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds
import os
import glob
import pickle

loxDir='D:/asobi/target/data/multi_platformer/lox/'

execpath = os.path.dirname(os.path.abspath(__file__))
picklepath= execpath+'/MS_asobi_util.pickle'

# load all lox
def loadAllLox():
	loxes = []
	for each in glob.glob(loxDir + '*.lox'):
		each = each.replace('\\', '/')
		each = each.split('/')[-1].split('.')[0]
		loxes.append(each)

	return loxes

loxs = loadAllLox()


# data io
def save(path,data):
	with open( path , mode='wb') as f:
		pickle.dump(data, f)

def load(path):
	with open( path , mode='rb') as f:
		ret = pickle.load(f)
	return ret

def saveSetting():
	ps = preset
	checkQ2()
	save(picklepath,ps)

def loadSetting(preset='default'):
	loadSet = load(picklepath)
	for each in loadSet.keys():
		if cmds.checkBox(each,q=True,ex=True):
			cmds.checkBox(each,e=True,v=loadSet[each])

# data structure

def presets():
	presetsl=['a','b','c']
	presets = {}
	for each in presetsl:
		presets.setdefault(each,)

def grouping(selection_mode=False):
	dic={}
	resFalse=[]

	if selection_mode:
		SEL = cmds.ls(sl=True,type='transform',l=True)
	else:
		SEL = cmds.ls(type='transform',l=True,assemblies=True)

	for each in SEL:
		
		#親がいたらスキップ
		if cmds.listRelatives(each,p=True):continue

		#グループノードはスキップ
		if not cmds.listRelatives(each,s=True):continue

		#
		try:
			TYPE = cmds.nodeType(cmds.listRelatives(each,s=True)[0])
			if TYPE == 'camera' or TYPE == 'joint':
				continue
		except:
			pass
		
		#LOX無い奴はサンプル送り
		if not cmds.attributeQuery('LoxFile',n=each,ex=True):
			resFalse.append(each)
			continue

		FN=cmds.getAttr(each+'.LoxFile')
		if FN in dic.keys():
			dic[FN].append(each)
		else:
			dic.setdefault(FN,[each])

	for each in dic.keys():
		NGR = '|'+each+'_grp'

		# グループ無ければ作る
		if not cmds.objExists(NGR):
			cmds.group(em=True,n=NGR)

		for eachNode in dic[each]:
			try:
				cmds.parent(eachNode,NGR)
			except:
				print eachNode
				pass

	NGR = cmds.group(em=True,n='sample')
	for eachNode in resFalse:
		cmds.parent(eachNode,NGR)


def checkQ():
	ca=cmds.scrollLayout('MS_asobi_util_loxlist_p',q=True,ca=True)

	trueList =[]
	falseList=[]

	for each in ca:
		if cmds.checkBox(each,q=True,v=True):
			trueList.append(each.split('_')[-1])
		else:
			falseList.append(each.split('_')[-1])

	return [trueList,falseList]

def createList():

	cq = checkQ()

	trueList = cq[0]

	resTrue = []
	resFalse= []

	#SEL = cmds.ls(rn=True,type='transform',l=True)
	SEL = cmds.ls(type='transform',l=True)
	
	for each in SEL:
		if not cmds.attributeQuery('LoxFile',n=each,ex=True):
			resFalse.append(each)
			continue

		FN=cmds.getAttr(each+'.LoxFile')

		if FN in trueList:
			resTrue.append(each)
		else:
			resFalse.append(each)

	cmds.select(resTrue,r=True)
	
	return [resTrue,resFalse]

class uitemp:
	def __init__(self):
		self.var = {}
class preset:
	def __init__(self):
		self.preset=''
		self.uitemp={}

def checkQ2(preset='default'):
	ps = preset
	ca=cmds.scrollLayout('MS_asobi_util_loxlist_p',q=True,ca=True)
	ps.preset = preset
	for each in ca:
		if cmds.checkBox(each,q=True,v=True):
			ps.uitemp.setdefault(each,True)
		else:
			ps.uitemp.setdefault(each,False)


### select ###

def createLoxList(lox=[]):
	ret=[]
	#SEL = cmds.ls(rn=True,type='transform',l=True)
	SEL = cmds.ls(l=True,assemblies=True,tr=True)

	for each in SEL:

		if not cmds.attributeQuery('LoxFile',n=each,ex=True):
			if 'none' in lox:
				ret.append(each)
			continue

		#親がLOXはパス			
		if cmds.listRelatives(each,p=True):
			if cmds.attributeQuery('LoxFile',n=cmds.listRelatives(each,p=True,f=True)[0],ex=True):
				continue
		
		FN=cmds.getAttr(each+'.LoxFile')
		for eachlox in lox:
			if FN == eachlox:
				ret.append(each)
	return ret

def selectLoxInRef(lox=[]):
	def ret(dummy=''):
		addFlag=False
   		mods = cmds.getModifiers()
		if (mods & 1) > 0: addFlag=True
		res=createLoxList(lox)
		if addFlag:
			cmds.select(res,add=True)
		else:
			cmds.select(res,r=True)
	return ret

def selectChecked():
	activeLoxs = []
	if cmds.checkBox('MS_asobi_util_loxlist_checkbox:none',q=True,ex=True):
		if cmds.checkBox('MS_asobi_util_loxlist_checkbox:none',q=True,v=True):
			activeLoxs.append('none')

	for each in loxs:
		if cmds.checkBox('MS_asobi_util_loxlist_checkbox:'+each,q=True,ex=True):
			if cmds.checkBox('MS_asobi_util_loxlist_checkbox:'+each,q=True,v=True):
				activeLoxs.append(each)
	selectLoxInRef(activeLoxs)
	#cmds.select(createLoxList(activeLoxs),r=True)

def checkAll(Var=True):
	if cmds.checkBox('MS_asobi_util_loxlist_checkbox:none',q=True,ex=True):
		cmds.checkBox('MS_asobi_util_loxlist_checkbox:none',e=True,v=Var)
	for each in loxs:
		if cmds.checkBox('MS_asobi_util_loxlist_checkbox:'+each,q=True,ex=True):
			cmds.checkBox('MS_asobi_util_loxlist_checkbox:'+each,e=True,v=Var)


### save attributes

saveRefferenceAttributes_picklepath= execpath+'/MS_asobi_util_saveRefferenceAttributes.pickle'

def saveRefferenceAttributes(Attributes=[]):
	ret=[]
	#SEL = cmds.ls(rn=True,type='transform',l=True)
	SEL = cmds.ls(type='transform',l=True,assemblies=True)

	for each in SEL:
		for eachAttr in Attributes:
			if not cmds.attributeQuery(eachAttr,n=each,ex=True):
				continue
			Var=cmds.getAttr(each+'.'+eachAttr)
			ret.append([each,eachAttr,Var])

	save(saveRefferenceAttributes_picklepath,ret)

def loadRefferenceAttributes():
	data = load(saveRefferenceAttributes_picklepath)
	for each in data:
		if not cmds.objExists(each[0]):
			continue
		cmds.setAttr(each[0]+'.'+each[1],each[2])

### layout

def refleshList():

	if cmds.scrollLayout('MS_asobi_util_loxlist_p',q=True,ex=True):
		cmds.deleteUI('MS_asobi_util_loxlist_p')
	cmds.scrollLayout('MS_asobi_util_loxlist_p',p='MS_asobi_util_mainLayout')

	# 
	usingLox=[]
	#SEL = cmds.ls(rn=True,type='transform',l=True)
	SEL = cmds.ls(type='transform',l=True,assemblies=True)

	for eachSel in SEL:
		if not cmds.attributeQuery('LoxFile',n=eachSel,ex=True):
			continue
		FN = cmds.getAttr(eachSel+'.LoxFile')
		if not FN in usingLox:
			usingLox.append(FN)

	# 
	cmds.rowLayout(nc=2)
	cmds.button(l='selectRef',c=selectLoxInRef(['none']))
	cmds.checkBox('MS_asobi_util_loxlist_checkbox:none',l='none',v=True)
	cmds.setParent('..')

	for each in loxs:
		if not each in usingLox:
			continue
		cb=True
		cmds.rowLayout(nc=2)
		cmds.button(l='selectRef',c=selectLoxInRef([each]))
		cmds.checkBox('MS_asobi_util_loxlist_checkbox:'+each,l=each,v=cb)
		cmds.setParent('..')

	cmds.setParent('..')
	cmds.setParent('..')

def LayoutA():
	cmds.frameLayout('MS_asobi_util_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_asobi_util',cll=True,cl=False)
	cmds.columnLayout('MS_asobi_util_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_asobi_util',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='save',c=lambda *args:saveSetting())
	cmds.button(l='load',c=lambda *args:loadSetting())

	cmds.separator()
	cmds.text(l='save attributes',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='saveRefferenceAttributes',c=lambda *args:saveRefferenceAttributes(Attributes=['visibility']))
	cmds.button(l='loadRefferenceAttributes',c=lambda *args:loadRefferenceAttributes())

	cmds.separator()
	cmds.text(l='grouping',bgc=[0.9,0.9,0.9],fn='boldLabelFont')

	cmds.button(l='grouping assemblies',c=lambda *args:grouping())
	cmds.button(l='grouping selections',c=lambda *args:grouping(selection_mode=True))

	cmds.separator()
	cmds.text(l='selector',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='selectChecked',c=lambda *args:selectChecked(),bgc=[0.8,0.8,0.8])
	cmds.button(l='checkAllTrue',c=lambda *args:checkAll(True))
	cmds.button(l='checkAllFalse',c=lambda *args:checkAll(False))


	cmds.separator()
	cmds.text(l='MS_asobi_util',bgc=[0.9,0.9,0.9],fn='boldLabelFont')

	cmds.scrollLayout('MS_asobi_util_loxlist_p',w=400)
	cmds.setParent('..')


	
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_asobi_util_window',q=True,ex=True):
		cmds.deleteUI('MS_asobi_util_window')
	cmds.window('MS_asobi_util_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_asobi_util_window')

	refleshList()
	