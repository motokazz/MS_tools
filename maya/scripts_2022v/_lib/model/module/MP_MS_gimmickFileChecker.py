# _*_coding:utf-8_*_
########################################
# ファイル名
#			MP_MS_gimmickFileChecker.py
# 説明
#			
# 作成日\n#			
########################################

import maya.cmds as cmds
import maya.mel as mel
import os

import MS_module.MS_swatchMaker as MS_swatchMaker
reload(MS_swatchMaker)


EXPORT_PATH='d:/Mproject/graphic/gimmick/doc/'
	
##### ファイルセーブ #####
def SAVE(ROW,FILE_PATH):
	f=open(FILE_PATH,'w')#'r'読み込み：'w'書き込み：'a'追記：'+'読み書き両方' 't'テキストモード：'b'バイナリーモード
	f.write(ROW)
	f.close()
	
##### ファイルロード #####
def LOAD(FILE_PATH):
	f=open(FILE_PATH)
	DATA=[]
	for ROW in f:
		DATA.append(ROW)
	f.close()
	return DATA
	
	
	
def dirList():
	list=[
		'8000'
		,'8100'
		,'8200'
		,'8300'
		,'8400'
		,'8500'
		,'8600'
		,'8700'
		,'8800'
		,'8900'
		,'9000'
		,'9100'
		,'9200'
		,'9400'
		,'9600'
		,'9800'
		,'9900'
	]
	return list
	
def dirListz():
	list=[
		'9400'
		,'9600'
		,'9800'
		,'9900'
	]
	return list
	
	
##### checker
	
	
	
	
def check_obj(index=False):
	ret=[]
	objname=['gp_obj','vtx','gp_brk','vtx','gp_col','gp_deb','vtx','destruction']
	if index:
		return ','.join(objname)
	
	
	if cmds.objExists('gp_obj'):
		ret.append(str(len(cmds.ls('gp_obj'))))
		ret.append(str(checkPolyCount('gp_obj')))
	else:
		ret.append('0')
		ret.append('0')
	
	if cmds.objExists('gp_brk'):
		ret.append(str(len(cmds.ls('gp_brk'))))
		ret.append(str(checkPolyCount('gp_brk')))
	else:
		ret.append('0')
		ret.append('0')
	
	if cmds.objExists('gp_col'):
		ret.append(str(len(cmds.ls('gp_col'))))
	else:
		ret.append('0')
	
	if cmds.objExists('gp_deb'):
		ret.append(str(len(cmds.ls('gp_deb'))))
		ret.append(str(checkPolyCount('gp_deb')))
	else:
		ret.append('0')
		ret.append('0')
	
	#destruction
	if cmds.objExists('gp_brk'):
		if cmds.objExists('gp_obj'):
			ret.append('ok')
		else:
			ret.append('invailed')
	else:
		ret.append('none')
	
	return ','.join(ret)
	
def checkPolyCount(OBJ):
	try:
		shp=cmds.listRelatives(OBJ,ad=True,type='transform')
		cmds.select(shp,r=True)
		vertexCount=cmds.polyEvaluate(v=True)
		return vertexCount
	except:
		return 0
	
	
	
def deleteUnused():
	def deleteUselessObj():
		reguler=['persp','top','front','side','boneroot','gp_obj','gp_brk','gp_col','gp_deb']
		assem=cmds.ls(assemblies=True)
		for each in assem:
			if each in reguler:
				continue
			else:
				try:
					cmds.delete(each)
				except:
					continue
	
	def deleteUnusedMaterials():
		mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')
		return 'execute deleteUnusedMaterials'
		
	deleteUselessObj()
	deleteUnusedMaterials()
	
	
def check_mat(index=False):
	
	matType=['phong','ToroUberMaterial','M_EF_Smoke','M_EF_Gel','M_EF_Distortion']
	if index:
		return ','.join(matType)
	
	ret=[]
	deleteUnused()
	for each in matType:
		
		nodes=cmds.ls(type=each)
		if each=='ToroUberMaterial' and nodes:
			strpreset=''
			for node in nodes:
				preset=cmds.getAttr(node+'.preset0')
				strpreset+=preset+':'
			ret.append(strpreset)
		else:
			ret.append(str(len(nodes)))
	
	return ','.join(ret)
	
	
def check_member(ID):
	ret=''
	list=LOAD('D:/Mproject/graphic/gimmick/doc/gimmick_tantou.csv')
	for each in list:
		temp=each.split(',')
		if ID==temp[0]:
			ret=temp[1].replace('\r\n','')
			break
		
	return ret
	
def check_indb(ID):
	list=LOAD('d:/Mproject/graphic/gimmick/doc/list_in_db.csv')
	for each in list:
		temp=each.split(',')
		if ID==temp[2]:
			return 'ok'
	return 'x'
	
def check_location(ID):
	list=LOAD('d:/Mproject/graphic/gimmick/doc/list_no_located.csv')
	for each in list:
		temp=each.split(',')
		if ID==temp[1]:
			return 'x'
	return 'ok'
	
def check_light():
	lights=cmds.ls(type='light')
	return str(len(lights))
	
def check_col():
	penode=cmds.ls(type='mpPhysicsNode',l=True)
	col0,col1,col2,col3,colh,col0se=0,0,0,0,0,0
	for each in penode:
		if cmds.attributeQuery('collision0',node=each,ex=True):
			if cmds.getAttr(each+'.collision0'):
				col0+=1
		if cmds.attributeQuery('collision1',node=each,ex=True):
			if cmds.getAttr(each+'.collision1'):
				col1+=1
		if cmds.attributeQuery('collision2',node=each,ex=True):
			if cmds.getAttr(each+'.collision2'):
				col2+=1
		if cmds.attributeQuery('collision3',node=each,ex=True):
			if cmds.getAttr(each+'.collision3'):
				col3+=1
		if cmds.attributeQuery('collisionh',node=each,ex=True):
			if cmds.getAttr(each+'.collisionh'):
				colh+=1
		if cmds.attributeQuery('CollisionAttrID1',node=each,ex=True):
			if cmds.getAttr(each+'.CollisionAttrID1'):
				col0se+=1
	return '%s,%s,%s,%s,%s,%s'%(str(col0),str(col1),str(col2),str(col3),str(colh),str(col0se))
	
def swatch(ID):
	def objSwatchMaker(NODE_NAME,EX_PATH,SWATCH_NAME):
		#targetPanel = cmds.getPanel(withFocus=True)
		#if not 'modelPanel' in targetPanel:
		#	cmds.confirmDialog( m=u'warning ビューポートを選択してください\nサムネイルは出力されません')
		#	return
		targetPanel = 'modelPanel4'
		targetCamera=cmds.modelPanel(targetPanel,q=True,cam=True)
		hadEnable = cmds.modelEditor(targetPanel, q=True, hud=True)
		
		cmds.select(NODE_NAME,r=True)
		cmds.viewFit(f=0.5)
		cmds.select(clear=True)
		
		MS_swatchMaker.swatchMaker(EX_PATH,SWATCH_NAME,X=512,Y=512)
		
		cmds.modelEditor(targetPanel, e=True, rnm='base_OpenGL_Renderer', da='smoothShaded', dtx=True, hud=hadEnable)
		
	EX_PATH='d:/Mproject/graphic/gimmick/doc/swatch'
	
	if cmds.objExists('gp_col'):
		cmds.showHidden('gp_col*',b=True)
		cmds.modelEditor('modelPanel4',e=True,locators=True)
	if cmds.objExists('gp_obj'):
		cmds.showHidden('gp_obj*',b=True)
		objSwatchMaker('gp_obj',EX_PATH,ID)
	elif cmds.objExists('gp_brk'):
		cmds.showHidden('gp_brk*',b=True)
		objSwatchMaker('gp_brk',EX_PATH,ID)
	elif cmds.objExists('boneroot'):
		cmds.showHidden('boneroot*',b=True)
		objSwatchMaker('boneroot',EX_PATH,ID)
	else:
		DUMMY=cmds.polySphere()
		objSwatchMaker(DUMMY[0],EX_PATH,ID)
	
##### exec
	
def do():
	dirs=dirList()
	
	for dir in dirs:
		result=[]
		#createindesx
		index='filename,file_exists'							#base
		index+=',member'
		index+=',indb'
		index+=',location'
		index+=','+check_obj(index=True)	#checkobj
		index+=','+check_mat(index=True)	#checkmat
		index+=',light'
		index+=',col0,col1,col2,col3,colh,col0se'
		result.append(index)
		#
		files=os.listdir('D:/Mproject/graphic/fg/character/gimmick/'+dir)
		for each in files:
			path='D:/Mproject/graphic/fg/character/gimmick/'+dir+'/'+each+'/'+each+'_model.mb'
			if os.path.exists(path):							#exists
				#check base
				cmds.file(path,f=True,options='v=0',type='mayaBinary',ignoreVersion=True,o=True)
				#file
				rowstr=each+',ok'
				#member
				ID=each.split('_')[0]
				rowstr+=','+check_member(ID)
				#check_indb
				rowstr+=','+check_indb(ID)
				#check_location
				rowstr+=','+check_location(ID)
				#checkobj
				rowstr+=','+check_obj()
				#checkMat
				rowstr+=','+check_mat()
				#checkLight
				rowstr+=','+check_light()
				#check_col
				rowstr+=','+check_col()
				#
				result.append(rowstr.encode('utf-8'))
				
				
			else:											#not exists
				result.append(each+',notFound')
		ROW='\n'.join(result)+'\n'
		SAVE(ROW,EXPORT_PATH+'objcheck'+dir+'.csv')
	
def swatchCreation():
	dirs=dirList()
	for dir in dirs:
		files=os.listdir('D:/Mproject/graphic/fg/character/gimmick/'+dir)
		for each in files:
			path='D:/Mproject/graphic/fg/character/gimmick/'+dir+'/'+each+'/'+each+'_model.mb'
			if os.path.exists(path):							#exists
				#check base
				cmds.file(path,f=True,options='v=0',type='mayaBinary',ignoreVersion=True,o=True)
				#swatch
				#ID=each.split('_')[0]
				swatch(each)
				
##### UI
	
def layoutA(
	LABEL='MP_MS_gimmickFileChecker'
	,WIDTH=300
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	
	cmds.text(l=LABEL)
	cmds.text(l=u'MプロギミックMBファイル個別チェックリスト作成')
	cmds.separator(w=300,h=10)
	cmds.text(l=u'出力パス=>%s'%EXPORT_PATH)
	cmds.separator(w=300,h=10)
	cmds.button(w=WIDTH-4,bgc=[0.6,0.8,0.6],l=u'gimmickFileCheck',c=lambda *args:do())
	
	cmds.text(l=LABEL)
	cmds.text(l=u'MプロギミックMBファイル個別スウォッチ作成')
	cmds.separator(w=300,h=10)
	cmds.text(l=u'出力パス=>%s'%EXPORT_PATH)
	cmds.separator(w=300,h=10)
	cmds.button(w=WIDTH-4,bgc=[0.6,0.8,0.6],l=u'swatchCreation',c=lambda *args:swatchCreation())
	
	
	
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MP_MS_gimmickFileChecker_main_window',q=True,ex=True):
		cmds.deleteUI('MP_MS_gimmickFileChecker_main_window')
	cmds.window('MP_MS_gimmickFileChecker_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MP_MS_gimmickFileChecker_main_window')
	

