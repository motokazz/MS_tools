# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_primitives
# 説明
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import maya.mel as mel
import math
import os
import sys

#実行パス追加
#sys.path.append(os.path.dirname(__file__))

#import MS_insertLocator
#reload(MS_insertLocator)

import MS_getBestBB
reload(MS_getBestBB)

import MS_vector
reload (MS_vector)

import MS_duplicate
reload (MS_duplicate)

import MS_distance
reload (MS_distance)

import MS_createTube
reload (MS_createTube)

import MS_locatorToCurve
reload (MS_locatorToCurve)

import MS_resetPivot
reload (MS_resetPivot)


#execCheckList
import MS_execCheck
reload(MS_execCheck)
MS_execCheck.execCheckSafe('MS_primitives.py')


##### exec

class bestSubdivisions:
	size=1
	subdRate=1

	class cube:
		x=0
		y=0
		z=0

	class sphere:
		x=20
		y=20
		z=0

	class cone:
		x=20
		y=1
		z=0

	class cylinder:
		x=20
		y=1
		z=0

	class pyramid:
		x=0
		y=1
		z=0

	class plane:
		x=8
		y=8

	def AutoSubd():

		pass

	def GetSubdivision(self):
		subd=int(cmds.floatSliderGrp('interactiveSubdivision_controller',q=True,v=True))
		self.plane.x=subd
		self.plane.y=subd

class createPrimitive(bestSubdivisions):
	#==========================
	def __init__(self):
		self.name='msPrimitives'
		self.constructionHistory=True
		self.createUVs=2
		self.object=True
		self.obj=[]
		self.comp=[]
		self.trn=[0,0,0]
		self.rot=(0,0,0)
		self.scl=[1,1,1]
		self.height=1
		self.axis=[0,1,0]
		self.radius=0.5
		self.subdivisions=bestSubdivisions
		self.rotatemode = 'rm_auto' #SimpleScale,BBMesure
		self.scalemode = 'BBMesure' #SimpleScale,BBMesure
		self.scaleFilterMIN = 1.0
		self.scaleFilterMAX = 10000.0

	################
	# method
	################

	#Transform Utility

	def xFormAverage(self,xf):
		#xform が連続した戻り値リスト（[[0,0,0],[1,1,1],[2,2,2],[3,3,3]...])を返してくるので、それを平均化する。
		x=0.0
		y=0.0
		z=0.0
		n=0
		RET=[0.0,0.0,0.0]

		while xf:
			x+=xf.pop(0)
			y+=xf.pop(0)
			z+=xf.pop(0)
			n+=1

		if x and n:
			RET[0]=x/n
		else:
			RET[0]=0
		if y and n:
			RET[1]=y/n
		else:
			RET[1]=0
		if z and n:
			RET[2]=z/n
		else:
			RET[2]=0
		return RET
	
	#Translate Method

	#Rotation Method

	def getRotFromConstraint(self):#ノーマルコンストレインから値をとる。
		locator=cmds.spaceLocator()
		cmds.xform(locator,t=self.trn,ws=True)
		vtxs = cmds.polyListComponentConversion(self.comp,tvf=True)
		CONSTRAINT=cmds.normalConstraint(vtxs,locator[0],weight=1,aimVector=(0,1,0),upVector=(0,1,0),worldUpType='vector',worldUpVector=(0,1,0))
		self.rot=cmds.xform(locator[0],q=True,ro=True,ws=True)
		cmds.delete(CONSTRAINT)
		cmds.delete(locator)

	#Scale Method

	def scaleFilter(self):#MIN値以下のスケール値をMIN値にする MAX値以下のスケールをMAX値にする
		var=self.scaleFilterMIN

		if self.scl[0]<self.scaleFilterMIN:self.scl[0]=self.scaleFilterMIN
		if self.scl[1]<self.scaleFilterMIN:self.scl[1]=self.scaleFilterMIN
		if self.scl[2]<self.scaleFilterMIN:self.scl[2]=self.scaleFilterMIN

		var=self.scaleFilterMAX
		if self.scl[0]>self.scaleFilterMAX:self.scl[0]=self.scaleFilterMAX
		if self.scl[1]>self.scaleFilterMAX:self.scl[1]=self.scaleFilterMAX
		if self.scl[2]>self.scaleFilterMAX:self.scl[2]=self.scaleFilterMAX

	def scaleAverage(self):#スケールの値を平均化してXYZに同じ数字を割り振る。
		av=(self.scl[0]+self.scl[1]+self.scl[2])*(1.0/3)
		self.scl=[av,av,av]

	def sizeFromCamera(self):#何も選ばれてないときにカメラからの距離に応じてスケールを決める。
		targetPanel = cmds.getPanel(withFocus=True)
		
		if not 'modelPanel' in targetPanel:
			cmds.confirmDialog( m=u'warning ビューポートを選択してください')
			
		cam=cmds.modelPanel(targetPanel,q=True,cam=True)
		camtrans=cmds.xform(cam,q=True,ws=True,t=True)
		distance=MS_distance.distance(camtrans,[0,0,0],mode='vector')

		#sclRate=0.25#とりあえずどれくらいの大きさにするか？
		sclRate = 0.2
		size = distance * sclRate
		if size < 10:		size = 10
		elif size < 25:		size = 25
		elif size < 50:		size = 50
		elif size < 100:	size = 100
		elif size < 250:	size = 250
		elif size < 500:	size = 500
		elif size < 1000:	size = 1000
		elif size < 2500:	size = 2500
		elif size < 5000:	size = 5000
		elif size < 10000:	size = 10000
		elif size < 25000:	size = 25000
		elif size < 50000:	size = 50000
		elif size < 100000:	size = 100000
		else :			size = 1000000

		self.scl = [size,size,size]

	#Misc Method

	def getFrom_getBestBB(self):
		if self.comp:
			fin=MS_getBestBB.getBestBB(self.comp)
			self.trn=[fin[0],fin[1],fin[2]]
			self.rot=[fin[3],fin[4],fin[5]]
			self.scl=[fin[6],fin[7],fin[8]]

		else:
			self.comp=cmds.polyListComponentConversion(self.obj,tf=True)
			fin=MS_getBestBB.getBestBB(self.comp)
			self.trn=[fin[0],fin[1],fin[2]]
			self.rot=[fin[3],fin[4],fin[5]]
			self.scl=[fin[6],fin[7],fin[8]]

			###self.trn=MS_getBestBB.bbCenter(self.obj)
			###self.rot=[0,0,0]
			###self.scl=MS_getBestBB.BBMesure(self.obj)

	def simpleBB(self):
		if self.comp:
			self.trn=MS_getBestBB.bbCenter(self.comp)
			self.rot=[0,0,0]
			self.scl=MS_getBestBB.BBMesure_new(self.comp)
		else:
			self.trn=MS_getBestBB.bbCenter(self.obj)
			self.rot=[0,0,0]
			self.scl=MS_getBestBB.BBMesure(self.obj)

	##################
	#ditect transform
	##################
	def autoAxis(self):#AXIS自動判別 (今は一番小さいスケールにaxis)
		if self.scl.index(min(self.scl))==0:
			self.axis=[1,0,0]
		if self.scl.index(min(self.scl))==1:
			self.axis=[0,1,0]
		if self.scl.index(min(self.scl))==2:
			self.axis=[0,0,1]

	def GetTransform(self): #選択オブジェクトの型を見てメソッド振り分け。

		self.__init__()#クラスを初期化

		#オブジェクト取得
		self.obj = cmds.ls(sl=True,type=('transform','joint'),l=True)
		self.comp = cmds.filterExpand(sm = [31,32,34,70])

		### getOption from UI ###
		if cmds.radioCollection('MS_primitives_rotateMethod',ex=True):
			self.rotatemode=cmds.radioCollection('MS_primitives_rotateMethod',q=True,sl=True)

		if cmds.radioCollection('MS_primitives_scaleMethod',ex=True):
			self.scalemode=cmds.radioCollection('MS_primitives_scaleMethod',q=True,sl=True)

		if cmds.floatField('scaleFilterMIN',ex=True):
			self.scaleFilterMIN=cmds.floatField('scaleFilterMIN',q=True,v=True)

		if cmds.floatField('scaleFilterMAX',ex=True):
			self.scaleFilterMAX=cmds.floatField('scaleFilterMAX',q=True,v=True)

		### typeDitect ###
		if self.obj:
			shapeType = cmds.nodeType(self.obj[0])
			if shapeType == 'transform' :
				shape = cmds.listRelatives(self.obj[0],s=True,f=True)
				if shape:
					shapeType = cmds.nodeType(cmds.listRelatives(self.obj[0],s=True,f=True)[0])
		else:
			shapeType = ['none']

		#############
		### 値取得 ###
		#############

		### メッシュオブジェクト選択時 ###
		if shapeType in ['mesh']:
			# bestBBmethod
			if self.rotatemode=='rm_auto' and self.scalemode=='scl_auto':
				self.getFrom_getBestBB()
			else:
				### getTrn ###

				self.trn=MS_getBestBB.bbCenter(self.obj)


				#### getRot ###

				if len(self.obj)>1:#複数選択時
					self.rot=[0,0,0]
				else:
					self.rot=cmds.xform(self.obj,q=True,ro=True,ws=True)


				### getScl ###

				if cmds.nodeType(self.obj[0])=='transform':
					if  self.scalemode=='SimpleScale': #ScaleAttr
						self.scl=cmds.xform(self.obj,q=True,s=True,ws=True)
						
					elif  self.scalemode=='BBMesure' or self.scalemode=='scl_auto': #BBMesure
						if len(self.obj)>1: #複数選択時
							self.scl=MS_getBestBB.BBMesure_multi(self.obj)
						else:
							self.scl=MS_getBestBB.BBMesure(self.obj)

					else: #スケールなし
						self.scl=[1,1,1]

				else:
					self.scl=[1,1,1]


		### Joint選択時 ###
		elif shapeType in ['joint']:
			self.trn = cmds.xform(self.obj,q=True,t=True,ws=True)
			self.rot=cmds.getAttr(self.obj[0]+'.jointOrient')[0]
			self.scl=[1,1,1]

		elif shapeType in ['particle','pointEmitter','joint']:#その他のオブジェクト選択時
			self.trn = cmds.xform(self.obj,q=True,t=True,ws=True)
			self.rot = cmds.xform(self.obj,q=True,ro=True,ws=True)
			self.scl = cmds.xform(self.obj,q=True,s=True,ws=True)

		### コンポーネント選択時 ###
		elif self.comp:
			# bestBBmethod
			if self.rotatemode=='rm_auto' and self.scalemode=='scl_auto':
				self.getFrom_getBestBB()
				
			else:
				#trasform
				self.trn=MS_getBestBB.bbCenter(self.comp)

				#rotation
				if  self.rotatemode=='rm_auto':
					self.simpleBB()
				elif  self.rotatemode=='rm_normal':
					self.getRotFromConstraint()
				#scale
				if  self.scalemode=='SimpleScale':#ScaleAttr
					self.simpleBB()
				elif  self.scalemode=='BBMesure':#BBMesure
					self.scl = MS_getBestBB.BBMesure(self.comp)
				else:
					self.scl = [1,1,1]

		### 非選択時 ###
		elif not self.obj:
			self.sizeFromCamera()

		### 上記以外の選択状態（通常対応） ###
		else:
			# trn
			self.trn = cmds.xform(self.obj,q=True,t=True,ws=True)
			
			# rot
			self.rot=cmds.xform(self.obj,q=True,ro=True,ws=True)

			# scl
			if  self.scalemode=='scl_auto' or self.scalemode=='BBMesure':#BBMesure
				self.scl = MS_getBestBB.BBMesure(self.obj)
			elif  self.scalemode=='SimpleScale':#ScaleAttr
				self.scl=cmds.xform(self.obj,q=True,s=True,ws=True)
			else:
				self.scl = [1,1,1]
		
	#################
	# utility
	#################
	#
	def DoTransform(self):
		cmds.xform(self.newObject,ws=True,t=self.trn,ro=(self.rot[0],self.rot[1],self.rot[2]),s=self.scl)

	#　debugutil
	def DebugTrn(self):
		print self.newObject
		print self.trn
		print self.rot
		print self.scl

#################
# Utility
#################

### Roatate Ditection ###

def componentNormalAverage(COMP):
	#いろんなコンポーネントで法線ベクトルの平均値を帰す
	#フェースやエッジから法線平均値取るのに便利
	#モチロンバーテックスでも使えるよ。
	RET=[0.0,0.0,0.0]
	VVV=cmds.polyListComponentConversion(COMP,tvf=True)
	NRM=cmds.polyNormalPerVertex(VVV,q=True,xyz=True)
	NUM=0
	vecs=[]
	while NUM<len(NRM):
		vecs.append([NRM[NUM],NRM[NUM+1],NRM[NUM+2]])
		NUM+=3
	RET=MS_vector.getAverage(vecs)
	return RET
	
#################
# TransferAttributes
#################

def MS_transferAttributes(SRC,DST):

	cmds.polySoftEdge(DST,a=180)
	
	cmds.select(SRC[0],r=True)
	cmds.select(DST[0],tgl=True)

	mel.eval('performTransferAttributes 0')

	# transferShadingSets
	if cmds.checkBox('MS_transferAttributes_transferShadingSets',q=True,v=True):
		cmds.transferShadingSets( sampleSpace=1 )


###################
# create primitives
###################

#mcp=createPrimitive()

### サブディビジョン作成関数 ###

def GetSubdCircleG2(SCALE=[1,1,1],AXIS='Y'):#グラビティ２最適分割数算出
	
	SUBD_RATE = cmds.floatSliderGrp('interactiveSubdivision_controller',q=True,v=True)

	if AXIS=='X':RADIUS=(SCALE[1]+SCALE[2])*0.5
	if AXIS=='Y':RADIUS=(SCALE[0]+SCALE[2])*0.5
	if AXIS=='Z':RADIUS=(SCALE[0]+SCALE[1])*0.5
	RET=8
	if RADIUS<6:RET=6
	elif RADIUS<11:RET=8
	elif RADIUS<16:RET=10
	elif RADIUS<21:RET=12
	elif RADIUS<31:RET=14
	elif RADIUS<41:RET=16
	elif RADIUS<51:RET=18
	elif RADIUS<61:RET=20
	elif RADIUS<71:RET=22
	elif RADIUS<81:RET=24
	elif RADIUS<91:RET=26
	elif RADIUS<101:RET=28
	else:RET=30

	return RET*SUBD_RATE

def GetSubdTorusG2(SCALE=[1,1,1]):#グラビティ２最適分割数算出

	SUBD_RATE = cmds.floatSliderGrp('interactiveSubdivision_controller',q=True,v=True)
	
	RET=8
	if SCALE[0]<10:RET=4
	elif SCALE[0]<100:RET=6
	elif SCALE[0]<200:RET=8
	elif SCALE[0]<300:RET=10
	elif SCALE[0]<400:RET=12
	elif SCALE[0]<500:RET=14
	else:RET=16

	return RET*SUBD_RATE

def interactiveSubdivision_sphere(obj='',rate=1.0):
	#value from UI
	rate=cmds.floatSliderGrp('interactiveSubdivision_controller',q=True,v=True)

	shape=cmds.listRelatives(obj,s=True,f=True)[0]
	node=cmds.listConnections(shape,type='polySphere')[0]
	cmds.expression(
		alwaysEvaluate=True
		,name=obj+'interactiveSubdivision_sphere'
		,object=node
		,string=(
			node+'.subdivisionsHeight = ('+obj+'.scaleY*0.5+2)*'+str(rate)+';\n'
			+node+'.subdivisionsAxis = (('+obj+'.scaleX+'+obj+'.scaleZ)*0.66+2)*'+str(rate)+';'
			)
		,unitConversion='all'
		)

def interactiveSubdivision_cube(obj='',rate=1.0):
	
	#value from UI
	rate=cmds.floatSliderGrp('interactiveSubdivision_controller',q=True,v=True)

	shape=cmds.listRelatives(obj,s=True,f=True)[0]
	node=cmds.listConnections(shape,type='polyCube')[0]
	cmds.expression(
		alwaysEvaluate=True
		,name=obj+'interactiveSubdivision_cube'
		,object=node
		,string=(
			'float $rate = `floatSliderGrp -q -v "interactiveSubdivision_controller"`;\n'
			+'subdivisionsWidth = ('+obj+'.scaleX*0.5)*$rate;\n'
			+'subdivisionsHeight = ('+obj+'.scaleY*0.5)*$rate;\n'
			+'subdivisionsDepth = ('+obj+'.scaleZ*0.5)*$rate;\n'
			)
		,unitConversion='all'
		)

def interactiveSubdivision_cylinder(obj='',rate=1.0):
	
	#value from UI
	rate=cmds.floatSliderGrp('interactiveSubdivision_controller',q=True,v=True)

	shape=cmds.listRelatives(obj,s=True,f=True)[0]
	node=cmds.listConnections(shape,type='polyCylinder')[0]
	cmds.expression(
		alwaysEvaluate=True
		,name=obj+'interactiveSubdivision_cylinder'
		,object=node
		,string=(
			'subdivisionsAxis = (('+obj+'.scaleX+'+obj+'.scaleZ)*0.66+2)*'+str(rate)+';\n'
			+'subdivisionsHeight = ('+obj+'.scaleY*0.5)*'+str(rate)+';\n'
			+'subdivisionsCaps = (('+obj+'.scaleX+'+obj+'.scaleZ)*0.1)*'+str(rate)+';'
			)
		,unitConversion='all'
		)

### プリミティブ作成関数 ###

def MS_polySphere():
	mcp=createPrimitive()
	mcp.GetTransform()
	mcp.scaleFilter()
	if not mcp.scalemode=='SimpleScale':
		mcp.scaleAverage()
	SUBD=GetSubdCircleG2(mcp.scl)#分割数を最適化
	mcp.newObject=cmds.polySphere(
		axis = mcp.axis,
		constructionHistory = mcp.constructionHistory, 
		createUVs = mcp.createUVs, 
		name = mcp.name, 
		object = mcp.object, 
		radius = mcp.radius, 
		subdivisionsX = SUBD,
		subdivisionsY = SUBD*0.5
		)
	mcp.DoTransform()

	if cmds.checkBox('enable_interactiveSubdivision',q=True,v=True):
		interactiveSubdivision_sphere(mcp.newObject[0])


	return mcp.newObject

def MS_polyCube():
	mcp=createPrimitive()
	mcp.GetTransform()
	mcp.scaleFilter()
	mcp.newObject=cmds.polyCube(
		axis=[0,1,0],
		width=1,
		height=1,
		depth=1,
		subdivisionsX = mcp.subdivisions.cube.x,
		subdivisionsY = mcp.subdivisions.cube.y,
		subdivisionsZ = mcp.subdivisions.cube.z
		)
	mcp.DoTransform()
	if cmds.checkBox('enable_interactiveSubdivision',q=True,v=True):
		interactiveSubdivision_cube(mcp.newObject[0])

	return mcp.newObject

def MS_polyCylinderY():
	mcp=createPrimitive()
	mcp.GetTransform()

	#radius平均化
	av=(mcp.scl[0]+mcp.scl[2])*0.5
	mcp.scl[0]=av
	mcp.scl[2]=av
	mcp.scaleFilter()
	#分割数を最適化
	if cmds.checkBox('SUBD_RATE_ABS',q=True):
		SUBD=int(cmds.floatSliderGrp('interactiveSubdivision_controller',q=True,v=True))
	else:
		SUBD=GetSubdCircleG2(mcp.scl,AXIS='Y')

	mcp.newObject=cmds.polyCylinder(
		axis=[0,1,0],
		radius=mcp.radius,
		height=1,
		subdivisionsX = SUBD,
		subdivisionsY = mcp.subdivisions.cylinder.y,
		subdivisionsZ = mcp.subdivisions.cylinder.z
		)
	mcp.DoTransform()


	if cmds.checkBox('enable_interactiveSubdivision',q=True,v=True):
		interactiveSubdivision_cylinder(mcp.newObject[0])
	#mcp.DebugTrn()
	return mcp.newObject

def MS_polyCylinderX():
	mcp=createPrimitive()
	mcp.GetTransform()
	
	#radius平均化
	av=(mcp.scl[1]+mcp.scl[2])*0.5
	mcp.scl[1]=av
	mcp.scl[2]=av
	mcp.scaleFilter()

	#分割数を最適化
	SUBD=GetSubdCircleG2(mcp.scl,AXIS='X')

	mcp.newObject=cmds.polyCylinder(
		axis=[0,1,0],
		radius=mcp.radius,
		height=1,
		subdivisionsX = SUBD,
		subdivisionsY = mcp.subdivisions.cylinder.y,
		subdivisionsZ = mcp.subdivisions.cylinder.z
		)
	mcp.DoTransform()

	if cmds.checkBox('enable_interactiveSubdivision',q=True,v=True):
		interactiveSubdivision_cylinder(mcp.newObject[0])
	#mcp.DebugTrn()
	return mcp.newObject

def MS_polyCylinderZ():
	mcp=createPrimitive()
	mcp.GetTransform()
	
	#radius平均化
	av=(mcp.scl[0]+mcp.scl[1])*0.5
	mcp.scl[0]=av
	mcp.scl[1]=av
	mcp.scaleFilter()

	#分割数を最適化
	SUBD=GetSubdCircleG2(mcp.scl,AXIS='Z')

	mcp.newObject=cmds.polyCylinder(
		axis=[0,0,1],
		radius=mcp.radius,
		height=1,
		subdivisionsX = SUBD,
		subdivisionsY = mcp.subdivisions.cylinder.y,
		subdivisionsZ = mcp.subdivisions.cylinder.z
		)
	mcp.DoTransform()

	if cmds.checkBox('enable_interactiveSubdivision',q=True,v=True):
		interactiveSubdivision_cylinder(mcp.newObject[0])
	#mcp.DebugTrn()
	return mcp.newObject

def MS_polyCone():
	mcp=createPrimitive()
	mcp.GetTransform()
	mcp.scaleFilter()
	scl=[i*0.5 for i in mcp.scl]
	
	#分割数を最適化
	SUBD=GetSubdCircleG2(mcp.scl,AXIS='Z')

	mcp.newObject=cmds.polyCone(
		axis = mcp.axis,
		name = mcp.name, 
		height = mcp.height,
		radius = mcp.radius, 
		subdivisionsX = SUBD, 
		subdivisionsY = mcp.subdivisions.cone.y,
		subdivisionsZ = mcp.subdivisions.cone.z
		)
	mcp.DoTransform()

	#mcp.DebugTrn()
	return mcp.newObject

def MS_polyPlane(subX=0,subY=0):
	mcp=createPrimitive()
	mcp.GetTransform()
	mcp.scaleFilter()
	mcp.GetSubdivision()

	#subd
	if not subX:
		subX=mcp.subdivisions.plane.x
	if not subY:
		subY=mcp.subdivisions.plane.y

	mcp.newObject=cmds.polyPlane(
		width=1,
		height=1,
		subdivisionsX = subX,
		subdivisionsY = subY
		)
	mcp.DoTransform()

	return mcp.newObject

def MS_polyTorus():
	mcp=createPrimitive()
	mcp.GetTransform()
	mcp.scaleFilter()
	SUBD=GetSubdCircleG2(mcp.scl)#分割数を最適化

	SUBDY=GetSubdTorusG2(mcp.scl)#分割数を最適化

	mcp.newObject=cmds.polyTorus(
		axis=[0,1,0],
		radius=0.5,
		sectionRadius=0.25,
		twist=0.0,
		subdivisionsX = SUBD,
		subdivisionsY = SUBDY
		)
	mcp.DoTransform()
	return mcp.newObject

def MS_polyPyramid():
	mcp=createPrimitive()
	mcp.GetTransform()
	mcp.scaleFilter()
	mcp.newObject=cmds.polyPyramid(
		axis=[0,1,0],
		sideLength=1.0,
		numberOfSides=3,
		subdivisionsCaps = mcp.subdivisions.pyramid.x,
		subdivisionsHeight = mcp.subdivisions.pyramid.y
		)
	mcp.DoTransform()

	#mcp.DebugTrn()
	return mcp.newObject

def MS_polyPipe():
	mcp=createPrimitive()
	mcp.GetTransform()
	mcp.scaleFilter()
	SUBD=GetSubdCircleG2(mcp.scl)#分割数を最適化
	mcp.newObject=cmds.polyPipe(
		axis=[0,1,0],
		radius=0.5,
		height=1.0,
		thickness=0.25,
		subdivisionsAxis = SUBD,
		subdivisionsCaps = mcp.subdivisions.pyramid.x,
		subdivisionsHeight = mcp.subdivisions.pyramid.y
		)
	mcp.DoTransform()

	#mcp.DebugTrn()
	return mcp.newObject

def MS_locator():
	mcp=createPrimitive()
	mcp.GetTransform()
	#mcp.trn=MS_getBestBB.BBCenterByObj()
	#mcp.trn=MS_getBestBB.bbCenter()
	mcp.newObject=cmds.spaceLocator()

	mcp.DoTransform()
	#cmds.xform(mcp.newObject,ws=True,t=mcp.trn,ro=(mcp.rot[0],mcp.rot[1],mcp.rot[2]))
	#cmds.xform(mcp.newObject,ws=True,t=mcp.trn,ro=(mcp.rot[0],mcp.rot[1],mcp.rot[2]))

	#SHAPE=cmds.listRelatives(mcp.newObject,s=True)
	#cmds.setAttr(SHAPE[0]+'.localScaleX',50)
	#cmds.setAttr(SHAPE[0]+'.localScaleY',50)
	#cmds.setAttr(SHAPE[0]+'.localScaleZ',50)
	#mcp.getRotFromConstraint()
	
	#mcp.DoTransform()
	return mcp.newObject

def MS_multi(FUNCTION):

	#DELFLAG
	mods = cmds.getModifiers()
	if (mods & 4) > 0: DELETE_ORIGIN_FLAG=True
	else:DELETE_ORIGIN_FLAG=False

	#SELECT
	SEL=cmds.ls(sl=True,l=True,typ='transform')
	if not SEL:
		SEL=cmds.filterExpand(sm=[31,32,34,35],ex=True)
	if not SEL:
		FUNCTION()
		return

	NEW=[]
	if not cmds.checkBox('keep_face_together',q=True,v=True):

		#　選択数が多いときに実行確認
		if len(SEL)>4:
			DS=cmds.confirmDialog(m=u'Too many selected.\ncontinue? ',button=['yes','No'],defaultButton='yes',cancelButton='No',dismissString='No')
			if DS=='No':
				return

		for EACH in SEL:
			cmds.select(EACH,r=True)
			PRENEW=FUNCTION()
			if cmds.checkBox('transferAttributes',q=True,v=True):
				MS_transferAttributes(EACH,[PRENEW[0]])
			NEW.append(PRENEW[0])
	else:
		PRENEW=FUNCTION()
		if cmds.checkBox('transferAttributes',q=True,v=True):
			MS_transferAttributes(SEL,[PRENEW[0]])
		NEW.append(PRENEW[0])
	#DELETE
	if DELETE_ORIGIN_FLAG:
		cmds.delete(SEL)
	cmds.select(NEW,r=True)

#################
# UI
#################

def layoutPrimitives(
	LABEL='MS_primitives'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	msp=createPrimitive()
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	#
	cmds.gridLayout(nc=5)
	cmds.iconTextButton( style='iconOnly', image1='polySphere.xpm', label='sphere',c=lambda *args:MS_multi(MS_polySphere) )
	cmds.iconTextButton( style='iconOnly', image1='polyCube.xpm', label='polyCube',c=lambda *args:MS_multi(MS_polyCube) )
	cmds.iconTextButton( style='iconOnly', image1='polyCylinder.xpm', label='polyCylinder_V',c=lambda *args:MS_multi(MS_polyCylinderY) )
	cmds.iconTextButton( style='iconOnly', image1='polyCylinder.xpm', label='polyCylinder_H',c=lambda *args:MS_multi(MS_polyCylinderX) )
	cmds.iconTextButton( style='iconOnly', image1='polyCylinder.xpm', label='polyCylinder_H',c=lambda *args:MS_multi(MS_polyCylinderZ) )
	cmds.iconTextButton( style='iconOnly', image1='polyCone.xpm', label='polyCone',c=lambda *args:MS_multi(MS_polyCone) )
	cmds.iconTextButton( style='iconOnly', image1='polyMesh.xpm', label='polyMesh',c=lambda *args:MS_multi(MS_polyPlane) )
	cmds.iconTextButton( style='iconOnly', image1='polyTorus.xpm', label='polyTorus',c=lambda *args:MS_multi(MS_polyTorus))
	cmds.iconTextButton( style='iconOnly', image1='polyPyramid.xpm', label='polyPyramid',c=lambda *args:MS_multi(MS_polyPyramid))
	cmds.iconTextButton( style='iconOnly', image1='polyPipe.xpm', label='polyPipe',c=lambda *args:MS_multi(MS_polyPipe))
	cmds.setParent('..')
	#
	cmds.rowLayout(nc=5)
	cmds.iconTextButton( style='iconOnly', image1='locator.xpm', label='locator',c=lambda *args:MS_multi(MS_locator) )
	cmds.setParent('..')

	#keep_face_together
	cmds.checkBox('keep_face_together',l='keep face together',v=True)
	cmds.separator(w=200)

	#scaleFiletr
	cmds.separator(w=200)
	cmds.rowLayout(nc=5,cw5=[30,20,60,20,60],ann=u'スケール値の最小最大サイズ設定\n')
	cmds.text(l='scale')
	cmds.text(l='min')
	cmds.floatField('scaleFilterMIN',v=1.0)
	cmds.text(l='max')
	cmds.floatField('scaleFilterMAX',v=10000.0)
	cmds.setParent('..')
	cmds.separator(w=200)
	#
	cmds.checkBox('extendComponentToFace',v=1)

	cmds.setParent('..')
	cmds.setParent('..')

def layoutOptions(WIDTH=217,BGC=[0.2,0.2,0.2]):

	def layoutScaleMethod(WIDTH,BGC):
		#radio scaleMethod
		cmds.frameLayout('scaleMethod_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l='scaleMethod',cll=True,cl=True)
		cmds.columnLayout()
		cmds.rowLayout(nc=2,cw2=[80,100])
		cmds.columnLayout()
		cmds.text(l='scaleMethod')
		cmds.setParent('..')
		cmds.columnLayout()
		cmds.radioCollection('MS_primitives_scaleMethod')
		cmds.radioButton('scl_auto',l='auto',sl=True)	
		cmds.radioButton('SimpleScale',l='SimpleScale')
		cmds.radioButton('BBMesure',l='BBMesure')
		cmds.radioButton('scl_none',l='none')
		cmds.setParent('..')
		cmds.setParent('..')
		cmds.setParent('..')
		cmds.setParent('..')

	def layoutRotationMethod(WIDTH,BGC):
		#radio rotationMethod
		cmds.frameLayout('rotationMethod_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l='rotationMethod',cll=True,cl=True)
		cmds.columnLayout()
		cmds.rowLayout(nc=2,cw2=[80,100],ann=u'normal　＝　ノーマルコンストレインからローテーションを取得\n')
		cmds.columnLayout()
		cmds.text(l='rotationMethod')
		cmds.setParent('..')
		cmds.columnLayout()
		cmds.radioCollection('MS_primitives_rotateMethod')
		cmds.radioButton('rm_auto',l='auto',sl=True)
		cmds.radioButton('rm_normal',l='normal')
		cmds.radioButton('rm_none',l='none')
		cmds.setParent('..')
		cmds.setParent('..')
		cmds.setParent('..')

	layoutScaleMethod(WIDTH,BGC)
	cmds.separator(w=200)
	layoutRotationMethod(WIDTH,BGC)
	cmds.separator(w=200)
	cmds.setParent('..')

def layoutUtil(WIDTH=217,BGC=[0.2,0.2,0.2]):
	def layoutSubdivisions():
		#Subdivisions
		cmds.frameLayout('subivisions_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l='subdivisions option',cll=True,cl=False)
		cmds.columnLayout()
		cmds.text('subdivisions rate')
		cmds.floatSliderGrp('interactiveSubdivision_controller',f=True,v=1.0,min=0.1,max=10)
		cmds.checkBox('SUBD_RATE_ABS',l='absolute subdivide',v=False)
		cmds.checkBox('enable_interactiveSubdivision',v=False,bgc=[0.6,0.5,0.4])
		cmds.setParent('..')
		cmds.setParent('..')

	def layoutTransferAttributes(
		LABEL='MS_transferAttributes_util'
		,WIDTH=217
		,BGC=[0.2,0.2,0.2]
		,CL=False
		):

		cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
		cmds.columnLayout()

		#transferAttributes
		cmds.checkBox('transferAttributes',l='*transferAttributes',v=False,bgc=[0.6,0.5,0.4])
		cmds.checkBox('MS_transferAttributes_transferShadingSets',l='ShadingSets',v=True)
		cmds.iconTextButton( style='iconAndTextHorizontal', image1='polyTransferAttributes.png', label='open transferAttributes option',c=lambda *args:mel.eval('performTransferAttributes 1;') )

		cmds.setParent('..')
		cmds.setParent('..')


	layoutSubdivisions()
	layoutTransferAttributes()
	#layoutPivotSetter()


def UI():
	if cmds.window('MS_primitives_main_window',q=True,ex=True):
		cmds.deleteUI('MS_primitives_main_window')
	cmds.window('MS_primitives_main_window',rtf=True,s=True)
	
	layoutPrimitives()

	layoutOptions()
	
	layoutUtil()

	print 'catch : '+os.path.abspath(__file__)

	cmds.window('MS_primitives_main_window',e=True,w=217,h=640)

	cmds.showWindow('MS_primitives_main_window')

#UI()

