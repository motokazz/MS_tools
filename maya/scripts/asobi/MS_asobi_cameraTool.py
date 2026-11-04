# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_asobi_cameraTool
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds
import os
import pickle

sdir = os.path.dirname(os.path.abspath(__file__))
init_path = sdir.replace('\\','/') + '/MS_asobi_cameraTool_init.pickle'

init_var = [0,100,0,-20000]

def get_camera_assets():
	sel = cmds.ls(type='transform',l=True)
	result = []
	for each in sel:
		if cmds.attributeQuery('LoxFile',n=each,ex=True):
			if 'vr_player_' in cmds.getAttr(each+'.LoxFile'):result.append(each)
			if 'goal' in cmds.getAttr(each+'.LoxFile'):result.append(each)
			if 'carpet' in cmds.getAttr(each+'.LoxFile'):result.append(each)

	cmds.textScrollList('MS_asobi_cameraTool_camera_list',e=True,ra=True)
	cmds.textScrollList('MS_asobi_cameraTool_camera_list',e=True,append=result)

def get_camera_assets_selection():
	a=cmds.textScrollList('MS_asobi_cameraTool_camera_list',q=True,si=True)
	cmds.select(a,r=True)


def init_save():
	global init_var
	init_var = [
		cmds.floatField('MS_asobi_cameraTool_floatField_x',q=True,v=True)
		,cmds.floatField('MS_asobi_cameraTool_floatField_y',q=True,v=True)
		,cmds.floatSliderGrp('MS_asobi_cameraTool_floatField_z',q=True,max=True)
		,cmds.floatSliderGrp('MS_asobi_cameraTool_floatField_z',q=True,min=True)
	]

	f=open( init_path,'wb')
	pickle.dump(init_var,f)
	f.close()
	print 'init save success'

def init_load():
	global init_var
	if os.path.exists(init_path):
		f=open( init_path,'r')
		init_var = pickle.load(f)
		f.close()
		print init_var


def camera_update():

	if cmds.getAttr('|persp.tx',l=True):
		cmds.setAttr('|persp.tx',l=False)
		cmds.setAttr('|persp.ty',l=False)
		cmds.setAttr('|persp.tz',l=False)

	x = cmds.floatField('MS_asobi_cameraTool_floatField_x',q=True,v=True)
	y = cmds.floatField('MS_asobi_cameraTool_floatField_y',q=True,v=True)
	z = cmds.floatSliderGrp('MS_asobi_cameraTool_floatField_z',q=True,v=True)

	try:
		cmds.setAttr('|persp.tx',x)
	except:
		pass

	try:
		cmds.setAttr('|persp.ty',y)
	except:
		pass

	try:
		cmds.setAttr('|persp.tz',z)
	except:
		pass


def get_position_end():
	t = cmds.xform(q=True,t=True,ws=True)
	cmds.floatField('MS_asobi_cameraTool_floatField_end',e=True,v=t[2])
	set_slider()

def get_position_start():
	t = cmds.xform(q=True,t=True,ws=True)
	cmds.floatField('MS_asobi_cameraTool_floatField_x',e=True,v=t[0])
	cmds.floatField('MS_asobi_cameraTool_floatField_y',e=True,v=t[1])
	cmds.floatField('MS_asobi_cameraTool_floatField_start',e=True,v=t[2])
	set_slider()

def set_slider():

	a = cmds.floatField('MS_asobi_cameraTool_floatField_start',q=True,v=True)
	b = cmds.floatField('MS_asobi_cameraTool_floatField_end',q=True,v=True)

	if a>b:
		cmds.floatSliderGrp('MS_asobi_cameraTool_floatField_z',e=True,min = b,max = a)
	else:
		cmds.floatSliderGrp('MS_asobi_cameraTool_floatField_z',e=True,min = a,max = b)



def auto_lock_camera():
	cmds.setAttr('|persp.tx',l=True)
	cmds.setAttr('|persp.ty',l=True)
	cmds.setAttr('|persp.tz',l=True)
	cmds.button('MS_asobi_cameraTool_lock',l='locked',e=True,bgc=[0.8,0.6,0.8])

def lock_camera_attr():
	if cmds.getAttr('|persp.tx',l=True):
		cmds.setAttr('|persp.tx',l=False)
		cmds.setAttr('|persp.ty',l=False)
		cmds.setAttr('|persp.tz',l=False)
		cmds.button('MS_asobi_cameraTool_lock',l='unlocked',e=True,bgc=[0.6,0.8,0.6])

	else:
		cmds.setAttr('|persp.tx',l=True)
		cmds.setAttr('|persp.ty',l=True)
		cmds.setAttr('|persp.tz',l=True)
		cmds.button('MS_asobi_cameraTool_lock',l='locked',e=True,bgc=[0.8,0.6,0.8])


def LayoutA():
	
	init_load()

	cmds.frameLayout('MS_asobi_cameraTool_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_asobi_cameraTool',cll=True,cl=False)
	cmds.columnLayout('MS_asobi_cameraTool_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_asobi_cameraTool',bgc=[0.9,0.9,0.9],fn='boldLabelFont')

	cmds.button('get_camera_assets',c=lambda *args:get_camera_assets())	
	cmds.textScrollList('MS_asobi_cameraTool_camera_list',numberOfRows=8, allowMultiSelection=False,sc=lambda *args:get_camera_assets_selection())

	cmds.floatField('MS_asobi_cameraTool_floatField_x',v=init_var[0])
	cmds.floatField('MS_asobi_cameraTool_floatField_y',v=init_var[1])
	
	cmds.floatField('MS_asobi_cameraTool_floatField_start',v=init_var[2],cc=lambda *args:set_slider())
	cmds.button(l='get_position_start',c=lambda *args:get_position_start())
	
	cmds.floatField('MS_asobi_cameraTool_floatField_end',v=init_var[3],cc=lambda *args:set_slider())
	cmds.button(l='get_position_end',c=lambda *args:get_position_end())

	cmds.floatSliderGrp('MS_asobi_cameraTool_floatField_z',dc=lambda *args:camera_update(),cc=lambda *args:auto_lock_camera())
	cmds.floatSliderGrp('MS_asobi_cameraTool_floatField_z',e=True,min=init_var[3])
	cmds.floatSliderGrp('MS_asobi_cameraTool_floatField_z',e=True,max=init_var[2])

	cmds.button('MS_asobi_cameraTool_lock',l='lock_camera_attr',c=lambda *args:lock_camera_attr())
	
	cmds.separator()
	cmds.button(l='save init',c=lambda *argv:init_save())

	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_asobi_cameraTool_window',q=True,ex=True):
		cmds.deleteUI('MS_asobi_cameraTool_window')
	cmds.window('MS_asobi_cameraTool_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_asobi_cameraTool_window')
	
