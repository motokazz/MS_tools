#! /usr/bin/python
# -*- coding: utf-8 -*-

#モデルをサーフェイス上の頂点の法線方向に向けて並べる
#ベースモデル　パーツモデルの順に選択して実行

import maya.OpenMaya as OpenMaya
import maya.cmds as cmds
import math

def exe(scaleBias):
    selected = cmds.ls( sl=True )
    meshName = selected[0]
    
    #モデルはlsで拾って名前で選択します
    list = OpenMaya.MSelectionList()
    OpenMaya.MGlobal_getSelectionListByName( selected[0], list )
    baseObj = OpenMaya.MDagPath()
    list.getDagPath( 0, baseObj)
    
    meshFn = OpenMaya.MFnMesh( baseObj )
    
    vertexArray  = OpenMaya.MPointArray()
    meshFn.getPoints(vertexArray,OpenMaya.MSpace.kObject)

    for i in range(meshFn.numPolygons()):
        vArray = OpenMaya.MIntArray()
        meshFn.getPolygonVertices(i,vArray)
        
        #utl = OpenMaya.MScriptUtil()]
        nor = OpenMaya.MVector()
        meshFn.getPolygonNormal(i,nor)
        
        pt = OpenMaya.MVector(0,0,0)
        ptArray = OpenMaya.MVectorArray()
        num=0
        for k in vArray:
            ptArray.append(OpenMaya.MVector(vertexArray[k].x,vertexArray[k].y,vertexArray[k].z))
            pt =  pt + OpenMaya.MVector(vertexArray[k].x,vertexArray[k].y,vertexArray[k].z)
            num = num+1
            
        pt = pt/vArray.length()
        #print "point > %f:%f:%f" % (pt.x ,pt.y ,pt.z )
        #面積を求める
        vp0 = OpenMaya.MVector()
        vp1 = OpenMaya.MVector()
        vp2 = OpenMaya.MVector()
        
        vp0 = ptArray[0] - ptArray[1]
        vp1 = ptArray[1] - ptArray[2]
        vp2 = ptArray[2] - ptArray[0]

        a = vp0.length()
        b = vp1.length()
        c = vp2.length()
        
        s = (a+b+c)*0.5
        #S =math.sqrt(s*(s-a)*(s-b)*(s-c)) 
        S =math.sqrt(s*(s-a)*(s-b)*(s-c)) 
        
        #四角ポリゴンなら
        if num == 4:
            vp0 = ptArray[0] - ptArray[2]
            vp1 = ptArray[2] - ptArray[3]
            vp2 = ptArray[3] - ptArray[0]

            a = vp0.length()
            b = vp1.length()
            c = vp2.length()
            
            s = (a+b+c)*0.5
            #e =s*(s-a)*(s-c)*(s-d)
            #print "%f : %f : %f : %f" % (a,b,c,e)        
            S = S + math.sqrt(s*(s-a)*(s-b)*(s-c)) 

        
        
        tmpObj = cmds.duplicate(selected[1])
        
        S=S*scaleBias
       
        cmds.scale(S ,S ,S , tmpObj,r=True)
        cmds.move(pt.x ,pt.y ,pt.z,tmpObj)
        

        #メッシュの取得
        partsObj = OpenMaya.MDagPath()
        list1 = OpenMaya.MSelectionList()
        OpenMaya.MGlobal_getSelectionListByName(tmpObj[0], list1 )
        list1.getDagPath( 0,partsObj)
        
        
        #原点から面までのベクトル(Y軸up限定版)
        vtxBaseVec = OpenMaya.MVector(1,0,0)      
        vtxVec = OpenMaya.MVector(pt.x,0,pt.z)
        vtxVec.normalize()   
        partsRot = vtxBaseVec*vtxVec
            
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
        
        q0 = OpenMaya.MQuaternion()    
        r0 = math.acos(partsRot)
        
        #z位置が正なら角度反転
        if pt.z>0:
            r0 = -r0        
        q0.setAxisAngle(  OpenMaya.MVector(0,1,0) , r0)
        
        q = q0*q
                
        mfn =OpenMaya.MFnTransform(partsObj)
        mfn.setRotation(q,OpenMaya.MSpace.kWorld)
        

    