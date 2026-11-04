# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_moduleReaders.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

import glob

MODDIR='D:/Projects/Gravite2/tools/maya/maya2014/scripts/python/s2000_tools/MSG2_batch/modules/'
MODULES_PATH = 's2000_tools.MSG2_batch.modules.'

#################
# Module Readers
#################

def module_list():
	MODULES=[]
	
	ML=glob.glob(MODDIR+'*.py')
	for each in ML:
		if '__' in each:
			continue
		MODULES.append(each.replace('\\','/').replace('.py','').replace(MODDIR,''))
	return MODULES

def commandCreation(MODULES_PATH,MODULE_NAME,TARGET_NAME='',dummy=''):
	IMPC='import ' + MODULES_PATH+MODULE_NAME+'\n'
	IMPC+='reload('+MODULES_PATH+MODULE_NAME+')\n'
	COMMAND=MODULES_PATH+MODULE_NAME+'.main("'+TARGET_NAME+'")\n'
	RET=execs(IMPC,COMMAND)
	if RET:
		return RET
	else:
		return 'ok'

def moduleExecuter(MODULE_NAME='',TARGET_NAME=''):
	TARGET_NAME=cmds.file(q=True,sn=True).split('/')[-1].strip('.mb')

	def ret(dummy=''):
		commandCreation(MODULES_PATH,MODULE_NAME,TARGET_NAME)
	return ret

def execs(IMPC,COMMAND):
	exec(IMPC)
	RET=eval(COMMAND)
	return RET


#######################
#main


def main(TARGET_NAME):
	LOG=[]
	LOG.append(TARGET_NAME)

	MODULES=module_list()

	for each in MODULES:
		if not cmds.checkBox(each,q=True,ex=True):
			LOG.append('notfound')
			continue
		if cmds.checkBox(each,q=True,v=True):
			LOG.append(commandCreation(MODULES_PATH,each,TARGET_NAME))

	return ','.join(LOG)


### UI


def LayoutA():
	cmds.columnLayout('MS_moduleReaders.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_moduleReaders.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:commandCreation())
	cmds.separator()
	cmds.setParent('..')

def Layout_modules():
	MODULES=module_list()
	cmds.columnLayout()
	for each in MODULES:
		cmds.rowLayout(nc=2,cw2=(200,50))
		cmds.checkBox(each,l=each,v=False)
		cmds.button(l='do',w=50,c=moduleExecuter(each))
		cmds.setParent('..')
	cmds.setParent('..')



def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	Layout_modules()

	cmds.showWindow('MS_tools_window')
	