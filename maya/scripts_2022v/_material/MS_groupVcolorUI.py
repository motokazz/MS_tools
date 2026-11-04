# -*- coding:utf-8 -*-
import sys
import maya.cmds as cmds
from math import sqrt


class MS_distanceValue():
    def __init__(self, baseObj, distObjs):
        self.baseObj = baseObj
        self.distObjs = distObjs

    def sorted(self):
        # 戻り値: [オブジェクト名, 距離, 距離の正規化値]
        # ターゲットとの距離を検出
        baseLoc = cmds.xform(self.baseObj, q=True, ws=True, t=True)
        distances = []
        for each in self.distObjs:
            distObjLoc = cmds.xform(each, q=True, ws=True, t=True)
            # 三平方の定理で距離を計算
            tempRange = sqrt(
                (baseLoc[0] - distObjLoc[0]) ** 2 +
                (baseLoc[1] - distObjLoc[1]) ** 2 +
                (baseLoc[2] - distObjLoc[2]) ** 2
            )
            distances.append([each, tempRange])

        # Python 3対応: cmpの代わりにkeyを使用
        distances.sort(key=lambda x: x[1])

        if not distances:
            return []

        varMin = distances[0][1]
        varMax = distances[-1][1]

        # 距離の差が0の場合の除算エラー回避
        distDiff = (varMax - varMin) if (varMax - varMin) != 0 else 1.0

        distancesVar = []
        for var in distances:
            # 距離に基づいて0〜1に正規化（近いほど1）
            varTemp = 1 - (var[1] - varMin) / distDiff
            distancesVar.append([var[0], var[1], varTemp])
        return distancesVar


def MS_nearestObjectV2_distance(target_a, target_b):
    a = cmds.xform(target_a, q=True, ws=True, t=True)
    b = cmds.xform(target_b, q=True, ws=True, t=True)
    # 2点間の直線距離を計算
    dist = sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)
    return dist


def MS_nearestObjectV2(sourceObj, distObj):
    dists = []
    for each in sourceObj:
        ftemp = MS_nearestObjectV2_distance(distObj, each)
        dists.append([ftemp, each])

    # Python 3では単純な sort() で最初の要素(距離)を基準にソートされる
    dists.sort()

    final = [each[1] for each in dists]
    return final


def MS_groupVcolor_selectFilter():
    # 選択フィルタリング
    objz = cmds.ls(sl=True, dag=True, type='mesh')
    if not objz:
        # メッシュ、頂点、エッジ、フェースなどを許可
        objz = cmds.filterExpand(sm=(12, 31, 32, 34))
    return objz


def MS_groupVcolor():
    effectiveRGB = cmds.checkBox('effectiveRGB', q=True, v=True)
    effectiveAlpha = cmds.checkBox('effectiveAlpha', q=True, v=True)
    considerNearest = cmds.checkBox('considerNearest', q=True, v=True)

    startRGB = cmds.colorSliderGrp('startRGB', q=True, rgb=True)
    startAlpha = cmds.colorSliderGrp('startAlpha', q=True, rgb=True)

    endRGB = cmds.colorSliderGrp('endRGB', q=True, rgb=True)
    endAlpha = cmds.colorSliderGrp('endAlpha', q=True, rgb=True)

    interpMode = cmds.radioCollection('interpMode', q=True, sl=True)
    obj = MS_groupVcolor_selectFilter()
    target = cmds.textFieldGrp('objName', q=True, tx=True)

    if not obj:
        cmds.warning("オブジェクトが選択されていません。")
        return

    # 近傍距離を考慮して頂点カラーを塗る
    if considerNearest and len(obj) > 1 and target != '':
        distValues = MS_distanceValue(baseObj=target, distObjs=obj)
        for eachobj in distValues.sorted():
            # 補間モードの判定
            if interpMode == 'sqrt':
                DistanceValue = sqrt(eachobj[2])
            elif interpMode == 'pow':
                DistanceValue = eachobj[2] ** 2
            else:
                DistanceValue = eachobj[2]

            if effectiveRGB:
                colR = (startRGB[0] * DistanceValue) + (endRGB[0] * (1 - DistanceValue))
                colG = (startRGB[1] * DistanceValue) + (endRGB[1] * (1 - DistanceValue))
                colB = (startRGB[2] * DistanceValue) + (endRGB[2] * (1 - DistanceValue))
                cmds.polyColorPerVertex(eachobj[0], r=colR, g=colG, b=colB)
            if effectiveAlpha:
                colA = (startAlpha[0] * DistanceValue) + (endAlpha[0] * (1 - DistanceValue))
                cmds.polyColorPerVertex(eachobj[0], a=colA)
    else:
        # 選択順やリスト順でグラデーション
        i = 0
        num = len(obj)
        for eachobj in obj:
            ratio = (num - i) / float(num) if num > 0 else 1.0
            colR = endRGB[0] + (ratio * (startRGB[0] - endRGB[0]))
            colG = endRGB[1] + (ratio * (startRGB[1] - endRGB[1]))
            colB = endRGB[2] + (ratio * (startRGB[2] - endRGB[2]))
            colA = endAlpha[0] + (ratio * (startAlpha[0] - endAlpha[0]))

            if effectiveRGB:
                cmds.polyColorPerVertex(eachobj, r=colR, g=colG, b=colB)
            if effectiveAlpha:
                cmds.polyColorPerVertex(eachobj, a=colA)
            i += 1


def MS_groupVcolorUI_takeObj():
    # ターゲットオブジェクトを取得
    obj = cmds.ls(l=True, sl=True)
    if obj:
        cmds.textFieldGrp('objName', e=True, tx=obj[0])


def MS_groupVcolorUI_takeVcol():
    # 選択頂点等からカラーを取得
    obj = cmds.ls(l=True, sl=True)
    if obj:
        VCOL = cmds.polyColorPerVertex(obj[0], q=True, r=True, g=True, b=True, a=True)
        if VCOL:
            cmds.colorSliderGrp('startRGB', e=True, rgb=VCOL[0:3])
            cmds.colorSliderGrp('startAlpha', e=True, rgb=(VCOL[3], VCOL[3], VCOL[3]))


def UI():
    if cmds.window('MS_groupVcolor', exists=True):
        cmds.deleteUI('MS_groupVcolor')

    window = cmds.window('MS_groupVcolor', t='MS_groupVcolor', w=320, h=350)
    cmds.columnLayout(adj=True)
    cmds.text(al='left', fn='boldLabelFont', l=' 1. Select Objects / 2. Set Colors / 3. Go')
    cmds.separator(h=10)

    cmds.rowLayout(nc=2, ad2=2)

    # 左カラム: オプション
    cmds.columnLayout(w=120)
    cmds.frameLayout(l="Channels", cll=False, w=110)
    cmds.checkBox('effectiveRGB', v=1, l='Color RGB')
    cmds.checkBox('effectiveAlpha', v=1, l='Alpha')
    cmds.setParent('..')

    cmds.frameLayout(l="Distance Target", cll=False, w=110)
    cmds.checkBox('considerNearest', v=1, l='Use Distance')
    cmds.textFieldGrp('objName', w=100, en=1)  # 編集可能に変更
    cmds.button(bgc=(0.8, 0.8, 1.0), l='Set Target', c=lambda *args: MS_groupVcolorUI_takeObj())
    cmds.button(bgc=(0.8, 0.8, 1.0), l='Get V-Color', c=lambda *args: MS_groupVcolorUI_takeVcol())
    cmds.setParent('..')

    cmds.frameLayout(l="Interpolation", cll=False, w=110)
    cmds.radioCollection('interpMode')
    cmds.radioButton('linear', label='Linear', sl=True)
    cmds.radioButton('pow', label='Pow (Ease-in)')
    cmds.radioButton('sqrt', label='Sqrt (Ease-out)')
    cmds.setParent('..')
    cmds.setParent('..')

    # 右カラム: カラー設定
    cmds.columnLayout()
    cmds.frameLayout(l="Start", cll=False)
    cmds.colorSliderGrp('startRGB', cw3=(60, 40, 80), rgb=(1, 1, 1), l='RGB')
    cmds.colorSliderGrp('startAlpha', cw3=(60, 40, 80), rgb=(1, 1, 1), l='Alpha')
    cmds.setParent('..')

    cmds.frameLayout(l="End", cll=False)
    cmds.colorSliderGrp('endRGB', cw3=(60, 40, 80), rgb=(0, 0, 0), l='RGB')
    cmds.colorSliderGrp('endAlpha', cw3=(60, 40, 80), rgb=(0, 0, 0), l='Alpha')
    cmds.setParent('..')

    cmds.button('groupVcolor', bgc=(0.8, 1.0, 0.8), h=40, l='Apply Vertex Color', c=lambda *args: MS_groupVcolor())
    cmds.setParent('..')

    cmds.showWindow(window)


UI()