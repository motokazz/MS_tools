# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_dynaGareki
# 説明
#			
# 作成日
#			
########################################

import maya.cmds as cmds

def deleteSelectRigidBodies(NODES):
	for EACH in NODES:
		LEAVES=cmds.listRelatives(EACH,type='rigidBody')
		cmds.delete(LEAVES)
	
def centerResetter(NODES,MODE=False):
	
	for EACH in NODES:
		if not cmds.nodeType(cmds.listRelatives(EACH,s=True)):#TOROロケーター対策
			continue
			
		if MODE:#MODE=Trueはピボット位置をセンターにする。
			cmds.xform(EACH,cp=True)
			
		#トランスフォームノードにコネクション（アニメーション）があったら処理しない
		obj_a_tx=EACH+'.tx'
		obj_a_ty=EACH+'.ty'
		obj_a_tz=EACH+'.tz'
		
		obj_a_rptx=EACH+'.transMinusRotatePivotX'
		obj_a_rpty=EACH+'.transMinusRotatePivotY'
		obj_a_rptz=EACH+'.transMinusRotatePivotZ'
		
		orgx=cmds.getAttr(obj_a_tx)
		orgy=cmds.getAttr(obj_a_ty)
		orgz=cmds.getAttr(obj_a_tz)
		
		flpx=cmds.getAttr(obj_a_rptx)
		flpy=cmds.getAttr(obj_a_rpty)
		flpz=cmds.getAttr(obj_a_rptz)
		
		cmds.setAttr(obj_a_tx,flpx)
		cmds.setAttr(obj_a_ty,flpy)
		cmds.setAttr(obj_a_tz,flpz)
		
		cmds.makeIdentity(EACH,apply=True,t=1,r=0,s=0,n=0)
		
		cmds.setAttr(obj_a_tx,(orgx-flpx))
		cmds.setAttr(obj_a_ty,(orgy-flpy))
		cmds.setAttr(obj_a_tz,(orgz-flpz))

def bbObj(OBJ):
	#ポリゴンバウンディングボックス面積
	BB=cmds.xform(OBJ,q=True,bb=True)
	RET=((BB[3]-BB[0])*(BB[4]-BB[1])*(BB[5]-BB[2]))
	return RET
	
def bbSort(LIST):#頂点に隣接するフェースを面積比較してソート済みリスト作成
	RET=[]
	SRC=[]
	for EACH in LIST:
		AREA=bbObj(EACH)
		SRC.append([EACH,AREA])
	RETSORT=sorted(SRC,key=lambda x:x[1],reverse=False)
	for EACH in RETSORT:
		RET.append(EACH[0])
	return RET
	
	
def selectBBSorted():
	OBJ=cmds.ls(sl=True)
	SORTED=bbSort(OBJ)
	cmds.select(SORTED,r=True)
	
def sortedRename():
	NAME=cmds.textFieldGrp('ALIGNRENAME',q=True,tx=True)
	LIST=cmds.ls(sl=True)
	NUM=0
	for EACH in LIST:
		cmds.rename(EACH,('%s_%03d' % (NAME,NUM)))
		NUM+=1
	
	
	
def dynagarekiCore():
	
	fGetName=cmds.textFieldGrp('fGetName',q=True,tx=True).split()
	sGetName=cmds.textFieldGrp('sGetName',q=True,tx=True).split()
	
	
	MCHECK=cmds.checkBox('Keep',q=True,v=True)
	FRAME=cmds.intSliderGrp('FRAME',q=True,v=True)
	SKIP=cmds.intSliderGrp('SKIP',q=True,v=True)
	GRAV=cmds.floatSliderGrp('GRAV',q=True,v=True)
	
	TESSELATIONFACTOR=cmds.intSliderGrp('TESSELATIONFACTOR',q=True,v=True)
	MASS=cmds.floatSliderGrp('MASS',q=True,v=True)
	STATICFRICTION=cmds.floatSliderGrp('STATICFRICTION',q=True,v=True)
	DYNAMICFRICTION=cmds.floatSliderGrp('DYNAMICFRICTION',q=True,v=True)
	BOUNCINESS=cmds.floatSliderGrp('BOUNCINESS',q=True,v=True)
	DAMPING=cmds.floatSliderGrp('DAMPING',q=True,v=True)
	LOCKCENTEROFMATH=cmds.checkBox('LOCKCENTEROFMATH',q=True,v=True)
	
	newname='temp'
	cmds.currentTime(0)
	
	#ダイナミクスの種作成
	GRAVITY_NODE=cmds.gravity(pos=(0,0,0),m=GRAV,att=0,dx=0,dy=-1,dz=0,mxd=-1,vsh='none',vex=0,vof=(0,0,0),vsw=360,tsr=0.5)
	centerResetter(fGetName+sGetName)
	
	for PASSIVE in fGetName:
		#ベースpassive設定
		cmds.rigidBody(
			PASSIVE
			,passive=True
			,layer=0
			,mass=MASS
			,staticFriction=STATICFRICTION
			,dynamicFriction=DYNAMICFRICTION
			,bounciness=BOUNCINESS
			,damping=DAMPING
			,tesselationFactor=TESSELATIONFACTOR
			,lockCenterOfMass=LOCKCENTEROFMATH
			,iv=(0,0,0)
			,iav=(0,0,0)
			,c=0
			,pc=0
			,i=(0,0,0)
			,imp=(0,0,0)
			,si=(0,0,0)
			,standInObject='none'
			)
	
	for ACTIVE in sGetName:
		#active化
		cmds.rigidBody(
			ACTIVE
			,active=True
			,layer=0
			,mass=MASS
			,staticFriction=STATICFRICTION
			,dynamicFriction=DYNAMICFRICTION
			,bounciness=BOUNCINESS
			,damping=DAMPING
			,tesselationFactor=TESSELATIONFACTOR
			,lockCenterOfMass=LOCKCENTEROFMATH
			,iv=(0,0,0)
			,iav=(0,0,0)
			,cache=False
			,particleCollision=False
			,i=(0,0,0)
			,imp=(0,0,0)
			,si=(0,0,0)
			,standInObject='none'
		)
		
		cmds.connectDynamic(ACTIVE,f=GRAVITY_NODE)
		
		#アニメーション再生
		t_FRAME=FRAME/SKIP
		J=0
		for J in range(t_FRAME):
			cmds.currentTime(J*SKIP)
		
		
		if not MCHECK:
			#cmds.select(ACTIVE,r=True)
			deleteSelectRigidBodies([ACTIVE])
			
			#passive化
			cmds.rigidBody(
				ACTIVE
				,passive=True
				,layer=0
				,mass=0
				,staticFriction=STATICFRICTION
				,dynamicFriction=DYNAMICFRICTION
				,bounciness=BOUNCINESS
				,damping=DAMPING
				,tesselationFactor=TESSELATIONFACTOR
				,lockCenterOfMass=LOCKCENTEROFMATH
				,iv=(0,0,0)
				,iav=(0,0,0)
				,c=0
				,pc=0
				,i=(0,0,0)
				,imp=(0,0,0)
				,si=(0,0,0)
				,standInObject='none'
				)
		
	#rigidBody消去
	deleteSelectRigidBodies(fGetName+sGetName)
	
	cmds.delete(GRAVITY_NODE)
	


#ClickPssiveList-------------------------------------------
def ClickPassiveList():
	 selectSet =' '.join(cmds.ls(l=True,sl=True))
	 cmds.textFieldGrp('fGetName',e=True,tx=selectSet)


#ClickActiveList-------------------------------------------
def ClickActiveList():
	 selectSet =' '.join(cmds.ls(l=True,sl=True))
	 cmds.textFieldGrp('sGetName',e=True,tx=selectSet)


def layoutA():
	cmds.frameLayout('MS_dynaGareki_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l=u'MS_PYTHON_FORMAT',cll=True,cl=False)
	cmds.columnLayout()
	
	
	cmds.rowLayout(numberOfColumns=2,cat=(1,"left",5),columnWidth2=(130,210))
	cmds.button(al="center",l="SelectPassiveObjects",w=120,c=lambda *args:ClickPassiveList())
	cmds.textFieldGrp('fGetName',en=0,cw=(1,160))
	cmds.setParent('..')
	
	cmds.rowLayout(numberOfColumns=2,cat=(1,"left",5),columnWidth2=(130,210))
	cmds.button(al="center",l="SelectActiveObjects",w=120,c=lambda *args:ClickActiveList())
	cmds.textFieldGrp('sGetName',en=0,cw=(1,160))
	cmds.setParent('..')
	
	cmds.separator(w=200)
	
	cmds.intSliderGrp('FRAME',l="FRAME",field=True,min=1,max=1000,v=300)
	cmds.intSliderGrp('SKIP',l="SKIP",field=True,min=1,max=100,v=10)
	cmds.floatSliderGrp('GRAV',l="GRAV",field=True,min=1,max=10000,v=9.8)
	
	cmds.separator(w=200)
	
	cmds.intSliderGrp('TESSELATIONFACTOR',l='TESSELATIONFACTOR',field=True,min=0,max=1000,v=200,ann=u'リジッド ボディ サーフェスのテッセレーション係数を設定します。 範囲: >= 10 デフォルト: 200')
	cmds.floatSliderGrp('MASS',l='MASS',field=True,min=0,max=10000,v=3000,ann=u'リジッド ボディの質量を設定します。 範囲: > 0 デフォルト: 1.0')
	cmds.floatSliderGrp('STATICFRICTION',l='STATICFRICTION',field=True,min=0,max=1,v=1,ann=u'リジッド ボディの静止摩擦を設定します。 範囲: 0.0 - 1.0 デフォルト: 0.2')
	cmds.floatSliderGrp('DYNAMICFRICTION',l='DYNAMICFRICTION',field=True,min=0,max=1,v=1,ann=u'リジッド ボディの動摩擦を設定します。 範囲: 0.0 - 1.0 デフォルト: 0.2')
	cmds.floatSliderGrp('BOUNCINESS',l='BOUNCINESS',field=True,min=0,max=1,v=0,ann=u'リジッド ボディの回復（弾性）を設定します。 範囲: 0.0 - 2.0 デフォルト: 0.6')
	cmds.floatSliderGrp('DAMPING',l='DAMPING',field=True,min=0,max=1,v=0.0,ann=u'リジッド ボディのダンピング値を設定します。 範囲: -2.0 - 2.0 デフォルト: 0')
	cmds.checkBox('LOCKCENTEROFMATH',label='LOCKCENTEROFMATH',al='center',recomputeSize=0,v=0,width=128,ann=u'リジッド ボディの重心をロックします。 デフォルト: オフ')
	
	cmds.separator(w=200)
	
	cmds.checkBox('Keep',al='center',recomputeSize=0,v=0,label="keepRigidBodies",width=128)
	cmds.button(l='dynaGareki',w=200,command=lambda *args:dynagarekiCore())
	
	cmds.separator(w=200)
	cmds.button(l=u'バウンディングボックス順ソート選択',w=200,command=lambda *args:selectBBSorted())
	cmds.textFieldGrp('ALIGNRENAME',l=u'リネーム',cw=(1,160))
	cmds.button(l=u'選択順リネーム',w=200,command=lambda *args:sortedRename())
	
	cmds.setParent('..')
	cmds.setParent('..')



def UI():
	if cmds.window('MS_dynaGareki_main_window',q=True,ex=True):
		cmds.deleteUI('MS_dynaGareki_main_window')
	cmds.window('MS_dynaGareki_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MS_dynaGareki_main_window')
	


