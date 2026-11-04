# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_tools_ranking
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds
import os
import glob
import csv

import MS_tools_init
reload(MS_tools_init)

def read(CSVPATH):
	RET=[]

	if '.csv' in CSVPATH:
		csvFile = open(CSVPATH)
	else:
		return
	calc=0
	for row in csv.reader(csvFile):
		calc+=int(row[2])
	csvFile.close()
	filename=CSVPATH.split('checkList_')[-1].replace('.csv','')
	return [filename,calc]



def main():
	LIST=[]
	FILES = glob.glob(MS_tools_init.exec_check_path+'*.csv')
	for each in FILES:
		LIST.append(read(each))

	for each in sorted(LIST,key=lambda x:x[1],reverse=True):
		print each


def LayoutA():
	cmds.frameLayout('MS_tools_ranking_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_tools_ranking',cll=True,cl=False)
	cmds.columnLayout('MS_tools_ranking_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_tools_ranking',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_ranking_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_ranking_window')
	cmds.window('MS_tools_ranking_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_ranking_window')
	