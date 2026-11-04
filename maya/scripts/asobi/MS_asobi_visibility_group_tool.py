# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_asobi_visibility_group_tool
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds

# asobi utils
import muple.utility as util
import muple.importer as imp


def move_visibility_trigger_to_link_z():
	sel = cmds.ls(sl=True,l=True)
	for each in sel:
		UID=''
		if cmds.attributeQuery('TriggerOn',n=each,ex=True):
			UID = cmds.getAttr(each+'.TriggerOn')
			if UID:
				OBJ=cmds.ls(UID.split(',')[0],uid=True,l=True)
				TRN=cmds.xform(OBJ[0],q=True,t=True,ws=True)
				cmds.move(TRN[2],each,z=True,ws=True)




def set_lox_attributes(node, lox, odx = None):
	try:
		attributes = imp.loxes[lox]['Attributes']
		if odx != None:
			odx_attr = filter(lambda a:a['Name'] == 'Odx', attributes)
			odx_attr[0]['Value'] = odx
		util.set_attributes(node, attributes)
		util.add_common_attribute(node, add_as_template=False)
	except:
		pass


#####

# util

def easylink():
	sel = cmds.ls(sl=True,uuid=True)
	visibility_trigger_node = cmds.ls(sel[-1],uuid=True,l=True)[0]
	print visibility_trigger_node
	if cmds.attributeQuery('LoxFile',ex=True,n=visibility_trigger_node):
		if 'visibility_trigger' in cmds.getAttr(visibility_trigger_node+'.LoxFile'):
			str = ','.join(sel[0:-1])
			cmds.setAttr(visibility_trigger_node+'.TriggerOn',str,type='string')

def rename_belong_parent():
	sel = cmds.ls(sl=True)
	for eachsel in sel:
		name = eachsel.replace('vg_','')
		childlen = cmds.listRelatives(eachsel,c=True,f=True,type='transform')
		print childlen
		for each in childlen:
			try:
				if cmds.attributeQuery('LoxFile',ex=True,n=each):
					if 'visibility_group' in cmds.getAttr(each+'.LoxFile'):
						
						# ditectTriggerLink & connect

						try:
							linked_ap = cmds.ls(cmds.getAttr(each+'.TriggerAppear'),uid=True)[0]
							if linked_ap:
								cmds.rename(linked_ap,'visibility_trigger_'+name+'_ap')
						except:
							pass

						try:
							linked_dis = cmds.ls(cmds.getAttr(each+'.TriggerDisappear'),uid=True)[0]
							if linked_dis:
								cmds.rename(linked_dis,'visibility_trigger_'+name+'_dis')
						except:
							pass

						cmds.rename(each,'visibility_group_'+name)
			except:
				pass

	reflesh_vg_list()

# modify vg

def add(DAG = True):
	DAGS = cmds.ls(sl=True,dag=DAG,l=True,type='transform')
	sel = cmds.ls(DAGS,uid=True)
	vg = cmds.textScrollList('MS_asobi_visibility_group_tool_vg_scrollList',q=True,si=True)
	for each in vg:
		uids = cmds.getAttr(each+'.Targets').split(',')
		for eachsel in sel:
			objname = cmds.ls(eachsel,uid=True,l=True)[0]
			if cmds.attributeQuery('LoxFile',ex=True,n=objname):
				loxname = cmds.getAttr(objname+'.LoxFile')
				if not eachsel in uids:
					if 'visibility_group' in loxname:continue
					if 'visibility_trigger' in loxname:continue

					uids.append(eachsel)

		cmds.setAttr(each+'.Targets',','.join(uids),type='string')

def remove(DAG = True):
	DAGS = cmds.ls(sl=True,dag=DAG,l=True,type='transform')
	sel = cmds.ls(DAGS,uid=True)
	vg = cmds.textScrollList('MS_asobi_visibility_group_tool_vg_scrollList',q=True,si=True)
	for each in vg:
		uids = cmds.getAttr(each+'.Targets').split(',')
		for eachsel in sel:
			if eachsel in uids:
				uids.remove(eachsel)

		cmds.setAttr(each+'.Targets',','.join(uids),type='string')

def createVG(NAME = 'def'):
	
	sel = cmds.ls(sl=True,l=True)

	# create nodes
	vg = cmds.polyCube()
	set_lox_attributes(node = vg[0],lox = 'visibility_group')
	ap = cmds.spaceLocator()
	set_lox_attributes(node = ap[0],lox = 'visibility_trigger')
	dis = cmds.spaceLocator()
	set_lox_attributes(node = dis[0],lox = 'visibility_trigger')

	cmds.setAttr(vg[0]+'.TriggerAppear' , cmds.ls(ap[0],uuid=True)[0] , type ='string')
	cmds.setAttr(vg[0]+'.TriggerDisappear' , cmds.ls(dis[0],uuid=True)[0] , type='string')

	# transform
	trn = [0,0,0]
	rot = [0,0,0]
	scl = [1000,1000,1000]

	trn_ap = [0,0,0]
	trn_dis = [0,0,0]

	sel_is_visibility_group = False

	if cmds.attributeQuery('LoxFile',ex=True,n=sel[0]):
		if 'visibility_group' in cmds.getAttr(sel[0]+'.LoxFile'):

			sel_is_visibility_group =True

			trn = cmds.xform(sel[0],q=True,t=True,ws=True)
			rot = cmds.xform(sel[0],q=True,ro=True,ws=True)
			scl = cmds.xform(sel[0],q=True,s=True,ws=True)

			# ditectTriggerLink & connect

			try:
				linked_ap = cmds.ls(cmds.getAttr(sel[0]+'.TriggerAppear'),uid=True)[0]
				if linked_ap:
					trn_ap = cmds.xform(linked_ap,q=True,t=True,ws=True)
					cmds.xform(ap ,t=trn_ap,ws=True)
					linked_ap_TriggerOn = cmds.getAttr(linked_ap+'.TriggerOn')
					if linked_ap_TriggerOn:
						cmds.setAttr(ap+'.TriggerOn',linked_ap_TriggerOn,type='string')

			except:
				pass

			try:
				linked_dis = cmds.ls(cmds.getAttr(sel[0]+'.TriggerDisappear'),uid=True)[0]
				if linked_dis:
					trn_dis = cmds.xform(linked_dis,q=True,t=True,ws=True)
					cmds.xform(dis,t=trn_dis,ws=True)
					linked_ap_TriggerOn = cmds.getAttr(linked_dis+'.TriggerOn')
					if linked_ap_TriggerOn:
						cmds.setAttr(ap+'.TriggerOn',linked_ap_TriggerOn,type='string')
			except:
				pass

			# attr
			Targets = cmds.getAttr(sel[0]+'.Targets')
			cmds.setAttr(sel[0]+'.Targets',Targets,type='string')

	if len(sel) and not sel_is_visibility_group:

		#def_bb=[-0.5,-0.5,-0.5,0.5,0.5,0.5]
		DAG = cmds.ls(sel,dag=True,l=True,type='transform')
		
		for each in DAG:
			if not cmds.attributeQuery('LoxFile',ex=True,n=each):
				continue
			else:
				def_bb=cmds.xform(DAG.pop(0),q=True,t=True,ws=True)
				def_bb.extend(def_bb)
				break

		for each in DAG:
			
			if not cmds.attributeQuery('LoxFile',ex=True,n=each):continue

			pre_trn = cmds.xform(each,q=True,t=True,ws=True)

			if def_bb[0] > pre_trn[0]: def_bb[0]=pre_trn[0]
			if def_bb[1] > pre_trn[1]: def_bb[1]=pre_trn[1]
			if def_bb[2] > pre_trn[2]: def_bb[2]=pre_trn[2]
			if def_bb[3] < pre_trn[0]: def_bb[3]=pre_trn[0]
			if def_bb[4] < pre_trn[1]: def_bb[4]=pre_trn[1]
			if def_bb[5] < pre_trn[2]: def_bb[5]=pre_trn[2]

		trn=[(def_bb[3]+def_bb[0])*0.5,(def_bb[4]+def_bb[1])*0.5,(def_bb[5]+def_bb[2])*0.5]
		scl=[def_bb[3]-def_bb[0],def_bb[4]-def_bb[1],def_bb[5]-def_bb[2]]

	cmds.xform(vg,t=trn,ws=True)
	cmds.xform(vg,ro=rot,ws=True)
	cmds.xform(vg,s=scl,ws=True)

	if trn_ap == [0,0,0]:
		cmds.xform(ap ,t=[trn[0],trn[1],trn[2]+(scl[2])],ws=True)

	if trn_dis== [0,0,0]:
		cmds.xform(dis,t=[trn[0],trn[1],trn[2]-(scl[2])],ws=True)

	# rename
	rvg = cmds.rename(vg[0],'visibility_group_'+NAME)
	rap = cmds.rename(ap[0],'visibility_trigger_'+NAME+'_ap')
	rdis = cmds.rename(dis[0],'visibility_trigger_'+NAME+'_dis')

	ngp = cmds.group(em=True,n='vg_'+NAME)

	cmds.xform(ngp,t=trn,ws=True)

	cmds.parent(rvg,ngp)
	cmds.parent(rap,ngp)
	cmds.parent(rdis,ngp)

	if cmds.objExists('|optimize'):
		cmds.parent(ngp,'|optimize')

	cmds.select(sel,r=True)




	reflesh_vg_list()


# select
def select_pre():
	mods = cmds.getModifiers()
	if (mods & 1) > 0: # shift
		pass

	if (mods & 4) > 0: # ctrl
		pass

	if (mods & 8) > 0: # alt
		select_vg_node()

	if (mods & 16): # Command/Windows
		pass

def select_vg_node():
	sel = cmds.textScrollList('MS_asobi_visibility_group_tool_vg_scrollList',q=True,si=True)
	cmds.select(sel,r=True)

def select_targets():
	vg = cmds.textScrollList('MS_asobi_visibility_group_tool_vg_scrollList',q=True,si=True)
	cmds.select(cl=True)
	targets = []
	for each in vg:
		target_uid = cmds.getAttr(each+'.Targets')
		targets = target_uid.split(',')
		cmds.select(cmds.ls(targets),add=True)

def select_targets_filtered():
	vg = cmds.textScrollList('MS_asobi_visibility_group_tool_vg_scrollList',q=True,si=True)
	cmds.select(cl=True)
	targets = []
	for each in vg:
		target_uid = cmds.getAttr(each+'.Targets')
		targets = target_uid.split(',')
		filterd = remove_lox_from_loxs(cmds.ls(targets),searchWord='moving_object_joint')
		cmds.select(filterd,add=True)

def remove_lox_from_loxs(loxs,searchWord=''):
	ret=[]
	for each in loxs:
		if cmds.attributeQuery('LoxFile',ex=True,n=each):
			if not searchWord in cmds.getAttr(each+'.LoxFile'):
				ret.append(each)
	return ret

def select_appear():
	vg = cmds.textScrollList('MS_asobi_visibility_group_tool_vg_scrollList',q=True,si=True)
	cmds.select(cl=True)
	for each in vg:
		target_uid = cmds.getAttr(each+'.TriggerAppear')
		cmds.select(cmds.ls(target_uid),add=True)

def select_disappear():
	vg = cmds.textScrollList('MS_asobi_visibility_group_tool_vg_scrollList',q=True,si=True)
	cmds.select(cl=True)
	for each in vg:
		target_uid = cmds.getAttr(each+'.TriggerDisappear')
		cmds.select(cmds.ls(target_uid),add=True)

def select_registed():
	res = []
	sel = cmds.ls(sl=True,uuid=True)
	vgs = cmds.textScrollList('MS_asobi_visibility_group_tool_vg_scrollList',q=True,ai=True)

	for each in sel:
		for each_vgs in vgs:
			if each in cmds.getAttr(each_vgs+'.Targets'):
				if not each_vgs in res:
					res.append(each_vgs)
	cmds.textScrollList('MS_asobi_visibility_group_tool_vg_scrollList',e=True,da=True)
	for each_res in res:
		cmds.textScrollList('MS_asobi_visibility_group_tool_vg_scrollList',e=True,si=each_res)




# list

def sortZ(LIST,REVERSE=False):
	def sorter(LIST,COLUMN=0,REVERSE=False):
		RET=[]
		RETSORT=sorted(LIST,key=lambda x:x[COLUMN],reverse=REVERSE)
		for EACH in RETSORT:
			RET.append(EACH[0])
		return RET
		
	SRC=[]
	for EACH in LIST:
		VALUE = cmds.xform(EACH,q=True,t=True,ws=True)[2]
		SRC.append([EACH,VALUE])
	return sorter(SRC,COLUMN=1,REVERSE=REVERSE)

def list_notVG():
	res=[]
	vg = []
	all_nodes = cmds.ls(type='transform',l=True)
	all_uids = cmds.ls(type='transform',uuid=True)

	for each in all_nodes:
		if cmds.attributeQuery('LoxFile',ex=True,n=each):
			if 'visibility_group' in cmds.getAttr(each+'.LoxFile'):
				vg.append(each)

	
	for each in vg:
		target_uid = cmds.getAttr(each+'.Targets')
		targets = target_uid.split(',')
		for each_target in targets:
			if each_target in all_uids:
				all_uids.remove(each_target)

	cmds.select(all_uids,r=True)

def listVG():
	res=[]
	sel = cmds.ls(type='transform',l=True)
	for each in sel:
		if cmds.attributeQuery('LoxFile',ex=True,n=each):
			if 'visibility_group' in cmds.getAttr(each+'.LoxFile'):
				res.append(each)
	return res

def reflesh_vg_list():
	cmds.textScrollList('MS_asobi_visibility_group_tool_vg_scrollList',e=True,ra=True)
	VGS=sortZ(listVG(),REVERSE=True)
	cmds.textScrollList('MS_asobi_visibility_group_tool_vg_scrollList',e=True,a=VGS)

# ui

def LayoutA():
	cmds.frameLayout('MS_asobi_visibility_group_tool_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_asobi_visibility_group_tool',cll=True,cl=False)

	#
	cmds.columnLayout('MS_asobi_visibility_group_tool_mainLayout',adj=True)
	
	cmds.separator()
	cmds.text(l='MS_asobi_visibility_group_tool',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='reflesh_vg_list',bgc=[0.6,0.8,0.6],c=lambda *args:reflesh_vg_list())

	cmds.button(l='createVG',c=lambda *args:createVG())

	cmds.gridLayout(nc=2,cw=150)
	cmds.button(l='add DAG',c=lambda *args:add())
	cmds.button(l='removeDAG',c=lambda *args:remove())
	cmds.button(l='add ',c=lambda *args:add(DAG = False))
	cmds.button(l='remove',c=lambda *args:remove(DAG = False))
	cmds.setParent('..')

	cmds.separator()

	cmds.gridLayout(nc=2,cw=150)
	cmds.button(l='select_appear',c=lambda *args:select_appear())
	cmds.button(l='select_disappear',c=lambda *args:select_disappear())
	cmds.setParent('..')

	###

	cmds.textScrollList('MS_asobi_visibility_group_tool_vg_scrollList', ams = True ,sc=lambda *args:select_pre())
	
	###

	cmds.setParent('..')

	# 
	cmds.columnLayout('MS_asobi_visibility_group_tool_subLayout',adj=True)
	cmds.gridLayout(nc=2,cw=150)
	cmds.button(l='select_targets',c=lambda *args:select_targets())
	cmds.button(l='select_targets(without moj)',c=lambda *args:select_targets_filtered())
	cmds.setParent('..')

	cmds.button(l='rename_belong_parent',c=lambda *args:rename_belong_parent())
	cmds.separator()
	cmds.button(l='easylink',c=lambda *args:easylink())
	cmds.button(l='move_visibility_trigger_to_link_z',c=lambda *args:move_visibility_trigger_to_link_z())
	cmds.separator()
	
	cmds.button(l='list_notVG',c=lambda *args:list_notVG())
	cmds.button(l='select_registed',c=lambda *args:select_registed())
	cmds.setParent('..')
	#
	cmds.setParent('..')
	cmds.setParent('..')

	reflesh_vg_list()

def UI():
	if cmds.window('MS_asobi_visibility_group_tool_window',q=True,ex=True):
		cmds.deleteUI('MS_asobi_visibility_group_tool_window')
	cmds.window('MS_asobi_visibility_group_tool_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_asobi_visibility_group_tool_window')
	