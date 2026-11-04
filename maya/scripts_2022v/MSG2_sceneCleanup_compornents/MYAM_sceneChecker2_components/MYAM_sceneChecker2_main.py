#-*- coding:UTF-8 -*-

#*******************************************************************************
'''

Tool Name     : MYAM_sceneChecker2_main
Description   : シーンデータエラーチェックツールのメインモジュール

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

import maya.cmds         as cmds
import maya.mel          as mel
import maya.OpenMaya     as OpenMaya
import maya.OpenMayaAnim as OpenMayaAnim

import os
import re
import decimal
import time
import locale

import MayaUI
reload( MayaUI )

import MYAM_PyLib_geometry as geometry
reload( geometry )

import MYAM_PyLib_math as myamMath
reload( myamMath )

#import EclipseDebugger
#eclipseDebugger = EclipseDebugger.EclipseDebugger()





""""""
class MainWindow( object ):

  def __init__( self , **kwargs ):
    self.errorChecker = ErrorChecker()
    self.errorRepairer = ErrorRepairer()

    self.results = []
    self.resultBlocks = []

    self.createUI()
    self.layoutUI()

    self.setUIContents()

    self.createScriptJobs()

    self.checkFunctions = [ self.errorChecker.checkInvalidFrameRate ,
                            self.errorChecker.checkInvalidScale ,
                            self.errorChecker.checkAnimCurveConnection ,
                            self.errorChecker.checkInvalidVertexColor ,

                            self.errorChecker.checkJoint_WeightedDmy ,
                            self.errorChecker.checkJoint_OverMaxInfluence ,
                            self.errorChecker.checkJoint_NoWaigtedAndHasNotChildren ,

                            self.errorChecker.checkDoubleNameNotSameCase ,

                            self.errorChecker.checkJoint_DoubleNameInOBTree ,

                            self.errorChecker.checkAllLocator_LocalPosition ,

                            self.errorChecker.checkMV_DoubleNameInOBTree ,

                            self.errorChecker.checkMV_InvalidMatrix ,

                            self.errorChecker.checkOB_DoubleName ,
                            self.errorChecker.checkOB_TooManyOBLocators ,
                            self.errorChecker.checkOB_ValidChildNode ,
                            self.errorChecker.checkOB_HasMVMoveOrMVBase ]

  def createUI( self ):
    ''''''
    self.window = MayaUI.WindowEx( "MYAM_sceneChecker2_#" )

    ''''''
    self.rootLayout = MayaUI.FormLayoutEx()

    ''''''
    self.topAreaCLo = MayaUI.ColumnLayout()

    self.totalCheckBT = MayaUI.Button()
    self.progressBar = MayaUI.ProgressBar()

    self.repairButtonsHULo = MayaUI.HUniformLayout()
    self.repairPlaybackFramerateBT = MayaUI.Button()
    self.repairLocatorLocalPositionBT = MayaUI.Button()
    self.repairDAGScaleBT = MayaUI.Button()
    self.repairVertexColorBT = MayaUI.Button()
    self.repairInvalidAnimCurveBT = MayaUI.Button()
    self.repairButtonsHULo.arrange()
    cmds.setParent( ".." ) ## End of self.repairButtonsRLo

    MayaUI.Separator()
    MayaUI.Separator()
    MayaUI.Separator()

    self.frameControlHULo = MayaUI.HUniformLayout()
    self.allCollapseFramesBT = MayaUI.Button()
    self.allExpandFramesBT = MayaUI.Button()
    self.expandErrorFramesBT = MayaUI.Button()
    self.frameControlHULo.arrange()
    cmds.setParent( ".." ) ## End of self.repairButtonsRLo

    self.resultFilterHULo = MayaUI.HUniformLayout()
    self.filterTX = MayaUI.Text()
    self.filterAloneCB = MayaUI.CheckBox()
    self.filterCutCB = MayaUI.CheckBox()
    self.filterClochCB = MayaUI.CheckBox()
    self.resultFilterHULo.arrange()
    cmds.setParent( ".." ) ## End of self.repairButtonsRLo

    cmds.setParent( ".." ) ## End of self.topAreaCLo

    ''''''
    self.bottomAreaSLo = MayaUI.ScrollLayout( childResizable=1 )
    self.resultsCLo = MayaUI.ColumnLayout()
    cmds.setParent( ".." ) ## End of self.resultsCLo
    cmds.setParent( ".." ) ## End of self.bottomAreaSLo

  def layoutUI( self ):
    self.window.title = "MYAM_sceneChecker2"
    self.window.width = 566
    self.window.height = 600
    self.window.resizeToFitChildren = 1

    self.rootLayout.af = [ ( self.topAreaCLo.name , "top"   , 0 ) ,
                           ( self.topAreaCLo.name , "left"  , 0 ) ,
                           ( self.topAreaCLo.name , "right" , 0 ) ]

    self.rootLayout.ac = [ ( self.bottomAreaSLo.name , "top"    , 0 , self.topAreaCLo.name ) ]
    self.rootLayout.af = [ ( self.bottomAreaSLo.name , "bottom" , 0 ) ,
                           ( self.bottomAreaSLo.name , "left"   , 0 ) ,
                           ( self.bottomAreaSLo.name , "right"  , 0 ) ]

    self.topAreaCLo.adjustableColumn = 1

    self.bottomAreaSLo.childResizable = 1

    self.resultsCLo.adjustableColumn = 1

  def setUIContents( self ):
    ## Labels
    mayaUILanguage = getCurrentLocale()

    if "ja_JP" == mayaUILanguage:
      self.totalCheckBT.label = u'一括チェック'

      self.repairPlaybackFramerateBT.label = u'フレームレートを30fps'
      self.repairLocatorLocalPositionBT.label = u'localPositionをリセット'
      self.repairDAGScaleBT.label = u'scaleをリセット'
      self.repairVertexColorBT.label = u'vertexColorを埋める'
      self.repairInvalidAnimCurveBT.label = u'animCurveを削除する'

      self.allCollapseFramesBT.label = u'全てたたむ'
      self.allExpandFramesBT.label = u'全て展開する'
      self.expandErrorFramesBT.label = u'問題のある項目のみ展開'

      self.filterTX.label = u'結果フィルタ'
      self.filterAloneCB.label = u'alone階層を含める'
      self.filterCutCB.label = u'cut階層を含める'
      self.filterClochCB.label = u'cloth階層を含める'

    else:
      self.totalCheckBT.label = 'Total check'

      self.repairPlaybackFramerateBT.label = 'Set 30fps'
      self.repairLocatorLocalPositionBT.label = 'Reset localPosition'
      self.repairDAGScaleBT.label = 'Reset scale'
      self.repairVertexColorBT.label = 'Fill vertexColor'
      self.repairInvalidAnimCurveBT.label = 'Delete animCurve'

      self.allCollapseFramesBT.label = 'Collapse all'
      self.allExpandFramesBT.label = 'Expand all'
      self.expandErrorFramesBT.label = 'Expand error'

      self.filterTX.label      = 'Filter Results'
      self.filterAloneCB.label = 'Alone'
      self.filterCutCB.label   = 'Cut'
      self.filterClochCB.label = 'Cloth'

    ## Callbacks
    self.totalCheckBT.command = self.pushTotalCheckBT

    self.repairPlaybackFramerateBT.command = self.pushrepairPlaybackFramerateBT
    self.repairLocatorLocalPositionBT.command = self.pushrepairLocatorLocalPositionBT
    self.repairDAGScaleBT.command = self.pushrepairDAGScaleBT
    self.repairVertexColorBT.command = self.pushrepairVertexColorBT
    self.repairInvalidAnimCurveBT.command = self.pushrepairInvalidAnimCurveBT

    self.allCollapseFramesBT.command = self.pushallCollapseFramesBT
    self.allExpandFramesBT.command = self.pushallExpandFramesBT
    self.expandErrorFramesBT.command = self.pushexpandErrorFramesBT

    self.filterAloneCB.changeCommand = self.changeFilterCBs
    self.filterCutCB.changeCommand = self.changeFilterCBs
    self.filterClochCB.changeCommand = self.changeFilterCBs

    ## Values
    self.filterAloneCB.value = 1
    self.filterCutCB.value = 1
    self.filterClochCB.value = 1

    ## Others
    self.totalCheckBT.height *= 2
    self.totalCheckBT.backgroundColor = [0.4, 0.4, 0.4]

    self.filterTX.align = 'center'

  def createScriptJobs( self ):
    pass

  def setMayaMessage( self ):
    command = 'MYAM_sceneChecker2_autoCheckTotal();'
    self.MMA.setCallback( "BeforeSave" , command , 0 )

  def show( self ):
    self.window.show()

    self.totalCheck()
    self.createResults()

    self.forceResizeWindow()

  ''''''
  def pushTotalCheckBT( self , *args , **kwargs ):
    self.totalCheck()
    self.createResults()
    self.forceResizeWindow()

  ''''''
  def pushrepairPlaybackFramerateBT( self , *args , **kwargs ):
    try:
      cmds.undoInfo( openChunk=1 )
      self.errorRepairer.repairPlaybackFramerate()
    finally:
      cmds.undoInfo( closeChunk=1 )

  def pushrepairLocatorLocalPositionBT( self , *args , **kwargs ):
    try:
      cmds.undoInfo( openChunk=1 )
      self.errorRepairer.repairLocatorLocalPosition()
    finally:
      cmds.undoInfo( closeChunk=1 )

  def pushrepairDAGScaleBT( self , *args , **kwargs ):
    try:
      cmds.undoInfo( openChunk=1 )
      self.errorRepairer.repairDAGScale()
    finally:
      cmds.undoInfo( closeChunk=1 )

  def pushrepairVertexColorBT( self , *args , **kwargs ):
    try:
      cmds.undoInfo( openChunk=1 )
      self.errorRepairer.repairVertexColor()
    finally:
      cmds.undoInfo( closeChunk=1 )

  def pushrepairInvalidAnimCurveBT( self , *args , **kwargs ):
    try:
      cmds.undoInfo( openChunk=1 )
      self.errorRepairer.repairInvalidAnimCurve()
    finally:
      cmds.undoInfo( closeChunk=1 )

  ''''''
  def pushallCollapseFramesBT( self , *args , **kwargs ):
    self.collapseAllFrames()
    self.forceResizeWindow()

  def pushallExpandFramesBT( self , *args , **kwargs ):
    self.expandAllFrames()
    self.forceResizeWindow()

  def pushexpandErrorFramesBT( self , *args , **kwargs ):
    self.expandErrorFrames()
    self.forceResizeWindow()

  ''''''
  def changeFilterCBs( self , *args , **kwargs ):
    self.filterResults()

  ''''''
  def totalCheck( self ):
    self.results = []

    ''''''
    self.progressBar.maxValue = len( self.checkFunctions )

    for checkFunction in self.checkFunctions:
      ## 時間計測スタート
      startTime = time.time()

      self.progressBar.step = 1

      checkResult = checkFunction()
      self.results.append( checkResult )

      ## 時間計測エンド
      endTime = time.time()

      ## かかった時間を表示
      print "*****" * 10
      print checkResult.title
      duration = endTime - startTime
      print duration , "[s]"

    self.progressBar.endProgress = 1

  def createResults( self ):
    '''結果表示エリアを非表示化'''
    self.resultsCLo.visible = 0

    '''結果がすでに表示されていれば削除'''
    resultBlocks = self.resultsCLo.childArray
    if None != resultBlocks:
      for resultBlock in resultBlocks:
        cmds.deleteUI( resultBlock )

    '''結果ブロックを作りなおす'''
    self.resultBlocks = []
    cmds.setParent( self.resultsCLo.name )

    for result in self.results:
      if result == None:
        continue
      else:
        if result.funcName == "checkJoint_OverMaxInfluence":
          self.resultBlocks.append( ResultBlock_checkJoint_OverMaxInfluence( result.title , result.errors ) )
        else:
          self.resultBlocks.append( ResultBlock( result.title , result.errors ) )

    '''結果を作成し終えてからエリアを表示'''
    self.resultsCLo.visible = 1

  def filterResults( self ):
    '''結果表示エリアを非表示化'''
    self.resultsCLo.visible = 0

    for resultBlock in self.resultBlocks:
      resultBlock.setResultTSL( self.filterAloneCB.value , self.filterCutCB.value , self.filterClochCB.value )
      resultBlock.resizeResultTSL()
      resultBlock.changeFrameLabelColor()
      resultBlock.changeCollapseStatus()

    '''結果を作成し終えてからエリアを表示'''
    self.resultsCLo.visible = 1

  ''''''
  def forceResizeWindow( self ):
    self.window.height += 1
    self.window.height -= 1

  def expandAllFrames( self ):
    for resultBlock in self.resultBlocks:
      resultBlock.rootLayout.collapse = 0

  def expandErrorFrames( self ):
    for resultBlock in self.resultBlocks:
      errors = resultBlock.resultsTSL.allItems
      if None == errors:
        resultBlock.rootLayout.collapse = 1
      else:
        resultBlock.rootLayout.collapse = 0

  def collapseAllFrames( self ):
    for resultBlock in self.resultBlocks:
      resultBlock.rootLayout.collapse = 1

class BGSceneCheckerWindow( MainWindow ):
  def __init__( self , *args , **kwargs ):
    MainWindow.__init__( self , *args , **kwargs )

    self.checkFunctions = [ self.errorChecker.checkInvalidFrameRate ,
                            self.errorChecker.checkInvalidScale ,
                            self.errorChecker.checkAnimCurveConnection ,
                            self.errorChecker.checkInvalidVertexColor ,

                            self.errorChecker.checkJoint_WeightedDmy ,
                            self.errorChecker.checkJoint_OverMaxInfluence ,
                            self.errorChecker.checkJoint_NoWaigtedAndHasNotChildren ,

                            self.errorChecker.checkDoubleNameNotSameCase ,

                            self.errorChecker.checkJoint_DoubleNameInOBTree ,

                            self.errorChecker.checkAllLocator_LocalPosition ,

                            self.errorChecker.checkMV_DoubleNameInOBTree ,

                            self.errorChecker.checkMV_InvalidMatrix ,

                            self.errorChecker.checkOB_DoubleName ,
                            self.errorChecker.checkOB_TooManyOBLocators ,
                            self.errorChecker.checkOB_ValidChildNode ,
                            self.errorChecker.checkOB_HasMVMoveOrMVBase ]

    self.window.title = "Puppeteer - MYAM_BGSceneChecker"


class DemoSceneCheckerWindow( MainWindow ):
  def __init__( self , *args , **kwargs ):
    MainWindow.__init__( self , *args , **kwargs )

    self.checkFunctions = [ self.errorChecker.checkOBJ_changeReferenceNoGameObjects ]

    self.window.title = "Puppeteer - MYAM_DemoSceneChecker"


""""""
class ExtendMScriptUtil( OpenMaya.MScriptUtil ):
  def __init__( self , *args , **kwargs ):
    OpenMaya.MScriptUtil.__init__( self , *args , **kwargs )

  @staticmethod
  def nameListToMSelectionList( names ):
    selectionList = OpenMaya.MSelectionList()

    for name in names:
      selectionList.add( name )

    return selectionList

class NodeFinder( object ):
  def __init__( self , *args , **kwargs ):
    pass

  def getCheckTargets( self , root ):
    pass

""""""
class ResultBlock( object ):

  def __init__( self , title="" , lines=[] ):
    self.title = title
    self.lines = lines

    self.createUI()
    self.layoutUI()
    self.setUIContents()
    self.createScriptJobs()

  def createUI( self ):
    self.rootLayout = MayaUI.FrameLayout()

    self.contentsCLo = MayaUI.ColumnLayout()
    self.selectAllBT = MayaUI.Button()
    self.resultsTSL = MayaUI.TextScrollListEx()

    MayaUI.Separator()
    MayaUI.Separator()
    MayaUI.Separator()

    cmds.setParent( ".." )

    cmds.setParent( ".." )

  def layoutUI( self ):
    self.contentsCLo.adjustableColumn = 1

  def setUIContents( self ):
    self.rootLayout.collapsable = 1
    self.rootLayout.label = self.title

    self.selectAllBT.label = 'Select All'
    self.selectAllBT.command = self.pushselectAllBT
    self.selectAllBT.visible = 1

    ''''''
    self.resultsTSL.allowMultiSelection = 1
    self.resultsTSL.selectCommand = self.selectResultsTSL

    self.setResultTSL()
    self.resizeResultTSL()
    self.changeFrameLabelColor()
    self.changeCollapseStatus()

  def createScriptJobs( self ):
    pass

  ''''''
  def pushselectAllBT( self , *args , **kwargs ):
    self.selectAll()
    self.selectResultItem()

  def selectResultsTSL( self , *args , **kwargs ):
    self.selectResultItem()

  ''''''
  def selectAll( self ):
    self.resultsTSL.selectItem = self.resultsTSL.allItems

  def selectResultItem( self ):
    selectedItems = self.resultsTSL.selectItem
    cmds.select( selectedItems , r=1 )

  def setResultTSL( self , showAlone=1 , showCut=1 , showCloth=1 ):
    filteredLines = []
    self.resultsTSL.clear()

    for line in self.lines:
      lowerLine = line.lower()

      '''フィルタ処理'''
      if not ( ( "|alone|" in lowerLine ) or ( "|cut|" in lowerLine ) or ( "|cloth|" in lowerLine ) ):
        filteredLines.append( line )

      elif ( "|alone|" in lowerLine ) and showAlone:
        filteredLines.append( line )

      elif ( "|cut|" in lowerLine ) and showCut:
        filteredLines.append( line )

      elif ( "|cloth|" in lowerLine ) and showCloth:
        filteredLines.append( line )

      else:
        pass

    filteredLines = list( set( filteredLines ) )
    filteredLines.sort( cmp=lambda a, b : cmp( a.lower() , b.lower() ) )

    self.resultsTSL.set( filteredLines )

  def resizeResultTSL( self ):
    if None != self.resultsTSL.allItems:
      self.resultsTSL.numberOfRows = len( self.resultsTSL.allItems )
    else:
      self.resultsTSL.numberOfRows = 1

  def changeFrameLabelColor( self ):
    if None != self.resultsTSL.allItems:
      self.rootLayout.backgroundColor = [ 1.000 , 0.734 , 0.838 ]
    else:
      self.rootLayout.backgroundColor = [ 0.791 , 0.939 , 1.000 ]

  def changeCollapseStatus( self ):
    if None != self.resultsTSL.allItems:
      self.rootLayout.collapse = 0
    else:
      self.rootLayout.collapse = 1

class ResultBlock_checkJoint_OverMaxInfluence( ResultBlock ):
  def __init__( self , title="" , lines=[] ):
    ResultBlock.__init__( self , title=title , lines=lines )

  def selectResultItem( self ):
    exScriptUtil = ExtendMScriptUtil()

    selectedItems = self.resultsTSL.selectItem
    if None == selectedItems:
      selectedItems = []

##    skinClusters        = cmds.ls( type="skinCluster" )
    skinClustersSelList = exScriptUtil.nameListToMSelectionList( selectedItems )

    errorVertsSelectionList = OpenMaya.MSelectionList()

    for i in range( skinClustersSelList.length() ):
      currentSkinClusterNode = OpenMaya.MObject()
      skinClustersSelList.getDependNode( i , currentSkinClusterNode )

      mFnSkinCluster = OpenMayaAnim.MFnSkinCluster( currentSkinClusterNode )
      influenceDagPathArray = OpenMaya.MDagPathArray()
      mFnSkinCluster.influenceObjects( influenceDagPathArray )

      for j in range( influenceDagPathArray.length() ):
        currentInfluenceDagPath = influenceDagPathArray[j]
        affectedShapes = OpenMaya.MSelectionList()
        skinWeights = OpenMaya.MDoubleArray()
        mFnSkinCluster.getPointsAffectedByInfluence( currentInfluenceDagPath , affectedShapes , skinWeights )

        numOutputConnections = mFnSkinCluster.numOutputConnections()
        for k in range( numOutputConnections ):
          currentIndex = mFnSkinCluster.indexForOutputConnection( k )
          currentAffectedShapeDagPath = OpenMaya.MDagPath()
          mFnSkinCluster.getPathAtIndex( currentIndex , currentAffectedShapeDagPath )

          mItGeometry = OpenMaya.MItGeometry( currentAffectedShapeDagPath )
          while not mItGeometry.isDone():
            currentVertex = mItGeometry.currentItem()
            skinWeights = OpenMaya.MDoubleArray()
            influenceCountPtr = OpenMaya.MScriptUtil().asUintPtr()
            mFnSkinCluster.getWeights( currentAffectedShapeDagPath , currentVertex , skinWeights , influenceCountPtr )

            weightedCount = 0
            for skinWeight in skinWeights:
              if 0.0 < skinWeight:
                weightedCount += 1

            if 4 < weightedCount:
              errorVertsSelectionList.add( currentAffectedShapeDagPath , currentVertex )

            mItGeometry.next()

    OpenMaya.MGlobal_clearSelectionList()
    OpenMaya.MGlobal_setActiveSelectionList( errorVertsSelectionList )

class ErrorChecker( object ):
  def __init__( self ):
    self.innerRouteRE    = re.compile( "[|]a[0-9]*_[A-Z0-9]*_root.*" )
    self.innerRefRouteRE = re.compile( "[|]BG_set:a[0-9]*_[A-Z0-9]*_root.*" )
    self.mvLocatorNameRE = re.compile( "mv_[a-zA-Z0-9_]*" )
    self.obLocatorNameRE = re.compile( "ob_[a-zA-Z0-9_]*" )

    self.numberRE = re.compile( "[0-9.-]" )

    self.arrayCorrecter = ArrayCorrecter()
    self.dataCorrecter = DataCorrecter()

    self.mayaUILanguage = getCurrentLocale()

  '''一括共通チェック項目'''
  def isCheckTarget( self , nodePath ):
    if None != self.innerRouteRE.match( nodePath ):

      if not "|Other|" in nodePath:
        return True

    return False

  def isDAGNode( self , node ):
    pass

  ''''''
  def checkInvalidFrameRate( self ):
    checkResult = CheckResultData()

    currentTimeUnit = cmds.currentUnit( q=1 , time=1 )

    if "ja_JP" == self.mayaUILanguage:
      checkResult.title = u'再生フレームレートが30fps(ntsc)ではない'

      if currentTimeUnit != "ntsc":
        checkResult.errors.append( u"必ず、真っ先に修正してください！！！" )

    else:
      checkResult.title = u'Current playback framerate is not 30 fps.'

      if currentTimeUnit != "ntsc":
        checkResult.errors.append( u"Please be sure to correct first of all." )

    return checkResult

  def checkInvalidScale( self ):
    checkResult = CheckResultData()

    if "ja_JP" == self.mayaUILanguage:
      checkResult.title = u'scaleの値が [ 1.0 , 1.0 , 1.0 ] ではない'
    else:
      checkResult.title = u'scale value are not [ 1.0 , 1.0 , 1.0 ]'

    dagIt = OpenMaya.MItDag( OpenMaya.MItDag.kDepthFirst , OpenMaya.MFn.kTransform )

    while not dagIt.isDone():
      currentObject = dagIt.currentItem()
      transformFn = OpenMaya.MFnTransform( currentObject )

      transformDagPath = OpenMaya.MDagPath()
      transformFn.getPath( transformDagPath )

      nodePath = transformDagPath.fullPathName()

      '''走査中のノードパスが、検索対象でなければスキップ'''
      if not self.isCheckTarget( nodePath ):
        dagIt.next()
        continue

      scaleValueUtil = OpenMaya.MScriptUtil()
      scaleValueUtil.createFromList( [ 0.0 , 0.0 , 0.0 ] , 3 )

      scaleValuePtr = scaleValueUtil.asDoublePtr()
      transformFn.getScale( scaleValuePtr )

      scaleValue = [ float( "%.4f" % scaleValueUtil.getDoubleArrayItem( scaleValuePtr , 0 ) ) ,
                     float( "%.4f" % scaleValueUtil.getDoubleArrayItem( scaleValuePtr , 1 ) ) ,
                     float( "%.4f" % scaleValueUtil.getDoubleArrayItem( scaleValuePtr , 2 ) ) ]

      if [ 1.0, 1.0, 1.0 ] != self.arrayCorrecter.roundOffArray( scaleValue , 4 ):
        checkResult.errors.append( nodePath )

      dagIt.next()

    return checkResult

  def checkAnimCurveConnection( self ):
    checkResult = CheckResultData()

    if "ja_JP" == self.mayaUILanguage:
      checkResult.title = u'キーフレームがある'
    else:
      checkResult.title = u'Found animCurve connection.'

    animCurveIt = OpenMaya.MItDependencyNodes( OpenMaya.MFn.kAnimCurve )

    while not animCurveIt.isDone():
      animCurveObject = animCurveIt.thisNode()
      animCurveFn = OpenMaya.MFnDependencyNode( animCurveObject )
      outputPlug = animCurveFn.findPlug( "output" )
      dstPlugArray = OpenMaya.MPlugArray()
      outputPlug.connectedTo( dstPlugArray , False , True )

      for i in range( dstPlugArray.length() ):
        dstPlugNodeObject = dstPlugArray[i].node()
        dstDependencyNodeFn = OpenMaya.MFnDependencyNode( dstPlugNodeObject )

        if dstPlugNodeObject.hasFn( OpenMaya.MFn.kTransform ):
          dstNodeDagFn = OpenMaya.MFnDagNode( dstPlugNodeObject )
          dstNodePathString = dstNodeDagFn.fullPathName()

          if not self.isCheckTarget( dstNodePathString ):
            continue

          checkResult.errors.append( dstNodePathString )

      animCurveIt.next()

    checkResult.errors = sorted( list( set( checkResult.errors ) ) )

    return checkResult

  def checkInvalidVertexColor( self ):
    checkResult = CheckResultData()

    if "ja_JP" == self.mayaUILanguage:
      checkResult.title = u'頂点カラー設定済み頂点と未設定頂点が混在する'
    else:
      checkResult.title = u'Colored vertex and not colored vertex are intermingled.'

    meshIt = OpenMaya.MItDag( OpenMaya.MItDag.kDepthFirst , OpenMaya.MFn.kMesh )

    '''mesh走査'''
    while not meshIt.isDone():
      meshDagPath = OpenMaya.MDagPath()
      meshIt.getPath( meshDagPath )
      meshPath = meshDagPath.fullPathName()

      '''現在のメッシュが検査対象でなければスキップ'''
      if not self.isCheckTarget( meshPath ):
        meshIt.next()
        continue

      '''vertex走査'''
      dagNodeFn = OpenMaya.MFnDagNode( meshDagPath.node() )
      meshVtxIt = OpenMaya.MItMeshVertex( meshDagPath.node() )

      colorFlag = False
      emptyFlag = False

      while not meshVtxIt.isDone():

        '''頂点カラーチェック'''
        if meshVtxIt.hasColor():
          colorFlag = True
        else:
          emptyFlag = True

        '''両フラグがTrueなら頂点カラー混在の状態。エラーとして取得'''
        if colorFlag and emptyFlag:
          parentObject = dagNodeFn.parent( 0 )
          parentDagPath = OpenMaya.MDagPath()
          parentDagNodeFn = OpenMaya.MFnDagNode( parentObject )

          parentDagNodeFn.getPath( parentDagPath )
          parentFullPath = parentDagPath.fullPathName()

          checkResult.errors.append( parentFullPath )
          break ## ここに到達したら、もう頂点は走査しなくていいので次のメッシュに移る

        meshVtxIt.next()

      meshIt.next()

    return checkResult

  def checkDoubleNameNotSameCase( self ):
    checkResult = CheckResultData()

    if "ja_JP" == self.mayaUILanguage:
      checkResult.title = u'大文字小文字違いで重複する名前が存在する'
    else:
      checkResult.title = u'Overlapping name exists.(Case insensitive)'

    kNamespacePattern = r'(?:(?:[^:|]+):)*?'
    kNormalNodePrefixList = ['mv_', 'mvg_', 'jnt_']
    kExportNodePattern = r'(?:(?:' + r'|'.join( kNormalNodePrefixList ) + r')[^:|]+)'
    kNodeMatchPattern = kNamespacePattern + kExportNodePattern

    rxNode = re.compile( kNodeMatchPattern )

    l = cmds.ls( recursive=True, transforms=True, dagObjects=True )
    l = filter( lambda x: rxNode.match( x ) is not None, l )
    l = filter( lambda x: 'onstraint' not in cmds.nodeType( x, apiType=True ), l )

    m = {}
    for i in l:
      check = m.get( i.lower() )
      if ( check is None ):
        m[i.lower()] = i
      else:
        checkResult.errors.append( i )
        checkResult.errors.append( check )

    return checkResult

  ''''''
  def checkJoint_OverMaxInfluence( self ):
    checkResult = CheckResultData()

    checkResult.funcName = self.checkJoint_OverMaxInfluence.func_name

    if "ja_JP" == self.mayaUILanguage:
      checkResult.title = u'1つの頂点に影響を与えるジョイント数が5を超えている'
    else:
      checkResult.title = u'Too many maxInfluences. Requires less than 5.'

    exScriptUtil = ExtendMScriptUtil()

    skinClusters = cmds.ls( type="skinCluster" )
    skinClustersSelList = exScriptUtil.nameListToMSelectionList( skinClusters )

    errorVertsSelectionList = OpenMaya.MSelectionList()

    for i in range( skinClustersSelList.length() ):
      currentSkinClusterNode = OpenMaya.MObject()
      skinClustersSelList.getDependNode( i , currentSkinClusterNode )

      mFnDependencyNode = OpenMaya.MFnDependencyNode( currentSkinClusterNode )
      skinClusterName = mFnDependencyNode.name()

      mFnSkinCluster = OpenMayaAnim.MFnSkinCluster( currentSkinClusterNode )
      influenceDagPathArray = OpenMaya.MDagPathArray()
      mFnSkinCluster.influenceObjects( influenceDagPathArray )

      for j in range( influenceDagPathArray.length() ):
        currentInfluenceDagPath = influenceDagPathArray[j]
        affectedShapes = OpenMaya.MSelectionList()
        skinWeights = OpenMaya.MDoubleArray()
        mFnSkinCluster.getPointsAffectedByInfluence( currentInfluenceDagPath , affectedShapes , skinWeights )

        numOutputConnections = mFnSkinCluster.numOutputConnections()
        for k in range( numOutputConnections ):
          currentIndex = mFnSkinCluster.indexForOutputConnection( k )
          currentAffectedShapeDagPath = OpenMaya.MDagPath()
          mFnSkinCluster.getPathAtIndex( currentIndex , currentAffectedShapeDagPath )

          mItGeometry = OpenMaya.MItGeometry( currentAffectedShapeDagPath )
          while not mItGeometry.isDone():
            currentVertex = mItGeometry.currentItem()
            skinWeights = OpenMaya.MDoubleArray()
            influenceCountPtr = OpenMaya.MScriptUtil().asUintPtr()
            mFnSkinCluster.getWeights( currentAffectedShapeDagPath , currentVertex , skinWeights , influenceCountPtr )

            weightedCount = 0
            for skinWeight in skinWeights:
              if 0.0 < skinWeight:
                weightedCount += 1

            if 4 < weightedCount:
              checkResult.errors.append( skinClusterName )
              break

            mItGeometry.next()

    return checkResult

  def checkJoint_WeightedDmy( self ):
    checkResult = CheckResultData()

    if "ja_JP" == self.mayaUILanguage:
      checkResult.title = u'dmy_ジョイントがウエイト値を持っている'
    else:
      checkResult.title = u'[dmy_] joint has skin weight.'

    weightedJointPaths = OpenMaya.MDagPathArray()
    itDagNodes = OpenMaya.MItDependencyNodes( OpenMaya.MFn.kSkinClusterFilter )

    influencePaths = OpenMaya.MDagPathArray()
    errorJoints = []

    while not itDagNodes.isDone():
      skinCluster = itDagNodes.thisNode()

      skinClusterFn = OpenMayaAnim.MFnSkinCluster( skinCluster )
      skinClusterFn.influenceObjects( influencePaths )

      '''インフルエンス走査'''
      for i in range( influencePaths.length() ):
        influencePathStr = influencePaths[i].fullPathName()

        '''現在のインフルエンスが検査対象でなければスキップ'''
        if not self.isCheckTarget( influencePathStr ):
          continue

        '''dmy_ジョイント以外は特別に無視'''
        if not "dmy_" in influencePathStr:
          continue

        '''ウエイト'''
        weightedVts = OpenMaya.MSelectionList()
        weights = OpenMaya.MFloatArray()
        skinClusterFn.getPointsAffectedByInfluence( influencePaths[i] , weightedVts , weights )

        if 0 != len( weights ):
          checkResult.errors.append( influencePathStr )

      itDagNodes.next()

    return checkResult

  def checkJoint_NoWaigtedAndHasNotChildren( self ):
    checkResult = CheckResultData()

    if "ja_JP" == self.mayaUILanguage:
      checkResult.title = u'ジョイントがウエイト値も子ノードも持っていない'
    else:
      checkResult.title = u'Joint has not skin weight and child node.'

    allJoints = cmds.ls( type="joint" , l=1 )
    singleChainJointSet = set( [] )
    weightedJointSet = set( [] )

    ## ウエイトを持つジョイントを取得
    skinClusters = cmds.ls( type="skinCluster" )
    for skinCluster in skinClusters:
      weightedJoints = cmds.skinCluster( skinCluster , q=1 , weightedInfluence=1 )
      weightedJointSet |= set( cmds.ls( weightedJoints , l=1 ) )

    ## ウエイト無しのジョイント
    problemJoints = []
    noWeightedJointSet = set( allJoints ) - weightedJointSet
    for noWeightedJoint in sorted( list( noWeightedJointSet ) ):
      childTransforms = cmds.listRelatives( noWeightedJoint , children=1 , fullPath=1 , type="transform" )
      childJoints = cmds.listRelatives( noWeightedJoint , children=1 , fullPath=1 , type="joint" )

      if childJoints == None:
        childJoints = []

      if childTransforms == None:
        childTransforms = []

      ##
      filterFunc = self.dataCorrecter.filterByType

      if 1 != len( filterFunc( childJoints , [ "kJoint" ] ) ) or ( 0 != len( filterFunc( childTransforms , [ "kTransform" ] ) ) ):
        continue
      else:
        problemJoints.append( noWeightedJoint )

    ##
    checkResult.errors = problemJoints
    return checkResult

  def checkJoint_DoubleNameInOBTree( self ):
    checkResult = CheckResultData()

    if "ja_JP" == self.mayaUILanguage:
      checkResult.title = u'ジョイント名が、同一ob内で重複している'
    else:
      checkResult.title = u'Joint name is overlapping, in the same [ob] tree.'

    jointPaths = cmds.ls( type="joint" , long=1 )

    '''ジョイント走査'''
    for jointPath in jointPaths:

      '''現在のジョイントが検査対象でなければスキップ'''
      if not self.isCheckTarget( jointPath ):
        continue

      splitJointPath = jointPath.split( "|" )
      lastName = splitJointPath[-1]

      nearestOBPath = self.getNearestOBPath( jointPath )
      nearestOBName = self.dataCorrecter.getOBLocatorNameInNodePath( jointPath )

      doubleNamePaths = cmds.ls( lastName , l=1 )

      foundNum = 0
      for doubleNamePath in doubleNamePaths:

        if None != nearestOBPath:
          obNameOfDoubleNamePath = self.dataCorrecter.getOBLocatorNameInNodePath( doubleNamePath )

          if nearestOBName == obNameOfDoubleNamePath:
            foundNum += 1

          if 1 < foundNum:
            checkResult.errors.append( jointPath )
            break

    return checkResult

  ''''''
  def isValidTimeUnit( self ):
    checkResult = CheckResultData()

    if "ja_JP" == self.mayaUILanguage:
      checkResult.title = u'現在のフレームレートがntscではありません。'
    else:
      checkResult.title = u'Current frame rate is not ntsc(30fps).'

    checkResult.errors.append( "" )

    return checkResult

  '''All Locators'''
  def checkAllLocator_LocalPosition( self ):
    checkResult = CheckResultData()

    if "ja_JP" == self.mayaUILanguage:
      checkResult.title = u'ロケーターのlocalPositionが [ 0.0 , 0.0 , 0.0 ] ではない'
    else:
      checkResult.title = u'Locator localPosition are not [ 0.0 , 0.0 , 0.0 ].'

    locatorPaths = cmds.ls( type="locator" , l=1 )

    '''ロケーター走査'''
    for locatorPath in locatorPaths:

      '''現在のロケーターが検査対象でなければスキップ'''
      if not self.isCheckTarget( locatorPath ):
        continue

      locatorLocalPosition = cmds.getAttr( "%s.localPosition" % locatorPath )[0]

      if [ 0.0, 0.0, 0.0 ] != self.arrayCorrecter.roundOffArray( locatorLocalPosition , 4 ):
        parentTransform = cmds.listRelatives( locatorPath , parent=1 , type="transform" , fullPath=1 )[0]
        checkResult.errors.append( parentTransform )

    return checkResult

  '''MV Locators'''
  def checkMV_InvalidMatrix( self ):
    checkResult = CheckResultData()

    if "ja_JP" == self.mayaUILanguage:
      checkResult.title = u'mv_topの姿勢がデフォルトではない'
    else:
      checkResult.title = u'Transformed mv_top.'

    mvLocatorPaths = cmds.ls( "mv_top" , type="transform" , long=1 )

    '''mvロケーター走査'''
    for mvLocatorPath in mvLocatorPaths:

      '''現在のmvロケーターが検査対象でなければスキップ'''
      if not self.isCheckTarget( mvLocatorPath ):
        continue

      defaultMatrix = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
      locatorMatrix = cmds.getAttr( "%s.matrix" % mvLocatorPath )

      if defaultMatrix != self.arrayCorrecter.roundOffArray( locatorMatrix , 4 ):
        checkResult.errors.append( mvLocatorPath )

    return checkResult

  def checkMV_HasChildJoint( self ):
    checkResult = CheckResultData()

    if "ja_JP" == self.mayaUILanguage:
      checkResult.title = u'mv_topが子ジョイントを持っている'
    else:
      checkResult.title = u'mv_top has child joint.'

    mvLocatorPaths = cmds.ls( "mv_top" , type="transform" , long=1 )

    '''mvロケーター走査'''
    for mvLocatorPath in mvLocatorPaths:

      '''現在のmvロケーターが検査対象でなければスキップ'''
      if not self.isCheckTarget( mvLocatorPath ):
        continue

      childJoints = cmds.listRelatives( mvLocatorPath , children=1 , type="joint" )
      if None != childJoints:
        checkResult.errors.append( mvLocatorPath )

    return checkResult

  def checkMV_DoubleNameInOBTree( self ):
    checkResult = CheckResultData()

    if "ja_JP" == self.mayaUILanguage:
      checkResult.title = u'mvロケーター名が、同一ob内で重複している'
    else:
      checkResult.title = u'[mv] locator name is overlapping, in the same [ob] tree.'

    ## シーン内のobロケータ単位走査
    obLocators = cmds.ls( "ob_*" , type="transform" , long=1 )
    for obLocator in obLocators:

      ## チェック対象外ノードはスキップ
      if not self.isCheckTarget( obLocator ):
        continue

      ## 子孫全取得
      descendents = cmds.listRelatives( obLocator , allDescendents=1 , type="transform" , fullPath=1 )

      ## 子孫無しはスキップ
      if descendents == None:
        continue

      ## 子孫走査 まずは、見つかったmvロケータの本名をキーに、同じ本名を持つロケータのパスを辞書内の各リストに貯めこむ
      foundMVInOBDict = FoundErrorItems()
      for descendent in sorted( descendents ):
        ## 子孫の本名を取得
        trueDescendentName = self.dataCorrecter.getTrueNodeName( descendent )

        ## 子孫がmv_ロケータ以外の場合は無視
        if "mv_" != trueDescendentName[:3]:
          continue

        ## mvの本名がすでに見つかっているかチェック。見つかってればエラーとして取得
        if not trueDescendentName in foundMVInOBDict.keys():
          foundMVInOBDict[trueDescendentName] = [ descendent ]
        else:
          foundMVInOBDict[trueDescendentName].append( descendent )

      ## 上で溜め込んだ
      for foundMVs in foundMVInOBDict.values():
        if 2 <= len( foundMVs ):
          checkResult.errors += foundMVs

    return checkResult

  '''OB Locators'''
  def checkOB_HasSingleChild( self ):
    checkResult = CheckResultData()

    if "ja_JP" == self.mayaUILanguage:
      checkResult.title = u'obロケータが単一の子を持たない'
    else:
      checkResult.title = u'[ob] locator has two or more children.'

    return checkResult

  def checkOB_ValidChildNode( self ):
    checkResult = CheckResultData()

    if "ja_JP" == self.mayaUILanguage:
      checkResult.title = u'obロケータの子が単一のジョイント、またはmv_topではない'
    else:
      checkResult.title = u'Child of [ob] locator is not single joint or mv_top.'

    obLocatorPaths = cmds.ls( "ob_*" , l=1 , recursive=1 , type="transform" )

    '''obロケーター走査'''
    for obLocatorPath in obLocatorPaths:

      '''現在のobロケーターが検査対象でなければスキップ'''
      if not self.isCheckTarget( obLocatorPath ):
        continue

      '''ob_で始まるノードがシェープを持たない場合はロケーターではないノードであると判断し、スキップする'''
      obLocatorShape = cmds.listRelatives( obLocatorPath , fullPath=1 , shapes=1 )
      if obLocatorShape == None:
        continue

      childTransforms = self.convertNoneToEmptyList( cmds.listRelatives( obLocatorPath , children=1 , fullPath=1 , type="transform" ) )
      childJoints = self.convertNoneToEmptyList( cmds.listRelatives( obLocatorPath , children=1 , fullPath=1 , type="joint" ) )
      childConstraints = self.convertNoneToEmptyList( cmds.listRelatives( obLocatorPath , children=1 , fullPath=1 , type="constraint" ) )
      validChildren = list( set( childTransforms ) - set( childConstraints ) )

      ## 子が単一のノードでなければエラー
      if 1 != len( validChildren ):
        checkResult.errors.append( obLocatorPath )

      else:
        childName = self.dataCorrecter.getTrueNodeName( validChildren[0] )
        childType = cmds.nodeType( validChildren[0] )

        if ( "mv_top" == childName ) or ( "joint" == childType ):
          continue
        else:
          checkResult.errors.append( obLocatorPath )

    return checkResult

  def checkOB_DoubleName( self ): ## まだ中途半端
    checkResult = CheckResultData()

    if "ja_JP" == self.mayaUILanguage:
      checkResult.title = u'同一レイヤーグループ内でob名が重複している'
    else:
      checkResult.title = u'[ob] locator name is overlapping, in the same layer group.'

    foundOBDict = {}

    ## シーン内obロケーター走査 まずは、各レイヤー名をキーに、obロケータを辞書にまとめる
    obLocatorPaths = cmds.ls( "ob_*" , l=1 , type="transform" )
    for obLocatorPath in sorted( obLocatorPaths ):

      ## 現在のobロケーターが検査対象でなければスキップ
      if not self.isCheckTarget( obLocatorPath ):
        continue

      ## パス整形
      splitOBLocatorPath = obLocatorPath.split( "|" )
      obLocatorTrueName = self.dataCorrecter.getTrueNodeName( obLocatorPath )
      layerName = splitOBLocatorPath[2]

      if not layerName in foundOBDict.keys():
        foundOBDict[ layerName ] = {}
      else:
        if not obLocatorTrueName in foundOBDict[ layerName ].keys():
          foundOBDict[ layerName ][ obLocatorTrueName ] = [ obLocatorPath ]
        else:
          foundOBDict[ layerName ][ obLocatorTrueName ].append( obLocatorPath )

    ##
    for layerName in sorted( foundOBDict.keys() ):
      for obLocatorTrueName in sorted( foundOBDict[ layerName ].keys() ):
        obLocators = foundOBDict[ layerName ][ obLocatorTrueName ]

        if 2 <= len( obLocators ):
          checkResult.errors += obLocators

    return checkResult

  def checkOB_TooManyOBLocators( self ):
    checkResult = CheckResultData()

    if "ja_JP" == self.mayaUILanguage:
      checkResult.title = u'obツリー内に別のobがある'
    else:
      checkResult.title = u'[ob] tree has [ob] locator.'

    obLocatorPaths = cmds.ls( "ob_*" , l=1 , type="transform" )

    '''obロケーター走査'''
    for obLocatorPath in obLocatorPaths:

      '''現在のobロケーターが検査対象でなければスキップ'''
      if not self.isCheckTarget( obLocatorPath ):
        continue

      '''最近接obロケーターがあるということは、ob内にobがあるのでエラー'''
      nearestOBPath = self.getNearestOBPath( obLocatorPath )
      if None != nearestOBPath:
        checkResult.errors.append( obLocatorPath )

    return checkResult

  def checkOB_HasMVMoveOrMVBase( self ):
    checkResult = CheckResultData()

    if "ja_JP" == self.mayaUILanguage:
      checkResult.title = u'obツリー内にmv_moveまたはmv_baseがある'
    else:
      checkResult.title = u'[ob] tree has [mv_move or mb_base].'

    mvMoves = cmds.ls( "*mv_move*" , long=1 , type="transform" )
    mvBases = cmds.ls( "*mv_base*" , long=1 , type="transform" )
    checkTargets = mvBases + mvMoves

    '''obロケーター走査'''
    for checkTarget in checkTargets:

      '''現在のobロケーターが検査対象でなければスキップ'''
      if not self.isCheckTarget( checkTarget ):
        continue

      '''最近接obロケーターがあるということは、ob内にobがあるのでエラー'''
      nearestOBPath = self.getNearestOBPath( checkTarget )
      if None != nearestOBPath:
        checkResult.errors.append( checkTarget )

    return checkResult

  ''' Changed Referenceed not game object '''
  def checkOBJ_changeReferenceNoGameObjects( self ):
    checkResult = CheckResultData()

    if "ja_JP" == self.mayaUILanguage:
      checkResult.title = u'リファレンス中のBGシーンに編集が行われた'
    else:
      checkResult.title = u'Change was made to the data of referenced BG scene.'

    refNodes = cmds.ls( type="reference" )
    for refNode in refNodes:
      ## BG_setRN以外のリファレンスノードは無視
      if "BG_setRN" != refNode:
        continue

      ## リファレンス編集履歴を走査
      refEdits = cmds.referenceQuery( refNode , editStrings=1 )
      for refEdit in refEdits:
        ## setAttrコマンド実行行以外は無視
        if not ( "setAttr" in refEdit ):
          continue

        stripRefEdit = refEdit.strip()

        if "|" == stripRefEdit[0]:
          splitRefEdit = stripRefEdit[1:].split()
        else:
          splitRefEdit = stripRefEdit.split()

        nodePath = splitRefEdit[1].split( "." )[0]
        nodeName = splitRefEdit[1].split( "|" )[-1].split( "." )[0]
        attrName = splitRefEdit[1].split( "." )[-1]

        ## ノード名が mv_ / jnt_ で始まっているものは無視
        if "BG_set:mv_" == nodeName[ :len( "BG_set:mv_" ) ]:
          continue
        
        if "BG_set:jnt_" == nodeName[ :len( "BG_set:jnt_" ) ]:
          continue

        ## ルートノードが axxx_XX_rootのパターンに当てはまっていなければ無視
        if None == self.innerRefRouteRE.match( nodePath ):
          continue

        ## ロケータ/ジョイントは無視
        shapes = cmds.listRelatives( nodePath , shapes=1 , fullPath=1 )
        if shapes == None:
          typeCheckTarget = nodePath
        else:
          typeCheckTarget = shapes[0]

        checkTargetNodes = OpenMaya.MSelectionList()
        OpenMaya.MGlobal_getSelectionListByName( typeCheckTarget , checkTargetNodes )

        checkTargetNode = OpenMaya.MObject()
        checkTargetNodes.getDependNode( 0 , checkTargetNode )

        targetType = checkTargetNode.apiTypeStr()
        safeTypes = [ "kJoint" , "kLocator" ]

        if ( targetType in safeTypes ):
          continue

        ## 変換アトリビュート以外は無視
        if not ( ( "translate" == attrName ) or ( "rotate" == attrName )  or ( "scale" == attrName ) ):
          continue
        else:
          ## 実際に値をセットするsetAttrコマンド行の分割時エレメント数は8 これ以外はとりあえずスルー
          if 7 != len( splitRefEdit ):
            continue

          ## ケツの３つの数値がデフォ値の場合は許可
          xString = splitRefEdit[-3]
          yString = splitRefEdit[-2]
          zString = splitRefEdit[-1]

          """ケツの3つの要素がすべて数値を表す文字列でない場合は無視（要改修かも）"""
          if not ( None != self.numberRE.match( xString ) and None != self.numberRE.match( yString ) and None != self.numberRE.match( zString ) ):
            continue

          x = float( xString )
          y = float( yString )
          z = float( zString )

          '''アトリビュート毎に編集されていないと見なすデフォ値を決定する'''
          if "scale" == attrName:
            defaultValue = 1
          else:
            defaultValue = 0

          '''編集された結果の値がデフォ値なら無視'''
          if ( x == y == z == defaultValue ):
            continue

          print "[Detect changed DAG]" , nodeName , attrName , x, y, z

        checkResult.errors.append( nodePath )

    return checkResult

  '''補助関数群'''
  def getNearestOBPath( self, nodePath ):
    splitLocatorPath = nodePath.split( "|" )
    nearestOBName = None
    nearestOBPath = ""

    for i in range( 0 , len( splitLocatorPath ) - 1 ):
      nodeName = splitLocatorPath[i]

      if ( nodeName == None ) or ( "" == nodeName ):
        continue

      nearestOBPath += "|%s" % nodeName

      if None != self.obLocatorNameRE.match( nodeName ):
        nearestOBName = nodeName
        break

    if nearestOBName != None:
      return nearestOBPath
    else:
      return None

  def convertNoneToEmptyList( self , data ):
    if data == None:
      return []
    else:
      return data

  def isMotionExportTarget( self , nodeTrueName ):
    if ( "mv_top" == nodeTrueName ):
      return False
    elif ( "mv_" != nodeTrueName[:3] ) and ( "jnt_" != nodeTrueName[:4] ) and ( "mvg_" != nodeTrueName[:4] ):
      return False
    else:
      return True

''''''
class ErrorRepairer( object ):
  def __init__( self ):
    self.errorChecker = ErrorChecker()

  def repairPlaybackFramerate( self ):
    cmds.currentUnit( time="ntsc" )

  def repairLocatorLocalPosition( self ):
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

  def repairDAGScale( self ):
    cmds.makeIdentity( t=0 , r=0 , s=1 , a=1 )

  def repairVertexColor( self ):
    if not cmds.pluginInfo( "MYAM_fillNotEnoughVertexColorsCmd.py" , q=1 , loaded=1 ):
      mel.eval( 'catch(`loadPlugin "D:/Puppeteer/Maya/plug-ins/2009-AMD64/MYAM_fillNotEnoughVertexColorsCmd.py"`);' )

    mel.eval( 'fillNotEnoughVertexColors -c 1 -ad 0;' )

  def repairInvalidAnimCurve( self ):
    animCurves = cmds.ls( type="animCurve" , long=1 )
    results = []

    for animCurve in animCurves:

      connectTargets = cmds.listConnections( "%s.output" % animCurve , s=0 , d=1 )
      if connectTargets == None:
        connectTargets = []

      for connectTarget in connectTargets:
        targetPath = cmds.ls( connectTarget , l=1 )

        if self.errorChecker.isCheckTarget( targetPath[0] ):
          cmds.delete( animCurve )

''''''
class CheckResultData( object ):
  def __init__( self ):
    self.funcName = u''
    self.title = u''
    self.errors = []

class DataCorrecter( object ):
  def __init__( self ):
    self.obLocatorNameRE = re.compile( "ob_[a-zA-Z0-9_]*" )

  def getTrueNodeName( self , nodeName , cutNamespace=False ):
    trueName = ""
    lastName = nodeName.split( "|" )[-1]

    if False == cutNamespace:
      return lastName
    else:
      return lastName.split( ":" )[-1]

  def getOBLocatorNameInNodePath( self , nodePath ):
    splitNodePath = nodePath.split( "|" )

    for nodeName in splitNodePath:
      matchObject = self.obLocatorNameRE.match( nodeName )

      if None != matchObject:
        return matchObject.group()

    return None

  def filterByType( self , nodeNames=[] , filterTypes=[] ):
    results = []

    for nodeName in nodeNames:
      selList = OpenMaya.MSelectionList()
      OpenMaya.MGlobal_getSelectionListByName( nodeName , selList )

      node = OpenMaya.MObject()
      selList.getDependNode( 0 , node )

      if node.apiTypeStr() in filterTypes:
        results.append( nodeName )

    return results

class ArrayCorrecter( DataCorrecter ):
  def __init__( self ):
    DataCorrecter.__init__( self )

  def round( self , number , shift=0.0 ):
    decNumber = decimal.Decimal( str( number ) )
    decShift = decimal.Decimal( str( shift ) )
    expNumber = decimal.Decimal( "10.0" )

    leftShift = decNumber * expNumber
    intNumber = int( leftShift )
    rightShift = intNumber / expNumber

    return float( rightShift )

  def roundOffArray( self , array=[] , shift=0.0 ):
    return [ self.round( float( elem ) , float( shift ) ) for elem in array ]

  def toFloatArray( self , array ):
    return [ float( x ) for x in array ]

  def multiplyArray( self , array=[] , coefficient=1.0 ):
    decCoefficient = decimal.Decimal( str( coefficient ) )
    return [ float( decimal.Decimal( str( elem ) ) * decCoefficient ) for elem in array ]

  def optimizeNumArray( self , array ):
    optimizedArray = self.toFloatArray( float( array ) )
    optimizedArray = self.multiplyArray( optimizedArray , 0.01 )
    optimizedArray = self.roundOffArray( optimizedArray , 4 )
    return optimizedArray

class FoundErrorItems( dict ):
  def __init__( self , *args , **kwargs ):
    dict.__init__( self )





def getCurrentLocale():
  envVars = os.environ.keys()

  if "MAYA_UI_LANGUAGE" in envVars:
    localeString = os.environ["MAYA_UI_LANGUAGE"]

  else:
    localeInfo = locale.getdefaultlocale()
    localeString = localeInfo[0]

  return localeString

def main():
  pass

if __name__ == '__main__':
  main()
