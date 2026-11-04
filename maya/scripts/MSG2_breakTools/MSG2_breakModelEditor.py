# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_breakModelEditor.py
# 説明
#			
#			
# 作成日
#			
########################################


import maya.cmds as cmds
import maya.mel as mel

import s2000_tools.MSG2_breakTools.MSG2_breakNodeUtil as MSG2_breakNodeUtil
reload(MSG2_breakNodeUtil)

#execCheckList
import s2000_tools.MS_lib.MSG2_execCheck as MSG2_execCheck
reload(MSG2_execCheck)


def momsBME_getSceneName():
	return cmds.file(q=True,sceneName=True,shortName=True).replace('.mb','')

#################
# ツリーシェーダー用ユーティリティ
#################
def copyBranchLocatorToChild():
	G2B = cmds.textField('MS_copyToCollision_BranchLocatorName',q=True,tx=True)
	NODES = cmds.ls(sl=True)
	for each in NODES:
		CHILD = cmds.listRelatives(each,c=True,type='transform')
		if CHILD:
			cmds.delete(CHILD)
		DUPED=cmds.duplicate(G2B,rr=True)
		cmds.parent(DUPED,each)




###################################
#ノード名の欠けているナンバリングを取得 (２桁)
###################################
def momsBME_top_md_count(name):
	md_group = cmds.ls('|'+name+'*',type='transform');#中間破壊モデル用グループ取得
	numbers=[]
	i=0
	for i in range(len(md_group)):
		NUM=str(i+1).zfill(2)
		if not cmds.objExists('|'+name+NUM): #無かったらその数字
			return NUM 

	return str(i+2).zfill(2) # 全部あったら追加



#################
# エクスポート用アトリビュートを追加
#################

def momsBME_addAttr(groupName=[]):

	sceneName = momsBME_getSceneName()#シーンの名前

	for each in groupName:
		top_node = cmds.listRelatives(each,p=True)
		type = top_node[0].replace('top_','')

		if not cmds.attributeQuery("export_top",node=each,ex=True): #アトリビュート追加
			cmds.addAttr (each,longName="export_top",at='bool')

		if not cmds.attributeQuery("export_name",node=each,ex=True):
			cmds.addAttr (each,longName="export_name",dt="string")

		if type == "bridge": #アトリビュート編集　橋の場合
			cmds.setAttr(each+'.export_name',sceneName,type="string")
			cmds.setAttr(each+'.export_top',1)

		else: #アトリビュート編集　橋以外
			cmds.setAttr(each+'.export_name',sceneName + "_" + type ,type="string")
			cmds.setAttr(each+'.export_top',1)


#################
# ノードを制作
#################

def momsBME_createGroup(type):
	SCENE_NAME = cmds.file(q=True,sceneName=True,shortName=True)
	if not SCENE_NAME:cmds.error(u"シーン名を取得できませんでした")

	TOP_NAME=''
	if type == "db" :
		if not cmds.objExists("top_db"):
			TOP_NAME = cmds.group(name="top_db",empty=True)
			CROOT = cmds.group(name="root",empty=True,parent=TOP_NAME)
			CCOL = cmds.group(name="col",empty=True,parent=TOP_NAME)
			momsBME_addAttr([CROOT,CCOL])
		else:
			cmds.error("既に同名のグループが存在しているので制作できませんでした")

	if type == "dy" :
		if not cmds.objExists("top_dy"):
			TOP_NAME = cmds.group(name="top_dy",empty=True)
			CROOT = cmds.group(name="root",empty=True,parent=TOP_NAME)
			CCOL = cmds.group(name="col",empty=True,parent=TOP_NAME)
			momsBME_addAttr([CROOT,CCOL])
		else:
			cmds.error("既に同名のグループが存在しているので制作できませんでした")
		
	if type == "bk" :
		if not cmds.objExists("top_bk"):
			TOP_NAME = cmds.group(name="top_bk",empty=True)
			CROOT = cmds.group(name="root",empty=True,parent=TOP_NAME)
			CCOL = cmds.group(name="col",empty=True,parent=TOP_NAME)
			momsBME_addAttr([CROOT,CCOL])
		
		else:
		
			cmds.error("既に同名のグループが存在しているので制作できませんでした")
		
	if type == "md" :
		number_str = momsBME_top_md_count("top_md")#top_mdの欠けている番号を取得
		TOP_NAME = cmds.group(name=("top_md" + number_str),empty=True)
		CROOT = cmds.group(name="root",empty=True,parent=TOP_NAME)
		CCOL = cmds.group(name="col",empty=True,parent=TOP_NAME)
		momsBME_addAttr([CROOT,CCOL])
	'''
	if type == "db_md" :
			md_group= cmds.ls('|top_md*',type='transform') #既に作られているtop_md**のリスト
			if not md_group:cmds.error("中間破壊モデル用グループがありません")
			string db_group[] = momsBME_search_group("top_md[0-9][0-9]_db")#既に作られているtop_md**_dbのリスト
			for(i = 0 i < size(md_group) i++)
			
				if(!stringArrayContains( (md_group[i]+"_db"), db_group) )
				
					TOP_NAME = cmds.group(name=(md_group[i] + "_db"),empty=True
					CROOT = cmds.group(name="root",empty=True,parent=TOP_NAME
					CCOL = cmds.group(name="col",empty=True,parent=TOP_NAME
					momsBME_addAttr([CROOT,CCOL])
				
				else:
				
					print(md_group[i]+"_db"+"は既に存在するのでスキップしました\n")
				
			

	if type ==  "null" :
		string scenename== cmds.momsBME_getSceneName#シーン名
		string md[] = momsBME_search_group("top_md[0-9][0-9]")#既にある中間破壊モデルグループ名
		string md_short
		if(size(md))#mdグループがあった場合
		
			for(i = 0 i < size(md) i++)
			
				md_short = momsBME_getUnderName(md[i])
				string count = momsBME_top_md_count(scenename=+ "_" + md_short+ "_")#欠けてるナンバリング
				count = momsBME_padding(count)
				spaceLocator,p 0 0 0,name=(scenename=+ "_" + md_short + "_" + count)
			
		
		else:#無かった場合
		
			spaceLocator,p 0 0 0,name=(scenename=+ "_md01_01")	
		
	if type == "bridge" :
		if(!cmds.objExists "top_bridge"cmds.)
		
			TOP_NAME = cmds.group(name="top_bridge",empty=True
			CROOT = cmds.group(name="root",empty=True,parent=TOP_NAME
			CCOL = cmds.group(name="col",empty=True,parent=TOP_NAME
			momsBME_addAttr([CROOT,CCOL])
		
		else:
		
			error"既に同名のグループが存在しているので制作できませんでした"
		
	'''
	#MSMOD-----------------------------------
	if type ==  "brk_db" :
		if not cmds.objExists("top_brk_db"):
		
			TOP_NAME = cmds.group(name="top_brk_db",empty=True)
			CROOT = cmds.group(name="root",empty=True,parent=TOP_NAME)
			CCOL = cmds.group(name="col",empty=True,parent=TOP_NAME)
			momsBME_addAttr([CROOT,CCOL])
		
		else:
		
			cmds.error("既に同名のグループが存在しているので制作できませんでした")
		
	if type ==  "brk_bk" :
		if not cmds.objExists("top_brk_bk"):
			TOP_NAME = cmds.group(name="top_brk_bk",empty=True)
			CROOT = cmds.group(name="root",empty=True,parent=TOP_NAME)
			CCOL = cmds.group(name="col",empty=True,parent=TOP_NAME)
			momsBME_addAttr([CROOT,CCOL])
		
		else:
		
			cmds.error("既に同名のグループが存在しているので制作できませんでした")
		
	if type ==  "brk_dy" :
		if not cmds.objExists("top_brk_dy"):
			TOP_NAME = cmds.group(name="top_brk_dy",empty=True)
			CROOT = cmds.group(name="root",empty=True,parent=TOP_NAME)
			CCOL = cmds.group(name="col",empty=True,parent=TOP_NAME)
			momsBME_addAttr([CROOT,CCOL])
		else:
		
			cmds.error("既に同名のグループが存在しているので制作できませんでした")
		
	if type ==  "brk_md" :
		number_str = momsBME_top_md_count("top_md")#top_mdの欠けている番号を取得
		TOP_NAME = cmds.group(name=("top_brk_md" + number_str),empty=True)
		CROOT = cmds.group(name="root",empty=True,parent=TOP_NAME)
		CCOL = cmds.group(name="col",empty=True,parent=TOP_NAME)
		momsBME_addAttr([CROOT,CCOL])

	'''
	if type ==  "brk_db_md" :
			string md_group[] = momsBME_search_group("top_brk_md[0-9][0-9]")#既に作られているtop_brk_md**のリスト
			if(!size(md_group))error"中間破壊モデル用グループがありません"
			string db_group[] = momsBME_search_group("top_brk_md[0-9][0-9]_db")#既に作られているtop_brk_md**_dbのリスト
			for(i = 0 i < size(md_group) i++)
			
				if(!stringArrayContains( (md_group[i]+"_db"), db_group) )
				
					TOP_NAME = cmds.group(name=(md_group[i] + "_db"),empty=True)
					CROOT = cmds.group(name="root",empty=True,parent=TOP_NAME)
					CCOL = cmds.group(name="col",empty=True,parent=TOP_NAME)
					momsBME_addAttr([CROOT,CCOL])
				
				else:
				
					print(md_group[i]+"_db"+"は既に存在するのでスキップしました\n")
				
			
			'''
	return TOP_NAME




def MS_copyToCollision(COM):
	SEL = cmds.ls(sl=True,l=True)
	if not SEL:
		return

	#テンポラリグループ作成
	TEMP_GROUP=cmds.group(name="MS_temp_zzzzz",empty=True)

	#対象トップグループ確認
	if cmds.objExists("top_"+COM):
		#対象トップグループ有り、グループを削除
		SEL=cmds.parent (SEL,TEMP_GROUP)
		cmds.delete ("top_"+COM)

	#グループを作成
	NEWGROUP = momsBME_createGroup(COM)

	#元オブジェクトを複製
	PARENTED_ROOT=cmds.parent(SEL,(NEWGROUP+"|root"))
	cmds.select(PARENTED_ROOT,r=True)

	#元モデルを対応するコリジョングループにコピー
	PARENTED_COL=main()

	cmds.select(PARENTED_COL,r=True)
	for each in PARENTED_COL:
		MSG2_breakNodeUtil.toHavok(each)

	#フリーズ＆リネーム
	SN=cmds.file(q=True,sceneName=True,shortName=True)
	if not SN:
		SN='ms_breakdef'
	else:
		SN=SN.split('.')[0]

	i=1
	for each in PARENTED_ROOT:
		momsBME_freeze(each)
		cmds.rename(SN+'_'+COM+'_'+str(i).zfill(2))
		i+=1

	i=1
	for each in PARENTED_COL:
		momsBME_freeze(each)
		cmds.rename(SN+'_'+COM+'_'+str(i).zfill(2)+'_hkx')
		i+=1

	#コリジョンをHIDE
	cmds.hide (NEWGROUP+"|col")

	#テンポラリグループを削除
	cmds.delete(TEMP_GROUP)


def momsBME_freeze(MODEL=''):
	cmds.select(MODEL,r=True)
	cmds.makeIdentity(apply=True,t=True,r=True,s=True,n=0,pn=1)
	mel.eval('ResetTransformations;')


def main():
	RET=[]

	MSG2_execCheck.execCheckSafe('MS_copyToCollision')#execCheckList
	OBJ=cmds.ls(sl=True,l=True)

	for each in OBJ:
		P = cmds.ls(each,l=True)
		PP=P[0].split('|')[1]
		DUPED=cmds.duplicate(each,n='MS_temp_zzzzz_01')
		#DUPED=cmds.ls(sl=True,l=True)
		#子供を消す
		try:
			cmds.delete(DUPED[1:-1])
		except:
			pass
		PCOL = PP+'|col'
		print DUPED
		PARENTED=cmds.parent(DUPED[0],PCOL)
		PARENTED=cmds.ls(sl=True,l=True)
		RET.extend(PARENTED)
		
	return RET

def LayoutTreeUtil():
	def getBranchNode():
		BranchNode=cmds.ls(sl=True,l=True)
		cmds.textField('MS_copyToCollision_BranchLocatorName',e=True,tx=BranchNode[0])

	cmds.columnLayout('MS_copyToCollision.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='Tree Util',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.textField('MS_copyToCollision_BranchLocatorName',en=False)

	cmds.button(l='get',c=lambda *args:getBranchNode())
	cmds.button(l='do',c=lambda *args:copyBranchLocatorToChild())
	cmds.setParent('..')	


def LayoutA():
	cmds.columnLayout('MS_copyToCollision.py _mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_copyToCollision.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator(h=10)
	cmds.button(l='db',c=lambda *args:MS_copyToCollision('db'))
	cmds.button(l='bk',c=lambda *args:MS_copyToCollision('bk'))
	cmds.button(l='md',c=lambda *args:MS_copyToCollision('md'))
	cmds.button(l='dy',c=lambda *args:MS_copyToCollision('dy'))
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_copyToCollision_window',q=True,ex=True):
		cmds.deleteUI('MS_copyToCollision_window')
	cmds.window('MS_copyToCollision_window',rtf=True,s=True)
	
	LayoutA()
	LayoutTreeUtil()
	cmds.showWindow('MS_copyToCollision_window')
	