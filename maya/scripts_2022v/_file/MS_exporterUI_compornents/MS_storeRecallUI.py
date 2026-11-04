# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_storeRecall
# 説明
#		UI情報をoptionVarに格納、呼び出し、削除を行う
#		例）
#		MS_storeRecall.store(parentUI)
#		MS_storeRecall.recall(parentUI)	
# 作成日
#			
########################################

import maya.cmds as cmds

########################
#初期設定
########################

Prefix='MS_'	#Prefixつきの名前で登録

########################
#基本機能
########################

def listControls(parentUI):#parentUIの子供にある指定コントロールをリスト化
	#戻り値：('コントロール名','コントロール種別',値)
	childrenArray=[parentUI]#まずはメインコントロールをリストに入れる。こいつを使って再起処理。
	controlLists=[]#フィルタかける前のテンポラリコントロールリスト。コントロール全部リスト化されてる。
	Result=[]#フィルタかけた後の最終結果。登録したいコントロールのみを刈り込んだリスト。

	while(childrenArray):
		#コントロールリスト作成
		cca=[]
		for each in childrenArray:
			if cmds.layout(each,ex=True):
				try:
					cca=cmds.layout(each,q=True,ca=True,fpn=True)
					controlLists+=cca
				except:
					pass


		childrenArray=cca
		#print (controlLists)
	#コントロールリストのフィルタリング
	for each in controlLists:
		Qc = queryControl(each)
		if Qc:
			Result.append(Qc)
	return Result

def listControlsQuick(parentUI,iterV=1):#parentUIの子供にある指定コントロールをリスト化
	#戻り値：('コントロール名','コントロール種別',値)
	childrenArray=[parentUI]#まずはメインコントロールをリストに入れる。こいつを使って再起処理。
	controlLists=[]#フィルタかける前のテンポラリコントロールリスト。コントロール全部リスト化されてる。
	Result=[]#フィルタかけた後の最終結果。登録したいコントロールのみを刈り込んだリスト。
	i=0
	while(iterV>i):
		#コントロールリスト作成
		cca=[]
		for each in childrenArray:
			if cmds.layout(each,ex=True):
				try:
					cca=cmds.layout(each,q=True,ca=True,fpn=True)
					controlLists+=cca
				except:
					pass


		childrenArray=cca
		i+=1
		#print (controlLists)
	return controlLists

def addCC(parentUI,controlName='',quickMode=False):#チェンジコマンドにストア関数を仕込む
	#ストア関数を指定
	if quickMode:
		func=lambda *args:storeQuick(parentUI)
	else:
		func=lambda *args:store(parentUI)
	
	#control
	if cmds.checkBox(controlName,ex=True):
		if '_ac_' in controlName:#例外コマンド
			cmds.checkBox(controlName,e=True,cc=lambda *args:activeControlCheckBox(parentUI,controlName))
		else:
			cmds.checkBox(controlName,e=True,cc=lambda *args:store(parentUI))

	if cmds.floatField(controlName,ex=True):cmds.floatField(controlName,e=True,cc=func)
	if cmds.floatFieldGrp(controlName,ex=True):cmds.floatFieldGrp(controlName,e=True,cc=func)
	if cmds.floatSlider(controlName,ex=True):cmds.floatSlider(controlName,e=True,cc=func)
	if cmds.floatSliderButtonGrp(controlName,ex=True):cmds.floatSliderButtonGrp(controlName,e=True,cc=func)
	if cmds.floatSliderGrp(controlName,ex=True):cmds.floatSliderGrp(controlName,e=True,cc=func)
	if cmds.intField(controlName,ex=True):cmds.intField(controlName,e=True,cc=func)
	if cmds.intFieldGrp(controlName,ex=True):cmds.intFieldGrp(controlName,e=True,cc=func)
	if cmds.intSlider(controlName,ex=True):cmds.intSlider(controlName,e=True,cc=func)
	if cmds.intSliderGrp(controlName,ex=True):cmds.intSliderGrp(controlName,cc=func)
	if cmds.textField(controlName,ex=True):cmds.textField(controlName,e=True,cc=func)
	if cmds.textFieldButtonGrp(controlName,ex=True):cmds.textFieldButtonGrp(controlName,e=True,cc=func)
	if cmds.textFieldGrp(controlName,ex=True):cmds.textFieldGrp(controlName,e=True,cc=func)
	if cmds.textScrollList(controlName,ex=True):cmds.textScrollList(controlName,e=True,cc=func)
	
	#layout
	if cmds.frameLayout(controlName,ex=True):cmds.frameLayout(controlName,e=True,ec=func,cc=func)
	if cmds.tabLayout(controlName,ex=True):cmds.tabLayout(controlName,e=True,cc=func)
	if cmds.shelfTabLayout(controlName,ex=True):cmds.shelfTabLayout(controlName,e=True,cc=func)

def queryControl(controlName=''):#コントロールの設定値を取得する
	if cmds.checkBox(controlName,ex=True):return controlName,'checkBox', cmds.checkBox(controlName,q=True,v=True)
	if cmds.floatField(controlName,ex=True):return controlName,'floatField',cmds.floatField(controlName,q=True,v=True)
	if cmds.floatFieldGrp(controlName,ex=True):return controlName,'floatFieldGrp',cmds.floatFieldGrp(controlName,q=True,v=True)
	if cmds.floatSlider(controlName,ex=True):return controlName,'floatSlider',cmds.floatSlider(controlName,q=True,v=True)
	if cmds.floatSliderButtonGrp(controlName,ex=True):return controlName,'floatSliderButtonGrp',cmds.floatSliderButtonGrp(controlName,q=True,v=True)
	if cmds.floatSliderGrp(controlName,ex=True):return controlName,'floatSliderGrp',cmds.floatSliderGrp(controlName,q=True,v=True)
	if cmds.intField(controlName,ex=True):return controlName,'intField',cmds.intField(controlName,q=True,v=True)
	if cmds.intFieldGrp(controlName,ex=True):return controlName,'intFieldGrp',cmds.intFieldGrp(controlName,q=True,v=True)
	if cmds.intSlider(controlName,ex=True):return controlName,'intSlider',cmds.intSlider(controlName,q=True,v=True)
	if cmds.intSliderGrp(controlName,ex=True):return controlName,'intSliderGrp',cmds.intSliderGrp(controlName,q=True,v=True)
	if cmds.textField(controlName,ex=True):return controlName,'textField',cmds.textField(controlName,q=True,tx=True)
	if cmds.textFieldButtonGrp(controlName,ex=True):return controlName,'textFieldButtonGrp',cmds.textFieldButtonGrp(controlName,q=True,v=True)
	if cmds.textFieldGrp(controlName,ex=True):return controlName,'textFieldGrp',cmds.textFieldGrp(controlName,q=True,v=True)
	if cmds.textScrollList(controlName,ex=True):return controlName,'textScrollList',cmds.textScrollList(controlName,q=True,v=True)
	if cmds.radioCollection(controlName,ex=True):return controlName,'radioCollection',cmds.radioCollection(controlName,q=True,sl=True)
	if cmds.radioButton(controlName,ex=True):return controlName,'radioButton',cmds.radioButton(controlName,q=True,sl=True)

	#layout
	if cmds.frameLayout(controlName,ex=True):return controlName,'frameLayout',cmds.frameLayout(controlName,q=True,cl=True)
	if cmds.tabLayout(controlName,ex=True):return controlName,'tabLayout',cmds.tabLayout(controlName,q=True,selectTab=True)
	if cmds.shelfTabLayout(controlName,ex=True):return controlName,'shelfTabLayout',cmds.shelfTabLayout(controlName,q=True,selectTab=True)

def editControl(controlName='',value=''):#リコール時にコントロールの値を書き換える
	#boolをキャスト
	if value=='True':value=True
	if value=='False':value=False

	if cmds.checkBox(controlName,ex=True):cmds.checkBox(controlName,e=True,v=value)
	if '_ac_' in controlName:#例外コマンド
		activeControlCheckBox('',controlName)

	if cmds.floatField(controlName,ex=True):cmds.floatField(controlName,e=True,v=float(value))
	if cmds.floatFieldGrp(controlName,ex=True):cmds.floatFieldGrp(controlName,e=True,v=float(value))
	if cmds.floatSlider(controlName,ex=True):cmds.floatSlider(controlName,e=True,v=float(value))
	if cmds.floatSliderButtonGrp(controlName,ex=True):cmds.floatSliderButtonGrp(controlName,e=True,v=float(value))
	if cmds.floatSliderGrp(controlName,ex=True):cmds.floatSliderGrp(controlName,e=True,v=float(value))
	if cmds.intField(controlName,ex=True):cmds.intField(controlName,e=True,v=int(value))
	if cmds.intFieldGrp(controlName,ex=True):cmds.intFieldGrp(controlName,e=True,v=int(value))
	if cmds.intSlider(controlName,ex=True):cmds.intSlider(controlName,e=True,v=int(value))
	if cmds.intSliderGrp(controlName,ex=True):cmds.intSliderGrp(controlName,e=True,v=int(value))
	if cmds.textField(controlName,ex=True):cmds.textField(controlName,e=True,tx=value)
	if cmds.textFieldButtonGrp(controlName,ex=True):cmds.textFieldButtonGrp(controlName,e=True,v=value)
	if cmds.textFieldGrp(controlName,ex=True):cmds.textFieldGrp(controlName,e=True,v=value)
	if cmds.textScrollList(controlName,ex=True):cmds.textScrollList(controlName,e=True,v=int(value))
	if cmds.radioCollection(controlName,ex=True):cmds.radioCollection(controlName,e=True,sl=value)
	if cmds.radioButton(controlName,ex=True):cmds.radioButton(controlName,e=True,sl=value)
	#layout
	if cmds.frameLayout(controlName,ex=True):cmds.frameLayout(controlName,e=True,cl=value)
	if cmds.tabLayout(controlName,ex=True):cmds.tabLayout(controlName,e=True,selectTab=value)
	if cmds.shelfTabLayout(controlName,ex=True):cmds.shelfTabLayout(controlName,e=True,selectTab=value)

########################
#その他の機能

def activeControlCheckBox(parentUI='',controlName=''):#チェックボックス連動コントロール設定
	#コントロール名に'_ac_'が含まれているときに続くコントロールのアクティブ状況を切り替える
	#例）checkBox('testCheckBox_ac_testTextField',...) : checkBoxのON/OFFでtestTextFieldのアクティブフラグ（en/enabele）を書き換える
	str=controlName.split('_ac_')
	Check=cmds.checkBox(controlName,q=True,v=True)
	cmds.control(str[1],e=True,en=Check)
	if parentUI:
		store(parentUI)


########################
#コアコマンド
########################

#高速ストア（指定レイアウトの子供のみ）
def ccOnQuick(parentUI,iterV=1):#子供だけにストアコマンド追加
	Qc=listControlsQuick(parentUI,iterV)
	print (Qc)
	for Each in Qc:
		addCC(parentUI,Each,quickMode=False)
	
def storeQuick(parentUI,iterV=1):#UI名を直接指定してストアする
	OptionVarName=Prefix+parentUI
	cca=listControlsQuick(parentUI,iterV)
	Ret=[]
	for each in cca:
		temp=queryControl(each)
		str=';'.join(temp)
		Ret.append(str)

	Retur='<>'.join(Ret)
	cmds.optionVar(stringValue=[OptionVarName,Retur])

#完全ストア（指定レイアウトの子供以下すべて）
def ccOn(parentUI):#子供以下のccコマンド付加可能なコントロールにccコマンドをつける
	Qc=listControls(parentUI)
	for Each in Qc:
		addCC(parentUI,Each[0])


def store(parentUI):#子供以下のUI情報全部ストアする。コントロール直接指定するとそれだけストアできるはず。
	try:
		OptionVarName=Prefix+parentUI	#Prefixつきの名前で登録
		Qc=listControls(parentUI)
		Ret=[]
		for each in Qc:
			temp=[]
			for item in each:
				temp.append('%s' % item)
			str=';'.join(temp)
			Ret.append(str)
		Retur='<>'.join(Ret)
		#
		cmds.optionVar(stringValue=[OptionVarName,Retur])
	except:
		print ('MS_storeRecallUI error : optionVar store error ! : control name = [%s] ' % parentUI)

def recall(parentUI):#子供以下のUI情報を全部リコールする
	try:
		OptionVarName=Prefix+parentUI	#Prefixつきの名前で登録
		Ov=''
		if cmds.optionVar(exists=OptionVarName):
			Ov=cmds.optionVar(q=OptionVarName)
		Sov=Ov.split('<>')

		for Each in Sov:
			try:
				SSov=Each.split(';')
				editControl(SSov[0],SSov[2])
			except:
				print ('MS_storeRecallUI error : optionVar recall error ! : control name = [%s|%s] ' % (parentUI,SSov[0]))

	except:
		print ('MS_storeRecallUI error : optionVar recall error ! : control name = [%s] ' % parentUI)

