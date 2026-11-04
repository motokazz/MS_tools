# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_CSVImportDict
# 説明
#			
# 作成日
#			
########################################
import csv
	
def importCSV(FILENAME,REMOVE_INDEX=False):
	#戻り値:CSV内容のリスト
	DICT={}
	RET=[]
	CSVFILE = open(FILENAME)
	for ROW in csv.reader(CSVFILE):
		RET.append(ROW)
	CSVFILE.close()
	if REMOVE_INDEX:
		RET.pop(0)
	return RET
	
def toDictColumn(CSV,INDEX=0):
	#リストのカラムを利用してDICT化する
	DICT={}
	for ROW in CSV:
		KEY=ROW[INDEX]
		if not KEY in DICT.keys():
			DICT[KEY]=[]
		DICT[KEY].append(ROW)
	return DICT
	
	
def indexColumn(FILENAME,INDEX=0):
	#戻り値:INDEX　で指定したカラムをキーに辞書を作成
	DICT={}
	CSVFILE = open(FILENAME)
	for ROW in csv.reader(CSVFILE):
		KEY=ROW.pop(INDEX)
		if not KEY in DICT.keys():
			DICT[KEY]=[]
		DICT[KEY].append(ROW)
	CSVFILE.close()
	return DICT
	

def CSV_importDict(FileName,INDEX='cathegory'):
	#戻り値[0]　INDEX　で指定した項目別に辞書を作成
	#戻り値[1]　INDEXリスト　CSV出現順にソートされた見出しを作成
	if '.csv' in FileName:
		CSVFILE = open(FileName)
	else:
		return

	DATA={}
	INDEX_LIST=[]
	for ROW in csv.DictReader(CSVFILE):
		if not ROW[INDEX] in INDEX_LIST:
			INDEX_LIST.append(ROW[INDEX])
			DATA[ROW[INDEX]]=[]
		CATHEGORY=ROW[INDEX]
		DATA[CATHEGORY].append(ROW)
	CSVFILE.close()
	return DATA,INDEX_LIST

