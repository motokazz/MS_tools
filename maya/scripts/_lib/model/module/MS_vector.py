#  coding: utf-8
import maya.cmds as cmds
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