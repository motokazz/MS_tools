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
		SEL = cmds.ls(mat=True)
		#SEL=cmds.ls(type=['G2_BG_Main','file'])
	elif MODE=='SEL':
		SEL=cmds.ls(sl=True,type=['G2_BG_Main','file'])
	
	for EACH in SEL:
		TYPE=cmds.nodeType(EACH)
		if 'pasted__' in EACH:
			EACH=cmds.rename(EACH,EACH.replace('pasted__',''))
		#if TYPE=='lambert' or TYPE=='G2_BG_Main':
		#

		if TYPE=='file':
			textureFunctionalRenamer(EACH)
		materialFunctionalRenamer(EACH)


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

def checkTextureAlpha():
	RET=[]
	SEL = cmds.ls(type='file')
	for EACH in SEL:
		if cmds.getAttr(EACH+'.fileHasAlpha'):
			RET.append(EACH)
	if RET:
		cmds.select(RET,r=True)
	return RET

def Util_twoMaterialDifference():
	sel = cmds.ls(sl=True)
	print 'material:'+str(twoMaterialDifference(sel[0],sel[1]))
	print 'connection:'+str(twoMaterialConnectionsDifference(sel[0],sel[1]))

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
		
		#if 'lambert1' in BASEMAT:
		#	continue

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
				for i in range(0,len(DISTCONNECTION),2):
					cmds.disconnectAttr(DISTCONNECTION[i],DISTCONNECTION[i+1])
					cmds.connectAttr(SOURCECONNECTION[0],DISTCONNECTION[i+1])

	cmds.deleteUI('MS_ProgressWindow')#プログレス

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

def twoMaterialDifference(MAT_A,MAT_B,THRESHOULD=0.01):
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
		#,'outColorR'
		#,'outColorG'
		#,'outColorB'
		,'outTransparency'
		#,'outTransparencyR'
		#,'outTransparencyG'
		#,'outTransparencyB'
		,'outGlowColor'
		#,'outGlowColorR'
		#,'outGlowColorG'
		#,'outGlowColorB'
		,'outMatteOpacity'
		#,'outMatteOpacityR'
		#,'outMatteOpacityG'
		#,'outMatteOpacityB'
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
		#,'color'
		#,'colorR'
		#,'colorG'
		#,'colorB'
		#,'color2'
		,'color2R'
		,'color2G'
		,'color2B'
		#,'normal2'
		,'normal2R'
		,'normal2G'
		,'normal2B'
		#,'normal'
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
		#,'mask'
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
					print ORGATTR
					return False

			elif TYPE=='float':
				if abs(ORGATTR-SCHATTR)>THRESHOULD_TEMP:
					print ORGATTR
					return False

			elif TYPE=='float3':
				if abs(ORGATTR[0]-SCHATTR[0])>THRESHOULD_TEMP or abs(ORGATTR[1]-SCHATTR[1])>THRESHOULD_TEMP or abs(ORGATTR[2]-SCHATTR[2])>THRESHOULD_TEMP:
					print ORGATTR
					return False

			else:
				continue


		except Exception as e:

			print each+' : '+e.message
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
	print MAT_A+' ; '+MAT_B
	if MAT_B == 'lambert1' or MAT_A==MAT_B:
		return

	sg=[]
	if cmds.objExists(MAT_B+'.outColor'):
		sg = cmds.listConnections(MAT_B+'.outColor')
	elif cmds.objExists(MAT_B+'.oc'):#unknownファイル対応
		sg = cmds.listConnections(MAT_B,t='shadingEngine')
	if sg:
		sgs = cmds.sets(sg[0],q=True)
	else:
		return

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



#######
# UI
#######

def LayoutShaderClean():
	cmds.frameLayout(l='ShaderClean',cl=False,cll=True,bgc=[0.4,0.4,0.4])

	cmds.separator(h=1,style='none')

	cmds.gridLayout(nc=3,cw=100,ch=16)
	cmds.checkBox('MS_G2ShaderUtil_compairAllMatAttributes',l='compairAllMatAttributes',v=True)
	cmds.text(l='threshould')
	cmds.floatField('MS_G2ShaderUtil_compairConnections_threshould',v=0.01)
	cmds.setParent('..')
	
	cmds.checkBox('MS_G2ShaderUtil_compairConnections',l='compairConnections',v=True)
	
	cmds.checkBox('MS_G2ShaderUtil_cleanTextures',l='cleanTextures',v=True)

	cmds.button(l='shaderClean',bgc=[0.7,0.8,0.8],h=40,c=lambda *args:shaderClean())

	cmds.separator()

	cmds.setParent('..')

def LayoutUtility():
	cmds.frameLayout(l='Utility',cl=False,cll=True,bgc=[0.4,0.4,0.4])
	cmds.button(l=u'テクスチャ名を元に、マテリアル名とファイルテクスチャノード名を変更',bgc=[0.8,0.7,0.8],h=20,c=lambda *args:functionalRenamer('ALL'),ann=u'テクスチャ名を元に、マテリアル名とファイルテクスチャノード名を変更します')
	cmds.button(l=u'選択したメッシュに割り当てられているマテリアルを選択',bgc=[0.7,0.8,0.8],h=20,c=lambda *args:selectMaterialFromMesh(),ann=u'選択したメッシュに割り当てられているマテリアルを選択します。')
	cmds.button(l=u'アルファチャンネルのあるテクスチャを選択',bgc=[0.7,0.7,0.7],h=20,c=lambda *args:checkTextureAlpha(),ann=u'アルファチャンネルのあるテクスチャを選択します。')
	cmds.button(l=u'シェーディンググループの不具合を修正',bgc=[0.7,0.8,0.7],h=20,c=lambda *args:fixShadingEngines(),ann=u'シェーディンググループの不具合を修正します。')	
	cmds.button(l=u'選択した2つのマテリアルを比較',bgc=[0.7,0.8,0.7],h=20,c=lambda *args:Util_twoMaterialDifference(),ann=u'選択した2つのマテリアルを比較。')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_shaderUtil_window',q=True,ex=True):
		cmds.deleteUI('MS_shaderUtil_window')
	cmds.window('MS_shaderUtil_window',rtf=True,s=True)
	
	cmds.columnLayout(adj=True)

	LayoutShaderClean()
	LayoutUtility()

	cmds.setParent('..')
	
	cmds.window('MS_shaderUtil_window',e=True,w=308,h=331)
	cmds.showWindow('MS_shaderUtil_window')

