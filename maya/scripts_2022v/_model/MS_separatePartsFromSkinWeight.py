# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_separatePartsFromSkinWeight
# 説明
#
# 作成日
#
########################################


import maya.cmds as cmds

import _lib.UI.nodeList as nodeList
import MS_primitives.MS_resetPivot as MS_resetPivot

###
# Util
###

def dupComp(COMP=[]):
    face = cmds.polyListComponentConversion(COMP, tf=True)
    OBJ = face[0].split('.')[0]
    DUPED = cmds.duplicate(OBJ)
    unlockAttr(DUPED)
    ncomp = []
    for i in face:
        a, b = i.split('.')
        ncomp.append(DUPED[0] + '.' + b)

    cmds.select(DUPED[0] + '.f[*]', r=True)
    cmds.select(ncomp, tgl=True)
    temptrn = cmds.xform(ncomp, q=True, t=True, ws=True)
    cmds.delete()
    cmds.select(DUPED, r=True)
    return DUPED


def unlockAttr(objs=[]):
    attrs = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'visibility']
    for each in objs:
        for eachattr in attrs:
            cmds.setAttr(each + '.' + eachattr, l=False)




###
# Main
###
def SkinPercentFilter(Joints=[],Components = [],Threshould=0.5):
    RET=[]
    VTXS=cmds.filterExpand(Components , sm=31,ex=True)

    for Joint in Joints:
        for VTX in VTXS:
            var = cmds.skinPercent( 'skinCluster1',VTX,query=True ,transform=Joint,v=True)
            if var > Threshould:
                RET.append(VTX)

    return RET


def main():
    SEL = cmds.ls(sl=True,type='joint')
    MESH = nodeList.nodeList('MS_separatePartsFromSkinWeight_nodelList',q=True)

    THRESHOULD = cmds.floatField('MS_separatePartsFromSkinWeight_threshould',q=True,v=True)

    cmds.select(MESH,r=True)
    cmds.skinCluster(e=True, siv=SEL)
    VTX = cmds.filterExpand(sm=31, ex=True)

    VTX = SkinPercentFilter(SEL,VTX,THRESHOULD)

    if not VTX:
        return

    new = dupComp(VTX)

    #Pivot Reset
    Parent = cmds.listRelatives(new,p=True)
    ParentTranslate = cmds.xform( Parent , q=True, t=True, ws=True)
    cmds.xform( new , ws = True, piv = ParentTranslate)
    cmds.makeIdentity(new,a=True, t=True, r=True, s=True)

    #parenting
    new = cmds.parent(new, SEL[0])

    #rename
    cmds.rename(new,SEL[0].split('|')[-1]+'_mesh')


###
# UI
###

def LayoutA(
        LABEL='MS_separatePartsFromSkinWeight'
        , WIDTH=217
        , BGC=[0.2, 0.2, 0.2]
        , CL=False
    ):
    cmds.frameLayout(LABEL + '_frameLayout', w=WIDTH, bgc=BGC, fn='boldLabelFont', l=LABEL, cll=True, cl=CL)

    cmds.columnLayout()  # column1

    cmds.separator()
    nodeList.nodeList('MS_separatePartsFromSkinWeight_nodelList')
    cmds.separator()

    cmds.floatField('MS_separatePartsFromSkinWeight_threshould',v=0.5)

    cmds.button(label='exec', c=lambda *args: main())

    cmds.setParent('..')  # column1

    cmds.setParent('..')


def UI():
    if cmds.window('MS_separatePartsFromSkinWeight_window', q=True, ex=True):
        cmds.deleteUI('MS_separatePartsFromSkinWeight_window')
    cmds.window('MS_separatePartsFromSkinWeight_window', rtf=True, s=True)

    LayoutA()

    cmds.showWindow('MS_separatePartsFromSkinWeight_window')
