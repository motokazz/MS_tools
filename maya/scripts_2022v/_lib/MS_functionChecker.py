# _*_coding:utf-8_*_

import maya.cmds as cmds
import re

import ui.MS_window as MS_window
reload(MS_window)

msw=MS_window.main()
testWindow=MS_window.main('MS_functionChecker_testWindow')

mainLayout=msw.mainLayout

class option:
	command=''
	optionName=''
	arg=''


def getControlFlags():#コントロールのフラグを返す['フラグ名','変数型']
	mayaCommands=cmds.textField('MS_functionChecker_command',q=True,tx=True)
	Ret=[]
	try:
		helpStr=cmds.help(mayaCommands)
	except:
		print 'Error'
		return
	helpStr =	helpStr.replace('-','')
	helpStr =	helpStr.replace('Float Float Float','Float_Float_Float')
	spRet=helpStr.split('Flags:')
	g=re.split('\n+',spRet[1])
	for each in g:
		temp=re.split('\s+',each)

		if len(temp)>2:
			if temp[2]=='command':
				continue
			Ret.append(temp)
	return Ret

def getDefaultFlagValue():#デフォルト値取得
	Ret=[]
	gcf=getControlFlags()
	mayaCommands=cmds.textField('MS_functionChecker_command',q=True,tx=True)
	def layoutA():
		eval('cmds.'+mayaCommands+'("MS_textCommandControl")')
	#一回ダミーウインドウに配置したものを取得
	testWindow.layoutA=layoutA
	testWindow.hiddenUI()
	for each in gcf:
		try:
			temp=eval('cmds.'+mayaCommands+'("MS_textCommandControl",q=True,'+each[1]+'=True)')
			Ret.append([each[2],each[3],temp])
		except:
			Ret.append([each[2],'Error','Error'])
			continue
	testWindow.close()
	return Ret

def cc(mayaCommands,flagname,value):#フラグコントローラー用チェンジコマンド
	def layout0():
		baseCommand='cmds.'+mayaCommands+'("MS_textCommandControl")'
		eval(baseCommand)

	def layoutA():
		gcf=getDefaultFlagValue()
		ccom=''
		for each in gcf:
			if each[2]=='Error':
				continue
			try:
				temp= queryControl(each[0])
				if temp and not temp=='""' and not each[0]=='parent':
					ccom+=',%s=%s'%(each[0],temp)
			except:
				print each[0],'error'
				continue

		baseCommand='cmds.'+mayaCommands+'("MS_textCommandControl"'+ccom+')'

		
		print (baseCommand)
		if cmds.window('testtesttest',q=True,ex=True):
			cmds.deleteUI('testtesttest')
		cmds.window('testtesttest',rtf=True,s=True,w=200,h=400)
		cmds.columnLayout()
		eval(baseCommand)
		cmds.setParent('..')
		cmds.showWindow('testtesttest')
	layoutA()
	#testWindow.UI()
	#testWindow.layoutA=layoutA
	#print testWindow.mainLayout
	#testWindow.layoutA=layoutA
	
	#testWindow.reflesh()

def queryControl(controlName):#フラグコントローラー：コマンドのフラグ一覧をコントローラーとしてレイアウト

	if cmds.textField(controlName,ex=True):
		return '"'+cmds.textField(controlName,q=True,tx=True)+'"'

	elif cmds.checkBox(controlName,ex=True):
		return cmds.checkBox(controlName,q=True,v=True)

	elif cmds.intField(controlName,ex=True):
		return cmds.intField(controlName,q=True,v=True)

	elif cmds.floatField(controlName,ex=True):
		return cmds.floatField(controlName,q=True,v=True)

	else:
		return


def getControl():#フラグコントローラー：コマンドのフラグ一覧をコントローラーとしてレイアウト
	gcf=getDefaultFlagValue()
	mayaCommands=cmds.textField('MS_functionChecker_command',q=True,tx=True)
	cmds.scrollLayout(p='MS_functionChecker_commandControl')
	for each in gcf:

		if len(each)<2:
			continue
		cmds.rowLayout(nc=2,cw2=[150,200])
		cmds.text(l=each[0])

		if each[1]=='String':
			cmds.textField(each[0],tx=each[2],cc=lambda *args:cc(mayaCommands,each[0],each[2]))
		elif each[1]=='Float_Float_Float':
			cmds.rowLayout(nc=3)
			cmds.floatField(each[0]+'X')
			cmds.floatField(each[0]+'Y')
			cmds.floatField(each[0]+'Z')
			cmds.setParent('..')
		elif each[1]=='Script':
			cmds.textField(each[0],tx=each[2],cc=lambda *args:cc(mayaCommands,each[0],each[2]))
		elif each[1]=='on|off':
			cmds.checkBox(each[0],v=each[2],cc=lambda *args:cc(mayaCommands,each[0],each[2]))
		elif each[1]=='Int':
			cmds.intField(each[0],v=each[2],cc=lambda *args:cc(mayaCommands,each[0],each[2]))
		elif each[1]=='Float':
			cmds.floatField(each[0],v=each[2],cc=lambda *args:cc(mayaCommands,each[0],each[2]))
		else:
			cmds.text(each[1])
		#
		cmds.setParent('..')
	cmds.setParent('..')


def layoutCommand():#コマンドのフラグ設定用レイアウト表示

	if cmds.layout('MS_functionChecker_commandControl',q=True,ex=True):
		cmds.deleteUI('MS_functionChecker_commandControl')
	cmds.columnLayout('MS_functionChecker_commandControl',p='MS_functionChecker_sub',adj=True)
	getControl()
	cmds.setParent('..')


def layoutA():
	#main
	cmds.frameLayout('MS_functionChecker_main',w=200,p=mainLayout)
	cmds.textField('MS_functionChecker_command',cc=lambda *args:layoutCommand())
	cmds.button('layoutCommand',c=lambda args:layoutCommand())
	cmds.button('getDefaultFlagValue',c=lambda args:getDefaultFlagValue())
	cmds.button('checklist',c=lambda args:getControlFlags())
	cmds.setParent('..')

	#sub
	cmds.frameLayout('MS_functionChecker_sub',w=200,p=mainLayout)
	cmds.columnLayout('MS_functionChecker_commandControl',adj=True)
	cmds.text('commandControl')
	cmds.setParent('..')
	cmds.setParent('..')


msw.layoutA=layoutA

msw.UI()



