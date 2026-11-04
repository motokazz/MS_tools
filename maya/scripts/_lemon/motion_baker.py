# -*- coding: utf-8 -*-
from maya import cmds
def importReference():
    refFiles = cmds.file(q=1,r=1)
    if refFiles:
        for r in refFiles:
            refName = cmds.file(r,q=1,rfn=1)
            cmds.file(r,ir=1)
def delNamespace():
    cmds.namespace(setNamespace=':')
    for ns in reversed(cmds.namespaceInfo(listOnlyNamespaces=True, recurse=True)):
        if ns != 'UI' and ns != 'shared':
            cmds.namespace(moveNamespace=(ns, ':'), force=True)
            cmds.namespace(removeNamespace=ns)
def bakeAnimation():
    joints = cmds.ls(type = 'joint')
    targetJoints=[]
    for target in joints:
        if target.find('physics') == -1:
            targetJoints.append(target)
            cmds.setAttr(target + '.tx',keyable=True)
            cmds.setAttr(target + '.ty',keyable=True)
            cmds.setAttr(target + '.tz',keyable=True)
            cmds.setAttr(target + '.rx',keyable=True)
            cmds.setAttr(target + '.ry',keyable=True)
            cmds.setAttr(target + '.rz',keyable=True)
            cmds.setAttr(target + '.sx',keyable=True)
            cmds.setAttr(target + '.sy',keyable=True)
            cmds.setAttr(target + '.sz',keyable=True)
            cmds.setAttr(target + '.visibility',keyable=True)
    min = cmds.playbackOptions(q=True, minTime=True)
    max = cmds.playbackOptions(q=True, maxTime=True)
    cmds.bakeResults(targetJoints, simulation=True, t= (min,max), sampleBy=1, oversamplingRate=1,
        disableImplicitControl=True, preserveOutsideKeys=True, sparseAnimCurveBake=False, removeBakedAttributeFromLayer=False,
        removeBakedAnimFromLayer=False, bakeOnOverrideLayer=False, minimizeRotation=True, controlPoints=False, shape=True
    )
def delTargetJointAnim():
    joints = cmds.ls(type = 'joint')
    targetJoints=[]
    for target in joints:
        if target.find('physics') == -1:continue
        cmds.delete(cmds.listConnections(target,type='animCurve',s=True))

def exec_motion_baker():
    importReference()
    delNamespace()
    bakeAnimation()
    #
    cmds.select('bone_root',r=True)
    cmds.keyTangent( 'bone_root', inTangentType='linear',outTangentType='linear' )
