# -*- coding:utf-8 -*-
#MS_STORE_RECALL_UI

#####使用例####
'''
def storeRecallUI( MODE ):
	PREFIX='MP_MS_setUtil__'
	CONTROLL_DICT={}
	CONTROLL_DICT.setdefault('textFieldList', ['MP_MS_setUtil_USERNAME'])
	CONTROLL_DICT.setdefault('tabLayoutList', ['MP_MS_setUtil_MAINTAB'])
	
	if MODE=='store':
		MS_STORE_RECALL_UI.store(PREFIX,CONTROLL_DICT)
	if MODE=='recall':
		MS_STORE_RECALL_UI.recall(PREFIX,CONTROLL_DICT)
	if MODE=='reset':
		MS_STORE_RECALL_UI.reset(PREFIX,CONTROLL_DICT)
'''

import maya.cmds as cmds


PREFIX_HEAD='MP_MS_'


def main(MODE,PREFIX,CONTROLL_DICT):
	if MODE=='store':
		store(PREFIX,CONTROLL_DICT)
	if MODE=='recall':
		recall(PREFIX,CONTROLL_DICT)
	if MODE=='reset':
		reset(PREFIX,CONTROLL_DICT)


def store(PREFIX,DICT):
	#{UI_TYPE:[CONTROLL_NAMES]
	for UI_TYPE in DICT:
		for EACH in DICT[UI_TYPE]:
			NAME=PREFIX_HEAD+PREFIX+EACH
			if UI_TYPE=='floatFieldList' and cmds.control(EACH,ex=True):
				cmds.optionVar(floatValue=[NAME,cmds.floatField(EACH,q=True,value=True)])
			if UI_TYPE=='intFieldList' and cmds.control(EACH,ex=True):
				cmds.optionVar(intValue=[NAME,cmds.intField(EACH,q=True,value=True)])
			if UI_TYPE=='floatSliderGrpList' and cmds.control(EACH,ex=True):
				cmds.optionVar(floatValue=[NAME,cmds.floatSliderGrp(EACH,q=True,value=True)])
			if UI_TYPE=='intSliderGrpList' and cmds.control(EACH,ex=True):
				cmds.optionVar(intValue=[NAME,cmds.intSliderGrp(EACH,q=True,value=True)])
			if UI_TYPE=='checkBoxList' and cmds.control(EACH,ex=True):
				cmds.optionVar(intValue=[NAME,cmds.checkBox(EACH,q=True,value=True)])
			if UI_TYPE=='radioButtonGrpList' and cmds.control(EACH,ex=True):
				cmds.optionVar(intValue=[NAME,cmds.radioButtonGrp(EACH,q=True,select=True)])
			if UI_TYPE=='frameLayoutList' and cmds.control(EACH,ex=True):
				cmds.optionVar(intValue=[NAME,cmds.frameLayout(EACH,q=True,collapse=True)])
			if UI_TYPE=='textFieldList' and cmds.control(EACH,ex=True):
				cmds.optionVar(stringValue=[NAME,cmds.textField(EACH,q=True,tx=True)])
			if UI_TYPE=='textFieldList_file' and cmds.control(EACH,ex=True):
				cmds.optionVar(stringValue=[NAME,cmds.textField(EACH,q=True,fileName=True)])
			if UI_TYPE=='tabLayoutList' and cmds.control(EACH,ex=True):
				cmds.optionVar(stringValue=[NAME,cmds.tabLayout(EACH,q=True,selectTab=True)])
			if UI_TYPE=='optionMenuGrpList' and cmds.control(EACH,ex=True):
				cmds.optionVar(stringValue=[NAME,cmds.optionMenuGrp(EACH,q=True,v=True)])
			if UI_TYPE=='optionMenuList' and cmds.control(EACH,ex=True):
				cmds.optionVar(stringValue=[NAME,cmds.optionMenu(EACH,q=True,v=True)])
			

def recall(PREFIX,DICT):
	for UI_TYPE in DICT:
		for EACH in DICT[UI_TYPE]:
			NAME=PREFIX_HEAD+PREFIX+EACH
			if UI_TYPE=='floatFieldList' and cmds.control(EACH,ex=True):
				if cmds.optionVar(exists=NAME):
					cmds.floatField(EACH,e=True,v=cmds.optionVar(q=NAME))
			if UI_TYPE=='intFieldList' and cmds.control(EACH,ex=True):
				if cmds.optionVar(exists=NAME):
					cmds.intField(EACH,e=True,v=cmds.optionVar(q=NAME))
			if UI_TYPE=='floatSliderGrpList' and cmds.control(EACH,ex=True):
				if cmds.optionVar(exists=NAME):
					cmds.floatSliderGrp(EACH,e=True,v=cmds.optionVar(q=NAME))
			if UI_TYPE=='intSliderGrpList' and cmds.control(EACH,ex=True):
				if cmds.optionVar(exists=NAME):
					cmds.intSliderGrp(EACH,e=True,v=cmds.optionVar(q=NAME))
			if UI_TYPE=='checkBoxList' and cmds.control(EACH,ex=True):
				if cmds.optionVar(exists=NAME):
					cmds.checkBox(EACH,e=True,v=cmds.optionVar(q=NAME))
			if UI_TYPE=='radioButtonGrpList' and cmds.control(EACH,ex=True):
				if cmds.optionVar(exists=NAME):
					cmds.radioButtonGrp(EACH,e=True,select=cmds.optionVar(q=NAME))
			if UI_TYPE=='frameLayoutList' and cmds.control(EACH,ex=True):
				if cmds.optionVar(exists=NAME):
					cmds.frameLayout(EACH,e=True,collapse=cmds.optionVar(q=NAME))
			if UI_TYPE=='textFieldList' and cmds.control(EACH,ex=True):
				if cmds.optionVar(exists=NAME):
					cmds.textField(EACH,e=True,tx=cmds.optionVar(q=NAME))
			if UI_TYPE=='textFieldList_file' and cmds.control(EACH,ex=True):
				if cmds.optionVar(exists=NAME):
					cmds.textField(EACH,e=True,fileName=cmds.optionVar(q=NAME))
			if UI_TYPE=='tabLayoutList' and cmds.control(EACH,ex=True):
				if cmds.optionVar(exists=NAME):
					cmds.tabLayout(EACH,e=True,selectTab=cmds.optionVar(q=NAME))
			if UI_TYPE=='optionMenuGrpList' and cmds.control(EACH,ex=True):
				if cmds.optionVar(exists=NAME):
					cmds.optionMenuGrp(EACH,e=True,v=cmds.optionVar(q=NAME))
			if UI_TYPE=='optionMenuList' and cmds.control(EACH,ex=True):
				if cmds.optionVar(exists=NAME):
					cmds.optionMenu(EACH,e=True,v=cmds.optionVar(q=NAME))
def reset(PREFIX,DICT):
	for UI_TYPE in DICT:
		for EACH in DICT[UI_TYPE]:
			NAME=PREFIX_HEAD+PREFIX+EACH
			print ('deleted : '+NAME)
			cmds.optionVar(remove=NAME)

def check(CONTROLL_NAME):
	NAME=PREFIX_HEAD+CONTROLL_NAME
	if cmds.optionVar(exists=NAME):
		return cmds.optionVar(q=NAME)
	else:
		return 0
