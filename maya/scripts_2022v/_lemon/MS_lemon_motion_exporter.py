# _*_coding:utf-8_*_
########################################
# ファイル名
#   MS_lemon_motion_exporter
# 説明
#
#
# 作成日
#
########################################

import maya.cmds as cmds
import maya.mel as mel
import os
import importlib

import _lemon.motion_baker as motion_baker
import _lemon.MS_lemon_P4Lib as MS_lemon_P4Lib

importlib.reload(motion_baker)
importlib.reload(MS_lemon_P4Lib)

# Define ####################################

scene_name = ''
# 正規出力パス

ExportPath = 'M:/Assets/LemonArt/Chara/common/anim'

# プリセット名
PresetName = 'Lemon_anim'  # 正しいプリセット名
PresetName_bak = 'New Lemon_anim'  # 古いプリセット名

FBX_version = 'FBX201800'
Valid_Suffix = ['_in', '_loop', '_out']  # 正しいSuffix

# Var ####################
AutoFix = False
GameExporterNodeUsing = ''
message = []
baked = False
AnimClips = []


##################


def check_preset():  # ditect Prest Used

    global GameExporterNodeUsing
    global message

    PresetVailed = False
    # 正規プリセット名存在確認
    for each in GameExporterNodes:
        if cmds.getAttr(each + ".presetName") == PresetName:
            GameExporterNodeUsing = each
            PresetVailed = True
            break

    # 過去に使われていたプリセット名しか無いとき、正規の名前にリネーム
    if not PresetVailed:
        for each in GameExporterNodes:
            if cmds.getAttr(each + ".presetName") == PresetName_bak:
                if AutoFix:
                    cmds.setAttr(each + ".presetName", PresetName, type='string')
                    message.append(u'OK : Preset リネーム　=> ' + PresetName_bak)
                    GameExporterNodeUsing = each
                    PresetVailed = True
                else:
                    message.append(u'NG : 古い名前のPreset = ' + PresetName_bak)
                break

    # PresetCheck
    if PresetVailed:
        message.append('OK : Preset = ' + PresetName)
        return True
    else:
        message.append(u'NG : Presetが無い = ' + PresetName)
        return False


def CheckAnimationClips():  # check AnimationClips
    global message
    global AnimClips

    AllClipsValid = True
    animClipsExist = False

    AnimClips = []
    # アニメーションクリップ取得
    if cmds.getAttr(GameExporterNodeUsing + '.ac', size=True) > 1:  # アニメーションクリップが複数ある
        animClips = cmds.getAttr(GameExporterNodeUsing + '.ac[*].acn')
        animClipsExist = True
        print('multi')
    else:  # アニメーションクリップは一つ
        print('single')
        animClips = [cmds.getAttr(GameExporterNodeUsing + '.ac[0].acn')]
        animClipsExist = True

    if not animClipsExist:
        message.append(u'NG : AnimationClipが無い')
        return False

    # クリップ名チェック
    i = 0
    for each in animClips:
        print('c' + each)
        # check filename & suffix
        ClipName_Valid = False

        #

        if scene_name == each:  # シーン名と一致
            ClipName_Valid = True
        else:

            for each_Valid_Suffix in Valid_Suffix:
                # シーン名と一致、かつ正規のSuffix
                if each == scene_name + each_Valid_Suffix:
                    ClipName_Valid = True
                    break
                # 大文字小文字チェック
                elif each.lower().endswith(each_Valid_Suffix):
                    if AutoFix:
                        cmds.setAttr(GameExporterNodeUsing + '.ac[' + str(i) + '].acn', scene_name + each_Valid_Suffix,
                                    type='string')
                        message.append(u'OK : ClipName 修正\n  ' + each + ' => ' + scene_name + each_Valid_Suffix)
                        ClipName_Valid = True
                        break
                    else:
                        message.append('NG : ClipName = ' + each)

        i += 1
        #

        if ClipName_Valid:
            message.append('OK : clipname = ' + each)
            AnimClips.append(each)
        else:
            AllClipsValid = False
            message.append('NG : clipname = ' + each)

    if AllClipsValid:
        message.append('OK : All Animation Clips')
    else:
        message.append('NG : NG Clip Exist !')
    return AllClipsValid


def CheckVersion():
    global message
    Var = cmds.getAttr(GameExporterNodeUsing + '.fv')
    if Var == FBX_version:
        message.append('OK : FBX_version = ' + FBX_version)
        return True
    elif AutoFix:
        cmds.setAttr(GameExporterNodeUsing + '.fv', FBX_version, type='string')
        message.append('OK : set FBX_version = ' + FBX_version)
        return True
    else:
        message.append('NG : FBX_version = ' + Var)
        return False


def CheckExportPath():
    global message
    Var = cmds.getAttr(GameExporterNodeUsing + '.exportPath')
    if Var == ExportPath:
        message.append('OK : ExportPath = ' + Var)
        return True
    elif AutoFix:
        cmds.setAttr(GameExporterNodeUsing + '.exportPath', ExportPath, type='string')
        message.append('OK : set ExportPath = ' + ExportPath)
        return True
    else:
        message.append('NG : ExportPath = ' + Var)
        return False


def GameFbxExporter():
    if cmds.window('gameExporterWindow', q=True, ex=True):
        cmds.deleteUI('gameExporterWindow')
    mel.eval('gameFbxExporter()')


# exec ##############################################################################################################
def initialize():
    global scene_name
    global GameExporterNodes
    global GameExporterNodeUsing
    global message
    global AnimClips
    scene_name = cmds.file(q=True, sn=True).split('/')[-1].split('.')[0]
    GameExporterNodes = cmds.ls(typ='gameFbxExporter')
    GameExporterNodeUsing = ''
    message = []
    cmds.scrollField('MS_lemon_motion_exporter_log', e=True, cl=True)
    AnimClips = []


def Check_All(
        exec_CheckAnimationClips=True
        , exec_SetupSettings=True
        , exec_motion_baker=False
        , auto_fix=False
):
    #
    global message
    global AutoFix
    #
    AutoFix = auto_fix

    initialize()

    CheckProgress = []
    if check_preset():
        CheckProgress.append(True)
        if exec_CheckAnimationClips:
            CheckProgress.append(CheckAnimationClips())

        if exec_SetupSettings:
            CheckProgress.append(CheckVersion())
            CheckProgress.append(CheckExportPath())
    else:
        CheckProgress.append(False)

    # 全部OK判定
    if False in CheckProgress:
        # 一個でもNGがあったらここで処理を中断########################################
        message.append('xxx All Check NG xxx')
        # cmdss.confirmDialog(m='\n'.join(message))
        cmds.scrollField('MS_lemon_motion_exporter_log', e=True, it='\n'.join(message))
        return False

    else:
        # 全部OK ##############################################################
        message.append('ooo All Check OK ooo')
        cmds.button('MS_lemon_motion_exporter_bakeButton', e=True, en=True, bgc=[0.5, 0.7, 0.5])
        # cmdss.confirmDialog(m='\n'.join(message))
        cmds.scrollField('MS_lemon_motion_exporter_log', e=True, it='\n'.join(message))
        return True


def bake_motion():
    if cmds.file(q=True, modified=True):
        cmds.confirmDialog(m=u'ベイク前にシーンを保存してください')
        return

    global baked
    motion_baker.exec_motion_baker()
    cmds.button('MS_lemon_motion_exporter_bakeButton', e=True, en=False, bgc=[0.4, 0.3, 0.3])
    cmds.button('MS_lemon_motion_exporter_GameFbxExporter', e=True, bgc=[0.5, 0.7, 0.7])


# P4 ##################################################


WALKED_DATA = []


def walked(SEARCH_PATH):
    global WALKED_DATA
    WALKED_DATA = []
    for (root, dir, files) in os.walk(SEARCH_PATH):
        WALKED_DATA.append([root, files])


def searchPath(SEARCH_PATH, SEARCH_FILE='', TARGET_EXT='py'):
    global WALKED_DATA
    for EACH in WALKED_DATA:
        if (SEARCH_FILE + '.' + TARGET_EXT).lower() in list(map(str.lower, EACH[1])):
            root = EACH[0].replace('\\', '/').replace('//', '/')
            return root + '/' + SEARCH_FILE + '.fbx'
    return False


def p4_CheckStatus():
    P4MasterPath = '//Lemon/Master/'
    P4ArtPath = '//LemonArtist/Master/'

    Check_All()

    # MA
    ma_scene_path = P4ArtPath + cmds.file(q=True, sn=True).split(':/')[-1]

    # FBX
    walked('M:/Assets/LemonArt')
    unity_asset_path=''
    for each in AnimClips:
        fbx_path = searchPath(SEARCH_PATH='L:/Assets/LemonArt', SEARCH_FILE=each, TARGET_EXT='fbx')
        if not fbx_path == '':
            unity_asset_path = P4MasterPath + fbx_path.replace('M:/', '')

    # print (unity_asset_path)
    # print (ma_scene_path)

    # print (MS_lemon_P4Lib.P4Info())
    # print (MS_lemon_P4Lib.P4Status(PATH=unity_asset_path))
    # print (MS_lemon_P4Lib.P4headRev(PATH=unity_asset_path))
    print(MS_lemon_P4Lib.P4CheckOut(PATHLIST=[unity_asset_path], ENABLE_DIALOG=True))


# Script job ######################################################################################################
def job():
    jobNum = cmds.scriptJob(e=["SceneOpened", lambda *args: job_newscene()], parent='MS_lemon_motion_exporter_window',
                           protected=True)


def job_newscene():
    initialize()
    UI()


# UI ##############################################################################################################


def LayoutC():
    cmds.frameLayout(l='MS_lemon_motion_exporter', cl=True, cll=False, bgc=[0.4, 0.4, 0.4])
    cmds.separator()
    #
    cmds.columnLayout(adj=True)

    ###
    cmds.rowLayout(nc=2, cw2=[100, 200], ct2=['left', 'both'], ad2=2, rat=[1, 'top', 0])

    ###### left #####
    cmds.columnLayout(adj=True)
    LayoutA()
    LayoutB()
    cmds.setParent('..')

    ###### right #####
    cmds.columnLayout(adj=True)
    # ログ用 #
    cmds.scrollField('MS_lemon_motion_exporter_log', ed=False, h=300)
    cmds.setParent('..')

    cmds.setParent('..')
    ###

    cmds.setParent('..')
    #
    cmds.separator()
    cmds.setParent('..')


def LayoutB():
    cmds.frameLayout(l='util', cl=True, cll=True, bgc=[0.4, 0.4, 0.4])
    cmds.separator()
    #
    cmds.columnLayout(adj=True)
    cmds.button(l='fix_preset', c=lambda *args: Check_All(exec_CheckAnimationClips=False, exec_SetupSettings=False))
    cmds.button(l='fix_AnimationClips',
               c=lambda *args: Check_All(exec_CheckAnimationClips=True, exec_SetupSettings=False))
    cmds.button(l='SetupSettings', c=lambda *args: Check_All(exec_CheckAnimationClips=False, exec_SetupSettings=True))
    cmds.button(l='P4', c=lambda *args: p4_CheckStatus())
    cmds.setParent('..')
    #
    cmds.separator()
    cmds.setParent('..')


def LayoutA():
    cmds.frameLayout(l='', cl=True, cll=False, bgc=[0.4, 0.4, 0.4])
    cmds.separator()
    #
    cmds.columnLayout(adj=True)

    cmds.checkBox('MS_lemon_motion_exporter_autofix', l='Auto fix', v=False, visible=False)
    cmds.button(l='check_All', c=lambda *args: Check_All())
    cmds.button(l='FIX_All', c=lambda *args: Check_All(auto_fix=True))
    cmds.button('MS_lemon_motion_exporter_bakeButton', l='bake motion', en=False, c=lambda *args: bake_motion(),
               ann=u'全てのチェックがOKにならないと、ベイク出来ません')
    cmds.button('MS_lemon_motion_exporter_GameFbxExporter', l='GameFbxExporter', c=lambda *args: GameFbxExporter())
    cmds.setParent('..')
    #
    cmds.separator()
    cmds.setParent('..')


def UI():
    if cmds.window('MS_lemon_motion_exporter_window', q=True, ex=True):
        cmds.deleteUI('MS_lemon_motion_exporter_window')
    cmds.window('MS_lemon_motion_exporter_window', rtf=True, s=True)

    ##LayoutA()
    ##LayoutB()
    LayoutC()
    cmds.showWindow('MS_lemon_motion_exporter_window')

    job()
