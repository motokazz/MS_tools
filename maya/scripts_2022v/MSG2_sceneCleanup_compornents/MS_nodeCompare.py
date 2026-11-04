# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_nodeCompare
# 説明
#			二つの選択ノードアトリビュートの差を比較します
# 作成日\n#			
########################################

import maya.cmds as cmds

def compare(node_a,node_b):
	#type
	type_a=cmds.nodeType(node_a)
	type_b=cmds.nodeType(node_b)
	if not type_a==type_b:
		return 'both type is different:'+type_a+','+type_b
	#attr
	ret=''
	line=cmds.listAttr(node_a,se=True)
	for each in line:
		try:
			var_a=cmds.getAttr(node_a+'.'+each)
			if not cmds.attributeQuery(each,n=node_b,ex=True):
				ret+=node_b+' has no attribute : '+each
				continue
			var_b=cmds.getAttr(node_b+'.'+each)
			if not var_a==var_b:
				ret+='*different:'+each+'\n'
		except:
			continue
	if ret:
		return ret
	else:
		return True
	
	
	
	
