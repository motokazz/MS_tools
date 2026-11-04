# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_math.py
# 説明
#			
# 作成日
#			
########################################

import math


def vectorRot(MATRIX, DEGREE, AXIS):
	#ベクトルの回転
	# float[11] MATRIX=掛け合わせの対象となる行列:
	# float DEGREE=回転値
	# vector3 AXIS=回転軸
	#戻り値：12個のリスト。回転後のベクトルは（dist[8],dist[9],dist[10]）
	ANGLE=math.radians(DEGREE)
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

def vectorMove(MATRIX,VAR=0.0):
	#MATRIX[12]の回転軸Y方向にVAR分移動した座標を返す
	VEC=[MATRIX[8],MATRIX[9],MATRIX[10]]
	return [MATRIX[12]+(VEC[0]*VAR),MATRIX[13]+(VEC[1]*VAR),MATRIX[14]+(VEC[2]*VAR)]


