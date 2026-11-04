#coding=utf-8
########################################
# ファイル名
#			MS_nameConvert.py
# 説明
#			
#			
# 作成日
#			
########################################


import hashlib

import maya.OpenMaya as Maya
import maya.cmds as cmds

#execCheckList
import s2000_tools.MS_lib.MSG2_execCheck as MSG2_execCheck
reload(MSG2_execCheck)


#全シーン内オブジェクトのHashリスト定義
AllHashes={}

def objectByName(name):
	select = Maya.MSelectionList()
	Maya.MGlobal.getSelectionListByName(name, select)
	if select.length() == 1:
		obj = Maya.MObject()
		select.getDependNode(0, obj)
		return obj

def worldMatrixHash( node ):
	md5 = hashlib.md5()
	precision = 4
	mark = '%%.%sf' % precision
	#u = pow( 10, precision )
	d = pow( 10, precision * -1 )
	#exMat = dag.inclusiveMatrix()
	exMat = cmds.xform( node, q=True, ws=True, a=True, t=True )
	exMat.extend( cmds.xform( node, q=True, ws=True, a=True, ro=True ) )
	exMat.extend( cmds.xform( node, q=True, os=True, r=True, s=True ) )
	parents = cmds.listRelatives( node, ap=True, ni=True, f=True )
	if parents:
		for aParent in parents:
			exMat.extend( cmds.xform( aParent, q=True, os=True, r=True, s=True ) )
	for aVal in exMat:
		if aVal < d and aVal > d * -1:
			aVal = 0
		md5.update( mark % ( round( aVal, precision ) ) )		# XXX 末尾の桁で四捨五入
	return md5.hexdigest()

def meshPointsHash( node ):
	obj = objectByName(node)
	if obj.apiType() == Maya.MFn.kMesh:
		meshFn = Maya.MFnMesh( obj )
		points = Maya.MPointArray()
		try:
			meshFn.getPoints(points)
		except:
			print 'not kWorld', meshFn.name()
		m = hashlib.md5()
		for cnt in range(points.length()):
			p = points[cnt]
			dx = p.x
			dy = p.y
			dz = p.z
			if dx == -0 : dx = 0
			if dy == -0 : dy = 0
			if dz == -0 : dz = 0
			m.update('%.2f' % dx)
			m.update('%.2f' % dy)
			m.update('%.2f' % dz)
		return m.hexdigest()


#############################################

def unique2(LIST):
    #リストから重複要素を取り除く。リストの並びは要素の登場順になる。
    RET=[]
    for EACH in LIST:
        if not EACH in RET:
            RET.append(EACH)
    return RET

def nodeTypeSafe(NODE):
	SHAPE = cmds.listRelatives(NODE,s=True,f=True)
	try:
		NODETYPE = cmds.nodeType(SHAPE[0])
		return NODETYPE
	except:
		return False

def searchAtgi(NODE=''):
	NODE=cmds.ls(sl=True)[0]
	if not nodeTypeSafe(NODE)=='GraviteAtgiLocatorNode':
		return False
	SHAPE = cmds.listRelatives(NODE,s=True)[0]
	ATGI = cmds.getAttr(SHAPE+'.atgiFilename')
	ALL=cmds.ls(type='GraviteAtgiLocatorNode',l=True)
	RESULT=[]
	for each in ALL:
		try:
			TEMP=cmds.getAttr(each+'.atgiFilename')
		except:
			continue
		if ATGI==TEMP:
			#TRN=cmds.listRelatives(TEMP,ap=True,tr=True)
			RESULT.append(each)

	cmds.select(RESULT,r=True)


def searchSameMesh():#同一形状のメッシュを選択
	MSG2_execCheck.execCheckSafe('MS_nameConvert')#execCheckList
	HASHES=[]
	SAMEMESH=[]
	#AllHashesがなければ作る
	createAllHashList()
	NODES = cmds.ls(sl=True)
	for each in NODES:

		SHAPE = cmds.listRelatives(each,s=True)[0]

		HASHES.append(meshPointsHash(SHAPE))

	HASHES=unique2(HASHES)

	for each in HASHES:
		if each in AllHashes:
			SAMEMESH.extend(AllHashes[each])
	if not len(SAMEMESH)>1:
		print '== Not Found Mesh of the same topology =='
	cmds.select(SAMEMESH,r=True)

def searchSingleUse():#一度しか使っていないと思われるオブジェクトを選択
	MSG2_execCheck.execCheckSafe('MS_nameConvert')#execCheckList
	SINGLE=[]
	#AllHashesがなければ作る
	createAllHashList()

	for each in AllHashes.keys():
		if len(AllHashes[each])>1:
			continue
		else:
			SINGLE.extend(AllHashes[each])
	
	cmds.select(SINGLE,r=True)

def searchMultipleUse():#複製と思われるオブジェクトがあるものを選択
	MSG2_execCheck.execCheckSafe('MS_nameConvert')#execCheckList
	SINGLE=[]
	#AllHashesがなければ作る
	createAllHashList()

	for each in AllHashes.keys():
		if len(AllHashes[each])>1:
			SINGLE.extend(AllHashes[each])
		else:
			continue
	
	cmds.select(SINGLE,r=True)

def createAllHashList():#シーン内の全てのオブジェクトをHashListとしてDictに格納
	global AllHashes
	AllHashes={}
	NODES = cmds.ls(tr=True,l=True)
	for each in NODES:
		try:
			SHAPE = cmds.listRelatives(each,s=True,f=True)[0]
		except:
			continue

		HASH = meshPointsHash(SHAPE)
		if not HASH in AllHashes:
			AllHashes.setdefault(HASH,[each])
		else:
			AllHashes[HASH].append(each)

def LayoutA():
	cmds.columnLayout('MS_tools_mainLayoutV',adj=True)
	cmds.separator()
	cmds.text(l='searchMesh',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	#cmds.button(l='createAllHashList',c=lambda *args:createAllHashList())
	cmds.button(l='searchSameMesh',c=lambda *args:searchSameMesh())
	cmds.button(l='searchSingleUse',c=lambda *args:searchSingleUse())
	cmds.button(l='searchMultipleUse',c=lambda *args:searchMultipleUse())
	cmds.button(l='searchSameAtgi',c=lambda *args:searchAtgi())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	