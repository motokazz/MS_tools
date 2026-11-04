# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_readFileText
# 説明
#			ファイルの内容を文字列として読み込む
#			read(
#				filePath = str : ファイルパス
#				readLine = int : 読み込む行数
#				)
# 作成日
#			
########################################
import maya.cmds as cmds

def read(filePath,readLine=10):
	ret=''
	f=open(filePath)
	i=0
	for row in f:
	    if i<readLine and row[0]=='#':
	        ret += row
	    else:
	        break
	    i+=1
	f.close()

	return ret.replace('\t', '  ').decode('utf-8')

def confirm(filePath,readLine=10):
	cmds.confirmDialog(m=read(filePath,readLine))

def rButton(filePath,readLine=10):
	cmds.button(l='r',w=16,h=16,bgc=[0.7,0.8,0.7],c=lambda *args:confirm(filePath,readLine))
