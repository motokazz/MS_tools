# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_rigger
# 説明
#			rig
#			
# 作成日
#			
########################################

import maya.cmds as cmds


# UI

def layoutA():
    cmds.frameLayout('MS_rigger_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l=u'MS_rigger',cll=True,cl=False)
    cmds.columnLayout()

    cmds.button(w=150,l=u'ROOT',c=lambda *args:Root())
    cmds.button(w=150,l=u'HIP',c=lambda *args:Hip())
    cmds.button(w=150,l=u'Spine_a',c=lambda *args:Spine_a()) 
    cmds.button(w=150,l=u'LEG',c=lambda *args:LEG())
    cmds.button(w=150,l=u'ARM',c=lambda *args:ARM())
    cmds.button(w=150,l=u'HEAD',c= lambda *args:Head())

    cmds.separator(w=150)
    cmds.button(w=150,l=u'work',c=lambda *args:work())
    
    #
    cmds.button(w=150,l=u'releaseTramsformLimits',c=lambda *args:releaseTramsformLimits())

    cmds.setParent('..')
    cmds.setParent('..')

def UI():
    if cmds.window('MS_rigger_main_window',q=True,ex=True):
        cmds.deleteUI('MS_rigger_main_window')
    cmds.window('MS_rigger_main_window',rtf=True,s=True)

    layoutA()

    cmds.showWindow('MS_rigger_main_window')

UI()
