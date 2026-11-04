#  coding: utf-8
import maya.cmds as cmds
import maya.OpenMaya as om
import sys, math



def getWorldMatrix(node):
	ret=cmds.getAttr(node+'.worldMatrix')
	return ret
	
def getWorldInverseMatrix(node):
	ret=cmds.getAttr(node+'.worldInverseMatrix')
	return ret
	
def getInverseMatrix(node):
	ret=cmds.getAttr(node+'.inverseMatrix')
	return ret
	
def getParentMatrix(node):
	ret=cmds.getAttr(node+'.parentMatrix')
	return ret
	
def getMatrix(node):
	ret=cmds.getAttr(node+'.matrix')
	return ret
	
def getParentInverseMatrix(node):
	ret=cmds.getAttr(node+'.parentInverseMatrix')
	return ret
	
#vectormath

def pointProduct(wmxa,wmxb):
	ret=[0.0]*16
	for x in [0,4,8]:
		ret[x]	=	(wmxa[x]*wmxb[0])	+(wmxa[x+1]*wmxb[1])	+(wmxa[x+2]*wmxb[2])	+wmxb[3]
		ret[x+1]	=	(wmxa[x]*wmxb[4])	+(wmxa[x+1]*wmxb[5])	+(wmxa[x+2]*wmxb[6])	+wmxb[7]
		ret[x+2]	=	(wmxa[x]*wmxb[8])	+(wmxa[x+1]*wmxb[9])	+(wmxa[x+2]*wmxb[10])	+wmxb[11]
		
	for x in range(12,16):
		ret[x]=wmxa[x]
	print ret
	return ret
	

def sum(ls):
    """リストの要素を合計します。"""
    s=0
    for x in ls:
        s+=x
    return(s)
    	
def easymul(v,m):
	return sum([ x * y for x, y in zip(v, m)])

#vector util
def MVecToList(MVec):
    return (MVec.x,MVec.y,MVec.z)

def vecToRad(vec):
    print vec
    OUT=[0.0,0.0,0,0]
    xA=0.0
    zA=0.0
    xyLen= math.sqrt(vec[0] * vec[0] + vec[1] * vec[1])
    vecLen = math.sqrt(vec[0] * vec[0] + vec[1] * vec[1] + vec[2] * vec[2])

    if xyLen == 0:
        if vec[0] > 0:
            zA = math.radians(90)
        else:
            zA = math.radians(-90)
    else:
        zA = math.acos(vec[1]/xyLen)
    
    if xyLen and vecLen:
        xA = math.acos(xyLen/vecLen)
    else:
        xA = 0

    if vec[2] < 0:
        xA = -xA
    OUT[0] = math.degrees(xA)
    print math.degrees(xA)

    if vec[0] > 0:
        zA = -zA
    OUT[2] = math.degrees(zA)
    print math.degrees(zA)
    return OUT

def getAverage(lav):
    #return average from multi point
    
    if len(lav)<2:
        return(0,1,0)

    ta=lav.pop(0)
    vectA=om.MVector(ta[0],ta[1],ta[2])
    n=0
    while lav:
        tb=lav.pop(0)
        vectA+=om.MVector(tb[0],tb[1],tb[2])
        n+=1
    RET=(vectA/n)
    return MVecToList(RET)


class vv():
    def get(self,*av):

        lav=list(av)[0]

        if len(lav)>=2:
            ret=self.getAvarage(lav)

        return (ret.x,ret.y,ret.z)

    def getAvarage(self,*av):
        #return average from multi point
        lav=list(*av)
        
        if len(lav)<2:
            return(0,1,0)

        ta=lav.pop(0)
        vectA=om.MVector(ta[0],ta[1],ta[2])
        n=0
        while lav:
            tb=lav.pop(0)
            vectA+=om.MVector(tb[0],tb[1],tb[2])
            n+=1
        return (vectA/n)

    def getCrossProduct(self, p1, p2, p3):
        '''
        return the cross product from the 3 points
        '''
        vectA = om.MVector( (p2[0]-p1[0]), (p2[1]-p1[1]), (p2[2]-p1[2]) )
        vectB = om.MVector( (p3[0]-p1[0]), (p3[1]-p1[1]), (p3[2]-p1[2]) )
        vectA.normalize()
        vectB.normalize()
        ret = self.doCrossProduct(vectA, vectB)
        return ret


    def doCrossProduct(self, v1, v2):
        '''
        compute the cross product vectors
        '''
        ret = om.MVector( ((v1.y*v2.z) - (v1.z*v2.y)) , ((v1.z*v2.x) - (v1.x*v2.z)), ((v1.x*v2.y) - (v1.y*v2.x)) )
        ret.normalize()
        return ret




class Vector:
    """
    Vector はベクトル演算のためのクラスです。
    """
    def __init__(self, *rest, **key):
        """
        ベクトルを初期化します。
        要素が渡されたら、その要素からなるベクトルを作ります。
        v1 = Vector(1,2,3)
        次元と初期値が渡されたら初期値 val, 次元 dim のベクトルを作ります。
        val が省略されると初期値は 0 になります。
        v1 = Vector(dim=3, val=3)
        """
        if rest:
            self.v = list(rest)
        else:
            dim = key['dim']
            val = (('val' in key) and key['val']) or 0
            self.v =  [val for x in range(dim)]

    def __len__(self):
        """ベクトルの次元を返します。"""
        return len(self.v)
    
    def abs(self):
        """ベクトルの絶対値を返します。"""
        return math.sqrt(sum([ x * x for x in self.v ]))

    def norm(self):
        """規格化されたベクトルを返します。"""
        a = self.abs()
        b = Vector(dim=len(self))
        b.v = [x/a for x in self.v]
        return b
        
    def __add__(self, a):
        """ベクトルと実数、またはベクトル間の足し算をします。"""
        b = Vector(dim=len(self))
        if isinstance(a, Vector):
            if len(self) != len(a):
                print >> sys.stderr, "Dimension Error"
            else:
                b.v =  [ x + y for x, y in zip(self.v, a.v)]
        else:
            b.v = [ x + a for x in self.v]
        return b
            
    def __mul__(self, m):
        """ベクトルと実数、またはベクトル間の掛け算（内積）をします。"""
        if isinstance(m, Vector):
            if len(self) != len(m):
                print >> sys.stderr, "Dimension Error"
            else:
                return sum([ x * y for x, y in zip(self.v, m.v)])
        else:
            b = Vector(dim=len(self))
            b.v = [ x * m for x in self.v]
            return b

    def __repr__(self):
        """表示するときの文字列を定義します。"""
        return 'v#'+`self.v`

    __str__ = __repr__