# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_larmorVoronoiControl.py
# 説明
#			
#			
# 作成日
#			
########################################
	
import maya.cmds as cmds
import maya.mel as mel

##### プラグインチェッカー #####
	
if not cmds.pluginInfo('LarmorVoronoi.mll',q=True,loaded=True):
	cmds.loadPlugin('LarmorVoronoi.mll')
	

def subcom_a():
	command='global vector $vp[];\n'
	command+='$vp={};\n'
	var=1.0
	i=0
	for x in range(-1,1):
		for y in range(-1,1):
			for z in range(-1,1):
				command+='$vp[%s]=<<%s,%s,%s>>;\n'%(i,x*var,y*var,z*var)
				i+=1

	return command

def useVp():

	bool_disjoint = cmds.checkBox('bool_disjoint',q=True,v=True)
	float_explode = cmds.floatSliderGrp('float_explode',q=True,v=True)

	command=''
	command+=subcom_a()
	command+='LarmorVoronoi'
	command+=' -p vp '
	if bool_disjoint:
		command+=' -d %s'%bool_disjoint
	if float_explode:
		command+=' -ex %s'%float_explode
	command+=';'
	print command
	mel.eval(command)



def mainCommand():
	def retDef(int_num_pieces = 10
		,string_vector_array_name = 'vp'
		,bool_disjoint = False
		,float_explode = 0.5
		,bool_use_delaunay = False
		,delaunay_b_criteria = 0
		,delaunay_s_criteria = 0
		):

		int_num_pieces =	cmds.intSliderGrp('int_num_pieces',q=True,v=True)
		string_vector_array_name = cmds.textFieldGrp('string_vector_array_name',q=True,tx=True)
		bool_disjoint = cmds.checkBox('bool_disjoint',q=True,v=True)
		float_explode = cmds.floatSliderGrp('float_explode',q=True,v=True)
		command=''


		command+=subcom_a()

		command+='LarmorVoronoi'

		if int_num_pieces:
			command+=' -np %s'%int_num_pieces
		if string_vector_array_name:
			command+=' -p %s'%string_vector_array_name
		if bool_disjoint:
			command+=' -d %s'%bool_disjoint
		if float_explode:
			command+=' -ex %s'%float_explode
		if bool_use_delaunay:
			command+=' -dy %s'%bool_use_delaunay
		if delaunay_b_criteria:
			command+=' -dyb %s'%delaunay_b_criteria
		if delaunay_s_criteria:
			command+=' -dys %s'%delaunay_s_criteria
		command+=';'

		mel.eval(command)
	return retDef
'''
		LarmorVoronoi [-np int_num_pieces | -p string_vector_array_name] [-d bool_disjoint] [-ex float_explode]
     [-dy bool_use_delaunay [-dyb delaunay_b_criteria] [-dys delaunay_s_criteria] ]
'''



def LayoutA():
	cmds.columnLayout('MS_larmorVoronoi_mainLayout',adj=True)
	cmds.intSliderGrp('int_num_pieces',l='int_num_pieces',v=10,f=True)
	cmds.textFieldGrp('string_vector_array_name')
	cmds.checkBox('bool_disjoint',v=False)
	cmds.floatSliderGrp('float_explode',l='float_explode',v=0,f=True)

	cmds.button(l='tet',c=mainCommand())
	cmds.button(l='use VP',c=lambda *args:useVp())
	cmds.setParent('..')

def UI():
	if cmds.window('MS_larmorVoronoi_window',q=True,ex=True):
		cmds.deleteUI('MS_larmorVoronoi_window')
	cmds.window('MS_larmorVoronoi_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_larmorVoronoi_window')
	