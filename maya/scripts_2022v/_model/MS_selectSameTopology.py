# Python版（MayaのScript Editorに貼り付けて実行）
import maya.cmds as cmds


def select_same_topology():
    selected = cmds.ls(selection=True, long=True)
    if not selected:
        print("オブジェクトを1つ選択してください")
        return

    target = selected[0]

    # トポロジー情報の取得（ポリゴンメッシュのみ対応）
    if cmds.nodeType(target) != 'transform' or not cmds.listRelatives(target, shapes=True):
        print("ポリゴンメッシュを選択してください")
        return

    shape = cmds.listRelatives(target, shapes=True)[0]

    vtx_count = cmds.polyEvaluate(shape, vertex=True)
    edge_count = cmds.polyEvaluate(shape, edge=True)
    face_count = cmds.polyEvaluate(shape, face=True)

    print(f"基準メッシュ: {target}")
    print(f"頂点数: {vtx_count}, 辺数: {edge_count}, 面数: {face_count}")

    all_meshes = cmds.ls(type='mesh')
    same_topo = []

    for mesh in all_meshes:
        parent = cmds.listRelatives(mesh, parent=True)[0]
        if parent == target:
            continue

        if (cmds.polyEvaluate(mesh, vertex=True) == vtx_count and
                cmds.polyEvaluate(mesh, edge=True) == edge_count and
                cmds.polyEvaluate(mesh, face=True) == face_count):
            same_topo.append(parent)

    if same_topo:
        cmds.select(same_topo, add=True)  # 基準オブジェクトも含めて選択したい場合はadd=True
        print(f"同じトポロジーのオブジェクトを {len(same_topo)} 個選択しました")
    else:
        print("同じトポロジーのオブジェクトは見つかりませんでした")

def layout_MS_selectSameTopology():
    cmds.columnLayout()
    cmds.text(l='SelectSameTopology',w=200,bgc=[0.8,0.8,0.8])
    cmds.button(l='Select same topology',w=200,c=lambda *args:select_same_topology())
    cmds.setParent('..')

# 実行
#select_same_topology()