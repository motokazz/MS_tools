#-*- coding:UTF-8 -*-

#*******************************************************************************
'''

Tool Name     : MYAM_PyLib_geometry
Description   : 計算幾何学モジュール

Copyright     : (c)2012 Michiyoshi Yamabe
Author Name   : Michiyoshi Yamabe
Contact       : Yamabe.Michiyoshi@me.com

------------------------------------
----- Using external libraries -----
------------------------------------
[lisenceType] libraryName version

-------------------------
----- UPDATE RECORD -----
-------------------------
  2009/10/05
    追加 -> MYAMBezier3D( CPs )

  2009/12/20
    新規　->　MYAMVectorCollection()
              MYAMVector3Dをまとめるクラスを作成

    新規　->　MYAMMatrixCollection()
              MYAMMatrix3Dをまとめるクラスを作成

    更新　->　MYAMVector3D()
              配列で作成と、個別要素へのアクセスに対応。
              必要な関数を絞り込んで、シェイプアップ。

    更新　->　MYAMMatrix3D()
              配列で作成と、個別要素へのアクセスに対応
              必要な関数を絞り込んで、シェイプアップ

    更新　->　MYAMPolarCircular()
              配列で作成と、個別要素へのアクセスに対応
              必要な関数を絞り込んで、シェイプアップ

    更新　->　MYAMPolarCylindrical()
              配列で作成と、個別要素へのアクセスに対応
              必要な関数を絞り込んで、シェイプアップ

    更新　->　MYAMPolarSpherical()
              配列で作成と、個別要素へのアクセスに対応
              必要な関数を絞り込んで、シェイプアップ

    更新　->　MYAMFnTriangle()
              改名　FnTriangle　->　MYAMFnTriangle

    更新　->　MYAMFnQuadrangle()
              改名　FnQuadrangle　->　MYAMFnQuadrangle

    更新　->　MYAMFnPolygon()
              改名　FnPolygon　->　MYAMFnPolygon

'''
#*******************************************************************************



######################
## Import official modules
######################

import math
import copy
import random

######################
## Import custom modules
######################

######################
## Reload custom modules
######################

#################################################
##### コレクションクラス - Collection Class #####
#################################################

class MYAMVectorCollection( object ):
  def __init__( self , collection=[] ):
    self.collection = []

    for item in collection:
      if isinstance( item , MYAMVector3D ):
        self.collection.append( item )
      else:
        print "[SKIPPED] :" , item , "is not instance of [MYAMVector3D]..."

  def add( self , addItems=[] ):
    for item in addItems:
      if isinstance( item , MYAMVector3D ):
        self.collection.append( item )
      else:
        print "[SKIPPED] :" , item , "is not instance of [MYAMVector3D]..."

  def delete( self , deleteItems=[] ):
    for item in deleteItems:
      if item in self.collection:
        self.collection.remove( item )
      else:
        print "[SKIPPED] :" , item , "was not found in this collection..."



class MYAMMatrixCollection( object ):
  def __init__( self , collection=[] ):
    self.collection = []

    for item in collection:
      if isinstance( item , MYAMMatrix3D ):
        self.collection.append( item )
      else:
        print "[SKIPPED] :" , item , "is not instance of [MYAMMatrix3D]..."

  def add( self , addItems=[] ):
    for item in addItems:
      if isinstance( item , MYAMMatrix3D ):
        self.collection.append( item )
      else:
        print "[SKIPPED] :" , item , "is not instance of [MYAMMatrix3D]..."

  def delete( self , deleteItems=[] ):
    for item in deleteItems:
      if item in self.collection:
        self.collection.remove( item )
      else:
        print "[SKIPPED] :" , item , "was not found in this collection..."










#########################################
##### ベクトルクラス - Vector Class #####
#########################################

class MYAMVector3D( object ):
  """
  Custom vector class.

  Construction pattern...
    1 : var = MYAMVector3D( x(float) , y(float) , z(float) )
    2 : var = MYAMVector3D( [ x(float) , y(float) , z(float) ] )
  """

  ##### Accesser #####
  def getX( self ):
    return self.array[0]

  def setX( self , value ):
    self.array[0] = value

  def getY( self ):
    return self.array[1]

  def setY( self , value ):
    self.array[1] = value

  def getZ( self ):
    return self.array[2]

  def setZ( self , value ):
    self.array[2] = value

  x = property( getX , setX )
  y = property( getY , setY )
  z = property( getZ , setZ )



  ##### Builtin Functions #####
  def __init__( self , x=None , y=None , z=None ):
    if isinstance( x , list ) or isinstance( x , tuple ):
      self.array = x
    else:
      if ( x == y == z == None ):
        self.array = [ 0 , 0 , 0 ]
      else:
        self.array = [ x , y , z ]

  def __call__( self ):
    return copy.copy( self )

  def __pos__( self ):
    return copy.copy( self )

  def __neg__( self ):
    return MYAMVector3D( -self.array[0] ,
                         -self.array[1] ,
                         -self.array[2] )

  def __add__( self , other ):
    return MYAMVector3D( self.x + other.x ,
                         self.y + other.y ,
                         self.z + other.z )
  __iadd__ = __add__
  __radd__ = __add__

  def __sub__( self , other ):
    return MYAMVector3D( self.x - other.x ,
                         self.y - other.y ,
                         self.z - other.z )

  def __rsub__( self , other ):
    return MYAMVector3D( other.x - self.x ,
                         other.y - self.y ,
                         other.z - self.z )
  __isub__ = __sub__

  def __mul__( self , scalar ):
    return MYAMVector3D( self.x * scalar ,
                         self.y * scalar ,
                         self.z * scalar )
  __rmul__ = __mul__
  __imul__ = __mul__

  def __div__( self , scalar ):
    buf = MYAMVector3D()

    if scalar != 0:
      if self.x == 0:
        buf.x = 0
      else:
        buf.x = self.x / scalar

      if self.y == 0:
        buf.y = 0
      else:
        buf.y = self.y / scalar

      if self.z == 0:
        buf.z = 0
      else:
        buf.z = self.z / scalar

    return buf

  def __rdiv__( self , scalar ):
    buf = MYAMVector3D()

    if scalar != 0:
      if self.x != 0:
        buf.x = scalar / self.x
      else:
        buf.x = 0

      if self.y != 0:
        buf.y = scalar / self.y
      else:
        buf.y = 0

      if self.z != 0:
        buf.z = scalar / self.z
      else:
        buf.z = 0

    return buf

  __idiv__ = __div__

  def __cmp__( self , other ):
    if self.x != other.x:
      return 0
    elif self.y != other.y:
      return 0
    elif self.z != other.z:
      return 0
    else:
      return 1



  ##### Member Methods #####
  def length( self ):
    """
    DESCRIPTION : Return self length.
           NAME : length()
         RETURN : No Variable:float
    """
    return math.sqrt( self.x * self.x + self.y * self.y + self.z * self.z )

  def normal( self ):
    """
    DESCRIPTION : Return Normalized self.
           NAME : normal()
         RETURN : No Variable:MYAMVector3D
    """
    length = self.length()
    if 0 == length:
      raise ZeroDivisionError , "Can't normalize Zero length vector."
    else:
      return MYAMVector3D( self.x / length ,
                           self.y / length ,
                           self.z / length )

  def dot( self , other ):
    """
    DESCRIPTION : Return dotProduct value.
           NAME : dot( self:MYAMVector3D , other:MYAMVector3D )
         RETURN : No Variable:float
    """
    return ( self.x * other.x +
             self.y * other.y +
             self.z * other.z )

  def cross( self , other ):
    """
    DESCRIPTION : Return cross product vector.
           NAME : cross( self:MYAMVector3D , other:MYAMVector3D )
         RETURN : No Variable:MYAMVector3D
    """
    return MYAMVector3D( self.y * other.z - self.z * other.y ,
                         self.z * other.x - self.x * other.z ,
                         self.x * other.y - self.y * other.x )

  def angle( self , other ):
    """
    DESCRIPTION : Return angle betweewn two vector.
           NAME : vectorAngle( vector1:MYAMVector3D , vector2:MYAMVector3D )
         RETURN : No Variable:float(radian)
    """
    selfLength      = self.length()
    otherLength     = other.length()
    dotProductValue = self.dot( other )

    if dotProductValue == 0.0:
      return 1.57079632679
    else:
      return math.acos( dotProductValue / ( selfLength * otherLength ) )










#####################################
##### 行列クラス - Matrix Class #####
#####################################

class MYAMMatrix3D( object ):
  """
  Custom matrix class.
  """

  ##### Accesser #####
  def get_11( self ):
    return self.array[0]

  def set_11( self , value ):
    self.array[0] = value

  def get_12( self ):
    return self.array[1]

  def set_12( self , value ):
    self.array[1] = value

  def get_13( self ):
    return self.array[2]

  def set_13( self , value ):
    self.array[2] = value

  def get_14( self ):
    return self.array[3]

  def set_14( self , value ):
    self.array[3] = value


  def get_21( self ):
    return self.array[4]

  def set_21( self , value ):
    self.array[4] = value

  def get_22( self ):
    return self.array[5]

  def set_22( self , value ):
    self.array[5] = value

  def get_23( self ):
    return self.array[6]

  def set_23( self , value ):
    self.array[6] = value

  def get_24( self ):
    return self.array[7]

  def set_24( self , value ):
    self.array[7] = value


  def get_31( self ):
    return self.array[8]

  def set_31( self , value ):
    self.array[8] = value

  def get_32( self ):
    return self.array[9]

  def set_32( self , value ):
    self.array[9] = value

  def get_33( self ):
    return self.array[10]

  def set_33( self , value ):
    self.array[10] = value

  def get_34( self ):
    return self.array[11]

  def set_34( self , value ):
    self.array[11] = value


  def get_41( self ):
    return self.array[12]

  def set_41( self , value ):
    self.array[12] = value

  def get_42( self ):
    return self.array[13]

  def set_42( self , value ):
    self.array[13] = value

  def get_43( self ):
    return self.array[14]

  def set_43( self , value ):
    self.array[14] = value

  def get_44( self ):
    return self.array[15]

  def set_44( self , value ):
    self.array[15] = value

  _11 = property( get_11 , set_11 )
  _12 = property( get_12 , set_12 )
  _13 = property( get_13 , set_13 )
  _14 = property( get_14 , set_14 )

  _21 = property( get_21 , set_21 )
  _22 = property( get_22 , set_22 )
  _23 = property( get_23 , set_23 )
  _24 = property( get_24 , set_24 )

  _31 = property( get_31 , set_31 )
  _32 = property( get_32 , set_32 )
  _33 = property( get_33 , set_33 )
  _34 = property( get_34 , set_34 )

  _41 = property( get_41 , set_41 )
  _42 = property( get_42 , set_42 )
  _43 = property( get_43 , set_43 )
  _44 = property( get_44 , set_44 )



  ##### Builtin Functions #####
  def __init__( self , _11=None , _12=None , _13=None , _14=None ,
                       _21=None , _22=None , _23=None , _24=None ,
                       _31=None , _32=None , _33=None , _34=None ,
                       _41=None , _42=None , _43=None , _44=None ):

    if isinstance( _11 , list ):
      self.array = _11
    else:
      if ( _11 == _12 == _13 == _14 == _21 == _22 == _23 == _24 == _31 == _32 == _33 == _34 == _41 == _42 == _43 == _44 == None ):
        self.array = [ 1,0,0,0 , 0,1,0,0 , 0,0,1,0 , 0,0,0,1 ]
      else:
        self.array = [ _11 , _12 , _13 , _14 ,
                       _21 , _22 , _23 , _24 ,
                       _31 , _32 , _33 , _34 ,
                       _41 , _42 , _43 , _44 ]

  def __call__( self ):
    return copy.copy( self )

  def __pos__( self ):
    return copy.copy( self )

  def __neg__( self ):
    return MYAMMatrix3D( [ -self._11 ,
                           -self._12 ,
                           -self._13 ,
                           -self._14 ,

                           -self._21 ,
                           -self._22 ,
                           -self._23 ,
                           -self._24 ,

                           -self._31 ,
                           -self._32 ,
                           -self._33 ,
                           -self._34 ,

                           -self._41 ,
                           -self._42 ,
                           -self._43 ,
                           -self._44 ] )

  def __add__( self , other ):
    return MYAMMatrix3D( [ self._11 + other._11 ,
                           self._12 + other._12 ,
                           self._13 + other._13 ,
                           self._14 + other._14 ,

                           self._21 + other._21 ,
                           self._22 + other._22 ,
                           self._23 + other._23 ,
                           self._24 + other._24 ,

                           self._31 + other._31 ,
                           self._32 + other._32 ,
                           self._33 + other._33 ,
                           self._34 + other._34 ,

                           self._41 + other._41 ,
                           self._42 + other._42 ,
                           self._43 + other._43 ,
                           self._44 + other._44 ] )
  __iadd__ = __add__
  __radd__ = __add__

  def __sub__( self , other ):
    return MYAMMatrix3D( [ self._11 - other._11 ,
                           self._12 - other._12 ,
                           self._13 - other._13 ,
                           self._14 - other._14 ,

                           self._21 - other._21 ,
                           self._22 - other._22 ,
                           self._23 - other._23 ,
                           self._24 - other._24 ,

                           self._31 - other._31 ,
                           self._32 - other._32 ,
                           self._33 - other._33 ,
                           self._34 - other._34 ,

                           self._41 - other._41 ,
                           self._42 - other._42 ,
                           self._43 - other._43 ,
                           self._44 - other._44 ] )

  def __rsub__( self , other ):
    return MYAMMatrix3D( [ other._11 - self._11 ,
                           other._12 - self._12 ,
                           other._13 - self._13 ,
                           other._14 - self._14 ,

                           other._21 - self._21 ,
                           other._22 - self._22 ,
                           other._23 - self._23 ,
                           other._24 - self._24 ,

                           other._31 - self._31 ,
                           other._32 - self._32 ,
                           other._33 - self._33 ,
                           other._34 - self._34 ,

                           other._41 - self._41 ,
                           other._42 - self._42 ,
                           other._43 - self._43 ,
                           other._44 - self._44 ] )
  __isub__ = __sub__

  def __mul__( self , scalar ):
    return MYAMMatrix3D( [ self._11 * scalar ,
                           self._12 * scalar ,
                           self._13 * scalar ,
                           self._14 * scalar ,

                           self._21 * scalar ,
                           self._22 * scalar ,
                           self._23 * scalar ,
                           self._24 * scalar ,

                           self._31 * scalar ,
                           self._32 * scalar ,
                           self._33 * scalar ,
                           self._34 * scalar ,

                           self._41 * scalar ,
                           self._42 * scalar ,
                           self._43 * scalar ,
                           self._44 * scalar ] )
  __rmul__ = __mul__
  __imul__ = __mul__

  def __div__( self , scalar ):
    localArray = []

    if scalar != 0:
      for elem in self.array:
        if elem != 0:
          localArray.append( elem / scalar )
        else:
          localArray.append( 0.0 )

      return MYAMMatrix3D( localArray )

    else:
      return MYAMMatrix3D( [ 0,0,0,0 , 0,0,0,0 , 0,0,0,0 , 0,0,0,0 ] )

  def __rdiv__( self , scalar ):
    localArray = []

    if scalar != 0:
      for elem in self.array:
        if elem != 0:
          localArray.append( scalar / elem )
        else:
          localArray.append( 0.0 )

      return MYAMMatrix3D( localArray )

    else:
      return MYAMMatrix3D( [ 0,0,0,0 , 0,0,0,0 , 0,0,0,0 , 0,0,0,0 ] )

  __idiv__ = __div__



  ##### Member Methods #####
  def product( self , other ):
    """
    DESCRIPTION : Return product calculated matrix.
           NAME : product( self:MYAMMatrix3D , other:MYAMMatrix3D )
         RETURN : matrixProduct:MYAMMatrix3D
    """
    _11 = ( self._11 * other._11 ) + ( self._12 * other._21 ) + ( self._13 * other._31 ) + ( self._14 * other._41 )
    _12 = ( self._11 * other._12 ) + ( self._12 * other._22 ) + ( self._13 * other._32 ) + ( self._14 * other._42 )
    _13 = ( self._11 * other._13 ) + ( self._12 * other._23 ) + ( self._13 * other._33 ) + ( self._14 * other._43 )
    _14 = ( self._11 * other._14 ) + ( self._12 * other._24 ) + ( self._13 * other._34 ) + ( self._14 * other._44 )

    _21 = ( self._21 * other._11 ) + ( self._22 * other._21 ) + ( self._23 * other._31 ) + ( self._24 * other._41 )
    _22 = ( self._21 * other._12 ) + ( self._22 * other._22 ) + ( self._23 * other._32 ) + ( self._24 * other._42 )
    _23 = ( self._21 * other._13 ) + ( self._22 * other._23 ) + ( self._23 * other._33 ) + ( self._24 * other._43 )
    _24 = ( self._21 * other._14 ) + ( self._22 * other._24 ) + ( self._23 * other._34 ) + ( self._24 * other._44 )

    _31 = ( self._31 * other._11 ) + ( self._32 * other._21 ) + ( self._33 * other._31 ) + ( self._34 * other._41 )
    _32 = ( self._31 * other._12 ) + ( self._32 * other._22 ) + ( self._33 * other._32 ) + ( self._34 * other._42 )
    _33 = ( self._31 * other._13 ) + ( self._32 * other._23 ) + ( self._33 * other._33 ) + ( self._34 * other._43 )
    _34 = ( self._31 * other._14 ) + ( self._32 * other._24 ) + ( self._33 * other._34 ) + ( self._34 * other._44 )

    _41 = ( self._41 * other._11 ) + ( self._42 * other._21 ) + ( self._43 * other._31 ) + ( self._44 * other._41 )
    _42 = ( self._41 * other._12 ) + ( self._42 * other._22 ) + ( self._43 * other._32 ) + ( self._44 * other._42 )
    _43 = ( self._41 * other._13 ) + ( self._42 * other._23 ) + ( self._43 * other._33 ) + ( self._44 * other._43 )
    _44 = ( self._41 * other._14 ) + ( self._42 * other._24 ) + ( self._43 * other._34 ) + ( self._44 * other._44 )

    matrixProduct = MYAMMatrix3D( _11 , _12 , _13 , _14 ,
                                  _21 , _22 , _23 , _24 ,
                                  _31 , _32 , _33 , _34 ,
                                  _41 , _42 , _43 , _44 )
    return matrixProduct

  def transpose( self ):
    """
    DESCRIPTION : Transpose self.
           NAME : doTransposeSelf()
         RETURN : None
    """
    return MYAMMatrix3D( [ self._11 ,
                           self._21 ,
                           self._31 ,
                           self._41 ,

                           self._12 ,
                           self._22 ,
                           self._32 ,
                           self._42 ,

                           self._13 ,
                           self._23 ,
                           self._33 ,
                           self._43 ,

                           self._14 ,
                           self._24 ,
                           self._34 ,
                           self._44 ] )

  def inverse( self ):
    """
    DESCRIPTION : Inverse self.
           NAME : doInverseSelf()
         RETURN : None
    """
    pass

  def setTranslate( self , x , y , z ):
    """
    DESCRIPTION : Set translate matrix to self.
           NAME : setTranslate( translateX:float , translateY:float , translateZ:float )
         RETURN : None
    """
    self._11 = 1.0
    self._12 = 0.0
    self._13 = 0.0
    self._14 = 0.0

    self._21 = 0.0
    self._22 = 1.0
    self._23 = 0.0
    self._24 = 0.0

    self._31 = 0.0
    self._32 = 0.0
    self._33 = 1.0
    self._34 = 0.0

    self._41 = x
    self._42 = y
    self._43 = z
    self._44 = 1.0

  def getTranslate( self ):
    return [ self._41 , self._42 , self._43 ]

  def setRotateX( self , angle ):
    """
    DESCRIPTION : Set rotateX matrix to self.
           NAME : setRotateX( rotateX:float )
         RETURN : None
    """
    self._11 = 1.0
    self._12 = 0.0
    self._13 = 0.0
    self._14 = 0.0

    self._21 = 0.0
    self._22 = math.cos( angle )
    self._23 = -math.sin( angle )
    self._24 = 0.0

    self._31 = 0.0
    self._32 = math.sin( angle )
    self._33 = math.cos( angle )
    self._34 = 0.0

    self._41 = 0.0
    self._42 = 0.0
    self._43 = 0.0
    self._44 = 1.0

  def getRotateX( self ):
    return math.acos( self._22 )

  def setRotateY( self , angle ):
    """
    DESCRIPTION : Set rotateY matrix to self.
           NAME : setRotateY( rotateY:float )
         RETURN : None
    """
    self._11 = math.cos( angle )
    self._12 = 0.0
    self._13 = -math.sin( angle )
    self._14 = 0.0

    self._21 = 0.0
    self._22 = 1.0
    self._23 = 0.0
    self._24 = 0.0

    self._31 = math.sin( angle )
    self._32 = 0.0
    self._33 = math.cos( angle )
    self._34 = 0.0

    self._41 = 0.0
    self._42 = 0.0
    self._43 = 0.0
    self._44 = 1.0

  def getRotateY( self ):
    return math.acos( self._11 )

  def setRotateZ( self , angle ):
    """
    DESCRIPTION : Set rotateZ matrix to self.
           NAME : setRotateZ( rotateZ:float )
         RETURN : None
    """
    self._11 = math.cos( angle )
    self._12 = -math.sin( angle )
    self._13 = 0.0
    self._14 = 0.0

    self._21 = math.sin( angle )
    self._22 = math.cos( angle )
    self._23 = 0.0
    self._24 = 0.0

    self._31 = 0.0
    self._32 = 0.0
    self._33 = 1.0
    self._34 = 0.0

    self._41 = 0.0
    self._42 = 0.0
    self._43 = 0.0
    self._44 = 1.0

  def getRotateZ( self ):
    return math.acos( self._11 )

  def setScale( self , x , y , z ):
    """
    DESCRIPTION : Set scale matrix to self.
           NAME : setScale( scaleX:float , scaleY:float , scaleZ:float )
         RETURN : None
    """
    self._11 = x
    self._12 = 0.0
    self._13 = 0.0
    self._14 = 0.0

    self._21 = 0.0
    self._22 = y
    self._23 = 0.0
    self._24 = 0.0

    self._31 = 0.0
    self._32 = 0.0
    self._33 = z
    self._34 = 0.0

    self._41 = 0.0
    self._42 = 0.0
    self._43 = 0.0
    self._44 = 1.0

  def getScale( self ):
    return [ self._11 , self._22 , self._33 ]

  def setRotateAtAnyAxis( self , axis , angle ):
    self._11 = axis.x * axis.x * ( 1 - math.cos( angle ) ) + math.cos( angle )
    self._12 = axis.x * axis.y * ( 1 - math.cos( angle ) ) + axis.z * math.sin( angle )
    self._13 = axis.x * axis.z * ( 1 - math.cos( angle ) ) - axis.y * math.sin( angle )
    self._14 = 0.0

    self._21 = axis.x * axis.y * ( 1 - math.cos( angle ) ) - axis.z * math.sin( angle )
    self._22 = axis.y * axis.y * ( 1 - math.cos( angle ) ) + math.cos( angle )
    self._23 = axis.y * axis.z * ( 1 - math.cos( angle ) ) + axis.x * math.sin( angle )
    self._24 = 0.0

    self._31 = axis.x * axis.z * ( 1 - math.cos( angle ) ) + axis.y * math.sin( angle )
    self._32 = axis.y * axis.z * ( 1 - math.cos( angle ) ) - axis.x * math.sin( angle )
    self._33 = axis.z * axis.z * ( 1 - math.cos( angle ) ) + math.cos( angle )
    self._34 = 0.0

    self._41 = 0.0
    self._42 = 0.0
    self._43 = 0.0
    self._44 = 1.0










###############################################
##### 円座標クラス - Polar Circular Class #####
###############################################

class MYAMPolarCircular( object ):
  """
  Custom polar circular class.
  """

  ##### Accesser #####
  def getRadius( self ):
    return self.array[0]

  def setRadius( self , value ):
    self.array[0] = value

  def getAngle( self ):
    return self.array[1]

  def setAngle( self , value ):
    self.array[1] = value

  radius = property( getRadius , setRadius )
  angle  = property( getAngle  , setAngle )


  ##### Builtin Functions #####
  def __init__( self , radius=None , angle=None ):
    if isinstance( radius , list ):
      self.array = radius
    else:
      if ( radius == angle == None ):
        self.array = [ 0 , 0 ]
      else:
        self.array = [ radius , angle ]

  def __call__( self ):
    return copy.copy( self )

  def __pos__( self ):
    return copy.copy( self )

  def __neg__( self ):
    return MYAMPolarCircular( [ -self.radius , self.angle ] )

  def __add__( self , other ):
    return MYAMPolarCircular( self.radius + other.radius , self.angle + other.angle )

  __iadd__ = __add__
  __radd__ = __add__

  def __sub__( self , other ):
    return MYAMPolarCircular( [ self.radius - other.radius , self.angle - other.angle ] )

  def __rsub__( self , other ):
    return MYAMPolarCircular( other.radius - self.radius , other.angle - self.angle )

  __isub__ = __sub__

  def __mul__( self , scalar ):
    return MYAMPolarCircular( self.radius * scalar , self.angle )

  __rmul__ = __mul__
  __imul__ = __mul__

  def __div__( self , scalar ):
    return MYAMPolarCircular( self.radius / scalar , self.angle )

  def __rdiv__( self , scalar ):
    return MYAMPolarCircular( scalar / self.radius , self.angle )

  __idiv__ = __div__


  ##### Member Methods #####
  def fromCartesian( self , array ):
    """
    DESCRIPTION : Convert cartesian value array to self member variables.
           NAME : convertFromArray( [ axis1:float , axis2:float ] )
         RETURN : None
    """
    self.radius = math.sqrt( array[0] * array[0] + array[1] * array[1] )
    self.angle  = math.atan2( array[1] , array[0] )

  def toCartesian( self ):
    """
    DESCRIPTION : Convert self member variables to cartesian value array.
           NAME : convertToArray()
         RETURN : [ axis1:float , axis2:float ]
    """
    axis1 = self.radius * math.cos( self.angle )
    axis2 = self.radius * math.sin( self.angle )
    return [ axis1 , axis2 ]



########### MYAMPolarCircular class Test code #####
##
##PC1 = MYAMPolarCircular( [ 1 , math.radians( 45 ) ] )
##PC2 = MYAMPolarCircular( 2 , math.radians( 45 ) )
##
##print "PC1.array  =" , PC1.array
##print "PC1.radius =" , PC1.radius
##print "PC1.angle  =" , PC1.angle
##print ""
##
##print "PC2.array  =" , PC2.array
##print "PC2.radius =" , PC2.radius
##print "PC2.angle  =" , PC2.angle
##print ""
##
##print "(+PC1).array =" , (+PC1).array
##print "(-PC1).array =" , (-PC1).array
##print ""
##
##print "( PC1 + PC2 ).array =" , ( PC1 + PC2 ).array
##print "( PC1 - PC2 ).array =" , ( PC1 - PC2 ).array
##print "( PC2 - PC1 ).array =" , ( PC2 - PC1 ).array
##
##print "( PC1 * 2 ).array =" , ( PC1 * 10 ).array
##print "( PC1 / 2.0 ).array =" , ( PC1 / 2.0 ).array
##print "( 2.0 / PC1 ).array =" , ( 2.0 / PC1 ).array
##print ""
##
##print PC1.toCartesian()
##
##PC3 = MYAMPolarCircular()
##PC3.fromCartesian( [ 0.70710678118654757, 0.70710678118654746 ] )
##print "PC3.fromCartesian( [ 0.70710678118654757, 0.70710678118654746 ] ) =" , PC3.array

########### MYAMPolarCircular class Test code Results #####
##
##PC1.array  = [1, 0.78539816339744828]
##PC1.radius = 1
##PC1.angle  = 0.785398163397
##
##PC2.array  = [2, 0.78539816339744828]
##PC2.radius = 2
##PC2.angle  = 0.785398163397
##
##(+PC1).array = [1, 0.78539816339744828]
##(-PC1).array = [-1, 0.78539816339744828]
##
##( PC1 + PC2 ).array = [3, 1.5707963267948966]
##( PC1 - PC2 ).array = [-1, 0.0]
##( PC2 - PC1 ).array = [1, 0.0]
##( PC1 * 2 ).array = [10, 0.78539816339744828]
##( PC1 / 2.0 ).array = [0.5, 0.78539816339744828]
##( 2.0 / PC1 ).array = [2.0, 0.78539816339744828]
##
##[0.70710678118654757, 0.70710678118654746]
##PC3.fromCartesian( [ 0.70710678118654757, 0.70710678118654746 ] ) = [1.0, 0.78539816339744828]










####################################################
##### 円筒座標クラス - Polar Cylindrical Class #####
####################################################

class MYAMPolarCylindrical():
  """
  Custom polar cylindrical class.
  """

  ##### Accesser #####
  def getRadius( self ):
    return self.array[0]

  def setRadius( self , value ):
    self.array[0] = value

  def getAngle( self ):
    return self.array[1]

  def setAngle( self , value ):
    self.array[1] = value

  def getDepth( self ):
    return self.array[2]

  def setDepth( self , value ):
    self.array[2] = value

  radius = property( getRadius , setRadius )
  angle  = property( getAngle  , setAngle )
  depth  = property( getDepth  , setDepth )



  ##### Builtin Functions #####
  def __init__( self , radius=None , angle=None , depth=None ):
    if isinstance( radius , list ):
      self.array = radius
    else:
      if ( radius == angle == depth == None ):
        self.array = [ 0 , 0 , 0 ]
      else:
        self.array = [ radius , angle , depth ]

  def __call__( self ):
    return copy.copy( self )

  def __pos__( self ):
    return copy.copy( self )

  def __neg__( self ):
    return MYAMPolarCylindrical( -self.radius , self.angle , -self.depth )

  def __add__( self , other ):
    return MYAMPolarCylindrical( self.radius + other.radius , self.angle + other.angle , self.depth + other.depth )

  __iadd__ = __add__
  __radd__ = __add__

  def __sub__( self , other ):
    return MYAMPolarCylindrical( self.radius - other.radius , self.angle - other.angle , self.depth - other.depth )

  def __rsub__( self , other ):
    return MYAMPolarCylindrical( other.radius - self.radius , other.angle - self.angle , other.depth - self.depth )

  __isub__ = __sub__

  def __mul__( self , scalar ):
    return MYAMPolarCylindrical( self.radius * scalar , self.angle , self.depth * scalar )

  __rmul__ = __mul__
  __imul__ = __mul__

  def __div__( self , scalar ):
    return MYAMPolarCylindrical( self.radius / scalar , self.angle , self.depth / scalar )

  def __rdiv__( self , scalar ):
    return MYAMPolarCylindrical( scalar / self.radius , self.angle , scalar / self.depth )

  __idiv__ = __div__


  ##### Member Methods #####
  def fromCartesian( self , array ):
    """
    DESCRIPTION : Convert cartesian value array to self member variables.
           NAME : convertFromCartesian( [ x:float , y:float , z:float ] )
         RETURN : None
    """
    self.radius = math.sqrt( array[0] * array[0] + array[1] * array[1] )
    self.angle  = math.atan2( array[1] , array[0] )
    self.depth  = array[2]

  def toCartesian( self ):
    """
    DESCRIPTION : Convert self member variables to cartesian value array.
           NAME : convertToCartesian()
         RETURN : [ x:float , y:float , z:float ]
    """
    axis1 = self.radius * math.cos( self.angle )
    axis2 = self.radius * math.sin( self.angle )
    axis3 = self.depth
    return [ axis1 , axis2 , axis3 ]




########### MYAMPolarCylindrical class Test code #####
##
##PC1 = MYAMPolarCylindrical( [ 1 , math.radians( 45 ) , 10 ] )
##PC2 = MYAMPolarCylindrical(   1 , math.radians( 45 ) , 10   )
##
##print "PC1.array  =" , PC1.array
##print "PC1.radius =" , PC1.radius
##print "PC1.angle  =" , PC1.angle
##print "PC1.depth  =" , PC1.depth
##print ""
##
##print "PC2.array  =" , PC2.array
##print "PC2.radius =" , PC2.radius
##print "PC1.angle  =" , PC1.angle
##print "PC2.depth  =" , PC2.depth
##print ""
##
##print "(+PC1).array =" , (+PC1).array
##print "(-PC1).array =" , (-PC1).array
##print ""
##
##print "( PC1 + PC2 ).array =" , ( PC1 + PC2 ).array
##print "( PC1 - PC2 ).array =" , ( PC1 - PC2 ).array
##print "( PC2 - PC1 ).array =" , ( PC2 - PC1 ).array
##
##print "( PC1 * 2 ).array   =" , ( PC1 * 10 ).array
##print "( PC1 / 2.0 ).array =" , ( PC1 / 2.0 ).array
##print "( 2.0 / PC1 ).array =" , ( 2.0 / PC1 ).array
##print ""
##
##print PC1.toCartesian()
##
##PC3 = MYAMPolarCircular()
##PC3.fromCartesian( [ 0.70710678118654757, 0.70710678118654746 ] )
##print "PC3.fromCartesian( [ 0.70710678118654757, 0.70710678118654746 ] ) =" , PC3.array

############# MYAMPolarCylindrical class Test code Results #####
##
##PC1.array  = [1, 0.78539816339744828, 10]
##PC1.radius = 1
##PC1.angle  = 0.785398163397
##PC1.depth  = 10
##
##PC2.array  = [1, 0.78539816339744828, 10]
##PC2.radius = 1
##PC1.angle  = 0.785398163397
##PC2.depth  = 10
##
##(+PC1).array = [1, 0.78539816339744828, 10]
##(-PC1).array = [-1, 0.78539816339744828, -10]
##
##( PC1 + PC2 ).array = [2, 1.5707963267948966, 20]
##( PC1 - PC2 ).array = [0, 0.0, 0]
##( PC2 - PC1 ).array = [0, 0.0, 0]
##( PC1 * 2 ).array   = [10, 0.78539816339744828, 100]
##( PC1 / 2.0 ).array = [0.5, 0.78539816339744828, 5.0]
##( 2.0 / PC1 ).array = [2.0, 0.78539816339744828, 0.20000000000000001]
##
##[0.70710678118654757, 0.70710678118654746, 10]
##PC3.fromCartesian( [ 0.70710678118654757, 0.70710678118654746 ] ) = [1.0, 0.78539816339744828]










####################################################
##### 球座標クラス - Polar Spherical Functions #####
####################################################

class MYAMPolarSpherical():
  """
  Custom polar cylindrical class.
  """

  ##### Accesser #####
  def getRadius( self ):
    return self.array[0]

  def setRadius( self , value ):
    self.array[0] = value

  def getAngle1( self ):
    return self.array[1]

  def setAngle1( self , value ):
    self.array[1] = value

  def getAngle2( self ):
    return self.array[1]

  def setAngle2( self , value ):
    self.array[1] = value

  radius = property( getRadius , setRadius )
  angle1 = property( getAngle1 , setAngle1 )
  angle2 = property( getAngle2 , setAngle2 )


  ##### Builtin Functions #####
  def __init__( self , radius=None , angle1=None , angle2=None ):
    if isinstance( radius , list ):
      self.array = radius
    else:
      if ( radius == angle1 == angle2 == None ):
        self.array = [ 0 , 0 , 0 ]
      else:
        self.array = [ radius , angle1 , angle2 ]

  def __call__( self ):
    return copy.copy( self )

  def __pos__( self ):
    return copy.copy( self )

  def __neg__( self ):
    return MYAMPolarSpherical( -self.radius , self.angle1 , self.angle2 )

  def __add__( self , other ):
    return MYAMPolarSpherical( self.radius + other.radius , self.angle1 + other.angle1 , self.angle2 + other.angle2 )

  __iadd__ = __add__
  __radd__ = __add__

  def __sub__( self , other ):
    return MYAMPolarSpherical( self.radius - other.radius , self.angle1 - other.angle1 , self.angle2 - other.angle2 )

  def __rsub__( self , other ):
    return MYAMPolarSpherical( other.radius - self.radius , other.angle1 - self.angle1 , self.radius , other.angle2 - self.angle2 )

  __isub__ = __sub__

  def __mul__( self , scalar ):
    return MYAMPolarSpherical( self.radius * scalar , self.angle1 , self.angle2 )

  __rmul__ = __mul__
  __imul__ = __mul__

  def __div__( self , scalar ):
    return MYAMPolarSpherical( self.radius / scalar , self.angle1 , self.angle2 )

  def __rdiv__( self , scalar ):
    return MYAMPolarSpherical( scalar / self.radius , self.angle1 , self.angle2 )

  __idiv__ = __div__


  ##### Member Methods #####
  def fromCartesian( self , array ):
    """
    DESCRIPTION : Convert cartesian value array to self member variables.
           NAME : convertFromArray( [ x:float , y:float , z:float ] )
         RETURN : None
    """
    self.radius = math.sqrt( array[0] * array[0] + array[1] * array[1] + array[2] * array[2] )
    self.angle1 = math.acos( array[2] / self.radius )
    self.angle2 = math.acos( array[0] / math.sqrt( array[0] * array[0] + array[1] * array[1] ) )

  def toCartesian( self ):
    """
    DESCRIPTION : Convert self member variables to cartesian value array.
           NAME : convertToArray()
         RETURN : [ x:float , y:float , z:float ]
    """
    axis1 = self.radius * math.sin( self.angle1 ) * math.cos( self.angle2 )
    axis2 = self.radius * math.sin( self.angle1 ) * math.sin( self.angle2 )
    axis3 = self.radius * math.cos( self.angle1 )
    return [ axis1 , axis2 , axis3 ]




########### MYAMPolarSpherical class Test code #####
##
##PC1 = MYAMPolarSpherical( [ 1 , math.radians( 45 ) , math.radians( 45 ) ] )
##PC2 = MYAMPolarSpherical(   1 , math.radians( 45 ) , math.radians( 45 )   )
##
##print "PC1.array  =" , PC1.array
##print "PC1.radius =" , PC1.radius
##print "PC1.angle1 =" , PC1.angle1
##print "PC1.angle2 =" , PC1.angle2
##print ""
##
##print "PC2.array  =" , PC2.array
##print "PC2.radius =" , PC2.radius
##print "PC2.angle1 =" , PC2.angle1
##print "PC2.angle2 =" , PC2.angle2
##print ""
##
##print "(+PC1).array =" , (+PC1).array
##print "(-PC1).array =" , (-PC1).array
##print ""
##
##print "( PC1 + PC2 ).array =" , ( PC1 + PC2 ).array
##print "( PC1 - PC2 ).array =" , ( PC1 - PC2 ).array
##print "( PC2 - PC1 ).array =" , ( PC2 - PC1 ).array
##
##print "( PC1 * 2 ).array   =" , ( PC1 * 10 ).array
##print "( PC1 / 2.0 ).array =" , ( PC1 / 2.0 ).array
##print "( 2.0 / PC1 ).array =" , ( 2.0 / PC1 ).array
##print ""
##
##print PC1.toCartesian()
##
##PC3 = MYAMPolarCircular()
##PC3.fromCartesian( [ 0.70710678118654757, 0.70710678118654746 ] )
##print "PC3.fromCartesian( [ 0.70710678118654757, 0.70710678118654746 ] ) =" , PC3.array


########### MYAMPolarSpherical class Test code Results #####
##
##PC1.array  = [1, 0.78539816339744828, 0.78539816339744828]
##PC1.radius = 1
##PC1.angle1 = 0.785398163397
##PC1.angle2 = 0.785398163397
##
##PC2.array  = [1, 0.78539816339744828, 0.78539816339744828]
##PC2.radius = 1
##PC2.angle1 = 0.785398163397
##PC2.angle2 = 0.785398163397
##
##(+PC1).array = [1, 0.78539816339744828, 0.78539816339744828]
##(-PC1).array = [-1, 0.78539816339744828, 0.78539816339744828]
##
##( PC1 + PC2 ).array = [2, 1.5707963267948966, 1.5707963267948966]
##( PC1 - PC2 ).array = [0, 0.0, 0.0]
##( PC2 - PC1 ).array = [0, 0.0, 0.0]
##( PC1 * 2 ).array   = [10, 0.78539816339744828, 0.78539816339744828]
##( PC1 / 2.0 ).array = [0.5, 0.78539816339744828, 0.78539816339744828]
##( 2.0 / PC1 ).array = [2.0, 0.78539816339744828, 0.78539816339744828]
##
##[0.5, 0.49999999999999989, 0.70710678118654757]
##PC3.fromCartesian( [ 0.70710678118654757, 0.70710678118654746 ] ) = [1.0, 0.78539816339744828]






























###########################################
##### 三角形関数 - Triangle functions #####
###########################################

class MYAMFnTriangle():

  def getCenterOfMassSpacePosition( self , vertexList=[] , weightList=[1,0,0] ):
    """
    DESCRIPTION : Return world space coordinates position, converted from center of mass space coordinates.
           NAME : getCenterOfMassSpace( vertexVector1:MYAMVector3D , vertexVector2:MYAMVector3D , vertexVector3:MYAMVector3D ,
                                        weight1:float , weight2:float , weight3:float )
         RETURN : MYAMVector3D
    """
    ## 頂点にウエイトを掛け合わせる
    ## ウエイトの合計値は1にしなければならない
    ## 合計が1でない場合は、三角形平面上の位置が取れない
    d1 = vertexList[0] * weightList[0]
    d2 = vertexList[1] * weightList[1]
    d3 = vertexList[2] * weightList[2]

    worldPosition = d1 + d2 + d3

    return worldPosition


  def absoluteArea( self , vertexVector1 , vertexVector2 , vertexVector3 ):
    """
    DESCRIPTION : Return absolute triangle area.
           NAME : getAbsoluteArea3D( vertexVector1:MYAMVector3D , vertexVector2:MYAMVector3D , vertexVector3:MYAMVector3D )
         RETURN : area:float
    """
    e1 = vertexVector2 - vertexVector1
    e2 = vertexVector3 - vertexVector1
    normal = crossProduct( e1 , e2 )
    area   = vectorLength( normal ) * 0.5
    return area


  def relativeVolume( self , vertexVector1 , vertexVector2 , vertexVector3 ):
    """
    DESCRIPTION : Return triangle volume.
           NAME : getRelativeVolume3D( vertexVector1:MYAMVector3D , vertexVector2:MYAMVector3D , vertexVector3:MYAMVector3D )
         RETURN : volume:float
    """
    x1 = vertexVector1.x
    y1 = vertexVector1.y
    z1 = vertexVector1.z

    x2 = vertexVector2.x
    y2 = vertexVector2.y
    z2 = vertexVector2.z

    x3 = vertexVector3.x
    y3 = vertexVector3.y
    z3 = vertexVector3.z

    e1 = ( x3 * x3 * y3 * z3 - 2 * x2 * x3 * y3 * z3 +  x2 * x2 * y3 * z3 +  x3 * x3 * y2 * z3 - 2 * x2 * x3 * y2 * z3 +  x2 * x2 * y2 * z3 +  x3 * x3 * y3 * z2 - 2 * x2 * x3 * y3 * z2 +  x2 * x2 * y3 * z2 +  x3 * x3 * y2 * z2 - 2 * x2 * x3 * y2 * z2 +  x2 * x2 * y2 * z2 ) / 4.0
    e2 = ( x3 * x3 * y3 * z3 - 2 * x1 * x3 * y3 * z3 +  x1 * x1 * y3 * z3 +  x3 * x3 * y1 * z3 - 2 * x1 * x3 * y1 * z3 +  x1 * x1 * y1 * z3 +  x3 * x3 * y3 * z1 - 2 * x1 * x3 * y3 * z1 +  x1 * x1 * y3 * z1 +  x3 * x3 * y1 * z1 - 2 * x1 * x3 * y1 * z1 +  x1 * x1 * y1 * z1 ) / 4.0
    e3 = ( x2 * x2 * y2 * z2 - 2 * x1 * x2 * y2 * z2 +  x1 * x1 * y2 * z2 +  x2 * x2 * y1 * z2 - 2 * x1 * x2 * y1 * z2 +  x1 * x1 * y1 * z2 +  x2 * x2 * y2 * z1 - 2 * x1 * x2 * y2 * z1 +  x1 * x1 * y2 * z1 +  x2 * x2 * y1 * z1 - 2 * x1 * x2 * y1 * z1 +  x1 * x1 * y1 * z1 ) / 4.0

    return e1 + e2 + e3


  def edgeLength( self , vertexVector1 , vertexVector2 , vertexVector3 ):
    """
    DESCRIPTION : Return three triangle edge lengths.
           NAME : getAllEdgeLength( vertexVector1:MYAMVector3D , vertexVector2:MYAMVector3D , vertexVector3:MYAMVector3D )
         RETURN : [ edgeLength1( float ) , edgeLength2( float ) , edgeLength3( float ) ]
    """
    e1 = vectorLength( vertexVector3 - vertexVector2 )
    e2 = vectorLength( vertexVector1 - vertexVector3 )
    e3 = vectorLength( vertexVector2 - vertexVector1 )
    edgeLengthList = [ e1 , e2 , e3 ]
    return edgeLengthList



  ## 五心 ##
  def centroid( vertexVector1 , vertexVector2 , vertexVector3 ):
    """
    DESCRIPTION : Return centroid position.
           NAME : getCentroid( vertexVector1:MYAMVector3D , vertexVector2:MYAMVector3D , vertexVector3:MYAMVector3D )
         RETURN : centroidPosition:MYAMVector3D
    """
    centroidPosition = FnTriangle.getCenterOfMassSpacePosition( vertexVector1 , vertexVector2 , vertexVector3 , 1.0 / 3.0 ,  1.0 / 3.0 ,  1.0 / 3.0 )
    return centroidPosition


  def incenter( vertexVector1 , vertexVector2 , vertexVector3 ):
    """
    DESCRIPTION : Return incenter position.
           NAME : getIncenter( vertexVector1:MYAMVector3D , vertexVector2:MYAMVector3D , vertexVector3:MYAMVector3D )
         RETURN : incenterPosition:MYAMVector3D
    """
    edgeLength  = getAllEdgeLength( vertexVector1 , vertexVector2 , vertexVector3 )
    totalLength = sum( edgeLength )

    d1 = edgeLength[0] / totalLength
    d2 = edgeLength[1] / totalLength
    d3 = edgeLength[2] / totalLength

    incenterPosition = getCenterOfMassSpace( vertexVector1 , vertexVector2 , vertexVector3 , [ d1 , d2 , d3 ] )
    return incenterPosition


  def inscribedCircleRadius( vertexVector1 , vertexVector2 , vertexVector3 ):
    """
    DESCRIPTION : Return inscribed circle radius.
           NAME : getInscribedCircleRadius( vertexVector1:MYAMVector3D , vertexVector2:MYAMVector3D , vertexVector3:MYAMVector3D )
         RETURN : inscribedCircleRadius:float
    """
    absoluteArea = getAbsoluteArea3D( vertexVector1 , vertexVector2 , vertexVector3 )
    edgeLength   = getAllEdgeLength( vertexVector1 , vertexVector2 , vertexVector3 )
    totalLength  = sum( edgeLength )
    inscribedCircleRadius = 2 * absoluteArea / totalLength
    return inscribedCircleRadius


  def circumcenter( vertexVector1 , vertexVector2 , vertexVector3 ):
    """
    DESCRIPTION : Return circumcenter position.
           NAME : getCircumcenter( vertexVector1:MYAMVector3D , vertexVector2:MYAMVector3D , vertexVector3:MYAMVector3D )
         RETURN : circumcenterPosition:MYAMVector3D
    """
    e1 = ( vertexVector3 - vertexVector2 )
    e2 = ( vertexVector1 - vertexVector3 )
    e3 = ( vertexVector2 - vertexVector1 )

    dot1 = -( dotProduct( e2 , e3 ) )
    dot2 = -( dotProduct( e3 , e1 ) )
    dot3 = -( dotProduct( e1 , e2 ) )

    c1 = dot2 * dot3
    c2 = dot3 * dot1
    c3 = dot1 * dot2

    c = c1 + c2 + c3

    d1 = ( c2 + c3 ) / ( 2.0 * c )
    d2 = ( c3 + c1 ) / ( 2.0 * c )
    d3 = ( c1 + c2 ) / ( 2.0 * c )

    circumcenterPosition = getCenterOfMassSpace( vertexVector1 , vertexVector2 , vertexVector3 , [ d1 , d2 , d3 ] )
    return circumcenterPosition


  def circumcircleRadius( vertexVector1 , vertexVector2 , vertexVector3 ):
    """
    DESCRIPTION : Return circumcircle radius.
           NAME : getCircumcircleRadius( vertexVector1:MYAMVector3D , vertexVector2:MYAMVector3D , vertexVector3:MYAMVector3D )
         RETURN : circumcircleRadius:float
    """
    e1 = ( vertexVector3 - vertexVector2 )
    e2 = ( vertexVector1 - vertexVector3 )
    e3 = ( vertexVector2 - vertexVector1 )

    dot1 = -( dotProduct( e2 , e3 ) )
    dot2 = -( dotProduct( e3 , e1 ) )
    dot3 = -( dotProduct( e1 , e2 ) )

    c1 = dot2 * dot3
    c2 = dot3 * dot1
    c3 = dot1 * dot2

    c = c1 + c2 + c3

    d1 = ( c2 + c3 ) / ( 2.0 * c )
    d2 = ( c3 + c1 ) / ( 2.0 * c )
    d3 = ( c1 + c2 ) / ( 2.0 * c )

    circumcircleRadius = math.sqrt( ( dot1 + dot2 ) * ( dot2 + dot3 ) * ( dot3 + dot1 ) / c ) / ( 2.0 )
    return circumcircleRadius


  def excenters( self ):
    """
    !!! Incompleteness !!!
    DESCRIPTION : Return excenters position list.
           NAME : getExcenters( vertexVector1:MYAMVector3D , vertexVector2:MYAMVector3D , vertexVector3:MYAMVector3D )
         RETURN : [ MYAMVector3D , MYAMVector3D , MYAMVector3D ]
    """
    pass


  def inscribedCircleRadius( self ):
    """
    !!! Incompleteness !!!
    DESCRIPTION : Return excenters radius list.
           NAME : getEscribedCircleRadius( vertexVector1:MYAMVector3D , vertexVector2:MYAMVector3D , vertexVector3:MYAMVector3D )
         RETURN : [ float , float , float ]
    """
    pass


  def orthocenter( self ):
    """
    !!! Incompleteness !!!
    DESCRIPTION : Return orthocenter position.
           NAME : Orthocenter( vertexVector1:MYAMVector3D , vertexVector2:MYAMVector3D , vertexVector3:MYAMVector3D )
         RETURN : float
    """
    pass









#############################################
##### 四角形関数 - Quadrangle functions #####
#############################################

class MYAMFnQuadrangle():

  def getCenterOfMassSpacePosition( self , vertexList=[] , weightList=[1,0,0,0] ):
    """
    DESCRIPTION : Return world space coordinates position, converted from center of mass space coordinates.
           NAME : getCenterOfMassSpace( vertexVector1:MYAMVector3D , vertexVector2:MYAMVector3D , vertexVector3:MYAMVector3D , vertexVector4:MYAMVector3D ,
                                        weight1:float , weight2:float , weight3:float , weight4:float )
         RETURN : worldPosition:MYAMVector3D
    """
    center = ( vertexList[0] + vertexList[1] + vertexList[2] + vertexList[3] ) * 0.25

    D1 = center - vertexList[0]
    D2 = center - vertexList[1]
    D3 = center - vertexList[2]
    D4 = center - vertexList[3]

    worldPosition = ( D1 * weightList[0] + D2 * weightList[1] + D3 * weightList[2] + D4 * weightList[3] ) + center

    return worldPosition

  def getArea( self , vertexList=[] ):
    """
    DESCRIPTION : Return absolute quadrangle area.
           NAME : getAbsoluteArea3D( vertexVector1:MYAMVector3D , vertexVector2:MYAMVector3D , vertexVector3:MYAMVector3D , vertexVector4:MYAMVector3D )
         RETURN : area:float
    """
    pass

  def getVolume( self , vertexList=[] ):
    """
    DESCRIPTION : Return quadrangle volume.
           NAME : getRelativeVolume3D( vertexVector1:MYAMVector3D , vertexVector2:MYAMVector3D , vertexVector3:MYAMVector3D , vertexVector4:MYAMVector3D )
         RETURN : volume:float
    """
    pass

  def getEdgeLengthList( self , vertexList=[] ):
    """
    DESCRIPTION : Return four quadrangle edge lengths.
           NAME : getAllEdgeLength( vertexVector1:MYAMVector3D , vertexVector2:MYAMVector3D , vertexVector3:MYAMVector3D )
         RETURN : [ edgeLength1( float ) , edgeLength2( float ) , edgeLength3( float ) , edgeLength4( float ) ]
    """
    e1 = vectorLength( vertexList[1] - vertexList[0] )
    e2 = vectorLength( vertexList[2] - vertexList[1] )
    e3 = vectorLength( vertexList[3] - vertexList[2] )
    e4 = vectorLength( vertexList[0] - vertexList[3] )

    edgeLengthList = [ e1 , e2 , e3 , e4 ]
    return edgeLengthList





##########################################
##### 多角形関数 - Polygon functions #####
##########################################

class MYAMFnPolygon():

  def getCenterOfMassSpacePosition( self , vertexList=[] , weightList=[] ):
    """
    DESCRIPTION : Return world space coordinates position, converted from center of mass space coordinates.
           NAME : getCenterOfMassSpace( vertexVector1:MYAMVector3D , vertexVector2:MYAMVector3D , vertexVector3:MYAMVector3D , vertexVector4:MYAMVector3D ,
                                        weight1:float , weight2:float , weight3:float , weight4:float )
         RETURN : worldPosition:MYAMVector3D
    """
    pass

  def getArea( self , vertexList=[] ):
    """
    DESCRIPTION : Return absolute quadrangle area.
           NAME : getAbsoluteArea3D( vertexVector1:MYAMVector3D , vertexVector2:MYAMVector3D , vertexVector3:MYAMVector3D , vertexVector4:MYAMVector3D )
         RETURN : area:float
    """
    pass


  def getVolume( self , vertexList=[] ):
    """
    DESCRIPTION : Return quadrangle volume.
           NAME : getRelativeVolume3D( vertexVector1:MYAMVector3D , vertexVector2:MYAMVector3D , vertexVector3:MYAMVector3D , vertexVector4:MYAMVector3D )
         RETURN : volume:float
    """
    pass


  def getEdgeLengthList( self , vertexList=[] ):
    """
    DESCRIPTION : Return four quadrangle edge lengths.
           NAME : getAllEdgeLength( vertexVector1:MYAMVector3D , vertexVector2:MYAMVector3D , vertexVector3:MYAMVector3D )
         RETURN : [ edgeLength1( float ) , edgeLength2( float ) , edgeLength3( float ) , edgeLength4( float ) ]
    """
    pass


















######################################
##### 幾何テスト - Geometry test #####
######################################

##################################
##### 最近点 - Nearest Point #####
##################################

class MYAMFnNearestPoint():

  ##### 平面上 - On plane
  def plane( anyPoint , planePoint , planeNormal ):
    """
    DESCRIPTION : Return nearest point on plane.
           NAME : nearestPointOnPlane( anyPoint:MYAMVector3D , planePoint:MYAMVector3D , normal:MYAMVector3D )
         RETURN : nearestPoint:MYAMVector3D
    """
    planeNormal = normalizeVector( planeNormal )

    distancePlanePoint = dotProduct( planePoint , planeNormal )
    distanceAnyPoint   = dotProduct( anyPoint   , planeNormal )

    planeDistance = distancePlanePoint - distanceAnyPoint
    nearestPoint  = anyPoint + ( planeNormal * planeDistance )

    return nearestPoint

  ##### ベクトル上 - On Vector
  def vector( anyPoint , Vi , Vf ):
    """
    DESCRIPTION : Return nearest point on vector.
           NAME : nearestPointOnVector( anyPoint:MYAMVector3D , Pi_vectorInit:MYAMVector3D , Pi_vectorFinish:MYAMVector3D )
         RETURN : nearestPoint:MYAMVector3D
    """
    V1 = Vi - Vf
    normalizedV1 = V1.normal()

    V2 = anyPoint - Vi
    projectionLength = V2.dot( normalizedV1 )

    nearestPoint = Vi + normalizedV1 * projectionLength

    return nearestPoint

  ##### 球面上 - On Sphere Surface
  def sphere( anyPoint , sphereCenter , sphereRadius ):
    """
    DESCRIPTION : Return nearest point on sphere surface.
           NAME : nearestPointOnSphereSurface( anyPoint:MYAMVector3D , radius:float , sphereCenter:MYAMVector3D )
         RETURN : nearestPoint:MYAMVector3D
    """
    vectorPointToCenter = sphereCenter - anyPoint

    distancePointToCenter  = vectorLength( vectorPointToCenter )
    distancePointToSurface = ( distancePointToCenter - sphereRadius )

    nearestPoint = anyPoint + ( distancePointToSurface / distancePointToCenter ) * vectorPointToCenter

    return nearestPoint





###################################
##### 交差点 - intersectPoint #####
###################################

class MYAMFnIntersectPoint():

  ##### 三平面 - Cross point of Three plane
  def threePlanes( n1 , d1 , n2 , d2 , n3 , d3 ):
    """
    DESCRIPTION : Return cross point 3 planes.
           NAME : getCrossPoint3Planes( n1_plane1Normal:MYAMVector3D , d1_plane1Distance:float ,
                                        n2_plane1Normal:MYAMVector3D , d2_plane2Distance:float ,
                                        n3_plane1Normal:MYAMVector3D , d3_plane3Distance:float )
         RETURN : crossingPoint:MYAMVector3D
    """
    numerator   = d1 * n2.cross( n3 ) + d2 * n3.cross( n1 ) + d3 * n1.cross( n2 )
    denominator = ( n1.cross( n2 ) ).dot( n3 )

    crossingPoint = numerator / denominator

    return crossingPoint





#############################################
##### ベクトル交差時間 - Intersect time #####
#############################################

class MYAMFnVectorIntersectTime():

  def vector( V1i , V1f , V2i , V2f ):
    """
    DESCRIPTION : Return coefficient to point of the approach of two vectors.
           NAME : intersectTimeVectorToVector( V1i:MYAMVector3D , V1f:MYAMVector3D ,
                                               V2i:MYAMVector3D , V2f:MYAMVector3D )
         RETURN : [ t1_crossingTime1:float , t2_crossingTime2:float ]
    """
    V1 = V1f - V1i
    V2 = V2f - V2i
    deferenceV1ToV2 = V2i - V1i

    cross1 = crossProduct( deferenceV1ToV2 , V2 )
    cross2 = crossProduct( deferenceV1ToV2 , V1 )

    crossV1ToV2 = crossProduct( V1 , V2 )

    crossLength = vectorLength( crossV1ToV2 )

    t1 = dotProduct( cross1 , crossV1ToV2 ) / ( crossLength * crossLength )
    t2 = dotProduct( cross2 , crossV1ToV2 ) / ( crossLength * crossLength )

    intersectTimeList = [ t1 , t2 ]

    return intersectTimeList


  def plane( V1i , V1f , planePoint , planeNormal ):
    """
    DESCRIPTION : Return coefficient to vector of the approach of plane.
           NAME : intersectTimeVectorToPlane(  V1i_vector1Init:MYAMVector3D , V1f_vector1Finish:MYAMVector3D ,
                                               planePoint:MYAMVector3D , planeNormal:MYAMVector3D )
         RETURN : intersectTime:float
    """
    V1 = V1f - V1i
    normalizedPN = normalizeVector( planeNormal )
    faceD = dotProduct( planePoint , normalizedPN )

    intersectTime = ( faceD - dotProduct( V1i , normalizedPN ) ) / ( dotProduct( V1 , normalizedPN ) )

    return intersectTime


  def sphere( V1i , V1f , sphereCenter , radius ):
    """
    DESCRIPTION : Return coefficient to vector of the approach of Sphere.
           NAME : intersectTimeVectorToSphere( V1i:MYAMVector3D , V1f:MYAMVector3D , sphereCenter:MYAMVector3D , radius:float )
         RETURN : [ inTime:float , outTime:float ]
    """
    V1  = V1f - V1i

    pointToSphereCenter = sphereCenter - V1i
    projectionDistance  = dotProduct( V1 , pointToSphereCenter )

    f = math.sqrt( math.pow( radius , 2 ) -
                   math.pow( vectorLength( pointToSphereCenter ) , 2 ) +
                   math.pow( projectionDistance  , 2 ) )

    inTime  = projectionDistance - f
    outTime = projectionDistance + f

    return [ inTime , outTime ]





###################################
##### 内包判定 - include test #####
###################################

class MYAMFnIncludeTest():

  def pointInSphere( anyPoint , sphereCenter , sphereRadius ):
    """
    DESCRIPTION : Return is point includes sphere test result.
           NAME : isIncludePointInSphere( point:MYAMVector3D , sphereCenter:MYAMVector3D , radius:float )
         RETURN : bool
    """
    distance = ( sphereCenter - point ).length()

    if distance > sphereRadius:
      return False
    else:
      return True

  def pointInBox( anyPoint , minPointBB , maxPointBB ):
    """
    DESCRIPTION : Return is point includes box test result.
           NAME : isIncludePointInBox( point:MYAMVector3D , minPointBB:MYAMVector3D , maxPointBB:MYAMVector3D )
         RETURN : bool
    """
    if ( minPointBB.x <= anyPoint.x <= maxPointBB.x ) and ( minPointBB.y <= anyPoint.y <= maxPointBB.y ) and ( minPointBB.z <= anyPoint.z <= maxPointBB.z ):
      return True
    else:
      return False









#####################################
##### 交差判定 - intersect test #####
#####################################

class MYAMFnIntersectTest():

  def vectorToVector( V1i , V1f , V2i , V2f ):
    """
    DESCRIPTION : Return is vector intersects vector test result.
           NAME : isIntersectVectorToVector( V1i:MYAMVector3D , V1f:MYAMVector3D , V2i:MYAMVector3D , V2f:MYAMVector3D )
         RETURN : bool
    """
    intersectTime = intersectTimeVectorToVector( V1i , V1f , V2i , V2f )

    if ( 0.0 <= intersectTime[0] <= 1.0 ) and ( 0.0 <= intersectTime[1] <= 1.0 ):
      return True
    else:
      return False

  def sphereToPlane( sphereCenter , sphereRadius , planePoint , planeNormal ):
    """
    DESCRIPTION : Return is sphere intersects plane test result.
           NAME : isIntersectSphereToPlane( sphereCenter:MYAMVector3D , planePoint:MYAMVector3D , planeNormal:MYAMVector3D )
         RETURN : bool
    """
    nearestPoint = nearestPointOnPlane( sphereCenter , planePoint , planeNormal )
    distVector   = nearestPoint - sphereCenter

    distance     = vectorLength( distVector )

    if sphereRadius >= distance:
      return True
    else:
      return False

  ##### 球->球 - Sphere to sphere
  def sphereToSphere( self , sphereCenter1 , sphereRadius1 , sphereCenter2 , sphereRadius2 ):
    """
    DESCRIPTION : Return is sphere intersects sphere test result.
           NAME : isIntersectSphereToSphere( center1:MYAMVector3D , radius1:float , center2:MYAMVector3D , radius2:float )
         RETURN : bool
    """
    distance = ( sphereCenter2 - sphereCenter1 ).length()

    if distance > ( sphereRadius1 + sphereRadius2 ):
      return False
    else:
      return True













##################################################################
##### ワールド座標系関数 - World coordinate system functions #####
##################################################################

##### 最も近いワールド軸をとる -
def nearestWorldAxis( vector ):
  axisVectorList = [ MYAMVector3D( 1,0,0 ) ,
                     MYAMVector3D( 0,1,0 ) ,
                     MYAMVector3D( 0,0,1 ) ,
                     MYAMVector3D( -1,0,0 ) ,
                     MYAMVector3D( 0,-1,0 ) ,
                     MYAMVector3D( 0,0,-1 ) ]

  maxDot = 0
  nearestAxis = None

  for axisVector in axisVectorList:
    dot = dotProduct( vector , axisVector )

    if maxDot < dot:
      maxDot = dot
      nearestAxis = axisVector

  return nearestAxis





###################################################
##### ベジェ曲線関数 - Bezier curve functions #####
###################################################

def bezier3D( P , t ):
  res = MYAMVector3D()
  res.x = P[0].x*(1-t)**3 + 3*P[1].x*(1-t)**2*t + 3*P[2].x*(1-t)*t**2 + P[3].x*t**3
  res.y = P[0].y*(1-t)**3 + 3*P[1].y*(1-t)**2*t + 3*P[2].y*(1-t)*t**2 + P[3].y*t**3
  res.z = P[0].y*(1-t)**3 + 3*P[1].z*(1-t)**2*t + 3*P[2].z*(1-t)*t**2 + P[3].z*t**3
  return res






FnTri  = MYAMFnTriangle()
FnQuad = MYAMFnQuadrangle()













######################################
##### 以下はクラス化しない関数群 #####
######################################

################################################################
##### 2元1次連立方程式 - Simultaneous equation 2 variables #####
################################################################

def solveSimultaneousEquation2Variables( a1 , b1 , d1 , a2 , b2 , d2 ):
  """
  DESCRIPTION : Solve simultaneous equations of two variables.
                a1x + b1y = d1
                a2x + b2y = d2
         NAME : solveSimultaneousEquation2Variables( a1:float , b1:float , d1:float ,
                                                     a2:float , b2:float , d2:float )

       RETURN : [ X:float , Y:float ]
  """
  numeratorX   = b2 * d1 - b1 * d2
  denominatorX = a2 * b1 - a1 * b2

  if numeratorX == 0:
    raise ValueError , "numeratorX is zero. stop this process."
  if denominatorX == 0:
    raise ValueError , "denominatorX is zero. stop this process."

  numeratorY   = a2 * d1 - a1 * d2
  denominatorY = a2 * b1 - a1 * b2

  if numeratorY == 0:
    raise ValueError , "numeratorY is zero. stop this process."
  if denominatorY == 0:
    raise ValueError , "denominatorY is zero. stop this process."

  X = -( numeratorX / denominatorX )
  Y =  ( numeratorY / denominatorY )

  solvedValueList = [ X , Y ]

  return solvedValueList

################################################################
##### 3元1次連立方程式 - Simultaneous equation 3 variables #####
################################################################

def solveSimultaneousEquation3Variables( a1 , b1 , c1 , d1 , a2 , b2 , c2 , d2 ,  a3 , b3 , c3 , d3 ):
  """
  DESCRIPTION : Solve simultaneous equations of three variables.
                a1x + b1y + c1z = d1
                a2x + b2y + c2z = d2
                a3x + b3y + c3z = d3

         NAME : solveSimultaneousEquation3Variables( a1:float , b1:float , c1:float , d1:float ,
                                                     a2:float , b2:float , c2:float , d2:float ,
                                                     a3:float , b3:float , c3:float , d3:float )

       RETURN : [ X:float , Y:float , Z:float ]
  """
  numeratorX   = b1*(c3*d2-c2*d3) + c1*(b2*d3-b3*d2) + (b3*c2-b2*c3)*d1
  denominatorX = a1*(b3*c2-b2*c3) + b1*(a2*c3-a3*c2) + (a3*b2-a2*b3)*c1

  if numeratorX == 0:
    raise ValueError , "numeratorX is zero. stop this process."
  if denominatorX == 0:
    raise ValueError , "denominatorX is zero. stop this process."

  numeratorY   = a1*(c3*d2-c2*d3) + c1*(a2*d3-a3*d2) + (a3*c2-a2*c3)*d1
  denominatorY = a1*(b3*c2-b2*c3) + b1*(a2*c3-a3*c2) + (a3*b2-a2*b3)*c1

  if numeratorY == 0:
    raise ValueError , "numeratorY is zero. stop this process."
  if denominatorY == 0:
    raise ValueError , "denominatorY is zero. stop this process."

  numeratorZ   = a1*(b3*d2-b2*d3) + b1*(a2*d3-a3*d2) + (a3*b2-a2*b3)*d1
  denominatorZ = a1*(b3*c2-b2*c3) + b1*(a2*c3-a3*c2) + (a3*b2-a2*b3)*c1

  if numeratorZ == 0:
    raise ValueError , "numeratorZ is zero. stop this process."
  if denominatorZ == 0:
    raise ValueError , "denominatorZ is zero. stop this process."

  X =  ( numeratorX / denominatorX )
  Y = -( numeratorY / denominatorY )
  Z =  ( numeratorZ / denominatorZ )

  solvedValueList = [ X , Y , Z ]
  return solvedValueList





###########################################
##### ベクトル関数 - Vector Functions #####
###########################################

def projectionLength( vector1 , vector2 ):
  """
  DESCRIPTION : Return projected vector length.
         NAME : projectionLength( vector1:MYAMVector3D , vector2:MYAMVector3D )
       RETURN : projectionLength:float
  """
  normalizedVector2 = vectorNormalize( vector2 )
  projectionLength  = dotProduct( vector1 , normalizedVector2 )
  return projectionLength

def rotateVectorAtAnyAxis( vector , axis , angle ):
  """
  DESCRIPTION : Return rotated vector at any axis.
         NAME : rotateVectorAtAnyAxis( vector:MYAMVector3D , axis:MYAMVector3D , angle:float_radian )
       RETURN : rotatedVector:MYAMVector3D
  """
  ## 回転軸ベクトルを正規化しておく
  axis.doNormalizeSelf()

  ## 回転させたいベクトルを回転軸に投影し回転軸に掛けることで、投影されたベクトルを得る（V||）
  projectionVA = dotProduct( vector , axis ) * axis

  ## 回転させるベクトルから回転軸に対して垂直に下ろされるベクトルを得る（V⊥）
  verticalVA   = vector - projectionVA

  ## 回転軸とV⊥の外積をとる
  crossA_verticalVA = crossProduct( axis , verticalVA )

  ## 回転後のベクトルから回転軸へ垂直に降ろされるベクトルを得る
  rotateVector = math.cos( angle ) * verticalVA + math.sin( angle ) * crossA_verticalVA

  return projectionVA + rotateVector





#######################################
##### 行列関数 - Matrix Functions #####
#######################################

def productMatrix3DToVector3D( m , v ):
  """
  DESCRIPTION : Return product calculated vector.
         NAME : productMatrix3DToVector3D( m:MYAMMatrix3D , v:MYAMVector3D )
       RETURN : No Variable:MYAMVector3D
  """
  _11 = ( v.x * m._11 ) + ( v.y * m._21 ) + ( v.z * m._31 ) + ( v.w * m._41 )
  _12 = ( v.x * m._12 ) + ( v.y * m._22 ) + ( v.z * m._32 ) + ( v.w * m._42 )
  _13 = ( v.x * m._13 ) + ( v.y * m._23 ) + ( v.z * m._33 ) + ( v.w * m._43 )
  _14 = ( v.x * m._14 ) + ( v.y * m._24 ) + ( v.z * m._34 ) + ( v.w * m._44 )

  return MYAMVector3D( _11 , _12 , _13 , _14 )


def determinantMatrix( m ):
  return ( m._11 * ( m._22 * ( m._33 * m._44 - m._34 * m._43 ) - m._32 * ( m._23 * m._44 + m._24 * m._43 ) + m._42 * ( m._23 * m._34 - m._24 * m._33 ) ) -
           m._21 * ( m._12 * ( m._33 * m._44 - m._34 * m._43 ) - m._32 * ( m._13 * m._44 + m._14 * m._43 ) + m._42 * ( m._13 * m._34 - m._14 * m._33 ) ) +
           m._31 * ( m._12 * ( m._23 * m._44 - m._24 * m._43 ) - m._22 * ( m._13 * m._44 + m._14 * m._43 ) + m._42 * ( m._13 * m._24 - m._14 * m._23 ) ) -
           m._41 * ( m._12 * ( m._23 * m._34 - m._24 * m._33 ) - m._22 * ( m._13 * m._34 + m._14 * m._33 ) + m._32 * ( m._13 * m._24 - m._14 * m._23 ) ) )

def adjointMatrix( m ):
  determinant = determinantMatrix( m )






###########################
##### 数列操作関数 -  #####
###########################

def normalyzeFloatList( floatNums ):
  res = []
  buf = 0

  for floatNum in floatNums:
    buf += floatNum * floatNum

  length = math.sqrt( buf )

  for floatNum in floatNums:
    res.append( floatNum / length )

  return res







######################
## Import process Message
######################
print "MODULE IMPORTED... MYAM_PyLib_geometry"