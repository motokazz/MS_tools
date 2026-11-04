# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_atgi_send_to_win_run.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import subprocess

#DEFINE
TX,TY,TZ,SP = 0,0,0,-300

#################
# コマンド送信コア
#################

def cmdline(cmdline):
	
	logtex=[]
	
	p=subprocess.Popen(cmdline, shell=True, stdin=subprocess.PIPE,
						 stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
						 )
	(stdouterr, stdin) = (p.stdout, p.stdin)  # 
	print "-" * 80  # 区切り表示(開始)
	while True:
		line = stdouterr.readline()  # 改行を含んで行を読み込む
		if not line:
			break
		logtex.append(line.rstrip())  # 後ろの改行を消して出力
	print "-" * 80  # 区切り表示(終了)
	ret = p.wait()  # 戻り値が入る
	print "Return code: %d" % ret
	
	return logtex



def resetSpacing():
	global TX,TY,TZ,SP
	TX=cmds.floatField('MSG2_atgi_send_to_win_run_ATGIS_X',q=True,v=True)
	TY=cmds.floatField('MSG2_atgi_send_to_win_run_ATGIS_Y',q=True,v=True)
	TZ=cmds.floatField('MSG2_atgi_send_to_win_run_ATGIS_Z',q=True,v=True)
	SP=cmds.floatField('MSG2_atgi_send_to_win_run_ATGIS_SPACE',q=True,v=True)

def spacing():
	global TX,TY,TZ,SP
	SP=cmds.floatField('MSG2_atgi_send_to_win_run_ATGIS_SPACE',q=True,v=True)
	TZ+=SP
	'''
	if abs(TX)>abs(SP*20):
		TX=0
		TZ+=SP
	if abs(TZ)>abs(SP*20):
		resetSpacing()
		return
	'''


# 破壊コマンド送信
def sendBreak_bak(RANGE=30,COUNT=20):
	global TX,TY,TZ
	RANGE=cmds.floatField('MSG2_atgi_send_to_win_run_BreakRange',q=True,v=True)
	COUNT=cmds.intField('MSG2_atgi_send_to_win_run_BreakCount',q=True,v=True)
	COM='D:\\Projects\\Gravite2\\tools\\Supporter\\VS_Gravite2_Utility\\VS_Gravite2_Commander.exe break -range '+str(RANGE)+' -count'+str(COUNT)+' -pos ' +str(TX*0.01)+', ' +str(TY*0.01)+', '+ str(TZ*0.01)+'\n'
	cmdline(COM)

def sendBreak(RANGE=30,COUNT=20):
	global TX,TY,TZ
	RANGE=cmds.floatField('MSG2_atgi_send_to_win_run_BreakRange',q=True,v=True)
	COUNT=cmds.intField('MSG2_atgi_send_to_win_run_BreakCount',q=True,v=True)
	COM='D:\\Projects\\Gravite2\\tools\\Supporter\\VS_Gravite2_Utility\\VS_Gravite2_Commander.exe break -range '+str(RANGE)+' -count'+str(COUNT)+' -r ' +str(TX*0.01)+', ' +str(TY*0.01)+', '+ str(TZ*0.01)+'\n'
	cmdline(COM)

#D:\Projects\Gravite2\tools\Supporter\VS_Gravite2_Utility\VS_Gravite2_Commander.exe create –name barrel_kk_01 –localpos 0, 2, 0
#D:\Projects\Gravite2\tools\Supporter\VS_Gravite2_Utility\VS_Gravite2_Commander.exe create –name barrel_kk_01 –r 0, 2, 0
#D:\Projects\Gravite2\tools\Supporter\VS_Gravite2_Utility\VS_Gravite2_Commander.exe create –name barrel_kk_01 –relation 0, 2, 0



# リストからのコマンド
def sendAtgiFromList():
	global TX,TY,TZ,SP
	ATGIS=cmds.scrollField('MSG2_atgi_send_to_win_run_ATGIS',q=True,tx=True).split()
	for each in ATGIS:
		sendAtgi(each,TX,TY,TZ)
		spacing()
	resetSpacing()

def sendListExec():
	global TX,TY,TZ,SP
	ATGINAME=cmds.textScrollList('MSG2_atgi_send_to_win_run_ATGIS_sl',q=True,selectItem=True)
	sendAtgi(ATGINAME[0],TX,TY,TZ)
	#spacing()

def sendList(LIST=[]):
	LIST=cmds.scrollField('MSG2_atgi_send_to_win_run_ATGIS',q=True,tx=True).split()
	cmds.textScrollList('MSG2_atgi_send_to_win_run_ATGIS_sl',e=True,ra=True)
	cmds.textScrollList('MSG2_atgi_send_to_win_run_ATGIS_sl'
		,e=True
		,append=LIST
		,allowMultiSelection=False
		,doubleClickCommand=lambda *args:sendListExec()
		)

# シーンに配置されているAtgiを送信

def sendAtgi_abs(ATGI_NAME,TX=0,TY=0,TZ=0):
		COM='D:\\Projects\\Gravite2\\tools\\Supporter\\VS_Gravite2_Utility\\VS_Gravite2_Commander.exe create -name '+ATGI_NAME+' -pos ' +str(TX*0.01)+', ' +str(TY*0.01)+', '+ str(TZ*0.01)+'\n'
		cmdline(COM)

def sendAtgi(ATGI_NAME,TX=0,TY=0,TZ=0):
		COM='D:\\Projects\\Gravite2\\tools\\Supporter\\VS_Gravite2_Utility\\VS_Gravite2_Commander.exe create -name '+ATGI_NAME+' -r ' +str(TX*0.01)+', ' +str(TY*0.01)+', '+ str(TZ*0.01)+'\n'
		cmdline(COM)


def main():
	GALN = cmds.ls(sl=True,dag=True,type='GraviteAtgiLocatorNode',l=True)
	for each in GALN:
		ATGI_NAME = cmds.getAttr(each+'.atgiFilename').split('/')[-1].split('.')[0]
		T=cmds.xform(cmds.listRelatives(each,p=True,f=True),q=True,t=True,ws=True)
		sendAtgi_abs(ATGI_NAME,T[0],T[1],T[2])



def LayoutA():
	cmds.columnLayout('MSG2_atgi_send_to_win_run.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_atgi_send_to_win_run.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l=u'選択AtgiをWINRUNに出力',c=lambda *args:main())

	cmds.rowLayout(nc=6,cw6=[20,80,20,80,20,80])
	cmds.text(l='X')
	cmds.floatField('MSG2_atgi_send_to_win_run_ATGIS_X',pre=2,v=0)
	cmds.text(l='Y')
	cmds.floatField('MSG2_atgi_send_to_win_run_ATGIS_Y',pre=2,v=0)
	cmds.text(l='Z')
	cmds.floatField('MSG2_atgi_send_to_win_run_ATGIS_Z',pre=2,v=300)
	cmds.setParent('..')
	cmds.rowLayout(nc=6,cw6=[20,80,20,80,20,80])
	cmds.text(l=u'間隔')
	cmds.floatField('MSG2_atgi_send_to_win_run_ATGIS_SPACE',pre=2,v=300)
	cmds.button(l=u'ポジションのリセット',c=lambda *args:resetSpacing())
	cmds.setParent('..')
	
	#

	cmds.rowLayout(nc=6,cw6=[40,80,40,80,20,80])
	cmds.text(l=u'破壊範囲')
	cmds.floatField('MSG2_atgi_send_to_win_run_BreakRange',pre=2,v=30)
	cmds.text(l=u'破壊数')
	cmds.intField('MSG2_atgi_send_to_win_run_BreakCount',v=10)
	cmds.button(l=u'壊す',bgc=[0.8,0.6,0.5],c=lambda *args:sendBreak())
	cmds.setParent('..')

	cmds.separator()

	cmds.scrollField('MSG2_atgi_send_to_win_run_ATGIS')


	cmds.button(l=u'リストのAtgiをWINRUNに出力',c=lambda *args:sendAtgiFromList())

	cmds.button(l=u'↓',c=lambda *args:sendList())
	cmds.textScrollList('MSG2_atgi_send_to_win_run_ATGIS_sl',h=200)
	cmds.setParent('..')

def UI():
	if cmds.window('MSG2_atgi_send_to_win_run_window',q=True,ex=True):
		cmds.deleteUI('MSG2_atgi_send_to_win_run_window')
	cmds.window('MSG2_atgi_send_to_win_run_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MSG2_atgi_send_to_win_run_window')

	resetSpacing()
	