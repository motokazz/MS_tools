# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_G2ShaderUtil.py
# 説明
#			シェーダーの差し替えツール
#			
# 作成日
#			
########################################
	
import maya.cmds as cmds
import maya.mel as mel
import os

import MSG2_selectInSelectedObjectWithMaterial
reload(MSG2_selectInSelectedObjectWithMaterial)

import MS_G2ShaderUtil_attrControl
reload(MS_G2ShaderUtil_attrControl)



#プログレスバー
def MS_Progress():
	#プログレスウィンドウ
	if cmds.window('MS_ProgressWindow',ex=True):
		cmds.deleteUI('MS_ProgressWindow')
	if cmds.windowPref('MS_ProgressWindow',ex=True):
		cmds.windowPref('MS_ProgressWindow',r=True)
	cmds.window('MS_ProgressWindow',wh=[248,70],tlc=[414,516],tlb=True,s=True,t='Calculating')
	cmds.columnLayout()
	cmds.progressBar('MS_progress',maxValue=10,width=246)
	cmds.setParent ('..')
	cmds.showWindow ('MS_ProgressWindow')

#################
# UTIL
#################

def functionalRenamer(MODE='ALL'):
	if MODE=='ALL':
		SEL=cmds.ls(type=['G2_BG_Main','file'])
	elif MODE=='SEL':
		SEL=cmds.ls(sl=True,type=['G2_BG_Main','file'])
	
	for EACH in SEL:
		TYPE=cmds.nodeType(EACH)
		if 'pasted__' in EACH:
			EACH=cmds.rename(EACH,EACH.replace('pasted__',''))
		if TYPE=='lambert' or TYPE=='G2_BG_Main':
			materialFunctionalRenamer(EACH)
		if TYPE=='file':
			textureFunctionalRenamer(EACH)

def materialFunctionalRenamer(NODE):
	TYPE=cmds.nodeType(NODE)
	FTN = cmds.listConnections(NODE+'.color')
	try:
		FILETEXTURE = cmds.getAttr(FTN[0]+'.fileTextureName').split('/')[-1].split('.')[0]
	except:
		FILETEXTURE = ''

	try:
		cmds.rename(NODE,TYPE+'_'+FILETEXTURE)
	except:
		pass

def textureFunctionalRenamer(NODE):
	try:
		FILETEXTURE = cmds.getAttr(NODE+'.fileTextureName').split('/')[-1].split('.')[0]
	except:
		FILETEXTURE = ''
	try:
		cmds.rename(NODE,FILETEXTURE)
	except:
		pass

def selectMaterialFromMesh():
	SEL=cmds.ls(sl=True)
	if not SEL:
		return
	cmds.hyperShade(smn=True)
	#SELMAT=cmds.ls(sl=True,mat=True)

def checkTextureAlpha():
	RET=[]
	SEL = cmds.ls(type='file')
	for EACH in SEL:
		if cmds.getAttr(EACH+'.fileHasAlpha'):
			RET.append(EACH)
	if RET:
		cmds.select(RET,r=True)
	return RET


#################
# Preset
#################
presetDict={
		'rock'	:['rock','stone']
	,	'soil'	:['soil']
	,	'metal'	:['metal','gastank','roof_kk_09','pan_','can_','cooker_ms_02','base_sk_08','garbage_kw_05','garbage_kw_08','glass']
	,	'wood'	:['wood','tree']
	,	'cloth'	:['cloth','fablic','fabric']
	,	'grass'	:['grass','leaf','leaves']
	,	'vinyl'	:['vinyl','parasol',]
}

def autoPreset(MODE='ALL'):
	try:
		FORCE_PRESET=cmds.checkBox('forceSetPreset',q=True,v=True)
	except:
		FORCE_PRESET=False
	RET=''
	if MODE=='ALL':
		SEL=cmds.ls(type='G2_BG_Main')
	elif MODE=='SEL':
		SEL=cmds.ls(sl=True,type='G2_BG_Main')

	for EACH in SEL:
		FTN = cmds.listConnections(EACH+'.color')

		#unknown以外はセットしないオプション
		if cmds.attributeQuery('exportable_preset',node=EACH,ex=True):
			if FORCE_PRESET and not cmds.getAttr(EACH+'.exportable_preset')=='unknown':
				continue
		
		#
		PRESET_STR='rock'
		
		if FTN:
			FILETEXTURE = cmds.getAttr(FTN[0]+'.fileTextureName')
			
			for KEY in presetDict.keys():
				for SW in presetDict[KEY]:
					if SW in FILETEXTURE:
						PRESET_STR=KEY

		RET+=presetSet(EACH,PRESET_STR)

	return RET

def presetSet(NODE,PRESET_STR):
	RET=''
	cmds.select(NODE,r=True)
	mel.eval("editSelected")
	try:
		mel.eval('_g2AEPresetEnumChangeCB %s.exportable_preset %s;'%(NODE,PRESET_STR))
		cmds.optionMenuGrp("G2_BG_MainPreset",e=1,v=PRESET_STR)
		RET+='SUCCESS : PRESET  %s >　%s \n'
	except:
		pass
	return RET

def presetSelector(PRESETNAME='unknown'):
	RET=[]
	SEL = cmds.ls(sl=True)
	SHD=cmds.ls(type='G2_BG_Main')
	for EACH in SHD:
		if cmds.attributeQuery('exportable_preset',node=EACH,ex=True):
			if cmds.getAttr(EACH+'.exportable_preset')==PRESETNAME:
				cmds.hyperShade(o=EACH)
				SHDSEL=cmds.ls(sl=True)
				if SHDSEL:
					if cmds.checkBox('PresetChecker_Select_Material',q=True,v=True):
						RET.append(EACH)
					if cmds.checkBox('PresetChecker_Select_Mesh',q=True,v=True):
						RET.extend(SHDSEL)
		elif PRESETNAME=='unknown':
			RET.append(EACH)


	if RET:
		cmds.select(RET,r=True)
		print PRESETNAME+' : '+','.join(RET)
	else:
		print PRESETNAME+' : none'
		if SEL:
			cmds.select(SEL,r=True)

def selectionPreset(PRESETNAME='rock'):
	RET=''
	SEL=cmds.ls(sl=True)
	SELMAT=cmds.ls(sl=True,mat=True)
	SELTEX=cmds.ls(sl=True,type='file')

	if SELTEX:
		cmds.select(SELTEX,r=True)
		TEXCON=cmds.listConnections('.outColor')
		SELMAT=list(set(TEXCON))
	elif SELMAT:
		SEL=SELMAT
	else:
		SEL=cmds.ls(sl=True)
		if not SEL:
			return
		cmds.hyperShade(smn=True)
		SELMAT=cmds.ls(sl=True,mat=True)

	for EACH in SELMAT:
		cmds.select(EACH,r=True)
		mel.eval("editSelected")
		try:
			mel.eval('_g2AEPresetEnumChangeCB %s.exportable_preset %s;'%(EACH,PRESETNAME))
			cmds.optionMenuGrp("G2_BG_MainPreset",e=1,v=PRESET_STR)
			RET+='SUCCESS : PRESET  %s >　%s \n'
		except:
			pass
	cmds.select(SEL,r=True)


#################
# MaterialTemplate
#################

def matTemplate(NAME='default'):
	TEMPLATE_DIC={
		'default':[0.5,0.7,0.0,0.0]
		,'metal':[1.0,0.5,0.0,0.0]
		,'defaultParallax':[0.5,0.7,0.0,0.1]
		,'metalParallax':[1.0,0.5,0.0,0.1]
		,}
	SEL=cmds.ls(sl=True)
	for each in SEL:
		cmds.setAttr(each+'.specularIntensity',TEMPLATE_DIC[NAME][0])
		cmds.setAttr(each+'.roughnessIntensity',TEMPLATE_DIC[NAME][1])
		cmds.setAttr(each+'.translucencyIntensity',TEMPLATE_DIC[NAME][2])
		cmds.setAttr(each+'.parallaxIntensity',TEMPLATE_DIC[NAME][3])


#################
# cleanup
#################
def shaderClean(CLEAN_TEXTURE=True,COMPAIR_ALL_MAT_ATTRIBUTES=True,COMPAIR_CONNECTIONS=True):
	#未使用ノード削除（これをやらないとうまくいかない）
	mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')

	#テクスチャクリーンナップ（最初にやった方がいい）

	if cmds.checkBox('MS_G2ShaderUtil_cleanTextures',q=True,ex=True):
		if cmds.checkBox('MS_G2ShaderUtil_cleanTextures',q=True,v=True):
			textureClean()
	elif CLEAN_TEXTURE:
		textureClean()
	
	#マテリアルクリーンナップ
	if cmds.checkBox('MS_G2ShaderUtil_compairAllMatAttributes',q=True,ex=True):
		COMPAIR_ALL_MAT_ATTRIBUTES=cmds.checkBox('MS_G2ShaderUtil_compairAllMatAttributes',q=True,v=True)

	if cmds.checkBox('MS_G2ShaderUtil_compairConnections',q=True,ex=True):
		COMPAIR_CONNECTIONS=cmds.checkBox('MS_G2ShaderUtil_compairConnections',q=True,v=True)

	matterClean(COMPAIR_ALL_MAT_ATTRIBUTES,COMPAIR_CONNECTIONS)

	#プログレス
	if cmds.window('MS_ProgressWindow',ex=True):
		cmds.deleteUI('MS_ProgressWindow')
	cmds.window('MS_ProgressWindow',wh=[248,70],tlc=[414,516],tlb=True,s=True,t='Calculating')
	cmds.columnLayout()
	cmds.text(l='deleteUnusedNodes')
	cmds.setParent ('..')
	cmds.showWindow ('MS_ProgressWindow')
	
	#未使用ノード削除
	mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')
	#
	cmds.deleteUI('MS_ProgressWindow')#プログレス
	
def fixShadingEngines():
	SE=cmds.ls(type='shadingEngine',l=True)
	for each in SE:
		if each=='initialParticleSE' or each=='initialShadingGroup':
			continue
		SHADERS=cmds.listConnections(each+'.surfaceShader')
		if len(SHADERS)==1:
			SG=SHADERS[0]+'SG'
			cmds.rename(each,SG)
			print 'rename : '+each+' -> '+SG+'\n'
		else:
			print 'ERROR!! find multi connection shader!\n '
			print SHADERS
			print '\n'


def matterClean(compairAllMatAttributes=False,compairConnections=False):
	if not compairAllMatAttributes and not compairConnections:
		return
		
	ALLMATS=cmds.ls(mat=True,l=True)
	if not ALLMATS:
		return
	#数値を比較するときの閾値を取得
	THRESHOULD=cmds.floatField('MS_G2ShaderUtil_compairConnections_threshould',q=True,v=True)

	#プログレスバー
	MS_Progress()
	cmds.progressBar('MS_progress',edit=True,beginProgress=True,isInterruptable=True,maxValue=len(ALLMATS))
	while ALLMATS:
		cmds.progressBar('MS_progress',edit=True,s=1)#プログレス
		BASEMAT=ALLMATS.pop(0)
		
		if 'lambert1' in BASEMAT:
			continue

		SAMEMAT=[]
		for EACHMAT in ALLMATS:
			if EACHMAT==BASEMAT:
				continue

			#コネクション比較（マテリアルより先にやったほうがいい）
			if 	compairConnections:
				if not twoMaterialConnectionsDifference(BASEMAT,EACHMAT):
					continue

			#マテリアルアトリビュート比較
			if 	compairAllMatAttributes:

				if not twoMaterialDifference(BASEMAT,EACHMAT,THRESHOULD):
					continue
					
			SAMEMAT.append(EACHMAT)

		for eachSAMEMAT in SAMEMAT:
			matBtoMatA(BASEMAT,eachSAMEMAT)
	#
	cmds.deleteUI('MS_ProgressWindow')#プログレス
	#mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')

def twoTextureDifference(FTN_A,FTN_B): #２つのテクスチャを比べて同じだったらTrue

	if not cmds.getAttr(FTN_A+'.fileTextureName').lower()==cmds.getAttr(FTN_B+'.fileTextureName').lower(): #名前が一致
		return False

	#CONNECTION
	ATTRS={
		'repeatUV':(1,1)
		,'rotateUV':0
		,'offset':(0,0)
		}

	for eATTR in ATTRS.keys():

		CON_A = cmds.listConnections(FTN_A+'.'+eATTR,p=True)
		CON_B = cmds.listConnections(FTN_B+'.'+eATTR,p=True)

		if CON_A:
			ATTR_A = cmds.getAttr(CON_A[0])
		else:
			ATTR_A = ATTRS[eATTR]
			
		if CON_B:
			ATTR_B = cmds.getAttr(CON_B[0])
		else:
			ATTR_B = ATTRS[eATTR]

		if not ATTR_A == ATTR_B:
			return False

	return True

def textureClean():
	RESULT=[]
	FTN=cmds.ls(type='file',l=True)
	if not FTN:
		return
	#プログレスバー
	MS_Progress()
	cmds.progressBar('MS_progress',edit=True,beginProgress=True,isInterruptable=True,maxValue=len(FTN))
	while FTN:
		cmds.progressBar('MS_progress',edit=True,s=1)#プログレス
		base=FTN.pop(0)
		TEMP=[base]
		for each in FTN:
			if twoTextureDifference(base,each):
				TEMP.append(each)

		if len(TEMP)>1:
			RESULT.append(TEMP)

	for EACHRESULT in RESULT:
		base=EACHRESULT.pop(0)
		SOURCECONNECTION=cmds.listConnections(base+'.outColor',c=True,p=True)
		if not SOURCECONNECTION:
			continue
		for EACHRESULTB in EACHRESULT:
			DISTCONNECTION=cmds.listConnections(EACHRESULTB+'.outColor',c=True,p=True)
			if DISTCONNECTION:
				cmds.disconnectAttr(DISTCONNECTION[0],DISTCONNECTION[1])
				cmds.connectAttr(SOURCECONNECTION[0],DISTCONNECTION[1])

	cmds.deleteUI('MS_ProgressWindow')#プログレス

def twoMaterialDifference(MAT_A,MAT_B,THRESHOULD=0.15):
	'''
	ATTRS=['colorScale'
		#,'alphaTest'
		#,'colorScale'
		#,'color2Scale'
		#,'alphaRef'
		#,'parallaxIntensity'
		#,'roughnessIntensity'
		#,'translucencyIntensity'
		#,'backFaceCulling'
		#,'decalMasking'
		#,'emissiveIntensity'
		#,'metallic2Intensity'
		#,'roughness2Intensity'
		#,'translucency2Intensity'
		#,'metallicIntensity'
		#,'emissive2Intensity'
		#,'parallax2Intensity'
		#,'shadowCast'
		]
		'''
	IGNORE=[
		'caching'
		,'nodeState'
		,'outColor'
		,'outTransparency'
		,'outGlowColor'
		,'outMatteOpacity'
		,'outColorR'
		,'outColorG'
		,'outColorB'
		,'outTransparency'
		,'outTransparencyR'
		,'outTransparencyG'
		,'outTransparencyB'
		,'outGlowColor'
		,'outGlowColorR'
		,'outGlowColorG'
		,'outGlowColorB'
		,'outMatteOpacity'
		,'outMatteOpacityR'
		,'outMatteOpacityG'
		,'outMatteOpacityB'
		,'enableHwShading'
		,'varyingParameters'
		,'uniformParameters'
		#,'alphaTest'
		#,'colorScale'
		#,'color2Scale'
		#,'alphaRef'
		#,'parallaxIntensity'
		#,'roughnessIntensity'
		#,'translucencyIntensity'
		,'color'
		,'colorR'
		,'colorG'
		,'colorB'
		,'color2'
		,'color2R'
		,'color2G'
		,'color2B'
		,'normal2'
		,'normal2R'
		,'normal2G'
		,'normal2B'
		,'normal'
		,'normalR'
		,'normalG'
		,'normalB'
		#,'backFaceCulling'
		#,'decalMasking'
		,'POSITION'
		,'POSITION_DefaultTexture'
		,'NORMAL'
		,'NORMAL_DefaultTexture'
		,'TEXCOORD0'
		,'TEXCOORD0_DefaultTexture'
		,'BINORMAL0'
		,'BINORMAL0_DefaultTexture'
		,'TANGENT0'
		,'TANGENT0_DefaultTexture'
		,'COLOR0'
		,'COLOR0_DefaultTexture'
		,'exportable_preset'
		#,'emissiveIntensity'
		#,'metallic2Intensity'
		#,'roughness2Intensity'
		#,'translucency2Intensity'
		#,'metallicIntensity'
		#,'emissive2Intensity'
		#,'parallax2Intensity'
		,'mask'
		,'maskR'
		,'maskG'
		,'maskB'
		#,'shadowCast'
		]

	IGNORE_THRESHOULD={
		'parallaxIntensity'
		,'parallax2Intensity'
	}

	#二つのマテリアルが同じだったらTrueを返す
	ATTRS = cmds.listAttr(MAT_A,v=True)
	
	for each in ATTRS:
		if each in IGNORE:
			continue

		try:
			THRESHOULD_TEMP=THRESHOULD
			TYPE=cmds.attributeQuery(each,node=MAT_A,at=True)
			
			#アトリビュートの値をチェック
			ORGATTR=cmds.getAttr(MAT_A+'.'+each)
			SCHATTR=cmds.getAttr(MAT_B+'.'+each)

			#閾値に関する例外
			if each in IGNORE_THRESHOULD:
				THRESHOULD_TEMP=0.0
				
			#処理
			if TYPE=='bool':
				if not ORGATTR==SCHATTR:
					return False

			elif TYPE=='float':
				if abs(ORGATTR-SCHATTR)>THRESHOULD_TEMP:
					return False

			elif TYPE=='float3':
				if abs(ORGATTR[0]-SCHATTR[0])>THRESHOULD_TEMP or abs(ORGATTR[1]-SCHATTR[1])>THRESHOULD_TEMP or abs(ORGATTR[2]-SCHATTR[2])>THRESHOULD_TEMP:
					return False

			else:
				continue


		except Exception as e:
			print e.message
			pass
	return True

def twoMaterialConnectionsDifference(MAT_A,MAT_B):
	#二つのマテリアルのテクスチャコネクションが同じだったらTrueを返す

	#比較元のコネクション状況
	TEMP=cmds.listConnections(MAT_A,type='file',d=True,c=True)
	if TEMP:
		ORGFILE={i.split('.')[-1]:j for (i,j) in zip(TEMP[::2],TEMP[1::2])}
	else:
		ORGFILE={}

	#比較対象側のコネクション状況
	TEMP=cmds.listConnections(MAT_B,type='file',d=True,c=True)
	if TEMP:
		SCHFILE={i.split('.')[-1]:j for (i,j) in zip(TEMP[::2],TEMP[1::2])}
	else:
		SCHFILE={}

	#テクスチャのコネクション数をチェック
	if not ORGFILE and not SCHFILE:		#どっちもなしならTrue
		return True
	elif not ORGFILE or not SCHFILE:	#どっちかが在りならFalse
		return False

	if not len(ORGFILE)==len(SCHFILE):	#コネクション数一緒でなければFalse
		return False

	#コネクション先のテクスチャをチェック
	for EACH in ORGFILE.keys():
		if ORGFILE[EACH] == SCHFILE[EACH]:	#コネクション先のノードが同じならContinue
			continue
		else:
			return False
		'''
		ORGTEX=cmds.getAttr(ORGFILE[EACH]+'.fileTextureName')
		SCHTEX=cmds.getAttr(SCHFILE[EACH]+'.fileTextureName')
		if not ORGTEX==SCHTEX:
			return False
		'''

	return True

def matBtoMatA(MAT_A,MAT_B):
	### core ###

	if MAT_B == 'lambert1' or MAT_A==MAT_B:
		return
	if cmds.objExists(MAT_B+'.outColor'):
		sg = cmds.listConnections(MAT_B+'.outColor')
	elif cmds.objExists(MAT_B+'.oc'):#unknownファイル対応
		sg = cmds.listConnections(MAT_B,t='shadingEngine')

	sgs = cmds.sets(sg[0],q=True)

	certified=[]#発見できないオブジェクトを排斥したリストを作成する
	if sgs:
		for each in sgs:
			if cmds.objExists(each):
				certified.append(each)
			else:
				print each
		if not certified:
			print 'certifiedObjectNotFount!'
			return

		cmds.select(certified,r=True)
		
		cmds.hyperShade(a=MAT_A)

		try:
			cmds.connectAttr(MAT_A+'.outColor',sg[0]+'.surfaceShader')
			return 'Success'
		except:
			pass

#################
# connectNormal
#################
def connectNormal(FROM ='selection'):

	if FROM =='selection':
		shd=cmds.ls(sl=True,type='G2_BG_Main',l=True)
	if FROM =='allG2BG':
		shd=cmds.ls(type='G2_BG_Main',l=True)

	for each in shd:
		if cmds.listConnections(each+'.normal'):#コネクションがあったらスキップ
			continue

		tex=cmds.listConnections(each+'.color')
		if not tex:
			continue
		texname=cmds.getAttr(tex[0]+'.fileTextureName')
		ntex = texname.replace('_c','_n')
		
		#テクスチャー存在確認
		if not os.path.exists(ntex):
			ntex=texname.replace('_c','_na')
			if not os.path.exists(ntex):
				continue


		ntexname=ntex.split('/')[-1]
		nnode = cmds.shadingNode('file',asTexture=True)

		cmds.setAttr(nnode+'.fileTextureName',ntex,type='string')
		
		cmds.connectAttr(nnode+'.outColor',each+'.normal')
		#cmds.setAttr(each+'.parallaxIntensity',0.1)

		cmds.rename(nnode,ntexname)

#################
# shaderChanger
#################
def copyParamGToG2(G_SRC,D2_DST):
	
	colorScaleR = cmds.getAttr(G_SRC+'.colorScaleR')
	colorScaleG = cmds.getAttr(G_SRC+'.colorScaleG')
	colorScaleB = cmds.getAttr(G_SRC+'.colorScaleB')

	backFaceCulling = cmds.getAttr(G_SRC+'.backFaceCulling')
	punchThrough = cmds.getAttr(G_SRC+'.punchThrough')
	alphaBlend = cmds.getAttr(G_SRC+'.alphaBlend')
	discardThreshold = cmds.getAttr(G_SRC+'.discardThreshold')

	cmds.setAttr(D2_DST+'.colorScaleR',colorScaleR)
	cmds.setAttr(D2_DST+'.colorScaleR',colorScaleG)
	cmds.setAttr(D2_DST+'.colorScaleR',colorScaleB)

	cmds.setAttr(D2_DST+'.backFaceCulling',backFaceCulling)
	if punchThrough or alphaBlend:
		cmds.setAttr(D2_DST+'.alphaTest',1)
	
	cmds.setAttr(D2_DST+'.alphaRef',discardThreshold)

def shaderChanger(shdName='G2_BG_Main',FROM ='selection'):
	RET=''
	#### selectionmode ###
	if FROM =='selection':
		nodes=cmds.ls(sl=True,l=True)
	elif FROM =='allGBG':
		nodes=cmds.ls(type='G_BG_Main',l=True)
	elif FROM =='allG2BG':
		nodes=cmds.ls(type='G2_BG_Main',l=True)
	elif FROM =='alllambert':
		nodes=cmds.ls(type='lambert',l=True)

	### core ###
	for each in nodes:

		if each == 'lambert1':
			continue

		success=False
		#color
		try:
			con = cmds.listConnections(each+'.color')
		except:
			con = False
		#normal
		try:
			con_n = cmds.listConnections(each+'.normal')
		except:
			con_n = False

		sg = cmds.listConnections(each,type='shadingEngine')
		sgs = cmds.sets(sg[0],q=True)

		#
		shd = cmds.shadingNode(shdName,asShader=True)

		if shdName=='dx11Shader':
			cmds.setAttr(shd+'.shader','AutodeskUberShader.fxo',type='string')

		certified=[]#発見できないオブジェクトを排斥したリストを作成する
		if sgs:
			for eachsgs in sgs:
				if cmds.objExists(eachsgs):
					certified.append(eachsgs)
				else:
					print each

			cmds.select(certified,r=True)
			try:
				cmds.hyperShade(a=shd)
				RET+='success : '+each+' to '+shd+'\n'
			except:
				RET+='failed : '+each+' to '+shd+'\n'
				pass
			###
			if shdName=='dx11Shader':
				
				if con:
					cmds.setAttr(shd+'.UseDiffuseTexture',True)
					cmds.connectAttr(con[0]+'.outColor',shd+'.DiffuseTexture')
				if con_n:
					cmds.setAttr(shd+'.UseNormalTexture',True)
					cmds.connectAttr(con_n[0]+'.outColor',shd+'.NormalTexture')
			else:
				if con:
					cmds.connectAttr(con[0]+'.outColor',shd+'.color')

			cmds.connectAttr(shd+'.outColor',sg[0]+'.surfaceShader',force=True)

			success=True

			#
			if shdName=='G2_BG_Main' and cmds.nodeType(each)=='G_BG_Main':
				try:
					copyParamGToG2(each,shd)
				except:
					pass


	#mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')
	return RET

def shaderChangerNormalToColor(shdName='G2_BG_Main',FROM ='selection'):
	RET=''
	#### selectionmode ###
	if FROM =='selection':
		nodes=cmds.ls(sl=True,l=True)
	else:
		nodes=cmds.ls(type=['G2_BG_Main','lambert'],l=True)

	### core ###
	for each in nodes:
		if each == 'lambert1':
			continue

		if cmds.nodeType(each)=='lambert' or cmds.nodeType(each)=='phong' or cmds.nodeType(each)=='blinn':
			ftnColorToNormal(each)
			continue
		success=False
		con = cmds.listConnections(each+'.normal')
		sg = cmds.listConnections(each+'.outColor')
		sgs = cmds.sets(sg[0],q=True)
		#
		shd = cmds.shadingNode(shdName,asShader=True)

		certified=[]#発見できないオブジェクトを排斥したリストを作成する
		if sgs:
			for eachsgs in sgs:
				if cmds.objExists(eachsgs):
					certified.append(eachsgs)
				else:
					print each

			cmds.select(certified,r=True)
			try:
				cmds.hyperShade(a=shd)
				RET+='success : '+each+' to '+shd+'\n'
			except:
				RET+='failed : '+each+' to '+shd+'\n'
				pass

			#print con[0]
			print shd
			try:
				if not con:
					print 'not con[0]'
					cmds.setAttr(shd+'.color',0.5,0.5,1.0,type='double3')
					success=True

				elif not os.path.exists(cmds.getAttr(con[0]+'.fileTextureName')):
					print 'not Path'
					cmds.setAttr(shd+'.color',0.5,0.5,1.0,type='double3')
					success=True

				elif con[0]:
					cmds.connectAttr(con[0]+'.outColor',shd+'.color')
					cmds.connectAttr(shd+'.outColor',sg[0]+'.surfaceShader')
					success=True
			except:
				pass

			'''
			if shdName=='G2_BG_Main' and cmds.nodeType(each)=='G_BG_Main':
				try:
					copyParamGToG2(each,shd)
				except:
					pass
			'''

	mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')
	return RET

def ftnColorToNormal(SHD=''):
	con = cmds.listConnections(SHD+'.color')
	if not con:
		cmds.setAttr(SHD+'.color',0.5,0.5,1.0,type='double3')
		return
	#
	PATH=cmds.getAttr(con[0]+'.fileTextureName')
	if '_n.' in PATH:return
	if '_na.' in PATH:return

	if '_c.' in PATH:

		if os.path.exists(PATH.replace('_c.','_n.')):
			cmds.setAttr(con[0]+'.fileTextureName',PATH.replace('_c.','_n.'),type='string')
			return

		elif os.path.exists(PATH.replace('_c.','_na.')):
			cmds.setAttr(con[0]+'.fileTextureName',PATH.replace('_c.','_na.'),type='string')
			return

	if '_ca.' in PATH:

		if os.path.exists(PATH.replace('_ca.','_na.')):
			cmds.setAttr(con[0]+'.fileTextureName',PATH.replace('_ca.','_na.'),type='string')
			return

		elif os.path.exists(PATH.replace('_ca.','_n.')):
			cmds.setAttr(con[0]+'.fileTextureName',PATH.replace('_ca.','_n.'),type='string')
			return



	#ノーマルのパスが見つからなかったら。
	cmds.disconnectAttr(con[0]+'.outColor',SHD+'.color')
	cmds.setAttr(SHD+'.color',0.5,0.5,1.0,type='double3')

def LayoutA():
	cmds.frameLayout(l='MS_G2ShaderUtil',cl=True,cll=True,bgc=[0.4,0.4,0.4])
	cmds.text(l='MS_G2ShaderUtil',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.separator(w=300)
	#
	cmds.text(l='to G2_BG_Main',bgc=[0.6,0.55,0.6],fn='boldLabelFont')
	cmds.rowLayout(nc=2,cw2=[100,200])
	cmds.button(l='selection to G2BG',w=100,h=50,bgc=[0.8,0.7,0.8],c=lambda *args:shaderChanger())
	cmds.columnLayout(adj=True)
	cmds.button(l='all GBG to G2BG',w=200,h=25,bgc=[0.8,0.7,0.8],c=lambda *args:shaderChanger(shdName='G2_BG_Main',FROM ='allGBG'))
	cmds.button(l='all lambert to G2BG',w=200,h=25,bgc=[0.8,0.7,0.8],c=lambda *args:shaderChanger(shdName='G2_BG_Main',FROM ='alllambert'))
	cmds.setParent('..')
	cmds.setParent('..')
	#
	cmds.text(l='to G_BG_Main',bgc=[0.55,0.55,0.6],fn='boldLabelFont')
	cmds.rowLayout(nc=2,cw2=[100,200])
	cmds.button(l='selection to GBG',w=100,h=50,bgc=[0.7,0.7,0.8],c=lambda *args:shaderChanger('G_BG_Main'))
	cmds.columnLayout(adj=True)
	cmds.button(l='all G2BG to GBG',w=200,h=25,bgc=[0.7,0.7,0.8],c=lambda *args:shaderChanger(shdName='G_BG_Main',FROM ='allG2BG'))
	cmds.button(l='all lambert to GBG',w=200,h=25,bgc=[0.7,0.7,0.8],c=lambda *args:shaderChanger(shdName='G_BG_Main',FROM ='alllambert'))
	cmds.setParent('..')
	cmds.setParent('..')
	#
	cmds.text(l='to dx11Shader',bgc=[0.55,0.6,0.55],fn='boldLabelFont')
	cmds.rowLayout(nc=2,cw2=[100,200])
	cmds.button(l='selection to dx11Shader',w=100,h=50,bgc=[0.7,0.8,0.7],c=lambda *args:shaderChanger('dx11Shader'))
	cmds.columnLayout(adj=True)
	cmds.button(l='all G2BG to dx11Shader',w=200,h=25,bgc=[0.7,0.8,0.7],c=lambda *args:shaderChanger(shdName='dx11Shader',FROM ='allG2BG'))
	cmds.button(l='all GBG to dx11Shader',w=200,h=25,bgc=[0.7,0.8,0.7],c=lambda *args:shaderChanger(shdName='dx11Shader',FROM ='allGBG'))
	cmds.setParent('..')
	cmds.setParent('..')

	#
	cmds.text(l='to lambert',bgc=[0.55,0.6,0.55],fn='boldLabelFont')
	cmds.rowLayout(nc=2,cw2=[100,200])
	cmds.button(l='selection to lambert',w=100,h=50,bgc=[0.7,0.8,0.7],c=lambda *args:shaderChanger('lambert'))
	cmds.columnLayout(adj=True)
	cmds.button(l='all G2BG to lambert',w=200,h=25,bgc=[0.7,0.8,0.7],c=lambda *args:shaderChanger(shdName='lambert',FROM ='allG2BG'))
	cmds.button(l='all GBG to lambert',w=200,h=25,bgc=[0.7,0.8,0.7],c=lambda *args:shaderChanger(shdName='lambert',FROM ='allGBG'))
	cmds.setParent('..')
	cmds.setParent('..')
	#
	cmds.text(l='Color to Normal lambert',bgc=[0.6,0.6,0.8],fn='boldLabelFont')
	cmds.rowLayout(nc=2,cw2=[100,200])
	cmds.button(l='selection To ...',w=100,h=40,bgc=[0.6,0.6,0.8],c=lambda *args:shaderChangerNormalToColor('lambert'))
	cmds.button(l='all Color To Normal',w=200,h=40,bgc=[0.6,0.6,0.8],c=lambda *args:shaderChangerNormalToColor(shdName='lambert',FROM ='allG2BG'))
	cmds.setParent('..')

	cmds.separator()

	cmds.setParent('..')

def LayoutMaterialTemplate():

	cmds.text(l='MaterialTemplate',bgc=[0.6,0.6,0.6],fn='boldLabelFont')
	cmds.gridLayout(nc=4,cw=75)

	cmds.button(l='default',bgc=[0.75,0.75,0.75],c=lambda *args:matTemplate('default'))
	cmds.button(l='Metal',bgc=[0.75,0.75,0.75],c=lambda *args:matTemplate('metal'))
	cmds.button(l='default\nParallax',bgc=[0.75,0.75,0.75],c=lambda *args:matTemplate('defaultParallax'))
	cmds.button(l='metal\nParallax',bgc=[0.75,0.75,0.75],c=lambda *args:matTemplate('metalParallax'))
	
	cmds.setParent('..')
	
def LayoutManualPreset():
	cmds.columnLayout(adj=True)
	cmds.text(l='ManualPreset',bgc=[0.6,0.6,0.6],fn='boldLabelFont',ann=u'選択したものに関連するマテリアルにプリセットを設定します\n～対応ノード～\nメッシュオブジェクト\nメッシュコンポーネント\nマテリアル\nテクスチャ')
	cmds.gridLayout(nc=8,cw=40,ann=u'選択したものに関連するマテリアルにプリセットを設定します\n～対応ノード～\nメッシュオブジェクト\nメッシュコンポーネント\nマテリアル\nテクスチャ')
	cmds.button(l='rock',bgc=[0.8,0.9,0.8],c=lambda *args:selectionPreset(PRESETNAME='rock'))
	cmds.button(l='soil',bgc=[0.8,0.9,0.8],c=lambda *args:selectionPreset(PRESETNAME='soil'))
	cmds.button(l='metal',bgc=[0.8,0.9,0.8],c=lambda *args:selectionPreset(PRESETNAME='metal'))
	cmds.button(l='wood',bgc=[0.8,0.9,0.8],c=lambda *args:selectionPreset(PRESETNAME='wood'))
	cmds.button(l='cloth',bgc=[0.8,0.9,0.8],c=lambda *args:selectionPreset(PRESETNAME='cloth'))
	cmds.button(l='grass',bgc=[0.8,0.9,0.8],c=lambda *args:selectionPreset(PRESETNAME='grass'))
	cmds.button(l='vinyl',bgc=[0.8,0.9,0.8],c=lambda *args:selectionPreset(PRESETNAME='vinyl'))
	cmds.setParent('..')
	cmds.text(l='PresetChecker',bgc=[0.6,0.6,0.6],fn='boldLabelFont',ann=u'プリセットがついているオブジェクトを選択します')
	cmds.checkBox('PresetChecker_Select_Material',l='Select_Material',v=True,ann=u'ON：結果をマテリアル選択します')
	cmds.checkBox('PresetChecker_Select_Mesh',l='Select_Mesh',v=True,ann=u'ON：結果をメッシュ選択します')

	cmds.gridLayout(nc=8,cw=40,ann=u'プリセットがついているオブジェクトを選択します')
	cmds.button(l='rock',bgc=[0.8,0.8,0.8],c=lambda *args:presetSelector(PRESETNAME='rock'))
	cmds.button(l='soil',bgc=[0.8,0.8,0.8],c=lambda *args:presetSelector(PRESETNAME='soil'))
	cmds.button(l='metal',bgc=[0.8,0.8,0.8],c=lambda *args:presetSelector(PRESETNAME='metal'))
	cmds.button(l='wood',bgc=[0.8,0.8,0.8],c=lambda *args:presetSelector(PRESETNAME='wood'))
	cmds.button(l='cloth',bgc=[0.8,0.8,0.8],c=lambda *args:presetSelector(PRESETNAME='cloth'))
	cmds.button(l='grass',bgc=[0.8,0.8,0.8],c=lambda *args:presetSelector(PRESETNAME='grass'))
	cmds.button(l='vinyl',bgc=[0.8,0.8,0.8],c=lambda *args:presetSelector(PRESETNAME='vinyl'))
	cmds.button(l='unknown',bgc=[0.8,0.8,0.8],c=lambda *args:presetSelector(PRESETNAME='unknown'))
	cmds.setParent('..')
	cmds.setParent('..')

def LayoutAutoPreset():
	cmds.columnLayout(adj=True)
	cmds.text(l='AutoPreset',bgc=[0.6,0.6,0.6],fn='boldLabelFont')
	cmds.checkBox('forceSetPreset',v=False,ann=u'OFF：既に割り当てられているプリセットがあるマテリアルには自動プリセット設定しません\nON：シーン内の全てのマテリアルに自動プリセット設定します')
	cmds.button(l='AutoPresetAll',bgc=[0.8,0.8,0.7],h=40,c=lambda *args:autoPreset('ALL'),ann=u'テクスチャー名、フォルダ名を元に自動プリセット設定します')

	cmds.setParent('..')

def LayoutNomalmapUtil():
	cmds.frameLayout(l='normalMapConnector',cl=False,cll=True,bgc=[0.4,0.4,0.4])
	#cmds.text(l='normalMapConnector',bgc=[0.6,0.6,0.6],fn='boldLabelFont')
	cmds.button(l='connectNormal',bgc=[0.75,0.75,0.75],c=lambda *args:connectNormal())
	cmds.button(l='connectNormaltoAllG2BG',bgc=[0.75,0.75,0.75],c=lambda *args:connectNormal(FROM ='allG2BG'))
	#cmds.separator()
	cmds.setParent('..')

def LayoutShaderClean():
	cmds.frameLayout(l='ShaderClean',cl=False,cll=True,bgc=[0.4,0.4,0.4])

	cmds.separator(h=1,style='none')

	cmds.gridLayout(nc=3,cw=100,ch=16)
	cmds.checkBox('MS_G2ShaderUtil_compairAllMatAttributes',l='compairAllMatAttributes',v=True)
	cmds.text(l='threshould')
	cmds.floatField('MS_G2ShaderUtil_compairConnections_threshould',v=0.15)
	cmds.setParent('..')
	
	cmds.separator()
	
	cmds.checkBox('MS_G2ShaderUtil_compairConnections',l='compairConnections',v=True)

	cmds.separator()
	
	cmds.checkBox('MS_G2ShaderUtil_cleanTextures',l='cleanTextures',v=True)
	cmds.button(l='shaderClean',bgc=[0.7,0.8,0.8],h=40,c=lambda *args:shaderClean())

	cmds.separator()

	cmds.setParent('..')

def LayoutUtility():
	cmds.frameLayout(l='Utility',cl=False,cll=True,bgc=[0.4,0.4,0.4])
	#cmds.columnLayout(adj=True)
	#cmds.text(l='Utility',bgc=[0.6,0.6,0.6],fn='boldLabelFont')
	cmds.button(l=u'テクスチャ名を元に、マテリアル名とファイルテクスチャノード名を変更',bgc=[0.8,0.7,0.8],h=20,c=lambda *args:functionalRenamer('ALL'),ann=u'テクスチャ名を元に、マテリアル名とファイルテクスチャノード名を変更します')
	cmds.button(l=u'選択したメッシュに割り当てられているマテリアルを選択',bgc=[0.7,0.8,0.8],h=20,c=lambda *args:selectMaterialFromMesh(),ann=u'選択したメッシュに割り当てられているマテリアルを選択します。')
	cmds.button(l=u'アルファチャンネルのあるテクスチャを選択',bgc=[0.7,0.7,0.7],h=20,c=lambda *args:checkTextureAlpha(),ann=u'アルファチャンネルのあるテクスチャを選択します。')
	cmds.button(l=u'シェーディンググループの不具合を修正',bgc=[0.7,0.8,0.7],h=20,c=lambda *args:fixShadingEngines(),ann=u'シェーディンググループの不具合を修正します。')	
	#cmds.setParent('..')
	cmds.setParent('..')

def UIautpPresetWindow():
	if cmds.window('MS_G2ShaderUtil_window',q=True,ex=True):
		cmds.deleteUI('MS_G2ShaderUtil_window')
	cmds.window('MS_G2ShaderUtil_window',rtf=True,s=True)
	
	LayoutManualPreset()
	
	cmds.window('MS_G2ShaderUtil_window',e=True,w=308,h=331)
	cmds.showWindow('MS_G2ShaderUtil_window')

def UI():
	if cmds.window('MS_G2ShaderUtil_window',q=True,ex=True):
		cmds.deleteUI('MS_G2ShaderUtil_window')
	cmds.window('MS_G2ShaderUtil_window',rtf=True,s=True)
	
	cmds.columnLayout(adj=True)
	LayoutA()
	cmds.separator(h=10,style='none')
	LayoutNomalmapUtil()
	cmds.separator(h=10,style='none')
	LayoutShaderClean()
	cmds.separator(h=10,style='none')

	#LayoutManualPreset()
	#LayoutAutoPreset()
	
	MS_G2ShaderUtil_attrControl.LayoutA()
	cmds.separator(h=10,style='none')
	MSG2_selectInSelectedObjectWithMaterial.LayoutA()
	cmds.separator(h=10,style='none')
	LayoutUtility()
	cmds.separator(h=10,style='none')

	cmds.setParent('..')
	
	cmds.window('MS_G2ShaderUtil_window',e=True,w=308,h=331)
	cmds.showWindow('MS_G2ShaderUtil_window')

