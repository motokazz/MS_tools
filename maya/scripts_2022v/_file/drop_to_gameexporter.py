# -*- coding: utf-8 -*-

import maya.OpenMayaUI as omui
import maya.OpenMaya as om
import maya.cmds as cmds
import maya.mel as mel
import os

try:
    from PySide6.QtCore import QUrl
except ImportError:
    from PySide2.QtCore import QUrl


_drop_callback_instance = None
_UI_WINDOW_NAME = "FBXDropToGameExporterUI"


# ============================================================
# FBX Drop Callback
# ============================================================

class FBXDropToGameExporter(omui.MExternalDropCallback):

    def __init__(self):
        omui.MExternalDropCallback.__init__(self)

    def externalDropCallback(self, doDrop, controlName, data):

        if not data.hasUrls():
            return omui.MExternalDropCallback.kMayaDefault

        urls = data.urls()

        if not urls:
            return omui.MExternalDropCallback.kMayaDefault

        qurl = QUrl(urls[0])
        file_path = qurl.toLocalFile()

        if not file_path.lower().endswith(".fbx"):
            return omui.MExternalDropCallback.kMayaDefault

        if doDrop:

            directory = os.path.dirname(file_path).replace("\\", "/")
            filename = os.path.basename(file_path)
            filename_no_ext = os.path.splitext(filename)[0]

            # Python文字列を安全に渡す
            import maya.utils

            maya.utils.executeDeferred(
                lambda: safe_process_fbx(
                    file_path,
                    directory,
                    filename_no_ext
                )
            )

            # Maya標準のDrop処理はキャンセル
            return omui.MExternalDropCallback.kMayaDropAccept

        return omui.MExternalDropCallback.kMayaDefault


# ============================================================
# FBX処理
# ============================================================

def safe_process_fbx(file_path, directory, filename_no_ext):

    try:

        # ------------------------------------------------------
        # 1. FBXをImport
        # ------------------------------------------------------

        om.MGlobal.displayInfo(
            u"FBX Import開始: {}".format(file_path)
        )

        cmds.file(
            file_path,
            i=True,
            type="FBX",
            ignoreVersion=True,
            mergeNamespacesOnClash=False,
            options="v=0;",
            pr=True
        )

        # ------------------------------------------------------
        # 2. Game Exporterを起動
        # ------------------------------------------------------

        mel.eval("gameFbxExporter;")

        # ------------------------------------------------------
        # 3. Model用Presetを取得
        # ------------------------------------------------------

        node = "gameExporterPreset1"

        if not cmds.objExists(node):
            raise RuntimeError(
                "Game ExporterのModel Presetが見つかりません: {}".format(node)
            )

        # ------------------------------------------------------
        # 4. exportPath設定
        # ------------------------------------------------------

        if cmds.attributeQuery(
            "exportPath",
            node=node,
            exists=True
        ):

            cmds.setAttr(
                node + ".exportPath",
                directory,
                type="string"
            )

        # ------------------------------------------------------
        # 5. exportFilename設定
        # ------------------------------------------------------

        if cmds.attributeQuery(
            "exportFilename",
            node=node,
            exists=True
        ):

            cmds.setAttr(
                node + ".exportFilename",
                filename_no_ext,
                type="string"
            )

        # ------------------------------------------------------
        # 6. 設定確認
        # ------------------------------------------------------

        path_value = cmds.getAttr(
            node + ".exportPath"
        )

        filename_value = cmds.getAttr(
            node + ".exportFilename"
        )

        om.MGlobal.displayInfo(
            u"Game Exporter設定完了\n"
            u"Preset : {}\n"
            u"Path   : {}\n"
            u"File   : {}".format(
                node,
                path_value,
                filename_value
            )
        )

        # ------------------------------------------------------
        # 7. UI更新
        # ------------------------------------------------------

        try:
            mel.eval("gameExp_UpdateUIFromNode();")
        except Exception:
            pass

        msg = (
            u"FBXをインポートしました。\n\n"
            u"Game Exporter\n"
            u"Path : {}\n"
            u"File : {}"
        ).format(
            directory,
            filename_no_ext
        )

        cmds.inViewMessage(
            amg=msg.replace("\n", "<br>"),
            pos="midCenter",
            fade=True,
            time=3000
        )

    except Exception as e:

        om.MGlobal.displayError(
            u"FBX処理中にエラーが発生しました: {}".format(e)
        )


# ============================================================
# Callback管理
# ============================================================

def is_active():

    global _drop_callback_instance

    return _drop_callback_instance is not None


def install():

    global _drop_callback_instance

    if not is_active():

        _drop_callback_instance = FBXDropToGameExporter()

        omui.MExternalDropCallback.addCallback(
            _drop_callback_instance
        )

        om.MGlobal.displayInfo(
            u"【ON】FBX GameExporter連携を有効化しました。"
        )

    refresh_ui()


def uninstall():

    global _drop_callback_instance

    if is_active():

        omui.MExternalDropCallback.removeCallback(
            _drop_callback_instance
        )

        _drop_callback_instance = None

        om.MGlobal.displayInfo(
            u"【OFF】FBX GameExporter連携を無効化しました。"
        )

    refresh_ui()


def toggle_from_ui(*args):

    if is_active():
        uninstall()
    else:
        install()


# ============================================================
# UI
# ============================================================

def refresh_ui():

    if not cmds.window(
        _UI_WINDOW_NAME,
        exists=True
    ):
        return

    if is_active():

        cmds.text(
            "fbxDropStatusText",
            edit=True,
            label=u"ステータス : 【 ON 】",
            backgroundColor=(0.2, 0.6, 0.3)
        )

        cmds.button(
            "fbxDropToggleButton",
            edit=True,
            label=u"無効にする (Turn OFF)",
            backgroundColor=(0.3, 0.3, 0.3)
        )

    else:

        cmds.text(
            "fbxDropStatusText",
            edit=True,
            label=u"ステータス : 【 OFF 】",
            backgroundColor=(0.6, 0.2, 0.2)
        )

        cmds.button(
            "fbxDropToggleButton",
            edit=True,
            label=u"有効にする (Turn ON)",
            backgroundColor=(0.2, 0.5, 0.8)
        )


def UI():

    if cmds.window(
        _UI_WINDOW_NAME,
        exists=True
    ):
        cmds.deleteUI(_UI_WINDOW_NAME)

    cmds.window(
        _UI_WINDOW_NAME,
        title=u"FBX to GameExporter 設定",
        widthHeight=(300, 150),
        sizeable=False
    )

    cmds.columnLayout(
        adjustableColumn=True,
        rowSpacing=10,
        columnOffset=("both", 15)
    )

    cmds.separator(
        height=15,
        style="none"
    )

    cmds.text(
        label=u"FBXをビューポートにドロップした時の\n"
              u"GameExporter自動パス設定ツール",
        align="center",
        font="boldLabelFont"
    )

    cmds.separator(
        height=5,
        style="none"
    )

    cmds.text(
        "fbxDropStatusText",
        label="",
        align="center",
        height=30
    )

    cmds.button(
        "fbxDropToggleButton",
        label="",
        height=40,
        command=toggle_from_ui
    )

    cmds.separator(
        height=5,
        style="none"
    )

    refresh_ui()

    cmds.showWindow(_UI_WINDOW_NAME)

