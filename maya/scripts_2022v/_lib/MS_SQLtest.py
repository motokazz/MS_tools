# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_SQLtest
# 説明
#			
# 作成日
#			
########################################

import maya.cmds as cmds

import sqlite3

#CONNECTOR=sqlite3.connect(path_DB)
path_DB='d:/work/test.db'
	
def do():
	CONNECTOR=sqlite3.connect(path_DB)
	cur = CONNECTOR.cursor()
	cur.execute( "select * from test_table" )
	for row in cur:
		print row
	cur.close()
	
	
	cur.execute( "select * from test_table" )
	print cur.fetchall()
	cur.close()
	
	cur.execute( "select * from test_table" )
	print cur.fetchmany(2)
	cur.close()
	
	
	CONNECTOR.row_factory = sqlite3.Row
	cur = CONNECTOR.cursor()
	cur.execute( "select * from test_table" )
	
	for row in cur:
		print str(row['date'])
	cur.close()
	
	
	
	CONNECTOR.close()
	
	
def listRow():
	KEY=cmds.textField('MS_SQLtest_textField_a',q=True,tx=True)
	con=sqlite3.connect(path_DB)
	con.row_factory = sqlite3.Row
	cur = con.cursor()
	cur.execute( "select * from test_table" )
	print 'key : '+KEY
	for row in cur:
		print str(row[str(KEY)])
	cur.close()
	
	con.close()
	
	
def listAll():
	KEY=cmds.textField('MS_SQLtest_textField_a',q=True,tx=True)
	VAR=cmds.textField('MS_SQLtest_textField_b',q=True,tx=True)
	CONNECTOR=sqlite3.connect(path_DB)
	cur = CONNECTOR.cursor()
	cur.execute( "select %s from test_table where date='%s'" % (KEY,VAR))
	print cur.fetchall()
	cur.close()
	CONNECTOR.close()
	
	
def insert():
	CONNECTOR=sqlite3.connect(path_DB)
	S1=	cmds.textField('MS_SQLtest_textField_a',q=True,tx=True)
	S2=	cmds.textField('MS_SQLtest_textField_b',q=True,tx=True)
	sql='''insert into test_table values('%s','%s')''' % (str(S1),str(S2))
	CONNECTOR.execute(sql)
	CONNECTOR.commit()
	CONNECTOR.close()
	
def create():
	CONNECTOR=sqlite3.connect(path_DB)
	sql='''create table test_table('date','time')'''
	CONNECTOR.execute(sql)
	CONNECTOR.commit()
	CONNECTOR.close()
	
def connect():
	CONNECTOR=sqlite3.connect(path_DB)
	return CONNECTOR
	
def close():
	CONNECTOR=sqlite3.connect(path_DB)
	CONNECTOR.close()
	
def layoutA():
	cmds.frameLayout('MS_SQLtest_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l=u'MS_SQLtest',cll=True,cl=False)
	cmds.columnLayout()
	
	cmds.text(l='MS_SQLtest')
	cmds.textField('MS_SQLtest_textField_a',w=150,tx='')
	cmds.textField('MS_SQLtest_textField_b',w=150,tx='')
	cmds.intField('MS_SQLtest_floatField_a',w=150,v=0)
	
	cmds.button(w=150,l=u'do',c=lambda *args:do())
	cmds.button(w=150,l=u'insert',c=lambda *args:insert())
	cmds.button(w=150,l=u'create',c=lambda *args:create())
	cmds.button(w=150,l=u'close',c=lambda *args:close())
	cmds.button(w=150,l=u'listAll(textA)',c=lambda *args:listAll())
	cmds.button(w=150,l=u'listRow(textA)',c=lambda *args:listRow())
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_SQLtest_main_window',q=True,ex=True):
		cmds.deleteUI('MS_SQLtest_main_window')
	cmds.window('MS_SQLtest_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MS_SQLtest_main_window')
	


