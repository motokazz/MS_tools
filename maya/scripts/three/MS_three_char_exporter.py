# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_three_char_exporter.py
# 説明
#
#
# 作成日
#
########################################

import maya.cmds as cmds
import maya.mel as mel
import sys
import shutil
import os
import subprocess

import MS_three_char_checker

reload(MS_three_char_checker)

######################################
# define
######################################
unitypath = 'D:/three-app-client/UnityProject/Assets/RawData/Characters/'
PSD2TGA_droplet_path = 'D:/MS_tools/photoshop/droplets/TGA24bit.exe'


######################################
# class
######################################
class CharPath:
    def __init__(self):
        # name
        self.id = ''
        self.variation = ''
        self.name = ''

        # model names
        self.modelName_Head = ''
        self.modelName_Body = ''
        self.modelName_Leg = ''
        self.modelName_Foot = ''
        self.modelName_Enemy = ''
        self.modelName_Icon_Head = ''
        self.modelName_Icon_Body = ''
        self.modelName_Icon_Leg = ''
        self.modelName_Icon_Foot = ''

        # material names
        self.materialName_Head = ''
        self.materialName_Body = ''
        self.materialName_Leg = ''
        self.materialName_Foot = ''

        # texture node names
        self.textureNodeName_Head = ''
        self.textureNodeName_Body = ''
        self.textureNodeName_Leg = ''
        self.textureNodeName_Foot = ''

        # mainPath
        self.unityModelsPath = ''
        self.artMAYAPath = ''
        self.artMAPath = ''
        self.artFBXPath = ''

        # artFBX
        self.artFBXPath_Head = ''
        self.artFBXPath_Body = ''
        self.artFBXPath_Leg = ''
        self.artFBXPath_Foot = ''
        self.artFBXPath_Enemy = ''
        self.artFBXPath_Icon_Head = ''
        self.artFBXPath_Icon_Body = ''
        self.artFBXPath_Icon_Leg = ''
        self.artFBXPath_Icon_Foot = ''

        # unityFBX
        self.unityFBXPath_Head = ''
        self.unityFBXPath_Body = ''
        self.unityFBXPath_Leg = ''
        self.unityFBXPath_Foot = ''
        self.unityFBXPath_Enemy = ''
        self.unityFBXPath_Icon_Head = ''
        self.unityFBXPath_Icon_Body = ''
        self.unityFBXPath_Icon_Leg = ''
        self.unityFBXPath_Icon_Foot = ''

        # Textures
        self.artTGAPath = ''
        self.artPSDPath = ''
        self.unityTexturesPath = ''

        self.artPSDPath_Head = ''
        self.artPSDPath_Body = ''
        self.artPSDPath_Leg = ''
        self.artPSDPath_Foot = ''

        self.artTGAPath_Head = ''
        self.artTGAPath_Body = ''
        self.artTGAPath_Leg = ''
        self.artTGAPath_Foot = ''

        self.unityTexturesPath_Head = ''
        self.unityTexturesPath_Body = ''
        self.unityTexturesPath_Leg = ''
        self.unityTexturesPath_Foot = ''

    def getPath(self):
        temp = cmds.file(q=True, sn=True)

        # char ID
        self.id = temp.split('/')[-3].split('_')[1]
        self.variation = temp.split('/')[-1].split('_')[-2]
        self.name = temp.split('/')[-3].split('_')[-1]

        # main path
        self.artMAYAPath = '/'.join(temp.split('/')[0:-2])
        self.artMAPath = self.artMAYAPath + '/scenes/'
        self.artFBXPath = self.artMAYAPath + '/FBX/'

        # model names
        self.modelName_Head = 'head_' + self.id + '_' + self.name
        self.modelName_Body = 'body_' + self.id + '_' + self.name
        self.modelName_Leg = 'leg_' + self.id + '_' + self.name
        self.modelName_Foot = 'foot_' + self.id + '_' + self.name
        self.modelName_Enemy = 'en_' + self.id + '_' + self.name
        self.modelName_Icon_Head = 'head_' + self.id + '_' + self.name
        self.modelName_Icon_Body = 'body_' + self.id + '_' + self.name
        self.modelName_Icon_Leg = 'leg_' + self.id + '_' + self.name
        self.modelName_Icon_Foot = 'foot_' + self.id + '_' + self.name

        # material names
        self.materialName_Head = 'mat_head_' + self.id + '_' + self.variation + '_' + self.name
        self.materialName_Body = 'mat_body_' + self.id + '_' + self.variation + '_' + self.name
        self.materialName_Leg = 'mat_leg_' + self.id + '_' + self.variation + '_' + self.name
        self.materialName_Foot = 'mat_foot_' + self.id + '_' + self.variation + '_' + self.name

        # texture node names
        self.textureNodeName_Head = 'tex_head_' + self.id + '_' + self.variation + '_' + self.name
        self.textureNodeName_Body = 'tex_body_' + self.id + '_' + self.variation + '_' + self.name
        self.textureNodeName_Leg = 'tex_leg_' + self.id + '_' + self.variation + '_' + self.name
        self.textureNodeName_Foot = 'tex_foot_' + self.id + '_' + self.variation + '_' + self.name

        # artFBX
        self.artFBXPath_Head = self.artFBXPath + 'head_' + self.id + '_' + self.variation + '_' + self.name + '.fbx'
        self.artFBXPath_Body = self.artFBXPath + 'body_' + self.id + '_' + self.variation + '_' + self.name + '.fbx'
        self.artFBXPath_Leg = self.artFBXPath + 'leg_' + self.id + '_' + self.variation + '_' + self.name + '.fbx'
        self.artFBXPath_Foot = self.artFBXPath + 'foot_' + self.id + '_' + self.variation + '_' + self.name + '.fbx'
        self.artFBXPath_Enemy = self.artFBXPath + 'en_' + self.id + '_' + self.variation + '_' + self.name + '.fbx'
        self.artFBXPath_Icon_Head = self.artFBXPath + 'icon_head_' + self.id + '_' + self.variation + '_' + self.name + '.fbx'
        self.artFBXPath_Icon_Body = self.artFBXPath + 'icon_body_' + self.id + '_' + self.variation + '_' + self.name + '.fbx'
        self.artFBXPath_Icon_Leg = self.artFBXPath + 'icon_leg_' + self.id + '_' + self.variation + '_' + self.name + '.fbx'
        self.artFBXPath_Icon_Foot = self.artFBXPath + 'icon_foot_' + self.id + '_' + self.variation + '_' + self.name + '.fbx'

        # unityFBX
        self.unityFBXPath_Head = unitypath + 'Models/Head/' + 'head_' + self.id + '_' + self.variation + '_' + self.name + '.fbx'
        self.unityFBXPath_Body = unitypath + 'Models/Body/' + 'body_' + self.id + '_' + self.variation + '_' + self.name + '.fbx'
        self.unityFBXPath_Leg = unitypath + 'Models/Leg/' + 'leg_' + self.id + '_' + self.variation + '_' + self.name + '.fbx'
        self.unityFBXPath_Foot = unitypath + 'Models/Foot/' + 'foot_' + self.id + '_' + self.variation + '_' + self.name + '.fbx'
        self.unityFBXPath_Enemy = unitypath + 'Models/Enemy/' + 'en_' + self.id + '_' + self.variation + '_' + self.name + '.fbx'
        self.unityFBXPath_Icon_Head = unitypath + 'Models/Icon/' + 'icon_head_' + self.id + '_' + self.variation + '_' + self.name + '.fbx'
        self.unityFBXPath_Icon_Body = unitypath + 'Models/Icon/' + 'icon_body_' + self.id + '_' + self.variation + '_' + self.name + '.fbx'
        self.unityFBXPath_Icon_Leg = unitypath + 'Models/Icon/' + 'icon_leg_' + self.id + '_' + self.variation + '_' + self.name + '.fbx'
        self.unityFBXPath_Icon_Foot = unitypath + 'Models/Icon/' + 'icon_foot_' + self.id + '_' + self.variation + '_' + self.name + '.fbx'

        # Textures
        self.artTGAPath = self.artMAYAPath + '/sourceimages/'
        self.artPSDPath = self.artMAYAPath + '/sourceimages/PSD/'

        self.artPSDPath_Head = self.artPSDPath + 'tex_head_' + self.id + '_' + self.variation + '_' + self.name + '.psd'
        self.artPSDPath_Body = self.artPSDPath + 'tex_body_' + self.id + '_' + self.variation + '_' + self.name + '.psd'
        self.artPSDPath_Leg = self.artPSDPath + 'tex_leg_' + self.id + '_' + self.variation + '_' + self.name + '.psd'
        self.artPSDPath_Foot = self.artPSDPath + 'tex_foot_' + self.id + '_' + self.variation + '_' + self.name + '.psd'

        self.artTGAPath_Head = self.artTGAPath + 'tex_head_' + self.id + '_' + self.variation + '_' + self.name + '.tga'
        self.artTGAPath_Body = self.artTGAPath + 'tex_body_' + self.id + '_' + self.variation + '_' + self.name + '.tga'
        self.artTGAPath_Leg = self.artTGAPath + 'tex_leg_' + self.id + '_' + self.variation + '_' + self.name + '.tga'
        self.artTGAPath_Foot = self.artTGAPath + 'tex_foot_' + self.id + '_' + self.variation + '_' + self.name + '.tga'

        #
        self.unityTexturesPath = unitypath + 'Textures/' + self.id + '_' + self.name + '/'

        self.unityTexturesPath_Head = self.unityTexturesPath + 'tex_head_' + self.id + '_' + self.variation + '_' + self.name + '.tga'
        self.unityTexturesPath_Body = self.unityTexturesPath + 'tex_body_' + self.id + '_' + self.variation + '_' + self.name + '.tga'
        self.unityTexturesPath_Leg = self.unityTexturesPath + 'tex_leg_' + self.id + '_' + self.variation + '_' + self.name + '.tga'
        self.unityTexturesPath_Foot = self.unityTexturesPath + 'tex_foot_' + self.id + '_' + self.variation + '_' + self.name + '.tga'


######################################
# main
######################################
def main(parts):
    def check_select(model_name, root_select=True, goto_bind_pose=True):
        # Model Check & Selection
        if cmds.objExists(model_name):
            cmds.select(model_name, r=True)
        else:
            cmds.confirmDialog(m='Object not found.')
            sys.exit()

        # delete non deformer history
        mel.eval('doBakeNonDefHistory( 1, {"prePost" });')

        # goto bind pose
        if goto_bind_pose:
            mel.eval("gotoBindPose;")

        # root bone check
        if root_select:
            if cmds.objExists('|root'):
                cmds.select('|root', add=True)
            else:
                cmds.confirmDialog(m='Object not found.')
                sys.exit()

    cp = CharPath()
    cp.getPath()

    #########
    # Parts
    #########
    if parts == 'head':
        check_select(cp.modelName_Head, root_select=True, goto_bind_pose=True)
        export_fbx(cp.modelName_Head, cp.artFBXPath_Head, cp.unityFBXPath_Head)
        return
    if parts == 'body':
        check_select(cp.modelName_Body, root_select=True, goto_bind_pose=True)
        export_fbx(cp.modelName_Body, cp.artFBXPath_Body, cp.unityFBXPath_Body)
        return
    if parts == 'leg':
        check_select(cp.modelName_Leg, root_select=True, goto_bind_pose=True)
        export_fbx(cp.modelName_Leg, cp.artFBXPath_Leg, cp.unityFBXPath_Leg)
        return
    if parts == 'foot':
        check_select(cp.modelName_Foot, root_select=True, goto_bind_pose=True)
        export_fbx(cp.modelName_Foot, cp.artFBXPath_Foot, cp.unityFBXPath_Foot)
        return

    #########
    # Enemy
    #########
    if parts == 'en':
        mel.eval("gotoBindPose;")
        check_select(cp.modelName_Enemy, root_select=True, goto_bind_pose=True)
        export_fbx(cp.modelName_Enemy, cp.artFBXPath_Enemy, cp.unityFBXPath_Enemy)
        return

    #########
    # Icon
    #########
    if parts == 'icon_head':
        check_select(cp.modelName_Icon_Head, root_select=False, goto_bind_pose=False)
        export_fbx(cp.modelName_Icon_Head, cp.artFBXPath_Icon_Head, cp.unityFBXPath_Icon_Head)
        return
    if parts == 'icon_body':
        # pose creation
        try:
            cmds.setAttr('RightArm.rotateZ', -35)
            cmds.setAttr('LeftArm.rotateZ', -35)
            cmds.setAttr('RightShoulder.rotateZ', -10)
            cmds.setAttr('LeftShoulder.rotateZ', -10)
        except:
            pass
        #
        check_select(cp.modelName_Icon_Body, root_select=False, goto_bind_pose=False)
        export_fbx(cp.modelName_Icon_Body, cp.artFBXPath_Icon_Body, cp.unityFBXPath_Icon_Body)
        return
    if parts == 'icon_leg':
        check_select(cp.modelName_Icon_Leg, root_select=False, goto_bind_pose=False)
        export_fbx(cp.modelName_Icon_Leg, cp.artFBXPath_Icon_Leg, cp.unityFBXPath_Icon_Leg)
        return
    if parts == 'icon_foot':
        check_select(cp.modelName_Icon_Foot, root_select=False, goto_bind_pose=False)
        export_fbx(cp.modelName_Icon_Foot, cp.artFBXPath_Icon_Foot, cp.unityFBXPath_Icon_Foot)
        return

    ###########
    # Texture
    ###########

    # 新規の場合テクスチャフォルダが無いので作る必要あり
    if not os.path.exists(cp.unityTexturesPath):
        con = cmds.confirmDialog(t='Confirm', m=u'キャラクターテクスチャ用フォルダがありません。\n フォルダを作成しますか？',
                                 button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
        if con == 'Yes':
            os.mkdir(cp.unityTexturesPath)
        else:
            cmds.confirmDialog(t='Confirm', m=u'フォルダを作成しませんでした\n処理を中断します。')
            return

    if parts == 'texture_head':
        export_textures(cp.artPSDPath_Head, cp.artTGAPath_Head, cp.unityTexturesPath_Head)
        return
    if parts == 'texture_body':
        export_textures(cp.artPSDPath_Body, cp.artTGAPath_Body, cp.unityTexturesPath_Body)
        return
    if parts == 'texture_leg':
        export_textures(cp.artPSDPath_Leg, cp.artTGAPath_Leg, cp.unityTexturesPath_Leg)
        return
    if parts == 'texture_foot':
        export_textures(cp.artPSDPath_Foot, cp.artTGAPath_Foot, cp.unityTexturesPath_Foot)
        return


def export_fbx(model_name, artFBXPath, unityFBXPath):
    # FBX Export
    cmds.file(artFBXPath, force=True, options='v=0;', typ='FBX export', pr=True, es=True)
    shutil.copy2(artFBXPath, unityFBXPath)


def export_textures(artPSDPath, artTGAPath, unityTexturesPath):
    ######################################
    # Texture Convert by Photoshop Droplet
    ######################################

    if not os.path.exists(PSD2TGA_droplet_path):
        cmds.confirmDialog(t='confirm', m='Photoshop droplet not found.')
        return

    if not os.path.exists(artPSDPath):
        cmds.confirmDialog(t='confirm', m='PSD file not found.')
        return

    # ドロップレット実行
    command = '%s %s' % (PSD2TGA_droplet_path.replace('/', '\\'), artPSDPath.replace('/', '\\'))
    cmdline(command)

    ######################################
    # Texture Convert & Copy
    ######################################
    tempTGAPath = artPSDPath.replace('.psd', '.tga')
    shutil.copy2(tempTGAPath, artTGAPath)
    shutil.copy2(tempTGAPath, unityTexturesPath)
    os.remove(tempTGAPath)


def finalize_texture_path(mode='finalize'):
    cp = CharPath()
    cp.getPath()
    ######################################
    # Check Materials
    ######################################
    materials = cmds.ls(mat=True)
    if 'lambert1' in materials: materials.remove('lambert1')
    if 'particleCloud1' in materials: materials.remove('particleCloud1')
    if cp.materialName_Head in materials: materials.remove(cp.materialName_Head)
    if cp.materialName_Body in materials: materials.remove(cp.materialName_Body)
    if cp.materialName_Leg in materials: materials.remove(cp.materialName_Leg)
    if cp.materialName_Foot in materials: materials.remove(cp.materialName_Foot)
    if len(materials) > 0:
        cmds.confirmDialog(m='invalid materials.\n' + '\n'.join(materials))
        return

    ######################################
    # Check Texture nodes
    ######################################
    textures = cmds.ls(type='file')
    if cp.textureNodeName_Head in textures: textures.remove(cp.textureNodeName_Head)
    if cp.textureNodeName_Body in textures: textures.remove(cp.textureNodeName_Body)
    if cp.textureNodeName_Leg in textures: textures.remove(cp.textureNodeName_Leg)
    if cp.textureNodeName_Foot in textures: textures.remove(cp.textureNodeName_Foot)
    if len(textures) > 0:
        cmds.confirmDialog(m='invalid texture nodes.\n' + '\n'.join(textures))
        return

    ######################################
    # Check Texture pathes
    ######################################
    invalid_texture_path = 0
    message_texture_pathes = []
    if not cmds.getAttr(cp.textureNodeName_Head + '.fileTex tureName') == cp.artTGAPath_Head and not cmds.getAttr(
            cp.textureNodeName_Head + '.fileTextureName') == cp.artPSDPath_Head:
        invalid_texture_path += 1
        message_texture_pathes.append('texture path invalid : %s' % cp.textureNodeName_Head)
    if not cmds.getAttr(cp.textureNodeName_Body + '.fileTextureName') == cp.artTGAPath_Body and not cmds.getAttr(
            cp.textureNodeName_Body + '.fileTextureName') == cp.artPSDPath_Body:
        invalid_texture_path += 1
        message_texture_pathes.append('texture path invalid : %s' % cp.textureNodeName_Body)
    if not cmds.getAttr(cp.textureNodeName_Leg + '.fileTextureName') == cp.artTGAPath_Leg and not cmds.getAttr(
            cp.textureNodeName_Leg + '.fileTextureName') == cp.artPSDPath_Leg:
        invalid_texture_path += 1
        message_texture_pathes.append('texture path invalid : %s' % cp.textureNodeName_Leg)
    if not cmds.getAttr(cp.textureNodeName_Foot + '.fileTextureName') == cp.artTGAPath_Foot and not cmds.getAttr(
            cp.textureNodeName_Foot + '.fileTextureName') == cp.artPSDPath_Foot:
        invalid_texture_path += 1
        message_texture_pathes.append('texture path invalid : %s' % cp.textureNodeName_Foot)
    if invalid_texture_path > 0:
        cmds.confirmDialog(m='invalid texture nodes.\n' + '\n'.join(message_texture_pathes))
        return

    ######################################
    # Set Texture pathes
    ######################################

    if mode == 'finalize':
        if cmds.objExists(cp.textureNodeName_Head):
            cmds.setAttr(cp.textureNodeName_Head + '.fileTextureName', cp.artTGAPath_Head, type='string')
        if cmds.objExists(cp.textureNodeName_Body):
            cmds.setAttr(cp.textureNodeName_Body + '.fileTextureName', cp.artTGAPath_Body, type='string')
        if cmds.objExists(cp.textureNodeName_Leg):
            cmds.setAttr(cp.textureNodeName_Leg + '.fileTextureName', cp.artTGAPath_Leg, type='string')
        if cmds.objExists(cp.textureNodeName_Foot):
            cmds.setAttr(cp.textureNodeName_Foot + '.fileTextureName', cp.artTGAPath_Foot, type='string')

    if mode == 'work':
        if cmds.objExists(cp.textureNodeName_Head):
            cmds.setAttr(cp.textureNodeName_Head + '.fileTextureName', cp.artPSDPath_Head, type='string')
        if cmds.objExists(cp.textureNodeName_Body):
            cmds.setAttr(cp.textureNodeName_Body + '.fileTextureName', cp.artPSDPath_Body, type='string')
        if cmds.objExists(cp.textureNodeName_Leg):
            cmds.setAttr(cp.textureNodeName_Leg + '.fileTextureName', cp.artPSDPath_Leg, type='string')
        if cmds.objExists(cp.textureNodeName_Foot):
            cmds.setAttr(cp.textureNodeName_Foot + '.fileTextureName', cp.artPSDPath_Foot, type='string')


######################################
# commandline
######################################
def cmdline(cmdline):
    logtex = []
    p = subprocess.Popen(cmdline, shell=True, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                         )
    (stdouterr, stdin) = (p.stdout, p.stdin)  #
    while True:
        line = stdouterr.readline()  # 改行を含んで行を読み込む
        if not line:
            break
        logtex.append(line.rstrip())  # 後ろの改行を消して出力
    ret = p.wait()  # 戻り値が入る
    return logtex


######################################
# UI
######################################
def LayoutA():
    cmds.columnLayout('MS_three_char_exporter_mainLayout', adj=True)
    cmds.separator()
    cmds.rowLayout(nc=2)
    cmds.text('variation')
    # cmds.intField('MS_three_char_exporter_variation', v=1)
    cmds.setParent('..')
    cmds.text(l='MS_three_char_exporter', bgc=[0.9, 0.9, 0.9], fn='boldLabelFont')
    cmds.button(l='head', c=lambda *args: main('head'))
    cmds.button(l='body', c=lambda *args: main('body'))
    cmds.button(l='leg', c=lambda *args: main('leg'))
    cmds.button(l='foot', c=lambda *args: main('foot'))
    cmds.separator()

    cmds.button(l='enemy', c=lambda *args: main('en'))
    cmds.separator()

    cmds.button(l='icon_head', c=lambda *args: main('icon_head'))
    cmds.button(l='icon_body', c=lambda *args: main('icon_body'))
    cmds.button(l='icon_leg', c=lambda *args: main('icon_leg'))
    cmds.button(l='icon_foot', c=lambda *args: main('icon_foot'))
    cmds.separator()

    cmds.button(l='texture_head', c=lambda *args: main('texture_head'))
    cmds.button(l='texture_body', c=lambda *args: main('texture_body'))
    cmds.button(l='texture_leg', c=lambda *args: main('texture_leg'))
    cmds.button(l='texture_foot', c=lambda *args: main('texture_foot'))

    cmds.separator()
    cmds.button(l='regulations', c=lambda *args: MS_three_char_checker.show_regulation())

    cmds.separator()
    cmds.button(l='finalize texture path', c=lambda *args: finalize_texture_path())
    cmds.button(l='work texture path', c=lambda *args: finalize_texture_path('work'))

    cmds.setParent('..')


def UI():
    if cmds.window('MS_three_char_exporter_window', q=True, ex=True):
        cmds.deleteUI('MS_three_char_exporter_window')
    cmds.window('MS_three_char_exporter_window', rtf=True, s=True)

    LayoutA()

    cmds.showWindow('MS_three_char_exporter_window')
