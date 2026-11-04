# _*_coding:utf-8_*_
########################################
# ファイル名
#            MS_checkInstance.py
# 説明
#            
#            
# 作成日
#            
########################################

import maya.cmds as cmds

#execCheckList
import s2000_tools.MS_lib.MSG2_execCheck as MSG2_execCheck
reload(MSG2_execCheck)

def unique2(LIST):
    #リストから重複要素を取り除く。リストの並びは要素の登場順になる。
    RET=[]
    for EACH in LIST:
        if not EACH in RET:
            RET.append(EACH)
    return RET

#【シーン内インスタンスリストの取得】
def checkInstance(Transform=[]):
    MSG2_execCheck.execCheckSafe('MS_checkInstance')#execCheckList

    Ret=[]

    if not Transform:#ノード選択・指定なし、シーン内のインスタンス全選択
        Shapes = cmds.ls(s=True)
        for each in Shapes:
            AP = cmds.listRelatives(each,ap=True)
            if len(AP)>1:
                Ret.extend(AP)

    else:#指定ノードのインスタンス使用状況を取得
        print Transform
        for each in Transform:
            Shape = cmds.listRelatives(each,s=True)
            uShape=unique2(Shape)
            for eachShape in uShape:
                AP = cmds.listRelatives(eachShape,ap=True)
                if len(AP)>1:
                    Ret.extend(AP)
    return Ret

def selectInstance():
    Transform = cmds.ls(sl=True,tr=True)
    Instanced = checkInstance(Transform)
    cmds.select(Instanced,r=True)

def selectAnotherInstance():
    Transform = cmds.ls(sl=True,tr=True)
    if not Transform:
        return
    Instanced = checkInstance(Transform)
    cmds.select(Instanced,r=True)
    cmds.select(Transform,d=True)

def LayoutA():
    cmds.columnLayout('MS_tools_mainLayout',adj=True)
    cmds.separator()
    cmds.text(l='Select Instance',bgc=[0.9,0.9,0.9],fn='boldLabelFont')
    cmds.button(l='selectInstance',c=lambda *args:selectInstance())
    cmds.button(l='selectAnotherInstance',c=lambda *args:selectAnotherInstance())
    cmds.separator()
    cmds.setParent('..')
    
def UI():
    if cmds.window('MS_tools_window',q=True,ex=True):
        cmds.deleteUI('MS_tools_window')
    cmds.window('MS_tools_window',rtf=True,s=True)
    
    LayoutA()
    
    cmds.showWindow('MS_tools_window')
    