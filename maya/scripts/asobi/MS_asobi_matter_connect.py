# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_asobi_matter_connect
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds
import os
import glob
path_texture='D:/asobi/asset/graphic/multi_platformer/bg/textures/'
texname = cmds.file(q=True,sn=True).split('/')[-1].split('.')[0].replace('mup_bg','mup_bg_tex')

def detailmap():
	
	dic={
		'd':'baseDetail0'
		,'n':'normDetail0'
		,'r':'roughDetail0'
	}

	shd = cmds.ls(type='JsPBRSingle',sl=True)[0]
	texname = cmds.textField('MS_asobi_matter_connect_detail',q=True,tx=True)

	for each in dic.keys():
		target_texture = path_texture+texname+'_'+each+'.tif'
		if os.path.exists(target_texture):
			ftn = cmds.shadingNode('file',asTexture=True,isColorManaged=True)
			cmds.setAttr(ftn+'.fileTextureName',target_texture,type='string')
			cmds.connectAttr(ftn+'.outColor',shd+'.'+dic[each],force=True)

	#
	detailScale = cmds.floatSliderGrp('MS_asobi_matter_connect_detailScale',q=True,v=True)
	cmds.setAttr(shd+'.detailScale0',detailScale)

	#
	detailMapWorldScaling = cmds.checkBox('MS_asobi_matter_connect_detailMapWorldScaling',q=True,v=True)
	cmds.setAttr(shd+'.detailMapWorldScaling',detailMapWorldScaling)
	cmds.select(sel)

def main():
	sel = cmds.ls(sl=True)
	#sg = cmds.listConnections(each,type='shadingEngine')
	#sgs = cmds.sets(sg[0],q=True)

	#
	pshd = cmds.ls(type='JsPBRSingle',sl=True)
	if len(pshd)>0:
		shd = pshd[0]
	else:
		shd = cmds.shadingNode('JsPBRSingle',asShader=True)

	texname = cmds.textField('MS_asobi_matter_connect_textures',q=True,tx=True)
	#
	dic={
		'd':'base0'
		,'n':'normal0'
		,'r':'roughness0'
		,'m':'metallic0'
		,'e':'emissive0'
		,'ao':'occlusion0'
	}

	for each in dic.keys():
		target_texture = path_texture+texname+'_'+each+'.tif'
		print target_texture
		connect=cmds.listConnections(shd+'.'+dic[each])
		if os.path.exists(target_texture):
			
			if connect:
				ftn=connect[0]
			else:
				ftn = cmds.shadingNode('file',asTexture=True,isColorManaged=True)
				cmds.connectAttr(ftn+'.outColor',shd+'.'+dic[each],force=True)
			cmds.setAttr(ftn+'.fileTextureName',target_texture,type='string')
		elif connect:
			try:
				cmds.disconnectAttr(ftn+'.outColor')
			except:
				pass
			

	if len(sel)>0 and len(pshd)>0:
		cmds.select(sel)
		cmds.hyperShade( assign = shd )

def detail_map_list():
	kw = cmds.textField('MS_asobi_matter_connect_detail',q=True,tx=True)
	detail_map_files = glob.glob(path_texture+'*_detail_*.tif')
	fnlist=[]
	for each in detail_map_files:
		fn='_'.join(each.split('/')[-1].split('\\')[-1].split('.')[0].split('_')[0:-1])
		if not fn in fnlist:
			if kw in fn:
				fnlist.append(fn)

	cmds.textScrollList('MS_asobi_matter_connect_detailMapList',e=True,ra=True,a=fnlist)

def texture_list():
	kw = cmds.textField('MS_asobi_matter_connect_textures',q=True,tx=True)
	texture_files = glob.glob(path_texture+'*'+kw+'*.tif')
	fnlist=[]
	for each in texture_files:
		fn='_'.join(each.split('/')[-1].split('\\')[-1].split('.')[0].split('_')[0:-1])
		if not fn in fnlist:
			fnlist.append(fn)

	cmds.textScrollList('MS_asobi_matter_connect_textureList',e=True,ra=True,a=fnlist)

def matter_list():
	matterlist=cmds.ls(type='JsPBRSingle',sl=True)
	cmds.textScrollList('MS_asobi_matter_connect_matterList',e=True,ra=True,a=matterlist)


#########
# UI
#########

def LayoutA():

	cmds.frameLayout('MS_asobi_matter_connect_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_asobi_matter_connect',cll=True,cl=False)
	cmds.columnLayout('MS_asobi_matter_connect_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_asobi_matter_list',bgc=[0.9,0.9,0.9],fn='boldLabelFont')

	def matter_selection_command():
		x = cmds.textScrollList('MS_asobi_matter_connect_matterList',q=True,si=True)
		cmds.select(x[0],r=True)

	cmds.textScrollList('MS_asobi_matter_connect_matterList',h=50,sc=lambda *args:matter_selection_command())

	cmds.separator()
	# main
	cmds.text(l='MS_asobi_matter_connect',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.textField('MS_asobi_matter_connect_textures',tx=texname,cc=lambda *args:texture_list())

	def textureList_selection_command():
		x = cmds.textScrollList('MS_asobi_matter_connect_textureList',q=True,si=True)
		cmds.textField('MS_asobi_matter_connect_textures',e=True,tx=x[0])

	cmds.textScrollList('MS_asobi_matter_connect_textureList',h=100,sc=lambda *args:textureList_selection_command())
	cmds.button(l='connect textures',bgc=[0.7,0.8,0.7],c=lambda *args:main())

	# detailmap
	cmds.separator(h=10)
	cmds.text(l='connect detailmap',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.textField('MS_asobi_matter_connect_detail',tx=texname,cc=lambda *args:detail_map_list())

	def detailMapList_selection_command():
		x = cmds.textScrollList('MS_asobi_matter_connect_detailMapList',q=True,si=True)
		cmds.textField('MS_asobi_matter_connect_detail',e=True,tx=x[0])

	cmds.textScrollList('MS_asobi_matter_connect_detailMapList',h=100,sc=lambda *args:detailMapList_selection_command())
	
	#
	cmds.text(l='detailmap option',bgc=[0.6,0.6,0.6],fn='boldLabelFont')
	cmds.checkBox('MS_asobi_matter_connect_detailMapWorldScaling',l='set detailMapWorldScaling',v=True)
	cmds.floatSliderGrp('MS_asobi_matter_connect_detailScale',l='detailScale',field=True,v=2)

	cmds.button(l='detailmap',bgc=[0.7,0.8,0.7],c=lambda *args:detailmap())
	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')


def UI():
	if cmds.window('MS_asobi_matter_connect_window',q=True,ex=True):
		cmds.deleteUI('MS_asobi_matter_connect_window')
	cmds.window('MS_asobi_matter_connect_window',rtf=True,s=True)
	
	LayoutA()
	matter_list()
	detail_map_list()
	cmds.showWindow('MS_asobi_matter_connect_window')
	