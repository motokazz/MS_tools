#! /usr/bin/python
# -*- coding: utf-8 -*-

#モデルをサーフェイス上の頂点の法線方向に向けて並べる
#ベースモデル　パーツモデルの順に選択して実行

import maya.OpenMaya as OpenMaya
import maya.cmds as cmds
import math
import maya.mel as mel
import attachFaceNomalsRev3

VERSION='v 0.6'
LASTUPDATE='2010/03/24'
SCRIPT_NAME='NIKO2attachTool'

def UI():
	if cmds.window('%sWin' % SCRIPT_NAME,ex=True) == True :
		cmds.deleteUI('%sWin' % SCRIPT_NAME)
	
	window=cmds.window('%sWin' % SCRIPT_NAME, t='%s %s %s' % (SCRIPT_NAME,VERSION,LASTUPDATE),menuBar=True)		
	
	cmds.columnLayout( )
	cmds.button( c ="attachFaceNomalsRev3.exe( 0 )" , l = "Duplicate to Face")
	cmds.showWindow()


def exe( a ):
	#partsName = mel.eval("$temp=$g_MS_instancer_RESULT_OBJ")
	#print TransferMELvar
	#return
	partsNameArray = mel.eval("MS_instancer_returenTargetList(\"TFGTgt\")")
	partsName = partsNameArray[0]
	
	#モデルはlsで拾って名前で選択します
	#ハイライトされたモデルの選択
	# selected = cmds.ls( sl=True )
	# meshName = selected[0]

	# list = OpenMaya.MSelectionList()
	# OpenMaya.MGlobal_getSelectionListByName( selected[0], list )
	# baseObj = OpenMaya.MDagPath()
	# list.getDagPath( 0, baseObj)

	# meshFn = OpenMaya.MFnMesh( baseObj )

	# vertexArray  = OpenMaya.MPointArray()
	# meshFn.getPoints(vertexArray,OpenMaya.MSpace.kWorld)

	#選択ポリゴンの取得
	polylist = OpenMaya.MSelectionList()
	OpenMaya.MGlobal.getActiveSelectionList( polylist )
	poly = OpenMaya.MObject()
	polylist.getDependNode( 0, poly)
	
	listIter = OpenMaya.MItSelectionList( polylist , OpenMaya.MFn.kMeshPolygonComponent  )
	a=0
	
	meshDagPath = OpenMaya.MDagPath()
	multiFaceComponent = OpenMaya.MObject()
	
	while not listIter.isDone():
		listIter.getDagPath(meshDagPath, multiFaceComponent)
		itpory = OpenMaya.MItMeshPolygon (meshDagPath, multiFaceComponent)
		
		vertexArray  = OpenMaya.MPointArray()
		meshFn = OpenMaya.MFnMesh( meshDagPath )
		meshFn.getPoints(vertexArray,OpenMaya.MSpace.kWorld)
		
		while not itpory.isDone():
		
			i = itpory.index()	
		#for i in range(meshFn.numPolygons()):
			vArray = OpenMaya.MIntArray()
			meshFn.getPolygonVertices(i,vArray)
			
			nor = OpenMaya.MVector()
			tn = OpenMaya.MFloatVector()
			bn = OpenMaya.MFloatVector()
			
			bnArray = OpenMaya.MFloatVectorArray()
			tnArray = OpenMaya.MFloatVectorArray()
					
			meshFn.getPolygonNormal(i,nor,OpenMaya.MSpace.kWorld)
			meshFn.getFaceVertexBinormals( i , bnArray ,OpenMaya.MSpace.kWorld,"map1")
			meshFn.getFaceVertexTangents( i , tnArray ,OpenMaya.MSpace.kWorld,"map1")
			
			for j in  range( tnArray.length() ):
				tn = tn + tnArray[j]

			for j in  range( bnArray.length() ):
				bn = bn + bnArray[j]			
				
			bn.normalize()
			tn.normalize()
			
			pt = OpenMaya.MVector(0,0,0)
			ptArray = OpenMaya.MVectorArray()
			num=0
			for k in vArray:
				ptArray.append(OpenMaya.MVector(vertexArray[k].x,vertexArray[k].y,vertexArray[k].z))
				pt =  pt + OpenMaya.MVector(vertexArray[k].x,vertexArray[k].y,vertexArray[k].z)
				num = num+1
				
			pt = pt/vArray.length()
			
			#パーツを複製
			tmpObj = cmds.duplicate( partsName )
			cmds.move(pt.x ,pt.y ,pt.z,tmpObj)

			#メッシュの取得
			partsObj = OpenMaya.MDagPath()
			list1 = OpenMaya.MSelectionList()
			OpenMaya.MGlobal_getSelectionListByName(tmpObj[0], list1 )
			list1.getDagPath( 0,partsObj)

			#各種ベクトル
			baseVec  = OpenMaya.MVector(0,1,0) #ベースモデルの方向ベクトル
			normalVec = OpenMaya.MVector(nor.x ,nor.y ,nor.z )
			axisVec = OpenMaya.MVector()
			normalVec.normalize()

			#回転軸ベクトルと回転角をもとめる
			axis = baseVec^normalVec
			rot =  baseVec*normalVec		
			#クォータニオンをもとめる
			q = OpenMaya.MQuaternion()    
			r = math.acos(rot)
			q.setAxisAngle( axis , r)

			
			
			#モデルのupVectorは回転軸方向に等しい　binormal方向にあわせる
			vtxBaseVec = axis
			vtxBaseVec.normalize() 

			vtxVec = OpenMaya.MVector( bn[0] , bn[1]  ,bn[2] )
			tanVec = OpenMaya.MVector( tn[0] , tn[1]  ,tn[2] )
			vtxVec.normalize() 
			tanVec.normalize() 

			ws=math.sin( r/2 );
			wc=math.cos( r/2 );

			qRot = OpenMaya.MQuaternion()
			qTrans = OpenMaya.MQuaternion()

			
			qP = OpenMaya.MQuaternion( 1.0 , 0 , 0, 0 )
			qQ = OpenMaya.MQuaternion(ws*axis[0] , ws*axis[1] ,ws*axis[2] ,wc)
			qR = OpenMaya.MQuaternion(-ws*axis[0] , -ws*axis[1] ,-ws*axis[2] ,wc)

			qTrans = qR*qP*qQ	
			qt = OpenMaya.MVector(qTrans[ 0 ],qTrans[ 1 ],qTrans[ 2 ])
			
			partsVec = qt^vtxVec
			partsRot = vtxVec*qt
			
			
			q0 = OpenMaya.MQuaternion()
			
			r0 = math.acos(partsRot)
			# if tanVec*qt > 0:
				# r0 = math.acos(partsRot)
			# else:
				# r0 = math.acos(-partsRot)
				
			q0.setAxisAngle(  partsVec , r0)


			q = q*q0
					
			mfn =OpenMaya.MFnTransform(partsObj)
			mfn.setRotation(q,OpenMaya.MSpace.kWorld)
			
			itpory.next()
		listIter.next()