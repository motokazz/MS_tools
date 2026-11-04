import maya.cmds as cmds

def cc4_bone_rename():
	sel = cmds.ls(typ='joint')
	for obj in sel:
		if 'RL_BoneRoot' in obj:
			cmds.rename(obj, 'root')
			continue

		cmds.rename(obj, obj.replace('CC_Base_', '').lower())

def cc4_dag_rename():
	sel = cmds.ls(typ='transform')
	for obj in sel:
		if 'RL_BoneRoot' in obj:
			cmds.rename(obj, 'root')
			continue
		try:
			cmds.rename(obj, obj.replace('CC_Base_', '').lower())
		except:
			pass