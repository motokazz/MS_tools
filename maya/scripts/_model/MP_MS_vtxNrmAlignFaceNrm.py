#coding=utf-8
#MP_MS_vtxNrmAlignFaceNrm
import maya.cmds as cmds
import maya.mel as mel
import math

def getFaceNormal( face ):
    try:
        normal = cmds.polyInfo( face, faceNormals=True )[0]
        temp   = normal.split(" ")
        result = [ float( temp[-3] ), float( temp[-2] ), float( temp[-1] ) ]
        return result
    except:
        return False
        
	
def MP_MS_vtxNormalAverage(vtxName):
	normalValue=[]
	n = 0
	normalSum=[0,0,0]
	normalValue = cmds.polyNormalPerVertex(vtxName,q=True,xyz=True)
	while normalValue:
		normalSum[0] += normalValue.pop(0)
		normalSum[1] += normalValue.pop(0)
		normalSum[2] += normalValue.pop(0)
	
	return normalize(normalSum)

def MP_MS_getFaces(CONP):
	FACE=cmds.polyListComponentConversion(CONP,tf=True)
	result=cmds.filterExpand(FACE,ex=True,sm=34)
	return result
	
def MP_MS_getVerts(CONP):
	VTX=cmds.polyListComponentConversion(CONP,tv=True)
	result=cmds.filterExpand(VTX,ex=True,sm=31)
	return result
	
def MP_MS_getEdges(CONP):
	EDGE=cmds.polyListComponentConversion(CONP,te=True)
	result=cmds.filterExpand(EDGE,ex=True,sm=32)
	return result

def MP_MS_getVertsFaces(CONP):
	FACE=cmds.polyListComponentConversion(CONP,tvf=True)
	result=cmds.filterExpand(FACE,ex=True,sm=70)
	return result
	


def MP_MS_stringArrayChk(item,list):
	result = 0
	for listItem in list:
		if item == listItem:
			result=1
			break
	return result

def dotproduct(v1, v2):
	return sum((a*b) for a, b in zip(v1, v2))

def length(v):
	return math.sqrt(dotproduct(v, v))
	
def angle(v1, v2):
	return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))
	
def normalize(vec):
    l=math.sqrt((vec[0]*vec[0])+(vec[1]*vec[1])+(vec[2]*vec[2]))
    result = [0.0,0.0,0.0]
    if l<0.00001:
        return [0,1,0]
    result[0]=vec[0]/l
    result[1]=vec[1]/l
    result[2]=vec[2]/l
    return result

def MP_MS_vtxNrmAlignFaceNrm():
	limitValue = cmds.floatField('MP_MS_vtxNrmAlignFaceNrm_LimitAngleFField',q=True,v=True)
	nrmBias = cmds.floatField('MP_MS_vtxNrmAlignFaceNrm_RateFField',q=True,v=True)
	
	PNPV_LIST={}
	
	OBJ=cmds.ls(sl=True)
	FACES = MP_MS_getFaces(OBJ)
	j = 0;
	resultEdges=[]
	objName=cmds.ls(hl=True)
	normalBias=[]
	
	for EACH_FACE in FACES:
		vec1 = getFaceNormal(EACH_FACE)
		getEdge =MP_MS_getEdges(EACH_FACE)
			
		for EACH_EDGE in getEdge:
			aglFlg = 0
			chkAngle =MP_MS_getFaces(EACH_EDGE)
			for EACH_chkAngle in chkAngle:
				if EACH_chkAngle in FACES:
					aglFlg+=1
			
			if aglFlg==2:
				if chkAngle[0] == EACH_FACE:
					chkAngle[0] = chkAngle[1]
					
				getConFace = cmds.polyInfo(chkAngle[0],fn=True)
				
				vec2 = getFaceNormal(chkAngle[0])
				limit = math.degrees(angle(vec1,vec2))
				
				if limit < limitValue:
					resultEdges.append(EACH_EDGE)
		print 'end 1st loop'
		
#--------------------------------------------------------------
		
		faceAlingNrm=[]
		FaceAlign =MP_MS_getVerts(EACH_FACE)
		
		if not nrmBias == 0:
			for EACH_FaceAlign in FaceAlign:
				#vector $resultRotVec;
				
				#調整前の法線が欲しい、、
				getSoftEdge = MP_MS_getFaces(EACH_FaceAlign)
				
				normalBias=[0,0,0]
				
				for EACH_getSoftEdge in getSoftEdge:
					fNrmArray=getFaceNormal(EACH_getSoftEdge)
					cfNrmArray=normalize(fNrmArray)
					
					normalBias[0] += cfNrmArray[0]
					normalBias[1] += cfNrmArray[1]
					normalBias[2] += cfNrmArray[2]
					
				normalBias=normalize(normalBias)
				
				resultVec =cmds.angleBetween(v1=vec1,v2=[normalBias[0],normalBias[1],normalBias[2]])
				#axis = [resultVec[0], resultVec[1], resultVec[2]]
				rotVec = vec1
				
				resultRotVec = mel.eval('rot <<'+str(vec1[0])+','+str(vec1[1])+','+str(vec1[2])+'>> <<'+str(resultVec[0])+','+str(resultVec[1])+','+str(resultVec[2])+'>> '+str(math.degrees(resultVec[3])*nrmBias*1/100))
				pfaceAlingNrm = resultRotVec
				
				faceAlingNrm=normalize(pfaceAlingNrm)
				PNPV_LIST[EACH_FaceAlign]=faceAlingNrm
				#cmds.polyNormalPerVertex(EACH_FaceAlign,xyz=[faceAlingNrm[0],faceAlingNrm[1],faceAlingNrm[2]])
		else:
			PNPV_LIST[FaceAlign]=vec1
			#cmds.polyNormalPerVertex(FaceAlign,xyz=[nrmX,nrmY,nrmZ])
			
	print 'end 2nd loop'
#--------------------------------------------------------------------
	print resultEdges
	
	vtxF=MP_MS_getVertsFaces(resultEdges)
	vtxFchkVerts = MP_MS_getVerts(vtxF)
	normalizeVtxFace = []
	print vtxF
	for EACH_vtxFchkVerts in vtxFchkVerts:
		
		
		
		pnormalizeNrm = [0,0,0]
		for EACH_vtxF in vtxF:
			chkinclude = MP_MS_getVerts(EACH_vtxF)
			if chkinclude[0] == EACH_vtxFchkVerts:
				print EACH_vtxF
				getFaceID =MP_MS_getFaces(EACH_vtxF)
				print getFaceID
					
				pre_fNrmArray = getFaceNormal(getFaceID[0])
				
				print pre_fNrmArray
				
				fNrmArray=normalize(pre_fNrmArray)
				
				pnormalizeNrm[0] += fNrmArray[0]
				pnormalizeNrm[1] += fNrmArray[1]
				pnormalizeNrm[2] += fNrmArray[2]
				
				normalizeVtxFace.append(EACH_vtxF)
		normalizeNrm=normalize(pnormalizeNrm)
		
		#print normalizeNrm
		if not nrmBias == 0:
			normalBias = MP_MS_vtxNormalAverage(vtxFchkVerts)
			resultVec =cmds.angleBetween(v1=[normalizeNrm[0],normalizeNrm[1],normalizeNrm[2]],v2=[normalBias[0],normalBias[1],normalBias[2]])
			axis = [resultVec[0],resultVec[1],resultVec[2]]
			rotVec = [normalizeNrm[0],normalizeNrm[1],normalizeNrm[2]]
			
			resultRotVec = mel.eval('rot <<'+str(resultVec[0])+','+str(resultVec[1])+','+str(resultVec[2])+'>> <<'+str(normalizeNrm[0])+','+str(normalizeNrm[1])+','+str(normalizeNrm[2])+'>> '+str(math.radians(resultVec[3])*nrmBias*1/100))
			normalizeNrm = normalize(resultRotVec)
			
			
		#print '3rd end'
		for EACH in normalizeVtxFace:
			PNPV_LIST[EACH]=normalizeNrm
		#cmds.polyNormalPerVertex(normalizeVtxFace,e=True,xyz=[normalizeNrm[0],normalizeNrm[1],normalizeNrm[2]])
		normalizeVtxFace=[]#メモリクリアしたつもり
		
	print PNPV_LIST
	PNPV(PNPV_LIST)
	cmds.select(OBJ,r=True)
	print 'end'
	
def PNPV(DICT):
	print 'Start'
	for EACH in DICT.keys():
		cmds.polyNormalPerVertex(EACH,xyz=[DICT[EACH][0],DICT[EACH][1],DICT[EACH][2]])
	
	print 'End'
	
def UI():
	if cmds.window('MP_MS_vtxNrmAlignFaceNrm',q=True,ex=True):
		cmds.deleteUI('MP_MS_vtxNrmAlignFaceNrm')
	cmds.window('MP_MS_vtxNrmAlignFaceNrm')
	cmds.columnLayout()
	
	cmds.floatField('MP_MS_vtxNrmAlignFaceNrm_LimitAngleFField',v=89.7)
	cmds.floatField('MP_MS_vtxNrmAlignFaceNrm_RateFField',v=2)
	cmds.button('EXEC',c='MP_MS_vtxNrmAlignFaceNrm.MP_MS_vtxNrmAlignFaceNrm()')
	cmds.window('MP_MS_vtxNrmAlignFaceNrm',e=True,w=160,h=150)
	
	cmds.showWindow('MP_MS_vtxNrmAlignFaceNrm')
	
	
	
	
	