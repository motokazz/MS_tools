#-*- coding:UTF-8 -*-

#*******************************************************************************
'''

Tool Name     : MYAM_sceneChecker_main
Description   : 主にBGシーンのエラーをチェックするツールのメインモジュール

Copyright     : (c)2012 Sony Computer Entertainment lnc. Visual Arts Group
Author Name   : Michiyoshi Yamabe
Contact       : Michiyoshi_Yamabe@hq.scei.sony.co.jp

------------------------------------
----- Using external libraries -----
------------------------------------
[lisenceType] libraryName version

-------------------------
----- UPDATE RECORD -----
-------------------------
[date] details

'''
#*******************************************************************************

## Import official modules

import maya.cmds as cmds
import maya.mel  as mel
import re
import os
import shutil
import time

## Import custom modules

import MYAM_PyLib_mayaUI   as mayaUI
import MYAM_PyLib_math     as myamMath
import MYAM_PyLib_geometry as geometry

import MYAM_PyLib_mayaMessageAdapter as mayaMessageAdapter

## Reload custom modules

reload( mayaUI )
reload( myamMath )
reload( geometry )

reload( mayaMessageAdapter )






## Main Functions

class mainWindow( object ):

  def __init__( self ):
    self.windowTitle = "MYAM_sceneChecker"
    self.windowName = cmds.window( "MYAM_sceneChecker_#" , title=self.windowTitle , menuBar=1 )

    self.width = 700
    self.height = 480

    self.MMA = mayaMessageAdapter.MayaMessagesAdapter()

    self.results = []

    self.isIncludeRootNodeRE = re.compile( "[|]a[0-9]*_[A-Z]*_root.*" )

    self.careStrategy = Carer_MV()

    self.carerDic = {}
    self.carerDic[ "Locator MV" ] = Carer_MV()
    self.carerDic[ "Locator OB" ] = Carer_OB()
    self.carerDic[ "Name Double" ] = Carer_DoubleName()
    self.carerDic[ "Scale" ] = Carer_Scale()
    self.carerDic[ "Hierarchy" ] = Carer_Hierarchy()
    self.carerDic[ "Vertex Color" ] = Carer_VertexColor()
    self.carerDic[ "Time Unit" ] = Carer_TimeUnit()
    self.carerDic[ "LocatorLocalPos" ] = Carer_LocatorLocalPosition()
    self.carerDic[ "Double MV Name" ] = Carer_DoubleMVName()
    self.carerDic[ "InvalidAnimCurve" ] = Carer_InvalidAnimCurve()
    self.carerDic[ "HasWeightEndJoint" ] = Carer_hasWeightEndJoint()

    ## UI Placement
    self.rootLayout = mayaUI.layout.FormLayout()

    ##
    self.methodTX = mayaUI.control.Text()
    self.resultTX = mayaUI.control.Text()

    ##
    self.methodTSL = mayaUI.control.TextScrollList()
    self.resultTSL = mayaUI.control.TextScrollList()

    ##
    self.resultPUMN = mayaUI.menu.PopupMenu()
    self.resultRepairMI = mayaUI.menu.MenuItem()

    ##
    self.buttonsCLo = mayaUI.layout.ColumnLayout()

    self.filterOptionsHULo = mayaUI.layout.HUniformLayout()
    self.filterOptionsTX = mayaUI.control.Text()
    self.aloneFilterCB = mayaUI.control.CheckBox()
    self.cutFilterCB = mayaUI.control.CheckBox()
    self.clothFilterCB = mayaUI.control.CheckBox()
    self.filterOptionsHULo.arrange()
    cmds.setParent( ".." ) ## End of self.resetButtonsHULo

    self.doCheckBT = mayaUI.control.Button()
    self.totalCheckBT = mayaUI.control.Button()

    self.resetButtonsTX = mayaUI.control.Text()

    self.resetButtonsHULo = mayaUI.layout.HUniformLayout()
    self.resetFrameRateBT = mayaUI.control.Button()
    self.resetLocalPosBT = mayaUI.control.Button()
    self.freezeScaleBT = mayaUI.control.Button()
    self.fillNotEnoughVtxColorBT = mayaUI.control.Button()
    self.deleteInvalidAnimCurveBT = mayaUI.control.Button()
    self.resetButtonsHULo.arrange()
    cmds.setParent( ".." ) ## End of self.resetButtonsHULo

    self.progressBar = mayaUI.control.ProgressBar()

    cmds.setParent( ".." ) ## End of self.buttonsCLo

    ## UI Placement

    self.rootLayout.af = [ ( self.methodTX.uiName , "top"   , 0 ) ,
                           ( self.methodTX.uiName , "left"  , 0 ) ]

    self.rootLayout.af = [ ( self.resultTX.uiName , "top"   , 0 ) ,
                           ( self.resultTX.uiName , "right" , 0 ) ]
    self.rootLayout.ac = [ ( self.resultTX.uiName , "left"  , 0 , self.methodTX.uiName ) ]

    self.rootLayout.af = [ ( self.methodTSL.uiName , "left"   , 0 ) ]
    self.rootLayout.ac = [ ( self.methodTSL.uiName , "top"    , 0 , self.methodTX.uiName ) ,
                           ( self.methodTSL.uiName , "bottom" , 0 , self.buttonsCLo.uiName ) ]

    self.rootLayout.af = [ ( self.resultTSL.uiName , "right"  , 0 ) ]
    self.rootLayout.ac = [ ( self.resultTSL.uiName , "top"    , 0 , self.resultTX.uiName ) ,
                           ( self.resultTSL.uiName , "left"   , 0 , self.methodTSL.uiName ) ,
                           ( self.resultTSL.uiName , "bottom" , 0 , self.buttonsCLo.uiName ) ]

    self.rootLayout.af = [ ( self.buttonsCLo.uiName , "left"   , 0 ) ,
                           ( self.buttonsCLo.uiName , "right"  , 0 ) ,
                           ( self.buttonsCLo.uiName , "bottom" , 0 ) ]

    ## Set UI Contents

    ##
    self.methodTX.label = "----- Method -----"
    self.methodTX.width = 100
    self.methodTX.align = "center"

    self.methodTSL.width = 100
    self.methodTSL.selectCommand = self.selectMethodTSL
    self.methodTSL.doubleClickCommand = self.doubleClickMethodTSL
    self.methodTSL.set( self.carerDic.keys() )
    self.methodTSL.selectIndexedItem = 1

    ##
    self.resultTX.label = "----- Results -----"
    self.resultTX.align = "center"

    self.resultTSL.allowMultiSelection = 1
    self.resultTSL.selectCommand = self.selectResultTSL

    self.resultRepairMI.label = 'Repair'
    self.resultRepairMI.command = self.selectResultRepairMI
    self.resultRepairMI.enable = 0

    ##
    self.buttonsCLo.adjustableColumn = 1

    self.filterOptionsTX.label = u'タイプ別結果フィルタ'
    self.filterOptionsTX.align = 'center'

    self.aloneFilterCB.label = u'Alone階層もチェック'
    self.aloneFilterCB.value = 1
    self.aloneFilterCB.changeCommand = self.changeFileterCBs

    self.cutFilterCB.label = u'cut階層もチェック'
    self.cutFilterCB.value = 1
    self.cutFilterCB.changeCommand = self.changeFileterCBs

    self.clothFilterCB.label = u'cloth階層もチェック'
    self.clothFilterCB.value = 1
    self.clothFilterCB.changeCommand = self.changeFileterCBs

    self.doCheckBT.label = 'Do Check'
    self.doCheckBT.visible = 0

    self.totalCheckBT.label = '一括チェック'
    self.totalCheckBT.command = self.pushTotalCheckBT

    self.resetButtonsTX.label = u"↓↓↓ いろいろ修復ボタン ↓↓↓"
    self.resetButtonsTX.backgroundColor = [0.5, 0.5, 0.5]

    self.resetLocalPosBT.label = u"ローカルポジションをリセット"
    self.resetLocalPosBT.command = self.pushResetLocalPosBT

    self.resetFrameRateBT.label = u'フレームレートを30fpsにする'
    self.resetFrameRateBT.command = self.pushResetFrameRateBT

    self.freezeScaleBT.label = u'スケールをフリーズ'
    self.freezeScaleBT.command = self.pushFreezeScaleBT

    self.fillNotEnoughVtxColorBT.label = u'未設定頂点カラーを埋める'
    self.fillNotEnoughVtxColorBT.command = self.pushFillNotEnoughVtxColorBT

    self.deleteInvalidAnimCurveBT.label = u'不正なanimCurveを削除'
    self.deleteInvalidAnimCurveBT.command = self.pushDeleteInvalidAnimCurveBT

    ## Show Window
    cmds.window( self.windowName , e=1 , sizeable=1 ,
                 minimizeButton=0 , maximizeButton=0 ,
                 width=self.width , height=self.height )

    cmds.showWindow( self.windowName )

    self.changeAnnotation()
    self.checkTotal()
    self.setResults()

  ##

  def setMayaMessage( self ):
    command = 'MYAM_sceneChecker_autoCheckTotal();'
    self.MMA.setCallback( "BeforeSave" , command , 0 )

  ## UI Control

  def selectMethodTSL( self , *args ):
    self.changeAnnotation()

  def doubleClickMethodTSL( self , *args ):
    self.changeCheckerStrategy()
    self.check()

  def selectResultTSL( self , *args ):
    self.selectResultItems()

  def selectResultRepairMI( self , *args ):
    self.careStrategy.repair()

  def pushTotalCheckBT( self , *args ):
    self.checkTotal()

  def pushResetFrameRateBT( self , *args ):
    try:
      cmds.undoInfo( openChunk=1 )
      self.resetFrameRate()
    finally:
      cmds.undoInfo( closeChunk=1 )

  def pushResetLocalPosBT( self , *args ):
    try:
      cmds.undoInfo( openChunk=1 )
      self.resetLocalPos()
    finally:
      cmds.undoInfo( closeChunk=1 )

  def pushFreezeScaleBT( self , *args ):
    try:
      cmds.undoInfo( openChunk=1 )
      self.freezeScale()
    finally:
      cmds.undoInfo( closeChunk=1 )

  def pushFillNotEnoughVtxColorBT( self , *args ):
    try:
      cmds.undoInfo( openChunk=1 )

      if not cmds.pluginInfo( "MYAM_fillNotEnoughVertexColorsCmd.py" , q=1 , loaded=1 ):
        mel.eval( 'catch(`loadPlugin "D:/Puppeteer/Maya/plug-ins/2009-AMD64/MYAM_fillNotEnoughVertexColorsCmd.py"`);' )

      mel.eval( 'fillNotEnoughVertexColors -c 1 -ad 0;' )
    finally:
      cmds.undoInfo( closeChunk=1 )

  def pushDeleteInvalidAnimCurveBT( self , *args ):
    try:
      cmds.undoInfo( openChunk=1 )
      self.deleteInvalidAnimCurve()
    finally:
      cmds.undoInfo( closeChunk=1 )

  def pushCleanupSaveBT( self , *args ):
    self.cleanUpSave()

  def changeFileterCBs( self, *args ):
    self.setResults()

  def changeAnnotation( self ):
    currentMethod = self.methodTSL.selectItem[0]

    if currentMethod == "Time Unit":
      self.methodTSL.annotation = u'現在のタイムユニットが 30fpsであるかチェックします。'

    elif currentMethod == "Scale":
      self.methodTSL.annotation = u'現在シーンに、スケール[ 1.0 , 1.0 , 1.0 ]以外の値を持つアイテムがあるかチェックします。'

    elif currentMethod == "Name Double":
      self.methodTSL.annotation = u'現在シーンに、重複する名前を持つロケータがあるかチェックします。'

    elif currentMethod == "Hierarchy":
      self.methodTSL.annotation = u'二つのノード階層を比較し、両方の同じ階層に存在しないノードをリストアップします。'

    elif currentMethod == "Vertex Color":
      self.methodTSL.annotation = u'頂点カラーを持つオブジェクトが、全頂点にカラーを持っていないかチェックします。'

    elif currentMethod == "Locator OB":
      self.methodTSL.annotation = u'OB_ の子が ob_ である、もしくは直下に mv_top がない場合に警告します。'

    elif currentMethod == "Locator MV":
      self.methodTSL.annotation = u'MVロケーターが正しい階層構造の中にあるかチェックします。'

    elif currentMethod == "LocatorLocalPos":
      self.methodTSL.annotation = u'ロケーターがローカルポジションを持っていないかチェックします。'

    elif currentMethod == "Double MV Name":
      self.methodTSL.annotation = u'ob内で名前が重複しているmvロケータを探します'

    elif currentMethod == "InvalidAnimCurve":
      self.methodTSL.annotation = u'不正なanimCurveが存在するかチェックします。'

    elif currentMethod == "HasWeightEndJoint":
      self.methodTSL.annotation = u'末端ジョイントがウエイト値を持っていないかチェックします。'

    else:
      pass

  ## Methods

  def changeCheckerStrategy( self ):
    selectedMethod = self.methodTSL.selectItem[0]
    self.careStrategy = self.carerDic[ selectedMethod ]

  def selectResultItems( self ):
    selectedItems = self.resultTSL.selectItem

    if None != selectedItems:
      cmds.select( selectedItems , r=1 )

  def check( self ):
    self.results = []
    self.results = self.careStrategy.check( self.progressBar )
    self.setResults()

  def checkTotal( self ):
    self.results = []
    self.carerDic["Time Unit"].check()
    self.results += self.carerDic["Scale"].check( self.progressBar )
    self.results += self.carerDic["Name Double"].check( self.progressBar )
    self.results += self.carerDic["LocatorLocalPos"].check( self.progressBar )
    self.results += self.carerDic["Locator OB"].check( self.progressBar )
    self.results += self.carerDic["Locator MV"].check( self.progressBar )
    self.results += self.carerDic["Double MV Name"].check( self.progressBar )
    self.results += self.carerDic["InvalidAnimCurve"].check( self.progressBar )
    self.results += self.carerDic["HasWeightEndJoint"].check( self.progressBar )
    self.setResults()

  def setResults( self ):
    filteredResults = []

    for result in self.results:

      if u'【' in result:
        filteredResults.append( result )
        continue

      if u'|other|' in result.lower():
        continue

      if not self.aloneFilterCB.value:
        if '|Alone|' in result:
          continue
      if not self.cutFilterCB.value:
        if '|Cut|' in result:
          continue
      if not self.clothFilterCB.value:
        if '|Cloth|' in result:
          continue

      if None == self.isIncludeRootNodeRE.match( result ):
        continue

      filteredResults.append( result )

    self.resultTSL.set( filteredResults )



  def resetFrameRate( self ):
    cmds.currentUnit( time="ntsc" )

  def resetLocalPos( self ):
    selectedItems = cmds.ls( sl=1 , long=1 )

    ## 何も選択されていなければ、全体のロケーターが処理対象になる
    if [] == selectedItems:
      locatorShapes = cmds.ls( ":*" , type="locator" , l=1 )
    ## 選ばれていれば選択ロケーターが処理対象になる
    else:
      locatorShapes = cmds.listRelatives( selectedItems , children=1 , type="locator" , fullPath=1 )

    ## ロケータシェープが見つかれば処理する
    if None != locatorShapes:

      ## ロケーターシェープ単位の処理
      for locatorShape in locatorShapes:
        locatorTransform = cmds.listRelatives( locatorShape , parent=1 , type="transform" , fullPath=1 )[0]

        print "*****" * 5
        print 'Checking... [' , locatorTransform , ']'

        ## 子供を外しておく
        children = cmds.listRelatives( locatorTransform , children=1 , type='transform' , fullPath=1 )

        if children != None:
          movedChildren = cmds.parent( children , world=1 )

        ## ロケータのクリーンアップ
        translateAttr = geometry.MYAMVector3D( cmds.getAttr( locatorTransform + ".translate" )[0] )
        localPosition = geometry.MYAMVector3D( cmds.getAttr( locatorShape + ".localPosition" )[0] )
        globalPosition = geometry.MYAMVector3D( cmds.pointPosition( locatorTransform ) )

        cmds.setAttr( locatorShape + '.localPosition' , 0 , 0 , 0 , type='double3' )
        cmds.xform( locatorTransform , os=1 , r=1 , translation=localPosition.array )
        cmds.xform( locatorTransform , centerPivots=1 )
        cmds.xform( locatorTransform , ws=1 , a=1 , pivots=globalPosition.array )

        ## After check
        if locatorTransform.split( '|' )[-1] == "mv_top":
          if [( 0.0 , 0.0 , 0.0 )] != cmds.getAttr( locatorTransform + '.translate' ):
            print "!!!!!!!!!! [" , locatorTransform , "] has not default translate."

          if [( 0.0 , 0.0 , 0.0 )] != cmds.getAttr( locatorTransform + '.rotate' ):
            print "!!!!!!!!!! [" , locatorTransform , "] has not default rotate."

          if [( 1.0 , 1.0 , 1.0 )] != cmds.getAttr( locatorTransform + '.scale' ):
            print "!!!!!!!!!! [" , locatorTransform , "] has not default scale."

        ## 子を戻す
        if children != None:
          cmds.parent( movedChildren , locatorTransform )

        ## 初期選択状態を復帰
        if [] != selectedItems:
          cmds.select( selectedItems )

  def freezeScale( self ):
    cmds.makeIdentity( t=0 , r=0 , s=1 , a=1 )

  def progresBarTest( self ):
    self.progressBar.minValue = 0
    self.progressBar.maxValue = 1000

    self.progressBar.progress = 0

    for i in range( self.progressBar.maxValue ):
      self.progressBar.progress = i

    self.progressBar.endProgress = 1

  ## clean up & save

  def cleanUpSave( self ):
    self.createBackUp()

    self.deleteIntermediateNodes()
    self.deleteNondeformableHistory()

    self.cleanUpWindow()
    self.cleanUpDisplayLayer()
    self.cleaUpMaterial()

    self.changeWireframe()

    self.exportAssemblies()

  def deleteNondeformableHistory( self ):
    meshs = cmds.ls( dag=1 , type="mesh" )

    for mesh in meshs:
      if cmds.objExists( mesh ):
        cmds.select( mesh , r=1 )
        cmds.BakeNonDefHistory()
        print "[CLEANUP HISTORY]" , mesh

  def deleteIntermediateNodes( self ):
    meshs = cmds.ls( dag=1 , type="mesh" )

    for mesh in meshs:
      if cmds.getAttr( mesh + ".intermediateObject" ):
        connections = cmds.listConnections( mesh , s=0 , d=1 )
        if connections == None:
          print "[DELETE ALONE INTERMEDIATE]" , mesh
          cmds.delete( mesh )

  def cleanUpWindow( self ):
    allWindows = cmds.lsUI( windows=1 )

    protectWindows = [ "MayaWindow" , "ColorEditor" , "CommandWindow" , "scriptEditorPanel1Window" , "MYAM_sceneChecker_1" ]

    for window in allWindows:
      if not window in protectWindows:
        cmds.deleteUI( window )

  def cleaUpMaterial( self ):
    mel.eval( 'hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");' )

  def cleanUpDisplayLayer( self ):
    layers = cmds.ls( type="displayLayer" )

    protectLayers = [ "defaultLayer" ]

    for layer in layers:
      dstConnections = cmds.listConnections( layer , s=0 , d=1 )

      if not layer in protectLayers:
        if ( dstConnections == None ):
          cmds.delete( layer )

  def changeWireframe( self ):
    panels = cmds.lsUI( panels=1 )

    for panel in panels:
      panelType = cmds.objectTypeUI( panel )

      if panelType == "TmodelPane":
        cmds.modelEditor( panel , e=1 , displayAppearance="wireframe" , displayLights="default" )

  def createBackUp( self ):
    cmds.file( save=1 )

    scenePath = cmds.file( q=1 , sceneName=1 )

    lt = time.localtime()
    st = time.strftime( "%Y%m%d_%H%M" , lt )

    shutil.copy2( scenePath , scenePath + "_" + st )

  def exportAssemblies( self ):
    selfPath = cmds.file( q=1 , sceneName=1 )

    assemblies = cmds.ls( assemblies=1 )
    cmds.select( assemblies , r=1 )

    cmds.file( selfPath , f=1 , exportSelected=1 , preserveReferences=1 )

## Carer Classes

  def deleteInvalidAnimCurve( self ):
    animCurves = cmds.ls( type="animCurve" , long=1 )
    results = []

    for animCurve in animCurves:

      connectTargets = cmds.listConnections( "%s.output" % animCurve , s=0 , d=1 )
      if connectTargets == None:
        connectTargets = []

      for connectTarget in connectTargets:
        if "BG_camera" in connectTarget:
          continue

        cmds.delete( animCurve )

  def filterResults( self ):
    results = []
    return results



class AbstractCarer( object ):
  def __init__( self ):
    pass

  def getTargets( self ):
    pass

  def check( self ):
    pass

  def repair( self ):
    pass

class Carer_total( AbstractCarer ):

  def __init__( self ):
    AbstractCarer.__init__( self )

  def check( self , ProgressBar=None ):
    res = []

    res += self.carerDic["Time Unit"]
    res += self.carerDic["Scale"]
    res += self.carerDic["Name Double"]
    res += self.carerDic["LocatorLocalPos"]
    res += self.carerDic["Locator OB"]
    res += self.carerDic["Locator MV"]
    res += self.carerDic["Double MV Name"]
    res += self.carerDic["InvalidAnimCurve"]

    return res

class Carer_MV( AbstractCarer ):

  def __init__( self ):
    AbstractCarer.__init__( self )
    self.header = [ u" " , u"【mvロケータエラー --> mv_topの位置異常/子無し、mv_cltの親がcltであるか】"]

  def check( self , ProgressBar=None ):

    ## 全ロケータを取得してから、親トランスフォームを取得
    buf = cmds.ls( type="locator" )
    if [] == buf:
      raise ValueError , "Scene has not locator. Procces was canceled."

    allLocators = cmds.listRelatives( buf , parent=1 , type="transform" , fullPath=1 )

    ## 全ロケータを走査し、異常があれば取得
    errorLocators = []
    ProgressBar.maxValue = len( allLocators )

    for locator in allLocators:
      ProgressBar.step = 1

      ## 現在のロケータがOtherグループに含まれていれば無視
      if "|Other|" in locator:
        continue

      locatorName = locator.split( '|' )[-1]
      parent = cmds.listRelatives( locator , parent=1 , type="transform" )
      children = cmds.listRelatives( locator , children=1 , type="transform" )

      ## mv_ ロケータ以外を無視
      if "mv_" != locatorName[:3]:
        continue

      ## mv_topのチェック
      if "mv_top" == locatorName:
        localMatrix = [ float( "%.10f" % x ) for x in cmds.getAttr( locator + ".matrix" ) ]
        defaultMatrix = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]

        ## マトリクスチェック
        invalidMatrixFlag = False
        for ( lMatrixElem , dMatrixElem ) in zip( localMatrix , defaultMatrix ):
          if ( lMatrixElem < ( dMatrixElem - 0.0001 ) ) or ( ( dMatrixElem + 0.0001 ) < lMatrixElem ):
            errorLocators.append( locator )
            continue

        ## 子ジョイント有無チェック
        childJoints = cmds.listRelatives( locator , children=1 , type="joint" )
        if None != childJoints:
          errorLocators.append( locator )
          continue

        ## 子無しチェック
        if children == None:
          errorLocators.append( locator )
          continue

      ## 自身が 通常のmv_ロケーターの場合
      parentMVFlag = False
      childMVFlag = False
      selfMVFlag = False

      ## 現在ロケータに親がある場合
      if None != parent:
        ## 親の名前が mv_ 他規格で許されたタイプで始まっていなければFalse
        if "mv_" == parent[0][:3]:
          parentMVFlag = True

        elif "ob_" == parent[0][:3]:
          parentMVFlag = True

        elif "gp_" == parent[0][:3]:
          parentMVFlag = True

        elif "bs_" == parent[0][:3]:
          parentMVFlag = True

        elif "clt_" == parent[0][:4]:
          parentMVFlag = True

        elif "jnt_" == parent[0][:4]:
          parentMVFlag = True

        else:
          pass

      ## 現在ロケータに子がある場合
      if None != children:
        ## 子単位のチェック
        for child in children:
          ## 子の名前が mv_ で始まっていれば
          if "mv_" == child[0:3]:
            childMVFlag = True
            break

      ## 親か子にmvがあれば
      if not( parentMVFlag or childMVFlag ):
        errorLocators.append( locator )
        continue

    ProgressBar.endProgress = 1

    return self.header + errorLocators

class Carer_OB( AbstractCarer ):

  def __init__( self ):
    AbstractCarer.__init__( self )

    self.header = [ u" " , u"【OBロケータエラー --> ob内にobがある／直下にmv_topが無い】" ]

  def check( self , ProgressBar=None ):
    errorLocators = []

    buf = cmds.ls( type="locator" )
    if [] == buf:
      raise ValueError , "Scene has not obLocator. Procces was canceled."

    obLocators = self.fiterTargets( cmds.listRelatives( buf , parent=1 , type="transform" , fullPath=1 ) )

    ProgressBar.maxValue = len( obLocators )

    ## ロケータ単位の処理
    for obLocator in obLocators:
      ProgressBar.step = 1

      childTransforms = cmds.listRelatives( obLocator , children=1 , fullPath=1 , type="transform" )
      if childTransforms == None:
        childTransforms = []

      childConstraints = cmds.listRelatives( obLocator , children=1 , fullPath=1 , type="constraint" )
      if childConstraints == None:
        childConstraints = []
      
      childJoints = cmds.listRelatives( obLocator , children=1 , fullPath=1 , type="joint" )
      if childJoints == None:
        childJoints = []

      childTransforms = cmds.listRelatives( obLocator , children=1 , fullPath=1 , type="transform" )
      if childTransforms == None:
        childTransforms = []
      else:
        childTransforms = sorted( list( set( childTransforms ) - ( set( childConstraints ) ) ) )

      '''子供チェック'''
      if 0 == len( childTransforms ):
        '''子なし'''
        errorLocators.append( obLocator )

      elif ( 1 == len( childTransforms ) ):
        '''一人っ子'''
        if "mv_top" == childTransforms[0][-6:]:
          continue
        
        elif "joint" == cmds.nodeType( childTransforms[0] ):
          continue
        
        else:
          errorLocators.append( obLocator )
          continue

      else:
        '''一人っ子で無い場合'''
        errorLocators.append( obLocator )

    ProgressBar.endProgress = 1

    return self.header + sorted( list( set( errorLocators ) ) )

  def hasChildByType( self, node , nodeType ):
    children = cmds.listRelatives( node , children=1 , fullPath=1 , type=nodeType )
    if None == children:
      return False
    else:
      return True

  def hasChildByName( self, node, childName ):
    children = cmds.listRelatives( node , children=1 , fullPath=1 )

    for child in children:
      splitChild = child.split( "|" )
      if childName == splitChild[-1]:
        return True

    return True

  def fiterTargets( self , obLocatorPaths ):
    filteredOBLocators = []

    for obLocatorPath in obLocatorPaths:
      locatorName = obLocatorPath.split( '|' )[-1]

      ## 現在のロケータがOtherグループに含まれていれば無視
      if "|Other|" in obLocatorPath:
        continue

      ## obロケータ以外は無視
      elif "ob_" != locatorName[:3]:
        continue

      else:
        filteredOBLocators.append( obLocatorPath )

    return filteredOBLocators


class Carer_Scale( AbstractCarer ):

  def __init__( self ):
    AbstractCarer.__init__( self )

    self.header = [ u" " , u"【スケールエラー --> スケールが等倍ではない】" ]

  def check( self , ProgressBar=None ):
    allDagNodes = cmds.ls( dagObjects=1 , long=1 )

    errorDagNodes = []

    ProgressBar.maxValue = len( allDagNodes )

    for dagNode in allDagNodes:
      ProgressBar.step = 1

      ## 現在のロケータがOtherグループに含まれていれば無視
      if "|Other|" in dagNode:
        continue

      ##
      existScaleFlag = cmds.attributeQuery( "scale" , node=dagNode , exists=1 )

      if existScaleFlag:
        scale = cmds.getAttr( dagNode + ".scale" )[0]

        scaleX = myamMath.roundOffFloat( scale[0] , 3 )
        scaleY = myamMath.roundOffFloat( scale[1] , 3 )
        scaleZ = myamMath.roundOffFloat( scale[2] , 3 )

        if ( 1.0 , 1.0 , 1.0 ) != ( scaleX , scaleY , scaleZ ):
          errorDagNodes.append( dagNode )

    ProgressBar.endProgress = 1

    return self.header + errorDagNodes

class Carer_DoubleName( AbstractCarer ):
  def __init__( self ):
    AbstractCarer.__init__( self )

    self.header = [u" " , u"【重複名エラー --> obロケーター名の重複】"]

  def check( self , ProgressBar=None ):
    locatorShapes = cmds.ls( type='locator' )
    locatorTransforms = cmds.listRelatives( locatorShapes , parent=1 , type='transform' , fullPath=1 )

    ## エラーロケータの抽出
    errorDagNodes = []

    ProgressBar.maxValue = len( locatorTransforms )

    for locatorTransform in locatorTransforms:
      ProgressBar.step = 1

      ## 現在のロケータがOtherグループに含まれていれば無視
      if "|Other|" in locatorTransform:
        continue

      ##
      lastNode = locatorTransform.split( "|" )[-1]

      if "ob_" == lastNode[:3]:
        sameNames = cmds.ls( lastNode , l=1 )

        for sameName in sameNames:
          if locatorTransform == sameName:
            continue
          elif "|Other|" in sameName:
            continue
          else:
            errorDagNodes.append( locatorTransform )

    ProgressBar.endProgress = 1

    return self.header + sorted( errorDagNodes )

class Carer_Hierarchy( AbstractCarer ):
  def __init__( self ):
    AbstractCarer.__init__( self )

    self.header = [u" " , u"【階層比較エラー --> 二つの階層構造が違う】"]

  def check( self , ProgressBar=None ):
    selectedItems = cmds.ls( sl=1 )

    if 2 != len( selectedItems ):
      raise ValueError , "Selection num is not two items"

    srcRoot = selectedItems[0]
    dstRoot = selectedItems[1]

    srcDescendents = cmds.listRelatives( srcRoot , allDescendents=1 , fullPath=1 )
    dstDescendents = cmds.listRelatives( dstRoot , allDescendents=1 , fullPath=1 )

    srcSplitDescendentDic = {}
    dstSplitDescendentDic = {}

    srcErrorDagNodes = set( [] )
    dstErrorDagNodes = set( [] )

    errorDagNodes = []

    for descendent in srcDescendents:
      srcSplitDescendentDic[ descendent.split( srcRoot )[-1] ] = descendent

    for descendent in dstDescendents:
      dstSplitDescendentDic[ descendent.split( dstRoot )[-1] ] = descendent

    for srcSplit in srcSplitDescendentDic.keys():
      if not srcSplit in dstSplitDescendentDic.keys():
        srcErrorDagNodes.add( srcSplitDescendentDic[srcSplit] )

    for dstSplit in dstSplitDescendentDic.keys():
      if not dstSplit in srcSplitDescendentDic.keys():
        dstErrorDagNodes.add( dstSplitDescendentDic[dstSplit] )

    errorDagNodes = list( srcErrorDagNodes.union( dstErrorDagNodes ) )

    return self.header + sorted( errorDagNodes )

class Carer_VertexColor( AbstractCarer ):
  def __init__( self ):
    AbstractCarer.__init__( self )

    self.header = [u" " , u"【メッシュエラー --> 設定済み／未設定頂点カラーが混在】"]

  def check( self , ProgressBar=None ):

    ## 開始時の選択リストを作成
    selectedItems = cmds.ls( sl=1 )

    ## 全体のメッシュを選択
    cmds.select( cmds.ls( type="mesh" ) , r=1 )

    ProgressBar.maxValue = len( selectedItems )

    ##
    import maya.OpenMaya as OpenMaya

    selList = OpenMaya.MSelectionList()
    OpenMaya.MGlobal_getActiveSelectionList( selList )

    ## if Needs components Use type define. if no define can get node
    selIter = OpenMaya.MItSelectionList( selList , OpenMaya.MFn.kMesh )

    meshObj = OpenMaya.MObject()
    meshFn = OpenMaya.MFnMesh()

    dagPath = OpenMaya.MDagPath()

    errorShapes = []
    errorVts = []

    while not selIter.isDone():
      ProgressBar.step = 1

      ## 現在アイテムのパスをdagPathにセット
      selIter.getDagPath( dagPath , meshObj )

      ## 現在のロケータがOtherグループに含まれていれば無視
      if "|Other|" in dagPath.fullPathName():
        selIter.next()
        continue

      ## dagPathに格納されたアイテムがメッシュでなければdagPathの中身をtransformからshapeに変換
      if dagPath.apiType != OpenMaya.MFn.kMesh:
        dagPath.extendToShape()

      meshIter = OpenMaya.MItMeshVertex( dagPath.node() )
      hasColorFlag = meshIter.hasColor()

      while not meshIter.isDone():
        if hasColorFlag != meshIter.hasColor():
          errorShapes.append( dagPath.fullPathName() )
          break

        meshIter.next()

      selIter.next()

    ## 開始時点の選択状態を復帰
    if selectedItems != []:
      cmds.select( selectedItems , r=1 )

    ProgressBar.endProgress = 1

    ## 結果を返す
    if errorShapes != []:
      return self.header + cmds.listRelatives( errorShapes , parent=1 , type="transform" , fullPath=1 )
    else:
      return self.header

class Carer_TimeUnit( AbstractCarer ):
  def __init__( self ):
    AbstractCarer.__init__( self )

  def check( self , ProgressBar=None ):
    currentTimeUnit = cmds.currentUnit( q=1 , time=1 )

    if currentTimeUnit != "ntsc":
    	cmds.confirmDialog( title=u"タイムユニットエラー" , message=u"タイムユニットがntsc[30fps]ではありません。" )

    return []

class Carer_LocatorLocalPosition( AbstractCarer ):
  def __init__( self ):
    AbstractCarer.__init__( self )

    self.header = [ u" " , u"【ロケータエラー --> ローカルポジションがデフォルト値ではない】" ]

  def check( self , ProgressBar=None ):
    locatorShapes = cmds.ls( type="locator" , long=1 )
    results = []

    ProgressBar.maxValue = len( locatorShapes )

    ##
    for locatorShape in locatorShapes:
      ProgressBar.step = 1

      ## 現在のロケータがOtherグループに含まれていれば無視
      if "|Other|" in locatorShape:
        continue

      localPosition = [ float( "%.8f" % x ) for x in cmds.getAttr( locatorShape + ".localPosition" )[0] ]

      if localPosition != [ 0.0, 0.0, 0.0 ]:
        locatorTransform = cmds.listRelatives( locatorShape , parent=1 , type='transform' , fullPath=1 )
        results.append( locatorTransform[0] )

    ProgressBar.endProgress = 1

    return self.header + results

class Carer_DoubleMVName( AbstractCarer ):
  def __init__( self ):
    AbstractCarer.__init__( self )

    self.header = [ u" " , u"【mvロケータ名重複エラー --> 指定したob内に重複する名前を持つmvロケータがあります】" ]

  def check( self , ProgressBar=None ):
    results = []

    '''とりあえず、選択しているobロケータを取得。何も選択してなければシーン内の全obロケータ取得'''
    obLocators = cmds.ls( "ob_*" , sl=1 , type='transform' , l=1 )
    if obLocators == []:
      obLocators = cmds.ls( "ob_*" , type='transform' , l=1 )

    errorMVLocatorPaths = []

    '''mvロケータに関する辞書組み立て'''
    ProgressBar.progress = 0
    ProgressBar.maxValue = len( obLocators )

    for obLocator in obLocators:
      ProgressBar.step = 1

      trueOBName = obLocator.split( '|' )[-1]

      foundMVLocatorDic = {}

      ''''''
      descendents = cmds.listRelatives( obLocator , allDescendents=1 , fullPath=1 , type='transform' )

      '''子孫無しはスキップ'''
      if None == descendents:
        continue

      for descendent in descendents:
        lastNode = descendent.split( '|' )[-1]

        if "mv_" == lastNode[:3]:
          if lastNode in foundMVLocatorDic.keys():
            foundMVLocatorDic[lastNode].append( descendent )
          else:
            foundMVLocatorDic[lastNode] = [ '-' * 60 , trueOBName , descendent ]

      '''mvロケータ辞書から出力する情報を組み立て'''
      for key in sorted( foundMVLocatorDic.keys() ):
        value = sorted( list( set( foundMVLocatorDic[ key ] ) ) )

        if 4 <= len( value ):
          results += value

    ProgressBar.endProgress = 1

    ''''''
    return self.header + results

## 実際のチェック関数群

class Carer_InvalidAnimCurve( AbstractCarer ):
  def __init__( self ):
    AbstractCarer.__init__( self )

    self.header = [ u" " , u"【animCurveが存在しています】" ]

  def check( self , ProgressBar=None ):
    animCurves = cmds.ls( type="animCurve" , long=1 )
    results = []

    ProgressBar.maxValue = len( animCurves )

    for animCurve in animCurves:
      ProgressBar.step = 1

      connectTargets = cmds.listConnections( "%s.output" % animCurve , s=0 , d=1 )
      if connectTargets == None:
        connectTargets = []

      for connectTarget in connectTargets:
        targetPath = cmds.ls( connectTarget , l=1 )

        if "BG_camera" in connectTarget:
          continue

        results += targetPath

    results = sorted( list( set( results ) ) )

    ProgressBar.endProgress = 1

    return self.header + results

class Carer_hasWeightEndJoint( AbstractCarer ):
  def __init__( self ):
    AbstractCarer.__init__( self )

    self.header = [ u" " , u"【末端ジョイントがskinWeight値を持っています】" ]

  def check( self , ProgressBar=None ):
    leafJoints = cmds.ls( type="joint" , long=1 , dag=1 , leaf=1 )
    errorJoints = []

    ProgressBar.maxValue = len( leafJoints )

    ## 末端ジョイント単位の処理
    for leafJoint in leafJoints:
      ProgressBar.step = 1

      lastName = leafJoint.split( "|" )[-1]

      ## 末端ジョイントが dmy ジョイントの場合のみウエイトチェック
      if "dmy_" == lastName[:4]:

        ## コネクトされたスキンクラスタがあるか
        connectedSkinClusters = cmds.listConnections( leafJoint , type="skinCluster" )
        if None != connectedSkinClusters:

          ## スキンクラスタ単位処理
          for connectedSkinCluster in connectedSkinClusters:

            ## スキンクラスタにメッシュがコネクトされてるか
            connectedMeshs = cmds.listConnections( connectedSkinClusters , type="mesh" )
            if None != connectedMeshs:

              ## メッシュ単位処理
              for mesh in connectedMeshs:
                vts = cmds.ls( mesh + ".vtx[*]" , flatten=1 )

                ## 頂点単位処理
                for vtx in vts:
                  weight = cmds.skinPercent( connectedSkinCluster , vtx , transform=leafJoint , query=True, value=True )

                  if 0.0 != float( "%.4f" % weight ):
                    errorJoints.append( leafJoint )

    ProgressBar.endProgress = 1

    return self.header + errorJoints




## Imported message
print "MODULE IMPORTED... MYAM_sceneChecker_main"
