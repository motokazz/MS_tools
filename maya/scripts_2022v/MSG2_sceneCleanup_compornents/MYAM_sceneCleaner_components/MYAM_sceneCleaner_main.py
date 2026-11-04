#-*- coding:UTF-8 -*-

#*******************************************************************************
'''

Tool Name     : MYAM_sceneCleaner_main
Description   : シーンデータをクリーンアップするためのツール
                クリーンアップする項目は以下のとおり
                
                不要シェーディングネットワークノードの削除
                余計なウインドウをすべて閉じる
                モデルパネルをワイヤーフレーム表示にする
                不要ヒストリの削除
                中間オブジェクトの削除
                メンバのないレイヤーを削除

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



######################
## Import official modules
######################

import maya.cmds as cmds
import maya.mel  as mel

import os
import shutil
import time

######################
## Import custom modules
######################

import MYAM_PyLib_mayaUI as mayaUI
import MYAM_PyLib_mayaMessageAdapter as MMA

######################
## Reload custom modules
######################

reload( mayaUI )
reload( MMA )

######################
##### Main Class #####
######################

#####
##
class SceneCleaner( object ):

  def __init__( self ):
    self.mayaMessageAdapter = MMA.MayaMessagesAdapter()

  def setMayaMessage( self ):
    command = 'python(\\\"SceneCleaner.popExportConfirmLayoutDialog()\\\");'
    self.mayaMessageAdapter.setCallback( "AfterSave" , command , 0 )

  def defineExportConfirmLayoutDialog( self , *args ):
    rootFLo = cmds.setParent( q=True )

    ##
    LDL_topCLo = mayaUI.layout.ColumnLayout()

    messageTX = mayaUI.control.Text()
    spacer = mayaUI.control.Spacer()

    LDL_BT1 = mayaUI.control.Button()
    LDL_BT2 = mayaUI.control.Button()

    mayaUI.control.Spacer()

    LDL_BT3 = mayaUI.control.Button()

    ##
    cmds.formLayout( rootFLo , e=1 , width=300 )

    cmds.formLayout( rootFLo , e=1 , af=[ ( LDL_topCLo.uiName , "top"    , 0 ) ,
                                          ( LDL_topCLo.uiName , "left"   , 0 ) ,
                                          ( LDL_topCLo.uiName , "right"  , 0 ) ,
                                          ( LDL_topCLo.uiName , "bottom" , 0 ) ] )

    messageTX.label = u"先ほど保存したシーンをクリーンアップできます。\nクリーンアップ後、先ほど保存したデータを上書きします）\n念のため、保存したデータのバックアップが必要であれば「クリーンアップ＋バックアップ」を選択してください。"

    LDL_topCLo.adjustableColumn = 1

    LDL_BT1.label = u'クリーンアップ＋バックアップ+シーンチェック'
    LDL_BT1.backgroundColor = [ 0.88484 , 0.3394 , 1.0 ]

    LDL_BT2.label = u'クリーンアップのみ'
    LDL_BT3.label = u'クリーンアップしない(通常保存のみ)'

    LDL_BT1.command = 'cmds.layoutDialog( dismiss="withBackup"  )'
    LDL_BT2.command = 'cmds.layoutDialog( dismiss="cleanupOnly" )'
    LDL_BT3.command = 'cmds.layoutDialog( dismiss="cancel"  )'

  def popExportConfirmLayoutDialog( self ):
    pushed = cmds.layoutDialog( uiScript=self.defineExportConfirmLayoutDialog )

    if pushed == "withBackup":
      self.doClaeanupWithBackupAndSceneCheck()
    elif pushed == "cleanupOnly":
      self.doClaeanupOnly()
    else:
      pass

  ###########################
  ##### UTILITY METHODS #####
  ###########################

  def getToolComponentPath( self ):
    toolComponentPath = os.path.dirname( __file__ ).replace( "\\" , "/" )
    return toolComponentPath

  #####################
  ##### UI EVENTS #####
  #####################

  #####################
  ##### UI METHOD #####
  #####################

  ##################
  ##### METHOD #####
  ##################

  def doClaeanupWithBackupAndSceneCheck( self ):
    self.createBackUp()

    self.deleteIntermediateNodes()
    self.deleteNondeformableHistory()

    self.cleanUpWindow()
    self.cleanUpDisplayLayer()
    self.cleaUpMaterial()

    self.changeWireframe()

    self.doPositionRecord()

    self.exportAssemblies()

    self.runSceneCheck()

  def doClaeanupOnly( self ):
    self.deleteIntermediateNodes()
    self.deleteNondeformableHistory()

    self.cleanUpWindow()
    self.cleanUpDisplayLayer()
    self.cleaUpMaterial()

    self.changeWireframe()

    self.doPositionRecord()

    self.exportAssemblies()

  ''''''
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
      if ( not window in protectWindows ) and ( not "MYAM" in window ):
        cmds.deleteUI( window )

  def cleaUpMaterial( self ):
    mel.eval( 'hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");' )

  def cleanUpDisplayLayer( self ):
    layers = cmds.ls( type="displayLayer" )

    protectLayers = [ "defaultLayer" ]

    for layer in layers:
      dstConnections = cmds.listConnections( layer , s=0 , d=1 )
      print dstConnections

      if not layer in protectLayers:
        if ( dstConnections == None ):
          print "[DELETE]    " , layer
          cmds.delete( layer )
        else:
          print "[NOT DELETE]" , layer

  def changeWireframe( self ):
    panels = cmds.lsUI( panels=1 )

    for panel in panels:
      panelType = cmds.objectTypeUI( panel )

      if panelType == "TmodelPane":
        cmds.modelEditor( panel , e=1 , displayAppearance="wireframe" , displayLights="default" )

  def createBackUp( self ):
    ## 時間文字列取得
    lt = time.localtime()
    st = time.strftime( "%Y%m%d_%H%M" , lt )

    ## 基本パス情報組み立て
    scenePath = cmds.file( q=1 , sceneName=1 )

    dirPath = os.path.dirname( scenePath )
    backupDirPath = dirPath + "/backup"

    if not os.path.exists( backupDirPath ):
      os.makedirs( backupDirPath )

    fileName = os.path.basename( scenePath )
    splitFileName = fileName.split( "." )
    trueFileName = splitFileName[0]
    extern = splitFileName[1]

    dstFilePath = backupDirPath + "/" + ( splitFileName[0] + "_" + str( st ) + "." + splitFileName[1] )

    ## 実際に複製バックアップ
    shutil.copy( scenePath , dstFilePath )
    print "[BACKUP DONE]" , scenePath , "--->" , dstFilePath

  def exportAssemblies( self ):
    selfPath = cmds.file( q=1 , sceneName=1 )

    assemblies = cmds.ls( assemblies=1 )
    cmds.select( assemblies , r=1 )

    cmds.file( selfPath , f=1 , exportSelected=1 , preserveReferences=1 )
    print "[EXPORT ASSEMBLIES] --->" , selfPath

  def doPositionRecord( self ):
    mel.eval( "source puppeteer_doPositionRecord.mel;puppeteer_doPositionRecord()" )

  def runSceneCheck( self ):
    mel.eval( 'source "D:/Puppeteer/Maya/scripts/mel/common/MYAM_sceneChecker2EXE_BG.mel";' )



######################
## Imported message
######################
print "MODULE IMPORTED... MYAM_sceneCleaner_main"
