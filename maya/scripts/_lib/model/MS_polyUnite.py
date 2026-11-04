import maya.cmds as cmds

def MS_polyUnite():
	obj_name=cmds.ls(sl=True)
	obj_parent=cmds.listRelatives(obj_name[0],p=True)
	full_path=cmds.ls(obj_parent,l=True)
	cmds.polyUnite(obj_name,ch=0, n="MS_polyUnite_XXXX")
	
	"""
	for name in obj_name:
		if(cmds.objExists (name)):
			cmds.delete (name)
	"""
	if len(obj_name)>0:
		cmds.parent ("MS_polyUnite_XXXX",full_path[0])
	print obj_name[0]
	cmds.rename ("MS_polyUnite_XXXX",obj_name[0].split('|')[0])

MSPY_polyUnite()

