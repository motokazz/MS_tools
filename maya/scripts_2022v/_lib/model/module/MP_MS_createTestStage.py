# _*_coding:utf-8_*_
########################################
# ファイル名
#			MP_MS_createTestStage
# 説明
#			
# 作成日\n#			
########################################

import maya.cmds as cmds
import os
import shutil


##### エクスプローラーで開く系 #####
	
def OPEN_EXPLOROR(DIR,MODE=''):
	DIR=DIR.replace('/','\\')
	
	if DIR[-1]=='\\':#行末がバックスラッシュの場合
		WINDOWS_PATH=DIR
	elif MODE=='file':#
		WINDOWS_PATH=DIR
	else :#ファイルパスの場合
		WINDOWS_PATH='\\'.join(DIR.split('\\')[:-1])
	
	os.popen('explorer "%s"' % WINDOWS_PATH)
	
##### I/O 
	
def save(PATH,ROW):
	f=open(PATH,'w')
	f.write(ROW)
	f.close()
	
def load(FILE_PATH):
	f=open(FILE_PATH)
	DATA=[]
	for ROW in f:
		DATA.append(ROW)
	f.close()
	return DATA
	
##### サンプルステージリスト #####
	
def tempStagePath():
	return 'd:/Mproject/graphic/gimmick/misc/samplestages/'
	
def gimmickSampleStagePath():
	return 'd:/Mproject/mgamedata/models/test/map_gimmicktest/map_ms_gim_work.toro'
	
def gimmickSampleStageSkyPath():
	return 'd:/Mproject/mgamedata/models/test/map_gimmicktest/map_ms_gim_work_sky.toro'
	
def gimmickSampleStageIblPath():
	return 'd:/Mproject/mgamedata/models/test/map_gimmicktest/map_ms_gim_work_ibl.toro'
	
def gimmickSampleStageColPath():
	return 'd:/Mproject/mgamedata/models/test/map_gimmicktest/map_ms_gim_work_col.toro'
	
	
	
	
def copyGimmickSampleStage():
	stage=cmds.textScrollList('MP_MS_createTestStage_textScrollList',q=True,si=True)
	print tempStagePath(),stage
	if not stage:
		return
	elif '_col' in stage[0]:
		shutil.copyfile(tempStagePath()+stage[0],gimmickSampleStageColPath())
	elif '_ibl' in stage[0]:
		shutil.copyfile(tempStagePath()+stage[0],gimmickSampleStageIblPath())
	elif '_sky' in stage[0]:
		shutil.copyfile(tempStagePath()+stage[0],gimmickSampleStageSkyPath())
	else:
		shutil.copyfile(tempStagePath()+stage[0],gimmickSampleStagePath())
	cmds.confirmDialog(m='testStageConfiged %s > gimmickSampleStage'%stage[0])
	
def createStageList():
	if cmds.textScrollList('MP_MS_createTestStage_textScrollList',q=True,ex=True):
		cmds.deleteUI('MP_MS_createTestStage_textScrollList')
	cmds.textScrollList('MP_MS_createTestStage_textScrollList',p='MP_MS_createTestStage_stageList',ams=False)
	stageList=os.listdir(tempStagePath())
	for each in stageList:
		cmds.textScrollList('MP_MS_createTestStage_textScrollList',e=True,a=each,dcc=lambda *args:copyGimmickSampleStage())
	
	
def layoutSampleStages():
	cmds.frameLayout(l='STAGES',w=220,cll=True,cl=False,ann=u'ギミックサンプルステージを選択します\nサンプルステージのパス：\n%s'%tempStagePath())
	cmds.columnLayout('MP_MS_createTestStage_stageList')
	cmds.button(bgc=[0.6,0.8,0.9],l='openFolder',w=220,c=lambda *args:OPEN_EXPLOROR(tempStagePath()))
	cmds.setParent('..')
	cmds.setParent('..')
	
#####エネミーセットアップ
	
def layoutEnemySetup():
	cmds.frameLayout(l='enemySetup',w=220,cll=True,cl=False,ann=u'エネミーのセットアップをします')
	cmds.columnLayout()
	cmds.checkBox('createEnemy',v=False)
	
	#
	cmds.rowLayout(nc=2)
	cmds.text(l='EnemyID',w=80)
	cmds.textField('MP_MS_createTestStage_EnemyID',tx='2041')
	cmds.setParent('..')
	#
	cmds.rowLayout(nc=2)
	cmds.text(l='StateID',w=80)
	cmds.textField('MP_MS_createTestStage_StateID',tx='0')
	cmds.setParent('..')
	#
	cmds.setParent('..')
	cmds.setParent('..')
	
	
	
	
	
	
##### DBからの情報取得
	
def ditectGimmickNameFromID(ID):#ギミックIDを指定してシンボル名を検索
	FILE_PATH='D:/Mproject/mgamedata/db/filelist/122_list_gimmick.csv'
	
	DATA=load(FILE_PATH)
	NAME=''
	NUM=0
	for EACH in DATA:
		if '#gimmik,'+ID.encode('utf-8') in EACH:
			break
		NUM+=1
		
	for X in range(NUM,0,-1):
		if '#name' in DATA[X]:
			NAME=DATA[X].split(',')[1]
			break
		
	return NAME
	
def ditectEnemyNameFromID(ID):#エネミーIDを指定してシンボル名を検索
	FILE_PATH='D:/Mproject/mgamedata/db/filelist/121_list_enemy.csv'
	
	DATA=load(FILE_PATH)
	NAME=''
	NUM=0
	for EACH in DATA:
		if '#enemy,'+ID.encode('utf-8') in EACH:
			break
		if '#vehicle,'+ID.encode('utf-8') in EACH:
			break
		NUM+=1
		
	for X in range(NUM,0,-1):
		if '#name' in DATA[X]:
			NAME=DATA[X].split(',')[1]
			break
		
	return NAME
	
	
	
##### ポジション取得
	
def getPos(NUM):
	print NUM
	OBJ=cmds.ls(typ='transform',sl=True)
	if not OBJ:
		return
	POS=cmds.xform(OBJ[0],q=True,t=True,ws=True)
	cmds.floatField('gimmickPosX%s'%NUM,e=True,v=POS[0])
	cmds.floatField('gimmickPosY%s'%NUM,e=True,v=POS[1])
	cmds.floatField('gimmickPosZ%s'%NUM,e=True,v=POS[2])
	
	ROT=cmds.xform(OBJ[0],q=True,ro=True,ws=True)
	cmds.floatField('gimmickPosRX%s'%NUM,e=True,v=ROT[0])
	cmds.floatField('gimmickPosRY%s'%NUM,e=True,v=ROT[1])
	cmds.floatField('gimmickPosRZ%s'%NUM,e=True,v=ROT[2])
	
##### UI
	
def layout_setTestStegeScript():
	cmds.frameLayout('MP_MS_createTestStage_frameLayout',w=200,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MP_MS_createTestStage',cll=True,cl=False)
	cmds.columnLayout()
	#
	cmds.rowLayout(nc=2)
	cmds.text(l='GimmickID',w=80)
	cmds.textField('MP_MS_createTestStage_ID',tx='')
	cmds.setParent('..')
	
	#ギミックポジション
		
	cmds.frameLayout(l='GimmickPosition',w=220,cll=True,cl=True,ann=u'ギミックのポジションを編集できます')
	cmds.columnLayout('MP_MS_createTestStagePOS')
	DEF_POS=[
		[0.0,0.0,0.0,0.0,0.0,0.0]
		,[50.0,0.0,0.0,0.0,0.0,0.0]
		,[-50.0,0.0,0.0,0.0,0.0,0.0]
		]
	NUM=0
	for POS in DEF_POS:
		cmds.rowLayout(nc=2)
		#
		cmds.columnLayout()
		#
		cmds.rowLayout(nc=4)
		cmds.text(l='POS%s'%NUM)
		cmds.floatField('gimmickPosX%s'%NUM,w=50,v=POS[0])
		cmds.floatField('gimmickPosY%s'%NUM,w=50,v=POS[1])
		cmds.floatField('gimmickPosZ%s'%NUM,w=50,v=POS[2])
		cmds.setParent('..')
		#
		cmds.rowLayout(nc=4)
		cmds.text(l='ROT%s'%NUM)
		cmds.floatField('gimmickPosRX%s'%NUM,w=50,v=POS[3])
		cmds.floatField('gimmickPosRY%s'%NUM,w=50,v=POS[4])
		cmds.floatField('gimmickPosRZ%s'%NUM,w=50,v=POS[5])
		cmds.setParent('..')
		#
		cmds.setParent('..')
		#
		cmds.button(l='get',c='MP_MS_createTestStage.getPos(%s)'%NUM,ann=u'選択オブジェクトの移動値を取得')
		cmds.setParent('..')
		NUM+=1
	cmds.setParent('..')
	#
	cmds.setParent('..')
	
	cmds.separator(w=200)
	
	#CHUNKMAN
		
	cmds.rowLayout(nc=2)
	cmds.text(l='CunkmanParts',w=80)
	cmds.intField('MP_MS_createTestStage_PARTS_COUNT',v=300,ann=u'チャンクマンのパーツ数を編集できます')
	cmds.setParent('..')
	#
	cmds.rowLayout(nc=8,ann=u'チャンクマンのポジションを編集できます')
	cmds.text(l='Cpos')
	cmds.floatField('chunkmanPosX',w=50,v=0.0)
	cmds.floatField('chunkmanPosY',w=50,v=5.0)
	cmds.floatField('chunkmanPosZ',w=50,v=100.0)
	cmds.floatField('chunkmanPosRY',w=50,v=-180.0)
	cmds.setParent('..')
		
		
	#エネミーセットアップ
		
	layoutEnemySetup()
	
	#ステージセレクト
		
	layoutSampleStages()
	createStageList()
	
	#
	cmds.rowLayout(nc=2)
	cmds.button(w=190,h=30,l=u'テストステージスクリプト作成',bgc=[0.8,0.8,0.8],c=lambda *args:pre_setTestStegeScript())
	cmds.button(w=20,bgc=[0.6,0.8,0.9],label='e',c=lambda *args:OPEN_EXPLOROR('d:/Mproject/mgamedata/scripts/bg/misc/map_ms_gim_work.cxx',MODE='file'))
	cmds.setParent('..')
	cmds.setParent('..')
	cmds.setParent('..')
	try:
		cmds.textField('MP_MS_createTestStage_ID',e=True,tx=cmds.optionVar(q='MP_MS_GIMMICK_ID'))
	except:
		return
	
def pre_setTestStegeScript():
	
	#ステージID取得
	ID=cmds.textField('MP_MS_createTestStage_ID',q=True,tx=True)
	#ポジションリスト取得
	GIMMICK_POS=[]
	LOS=cmds.columnLayout('MP_MS_createTestStagePOS',q=True,nch=True)
	for NUM in range(0,LOS):
		X=cmds.floatField('gimmickPosX%s'%str(NUM),q=True,v=True)
		Y=cmds.floatField('gimmickPosY%s'%str(NUM),q=True,v=True)
		Z=cmds.floatField('gimmickPosZ%s'%str(NUM),q=True,v=True)
		RX=cmds.floatField('gimmickPosRX%s'%str(NUM),q=True,v=True)
		RY=cmds.floatField('gimmickPosRY%s'%str(NUM),q=True,v=True)
		RZ=cmds.floatField('gimmickPosRZ%s'%str(NUM),q=True,v=True)
		GIMMICK_POS.append([X,Y,Z,RX,RY,RZ])
	#
	PARTS_COUNT=cmds.intField('MP_MS_createTestStage_PARTS_COUNT',q=True,v=True)
	CHAR_POS=[
		cmds.floatField('chunkmanPosX',q=True,v=True)
		,cmds.floatField('chunkmanPosY',q=True,v=True)
		,cmds.floatField('chunkmanPosZ',q=True,v=True)
		,cmds.floatField('chunkmanPosRY',q=True,v=True)
		]
	#エネミー作るか？
		
	enemyEnable=cmds.checkBox('createEnemy',q=True,v=True)
		
	setTestStegeScript([ID],PARTS_COUNT,CHAR_POS,GIMMICK_POS,ENEMY=enemyEnable)
	
	
	
##### スクリプト作成コア
	
def enemySetup(ENEMY_ID='2041'):
	ENEMY_ID=cmds.textField('MP_MS_createTestStage_EnemyID',q=True,tx=True)
	STATE_ID=cmds.textField('MP_MS_createTestStage_StateID',q=True,tx=True)
	COMMAND=''
	COMMAND+= u'//リスト指定\n'
	COMMAND+= u'int DEF_ENEMY_LIST_ID=121;\n'
	COMMAND+= u'string DEF_ENEMY_NAME0="%s";\n'%ditectEnemyNameFromID(ENEMY_ID)
	#COMMAND+= u'string DEF_ENEMY_NAME0="%s";\n'%'gobn06'
	COMMAND+= u'//キャラ指定\n'
	COMMAND+= u'int DEF_ENEMY_ID0=%s;\n'%ENEMY_ID
	COMMAND+= u'string DEF_FLAG0="P_WpnR";\n'
	COMMAND+= u'int DEF_STATE_ID0=%s;\n'%STATE_ID
	
	COMMAND+= u'//拡張フラグ\n'
	COMMAND+= u'int ENABLE_FLAG_A0=1;\n'
	COMMAND+= u'string DEF_FLAG_A0="P_Act";\n'
	COMMAND+= u'int DEF_STATE_ID_A0=1;\n'
	
	return COMMAND
	
def enemyPos():
	COMMAND=''
	ENEMY_POS=[[0.0,5.0,-100.0,0.0,0.0,0.0]]
	for EACH in ENEMY_POS:
		COMMAND+=u'	CreateEnemys(DEF_ENEMY_ID%s,DEF_ENEMY_NAME%s,%s,%s,%s,%s,%s,%s);\n'%("0","0",EACH[0],EACH[1],EACH[2],EACH[3],EACH[4],EACH[5])
	
	return COMMAND
	
	
	
	
def setTestStegeScript(IDS=[],PARTS_COUNT=300,CHAR_POS=[0.0,0.0,0.0,0.0],GIMMICK_POS=[[0.0,0.0,0.0,0.0,0.0,0.0]],ENEMY=True):#テストステージのCXXを作成
	
	#DEF_CHAR_NAME=ditectGimmickNameFromID(ID)
	
	FILE_PATH='D:/Mproject/mgamedata/db/filelist/122_list_gimmick.csv'
	
	DATA=load(FILE_PATH)
	
	COMMAND=''
	###HEADER
		
	COMMAND+=HEADER
	
	#ギミック初期設定
		
	NUM=0
	for ID in IDS:
		DEF_CHAR_NAME=ditectGimmickNameFromID(ID)
		COMMAND+= u'int DEF_CHAR_ID%s=%s;\n'%(str(NUM),ID)
		COMMAND+= u'string DEF_CHAR_NAME%s="%s";\n'%(str(NUM),DEF_CHAR_NAME)
		NUM+=1
		
	#エネミー初期設定
		
	if ENEMY:
		COMMAND+=enemySetup()
		COMMAND+=BODY_B
		
		
	#ギミック座標指定
		
	COMMAND+=u'//ギミック表示座標指定\n'
	
	COMMAND+=u'int preCerateChar(){\n'
	
	for EACH in GIMMICK_POS:
		COMMAND+=u'	CreateChar(DEF_CHAR_ID%s,DEF_CHAR_NAME%s,%s,%s,%s,%s,%s,%s);\n'%("0","0",EACH[0],EACH[1],EACH[2],EACH[3],EACH[4],EACH[5])
	#エネミー座標指定
		
	if ENEMY:
		COMMAND+=enemyPos()
	COMMAND+=u'	return(1);\n'
	COMMAND+=u'}\n'
	
	#チャンクマン設定
		
	COMMAND+=u'/////////////////////\n'
	COMMAND+=u'//チャンクマン設定\n'
	COMMAND+=u'/////////////////////\n'
	COMMAND+=u'\n'
	COMMAND+=u'//パーツ数\n'
	COMMAND+=u'int PARTS_COUNT=%s;\n'%PARTS_COUNT
	COMMAND+=u'\n'
	COMMAND+=u'//初期登場位置\n'
	COMMAND+=u'float KNACK_POSX=%s;\n'%CHAR_POS[0]
	COMMAND+=u'float KNACK_POSY=%s;\n'%CHAR_POS[1]
	COMMAND+=u'float KNACK_POSZ=%s;\n'%CHAR_POS[2]
	COMMAND+=u'float KNACK_ROT=%s;\n'%CHAR_POS[3]
	
	
	###BODY
		
	COMMAND+=BODY_A
	
	#ギミックロード
		
	NUM=0
	for ID in IDS:
		COMMAND+=u'	LoadListAsync(DEF_CHAR_LIST_ID,DEF_CHAR_NAME%s);\n'%str(NUM)
		NUM+=1
	
	#エネミーロード
		
	if ENEMY:#for Enemy
		COMMAND+=u'	LoadListAsync(DEF_ENEMY_LIST_ID,DEF_ENEMY_NAME0);\n'
	
	###FOOTER
		
	COMMAND+=FOOTER
	
	CXX_PATH='d:/Mproject/mgamedata/scripts/bg/misc/map_ms_gim_work.cxx'
	save(CXX_PATH,COMMAND.encode('utf-8'))
	
	cmds.confirmDialog(bgc=[1,1,1],m='testStageCreated:\n'+CXX_PATH)
	
#DATAPART#
	
HEADER=u'''
////////////////////////////////////////////////////////
// 平面だけのシンプルなステージ
#include <scripts/common/stage.hxx>
#include <scripts/bg/stfw.hxx>
#include <scripts/bg/misc/map_ms_gim_work_cam.hxx>
#include <scripts/bg/misc/map_ms_gim_work_lightnum.hxx>

////////////////////////////////////////////////////////

//ステージ設定
int DEF_BG_LIST_ID=119;
string DEF_STAGE_NAME="map_ms_gim_work";

//リスト指定
int DEF_CHAR_LIST_ID=122;

/////////////////////
//ギミック設定
/////////////////////
//D:\Mproject\mgamedata\db\filelist\122_list_gimmick.csv

//ギミック定義
'''

BODY_A=u'''

int CreateChar(int DEF_CHAR_ID,string DEF_CHAR_NAME,float TX,float TY,float TZ,float RX,float RY,float RZ)
{
//キャラ生む
	vector VEC_A=ftov(TX,TY,TZ,0.0);
	vector VEC_B=ftov(RX,RY,RZ,0.0);
	
	int id=CreateEnemy(DEF_CHAR_ID,VEC_A,VEC_B,DEF_CHAR_NAME);
	
	SetEnemyPos(id,VEC_A);
	
	return(1);
	
}


//ファイルを読み込みます
int OnPreload(int version)
{
	if(!StFw_OnPreload(version)){ return(INT_FALSE); }

	//プリロード
	PreloadListAsync(DEF_BG_LIST_ID,DEF_STAGE_NAME);//無理に変える必要ないかも

	return(INT_TRUE);
}

////////////////////////////////////////////////////////
//ゲームシステム初期化後に呼ばれます.
int OnInit(int version)
{
	if(!StFw_OnInit(version)){ return(INT_FALSE); }

	//ロード
	LoadListAsync(DEF_BG_LIST_ID,DEF_STAGE_NAME);//無理に変える必要ないかも
'''

BODY_B=u'''
int CreateEnemys(int DEF_ENEMY_ID,string DEF_ENEMY_NAME,float TX,float TY,float TZ,float RX,float RY,float RZ)
{
//エネミー生む
	vector VEC_A=ftov(TX,TY,TZ,0.0);
	vector VEC_B=ftov(RX,RY,RZ,0.0);
	
	int id=CreateEnemy(DEF_ENEMY_ID,VEC_A,VEC_B,DEF_ENEMY_NAME);
	SetFlag(id, DEF_FLAG0, DEF_STATE_ID0);
	if (ENABLE_FLAG_A0){
		SetFlag(id,DEF_FLAG_A0,DEF_STATE_ID_A0);
		SetTimerCallBack("SetHpOne("+id+")",1.0);	//矢徳が一時的に追加
	}
	SetEnemyPos(id,VEC_A);
	
	return(1);
	
}
'''


FOOTER=u'''

	//Player
	SetPlayerInitPartsCount(PARTS_COUNT);	//初期パーツ数
	SetPlayerInitGems(100);			//初期クリスタル数
	SetPlayerInitPosRot(KNACK_POSX,KNACK_POSY,KNACK_POSZ,KNACK_ROT);	//初期位置
	
	//
	//ここに初期化時に処理するものを記述します
	//
	LoadLayoutEntityAsync();
	//開始
	SetupEntityAsync();
	StartGameAsync();

	return(INT_TRUE);
}


int GameOver()
{
	if(!StFw_GameOver()){ return(INT_FALSE); }

	//
	//ここにゲームオーバー時に処理するものを記述します
	//

	return(INT_TRUE);
}

int Start()
{
	//ここにゲーム開始時に処理するものを記述します
	//
	NicoNico("Start Stage");
	preCerateChar();
	return(INT_TRUE);
}

//Seg変更時に呼ばれます
int StFwCb_SegChanged(string segName){
	return(INT_TRUE);
}
int StFwCb_OnTerm()
{
	return(INT_TRUE)
}

//GameOverから復帰時に呼ばれます
int StFwCb_Restart()
{
	preCerateChar();
	return(INT_TRUE);
}

int OnAI()
{
	if(!StFw_OnAI()){ return(INT_FALSE); }

	//
	//ここに毎フレーム処理するものを記述します
	//
	if(GetKeyboard("N"))
	{
	}

	return(INT_TRUE);
}

int StFwCb_DoMsg(int id, int msg)
{
	switch(msg)
	{//メッセージによる分岐
	case MSG_GIMMICK_END:
		ReceiveMessageInt();
		NicoNico("Stage: MSG_GIMMICK_END "+id);
		break;
	default:
		ReceiveMessageInt();
		NicoNico("Stage: Unknown msg "+itos(msg)+" from UID:"+itos(id),1.0,1.0,0.0,1.0);
		break;
	};

	return(INT_TRUE);
}

int StFwCb_OnIGCEnd(string igc)
{
	return(INT_TRUE);
}
'''





