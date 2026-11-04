# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_gammaCalc
# 説明
#			
# 作成日\n#			
########################################

import maya.cmds as cmds
	
def do():
	a=cmds.intField('MS_gammaCalc_intField_a',q=True,v=True)
	
	ans=(float(a)/255.0)**2.2
	cmds.text('MS_gammaCalc_answer_a',e=True,l=str(ans))
	
	counterColor=((1.0-ans)**0.4545)*255
	cmds.text('MS_gammaCalc_answer_b',e=True,l=str(counterColor))
	
	counterColorB=((0.86-ans)**0.4545)*255
	cmds.text('MS_gammaCalc_answer_c',e=True,l=str(counterColorB))
	
	
def layoutA(
	LABEL='MS_gammaCalc'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	
	cmds.text(l=LABEL)
	cmds.intField(LABEL+'_intField_a',w=WIDTH-4,v=0,cc=lambda *args:do())
	#cmds.intField(LABEL+'_intField_b',w=WIDTH-4,v=0)
	#cmds.button(w=WIDTH-4,l=u'do',c=lambda *args:do())
	cmds.text(l='RGBGamma')
	cmds.text('MS_gammaCalc_answer_a',l='answer')
	
	cmds.text(l='1.0counterColor(RGB)')
	cmds.text('MS_gammaCalc_answer_b',l='1.0counterColor(RGB)')

	cmds.text(l='0.86counterColor(RGB)')
	cmds.text('MS_gammaCalc_answer_c',l='0.86counterColor(RGB)')
	
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_gammaCalc_main_window',q=True,ex=True):
		cmds.deleteUI('MS_gammaCalc_main_window')
	cmds.window('MS_gammaCalc_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MS_gammaCalc_main_window')
	

