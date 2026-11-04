# _*_coding:utf-8_*_
########################################
# ファイル名
#			MP_MS_checkDestruction
# 説明
#			
# 作成日\n#			
########################################

import maya.cmds as cmds
import os
	
##### ファイルセーブ #####
def SAVE(ROW,FILE_PATH):
	f=open(FILE_PATH,'w')#'r'読み込み：'w'書き込み：'a'追記：'+'読み書き両方' 't'テキストモード：'b'バイナリーモード
	f.write(ROW)
	f.close()
	
def dirList():
	list=[
		'0000'
		,'8000'
		,'8100'
		,'8200'
		,'8300'
		,'8400'
		,'8500'
		,'8600'
		,'8700'
		,'8800'
		,'8900'
		,'9000'
		,'9100'
		,'9200'
		,'9400'
		,'9600'
		,'9800'
		,'9900'
	]
	return list

def check_obj():
	ret=[]
	if cmds.objExists('gp_obj'):
		ret.append('ok')
	else:
		ret.append('x')
	
	if cmds.objExists('gp_brk'):
		ret.append('ok')
	else:
		ret.append('x')
	
	if cmds.objExists('gp_col'):
		ret.append('ok')
	else:
		ret.append('x')
	
	if cmds.objExists('gp_deb'):
		ret.append('ok')
	else:
		ret.append('x')
	
	if cmds.objExists('gp_brk'):
		if cmds.objExists('gp_obj'):
			ret.append('ok')
		else:
			ret.append('invailed')
	else:
		ret.append('none')
	
	return ','.join(ret)
	
	
	
def do():
	dirs=dirList()
	
	for dir in dirs:
		result=[]
		files=os.listdir('D:/Mproject/graphic/fg/character/gimmick/'+dir)
		for each in files:
			path='D:/Mproject/graphic/fg/character/gimmick/'+dir+'/'+each+'/'+each+'_model.mb'
			print path
			if os.path.exists(path):
				cmds.file(path,f=True,options='v=0',type='mayaBinary',ignoreVersion=True,o=True)
				result.append(each+',ok,'+check_obj())
			else:
				result.append(each+',notFound')
		ROW='name,gp_obj,gp_brk,gp_col,gp_deb,destruction\n'+'\n'.join(result)
		SAVE(ROW,'d:/objcheck'+dir+'.csv')
	
	
	
	
def layoutA(
	LABEL='MP_MS_checkDestruction'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	
	cmds.text(l=LABEL)
	cmds.button(w=WIDTH-4,bgc=[0.6,0.8,0.6],l=u'checkDestruction',c=lambda *args:do())
	
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MP_MS_checkDestruction_main_window',q=True,ex=True):
		cmds.deleteUI('MP_MS_checkDestruction_main_window')
	cmds.window('MP_MS_checkDestruction_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MP_MS_checkDestruction_main_window')
	

