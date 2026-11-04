# -*- coding:utf-8 -*-
import maya.cmds as cmds
import csv
from xml.etree.ElementTree import ElementTree

import subprocess
import os

import math,copy

##### 
def filetest():
	output=subprocess.Popen('d:/Mproject/ToroTool.exe')
	print output

def componentNormalAverage(COMP):
	#いろんなコンポーネントで法線ベクトルの平均値を帰す
	#フェースやエッジから法線平均値取るのに便利
	#モチロンバーテックスでも使えるよ。
	PRET=[0.0,0.0,0.0]
	RET=[0.0,0.0,0.0]
	VVV=cmds.polyListComponentConversion(COMP,tv=True)
	NRM=cmds.polyNormalPerVertex(VVV,q=True,xyz=True)
	NUM=0
	while NUM<len(NRM)/3:
		PRET[0]=PRET[0]+NRM[NUM]
		PRET[1]=PRET[1]+NRM[NUM+1]
		PRET[2]=PRET[2]+NRM[NUM+2]
		NUM+=3
	try:
		RET[0]=(PRET[0]/(len(NRM)/3))
	except:
		RET[0]=0
	try:
		RET[1]=(PRET[1]/(len(NRM)/3))
	except:
		RET[1]=0
	try:
		RET[2]=(PRET[2]/(len(NRM)/3))
	except:
		RET[2]=0
	return RET


def globalAngleCheck(vec):
	#ベクトルをグローバル座標系で回転値に変換、戻り値はXとZ
	OUT=[]
	xyLength = math.sqrt((vec[0]) * (vec[0]) +(vec[1]) * (vec[1]))
	vecLength = math.sqrt((vec[0]) * (vec[0]) +(vec[1]) * (vec[1]) +  (vec[2]) * (vec[2]))
	# $xyLength will be zero when $vec is pointing
	# along the +z or -z axis
	if xyLength == 0:
		if (vec[0]) > 0:
			zAngle = mel.eval('deg_to_rad(90);')
		else:
			zAngle = mel.eval('deg_to_rad(-90);')
	else:
		zAngle = mel.eval('acos(%s);'%(float(vec[1])/xyLength))
	
	xAngle = mel.eval('acos(%s);'%(xyLength/vecLength))
	if  vec[2]<= 0:
		xAngle = -xAngle
	OUT.append(mel.eval('rad_to_deg(%s);'%xAngle))
	if vec[0]>0:
		zAngle = -zAngle
	OUT.append(mel.eval('rad_to_deg(%s);'%zAngle))
	return OUT



	
def getRot(SEL=[]):
	RET=[]
	if not SEL:
		SEL=cmds.ls(sl=True)
	if SEL:
		RET=cmds.xform(SEL,q=True,ws=True,ro=True)
	else:
		RET=[0.0,0.0,0.0]
	return RET
	
def getScl(SEL=[]):
	
	RET=[]
	if not SEL:
		SEL=cmds.ls(sl=True)
	COMP=cmds.filterExpand(SEL,ex=True,sm=(31,32,34,35,47))
	if COMP:
		RET=BBMesure(COMP)
		RET.append(1)
	elif SEL:
		RET=BBMesure(SEL)
		#RET=cmds.xform(q=True,ws=True,s=True)
		RET.append(0)
	else:
		RET=[1.0,1.0,1.0,0]
	if RET[0]<=0:
		RET[0]=1
	if RET[1]<=0:
		RET[1]=1
	if RET[2]<=0:
		RET[2]=1
		
	return RET
	
	
def getTransform(OBJ='',COMPS=[],CENTERMODE='',BBMODE='',ROTMODE=''):
	RET=[]
	DUPED=cmds.duplicate(OBJ)
	
	#componentFunction
	DUPEDCOMP=[]
	for EACHCOMP in COMPS:
		TEMP=EACHCOMP.split('.')
		TEMP[0]=DUPED[0]
		DUPEDCOMP.append('.'.join(TEMP))
	
	#getRotation
	if ROTMODE=='normalAverage':
		rotToNormalAverage(DUPED[0],DUPEDCOMP,AIM_VECTOR=[0,1,0])
		ROT=getRot(DUPED[0])
	
	else:
		#print 'non normalAverage'
		ROT=getRot(DUPED[0])
	
	
	#getBB
	#
	cmds.setAttr(DUPED[0]+'.rx',0)
	cmds.setAttr(DUPED[0]+'.ry',0)
	cmds.setAttr(DUPED[0]+'.rz',0)
	
	cmds.makeIdentity(DUPED[0],a=True,t=False,r=False,s=True)
	if BBMODE=='compornent':
		if len(DUPEDCOMP)==1 and CENTERMODE=='face':
			DUPEDCOMP=getFaces(DUPEDCOMP)
		TRN=bbCenter(COMPS)
		SCL=BBMesure(DUPEDCOMP)
	else:
		#print 'non COMPONENT'
		TRN=bbCenter(DUPED[0])
		SCL=BBMesure(DUPED[0])
		#print SCL
	####
	
	if SCL[0]<0.01:
		SCL[0]=1
	if SCL[1]<0.01:
		SCL[1]=1
	if SCL[2]<0.01:
		SCL[2]=1
	if DUPED:
		cmds.delete(DUPED[0])
	#
	
	RET.extend(TRN)
	RET.extend(ROT)
	RET.extend(SCL)
	
	return RET
	
def BBVolume(OBJ):
	MESURE=BBMesure(OBJ)
	Volume=MESURE[0]*MESURE[1]*MESURE[2]
	return Volume
	
#####コンポーネント選択

def getFaces(COMP):#フェース選択
	FACE=cmds.polyListComponentConversion(COMP,tf=True)
	result=cmds.filterExpand(FACE,ex=True,sm=34)
	return result
	
def getVerts(COMP):#頂点選択
	VTX=cmds.polyListComponentConversion(COMP,tv=True)
	result=cmds.filterExpand(VTX,ex=True,sm=31)
	return result
	
def getEdges(COMP):#エッジ選択
	EDGE=cmds.polyListComponentConversion(COMP,te=True)
	result=cmds.filterExpand(EDGE,ex=True,sm=32)
	return result

def getVertsFaces(COMP):#フェース頂点選択
	FACE=cmds.polyListComponentConversion(COMP,tvf=True)
	result=cmds.filterExpand(FACE,ex=True,sm=70)
	return result
	
def selectFaceEdge():
	#選択オブジェクトの境界線
	BORDER_EDGES=[]
	FACE=cmds.filterExpand(sm=34)
	BORDER_EDGES=cmds.polyListComponentConversion(FACE,fv=True,ff=True,fuv=True,fvf=True,te=True,bo=True)
	return BORDER_EDGES
	
##### BB util
	
def BBMesure(OBJ):
	if not OBJ:
		return [1,1,1]
	FACE=getFaces(OBJ)
	#ポリゴンバウンディングボックス面積
	cmds.select(FACE,r=True)
	
	BB=cmds.xform(FACE,q=True,ws=True,bb=True)
	RET=[(BB[3]-BB[0]),(BB[4]-BB[1]),(BB[5]-BB[2])]
	
	return RET
	
def bbCenter(COMP=[]):
	COMP=getVerts(COMP)
	
	if not COMP:
		return [0.0,0.0,0.0]
		
	if COMP:
		cmds.select(COMP,r=True)
		PREBB=cmds.polyEvaluate(COMP,bc=True,ae=True)
		BBOX=[]
		BBOX.append(PREBB[0][0])
		BBOX.append(PREBB[1][0])
		BBOX.append(PREBB[2][0])
		BBOX.append(PREBB[0][1])
		BBOX.append(PREBB[1][1])
		BBOX.append(PREBB[2][1])
		
	TRN=[]
	TRN.append((BBOX[0]+BBOX[3])*0.5)
	TRN.append((BBOX[1]+BBOX[4])*0.5)
	TRN.append((BBOX[2]+BBOX[5])*0.5)
	return TRN
	
def bbCenterX(OBJ=[]):
	if not OBJ:
		return [0.0,0.0,0.0]
		
	if OBJ:
		BBOX=cmds.xform(OBJ,q=True,ws=True,bb=True)
		
	TRN=[]
	TRN.append((BBOX[0]+BBOX[3])*0.5)
	TRN.append((BBOX[1]+BBOX[4])*0.5)
	TRN.append((BBOX[2]+BBOX[5])*0.5)
	return TRN
	

##### vector
	
def vectorMove(OBJ='',VAR=0.0):
	#ソースオブジェクトの回転軸Y方向にVAR分移動した座標を返す
	MATRIX=cmds.getAttr(OBJ+'.worldMatrix')
	return [MATRIX[4]*VAR,MATRIX[5]*VAR,MATRIX[6]*VAR]
	
def vectorRot(MATRIX, ANGLE, AXIS):
	#ベクトルの回転
	# float[11] MATRIX=掛け合わせの対象となる行列:
	# float ANGLE=回転値（ラジアン）
	# vector3 AXIS=回転軸
	#戻り値：12個のリスト。回転後のベクトルは（dist[8],dist[9],dist[10]）
	SQ = math.sqrt(AXIS[0] * AXIS[0] + AXIS[1] * AXIS[1] + AXIS[2] * AXIS[2])
	if not SQ:
		return
	a = AXIS[0]
	b = AXIS[1]
	c = AXIS[2]
	if not SQ == 1:
		SQ = 1 / SQ
		a *= SQX
		b *= SQ
		c *= SQ
	d = math.sin(ANGLE)
	e = math.cos(ANGLE)
	f = 1 - e
	g = MATRIX[0]
	h = MATRIX[1]
	i = MATRIX[2]
	j = MATRIX[3]
	k = MATRIX[4]
	l = MATRIX[5]
	m = MATRIX[6]
	n = MATRIX[7]
	o = MATRIX[8]
	p = MATRIX[9]
	q = MATRIX[10]
	r = MATRIX[11]
	s = a * a * f + e
	t = b * a * f + c * d
	u = c * a * f - b * d
	v = a * b * f - c * d
	w = b * b * f + e
	x = c * b * f + a * d
	y = a * c * f + b * d
	z = b * c * f - a * d
	A = c * c * f + e
	dest=[]
	dest.append( g * s + k * t + o * u)
	dest.append( h * s + l * t + p * u)
	dest.append(i * s + m * t + q * u)
	dest.append( j * s + n * t + r * u)
	dest.append( g * v + k * w + o * x)
	dest.append( h * v + l * w + p * x)
	dest.append( i * v + m * w + q * x)
	dest.append( j * v + n * w + r * x)
	dest.append( g * y + k * z + o * A)
	dest.append( h * y + l * z + p * A)
	dest.append( i * y + m * z + q * A)
	dest.append( j * y + n * z + r * A)
	return dest
	
	
	
##### 計算 #####
'''
#####ベクター型
class Vector(tuple):
  """
  Vector is a class for vector operation, which is a sub-class of tuple.
  """

	def __neg__(self):
		return Vector([-x for x in self])
	
	def __pos__(self):
		return copy.copy(self)
		
	def __abs__(self):
		"""it returns the magnitude of vector."""
		return math.sqrt(sum([ x * x for x in self]))
	
	def norm(self):
		"""it returns the normarized vector."""
		a = self.__abs__()
		return Vector([x/a for x in self])
		
	def __add__(self, a):
		"""it adds vector and vector."""
		if isinstance(a, Vector):
			if len(self) == len(a):
				return Vector([ x + y for x, y in zip(self, a)])
			else:
				raise ValueError, "Same dimension is required."
		else:
			raise TypeError, "Vector is required."
	
	__iadd__ = __add__
	
	def __sub__(self, a):
		return self.__add__(-a)
	
	__isub__ = __sub__
			
	def __mul__(self, m):
		"""if m is a vector, it calculate the inner product,
		   else if m is a number, it multiplies each element of vector by m."""
		   
		if isinstance(m, Vector):
			if len(self) == len(m):
				return sum([ x * y for x, y in zip(self, m)])
			else:
				raise ValueError, "Same dimension is required."
		elif isnum(m):
			return Vector([ x * m for x in self])
		else:
			raise TypeError, "Vector or number is required."
	
	__rmul__ = __mul__
	
	def __str__(self):
		"""add#V in front of the representation of tuple."""
		return '#V' + tuple.__str__(self)
	
	
	
##### ベクトル演算
def dotproduct(v1, v2):
	return sum((a*b) for a, b in zip(v1, v2))

def length(v):
	return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
	return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))

def RAD2VEC(NODE):
	VEC=cmds.getAttr(NODE+'.worldMatrix') #配列の8, 9, 10が平行光源のベクトル. 
	RET=[VEC[8],VEC[9],VEC[10]]
	return RET
'''
##### リスト連結　#####
def JOIN(LIST,JOIN_STR):
	return JOINTSTR.join(LIST)
	
##### シーン名取得 #####
def GET_SCENE_NAME():
	SN=cmds.file(q=True,sn=True)
	ARRAY=SN.replace('.','/').split('/')
	if SN:
		SCENE_NAME=ARRAY[-2]
	else:
		SCENE_NAME='NewScene'
	return SCENE_NAME
	
###############
##### IO #####
###############
##### ファイルセーブ #####
def SAVE(ROW,FILE_PATH):
	f=open(FILE_PATH,'w')#'r'読み込み：'w'書き込み：'a'追記：'+'読み書き両方' 't'テキストモード：'b'バイナリーモード
	f.write(ROW)
	f.close()
	
##### 階層つきリストファイルセーブ #####
def HRC_SAVE(HRC,FILE_PATH):
	f=open(FILE_PATH,'w')
	for DATA in HRC:
		f.write('>'+DATA+'\n')
	f.close()
	
##### ファイルロード #####
def LOAD(FILE_PATH):
	f=open(FILE_PATH)
	DATA=[]
	for ROW in f:
		DATA.append(ROW)
	f.close()
	return DATA
	
	
##### CSVインポート #####
def CSV_IMPORT(FILE_PATH):
	CSVFILE = open(FILE_PATH)
	DATA=[]
	for ROW in csv.reader(CSVFILE):
		DATA.append(ROW)
	CSVFILE.close()
	return DATA
	
###############
##### XML #####
###############
#http://d.hatena.ne.jp/hikm/20090206/1233950923

##### XML読み込み #####
def XML_LOAD(XML_PATH):
	ELEM=ElementTree(file=open(XML_PATH))
	return ELEM
	
##### XMLパーサー #####
#http://perl.wonder-boys.net/?p=155
class XML_PARSER(object):
	def __init__(self,url,type=file):
		"""XMLを読み込んでitemタグのリストを作る"""
		if type == 'url':
			rss = ElementTree(file=urlopen(url))
		else:
			rss = ElementTree(file=open(url))
		self.root = rss.getroot()
		self.items = rss.findall('//item')
	def get_data(self,arr):
		"""欲しいデータがディクショナリ形式で入ったリストを返す"""
		elm_list = []
		for item in self.items:
			elm_dic={}
			for t in item.getiterator():
				for data in arr:
					if t.tag in data:
						elm_dic[data] = t.text
					else:
						pass
			elm_list.append(elm_dic)
		return elm_list


##### アトリビュートフィルター #####
def attrFilter(ATTR,VALUE,MODE):
	#MODE=[GREATER,GEQUAL,EQUAL,LEQUAL,LESS]
	NODES=cmds.ls(sl=True)
	if not NODES:
		NODES=cmds.ls()
	RESULT=[]
	for EACH in NODES:
		try:
			VAR=cmds.getAttr(EACH+'.'+ATTR)
			if MODE=='GREATER':
				if VAR>VALUE:
					RESULT.append(EACH)
			if MODE=='GREQAL':
				if VAR>=VALUE:
					RESULT.append(EACH)
			if MODE=='EQUAL':
				if VAR==VALUE:
					RESULT.append(EACH)	
			if MODE=='LEQUAL':
				if VAR<=VALUE:
					RESULT.append(EACH)
			if MODE=='LESS':
				if VAR<VALUE:
					RESULT.append(EACH)
		except TypeError:
			pass
	'''
		try:
			SHAPE=cmds.listRelatives(EACH,s=True)
			VAR=cmds.getAttr(SHAPE[0]+'.'+ATTR)
		
			if MODE=='GREATER':
				if VAR>VALUE:
					RESULT.append(EACH)
			if MODE=='GREQAL':
				if VAR>=VALUE:
					RESULT.append(EACH)
			if MODE=='EQUAL':
				if VAR==VALUE:
					RESULT.append(EACH)	
			if MODE=='LEQUAL':
				if VAR<=VALUE:
					RESULT.append(EACH)
			if MODE=='LESS':
				if VAR<VALUE:
					RESULT.append(EACH)
		except TypeError:
			pass
	'''
	if RESULT:
		RESULT_UNIQUE=unique2(RESULT)
		cmds.select(RESULT_UNIQUE,r=True)
		
		TOTAL=len(RESULT_UNIQUE)
	else:
		RESULT_UNIQUE=['No Match ...']
		TOTAL=0
	print '-------result--------'
	for EACH in RESULT_UNIQUE:
		print EACH
	print '-------total--------'
	print TOTAL
	
##### 配列操作 #####

def UNIQUE(LIST):
	#リストから重複要素を取り除く。
	return sorted(set(LIST),key=LIST.index)
	
def unique2(LIST):
	#リストから重複要素を取り除く。リストの並びは要素の登場順になる。
	RET=[]
	for EACH in LIST:
		if not EACH in RET:
			RET.append(EACH)
	return RET

#####ファイル存在確認
	
def filePathExists(PATH):
	ret=os.path.exists(PATH)
	return ret

