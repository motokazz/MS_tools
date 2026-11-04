# _*_coding:utf-8_*_
########################################
# ファイル名
#			sqlite3_test
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds

import sqlite3

path_DB='d:/work/test.db'

tables=[
	'no'
	,'pack'
	,'batch'
	,'pre_atgi'
	,'maya_filename'
	,'priority'
	,'thumbneil'
	,'document_link'
	,'concept_art_link'
	,'refference_link'
	,'summary'
	,'type'
	,'relative_assets'
	,'texture_path'
	,'model'
	,'uv'
	,'tex'
	,'opt_tex'
	,'lod'
	,'z'
	,'collision'
	,'total'
]

def create_table(table_name='',columns=[]):
	exe("CREATE TABLE todo(pk INTEGER PRIMARY KEY, text VARCHAR(25), priority INTEGER, complete BOOLEAN);")

def exe(command='',values=[]):
	connector = sqlite3.connect(path_DB)
	cursor = connector.cursor()
	cursor.execute(command,values)
	result = cursor.fetchall()
	cursor.close()
	connector.commit()
	connector.close()
	return result

def test():
	print exe("select count(*) from sqlite_master where type = 'table' and name = 'ed'")
	

def main():
	#exe("create table test_table('id','var')")
	#exe("insert into test_table values('1', 'python')")
	exe(u"INSERT INTO todo(text,priority,complete) VALUES(?,?,?)",['aaa',3,0])
	exe(u"INSERT INTO todo(text,priority,complete) VALUES(?,?,?)",['Do homework',1,0])
	exe(u"INSERT INTO todo(text,priority,complete) VALUES(?,?,?)",['Learn Objective C',3,0])
	exe(u"INSERT INTO todo(text,priority,complete) VALUES(?,?,?)",['DIGG this tutorial',3,0])

	exe(u"INSERT INTO todo(text,priority,complete) VALUES('Do Computer Science homework',1,0)")
	exe(u"INSERT INTO todo(text,priority,complete) VALUES('Learn Objective C',1,0)")
	exe("INSERT INTO todo(text,priority,complete) VALUES('DIGG this tutorial',2,0)")
	

def viewData():
	connector = sqlite3.connect(path_DB)
	cursor = connector.cursor()

	#cursor.execute("select * from todo order by pk")
	cursor.execute("select text from todo where priority=3")

	result = cursor.fetchall()

	for row in result:
		print "===== hit! ====="
		print row

	cursor.close()
	connector.close()

def LayoutA():
	cmds.frameLayout('sqlite3_test_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='sqlite3_test',cll=True,cl=False)
	cmds.columnLayout('sqlite3_test_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='sqlite3_test',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='create_table',c=lambda *args:create_table())
	cmds.button(l='do',c=lambda *args:main())
	cmds.button(l='viewData',c=lambda *args:viewData())
	cmds.button(l='test',c=lambda *args:test())
	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('sqlite3_test_window',q=True,ex=True):
		cmds.deleteUI('sqlite3_test_window')
	cmds.window('sqlite3_test_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('sqlite3_test_window')
	


