#-*- coding:UTF-8 -*-

#*******************************************************************************
'''

Tool Name     : MYAM_PyLib_mayaUI_panel
Description   : Mayaのどのグループにも属さないUI要素をオブジェクト指向ライクに扱うためのモジュール

Copyright     : (c)2012 Michiyoshi Yamabe
Author Name   : Michiyoshi Yamabe
Contact       : Yamabe.Michiyoshi@gmail.com

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



import maya.cmds as cmds



class Annotate( object ):

  ##### initialize #####
  def __init__( self , point=None , text=None , **args ):
    self.uiName = cmds.annotate()

    ##### substitution #####
    if point != None:
      self.point = point
    if text != None:
      self.text = text

  ##### getFuncCode #####
  def getpoint( self ):
    return cmds.annotate( self.uiName , q=1 , point=1 )
  def gettext( self ):
    return cmds.annotate( self.uiName , q=1 , text=1 )

  ##### setFuncCode #####
  def setpoint( self , value ):
    cmds.annotate( self.uiName , e=1 , point=value )
  def settext( self , value ):
    cmds.annotate( self.uiName , e=1 , text=value )

  ##### propertyCode #####
  point = property( getpoint , setpoint )
  text = property( gettext , settext )

  ##### customCode #####





class AutoPlace( object ):

  ##### initialize #####
  def __init__( self , useMouse=None , **args ):
    self.uiName = cmds.autoPlace()

    ##### substitution #####
    if useMouse != None:
      self.useMouse = useMouse

  ##### getFuncCode #####
  def getuseMouse( self ):
    return cmds.autoPlace( self.uiName , q=1 , useMouse=1 )

  ##### setFuncCode #####
  def setuseMouse( self , value ):
    cmds.autoPlace( self.uiName , e=1 , useMouse=value )

  ##### propertyCode #####
  useMouse = property( getuseMouse , setuseMouse )

  ##### customCode #####





class ButtonManip( object ):

  ##### initialize #####
  def __init__( self , icon=None , **args ):
    self.uiName = cmds.buttonManip()

    ##### substitution #####
    if icon != None:
      self.icon = icon

  ##### getFuncCode #####
  def geticon( self ):
    return cmds.buttonManip( self.uiName , q=1 , icon=1 )

  ##### setFuncCode #####
  def seticon( self , value ):
    cmds.buttonManip( self.uiName , e=1 , icon=value )

  ##### propertyCode #####
  icon = property( geticon , seticon )

  ##### customCode #####





class GrabColor( object ):

  ##### initialize #####
  def __init__( self , hsvValue=None , rgbValue=None , **args ):
    self.uiName = cmds.grabColor()

    ##### substitution #####
    if hsvValue != None:
      self.hsvValue = hsvValue
    if rgbValue != None:
      self.rgbValue = rgbValue

  ##### getFuncCode #####
  def gethsvValue( self ):
    return cmds.grabColor( self.uiName , q=1 , hsvValue=1 )
  def getrgbValue( self ):
    return cmds.grabColor( self.uiName , q=1 , rgbValue=1 )

  ##### setFuncCode #####
  def sethsvValue( self , value ):
    cmds.grabColor( self.uiName , e=1 , hsvValue=value )
  def setrgbValue( self , value ):
    cmds.grabColor( self.uiName , e=1 , rgbValue=value )

  ##### propertyCode #####
  hsvValue = property( gethsvValue , sethsvValue )
  rgbValue = property( getrgbValue , setrgbValue )

  ##### customCode #####





class HeadsUpDisplay( object ):

  ##### initialize #####
  def __init__( self , attributeChange=None , allDescendants=None , allowOverlap=None , attachToRefresh=None , block=None , blockAlignment=None , blockSize=None , command=None , conditionChange=None , conditionFalse=None , connectionChange=None , conditionTrue=None , dataAlignment=None , dataFontSize=None , disregardIndex=None , decimalPrecision=None , dataWidth=None , event=None , exists=None , gridColor=None , label=None , listConditions=None , listEvents=None , labelFontSize=None , listHeadsUpDisplays=None , listNodeChanges=None , lastOccupiedBlock=None , listPresets=None , layoutVisibility=None , labelWidth=None , name=None , nodeChanges=None , nextFreeBlock=None , getOption=None , padding=None , preset=None , refresh=None , remove=None , removeID=None , resetNodeChanges=None , removePosition=None , section=None , showGrid=None , setOption=None , scriptResult=None , visible=None , **args ):
    self.uiName = cmds.headsUpDisplay()

    ##### substitution #####
    if attributeChange != None:
      self.attributeChange = attributeChange
    if allDescendants != None:
      self.allDescendants = allDescendants
    if allowOverlap != None:
      self.allowOverlap = allowOverlap
    if attachToRefresh != None:
      self.attachToRefresh = attachToRefresh
    if block != None:
      self.block = block
    if blockAlignment != None:
      self.blockAlignment = blockAlignment
    if blockSize != None:
      self.blockSize = blockSize
    if command != None:
      self.command = command
    if conditionChange != None:
      self.conditionChange = conditionChange
    if conditionFalse != None:
      self.conditionFalse = conditionFalse
    if connectionChange != None:
      self.connectionChange = connectionChange
    if conditionTrue != None:
      self.conditionTrue = conditionTrue
    if dataAlignment != None:
      self.dataAlignment = dataAlignment
    if dataFontSize != None:
      self.dataFontSize = dataFontSize
    if disregardIndex != None:
      self.disregardIndex = disregardIndex
    if decimalPrecision != None:
      self.decimalPrecision = decimalPrecision
    if dataWidth != None:
      self.dataWidth = dataWidth
    if event != None:
      self.event = event
    if exists != None:
      self.exists = exists
    if gridColor != None:
      self.gridColor = gridColor
    if label != None:
      self.label = label
    if listConditions != None:
      self.listConditions = listConditions
    if listEvents != None:
      self.listEvents = listEvents
    if labelFontSize != None:
      self.labelFontSize = labelFontSize
    if listHeadsUpDisplays != None:
      self.listHeadsUpDisplays = listHeadsUpDisplays
    if listNodeChanges != None:
      self.listNodeChanges = listNodeChanges
    if lastOccupiedBlock != None:
      self.lastOccupiedBlock = lastOccupiedBlock
    if listPresets != None:
      self.listPresets = listPresets
    if layoutVisibility != None:
      self.layoutVisibility = layoutVisibility
    if labelWidth != None:
      self.labelWidth = labelWidth
    if name != None:
      self.name = name
    if nodeChanges != None:
      self.nodeChanges = nodeChanges
    if nextFreeBlock != None:
      self.nextFreeBlock = nextFreeBlock
    if getOption != None:
      self.getOption = getOption
    if padding != None:
      self.padding = padding
    if preset != None:
      self.preset = preset
    if refresh != None:
      self.refresh = refresh
    if remove != None:
      self.remove = remove
    if removeID != None:
      self.removeID = removeID
    if resetNodeChanges != None:
      self.resetNodeChanges = resetNodeChanges
    if removePosition != None:
      self.removePosition = removePosition
    if section != None:
      self.section = section
    if showGrid != None:
      self.showGrid = showGrid
    if setOption != None:
      self.setOption = setOption
    if scriptResult != None:
      self.scriptResult = scriptResult
    if visible != None:
      self.visible = visible

  ##### getFuncCode #####
  def getattributeChange( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , attributeChange=1 )
  def getallDescendants( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , allDescendants=1 )
  def getallowOverlap( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , allowOverlap=1 )
  def getattachToRefresh( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , attachToRefresh=1 )
  def getblock( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , block=1 )
  def getblockAlignment( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , blockAlignment=1 )
  def getblockSize( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , blockSize=1 )
  def getcommand( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , command=1 )
  def getconditionChange( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , conditionChange=1 )
  def getconditionFalse( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , conditionFalse=1 )
  def getconnectionChange( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , connectionChange=1 )
  def getconditionTrue( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , conditionTrue=1 )
  def getdataAlignment( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , dataAlignment=1 )
  def getdataFontSize( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , dataFontSize=1 )
  def getdisregardIndex( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , disregardIndex=1 )
  def getdecimalPrecision( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , decimalPrecision=1 )
  def getdataWidth( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , dataWidth=1 )
  def getevent( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , event=1 )
  def getexists( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , exists=1 )
  def getgridColor( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , gridColor=1 )
  def getlabel( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , label=1 )
  def getlistConditions( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , listConditions=1 )
  def getlistEvents( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , listEvents=1 )
  def getlabelFontSize( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , labelFontSize=1 )
  def getlistHeadsUpDisplays( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , listHeadsUpDisplays=1 )
  def getlistNodeChanges( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , listNodeChanges=1 )
  def getlastOccupiedBlock( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , lastOccupiedBlock=1 )
  def getlistPresets( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , listPresets=1 )
  def getlayoutVisibility( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , layoutVisibility=1 )
  def getlabelWidth( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , labelWidth=1 )
  def getname( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , name=1 )
  def getnodeChanges( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , nodeChanges=1 )
  def getnextFreeBlock( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , nextFreeBlock=1 )
  def getgetOption( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , getOption=1 )
  def getpadding( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , padding=1 )
  def getpreset( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , preset=1 )
  def getrefresh( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , refresh=1 )
  def getremove( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , remove=1 )
  def getremoveID( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , removeID=1 )
  def getresetNodeChanges( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , resetNodeChanges=1 )
  def getremovePosition( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , removePosition=1 )
  def getsection( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , section=1 )
  def getshowGrid( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , showGrid=1 )
  def getsetOption( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , setOption=1 )
  def getscriptResult( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , scriptResult=1 )
  def getvisible( self ):
    return cmds.headsUpDisplay( self.uiName , q=1 , visible=1 )

  ##### setFuncCode #####
  def setattributeChange( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , attributeChange=value )
  def setallDescendants( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , allDescendants=value )
  def setallowOverlap( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , allowOverlap=value )
  def setattachToRefresh( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , attachToRefresh=value )
  def setblock( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , block=value )
  def setblockAlignment( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , blockAlignment=value )
  def setblockSize( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , blockSize=value )
  def setcommand( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , command=value )
  def setconditionChange( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , conditionChange=value )
  def setconditionFalse( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , conditionFalse=value )
  def setconnectionChange( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , connectionChange=value )
  def setconditionTrue( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , conditionTrue=value )
  def setdataAlignment( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , dataAlignment=value )
  def setdataFontSize( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , dataFontSize=value )
  def setdisregardIndex( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , disregardIndex=value )
  def setdecimalPrecision( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , decimalPrecision=value )
  def setdataWidth( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , dataWidth=value )
  def setevent( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , event=value )
  def setexists( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , exists=value )
  def setgridColor( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , gridColor=value )
  def setlabel( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , label=value )
  def setlistConditions( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , listConditions=value )
  def setlistEvents( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , listEvents=value )
  def setlabelFontSize( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , labelFontSize=value )
  def setlistHeadsUpDisplays( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , listHeadsUpDisplays=value )
  def setlistNodeChanges( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , listNodeChanges=value )
  def setlastOccupiedBlock( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , lastOccupiedBlock=value )
  def setlistPresets( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , listPresets=value )
  def setlayoutVisibility( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , layoutVisibility=value )
  def setlabelWidth( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , labelWidth=value )
  def setname( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , name=value )
  def setnodeChanges( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , nodeChanges=value )
  def setnextFreeBlock( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , nextFreeBlock=value )
  def setgetOption( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , getOption=value )
  def setpadding( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , padding=value )
  def setpreset( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , preset=value )
  def setrefresh( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , refresh=value )
  def setremove( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , remove=value )
  def setremoveID( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , removeID=value )
  def setresetNodeChanges( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , resetNodeChanges=value )
  def setremovePosition( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , removePosition=value )
  def setsection( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , section=value )
  def setshowGrid( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , showGrid=value )
  def setsetOption( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , setOption=value )
  def setscriptResult( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , scriptResult=value )
  def setvisible( self , value ):
    cmds.headsUpDisplay( self.uiName , e=1 , visible=value )

  ##### propertyCode #####
  attributeChange = property( getattributeChange , setattributeChange )
  allDescendants = property( getallDescendants , setallDescendants )
  allowOverlap = property( getallowOverlap , setallowOverlap )
  attachToRefresh = property( getattachToRefresh , setattachToRefresh )
  block = property( getblock , setblock )
  blockAlignment = property( getblockAlignment , setblockAlignment )
  blockSize = property( getblockSize , setblockSize )
  command = property( getcommand , setcommand )
  conditionChange = property( getconditionChange , setconditionChange )
  conditionFalse = property( getconditionFalse , setconditionFalse )
  connectionChange = property( getconnectionChange , setconnectionChange )
  conditionTrue = property( getconditionTrue , setconditionTrue )
  dataAlignment = property( getdataAlignment , setdataAlignment )
  dataFontSize = property( getdataFontSize , setdataFontSize )
  disregardIndex = property( getdisregardIndex , setdisregardIndex )
  decimalPrecision = property( getdecimalPrecision , setdecimalPrecision )
  dataWidth = property( getdataWidth , setdataWidth )
  event = property( getevent , setevent )
  exists = property( getexists , setexists )
  gridColor = property( getgridColor , setgridColor )
  label = property( getlabel , setlabel )
  listConditions = property( getlistConditions , setlistConditions )
  listEvents = property( getlistEvents , setlistEvents )
  labelFontSize = property( getlabelFontSize , setlabelFontSize )
  listHeadsUpDisplays = property( getlistHeadsUpDisplays , setlistHeadsUpDisplays )
  listNodeChanges = property( getlistNodeChanges , setlistNodeChanges )
  lastOccupiedBlock = property( getlastOccupiedBlock , setlastOccupiedBlock )
  listPresets = property( getlistPresets , setlistPresets )
  layoutVisibility = property( getlayoutVisibility , setlayoutVisibility )
  labelWidth = property( getlabelWidth , setlabelWidth )
  name = property( getname , setname )
  nodeChanges = property( getnodeChanges , setnodeChanges )
  nextFreeBlock = property( getnextFreeBlock , setnextFreeBlock )
  getOption = property( getgetOption , setgetOption )
  padding = property( getpadding , setpadding )
  preset = property( getpreset , setpreset )
  refresh = property( getrefresh , setrefresh )
  remove = property( getremove , setremove )
  removeID = property( getremoveID , setremoveID )
  resetNodeChanges = property( getresetNodeChanges , setresetNodeChanges )
  removePosition = property( getremovePosition , setremovePosition )
  section = property( getsection , setsection )
  showGrid = property( getshowGrid , setshowGrid )
  setOption = property( getsetOption , setsetOption )
  scriptResult = property( getscriptResult , setscriptResult )
  visible = property( getvisible , setvisible )

  ##### customCode #####





class HeadsUpMessage( object ):

  ##### initialize #####
  def __init__( self , horizontalOffset=None , object=None , selection=None , time=None , uvTextureEditor=None , verticalOffset=None , viewport=None , **args ):
    self.uiName = cmds.headsUpMessage()

    ##### substitution #####
    if horizontalOffset != None:
      self.horizontalOffset = horizontalOffset
    if object != None:
      self.object = object
    if selection != None:
      self.selection = selection
    if time != None:
      self.time = time
    if uvTextureEditor != None:
      self.uvTextureEditor = uvTextureEditor
    if verticalOffset != None:
      self.verticalOffset = verticalOffset
    if viewport != None:
      self.viewport = viewport

  ##### getFuncCode #####
  def gethorizontalOffset( self ):
    return cmds.headsUpMessage( self.uiName , q=1 , horizontalOffset=1 )
  def getobject( self ):
    return cmds.headsUpMessage( self.uiName , q=1 , object=1 )
  def getselection( self ):
    return cmds.headsUpMessage( self.uiName , q=1 , selection=1 )
  def gettime( self ):
    return cmds.headsUpMessage( self.uiName , q=1 , time=1 )
  def getuvTextureEditor( self ):
    return cmds.headsUpMessage( self.uiName , q=1 , uvTextureEditor=1 )
  def getverticalOffset( self ):
    return cmds.headsUpMessage( self.uiName , q=1 , verticalOffset=1 )
  def getviewport( self ):
    return cmds.headsUpMessage( self.uiName , q=1 , viewport=1 )

  ##### setFuncCode #####
  def sethorizontalOffset( self , value ):
    cmds.headsUpMessage( self.uiName , e=1 , horizontalOffset=value )
  def setobject( self , value ):
    cmds.headsUpMessage( self.uiName , e=1 , object=value )
  def setselection( self , value ):
    cmds.headsUpMessage( self.uiName , e=1 , selection=value )
  def settime( self , value ):
    cmds.headsUpMessage( self.uiName , e=1 , time=value )
  def setuvTextureEditor( self , value ):
    cmds.headsUpMessage( self.uiName , e=1 , uvTextureEditor=value )
  def setverticalOffset( self , value ):
    cmds.headsUpMessage( self.uiName , e=1 , verticalOffset=value )
  def setviewport( self , value ):
    cmds.headsUpMessage( self.uiName , e=1 , viewport=value )

  ##### propertyCode #####
  horizontalOffset = property( gethorizontalOffset , sethorizontalOffset )
  object = property( getobject , setobject )
  selection = property( getselection , setselection )
  time = property( gettime , settime )
  uvTextureEditor = property( getuvTextureEditor , setuvTextureEditor )
  verticalOffset = property( getverticalOffset , setverticalOffset )
  viewport = property( getviewport , setviewport )

  ##### customCode #####





class Hotkey( object ):

  ##### initialize #####
  def __init__( self , altModifier=None , autoSave=None , commandModifier=None , ctrlModifier=None , factorySettings=None , keyShortcut=None , isModifier=None , name=None , pressCommandRepeat=None , releaseCommandRepeat=None , releaseName=None , sourceUserHotkeys=None , **args ):
    self.uiName = cmds.hotkey()

    ##### substitution #####
    if altModifier != None:
      self.altModifier = altModifier
    if autoSave != None:
      self.autoSave = autoSave
    if commandModifier != None:
      self.commandModifier = commandModifier
    if ctrlModifier != None:
      self.ctrlModifier = ctrlModifier
    if factorySettings != None:
      self.factorySettings = factorySettings
    if keyShortcut != None:
      self.keyShortcut = keyShortcut
    if isModifier != None:
      self.isModifier = isModifier
    if name != None:
      self.name = name
    if pressCommandRepeat != None:
      self.pressCommandRepeat = pressCommandRepeat
    if releaseCommandRepeat != None:
      self.releaseCommandRepeat = releaseCommandRepeat
    if releaseName != None:
      self.releaseName = releaseName
    if sourceUserHotkeys != None:
      self.sourceUserHotkeys = sourceUserHotkeys

  ##### getFuncCode #####
  def getaltModifier( self ):
    return cmds.hotkey( self.uiName , q=1 , altModifier=1 )
  def getautoSave( self ):
    return cmds.hotkey( self.uiName , q=1 , autoSave=1 )
  def getcommandModifier( self ):
    return cmds.hotkey( self.uiName , q=1 , commandModifier=1 )
  def getctrlModifier( self ):
    return cmds.hotkey( self.uiName , q=1 , ctrlModifier=1 )
  def getfactorySettings( self ):
    return cmds.hotkey( self.uiName , q=1 , factorySettings=1 )
  def getkeyShortcut( self ):
    return cmds.hotkey( self.uiName , q=1 , keyShortcut=1 )
  def getisModifier( self ):
    return cmds.hotkey( self.uiName , q=1 , isModifier=1 )
  def getname( self ):
    return cmds.hotkey( self.uiName , q=1 , name=1 )
  def getpressCommandRepeat( self ):
    return cmds.hotkey( self.uiName , q=1 , pressCommandRepeat=1 )
  def getreleaseCommandRepeat( self ):
    return cmds.hotkey( self.uiName , q=1 , releaseCommandRepeat=1 )
  def getreleaseName( self ):
    return cmds.hotkey( self.uiName , q=1 , releaseName=1 )
  def getsourceUserHotkeys( self ):
    return cmds.hotkey( self.uiName , q=1 , sourceUserHotkeys=1 )

  ##### setFuncCode #####
  def setaltModifier( self , value ):
    cmds.hotkey( self.uiName , e=1 , altModifier=value )
  def setautoSave( self , value ):
    cmds.hotkey( self.uiName , e=1 , autoSave=value )
  def setcommandModifier( self , value ):
    cmds.hotkey( self.uiName , e=1 , commandModifier=value )
  def setctrlModifier( self , value ):
    cmds.hotkey( self.uiName , e=1 , ctrlModifier=value )
  def setfactorySettings( self , value ):
    cmds.hotkey( self.uiName , e=1 , factorySettings=value )
  def setkeyShortcut( self , value ):
    cmds.hotkey( self.uiName , e=1 , keyShortcut=value )
  def setisModifier( self , value ):
    cmds.hotkey( self.uiName , e=1 , isModifier=value )
  def setname( self , value ):
    cmds.hotkey( self.uiName , e=1 , name=value )
  def setpressCommandRepeat( self , value ):
    cmds.hotkey( self.uiName , e=1 , pressCommandRepeat=value )
  def setreleaseCommandRepeat( self , value ):
    cmds.hotkey( self.uiName , e=1 , releaseCommandRepeat=value )
  def setreleaseName( self , value ):
    cmds.hotkey( self.uiName , e=1 , releaseName=value )
  def setsourceUserHotkeys( self , value ):
    cmds.hotkey( self.uiName , e=1 , sourceUserHotkeys=value )

  ##### propertyCode #####
  altModifier = property( getaltModifier , setaltModifier )
  autoSave = property( getautoSave , setautoSave )
  commandModifier = property( getcommandModifier , setcommandModifier )
  ctrlModifier = property( getctrlModifier , setctrlModifier )
  factorySettings = property( getfactorySettings , setfactorySettings )
  keyShortcut = property( getkeyShortcut , setkeyShortcut )
  isModifier = property( getisModifier , setisModifier )
  name = property( getname , setname )
  pressCommandRepeat = property( getpressCommandRepeat , setpressCommandRepeat )
  releaseCommandRepeat = property( getreleaseCommandRepeat , setreleaseCommandRepeat )
  releaseName = property( getreleaseName , setreleaseName )
  sourceUserHotkeys = property( getsourceUserHotkeys , setsourceUserHotkeys )

  ##### customCode #####





class HotkeyCheck( object ):

  ##### initialize #####
  def __init__( self , altModifier=None , commandModifier=None , ctrlModifier=None , isRepeatable=None , keyString=None , toBeRemovedInFutureMayaRelease=None , keyUp=None , optionModifier=None , **args ):
    self.uiName = cmds.hotkeyCheck()

    ##### substitution #####
    if altModifier != None:
      self.altModifier = altModifier
    if commandModifier != None:
      self.commandModifier = commandModifier
    if ctrlModifier != None:
      self.ctrlModifier = ctrlModifier
    if isRepeatable != None:
      self.isRepeatable = isRepeatable
    if keyString != None:
      self.keyString = keyString
    if toBeRemovedInFutureMayaRelease != None:
      self.toBeRemovedInFutureMayaRelease = toBeRemovedInFutureMayaRelease
    if keyUp != None:
      self.keyUp = keyUp
    if optionModifier != None:
      self.optionModifier = optionModifier

  ##### getFuncCode #####
  def getaltModifier( self ):
    return cmds.hotkeyCheck( self.uiName , q=1 , altModifier=1 )
  def getcommandModifier( self ):
    return cmds.hotkeyCheck( self.uiName , q=1 , commandModifier=1 )
  def getctrlModifier( self ):
    return cmds.hotkeyCheck( self.uiName , q=1 , ctrlModifier=1 )
  def getisRepeatable( self ):
    return cmds.hotkeyCheck( self.uiName , q=1 , isRepeatable=1 )
  def getkeyString( self ):
    return cmds.hotkeyCheck( self.uiName , q=1 , keyString=1 )
  def gettoBeRemovedInFutureMayaRelease( self ):
    return cmds.hotkeyCheck( self.uiName , q=1 , toBeRemovedInFutureMayaRelease=1 )
  def getkeyUp( self ):
    return cmds.hotkeyCheck( self.uiName , q=1 , keyUp=1 )
  def getoptionModifier( self ):
    return cmds.hotkeyCheck( self.uiName , q=1 , optionModifier=1 )

  ##### setFuncCode #####
  def setaltModifier( self , value ):
    cmds.hotkeyCheck( self.uiName , e=1 , altModifier=value )
  def setcommandModifier( self , value ):
    cmds.hotkeyCheck( self.uiName , e=1 , commandModifier=value )
  def setctrlModifier( self , value ):
    cmds.hotkeyCheck( self.uiName , e=1 , ctrlModifier=value )
  def setisRepeatable( self , value ):
    cmds.hotkeyCheck( self.uiName , e=1 , isRepeatable=value )
  def setkeyString( self , value ):
    cmds.hotkeyCheck( self.uiName , e=1 , keyString=value )
  def settoBeRemovedInFutureMayaRelease( self , value ):
    cmds.hotkeyCheck( self.uiName , e=1 , toBeRemovedInFutureMayaRelease=value )
  def setkeyUp( self , value ):
    cmds.hotkeyCheck( self.uiName , e=1 , keyUp=value )
  def setoptionModifier( self , value ):
    cmds.hotkeyCheck( self.uiName , e=1 , optionModifier=value )

  ##### propertyCode #####
  altModifier = property( getaltModifier , setaltModifier )
  commandModifier = property( getcommandModifier , setcommandModifier )
  ctrlModifier = property( getctrlModifier , setctrlModifier )
  isRepeatable = property( getisRepeatable , setisRepeatable )
  keyString = property( getkeyString , setkeyString )
  toBeRemovedInFutureMayaRelease = property( gettoBeRemovedInFutureMayaRelease , settoBeRemovedInFutureMayaRelease )
  keyUp = property( getkeyUp , setkeyUp )
  optionModifier = property( getoptionModifier , setoptionModifier )

  ##### customCode #####





class LinearPrecision( object ):

  ##### initialize #####
  def __init__( self , **args ):
    self.uiName = cmds.linearPrecision()

    ##### substitution #####

  ##### getFuncCode #####

  ##### setFuncCode #####

  ##### propertyCode #####

  ##### customCode #####





class LoadPrefObjects( object ):

  ##### initialize #####
  def __init__( self , **args ):
    self.uiName = cmds.loadPrefObjects()

    ##### substitution #####

  ##### getFuncCode #####

  ##### setFuncCode #####

  ##### propertyCode #####

  ##### customCode #####





class NameCommand( object ):

  ##### initialize #####
  def __init__( self , annotation=None , command=None , default=None , data1=None , data2=None , data3=None , sourceType=None , **args ):
    self.uiName = cmds.nameCommand()

    ##### substitution #####
    if annotation != None:
      self.annotation = annotation
    if command != None:
      self.command = command
    if default != None:
      self.default = default
    if data1 != None:
      self.data1 = data1
    if data2 != None:
      self.data2 = data2
    if data3 != None:
      self.data3 = data3
    if sourceType != None:
      self.sourceType = sourceType

  ##### getFuncCode #####
  def getannotation( self ):
    return cmds.nameCommand( self.uiName , q=1 , annotation=1 )
  def getcommand( self ):
    return cmds.nameCommand( self.uiName , q=1 , command=1 )
  def getdefault( self ):
    return cmds.nameCommand( self.uiName , q=1 , default=1 )
  def getdata1( self ):
    return cmds.nameCommand( self.uiName , q=1 , data1=1 )
  def getdata2( self ):
    return cmds.nameCommand( self.uiName , q=1 , data2=1 )
  def getdata3( self ):
    return cmds.nameCommand( self.uiName , q=1 , data3=1 )
  def getsourceType( self ):
    return cmds.nameCommand( self.uiName , q=1 , sourceType=1 )

  ##### setFuncCode #####
  def setannotation( self , value ):
    cmds.nameCommand( self.uiName , e=1 , annotation=value )
  def setcommand( self , value ):
    cmds.nameCommand( self.uiName , e=1 , command=value )
  def setdefault( self , value ):
    cmds.nameCommand( self.uiName , e=1 , default=value )
  def setdata1( self , value ):
    cmds.nameCommand( self.uiName , e=1 , data1=value )
  def setdata2( self , value ):
    cmds.nameCommand( self.uiName , e=1 , data2=value )
  def setdata3( self , value ):
    cmds.nameCommand( self.uiName , e=1 , data3=value )
  def setsourceType( self , value ):
    cmds.nameCommand( self.uiName , e=1 , sourceType=value )

  ##### propertyCode #####
  annotation = property( getannotation , setannotation )
  command = property( getcommand , setcommand )
  default = property( getdefault , setdefault )
  data1 = property( getdata1 , setdata1 )
  data2 = property( getdata2 , setdata2 )
  data3 = property( getdata3 , setdata3 )
  sourceType = property( getsourceType , setsourceType )

  ##### customCode #####





class OverrideModifier( object ):

  ##### initialize #####
  def __init__( self , clear=None , press=None , release=None , **args ):
    self.uiName = cmds.overrideModifier()

    ##### substitution #####
    if clear != None:
      self.clear = clear
    if press != None:
      self.press = press
    if release != None:
      self.release = release

  ##### getFuncCode #####
  def getclear( self ):
    return cmds.overrideModifier( self.uiName , q=1 , clear=1 )
  def getpress( self ):
    return cmds.overrideModifier( self.uiName , q=1 , press=1 )
  def getrelease( self ):
    return cmds.overrideModifier( self.uiName , q=1 , release=1 )

  ##### setFuncCode #####
  def setclear( self , value ):
    cmds.overrideModifier( self.uiName , e=1 , clear=value )
  def setpress( self , value ):
    cmds.overrideModifier( self.uiName , e=1 , press=value )
  def setrelease( self , value ):
    cmds.overrideModifier( self.uiName , e=1 , release=value )

  ##### propertyCode #####
  clear = property( getclear , setclear )
  press = property( getpress , setpress )
  release = property( getrelease , setrelease )

  ##### customCode #####





class SaveAllShelves( object ):

  ##### initialize #####
  def __init__( self , **args ):
    self.uiName = cmds.saveAllShelves()

    ##### substitution #####

  ##### getFuncCode #####

  ##### setFuncCode #####

  ##### propertyCode #####

  ##### customCode #####





class SavePrefObjects( object ):

  ##### initialize #####
  def __init__( self , **args ):
    self.uiName = cmds.savePrefObjects()

    ##### substitution #####

  ##### getFuncCode #####

  ##### setFuncCode #####

  ##### propertyCode #####

  ##### customCode #####





class SavePrefs( object ):

  ##### initialize #####
  def __init__( self , colors=None , general=None , hotkeys=None , menuSets=None , plugins=None , uiLayout=None , **args ):
    self.uiName = cmds.savePrefs()

    ##### substitution #####
    if colors != None:
      self.colors = colors
    if general != None:
      self.general = general
    if hotkeys != None:
      self.hotkeys = hotkeys
    if menuSets != None:
      self.menuSets = menuSets
    if plugins != None:
      self.plugins = plugins
    if uiLayout != None:
      self.uiLayout = uiLayout

  ##### getFuncCode #####
  def getcolors( self ):
    return cmds.savePrefs( self.uiName , q=1 , colors=1 )
  def getgeneral( self ):
    return cmds.savePrefs( self.uiName , q=1 , general=1 )
  def gethotkeys( self ):
    return cmds.savePrefs( self.uiName , q=1 , hotkeys=1 )
  def getmenuSets( self ):
    return cmds.savePrefs( self.uiName , q=1 , menuSets=1 )
  def getplugins( self ):
    return cmds.savePrefs( self.uiName , q=1 , plugins=1 )
  def getuiLayout( self ):
    return cmds.savePrefs( self.uiName , q=1 , uiLayout=1 )

  ##### setFuncCode #####
  def setcolors( self , value ):
    cmds.savePrefs( self.uiName , e=1 , colors=value )
  def setgeneral( self , value ):
    cmds.savePrefs( self.uiName , e=1 , general=value )
  def sethotkeys( self , value ):
    cmds.savePrefs( self.uiName , e=1 , hotkeys=value )
  def setmenuSets( self , value ):
    cmds.savePrefs( self.uiName , e=1 , menuSets=value )
  def setplugins( self , value ):
    cmds.savePrefs( self.uiName , e=1 , plugins=value )
  def setuiLayout( self , value ):
    cmds.savePrefs( self.uiName , e=1 , uiLayout=value )

  ##### propertyCode #####
  colors = property( getcolors , setcolors )
  general = property( getgeneral , setgeneral )
  hotkeys = property( gethotkeys , sethotkeys )
  menuSets = property( getmenuSets , setmenuSets )
  plugins = property( getplugins , setplugins )
  uiLayout = property( getuiLayout , setuiLayout )

  ##### customCode #####





class SaveShelf( object ):

  ##### initialize #####
  def __init__( self , **args ):
    self.uiName = cmds.saveShelf()

    ##### substitution #####

  ##### getFuncCode #####

  ##### setFuncCode #####

  ##### propertyCode #####

  ##### customCode #####





class Scmh( object ):

  ##### initialize #####
  def __init__( self , absolute=None , ignore=None , relative=None , **args ):
    self.uiName = cmds.scmh()

    ##### substitution #####
    if absolute != None:
      self.absolute = absolute
    if ignore != None:
      self.ignore = ignore
    if relative != None:
      self.relative = relative

  ##### getFuncCode #####
  def getabsolute( self ):
    return cmds.scmh( self.uiName , q=1 , absolute=1 )
  def getignore( self ):
    return cmds.scmh( self.uiName , q=1 , ignore=1 )
  def getrelative( self ):
    return cmds.scmh( self.uiName , q=1 , relative=1 )

  ##### setFuncCode #####
  def setabsolute( self , value ):
    cmds.scmh( self.uiName , e=1 , absolute=value )
  def setignore( self , value ):
    cmds.scmh( self.uiName , e=1 , ignore=value )
  def setrelative( self , value ):
    cmds.scmh( self.uiName , e=1 , relative=value )

  ##### propertyCode #####
  absolute = property( getabsolute , setabsolute )
  ignore = property( getignore , setignore )
  relative = property( getrelative , setrelative )

  ##### customCode #####





class SetMenuMode( object ):

  ##### initialize #####
  def __init__( self , **args ):
    self.uiName = cmds.setMenuMode()

    ##### substitution #####

  ##### getFuncCode #####

  ##### setFuncCode #####

  ##### propertyCode #####

  ##### customCode #####





class SetNodeTypeFlag( object ):

  ##### initialize #####
  def __init__( self , display=None , **args ):
    self.uiName = cmds.setNodeTypeFlag()

    ##### substitution #####
    if display != None:
      self.display = display

  ##### getFuncCode #####
  def getdisplay( self ):
    return cmds.setNodeTypeFlag( self.uiName , q=1 , display=1 )

  ##### setFuncCode #####
  def setdisplay( self , value ):
    cmds.setNodeTypeFlag( self.uiName , e=1 , display=value )

  ##### propertyCode #####
  display = property( getdisplay , setdisplay )

  ##### customCode #####





class SetStartupMessage( object ):

  ##### initialize #####
  def __init__( self , **args ):
    self.uiName = cmds.setStartupMessage()

    ##### substitution #####

  ##### getFuncCode #####

  ##### setFuncCode #####

  ##### propertyCode #####

  ##### customCode #####





class TextManip( object ):

  ##### initialize #####
  def __init__( self , visible=None , **args ):
    self.uiName = cmds.textManip()

    ##### substitution #####
    if visible != None:
      self.visible = visible

  ##### getFuncCode #####
  def getvisible( self ):
    return cmds.textManip( self.uiName , q=1 , visible=1 )

  ##### setFuncCode #####
  def setvisible( self , value ):
    cmds.textManip( self.uiName , e=1 , visible=value )

  ##### propertyCode #####
  visible = property( getvisible , setvisible )

  ##### customCode #####





class SetParent( object ):

  ##### initialize #####
  def __init__( self , defineTemplate=None , menu=None , topLevel=None , upLevel=None , useTemplate=None , **args ):
    self.uiName = cmds.setParent("..")

    ##### substitution #####
    if defineTemplate != None:
      self.defineTemplate = defineTemplate
    if menu != None:
      self.menu = menu
    if topLevel != None:
      self.topLevel = topLevel
    if upLevel != None:
      self.upLevel = upLevel
    if useTemplate != None:
      self.useTemplate = useTemplate

  ##### getFuncCode #####
  def getdefineTemplate( self ):
    return cmds.setParent( self.uiName , q=1 , defineTemplate=1 )
  def getmenu( self ):
    return cmds.setParent( self.uiName , q=1 , menu=1 )
  def gettopLevel( self ):
    return cmds.setParent( self.uiName , q=1 , topLevel=1 )
  def getupLevel( self ):
    return cmds.setParent( self.uiName , q=1 , upLevel=1 )
  def getuseTemplate( self ):
    return cmds.setParent( self.uiName , q=1 , useTemplate=1 )

  ##### setFuncCode #####
  def setdefineTemplate( self , value ):
    cmds.setParent( self.uiName , e=1 , defineTemplate=value )
  def setmenu( self , value ):
    cmds.setParent( self.uiName , e=1 , menu=value )
  def settopLevel( self , value ):
    cmds.setParent( self.uiName , e=1 , topLevel=value )
  def setupLevel( self , value ):
    cmds.setParent( self.uiName , e=1 , upLevel=value )
  def setuseTemplate( self , value ):
    cmds.setParent( self.uiName , e=1 , useTemplate=value )

  ##### propertyCode #####
  defineTemplate = property( getdefineTemplate , setdefineTemplate )
  menu = property( getmenu , setmenu )
  topLevel = property( gettopLevel , settopLevel )
  upLevel = property( getupLevel , setupLevel )
  useTemplate = property( getuseTemplate , setuseTemplate )

  ##### customCode #####





print "MODULE IMPORTED... MYAM_PyLib_mayaUI_other"