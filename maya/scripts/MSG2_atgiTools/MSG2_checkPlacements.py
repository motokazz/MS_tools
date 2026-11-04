# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_checkPlacements.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import csv


from s2000_tools.MS_lib.MS_xlsx2csv import Xlsx2csv



PLACEMENT_XLSX ='D:/Projects/Gravite2/planning/datasheets/Placements.xlsx'
PLACEMENT_CSV ='D:/Projects/Gravite2/tools/maya/maya2014/scripts/python/s2000_tools/MSG2_atgiTools/Placements.csv'

#################
# XLSX2CSV
#################

def xlsx2csv(XLSX='',CSV=''):
	X=Xlsx2csv(XLSX)
	X.convert(CSV)

def csvImport(PATH=''):
	RET=[]
	f = open(PATH, 'rb')

	dataReader = csv.reader(f)

	for ROW in dataReader:
		RET.append(ROW)
	return RET

def anlizePlacements_core(DATA):
	DICT={}
	MIDASHI=DATA.pop(0)
	i=0
	for key in MIDASHI:
		TEMP=[]
		for each in DATA:
			AAA=each[i].split()
			for eachAAA in AAA:
				TEMP.append(eachAAA.strip())	
		DICT.setdefault(key,TEMP)
		i+=1
	return DICT


def anlizePlacements():
	RET=[]
	xlsx2csv(PLACEMENT_XLSX,PLACEMENT_CSV)
	DATA=csvImport(PLACEMENT_CSV)
	NEW = anlizePlacements_core(DATA)
	RET.append('datasheet_placements'+','.join(NEW['datasheet_placements']))
	RET.append('broken_model'+','.join(NEW['broken_model']))
	RET.append('debris_model'+','.join(NEW['debris_model']))
	RET.append('mid_models'+','.join(NEW['mid_models']))
	RET.append('dynamic_model'+','.join(NEW['dynamic_model']))
	return RET

def checkPlacements(NAME):
	CSV=csvImport(PLACEMENT_CSV)
	DATA=anlizePlacements_core(CSV)

	for each in CSV:
		if each[0]==NAME:
			return ','.join(each)

	for each in DATA['datasheet_placements']:
		if NAME.strip() == each:
			return 'gimmick'
	return 'BG'


def checkName():
	cmds.textField('MSG2_checkPlacements_name',q=True,tx=True)


def main():
	LOG=u''
	LOG+=cmds.file(q=True,sn=True).split('/')[-1].split('.')[0]
	LOG2=checkPlacements(LOG)
	cmds.scrollField('MSG2_checkPlacements_log',e=True,tx=LOG2)

	return NAME

def LayoutA():

	cmds.columnLayout('MSG2_checkPlacements.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_checkPlacements.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.textField('MSG2_checkPlacements_name')
	cmds.button(l='check this scene',c=lambda *args:main())
	cmds.scrollField('MSG2_checkPlacements_log')
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	