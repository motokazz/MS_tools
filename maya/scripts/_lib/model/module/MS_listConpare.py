# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_listConpare
# 説明
#			
# 作成日\n#			
########################################

import maya.cmds as cmds
import csv
import MS_fileExport
	
	
##### CSVインポート #####
	
def CSV_IMPORT(FILE_PATH):
	CSVFILE = open(FILE_PATH)
	DATA=[]
	for ROW in csv.reader(CSVFILE):
		DATA.append(ROW)
	CSVFILE.close()
	return DATA
	
	
def extractColumn(CSV,COL):
	ret=[]
	for each in CSV:
		ret.append(each[COL])
	return ret
		
		
		
def do(MODE='union'):
	result=[]
	csv_a=MS_fileExport.single('MS_listConpare_csv_a',Q=True)
	col_a=cmds.intField('MS_listConpare_csv_a_column',q=True,v=True)
	lista=extractColumn(CSV_IMPORT(csv_a),col_a)
	
	csv_b=MS_fileExport.single('MS_listConpare_csv_b',Q=True)
	col_b=cmds.intField('MS_listConpare_csv_b_column',q=True,v=True)
	listb=extractColumn(CSV_IMPORT(csv_b),col_b)
	
	if MODE=='union':
		result=union(lista,listb)
	if MODE=='difference':
		result=difference(lista,listb)
	if MODE=='intercect':
		result=intercect(lista,listb)
	
	print result
	
def unique2(LIST):
	#リストから重複要素を取り除く。リストの並びは要素の登場順になる。
	RET=[]
	for EACH in LIST:
		if not EACH in RET:
			RET.append(EACH)
	return RET
	
##### main modules
	
def union(lista=[],listb=[]):
	return lista+listb

def difference(lista=[],listb=[]):
	for each in listb:
		try:
			listb.remove(each)
		except:
			continue
	return listb
	
def intercect(lista=[],listb=[]):
	ret=[]
	for each in lista:
		if each in listb:
			ret.append(each)
	return ret


##### UI
	

def layoutA(
	LABEL='MS_listConpare'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()

	
	cmds.text(l=LABEL)
	MS_fileExport.single('MS_listConpare_csv_a')
	cmds.intField('MS_listConpare_csv_a_column',w=WIDTH-4,v=0)
	MS_fileExport.single('MS_listConpare_csv_b')
	cmds.intField('MS_listConpare_csv_b_column',w=WIDTH-4,v=0)
	cmds.button(w=WIDTH-4,l=u'union',c=lambda *args:do('union'))
	cmds.button(w=WIDTH-4,l=u'difference',c=lambda *args:do('difference'))
	cmds.button(w=WIDTH-4,l=u'intercect',c=lambda *args:do('intercect'))
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_listConpare_main_window',q=True,ex=True):
		cmds.deleteUI('MS_listConpare_main_window')
	cmds.window('MS_listConpare_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MS_listConpare_main_window')
	

