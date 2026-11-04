# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_listAtgi_locations.py
# 説明
#			
#			
# 作成日
#			
########################################

import maya.cmds as cmds
import subprocess

def copyClipboard( text ):
	try:
		p = subprocess.Popen( ['clip'], stdin=subprocess.PIPE, shell=True )
		p.stdin.write( text )
		p.stdin.close()
 
		retcode = p.wait()
		return True
	except Exception, inst:
		return False

def main():
	i=0
	STR='id\tep\ttrn\tatginame\ttx\tty\ttz\trx\try\trz\n'
	SEL = cmds.ls(sl=True,dag=True,s=True,l=True,type='GraviteAtgiLocatorNode')

	for each in SEL:
		TRF=cmds.listRelatives(each,p=True,f=True)[0]
		TR=TRF.split('|')[-1]
		TRP=TRF.split('|')[1]
		XFT=cmds.xform(TRF,q=True,t=True,ws=True)
		XFR=cmds.xform(TRF,q=True,ro=True,ws=True)

		try:
			ATGINAME=cmds.getAttr(each+'.atgiFilename').split('/')[-1].split('\\')[-1]
		except:
			ATGINAME='none'

		STR+=('%04d'%i)+'\t'+TRP+'\t'+TR+'\t'+ATGINAME+'\t'+str(round(XFT[0],6))+'\t'+str(round(XFT[1],6))+'\t'+str(round(XFT[2],6))+'\t'+str(round(XFR[0],6))+'\t'+str(round(XFR[1],6))+'\t'+str(round(XFR[2],6))+'\n'

		i+=1

	copyClipboard(STR)

def LayoutA():
	cmds.columnLayout('MSG2_listAtgi_locations.py_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MSG2_listAtgi_locations.py',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
	cmds.button(l='do',c=lambda *args:main())
	cmds.separator()
	cmds.setParent('..')

def UI():
	if cmds.window('MS_tools_window',q=True,ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_tools_window')
	
UI()