#-*- coding:UTF-8 -*-

#*******************************************************************************
'''

Tool Name     : MYAM_PyLib_math
Description   : 数学モジュール

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
[date] details

'''
#*******************************************************************************



#################################
##### import some libraries #####
#################################
import math

###########################
##### BASIC FUNCTIONS #####
###########################

##### 基本関数 - Basic numerical functions

def roundOffFloat( value , figure ):
  divider    = 10 ** -figure
  multiplier = 10 ** figure
  return math.floor( ( value * multiplier ) + 0.5 ) * divider





##### 名前考え中
def step( value , threshold ):
  return float( threshold <= value )

def pulse( value , threshold1 , threshold2 ):
  return step( value , threshold1 ) - step( value , threshold2 )

def clamp( value , min , max ):
  if value <= min:
    return min
  elif value >= max:
    return max
  else:
    return value

def smoothStep( value , threshold1 , threshold2 ):
  if value <= threshold1:
    return 0.0
  elif value >= threshold2:
    return 1.0
  else:
    n = ( value - threshold1  ) / ( threshold2 - threshold1 )

    resValue = ( n * n ) * ( 3.0 - 2.0 * n ) ## [ value = -2n^3 + 3n^2 ] のグラフを n=0-1 の範囲で描こうとしてる (三次曲線)
    return resValue

def gammaCorrect( value , gamma ):
  return math.pow( value , ( 1.0 / gamma ) )

def bias( value , biasValue ):
  return math.pow( value , ( math.log10( biasValue ) / math.log10( 0.5 ) ) )

def gain( value , gainValue ):
  if value == 0.0:
    return 0.0
  elif value == 1.0:
    return 1.0
  elif value < 0.5:
    return ( bias( ( 2.0 * value ) , ( 1.0 - gainValue ) ) * 0.5 )
  else:
    return ( 1 - bias( ( 2.0 - 2.0 * value ) , ( 1.0 - gainValue ) ) * 0.5 )

def boxStep( value , threshold1 , threshold2 ):
  return clamp( ( value - threshold1 ) / ( threshold2 - threshold1 ) , 0.0 , 1.0 )










######################
## Imported message
######################
print "MODULE IMPORTED... MYAM_PyLib_math"