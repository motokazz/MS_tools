# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_lemon_P4Lib.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import subprocess

UserName = 'motokazu.sakai'
ServerAddress = 'ssl:54.250.7.52:1666'
CliantName_LemonMaster='motokazu.sakai_Lemon_master_6458'
CliantName_LemonArtist='motokazu.sakai_20205843N_3359'

#Perforceコマンドの行頭を作る
P4_HEAD_COMMAND_LemonMaser = 'p4 -p %s -c %s -u %s'%(ServerAddress,CliantName_LemonMaster,UserName)


#################
# P4
#################
def cmdline(cmdline):
	
	logtex=[]
	
	p=subprocess.Popen(cmdline, shell=True, stdin=subprocess.PIPE,
						 stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
						 )
	(stdouterr, stdin) = (p.stdout, p.stdin)  # 
	#print ("-" * 80)  # 区切り表示(開始)
	while True:
		line = stdouterr.readline()  # 改行を含んで行を読み込む
		if not line:
			break
		logtex.append(line.rstrip())  # 後ろの改行を消して出力
	#print ("-" * 80)  # 区切り表示(終了)
	ret = p.wait()  # 戻り値が入る
	#print ("Return code: %d" % ret)
	
	return logtex

def P4Info():#ユーザー名返す
	command='p4 info'
	line=cmdline(command)
	for each in line:
		if 'User name:' in each:
			name=each.replace('User name:','')
			name=name.replace(' ','')
			name=name.replace('\r','')
			name=name.replace('\n','')
			name=name.replace('\t','')
	#return name
	return UserName

def P4headRev(PATH=''):
	#最新リビジョンチェック
	if not PATH:
		return
	msg=cmdline(P4_HEAD_COMMAND_LemonMaser + " fstat -T \"headRev\" %s"%PATH)

	if not msg[0]:# add状態で空の文字列が帰ってきた。
		return False

	rev=msg[0].split()[-1]
	if 'no such file(s)' in msg[0]:#存在しないファイルはFalseを返す。
		rev=False

	return rev
	
def P4AddMarking(PATH=''):
	try:
		cmdline(P4_HEAD_COMMAND_LemonMaser + " add -d -f default %s"%PATH)
		return True
	except:
		return False

def P4DeleteMarking(PATH=''):
	try:
		cmdline(P4_HEAD_COMMAND_LemonMaser + " delete %s"%PATH)
		return True
	except:
		return False

def P4Status(PATH=''):
	#ローカルファイルかどうかチェック
	if not P4headRev(PATH):
		return 'localFile'

	#チェックアウト情報
	line=cmdline(P4_HEAD_COMMAND_LemonMaser + ' opened -a %s'%PATH)
	print(line)
	for eachline in line:
		if  UserName in eachline:
			return 'checkout'
		elif '@' in eachline:
			return 'locked'
		else:
			return 'notcheckout'




def P4CheckOut(PATHLIST=[],ENABLE_DIALOG=True):
	checkFlag=True #正常にチェックアウト出来ないファイルがあったらFalse
	for each in PATHLIST:
		STRING=each.replace(' ','')+'...'
		#P4Check
		P4Check=P4Status(each)
		#print (P4Check)
		if P4Check=='localFile':#ローカルにしか存在しないファイル
			continue

		elif P4Check=='checkout': #チェックアウトされている
			continue

		elif P4Check=='locked': #誰かがロックしている
			if ENABLE_DIALOG:
				cmds.confirmDialog(m='file is locked',button=['confirm'],defaultButton='confirm')
			checkFlag=False
			continue

		else: #チェックアウトされていない
			if ENABLE_DIALOG:
				DS=cmds.confirmDialog(m='%s\nDo you want P4 CheckOut?'%each,button=['yes','No'],defaultButton='yes',cancelButton='No',dismissString='No')
				if DS=='No':
					checkFlag=False
					continue
			#else:ENABLE_DIALOGがFalseの場合、強制チェックアウト


		#sync
		command=P4_HEAD_COMMAND_LemonMaser + ' sync %s'%STRING
		line=cmdline(command)
		print (line)
		#lock
		command=P4_HEAD_COMMAND_LemonMaser + ' lock %s'%STRING
		line=cmdline(command)
		print (line)
		#edit
		command=P4_HEAD_COMMAND_LemonMaser + ' edit -c default %s'%STRING
		line=cmdline(command)
		print (line)
	#finish
	#print '---p4checkout complete---'
	
	return checkFlag
	#P4Status()
	
