#! /usr/bin/python
# -*- coding: utf-8 -*-

#モデルをサーフェイス上の頂点の法線方向に向けて並べる
#ベースモデル　パーツモデルの順に選択して実行

import maya.OpenMaya as OpenMaya
import maya.cmds as cmds
import math

def exe():
    selected = cmds.ls( sl=True )
    meshName = selected[0]
    
    #モデルはlsで拾って名前で選択します
    list = OpenMaya.MSelectionList()
    OpenMaya.MGlobal_getSelectionListByName( selected[0], list )
    baseObj = OpenMaya.MDagPath()
    list.getDagPath( 0, baseObj)
    
    meshFn = OpenMaya.MFnMesh( baseObj )
    
    for i in range(meshFn.numVertices()):
        vtx  = OpenMaya.MPoint()
        nor= OpenMaya.MVector()
        meshFn.getPoint(i,  vtx ,OpenMaya.MSpace.kObject)    
        meshFn.getVertexNormal(i,True,nor,OpenMaya.MSpace.kObject)
        
        tmpObj = cmds.duplicate(selected[1])
        cmds.move(vtx.x ,vtx.y ,vtx.z,tmpObj)
    
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
        
        #原点から頂点までのベクトル(Y軸up限定版)
        vtxBaseVec = OpenMaya.MVector(1,0,0)      
        vtxVec = OpenMaya.MVector(vtx.x,0,vtx.z)
        vtxVec.normalize()
        
        partsRot = vtxBaseVec*vtxVec
        
        #回転軸ベクトルと回転角をもとめる
        axis = baseVec^normalVec
        rot =  baseVec*normalVec
    
        #クォータニオンをもとめる
        q = OpenMaya.MQuaternion()
        r = math.acos(rot)
        q.setAxisAngle( axis , r)
        
        q0 = OpenMaya.MQuaternion()    
        r0 = math.acos(partsRot)
        
        #z位置が正なら角度反転
        if vtx.z>0:
            r0 = -r0        
        q0.setAxisAngle(  OpenMaya.MVector(0,1,0) , r0)
        
        q = q0*q
        
        mfn =OpenMaya.MFnTransform(partsObj)
        mfn.setRotation(q,OpenMaya.MSpace.kWorld)
        
    