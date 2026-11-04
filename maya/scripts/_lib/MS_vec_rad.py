# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_vec_rad
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds
import math
import maya.mel as mel

def computeAnglesFromMatrix(R):
	angle_x,angle_y,angle_z = 0,0,0

	threshold = 0.001

	if(abs(R[9] - 1.0) < threshold): # R[9] = sin(x) = 1の時
		print '1'
	 	angle_x = - math.pi / 2
	 	angle_y = 0
	 	angle_z = math.atan2(R[4], R[0])
	elif(abs(R[9] + 1.0) < threshold): # R(2,1) = sin(x) = -1の時
		print '2'
	 	angle_x = math.pi / 2
	 	angle_y = 0
	 	angle_z = math.atan2(R[4], R[0])
	else:
		print '3'
		print R[9]
		angle_x = math.asin(-R[9])
		angle_y = math.atan2(R[8], R[10])
		angle_z = math.atan2(R[1], R[5])
	return angle_x,angle_y,angle_z

def descale(R,scl=[1,1,1]):
	R[0] *= (1/scl[0])
	R[5] *= (1/scl[1])
	R[10] *= (1/scl[2])
	return R

def printMatrix(R):
	print R[0:4]
	print R[4:8]
	print R[8:12]
	print R[12:16]

def printMatrixD(R):
	print map(math.degrees,R[0:4])
	print map(math.degrees,R[4:8])
	print map(math.degrees,R[8:12])
	print map(math.degrees,R[12:16])

def main():
	OBJ=cmds.ls(sl=True)
	MATRIX = cmds.xform(OBJ[0],q=True,matrix=True)
	SCL = cmds.xform(OBJ[0],q=True,s=True,ws=True)
	
	printMatrixD(MATRIX)

	#MATRIX = descale(MATRIX,SCL)
	ROT = computeAnglesFromMatrix(MATRIX)
	cmds.xform(OBJ[0],ro=(math.degrees(ROT[0]),math.degrees(ROT[1]),math.degrees(ROT[2])))

	printMatrix(MATRIX)

	print ROT

def LayoutA():
	cmds.frameLayout('MS_vec_rad_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_vec_rad',cll=True,cl=False)
	cmds.columnLayout('MS_vec_rad_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_vec_rad',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_vec_rad_window',q=True,ex=True):
		cmds.deleteUI('MS_vec_rad_window')
	cmds.window('MS_vec_rad_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_vec_rad_window')
	