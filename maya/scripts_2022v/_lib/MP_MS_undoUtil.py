# coding=utf-8
# MP_MS_undoUtil
import maya.cmds as cmds


def flush(*args):
    cmds.flushUndo()
    print('アンドゥ情報をクリアしました')


def info(*args):
    cmds.confirmDialog(m=
                       '元に戻す/再実行のオンとオフを切り替えます。：' + str(cmds.undoInfo(q=True, state=True)) + '\n'
                       + '待ち行列の長さ（取り消しできる回数）を無限にします。：' + str(
                           cmds.undoInfo(q=True, infinity=True)) + '\n'
                       + '元に戻す待ち行列の項目数を指定します。 infinity フラグを使用すると、このフラグはオーバーライドされます。：' + str(
                           cmds.undoInfo(q=True, length=True)) + '\n'
                       + '元に戻す対象取り消しされるものがあれば、その名前を返します。：' + str(
                           cmds.undoInfo(q=True, undoName=True)) + '\n'
                       + 'やり直されるものがあれば、その名前を返します。：' + str(
                           cmds.undoInfo(q=True, redoName=True)) + '\n'
                       + '元に戻す待ち行列が空であれば、true を返します。待ち行列に元に戻すコマンドが 1 つでもあれば、false を返します。：' + str(
                           cmds.undoInfo(q=True, undoQueueEmpty=True)) + '\n'
                       + '再実行の待ち行列が空であれば、true を返します。待ち行列に再実行するコマンドが 1 つでもあれば、false を返します。：' + str(
                           cmds.undoInfo(q=True, redoQueueEmpty=True)) + '\n'
                       + '元に戻す待ち行列の内容をスクリプト エディタに出力します。：' + str(
                           cmds.undoInfo(q=True, printQueue=True)) + '\n'
                       + '待ち行列の内容を消去せずに、undo/redo のオンとオフを切り替えます。：' + str(
                           cmds.undoInfo(q=True, stateWithoutFlush=True)) + '\n'
                       )


def stateWithoutFlush(STATE):
    # 非破壊アンドゥ切り替え
    if STATE == 'on':
        cmds.undoInfo(stateWithoutFlush=True)
        print('アンドゥ：入')
    else:
        cmds.undoInfo(stateWithoutFlush=False)
        print('アンドゥ：切')
    undoState()


def undoState():  # UIステータス更新
    if cmds.undoInfo(q=True, state=True):
        cmds.button('MP_MS_undoInfo_undo_On', e=True, bgc=[1.0, 1.0, 1.0])
        cmds.button('MP_MS_undoInfo_undo_Off', e=True, bgc=[0.3, 0.3, 0.3])
    else:
        cmds.button('MP_MS_undoInfo_undo_Off', e=True, bgc=[1.0, 1.0, 1.0])
        cmds.button('MP_MS_undoInfo_undo_On', e=True, bgc=[0.3, 0.3, 0.3])


def controll():  # コントロール作成部
    cmds.frameLayout(l='アンドゥ関連', bgc=[0.4, 0.5, 0.5], cll=True, cl=False)
    cmds.columnLayout()
    cmds.button(l='フラッシュアンドゥ', c=flush)

    cmds.text(l='非破壊アンドゥ切り替え')
    cmds.rowLayout(nc=2)
    cmds.button('MP_MS_undoInfo_undo_On', l='入', c=lambda *args: stateWithoutFlush('on'))
    cmds.button('MP_MS_undoInfo_undo_Off', l='切', c=lambda *args: stateWithoutFlush('off'))
    cmds.setParent('..')
    cmds.button(l='アンドゥ情報', c=info)
    cmds.setParent('..')
    cmds.setParent('..')
    undoState()


def UI():  # UIメイン
    if cmds.window('MP_MS_commonUI', q=True, ex=True):
        cmds.deleteUI('MP_MS_commonUI')
    cmds.window('MP_MS_commonUI')

    controll()

    cmds.showWindow('MP_MS_commonUI')