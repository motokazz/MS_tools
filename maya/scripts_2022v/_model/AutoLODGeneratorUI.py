import maya.cmds as cmds
import maya.mel as mel
import re


class AutoLODGeneratorUI:
    def __init__(self):
        self.window_name = "AutoLODGeneratorWindow"
        self.window_title = "自動LOD生成ツール (スキン・上書き対応)"
        self.create_ui()

    def create_ui(self):
        if cmds.window(self.window_name, exists=True):
            cmds.deleteUI(self.window_name)

        # UI項目が増えたため、ウィンドウの高さを少し広げています
        self.window = cmds.window(self.window_name, title=self.window_title, widthHeight=(400, 220), sizeable=False)
        cmds.columnLayout(adjustableColumn=True, rowSpacing=10, columnAttach=('both', 15))

        cmds.text(label="オブジェクトを選択して設定・実行してください", font="boldLabelFont", align="center", height=30)
        cmds.separator(style="in")

        # 1. LODの数
        self.lod_count_ctrl = cmds.intSliderGrp(
            label="LODの生成数", field=True,
            minValue=1, maxValue=5, fieldMinValue=1, fieldMaxValue=10,
            value=2, columnWidth3=(100, 50, 150)
        )

        # 2. 削減率
        self.reduce_pct_ctrl = cmds.floatSliderGrp(
            label="1段階の削減率", field=True,
            minValue=10.0, maxValue=90.0, fieldMinValue=1.0, fieldMaxValue=99.0,
            value=50.0, columnWidth3=(100, 50, 150)
        )

        # 3. スキンウェイトのコピー設定
        self.copy_skin_ctrl = cmds.checkBoxGrp(
            numberOfCheckBoxes=1,
            label="スキニング",
            label1="元モデルから自動判別してウェイトを転送",
            value1=True,  # デフォルトでON
            columnWidth2=(100, 250)
        )

        # 4. 既存LODの削除設定（新規追加）
        self.delete_existing_ctrl = cmds.checkBoxGrp(
            numberOfCheckBoxes=1,
            label="既存の上書き",
            label1="同名のLODが存在する場合は削除して作り直す",
            value1=True,  # デフォルトでON
            columnWidth2=(100, 250)
        )

        cmds.separator(style="in")

        # 5. 実行ボタン
        cmds.button(
            label="LODを生成", command=self.execute_generation,
            height=40, backgroundColor=(0.2, 0.6, 0.8)
        )

        cmds.showWindow(self.window)

    def get_skin_cluster(self, obj):
        """オブジェクトに紐づくスキンクラスターを取得する関数"""
        history = cmds.listHistory(obj, pruneDagObjects=True) or []
        skin_clusters = cmds.ls(history, type='skinCluster')
        return skin_clusters[0] if skin_clusters else None

    def execute_generation(self, *args):
        # UIから値を取得
        lod_count = cmds.intSliderGrp(self.lod_count_ctrl, query=True, value=True)
        reduce_percent = cmds.floatSliderGrp(self.reduce_pct_ctrl, query=True, value=True)
        copy_skin = cmds.checkBoxGrp(self.copy_skin_ctrl, query=True, value1=True)
        delete_existing = cmds.checkBoxGrp(self.delete_existing_ctrl, query=True, value1=True)

        self.generate_lods(reduce_percent, lod_count, copy_skin, delete_existing)

    def generate_lods(self, reduce_percent, lod_count, copy_skin, delete_existing):
        selection = cmds.ls(selection=True, type='transform')
        if not selection:
            cmds.warning("対象のオブジェクトを選択してから実行してください。")
            return

        created_lods = []

        for obj in selection:
            # 名前に _LOD# が含まれているか解析
            match = re.search(r'^(.*)_LOD(\d+)$', obj)

            if match:
                base_name = match.group(1)
                start_index = int(match.group(2)) + 1
            else:
                base_name = obj
                start_index = 1

            # 元モデルのスキン情報を取得
            original_skin = self.get_skin_cluster(obj)
            influences = []

            if copy_skin and original_skin:
                influences = cmds.skinCluster(original_skin, query=True, influence=True)
                print(f"[{obj}] スキニング情報を検出しました。ウェイトを転送します。")

            current_source = obj

            for step in range(lod_count):
                current_lod_index = start_index + step
                new_name = f"{base_name}_LOD{current_lod_index}"

                # --- 新規追加：既存の同名LODを削除 ---
                if delete_existing:
                    # cmds.ls を使うことで階層違いの同名オブジェクトも含めて安全に検知
                    existing_objs = cmds.ls(new_name)
                    if existing_objs:
                        cmds.delete(existing_objs)
                        print(f"既存のモデル '{new_name}' を削除して上書きします。")
                # -----------------------------------

                # 複製して新しい名前にする
                duplicated = cmds.duplicate(current_source, returnRootsOnly=True, name=new_name)[0]

                cmds.select(duplicated, replace=True)

                if step == 0:
                    mel.eval('expandPolyGroupSelection;')
                    mel.eval(
                        'polyCleanupArgList 4 { "0","1","1","0","0","0","0","0","0","1e-05","0","1e-05","0","1e-05","0","1","1","0" };')

                # ポリゴン削減
                cmds.polyReduce(
                    duplicated, percentage=reduce_percent, preserveTopology=True,
                    keepBorder=True, keepMapBorder=True, keepColorBorder=True,
                    keepFaceGroupBorder=True, keepHardEdge=True, keepCreaseEdge=True,
                    caching=True, constructionHistory=False
                )

                # スキンウェイトの転送処理
                if copy_skin and original_skin and influences:
                    cmds.select(influences + [duplicated], replace=True)
                    new_skin = cmds.skinCluster(
                        toSelectedBones=True, bindMethod=0, skinMethod=0,
                        normalizeWeights=1, maximumInfluences=4, obeyMaxInfluences=False
                    )[0]

                    cmds.copySkinWeights(
                        sourceSkin=original_skin, destinationSkin=new_skin,
                        noMirror=True, surfaceAssociation='closestPoint', influenceAssociation='closestJoint'
                    )

                created_lods.append(duplicated)
                current_source = duplicated

        if created_lods:
            cmds.select(created_lods, replace=True)
            print(f"LODの作成が完了しました: {created_lods}")


def UI():
    AutoLODGeneratorUI()