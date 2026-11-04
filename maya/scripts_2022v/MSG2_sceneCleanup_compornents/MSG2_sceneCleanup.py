# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_sceneCleanup
# 説明
#			シーンの中をチェックしておかしな設定や異常なオブジェクト等を検査、修正するツール
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel

import os

import s2000_tools.MSG2_sceneCleanup_compornents.MSG2_loadPlugin as MSG2_loadPlugin
reload(MSG2_loadPlugin)

import s2000_tools.MSG2_sceneCleanup_compornents.MS_nodeCompare as MS_nodeCompare
reload(MS_nodeCompare)

import s2000_tools.MSG2_sceneCleanup_compornents.MS_resetPivot as MS_resetPivot
reload(MS_resetPivot)

#execCheckList
import s2000_tools.MS_lib.MSG2_execCheck as MSG2_execCheck
reload(MSG2_execCheck)
MSG2_execCheck.execCheckSafe('MSG2_sceneCleanup.py')

#pluginLoad
MSG2_loadPlugin.main()
	
def resetPivot():
	TOP_NODES=cmds.ls(assemblies=True)
	cmds.select(TOP_NODES,r=True)
	MS_resetPivot.reset_root()
	
##### メッシュのシェーダーノードのネームスペース削除 from 武人さん #####
def deleteAllNameSpace(a=''):
	#cmds.select(cmds.ls())
	sl=cmds.ls()
	max=len(sl)
	for i in range(max):
		a = sl.pop()
		if a.find("|") != -1:
			name=a.split('|')[-1]
		else:
			name = a
		if a.find(':') != -1:
			buffer=a.split(':')
			newname=buffer[-1]
			try: 
				new=cmds.rename(a,newname)
			except:
				pass
		else:
			new=a
	return 

def nameCheck():
	# check invailed node name
	RET=''
	deleteAllNameSpace()
	
	OBJS=cmds.ls(type='transform')
	SP_NAME=['obj_','col_','phy_','brk_','dsy_']
	
	for EACH in OBJS:
		for EACH_SP_NAME in SP_NAME:
			if EACH in EACH_SP_NAME:
				RET+='warning:Invaild animation object found = %s\n'%EACH
	return RET
	
def UNIQUE(LIST):
	#リストから重複要素を取り除く。
	return sorted(set(LIST),key=LIST.index)
	
def multipleNameCheck():
	RET=''
	NEW=[]
	OBJ=cmds.ls()
	for EACH in OBJ:
		NEW.append(EACH.split('|')[-1])
		
	NEWU=UNIQUE(NEW)
	RENAME_ENABLE=False
	CONFIRM=True
	for EACH in NEWU:
		nodes=cmds.ls(EACH,l=True)
		if len(nodes)>1:
			RET+='warning: Multiple object name found =%s * %s \n' % (EACH,len(nodes))
			#リネーム確認ダイアログ
			if CONFIRM:
				DS=cmds.confirmDialog(m='MultipleNameFond\n'+EACH+'\n resolve?',button=['Yes','No'],defaultButton='yes',cancelButton='No',dismissString='No')
				if not DS=='No':
					RENAME_ENABLE=True
				CONFIRM=False#一回しか確認はしない
			#リネーム処理
			if RENAME_ENABLE:
				RET+=resolveMultipleName(EACH)
	return RET
	
def resolveMultipleName(NAME):
	RET=''
	nodes=cmds.ls(NAME,l=True)
	if len(nodes)<2:
		return
	num=1
	nodes.pop(-1)
	for each in nodes:
		cmds.rename(each,NAME+str(num))
		RET+=('MultipleName resolved ='+each.replace('|','_')+' > '+NAME+str(num)+'\n')
		num+=1
	return RET
	
def replaceExceptEmptyNodes():
	RET=''
	#例外エンプティグループ処理
	EX_NODES=[#例外エンプティグループリスト
		'tgt_pt',
		'drop_pt'
		]
	
	for EACH in EX_NODES:#例外エンプティグループ置き換え
		if not cmds.objExists(EACH):
			continue
		NODES=cmds.ls(EACH,type='transform')
		
		#locatorノードのチェック
		
		for NODE in NODES:
			SHAPE=cmds.listRelatives(NODE,s=True,f=True)
			if SHAPE:
				if cmds.nodeType(SHAPE[0])=='locator':
					continue
				
			PARENT_NODE=cmds.listRelatives(EACH,p=True,f=True)
			LOC=cmds.spaceLocator()
			
			if PARENT_NODE:
				LOC_FP=cmds.parent(LOC[0],PARENT_NODE)
			
			TX=cmds.getAttr('%s.tx'%EACH)
			TY=cmds.getAttr('%s.ty'%EACH)
			TZ=cmds.getAttr('%s.tz'%EACH)
			RX=cmds.getAttr('%s.rx'%EACH)
			RY=cmds.getAttr('%s.ry'%EACH)
			RZ=cmds.getAttr('%s.rz'%EACH)
			SX=cmds.getAttr('%s.sx'%EACH)
			SY=cmds.getAttr('%s.sy'%EACH)
			SZ=cmds.getAttr('%s.sz'%EACH)
			VIS=cmds.getAttr('%s.visibility'%EACH)
			
			cmds.setAttr('%s.tx'%LOC_FP[0],TX)
			cmds.setAttr('%s.ty'%LOC_FP[0],TY)
			cmds.setAttr('%s.tz'%LOC_FP[0],TZ)
			cmds.setAttr('%s.rx'%LOC_FP[0],RX)
			cmds.setAttr('%s.ry'%LOC_FP[0],RY)
			cmds.setAttr('%s.rz'%LOC_FP[0],RZ)
			cmds.setAttr('%s.sx'%LOC_FP[0],SX)
			cmds.setAttr('%s.sy'%LOC_FP[0],SY)
			cmds.setAttr('%s.sz'%LOC_FP[0],SZ)
			cmds.setAttr('%s.visibility'%LOC_FP[0],VIS)
			
			cmds.delete(EACH)
			cmds.rename(LOC_FP[0],EACH)
			RET+='replace exception node  to locator: %s \n'%EACH
		
	return RET
	
def time30fps():
	CTU=cmds.currentUnit(q=True,time=True)
	cmds.currentUnit(time='ntsc',updateAnimation=True)
	if CTU=='ntsc':
		return 'TimeSetting=OK'
	else:
		return 'TimeSetting=Changed to NTSC'
		
def optimize():
	#remove unnesecary nodes

	MELCOM='''
		{
		source "cleanUpScene.mel";
		deleteUnusedNurbsSurfaces();
		deleteEmptyGroups();
		deleteEmptyLayers("Display");
		deleteEmptyLayers("Render");
		deleteUnusedConstraints;
		deleteUnusedPairBlends;
		deleteUnusedSets;
		deleteUnusedExpressions;
		//deleteUnusedInUnusedHierarchy;
		deleteUnknownNodes;
		}
		'''
	mel.eval(MELCOM)
	
def deleteConstructionHystory():
	#delete construction hystory
	JNT=cmds.ls(type='joint')
	if JNT:
		return 'warning: joint node found! constructionHistory is not deleted.'
	else:
		cmds.delete(all=True,ch=True)
		return 'constructionHistory is deleted.'

def deleteUnusedMaterials():
	mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')
	return 'execute deleteUnusedMaterials'
	
def addMotionLength():
	RET=''
	NODES=['gp_obj','gp_brk']
	for EACH in NODES:
		if cmds.objExists(EACH):
			if cmds.attributeQuery('MotionLength',n=EACH,ex=True):
				cmds.deleteAttr(EACH,attribute='MotionLength')
			cmds.addAttr(EACH,at='long',longName='MotionLength')
			cmds.setAttr(EACH+'.MotionLength',-1,keyable=True)
#
def selectAllPE():
	PENODE=cmds.ls(type='mpPhysicsNode')
	cmds.select(PENODE,r=True)
	return PENODE
		
def freezePE():
	NODE=cmds.ls(type='mpPhysicsNode',l=True)
	if not NODE:
		return
	PE_TRANS=cmds.listRelatives(NODE,p=True,type='transform',f=True)
	
	for EACH in NODE:
		cmds.setAttr(EACH+'.UseTRSData',False)
	cmds.makeIdentity(PE_TRANS,a=True,s=True)
	#setTRSflag(FLAG=True)
#
def checkOcclusionVolume(NODE):
	check=False
	try:
		shape=cmds.listRelatives(NODE,s=True)
		se=cmds.listConnections(shape,type='shadingEngine')
		mat=cmds.listConnections(se,type='phong')
		for each in mat:
			var=cmds.getAttr(each+'.Shader')
			if var=='OcclusionVolume':
				check=True
				break
	except:
		check=False
		
	return check
	
def lockScale(NODE,LOCK=True):
	cmds.setAttr(NODE+'.sx',l=LOCK)
	cmds.setAttr(NODE+'.sy',l=LOCK)
	cmds.setAttr(NODE+'.sz',l=LOCK)
	
def lockException():
	NODES=cmds.ls(type='transform',l=True)
	locked=[]
	for each in NODES:
		if checkOcclusionVolume(each):
			lockScale(each,LOCK=True)
			locked.append(each)
	return locked
	
def freezeNodes():
	#例外ノードチェック
	locked=lockException()
	
	cmds.select(all=True,r=True)
	
	#resetPivot.main.reset_root
	freezePE()
	NODES=cmds.ls(type='transform',l=True)
		
	for EACH in NODES:
			
		try:
			cmds.makeIdentity(EACH,apply=True,t=False,r=False,s=True,n=0)
		except:
			continue
	#例外ノードにかけたチェックを元に戻す
	for each in locked:
		lockScale(each,LOCK=False)
	
def checkBoneroot():
	RET='boneroot OK'
	BONEROOT=cmds.objExists('boneroot')
	if not BONEROOT:
		RET='warrning:IGCnode notExist!'
	return RET
	
def checkVisible():
	VISIBLE=['boneroot','gp_obj','*:boneroot','*:gp_obj']
	INVISIBLE=['gp_col','gp_deb','*:gp_col','*:gp_deb']
	
	for EACH in VISIBLE:
		if cmds.objExists(EACH):
			try:
				cmds.setAttr(EACH+'.visibility',True)
			except:
				continue
	for EACH in INVISIBLE:
		if cmds.objExists(EACH):
			try:
				cmds.setAttr(EACH+'.visibility',False)
			except:
				continue
	#例外処理
	BOTH=['gp_brk','*:gp_brk']
	if cmds.objExists('gp_obj')or cmds.objExists('*:gp_obj'):
		EXV=False
	else:
		EXV=True
	for EACH in BOTH:
		if cmds.objExists(EACH):
			cmds.setAttr(EACH+'.visibility',EXV)
	
def checkLayerVisible():
	LAYER=cmds.ls(type='displayLayer')
	for EACH in LAYER:
		if EACH=='defaultLayer':continue
		cmds.setAttr(EACH+'.visibility',True)
	
def checkInvailedAttribute():
	RET=''
	MESH=cmds.ls(type='mesh',l=True)
	ATTRS=[
		'collision'
		,'hit'
		,'collision0'
		,'hit0'
		,'collision1'
		,'hit1'
		,'collision2'
		,'hit2'
		,'collision3'
		,'hit3'
		,'collisionc'
		,'hitc'
		,'collisionh'
		,'hith'
		,'collisionw'
		,'hitw'
		#,'parts'
		,'convex'
	]
	
	for EACH in MESH:
		for EACHATTR in ATTRS:
			if cmds.attributeQuery(EACHATTR,node=EACH,ex=True):
				RET+= 'warnning:invailed mesh attributes found = '+EACH+'.'+EACHATTR+'\n'
	return RET
	
def checkSE():
	ret=''
	def checkCol0(NODE):
		checkAttr=['collision0','collision1','collision2','collision3','collisionh']
		RET=False
		for each in checkAttr:
			if cmds.attributeQuery(each,n=NODE,ex=True):
				RET=True
				break
		return RET
		
	cols=cmds.ls(type='mpPhysicsNode')
	if not cols:
		return 'warrning:not found mpPhysicsNode!'
	check=False
	col0check=False
	for each in cols:
		if checkCol0(each):
			col0check=True
			var=cmds.getAttr(each+'.CollisionAttrID1')
			if not var==0:
				check=True
		else:
			continue
	if not col0check:
			return 'warrning:not found col#node'
	
	if check:
		return 'SE=OK.'
	else:
		return 'warrning:SE setting is not yet ? found SEID=0'
	
def checkTextureSize():
	RET=''
	TEXS=cmds.ls(type='file')
	certifiedSize=[4,8,16,32,64,128,256,512,1024,2048]
	for EACH in TEXS:
		SIZE=cmds.getAttr(EACH+'.outSize')
		if not SIZE[0][0] in certifiedSize or not SIZE[0][1] in certifiedSize :
			RET+='Error:Invaild texture found = \n'
			RET+=' -> %s \n' % EACH
			RET+=' -> X:%s Y:%s\n' % (SIZE[0][0],SIZE[0][1])
			FTN=cmds.getAttr(EACH+'.fileTextureName')
			RET+=' -> %s \n' % FTN
	if RET=='':
		RET='textureSize=OK'
	return RET
	
def checkTextureName():
	RET=''
	TEXS=cmds.ls(type='file')
	certifiedSize=[4,8,16,32,64,128,256,512,1024,2048]
	for EACH in TEXS:
		TEXTURENAME=cmds.getAttr(EACH+'.fileTextureName')
		#EXT
		EXT=TEXTURENAME.split('/')[-1].split('.')[-1]
		if not EXT == 'tif':
			RET+='Error:Invaild texture extension found = \n'
			RET+=' -> %s \n' % EACH
			RET+=' -> %s \n' % TEXTURENAME
	if RET=='':
		RET='textureName=OK'
	return RET


def checkTextureLink():
	RET=''
	TEXS=cmds.ls(type='file')
	for EACH in TEXS:
		FTN=cmds.getAttr(EACH+'.fileTextureName')
		ex=os.path.exists(FTN)
		if not ex:
			RET+='Error:lost texture link = \n'
			RET+=' -> %s \n' % FTN
	if RET=='':
		RET='textureLink=OK'
	return RET
	
def checkLocalRotatePivot():
	RET=''
	OBJ=cmds.ls(typ='transform')
	
	for EACH in OBJ:
		check=False
		LRPX=round(cmds.getAttr(EACH+'.rpx'),8)
		if not -0.000001<LRPX<0.000001:
			check=True
		LRPY=round(cmds.getAttr(EACH+'.rpy'),8)
		if not -0.000001<LRPY<0.000001:
			check=True
		LRPZ=round(cmds.getAttr(EACH+'.rpz'),8)
		if not -0.000001<LRPZ<0.000001:
			check=True
		if check:
			if cmds.nodeType(cmds.listRelatives(EACH))=='camera':
				continue
			RET+= 'Warning:localRotatePivotExists='+EACH+'\n'
	
	return RET
	
def deleteUnusedNodes():
	RET=mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')
	return RET
	
def checkUVSet():
	RET=''
	MESHES=cmds.ls(type='mesh',l=True)
	for eachMesh in MESHES:
		AUV=cmds.polyUVSet(eachMesh,q=True,auv=True)
		for eachUV in AUV:
			if not eachUV == 'map1':
				try:
					cmds.polyUVSet(eachMesh,rn=True,nuv='map1',uvs=eachUV)
					RET+=eachMesh+'.'+eachUV+' : renamed to [map1]\n'
				except:
					cmds.polyUVSet(eachMesh,d=True,uvs=eachUV)
					RET+=eachMesh+'.'+eachUV+' : deleted\n'
	return RET

def checkColorSet():
	RET=''
	ACS=[]
	MESHES=cmds.ls(type='mesh',l=True)
	for eachMesh in MESHES:
		ACS=cmds.polyColorSet(eachMesh,q=True,acs=True)
		if not ACS:
			continue

		for eachCS in ACS:


			if eachCS == 'softness':
				continue

			try:
				cmds.polyColorSet(eachMesh,rn=True,nc='colorSet',cs=eachCS)
				RET+=eachMesh+'.'+eachCS+' : renamed to [colorSet]\n'
			except:
				cmds.polyColorSet(eachMesh,d=True,cs=eachCS)
				RET+=eachMesh+'.'+eachCS+' : deleted\n'
	return RET
##### MAIN
	
def do():
	LOG=[]
	if cmds.checkBox('time30fps',q=True,v=True):
		LOG.append(time30fps())
	if cmds.checkBox('replaceExceptEmptyNodes',q=True,v=True):
		LOG.append(replaceExceptEmptyNodes())
	if cmds.checkBox('deleteConstructionHystory',q=True,v=True):
		LOG.append(deleteConstructionHystory())
	if cmds.checkBox('deleteUnusedMaterials',q=True,v=True):
		LOG.append(deleteUnusedMaterials())
	if cmds.checkBox('optimizeScene',q=True,v=True):
		optimize()
	if cmds.checkBox('freezeObjectsScale',q=True,v=True):
		freezeNodes()
	if cmds.checkBox('InvaildNameCheck',q=True,v=True):
		LOG.append(nameCheck())
	if cmds.checkBox('multipleNameCheck',q=True,v=True):
		LOG.append(multipleNameCheck())
	if cmds.checkBox('checkBoneroot',q=True,v=True):
		LOG.append(checkBoneroot())
	if cmds.checkBox('checkVisible',q=True,v=True):
		checkVisible()
	if cmds.checkBox('checkLayerVisible',q=True,v=True):
		checkLayerVisible()
	if cmds.checkBox('checkInvailedAttribute',q=True,v=True):
		checkInvailedAttribute()
	if cmds.checkBox('resetPivot',q=True,v=True):
		resetPivot()
	if cmds.checkBox('addMotionLength',q=True,v=True):
		addMotionLength()
	if cmds.checkBox('checkTextureSize',q=True,v=True):
		LOG.append(checkTextureSize())
	if cmds.checkBox('checkTextureName',q=True,v=True):
		LOG.append(checkTextureName())
	if cmds.checkBox('checkLocalRotatePivot',q=True,v=True):
		LOG.append(checkLocalRotatePivot())
	if cmds.checkBox('checkSE',q=True,v=True):
		LOG.append(checkSE())
	if cmds.checkBox('checkSE',q=True,v=True):
		LOG.append(checkSE())
	if cmds.checkBox('checkUVSet',q=True,v=True):
		LOG.append(checkUVSet())
	if cmds.checkBox('checkColorSet',q=True,v=True):
		LOG.append(checkColorSet())
	
	cmds.scrollField('MSG2_sceneCleanup_log',e=True,cl=True)
	for EACH in LOG:
		if EACH:
			cmds.scrollField('MSG2_sceneCleanup_log',e=True,it=EACH+'\n')
	

def doNodeCompare():
	nodes=cmds.ls(sl=True,l=True)
	RESULT=MS_nodeCompare.compare(nodes[0],nodes[1])
	cmds.scrollField('MSG2_sceneCleanup_log',e=True,cl=True)
	if RESULT:
		cmds.scrollField('MSG2_sceneCleanup_log',e=True,it=RESULT+'\n')
	
	
	
	
##### UI
	
def layoutLog():
	cmds.columnLayout(po=True,adj=True)
	cmds.scrollField('MSG2_sceneCleanup_log',h=400,po=True)
	cmds.setParent('..')
	cmds.setParent('..')
	
def layoutCheckbox():
	cmds.columnLayout(adj=True)
	cmds.checkBox('time30fps',v=True,ann=u'Timeセッティングを30Fpsにします。')
	cmds.checkBox('replaceExceptEmptyNodes',v=False,ann=u'例外エンプティノードをロケーター化')
	cmds.checkBox('deleteConstructionHystory',v=True,ann=u'コンストラクションヒストリー削除')
	cmds.checkBox('optimizeScene',v=True,ann=u'シーンオプティマイズ')
	#cmds.checkBox('deleteUnusedNodes',v=True,ann=u'不要マテリアルノード削除')
	cmds.checkBox('deleteUnusedMaterials',v=True,ann=u'不使用マテリアルを削除')
	cmds.checkBox('freezeObjectsScale',v=True,ann=u'すべてのオブジェクトのスケールをフリーズ')
	cmds.checkBox('InvaildNameCheck',v=False,ann=u'不正な名前をチェック')
	cmds.checkBox('multipleNameCheck',v=True,ann=u'重複するオブジェクトの名前をチェック')
	cmds.checkBox('checkBoneroot',v=False,ann=u'bonerootノードがあるかどうかのチェック')
	cmds.checkBox('addMotionLength',v=False,ann=u'gp_obj,gp_brkにMotionLength-1を強制')
	cmds.checkBox('checkVisible',v=False,ann=u'可視状態を正規化')
	cmds.checkBox('checkLayerVisible',v=False,ann=u'レイヤー可視状態を正規化')
	cmds.checkBox('checkInvailedAttribute',v=False,ann=u'非正規アトリビュートのチェック')
	cmds.checkBox('resetPivot',v=True,ann=u'ピボットを正規化')
	cmds.checkBox('checkTextureSize',v=True,ann=u'テクスチャサイズが２のべき乗になっているかチェック')
	cmds.checkBox('checkTextureName',v=True,ann=u'テクスチャ名のチェック')
	cmds.checkBox('checkLocalRotatePivot',v=True,ann=u'checkLocalRotatePivotに値が入っているオブジェクトをチェック')
	cmds.checkBox('checkSE',v=False,ann=u'collisionに所定のSEが入っているかチェック')
	cmds.checkBox('checkUVSet',v=True,ann=u'UVSetが複数作られていないかチェック、あったら消す。')
	cmds.checkBox('checkColorSet',v=False,ann=u'ColorSetにおかしなセットが作られていないかチェック、あったら消す')
	cmds.setParent('..')
	
def layoutA(
	LABEL='MSG2_sceneCleanup'
	,WIDTH=400
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout(adj=True)
	cmds.text(l=LABEL)
	
	cmds.rowLayout(nc=2,po=True)
	layoutCheckbox()
	layoutLog()
	cmds.setParent('..')
	cmds.button(w=WIDTH-4,l=u'do',c=lambda *args:do())
	cmds.button(w=WIDTH-4,l=u'nodeCompare',c=lambda *args:doNodeCompare())
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MSG2_sceneCleanup_main_window',q=True,ex=True):
		cmds.deleteUI('MSG2_sceneCleanup_main_window')
	cmds.window('MSG2_sceneCleanup_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MSG2_sceneCleanup_main_window')
	


