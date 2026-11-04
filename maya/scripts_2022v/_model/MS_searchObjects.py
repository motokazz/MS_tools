# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_searchObjects
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds


dict = {}

def getUUID():
	sel = cmds.ls(sl=True,uid=True)
	cmds.textField('MS_searchODX_search_attr_var',e=True,tx=sel[0])

def getLongName():
	sel = cmds.ls(sl=True,l=True)
	cmds.textField('MS_searchODX_search_attr_var',e=True,tx=sel[0])

def search_by_attr_var():
	res = []
	uid = cmds.textField('MS_searchODX_search_attr_var',q=True,tx=True)
	obj = cmds.ls(type='transform',l=True)
	for each in obj:
		attrs = cmds.listAttr(each,ud = True,st='*rigger*')
		if attrs:
			for ea in attrs:
				try:
					if uid in cmds.getAttr(each + '.' + ea):
						res.append(each)
				except:
					pass
	cmds.select(res,r=True)
	cmds.textScrollList('MS_searchObjects_list_odx',e=True,da=True,ra=True)
	cmds.textScrollList('MS_searchObjects_list_obj',e=True,da=True,ra=True)
	for each in res:
		cmds.textScrollList('MS_searchObjects_list_obj',e=True,append=each)


def list_objects(ATTR='Odx'):
	
	global dict
	dict = {}

	search_word = cmds.textField('MS_searchODX_search_word',q=True,tx=True)

	ad = cmds.ls(type='transform',l=True)

	for each in ad:
		if cmds.attributeQuery(ATTR,node = each,ex=True):
			odx=cmds.getAttr(each + '.' + ATTR)
			if odx in dict.keys():
				dict[odx].append(each)
			else:
				dict.setdefault(odx,[each])

	cmds.textScrollList('MS_searchObjects_list_odx',e=True,da=True)
	cmds.textScrollList('MS_searchObjects_list_odx',e=True,ra=True)
	for each in sorted(dict.keys()):
	#for each in sorted(dict.keys(),key = lambda x: len(x[1])):
		if search_word == '':
			cmds.textScrollList('MS_searchObjects_list_odx',e=True,append=each)
		elif search_word in each:
			cmds.textScrollList('MS_searchObjects_list_odx',e=True,append=each)

	
def selectODX():
	sel = cmds.textScrollList('MS_searchObjects_list_odx',q=True,si=True)

	cmds.textScrollList('MS_searchObjects_list_obj',e=True,ra=True)

	cmds.select(cl=True)
	for each in sel:
		#cmds.select(dict[each],add=True)
		cmds.textScrollList('MS_searchObjects_list_obj',e=True,append=dict[each])

def selectObj():
	sel = cmds.textScrollList('MS_searchObjects_list_obj',q=True,si=True)
	cmds.select(sel,r=True)


def main():
	mode = cmds.radioButtonGrp('MS_searchObjects_mode',q=True,sl=True)

	search_word = cmds.textField('MS_searchObjects_search_word',q=True,tx=True)
	result = []
	ad = []

	if mode == 1:
		ad = cmds.listRelatives(ad=True,type='transform',f=True)
	if mode == 2:
		ad = cmds.listRelatives(c=True,type='transform',f=True)

	if not ad:
		if mode == 1:
			ad = cmds.ls(type='transform',l=True)

		if mode == 2:
			ad = cmds.ls(l=True,assemblies=True)

	for each in ad:
		if not cmds.listRelatives(each,s=True):
			continue
		if search_word in each:
			result.append(each)

	if len(result)>0:
		cmds.select(result,r=True)

def LayoutA():
	cmds.frameLayout('MS_searchObjects_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_searchObjects',cll=True,cl=False)
	cmds.columnLayout('MS_searchObjects_mainLayout',adj=True)
	cmds.separator()


	# search_word
	cmds.text(l='MS_searchObjects_by_nodename',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.rowLayout(nc=2,ad2=1,cw2=[200,50])
	cmds.textField('MS_searchObjects_search_word',cc=lambda *args:main())
	cmds.button(l='search',c=lambda *args:main())
	cmds.setParent('..')
	cmds.separator()
	cmds.radioButtonGrp('MS_searchObjects_mode',label='select mode', labelArray2=['all descendents', 'childlen'], numberOfRadioButtons=2 ,sl=2)
	cmds.separator()


	# search_attr_var
	cmds.text(l='MS_searchObjects_by_nodename',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.rowLayout(nc=3,ad3=1,cw3=[200,50,50])
	cmds.textField('MS_searchODX_search_attr_var',cc=lambda *args:search_by_attr_var())
	cmds.button(l='getUUID',c=lambda *args:getUUID())
	cmds.button(l='search',c=lambda *args:search_by_attr_var())

	cmds.setParent('..')
	cmds.separator()


	# ODX search
	cmds.text(l='MS_searchODX',bgc=[0.9,0.9,0.9],fn='boldLabelFont')

	cmds.rowLayout(nc=2,ad2=1,cw2=[200,50])
	cmds.textField('MS_searchODX_search_word',cc=lambda *args:list_objects(ATTR='Odx'))
	cmds.button(l='odx_list',c=lambda *args:list_objects(ATTR='Odx'))
	cmds.setParent('..')
	
	cmds.rowLayout(nc=2,ad2=1,cw2=[200,50])
	cmds.textField('MS_searchODX_search_word',cc=lambda *args:list_objects(ATTR='LoxFile'))
	cmds.button(l='lox_list',c=lambda *args:list_objects(ATTR='LoxFile'))
	cmds.setParent('..')

	cmds.rowLayout(nc=2,ad2=2,cw2=[200,50])
	cmds.textScrollList('MS_searchObjects_list_odx',w=200,numberOfRows=20,allowMultiSelection=True,sc=lambda *args:selectODX())
	cmds.textScrollList('MS_searchObjects_list_obj',w=100,numberOfRows=20,allowMultiSelection=True,sc=lambda *args:selectObj())
	cmds.setParent('..')
	#

	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_searchObjects_window',q=True,ex=True):
		cmds.deleteUI('MS_searchObjects_window')
	cmds.window('MS_searchObjects_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_searchObjects_window')
	