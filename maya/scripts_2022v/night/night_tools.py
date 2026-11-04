from audioop import reverse

import maya.cmds as cmds
import maya.mel as mel
import importlib

import _lib.MS_storeRecallUI as MS_storeRecallUI
importlib.reload(MS_storeRecallUI)


def cleanup():
    sel = cmds.ls(sl=True)
    for obj in sel:
        cmds.select(obj,r=True)
        # 1. 選択範囲をポリゴングループに拡張 (expandPolyGroupSelection)
        # 頂点やエッジから関連するフェースへ選択を広げます
        #cmds.select(cmds.polyListComponentConversion(toFace=True), replace=True)

        cleanup_cmd = 'polyCleanupArgList 4 { "0","1","1","0","0","0","0","0","1","1e-05","1","1e-05","1","0","0","1","1","1" };'
        mel.eval(cleanup_cmd)
        cmds.select(obj,r=True)
        cmds.polyMergeUV(d=0.0001)

    cmds.select(sel,r=True)
    print("クリーンアップが完了しました。")


def scales(x=1,y=1,z=1):
    sel = cmds.ls(sl=True)
    for obj in sel:
        cmds.setAttr(f"{obj}.scale", x, y, z)
        cmds.makeIdentity(obj, apply=True, t=False, r=False, s=True, n=False)

    print(f"{len(sel)} 個のオブジェクトを100倍にしてスケールをフリーズしました。")

def mergeVertx():
    sel = cmds.ls(selection=True)

    for obj in sel:
        # オブジェクト名.vtx[*] を指定して全頂点を対象にする
        vtx_all = obj + ".vtx[*]"
        cmds.polyMergeVertex(vtx_all, distance=0.001)

    print("オブジェクト内の重複頂点をマージしました。")

    cmds.select(sel,r=True)

def holeFix():
    # 1. 現在の選択（エッジなど）を取得
    sel = cmds.ls(selection=True, flatten=True)
    if not sel:
        cmds.warning("エッジ（または穴の周囲のコンポーネント）を選択してください。")
        return

    # オブジェクト名を取得
    obj = sel[0].split('.')[0]

    # 2. Fill Hole を実行
    # 実行前に現在のフェース数を取得して、新しく作られたフェースを特定できるようにする
    pre_face_count = cmds.polyEvaluate(obj, face=True)
    mel.eval('FillHole')
    post_face_count = cmds.polyEvaluate(obj, face=True)

    # 新しく作られたフェースのインデックスを特定
    new_faces = []
    if post_face_count > pre_face_count:
        new_faces = [f"{obj}.f[{i}]" for i in range(pre_face_count, post_face_count)]
    else:
        cmds.warning("新しいポリゴンが作成されませんでした。")
        return

    # 3. 新しいフェースにプレーンプロジェクションを実行
    # ひとまずY軸方向からの投影としています（必要に応じて変更可能）
    cmds.select(new_faces,r=True)

    mel.eval('performPolyProjection Planar 0')
    #projection_node = cmds.polyProjection(new_faces, type='Planar', mapDirection='y', ch=True)

    cmds.select(obj,r=True)
    cleanup()

    # 4. プロジェクションされたUVを選択
    # polyProjectionの後はUVが選択状態になることが多いですが、確実に対象を絞ります
    new_uvs = cmds.polyListComponentConversion(new_faces, toUV=True)
    #cmds.select(new_uvs, replace=True)
    cmds.select(new_faces,r=True)
    cmds.unfold(new_uvs, i=5000, ss=0.001, gb=0, gmb=0.5, pub=False, ps=False, oa=0, us=False)



    #cmds.u3dUnfold(ite=1, p=0, bi=1, tf=1, ms=1024, rs=0)

    # 7. polyLayoutUV でエリア指定配置
    # sc=1: スケールを維持（または 2: エリアにフィット）
    # lm=1: 単一の矩形エリアにレイアウト
    # l=2: ユーザー指定の矩形 (Layout Region)
    # gu, gv, su, sv: レイアウトの開始位置(U, V)とサイズ(U, V)
    # ここでは U=1, V=0 からサイズ1x1の範囲（つまり 1,0 から 2,1）に配置

    cmds.polyUVStackSimilarShells(to=0.001)
    return

    cmds.u3dLayout(res=1024,rot=2,scl=1,spc=0.00390625,mar=0.00390625,box=(1,2,0,1))
    mel.eval('texStackShells {};')
    # 仕上げ
    mel.eval('TextureViewWindow;')
    cmds.select(new_faces)
    print(f"完了: 新規フェース {new_faces} のUVを U[1,2] V[0,1] エリアにレイアウトしました。")



def merge_all_uvs(distance=0.01):
    # 現在選択されているオブジェクトを取得
    selection = cmds.ls(selection=True, objectsOnly=True)

    if not selection:
        cmds.warning("オブジェクトが選択されていません。ポリゴンモデルを選択して実行してください。")
        return

    merged_count = 0

    for obj in selection:
        # メッシュかどうかを確認（シェイプノードを取得）
        shapes = cmds.listRelatives(obj, shapes=True, type="mesh")

        if shapes:
            # オブジェクトの全UV（.map[*]）を対象にマージを実行
            uv_target = f"{obj}.map[*]"
            try:
                cmds.polyMergeUV(uv_target, distance=distance, constructionHistory=True)
                merged_count += 1
            except Exception as e:
                cmds.warning(f"{obj} のUVマージ中にエラーが発生しました: {e}")

    # 元の選択状態に戻す
    cmds.select(selection, replace=True)

    if merged_count > 0:
        print(f"完了: {merged_count} 個のオブジェクトの全UVをマージしました（しきい値: {distance}）")


# 実行（必要に応じて 0.001 の数値を変更してください）
merge_distance = 0.001
merge_all_uvs(merge_distance)




# Normals
def unlockNormals(angle=180):
    # 1. 選択されているコンポーネントまたはオブジェクトを取得
    sel = cmds.ls(selection=True, flatten=True)
    for obj in sel:
        if sel:
            cmds.polyNormalPerVertex(obj, unFreezeNormal=True)
            cmds.polySoftEdge(obj, angle=angle)  # ハードエッジにする場合は 0、ソフトなら 180
            print("法線のアンロックと再計算を完了しました。")
        else:
            cmds.warning("対象を選択してください。")
    cmds.select(sel,r=True)

def ReverseNormals():
    sel = cmds.ls(selection=True)
    for obj in sel:
        if sel:
            cmds.polyNormal(obj,normalMode=0, userNormalMode=1)
        else:
            cmds.warning("対象を選択してください。")
    cmds.select(sel,r=True)

# GameExporter
def SetGameExporter():
    # Game Exporter プラグインがロードされているか確認
    if not cmds.pluginInfo("gameFbxExporter", q=True, loaded=True):
        cmds.loadPlugin("gameFbxExporter")

    # Game Exporter ウィンドウを表示
    mel.eval("gameExporter;")

    # GameExporter設定Mel実行
    mel.eval('source "C:/Users/motok/Documents/maya/2022/presets/attrPresets/gameFbxExporter/_night_entity_model.mel";')

    # 最後に現在の設定をリフレッシュ
    mel.eval("gameExporter;")

    print(f"Game Exporter:プリセットを読み込みました。")

def SetGameExporterExportNameBySelection():
    sel = cmds.ls(sl=True)
    name = sel[0].replace('_LOD0','')
    cmds.setAttr('gameExporterPreset1.exportFilename',name,type="string")

def SetGameExporterExportPath():
    cmds.setAttr('gameExporterPreset1.exportSetIndex', 2)
    filepath = 'D:/night/night-app-client/Assets/Night/RawData/Entity/Models'
    cmds.setAttr('gameExporterPreset1.exportPath', filepath, type="string")


# Layout

def layoutTools(WIDTH=300,BGC=[0.2,0.2,0.2]):
    cmds.frameLayout('night_tools_frameLayout', w=WIDTH, bgc=BGC, fn='boldLabelFont', l='night_tools', cll=False,cl=True)
    cmds.columnLayout()

    #CC4
    cmds.text(l='scales',fn='boldLabelFont',w=WIDTH,bgc=(0.1,0.1,0.1))
    cmds.button(l='スケールを１００Xしてフリーズ',w=WIDTH,c=lambda *args:scales(100,100,100))
    cmds.rowLayout(nc=3,cw3=(WIDTH/3,WIDTH/3,WIDTH/3))
    cmds.button(l='sx-1',w=WIDTH/3,c=lambda *args:scales(-1,1,1))
    cmds.button(l='sy-1',w=WIDTH/3,c=lambda *args:scales(1,-1,1))
    cmds.button(l='sz-1',w=WIDTH/3,c=lambda *args:scales(1,1,-1))
    cmds.setParent('..')
    cmds.separator(h=10)

    #Vertex
    cmds.text(l='cleanup',fn='boldLabelFont',w=WIDTH,bgc=(0.1,0.1,0.1))
    cmds.button(l='複数選択一発MergeVertex',w=WIDTH,c=lambda *args:mergeVertx())
    cmds.button(l='cleanup',w=WIDTH,c=lambda *args:cleanup())
    cmds.separator(h=10)

    # UV
    cmds.text(l='uv',fn='boldLabelFont',w=WIDTH,bgc=(0.1,0.1,0.1))
    cmds.button(l='merge_all_uvs',w=WIDTH, c=lambda *args: merge_all_uvs())
    cmds.separator(h=10)

    #Texture
    cmds.text(l='unlockNormals',fn='boldLabelFont',w=WIDTH,bgc=(0.1,0.1,0.1))
    cmds.button(l='unlockNormals',w=WIDTH, c=lambda *args: unlockNormals())
    cmds.button(l='ReverseNormals',w=WIDTH, c=lambda *args: ReverseNormals())
    cmds.separator(h=10)

    #HoleFix
    cmds.text(l='holeFix',fn='boldLabelFont',w=WIDTH,bgc=(0.1,0.1,0.1))
    cmds.button(l='FillHoleしてUV作成（複数不可）',w=WIDTH, c=lambda *args: holeFix())
    cmds.separator(h=10)

    #Export
    cmds.text(l='Export',fn='boldLabelFont',w=WIDTH,bgc=(0.1,0.1,0.1))
    cmds.button(l='ExportPreset読み込み',w=WIDTH, c=lambda *args: SetGameExporter())
    #cmds.button(l='ExportPresetにファイルパス',w=WIDTH, c=lambda *args: SetGameExporterExportPath())
    #cmds.button(l='ExportPresetに選択モデル名',w=WIDTH, c=lambda *args: SetGameExporterExportNameBySelection())
    cmds.separator(h=10)

    cmds.setParent('..')
    cmds.setParent('..')


def UI():
    if cmds.window('night_tools_main_window', q=True, ex=True):
        cmds.deleteUI('night_tools_main_window')
    cmds.window('night_tools_main_window', rtf=True, s=True)
    cmds.columnLayout()

    layoutTools()

    cmds.setParent('..')

    cmds.window('night_tools_main_window', e=True, w=217, h=640)

    cmds.showWindow('night_tools_main_window')

    #MS_storeRecallUI.recall('night_tools_frameLayout')
