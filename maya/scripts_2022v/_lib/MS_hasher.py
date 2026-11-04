#coding=utf-8
#大内さんのやつを改造by坂井元一
########################################
# ファイル名
#			MP_MS_nameConvert
# 説明
#			メッシュの各情報を元にハッシュを作成。
#			同一オブジェクト検索などに重宝する。
# 作成日\n#			
########################################
import hashlib

import maya.OpenMaya as Maya
import maya.cmds as cmds



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
