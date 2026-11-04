#-*- coding:UTF-8 -*-

#*******************************************************************************
'''

Tool Name     : MYAM_PyLib_mayaUI_panel
Description   : MayaのPanelグループに属するUI要素をオブジェクト指向ライクに扱うためのモジュール

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



class Panel( object ):

  ##### initialize #####
  def __init__( self , copy=None , createString=None , control=None , defineTemplate=None , docTag=None , editString=None , exists=None , init=None , isUnique=None , label=None , menuBarVisible=None , needsInit=None , parent=None , popupMenuProcedure=None , replacePanel=None , tearOff=None , tearOffCopy=None , unParent=None , useTemplate=None , **args ):
    self.uiName = cmds.panel()

    ##### substitution #####
    if copy != None:
      self.copy = copy
    if createString != None:
      self.createString = createString
    if control != None:
      self.control = control
    if defineTemplate != None:
      self.defineTemplate = defineTemplate
    if docTag != None:
      self.docTag = docTag
    if editString != None:
      self.editString = editString
    if exists != None:
      self.exists = exists
    if init != None:
      self.init = init
    if isUnique != None:
      self.isUnique = isUnique
    if label != None:
      self.label = label
    if menuBarVisible != None:
      self.menuBarVisible = menuBarVisible
    if needsInit != None:
      self.needsInit = needsInit
    if parent != None:
      self.parent = parent
    if popupMenuProcedure != None:
      self.popupMenuProcedure = popupMenuProcedure
    if replacePanel != None:
      self.replacePanel = replacePanel
    if tearOff != None:
      self.tearOff = tearOff
    if tearOffCopy != None:
      self.tearOffCopy = tearOffCopy
    if unParent != None:
      self.unParent = unParent
    if useTemplate != None:
      self.useTemplate = useTemplate

  ##### getFuncCode #####
  def getcopy( self ):
    return cmds.panel( self.uiName , q=1 , copy=1 )
  def getcreateString( self ):
    return cmds.panel( self.uiName , q=1 , createString=1 )
  def getcontrol( self ):
    return cmds.panel( self.uiName , q=1 , control=1 )
  def getdefineTemplate( self ):
    return cmds.panel( self.uiName , q=1 , defineTemplate=1 )
  def getdocTag( self ):
    return cmds.panel( self.uiName , q=1 , docTag=1 )
  def geteditString( self ):
    return cmds.panel( self.uiName , q=1 , editString=1 )
  def getexists( self ):
    return cmds.panel( self.uiName , q=1 , exists=1 )
  def getinit( self ):
    return cmds.panel( self.uiName , q=1 , init=1 )
  def getisUnique( self ):
    return cmds.panel( self.uiName , q=1 , isUnique=1 )
  def getlabel( self ):
    return cmds.panel( self.uiName , q=1 , label=1 )
  def getmenuBarVisible( self ):
    return cmds.panel( self.uiName , q=1 , menuBarVisible=1 )
  def getneedsInit( self ):
    return cmds.panel( self.uiName , q=1 , needsInit=1 )
  def getparent( self ):
    return cmds.panel( self.uiName , q=1 , parent=1 )
  def getpopupMenuProcedure( self ):
    return cmds.panel( self.uiName , q=1 , popupMenuProcedure=1 )
  def getreplacePanel( self ):
    return cmds.panel( self.uiName , q=1 , replacePanel=1 )
  def gettearOff( self ):
    return cmds.panel( self.uiName , q=1 , tearOff=1 )
  def gettearOffCopy( self ):
    return cmds.panel( self.uiName , q=1 , tearOffCopy=1 )
  def getunParent( self ):
    return cmds.panel( self.uiName , q=1 , unParent=1 )
  def getuseTemplate( self ):
    return cmds.panel( self.uiName , q=1 , useTemplate=1 )

  ##### setFuncCode #####
  def setcopy( self , value ):
    cmds.panel( self.uiName , e=1 , copy=value )
  def setcreateString( self , value ):
    cmds.panel( self.uiName , e=1 , createString=value )
  def setcontrol( self , value ):
    cmds.panel( self.uiName , e=1 , control=value )
  def setdefineTemplate( self , value ):
    cmds.panel( self.uiName , e=1 , defineTemplate=value )
  def setdocTag( self , value ):
    cmds.panel( self.uiName , e=1 , docTag=value )
  def seteditString( self , value ):
    cmds.panel( self.uiName , e=1 , editString=value )
  def setexists( self , value ):
    cmds.panel( self.uiName , e=1 , exists=value )
  def setinit( self , value ):
    cmds.panel( self.uiName , e=1 , init=value )
  def setisUnique( self , value ):
    cmds.panel( self.uiName , e=1 , isUnique=value )
  def setlabel( self , value ):
    cmds.panel( self.uiName , e=1 , label=value )
  def setmenuBarVisible( self , value ):
    cmds.panel( self.uiName , e=1 , menuBarVisible=value )
  def setneedsInit( self , value ):
    cmds.panel( self.uiName , e=1 , needsInit=value )
  def setparent( self , value ):
    cmds.panel( self.uiName , e=1 , parent=value )
  def setpopupMenuProcedure( self , value ):
    cmds.panel( self.uiName , e=1 , popupMenuProcedure=value )
  def setreplacePanel( self , value ):
    cmds.panel( self.uiName , e=1 , replacePanel=value )
  def settearOff( self , value ):
    cmds.panel( self.uiName , e=1 , tearOff=value )
  def settearOffCopy( self , value ):
    cmds.panel( self.uiName , e=1 , tearOffCopy=value )
  def setunParent( self , value ):
    cmds.panel( self.uiName , e=1 , unParent=value )
  def setuseTemplate( self , value ):
    cmds.panel( self.uiName , e=1 , useTemplate=value )

  ##### propertyCode #####
  copy = property( getcopy , setcopy )
  createString = property( getcreateString , setcreateString )
  control = property( getcontrol , setcontrol )
  defineTemplate = property( getdefineTemplate , setdefineTemplate )
  docTag = property( getdocTag , setdocTag )
  editString = property( geteditString , seteditString )
  exists = property( getexists , setexists )
  init = property( getinit , setinit )
  isUnique = property( getisUnique , setisUnique )
  label = property( getlabel , setlabel )
  menuBarVisible = property( getmenuBarVisible , setmenuBarVisible )
  needsInit = property( getneedsInit , setneedsInit )
  parent = property( getparent , setparent )
  popupMenuProcedure = property( getpopupMenuProcedure , setpopupMenuProcedure )
  replacePanel = property( getreplacePanel , setreplacePanel )
  tearOff = property( gettearOff , settearOff )
  tearOffCopy = property( gettearOffCopy , settearOffCopy )
  unParent = property( getunParent , setunParent )
  useTemplate = property( getuseTemplate , setuseTemplate )

  ##### customCode #####





class ComponentEditor( Panel ):

  ##### initialize #####
  def __init__( self , filter=None , floatField=None , forceMainConnection=None , floatSlider=None , highlightConnection=None , hidePathName=None , hideZeroColumns=None , lockMainConnection=None , lockInput=None , mainListConnection=None , newTab=None , operationCount=None , operationLabels=None , operationType=None , panel=None , precision=None , removeTab=None , sortAlpha=None , selected=None , selectionConnection=None , showObjects=None , setOperationLabel=None , showSelected=None , stateString=None , unlockMainConnection=None , updateMainConnection=None , **args ):
    self.uiName = cmds.componentEditor()

    ##### substitution #####
    if filter != None:
      self.filter = filter
    if floatField != None:
      self.floatField = floatField
    if forceMainConnection != None:
      self.forceMainConnection = forceMainConnection
    if floatSlider != None:
      self.floatSlider = floatSlider
    if highlightConnection != None:
      self.highlightConnection = highlightConnection
    if hidePathName != None:
      self.hidePathName = hidePathName
    if hideZeroColumns != None:
      self.hideZeroColumns = hideZeroColumns
    if lockMainConnection != None:
      self.lockMainConnection = lockMainConnection
    if lockInput != None:
      self.lockInput = lockInput
    if mainListConnection != None:
      self.mainListConnection = mainListConnection
    if newTab != None:
      self.newTab = newTab
    if operationCount != None:
      self.operationCount = operationCount
    if operationLabels != None:
      self.operationLabels = operationLabels
    if operationType != None:
      self.operationType = operationType
    if panel != None:
      self.panel = panel
    if precision != None:
      self.precision = precision
    if removeTab != None:
      self.removeTab = removeTab
    if sortAlpha != None:
      self.sortAlpha = sortAlpha
    if selected != None:
      self.selected = selected
    if selectionConnection != None:
      self.selectionConnection = selectionConnection
    if showObjects != None:
      self.showObjects = showObjects
    if setOperationLabel != None:
      self.setOperationLabel = setOperationLabel
    if showSelected != None:
      self.showSelected = showSelected
    if stateString != None:
      self.stateString = stateString
    if unlockMainConnection != None:
      self.unlockMainConnection = unlockMainConnection
    if updateMainConnection != None:
      self.updateMainConnection = updateMainConnection

  ##### getFuncCode #####
  def getfilter( self ):
    return cmds.componentEditor( self.uiName , q=1 , filter=1 )
  def getfloatField( self ):
    return cmds.componentEditor( self.uiName , q=1 , floatField=1 )
  def getforceMainConnection( self ):
    return cmds.componentEditor( self.uiName , q=1 , forceMainConnection=1 )
  def getfloatSlider( self ):
    return cmds.componentEditor( self.uiName , q=1 , floatSlider=1 )
  def gethighlightConnection( self ):
    return cmds.componentEditor( self.uiName , q=1 , highlightConnection=1 )
  def gethidePathName( self ):
    return cmds.componentEditor( self.uiName , q=1 , hidePathName=1 )
  def gethideZeroColumns( self ):
    return cmds.componentEditor( self.uiName , q=1 , hideZeroColumns=1 )
  def getlockMainConnection( self ):
    return cmds.componentEditor( self.uiName , q=1 , lockMainConnection=1 )
  def getlockInput( self ):
    return cmds.componentEditor( self.uiName , q=1 , lockInput=1 )
  def getmainListConnection( self ):
    return cmds.componentEditor( self.uiName , q=1 , mainListConnection=1 )
  def getnewTab( self ):
    return cmds.componentEditor( self.uiName , q=1 , newTab=1 )
  def getoperationCount( self ):
    return cmds.componentEditor( self.uiName , q=1 , operationCount=1 )
  def getoperationLabels( self ):
    return cmds.componentEditor( self.uiName , q=1 , operationLabels=1 )
  def getoperationType( self ):
    return cmds.componentEditor( self.uiName , q=1 , operationType=1 )
  def getpanel( self ):
    return cmds.componentEditor( self.uiName , q=1 , panel=1 )
  def getprecision( self ):
    return cmds.componentEditor( self.uiName , q=1 , precision=1 )
  def getremoveTab( self ):
    return cmds.componentEditor( self.uiName , q=1 , removeTab=1 )
  def getsortAlpha( self ):
    return cmds.componentEditor( self.uiName , q=1 , sortAlpha=1 )
  def getselected( self ):
    return cmds.componentEditor( self.uiName , q=1 , selected=1 )
  def getselectionConnection( self ):
    return cmds.componentEditor( self.uiName , q=1 , selectionConnection=1 )
  def getshowObjects( self ):
    return cmds.componentEditor( self.uiName , q=1 , showObjects=1 )
  def getsetOperationLabel( self ):
    return cmds.componentEditor( self.uiName , q=1 , setOperationLabel=1 )
  def getshowSelected( self ):
    return cmds.componentEditor( self.uiName , q=1 , showSelected=1 )
  def getstateString( self ):
    return cmds.componentEditor( self.uiName , q=1 , stateString=1 )
  def getunlockMainConnection( self ):
    return cmds.componentEditor( self.uiName , q=1 , unlockMainConnection=1 )
  def getupdateMainConnection( self ):
    return cmds.componentEditor( self.uiName , q=1 , updateMainConnection=1 )

  ##### setFuncCode #####
  def setfilter( self , value ):
    cmds.componentEditor( self.uiName , e=1 , filter=value )
  def setfloatField( self , value ):
    cmds.componentEditor( self.uiName , e=1 , floatField=value )
  def setforceMainConnection( self , value ):
    cmds.componentEditor( self.uiName , e=1 , forceMainConnection=value )
  def setfloatSlider( self , value ):
    cmds.componentEditor( self.uiName , e=1 , floatSlider=value )
  def sethighlightConnection( self , value ):
    cmds.componentEditor( self.uiName , e=1 , highlightConnection=value )
  def sethidePathName( self , value ):
    cmds.componentEditor( self.uiName , e=1 , hidePathName=value )
  def sethideZeroColumns( self , value ):
    cmds.componentEditor( self.uiName , e=1 , hideZeroColumns=value )
  def setlockMainConnection( self , value ):
    cmds.componentEditor( self.uiName , e=1 , lockMainConnection=value )
  def setlockInput( self , value ):
    cmds.componentEditor( self.uiName , e=1 , lockInput=value )
  def setmainListConnection( self , value ):
    cmds.componentEditor( self.uiName , e=1 , mainListConnection=value )
  def setnewTab( self , value ):
    cmds.componentEditor( self.uiName , e=1 , newTab=value )
  def setoperationCount( self , value ):
    cmds.componentEditor( self.uiName , e=1 , operationCount=value )
  def setoperationLabels( self , value ):
    cmds.componentEditor( self.uiName , e=1 , operationLabels=value )
  def setoperationType( self , value ):
    cmds.componentEditor( self.uiName , e=1 , operationType=value )
  def setpanel( self , value ):
    cmds.componentEditor( self.uiName , e=1 , panel=value )
  def setprecision( self , value ):
    cmds.componentEditor( self.uiName , e=1 , precision=value )
  def setremoveTab( self , value ):
    cmds.componentEditor( self.uiName , e=1 , removeTab=value )
  def setsortAlpha( self , value ):
    cmds.componentEditor( self.uiName , e=1 , sortAlpha=value )
  def setselected( self , value ):
    cmds.componentEditor( self.uiName , e=1 , selected=value )
  def setselectionConnection( self , value ):
    cmds.componentEditor( self.uiName , e=1 , selectionConnection=value )
  def setshowObjects( self , value ):
    cmds.componentEditor( self.uiName , e=1 , showObjects=value )
  def setsetOperationLabel( self , value ):
    cmds.componentEditor( self.uiName , e=1 , setOperationLabel=value )
  def setshowSelected( self , value ):
    cmds.componentEditor( self.uiName , e=1 , showSelected=value )
  def setstateString( self , value ):
    cmds.componentEditor( self.uiName , e=1 , stateString=value )
  def setunlockMainConnection( self , value ):
    cmds.componentEditor( self.uiName , e=1 , unlockMainConnection=value )
  def setupdateMainConnection( self , value ):
    cmds.componentEditor( self.uiName , e=1 , updateMainConnection=value )

  ##### propertyCode #####
  filter = property( getfilter , setfilter )
  floatField = property( getfloatField , setfloatField )
  forceMainConnection = property( getforceMainConnection , setforceMainConnection )
  floatSlider = property( getfloatSlider , setfloatSlider )
  highlightConnection = property( gethighlightConnection , sethighlightConnection )
  hidePathName = property( gethidePathName , sethidePathName )
  hideZeroColumns = property( gethideZeroColumns , sethideZeroColumns )
  lockMainConnection = property( getlockMainConnection , setlockMainConnection )
  lockInput = property( getlockInput , setlockInput )
  mainListConnection = property( getmainListConnection , setmainListConnection )
  newTab = property( getnewTab , setnewTab )
  operationCount = property( getoperationCount , setoperationCount )
  operationLabels = property( getoperationLabels , setoperationLabels )
  operationType = property( getoperationType , setoperationType )
  panel = property( getpanel , setpanel )
  precision = property( getprecision , setprecision )
  removeTab = property( getremoveTab , setremoveTab )
  sortAlpha = property( getsortAlpha , setsortAlpha )
  selected = property( getselected , setselected )
  selectionConnection = property( getselectionConnection , setselectionConnection )
  showObjects = property( getshowObjects , setshowObjects )
  setOperationLabel = property( getsetOperationLabel , setsetOperationLabel )
  showSelected = property( getshowSelected , setshowSelected )
  stateString = property( getstateString , setstateString )
  unlockMainConnection = property( getunlockMainConnection , setunlockMainConnection )
  updateMainConnection = property( getupdateMainConnection , setupdateMainConnection )

  ##### customCode #####





class GetPanel( Panel ):

  ##### initialize #####
  def __init__( self , allConfigs=None , allPanels=None , allScriptedTypes=None , allTypes=None , containing=None , configWithLabel=None , invisiblePanels=None , scriptType=None , typeOf=None , type=None , underPointer=None , visiblePanels=None , withFocus=None , withLabel=None , **args ):
    self.uiName = cmds.getPanel()

    ##### substitution #####
    if allConfigs != None:
      self.allConfigs = allConfigs
    if allPanels != None:
      self.allPanels = allPanels
    if allScriptedTypes != None:
      self.allScriptedTypes = allScriptedTypes
    if allTypes != None:
      self.allTypes = allTypes
    if containing != None:
      self.containing = containing
    if configWithLabel != None:
      self.configWithLabel = configWithLabel
    if invisiblePanels != None:
      self.invisiblePanels = invisiblePanels
    if scriptType != None:
      self.scriptType = scriptType
    if typeOf != None:
      self.typeOf = typeOf
    if type != None:
      self.type = type
    if underPointer != None:
      self.underPointer = underPointer
    if visiblePanels != None:
      self.visiblePanels = visiblePanels
    if withFocus != None:
      self.withFocus = withFocus
    if withLabel != None:
      self.withLabel = withLabel

  ##### getFuncCode #####
  def getallConfigs( self ):
    return cmds.getPanel( self.uiName , q=1 , allConfigs=1 )
  def getallPanels( self ):
    return cmds.getPanel( self.uiName , q=1 , allPanels=1 )
  def getallScriptedTypes( self ):
    return cmds.getPanel( self.uiName , q=1 , allScriptedTypes=1 )
  def getallTypes( self ):
    return cmds.getPanel( self.uiName , q=1 , allTypes=1 )
  def getcontaining( self ):
    return cmds.getPanel( self.uiName , q=1 , containing=1 )
  def getconfigWithLabel( self ):
    return cmds.getPanel( self.uiName , q=1 , configWithLabel=1 )
  def getinvisiblePanels( self ):
    return cmds.getPanel( self.uiName , q=1 , invisiblePanels=1 )
  def getscriptType( self ):
    return cmds.getPanel( self.uiName , q=1 , scriptType=1 )
  def gettypeOf( self ):
    return cmds.getPanel( self.uiName , q=1 , typeOf=1 )
  def gettype( self ):
    return cmds.getPanel( self.uiName , q=1 , type=1 )
  def getunderPointer( self ):
    return cmds.getPanel( self.uiName , q=1 , underPointer=1 )
  def getvisiblePanels( self ):
    return cmds.getPanel( self.uiName , q=1 , visiblePanels=1 )
  def getwithFocus( self ):
    return cmds.getPanel( self.uiName , q=1 , withFocus=1 )
  def getwithLabel( self ):
    return cmds.getPanel( self.uiName , q=1 , withLabel=1 )

  ##### setFuncCode #####
  def setallConfigs( self , value ):
    cmds.getPanel( self.uiName , e=1 , allConfigs=value )
  def setallPanels( self , value ):
    cmds.getPanel( self.uiName , e=1 , allPanels=value )
  def setallScriptedTypes( self , value ):
    cmds.getPanel( self.uiName , e=1 , allScriptedTypes=value )
  def setallTypes( self , value ):
    cmds.getPanel( self.uiName , e=1 , allTypes=value )
  def setcontaining( self , value ):
    cmds.getPanel( self.uiName , e=1 , containing=value )
  def setconfigWithLabel( self , value ):
    cmds.getPanel( self.uiName , e=1 , configWithLabel=value )
  def setinvisiblePanels( self , value ):
    cmds.getPanel( self.uiName , e=1 , invisiblePanels=value )
  def setscriptType( self , value ):
    cmds.getPanel( self.uiName , e=1 , scriptType=value )
  def settypeOf( self , value ):
    cmds.getPanel( self.uiName , e=1 , typeOf=value )
  def settype( self , value ):
    cmds.getPanel( self.uiName , e=1 , type=value )
  def setunderPointer( self , value ):
    cmds.getPanel( self.uiName , e=1 , underPointer=value )
  def setvisiblePanels( self , value ):
    cmds.getPanel( self.uiName , e=1 , visiblePanels=value )
  def setwithFocus( self , value ):
    cmds.getPanel( self.uiName , e=1 , withFocus=value )
  def setwithLabel( self , value ):
    cmds.getPanel( self.uiName , e=1 , withLabel=value )

  ##### propertyCode #####
  allConfigs = property( getallConfigs , setallConfigs )
  allPanels = property( getallPanels , setallPanels )
  allScriptedTypes = property( getallScriptedTypes , setallScriptedTypes )
  allTypes = property( getallTypes , setallTypes )
  containing = property( getcontaining , setcontaining )
  configWithLabel = property( getconfigWithLabel , setconfigWithLabel )
  invisiblePanels = property( getinvisiblePanels , setinvisiblePanels )
  scriptType = property( getscriptType , setscriptType )
  typeOf = property( gettypeOf , settypeOf )
  type = property( gettype , settype )
  underPointer = property( getunderPointer , setunderPointer )
  visiblePanels = property( getvisiblePanels , setvisiblePanels )
  withFocus = property( getwithFocus , setwithFocus )
  withLabel = property( getwithLabel , setwithLabel )

  ##### customCode #####





class HardwareRenderPanel( Panel ):

  ##### initialize #####
  def __init__( self , camera=None , glRenderEditor=None , **args ):
    self.uiName = cmds.hardwareRenderPanel()

    ##### substitution #####
    if camera != None:
      self.camera = camera
    if glRenderEditor != None:
      self.glRenderEditor = glRenderEditor

  ##### getFuncCode #####
  def getcamera( self ):
    return cmds.hardwareRenderPanel( self.uiName , q=1 , camera=1 )
  def getglRenderEditor( self ):
    return cmds.hardwareRenderPanel( self.uiName , q=1 , glRenderEditor=1 )

  ##### setFuncCode #####
  def setcamera( self , value ):
    cmds.hardwareRenderPanel( self.uiName , e=1 , camera=value )
  def setglRenderEditor( self , value ):
    cmds.hardwareRenderPanel( self.uiName , e=1 , glRenderEditor=value )

  ##### propertyCode #####
  camera = property( getcamera , setcamera )
  glRenderEditor = property( getglRenderEditor , setglRenderEditor )

  ##### customCode #####





class HyperGraph( Panel ):

  ##### initialize #####
  def __init__( self , addBookmark=None , addDependGraph=None , addDependNode=None , attributeEditor=None , animateTransition=None , backward=None , breakConnectionCommand=None , bookmarkName=None , collapseContainer=None , connectionDrawStyle=None , currentEdge=None , clear=None , currentNode=None , deleteBookmark=None , dragAndDropBehaviorCommand=None , debug=None , dependGraph=None , dependNode=None , down=None , directoryPressCommand=None , dropNode=None , useDrawOverrideColor=None , dropTargetNode=None , downstream=None , enableAutomaticLayout=None , expandContainer=None , edgeDblClickCommand=None , edgeDimmedDblClickCommand=None , edgeDropCommand=None , edgePressCommand=None , edgeReleaseCommand=None , filter=None , fromAttr=None , feedbackGadget=None , feedbackNode=None , focusCommand=None , filterDetail=None , frameGraph=None , frameGraphNoRebuild=None , fitImageToHeight=None , fitImageToWidth=None , forceMainConnection=None , fold=None , forward=None , frame=None , frameBranch=None , freeform=None , forceRefresh=None , frameHierarchy=None , fromNode=None , graphDescription=None , graphLayoutStyle=None , getNodeList=None , getNodePosition=None , graphType=None , highlightConnection=None , heatMapDisplay=None , navigateHome=None , iconSize=None , imageForContainer=None , isHotkeyTarget=None , imageEnabled=None , image=None , imagePosition=None , imageScale=None , initializeScript=None , layout=None , lockMainConnection=None , limitGraphTraversal=None , look=None , layoutSubtree=None , layoutSelected=None , mergeConnections=None , mainListConnection=None , nodeConnectCommand=None , nodeDblClickCommand=None , nodeDropCommand=None , newInputConnection=None , nodeMenuCommand=None , newOutputConnection=None , nodePressCommand=None , nodeReleaseCommand=None , navup=None , nextView=None , opaqueContainers=None , orientation=None , panView=None , popupMenuScript=None , panel=None , previousView=None , rebuild=None , restoreBookmark=None , resetFreeform=None , range=None , removeNode=None , rename=None , showCachedConnections=None , showConstraints=None , showDeformers=None , showInvisible=None , showRelationships=None , showShapes=None , showUnderworld=None , showExpressions=None , selectionConnection=None , setNodePosition=None , scrollUpDownNoZoom=None , stateString=None , toAttr=None , transitionFrames=None , toNode=None , unfoldAll=None , unfoldAllShapes=None , unfold=None , unfoldHidden=None , useFeedbackList=None , unlockMainConnection=None , updateNodeAdded=None , updateMainConnection=None , upstream=None , updateSelection=None , visibility=None , viewOption=None , zoom=None , **args ):
    self.uiName = cmds.hyperGraph()

    ##### substitution #####
    if addBookmark != None:
      self.addBookmark = addBookmark
    if addDependGraph != None:
      self.addDependGraph = addDependGraph
    if addDependNode != None:
      self.addDependNode = addDependNode
    if attributeEditor != None:
      self.attributeEditor = attributeEditor
    if animateTransition != None:
      self.animateTransition = animateTransition
    if backward != None:
      self.backward = backward
    if breakConnectionCommand != None:
      self.breakConnectionCommand = breakConnectionCommand
    if bookmarkName != None:
      self.bookmarkName = bookmarkName
    if collapseContainer != None:
      self.collapseContainer = collapseContainer
    if connectionDrawStyle != None:
      self.connectionDrawStyle = connectionDrawStyle
    if currentEdge != None:
      self.currentEdge = currentEdge
    if clear != None:
      self.clear = clear
    if currentNode != None:
      self.currentNode = currentNode
    if deleteBookmark != None:
      self.deleteBookmark = deleteBookmark
    if dragAndDropBehaviorCommand != None:
      self.dragAndDropBehaviorCommand = dragAndDropBehaviorCommand
    if debug != None:
      self.debug = debug
    if dependGraph != None:
      self.dependGraph = dependGraph
    if dependNode != None:
      self.dependNode = dependNode
    if down != None:
      self.down = down
    if directoryPressCommand != None:
      self.directoryPressCommand = directoryPressCommand
    if dropNode != None:
      self.dropNode = dropNode
    if useDrawOverrideColor != None:
      self.useDrawOverrideColor = useDrawOverrideColor
    if dropTargetNode != None:
      self.dropTargetNode = dropTargetNode
    if downstream != None:
      self.downstream = downstream
    if enableAutomaticLayout != None:
      self.enableAutomaticLayout = enableAutomaticLayout
    if expandContainer != None:
      self.expandContainer = expandContainer
    if edgeDblClickCommand != None:
      self.edgeDblClickCommand = edgeDblClickCommand
    if edgeDimmedDblClickCommand != None:
      self.edgeDimmedDblClickCommand = edgeDimmedDblClickCommand
    if edgeDropCommand != None:
      self.edgeDropCommand = edgeDropCommand
    if edgePressCommand != None:
      self.edgePressCommand = edgePressCommand
    if edgeReleaseCommand != None:
      self.edgeReleaseCommand = edgeReleaseCommand
    if filter != None:
      self.filter = filter
    if fromAttr != None:
      self.fromAttr = fromAttr
    if feedbackGadget != None:
      self.feedbackGadget = feedbackGadget
    if feedbackNode != None:
      self.feedbackNode = feedbackNode
    if focusCommand != None:
      self.focusCommand = focusCommand
    if filterDetail != None:
      self.filterDetail = filterDetail
    if frameGraph != None:
      self.frameGraph = frameGraph
    if frameGraphNoRebuild != None:
      self.frameGraphNoRebuild = frameGraphNoRebuild
    if fitImageToHeight != None:
      self.fitImageToHeight = fitImageToHeight
    if fitImageToWidth != None:
      self.fitImageToWidth = fitImageToWidth
    if forceMainConnection != None:
      self.forceMainConnection = forceMainConnection
    if fold != None:
      self.fold = fold
    if forward != None:
      self.forward = forward
    if frame != None:
      self.frame = frame
    if frameBranch != None:
      self.frameBranch = frameBranch
    if freeform != None:
      self.freeform = freeform
    if forceRefresh != None:
      self.forceRefresh = forceRefresh
    if frameHierarchy != None:
      self.frameHierarchy = frameHierarchy
    if fromNode != None:
      self.fromNode = fromNode
    if graphDescription != None:
      self.graphDescription = graphDescription
    if graphLayoutStyle != None:
      self.graphLayoutStyle = graphLayoutStyle
    if getNodeList != None:
      self.getNodeList = getNodeList
    if getNodePosition != None:
      self.getNodePosition = getNodePosition
    if graphType != None:
      self.graphType = graphType
    if highlightConnection != None:
      self.highlightConnection = highlightConnection
    if heatMapDisplay != None:
      self.heatMapDisplay = heatMapDisplay
    if navigateHome != None:
      self.navigateHome = navigateHome
    if iconSize != None:
      self.iconSize = iconSize
    if imageForContainer != None:
      self.imageForContainer = imageForContainer
    if isHotkeyTarget != None:
      self.isHotkeyTarget = isHotkeyTarget
    if imageEnabled != None:
      self.imageEnabled = imageEnabled
    if image != None:
      self.image = image
    if imagePosition != None:
      self.imagePosition = imagePosition
    if imageScale != None:
      self.imageScale = imageScale
    if initializeScript != None:
      self.initializeScript = initializeScript
    if layout != None:
      self.layout = layout
    if lockMainConnection != None:
      self.lockMainConnection = lockMainConnection
    if limitGraphTraversal != None:
      self.limitGraphTraversal = limitGraphTraversal
    if look != None:
      self.look = look
    if layoutSubtree != None:
      self.layoutSubtree = layoutSubtree
    if layoutSelected != None:
      self.layoutSelected = layoutSelected
    if mergeConnections != None:
      self.mergeConnections = mergeConnections
    if mainListConnection != None:
      self.mainListConnection = mainListConnection
    if nodeConnectCommand != None:
      self.nodeConnectCommand = nodeConnectCommand
    if nodeDblClickCommand != None:
      self.nodeDblClickCommand = nodeDblClickCommand
    if nodeDropCommand != None:
      self.nodeDropCommand = nodeDropCommand
    if newInputConnection != None:
      self.newInputConnection = newInputConnection
    if nodeMenuCommand != None:
      self.nodeMenuCommand = nodeMenuCommand
    if newOutputConnection != None:
      self.newOutputConnection = newOutputConnection
    if nodePressCommand != None:
      self.nodePressCommand = nodePressCommand
    if nodeReleaseCommand != None:
      self.nodeReleaseCommand = nodeReleaseCommand
    if navup != None:
      self.navup = navup
    if nextView != None:
      self.nextView = nextView
    if opaqueContainers != None:
      self.opaqueContainers = opaqueContainers
    if orientation != None:
      self.orientation = orientation
    if panView != None:
      self.panView = panView
    if popupMenuScript != None:
      self.popupMenuScript = popupMenuScript
    if panel != None:
      self.panel = panel
    if previousView != None:
      self.previousView = previousView
    if rebuild != None:
      self.rebuild = rebuild
    if restoreBookmark != None:
      self.restoreBookmark = restoreBookmark
    if resetFreeform != None:
      self.resetFreeform = resetFreeform
    if range != None:
      self.range = range
    if removeNode != None:
      self.removeNode = removeNode
    if rename != None:
      self.rename = rename
    if showCachedConnections != None:
      self.showCachedConnections = showCachedConnections
    if showConstraints != None:
      self.showConstraints = showConstraints
    if showDeformers != None:
      self.showDeformers = showDeformers
    if showInvisible != None:
      self.showInvisible = showInvisible
    if showRelationships != None:
      self.showRelationships = showRelationships
    if showShapes != None:
      self.showShapes = showShapes
    if showUnderworld != None:
      self.showUnderworld = showUnderworld
    if showExpressions != None:
      self.showExpressions = showExpressions
    if selectionConnection != None:
      self.selectionConnection = selectionConnection
    if setNodePosition != None:
      self.setNodePosition = setNodePosition
    if scrollUpDownNoZoom != None:
      self.scrollUpDownNoZoom = scrollUpDownNoZoom
    if stateString != None:
      self.stateString = stateString
    if toAttr != None:
      self.toAttr = toAttr
    if transitionFrames != None:
      self.transitionFrames = transitionFrames
    if toNode != None:
      self.toNode = toNode
    if unfoldAll != None:
      self.unfoldAll = unfoldAll
    if unfoldAllShapes != None:
      self.unfoldAllShapes = unfoldAllShapes
    if unfold != None:
      self.unfold = unfold
    if unfoldHidden != None:
      self.unfoldHidden = unfoldHidden
    if useFeedbackList != None:
      self.useFeedbackList = useFeedbackList
    if unlockMainConnection != None:
      self.unlockMainConnection = unlockMainConnection
    if updateNodeAdded != None:
      self.updateNodeAdded = updateNodeAdded
    if updateMainConnection != None:
      self.updateMainConnection = updateMainConnection
    if upstream != None:
      self.upstream = upstream
    if updateSelection != None:
      self.updateSelection = updateSelection
    if visibility != None:
      self.visibility = visibility
    if viewOption != None:
      self.viewOption = viewOption
    if zoom != None:
      self.zoom = zoom

  ##### getFuncCode #####
  def getaddBookmark( self ):
    return cmds.hyperGraph( self.uiName , q=1 , addBookmark=1 )
  def getaddDependGraph( self ):
    return cmds.hyperGraph( self.uiName , q=1 , addDependGraph=1 )
  def getaddDependNode( self ):
    return cmds.hyperGraph( self.uiName , q=1 , addDependNode=1 )
  def getattributeEditor( self ):
    return cmds.hyperGraph( self.uiName , q=1 , attributeEditor=1 )
  def getanimateTransition( self ):
    return cmds.hyperGraph( self.uiName , q=1 , animateTransition=1 )
  def getbackward( self ):
    return cmds.hyperGraph( self.uiName , q=1 , backward=1 )
  def getbreakConnectionCommand( self ):
    return cmds.hyperGraph( self.uiName , q=1 , breakConnectionCommand=1 )
  def getbookmarkName( self ):
    return cmds.hyperGraph( self.uiName , q=1 , bookmarkName=1 )
  def getcollapseContainer( self ):
    return cmds.hyperGraph( self.uiName , q=1 , collapseContainer=1 )
  def getconnectionDrawStyle( self ):
    return cmds.hyperGraph( self.uiName , q=1 , connectionDrawStyle=1 )
  def getcurrentEdge( self ):
    return cmds.hyperGraph( self.uiName , q=1 , currentEdge=1 )
  def getclear( self ):
    return cmds.hyperGraph( self.uiName , q=1 , clear=1 )
  def getcurrentNode( self ):
    return cmds.hyperGraph( self.uiName , q=1 , currentNode=1 )
  def getdeleteBookmark( self ):
    return cmds.hyperGraph( self.uiName , q=1 , deleteBookmark=1 )
  def getdragAndDropBehaviorCommand( self ):
    return cmds.hyperGraph( self.uiName , q=1 , dragAndDropBehaviorCommand=1 )
  def getdebug( self ):
    return cmds.hyperGraph( self.uiName , q=1 , debug=1 )
  def getdependGraph( self ):
    return cmds.hyperGraph( self.uiName , q=1 , dependGraph=1 )
  def getdependNode( self ):
    return cmds.hyperGraph( self.uiName , q=1 , dependNode=1 )
  def getdown( self ):
    return cmds.hyperGraph( self.uiName , q=1 , down=1 )
  def getdirectoryPressCommand( self ):
    return cmds.hyperGraph( self.uiName , q=1 , directoryPressCommand=1 )
  def getdropNode( self ):
    return cmds.hyperGraph( self.uiName , q=1 , dropNode=1 )
  def getuseDrawOverrideColor( self ):
    return cmds.hyperGraph( self.uiName , q=1 , useDrawOverrideColor=1 )
  def getdropTargetNode( self ):
    return cmds.hyperGraph( self.uiName , q=1 , dropTargetNode=1 )
  def getdownstream( self ):
    return cmds.hyperGraph( self.uiName , q=1 , downstream=1 )
  def getenableAutomaticLayout( self ):
    return cmds.hyperGraph( self.uiName , q=1 , enableAutomaticLayout=1 )
  def getexpandContainer( self ):
    return cmds.hyperGraph( self.uiName , q=1 , expandContainer=1 )
  def getedgeDblClickCommand( self ):
    return cmds.hyperGraph( self.uiName , q=1 , edgeDblClickCommand=1 )
  def getedgeDimmedDblClickCommand( self ):
    return cmds.hyperGraph( self.uiName , q=1 , edgeDimmedDblClickCommand=1 )
  def getedgeDropCommand( self ):
    return cmds.hyperGraph( self.uiName , q=1 , edgeDropCommand=1 )
  def getedgePressCommand( self ):
    return cmds.hyperGraph( self.uiName , q=1 , edgePressCommand=1 )
  def getedgeReleaseCommand( self ):
    return cmds.hyperGraph( self.uiName , q=1 , edgeReleaseCommand=1 )
  def getfilter( self ):
    return cmds.hyperGraph( self.uiName , q=1 , filter=1 )
  def getfromAttr( self ):
    return cmds.hyperGraph( self.uiName , q=1 , fromAttr=1 )
  def getfeedbackGadget( self ):
    return cmds.hyperGraph( self.uiName , q=1 , feedbackGadget=1 )
  def getfeedbackNode( self ):
    return cmds.hyperGraph( self.uiName , q=1 , feedbackNode=1 )
  def getfocusCommand( self ):
    return cmds.hyperGraph( self.uiName , q=1 , focusCommand=1 )
  def getfilterDetail( self ):
    return cmds.hyperGraph( self.uiName , q=1 , filterDetail=1 )
  def getframeGraph( self ):
    return cmds.hyperGraph( self.uiName , q=1 , frameGraph=1 )
  def getframeGraphNoRebuild( self ):
    return cmds.hyperGraph( self.uiName , q=1 , frameGraphNoRebuild=1 )
  def getfitImageToHeight( self ):
    return cmds.hyperGraph( self.uiName , q=1 , fitImageToHeight=1 )
  def getfitImageToWidth( self ):
    return cmds.hyperGraph( self.uiName , q=1 , fitImageToWidth=1 )
  def getforceMainConnection( self ):
    return cmds.hyperGraph( self.uiName , q=1 , forceMainConnection=1 )
  def getfold( self ):
    return cmds.hyperGraph( self.uiName , q=1 , fold=1 )
  def getforward( self ):
    return cmds.hyperGraph( self.uiName , q=1 , forward=1 )
  def getframe( self ):
    return cmds.hyperGraph( self.uiName , q=1 , frame=1 )
  def getframeBranch( self ):
    return cmds.hyperGraph( self.uiName , q=1 , frameBranch=1 )
  def getfreeform( self ):
    return cmds.hyperGraph( self.uiName , q=1 , freeform=1 )
  def getforceRefresh( self ):
    return cmds.hyperGraph( self.uiName , q=1 , forceRefresh=1 )
  def getframeHierarchy( self ):
    return cmds.hyperGraph( self.uiName , q=1 , frameHierarchy=1 )
  def getfromNode( self ):
    return cmds.hyperGraph( self.uiName , q=1 , fromNode=1 )
  def getgraphDescription( self ):
    return cmds.hyperGraph( self.uiName , q=1 , graphDescription=1 )
  def getgraphLayoutStyle( self ):
    return cmds.hyperGraph( self.uiName , q=1 , graphLayoutStyle=1 )
  def getgetNodeList( self ):
    return cmds.hyperGraph( self.uiName , q=1 , getNodeList=1 )
  def getgetNodePosition( self ):
    return cmds.hyperGraph( self.uiName , q=1 , getNodePosition=1 )
  def getgraphType( self ):
    return cmds.hyperGraph( self.uiName , q=1 , graphType=1 )
  def gethighlightConnection( self ):
    return cmds.hyperGraph( self.uiName , q=1 , highlightConnection=1 )
  def getheatMapDisplay( self ):
    return cmds.hyperGraph( self.uiName , q=1 , heatMapDisplay=1 )
  def getnavigateHome( self ):
    return cmds.hyperGraph( self.uiName , q=1 , navigateHome=1 )
  def geticonSize( self ):
    return cmds.hyperGraph( self.uiName , q=1 , iconSize=1 )
  def getimageForContainer( self ):
    return cmds.hyperGraph( self.uiName , q=1 , imageForContainer=1 )
  def getisHotkeyTarget( self ):
    return cmds.hyperGraph( self.uiName , q=1 , isHotkeyTarget=1 )
  def getimageEnabled( self ):
    return cmds.hyperGraph( self.uiName , q=1 , imageEnabled=1 )
  def getimage( self ):
    return cmds.hyperGraph( self.uiName , q=1 , image=1 )
  def getimagePosition( self ):
    return cmds.hyperGraph( self.uiName , q=1 , imagePosition=1 )
  def getimageScale( self ):
    return cmds.hyperGraph( self.uiName , q=1 , imageScale=1 )
  def getinitializeScript( self ):
    return cmds.hyperGraph( self.uiName , q=1 , initializeScript=1 )
  def getlayout( self ):
    return cmds.hyperGraph( self.uiName , q=1 , layout=1 )
  def getlockMainConnection( self ):
    return cmds.hyperGraph( self.uiName , q=1 , lockMainConnection=1 )
  def getlimitGraphTraversal( self ):
    return cmds.hyperGraph( self.uiName , q=1 , limitGraphTraversal=1 )
  def getlook( self ):
    return cmds.hyperGraph( self.uiName , q=1 , look=1 )
  def getlayoutSubtree( self ):
    return cmds.hyperGraph( self.uiName , q=1 , layoutSubtree=1 )
  def getlayoutSelected( self ):
    return cmds.hyperGraph( self.uiName , q=1 , layoutSelected=1 )
  def getmergeConnections( self ):
    return cmds.hyperGraph( self.uiName , q=1 , mergeConnections=1 )
  def getmainListConnection( self ):
    return cmds.hyperGraph( self.uiName , q=1 , mainListConnection=1 )
  def getnodeConnectCommand( self ):
    return cmds.hyperGraph( self.uiName , q=1 , nodeConnectCommand=1 )
  def getnodeDblClickCommand( self ):
    return cmds.hyperGraph( self.uiName , q=1 , nodeDblClickCommand=1 )
  def getnodeDropCommand( self ):
    return cmds.hyperGraph( self.uiName , q=1 , nodeDropCommand=1 )
  def getnewInputConnection( self ):
    return cmds.hyperGraph( self.uiName , q=1 , newInputConnection=1 )
  def getnodeMenuCommand( self ):
    return cmds.hyperGraph( self.uiName , q=1 , nodeMenuCommand=1 )
  def getnewOutputConnection( self ):
    return cmds.hyperGraph( self.uiName , q=1 , newOutputConnection=1 )
  def getnodePressCommand( self ):
    return cmds.hyperGraph( self.uiName , q=1 , nodePressCommand=1 )
  def getnodeReleaseCommand( self ):
    return cmds.hyperGraph( self.uiName , q=1 , nodeReleaseCommand=1 )
  def getnavup( self ):
    return cmds.hyperGraph( self.uiName , q=1 , navup=1 )
  def getnextView( self ):
    return cmds.hyperGraph( self.uiName , q=1 , nextView=1 )
  def getopaqueContainers( self ):
    return cmds.hyperGraph( self.uiName , q=1 , opaqueContainers=1 )
  def getorientation( self ):
    return cmds.hyperGraph( self.uiName , q=1 , orientation=1 )
  def getpanView( self ):
    return cmds.hyperGraph( self.uiName , q=1 , panView=1 )
  def getpopupMenuScript( self ):
    return cmds.hyperGraph( self.uiName , q=1 , popupMenuScript=1 )
  def getpanel( self ):
    return cmds.hyperGraph( self.uiName , q=1 , panel=1 )
  def getpreviousView( self ):
    return cmds.hyperGraph( self.uiName , q=1 , previousView=1 )
  def getrebuild( self ):
    return cmds.hyperGraph( self.uiName , q=1 , rebuild=1 )
  def getrestoreBookmark( self ):
    return cmds.hyperGraph( self.uiName , q=1 , restoreBookmark=1 )
  def getresetFreeform( self ):
    return cmds.hyperGraph( self.uiName , q=1 , resetFreeform=1 )
  def getrange( self ):
    return cmds.hyperGraph( self.uiName , q=1 , range=1 )
  def getremoveNode( self ):
    return cmds.hyperGraph( self.uiName , q=1 , removeNode=1 )
  def getrename( self ):
    return cmds.hyperGraph( self.uiName , q=1 , rename=1 )
  def getshowCachedConnections( self ):
    return cmds.hyperGraph( self.uiName , q=1 , showCachedConnections=1 )
  def getshowConstraints( self ):
    return cmds.hyperGraph( self.uiName , q=1 , showConstraints=1 )
  def getshowDeformers( self ):
    return cmds.hyperGraph( self.uiName , q=1 , showDeformers=1 )
  def getshowInvisible( self ):
    return cmds.hyperGraph( self.uiName , q=1 , showInvisible=1 )
  def getshowRelationships( self ):
    return cmds.hyperGraph( self.uiName , q=1 , showRelationships=1 )
  def getshowShapes( self ):
    return cmds.hyperGraph( self.uiName , q=1 , showShapes=1 )
  def getshowUnderworld( self ):
    return cmds.hyperGraph( self.uiName , q=1 , showUnderworld=1 )
  def getshowExpressions( self ):
    return cmds.hyperGraph( self.uiName , q=1 , showExpressions=1 )
  def getselectionConnection( self ):
    return cmds.hyperGraph( self.uiName , q=1 , selectionConnection=1 )
  def getsetNodePosition( self ):
    return cmds.hyperGraph( self.uiName , q=1 , setNodePosition=1 )
  def getscrollUpDownNoZoom( self ):
    return cmds.hyperGraph( self.uiName , q=1 , scrollUpDownNoZoom=1 )
  def getstateString( self ):
    return cmds.hyperGraph( self.uiName , q=1 , stateString=1 )
  def gettoAttr( self ):
    return cmds.hyperGraph( self.uiName , q=1 , toAttr=1 )
  def gettransitionFrames( self ):
    return cmds.hyperGraph( self.uiName , q=1 , transitionFrames=1 )
  def gettoNode( self ):
    return cmds.hyperGraph( self.uiName , q=1 , toNode=1 )
  def getunfoldAll( self ):
    return cmds.hyperGraph( self.uiName , q=1 , unfoldAll=1 )
  def getunfoldAllShapes( self ):
    return cmds.hyperGraph( self.uiName , q=1 , unfoldAllShapes=1 )
  def getunfold( self ):
    return cmds.hyperGraph( self.uiName , q=1 , unfold=1 )
  def getunfoldHidden( self ):
    return cmds.hyperGraph( self.uiName , q=1 , unfoldHidden=1 )
  def getuseFeedbackList( self ):
    return cmds.hyperGraph( self.uiName , q=1 , useFeedbackList=1 )
  def getunlockMainConnection( self ):
    return cmds.hyperGraph( self.uiName , q=1 , unlockMainConnection=1 )
  def getupdateNodeAdded( self ):
    return cmds.hyperGraph( self.uiName , q=1 , updateNodeAdded=1 )
  def getupdateMainConnection( self ):
    return cmds.hyperGraph( self.uiName , q=1 , updateMainConnection=1 )
  def getupstream( self ):
    return cmds.hyperGraph( self.uiName , q=1 , upstream=1 )
  def getupdateSelection( self ):
    return cmds.hyperGraph( self.uiName , q=1 , updateSelection=1 )
  def getvisibility( self ):
    return cmds.hyperGraph( self.uiName , q=1 , visibility=1 )
  def getviewOption( self ):
    return cmds.hyperGraph( self.uiName , q=1 , viewOption=1 )
  def getzoom( self ):
    return cmds.hyperGraph( self.uiName , q=1 , zoom=1 )

  ##### setFuncCode #####
  def setaddBookmark( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , addBookmark=value )
  def setaddDependGraph( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , addDependGraph=value )
  def setaddDependNode( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , addDependNode=value )
  def setattributeEditor( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , attributeEditor=value )
  def setanimateTransition( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , animateTransition=value )
  def setbackward( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , backward=value )
  def setbreakConnectionCommand( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , breakConnectionCommand=value )
  def setbookmarkName( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , bookmarkName=value )
  def setcollapseContainer( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , collapseContainer=value )
  def setconnectionDrawStyle( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , connectionDrawStyle=value )
  def setcurrentEdge( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , currentEdge=value )
  def setclear( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , clear=value )
  def setcurrentNode( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , currentNode=value )
  def setdeleteBookmark( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , deleteBookmark=value )
  def setdragAndDropBehaviorCommand( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , dragAndDropBehaviorCommand=value )
  def setdebug( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , debug=value )
  def setdependGraph( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , dependGraph=value )
  def setdependNode( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , dependNode=value )
  def setdown( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , down=value )
  def setdirectoryPressCommand( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , directoryPressCommand=value )
  def setdropNode( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , dropNode=value )
  def setuseDrawOverrideColor( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , useDrawOverrideColor=value )
  def setdropTargetNode( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , dropTargetNode=value )
  def setdownstream( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , downstream=value )
  def setenableAutomaticLayout( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , enableAutomaticLayout=value )
  def setexpandContainer( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , expandContainer=value )
  def setedgeDblClickCommand( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , edgeDblClickCommand=value )
  def setedgeDimmedDblClickCommand( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , edgeDimmedDblClickCommand=value )
  def setedgeDropCommand( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , edgeDropCommand=value )
  def setedgePressCommand( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , edgePressCommand=value )
  def setedgeReleaseCommand( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , edgeReleaseCommand=value )
  def setfilter( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , filter=value )
  def setfromAttr( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , fromAttr=value )
  def setfeedbackGadget( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , feedbackGadget=value )
  def setfeedbackNode( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , feedbackNode=value )
  def setfocusCommand( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , focusCommand=value )
  def setfilterDetail( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , filterDetail=value )
  def setframeGraph( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , frameGraph=value )
  def setframeGraphNoRebuild( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , frameGraphNoRebuild=value )
  def setfitImageToHeight( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , fitImageToHeight=value )
  def setfitImageToWidth( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , fitImageToWidth=value )
  def setforceMainConnection( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , forceMainConnection=value )
  def setfold( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , fold=value )
  def setforward( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , forward=value )
  def setframe( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , frame=value )
  def setframeBranch( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , frameBranch=value )
  def setfreeform( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , freeform=value )
  def setforceRefresh( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , forceRefresh=value )
  def setframeHierarchy( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , frameHierarchy=value )
  def setfromNode( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , fromNode=value )
  def setgraphDescription( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , graphDescription=value )
  def setgraphLayoutStyle( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , graphLayoutStyle=value )
  def setgetNodeList( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , getNodeList=value )
  def setgetNodePosition( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , getNodePosition=value )
  def setgraphType( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , graphType=value )
  def sethighlightConnection( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , highlightConnection=value )
  def setheatMapDisplay( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , heatMapDisplay=value )
  def setnavigateHome( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , navigateHome=value )
  def seticonSize( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , iconSize=value )
  def setimageForContainer( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , imageForContainer=value )
  def setisHotkeyTarget( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , isHotkeyTarget=value )
  def setimageEnabled( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , imageEnabled=value )
  def setimage( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , image=value )
  def setimagePosition( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , imagePosition=value )
  def setimageScale( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , imageScale=value )
  def setinitializeScript( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , initializeScript=value )
  def setlayout( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , layout=value )
  def setlockMainConnection( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , lockMainConnection=value )
  def setlimitGraphTraversal( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , limitGraphTraversal=value )
  def setlook( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , look=value )
  def setlayoutSubtree( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , layoutSubtree=value )
  def setlayoutSelected( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , layoutSelected=value )
  def setmergeConnections( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , mergeConnections=value )
  def setmainListConnection( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , mainListConnection=value )
  def setnodeConnectCommand( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , nodeConnectCommand=value )
  def setnodeDblClickCommand( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , nodeDblClickCommand=value )
  def setnodeDropCommand( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , nodeDropCommand=value )
  def setnewInputConnection( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , newInputConnection=value )
  def setnodeMenuCommand( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , nodeMenuCommand=value )
  def setnewOutputConnection( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , newOutputConnection=value )
  def setnodePressCommand( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , nodePressCommand=value )
  def setnodeReleaseCommand( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , nodeReleaseCommand=value )
  def setnavup( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , navup=value )
  def setnextView( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , nextView=value )
  def setopaqueContainers( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , opaqueContainers=value )
  def setorientation( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , orientation=value )
  def setpanView( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , panView=value )
  def setpopupMenuScript( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , popupMenuScript=value )
  def setpanel( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , panel=value )
  def setpreviousView( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , previousView=value )
  def setrebuild( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , rebuild=value )
  def setrestoreBookmark( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , restoreBookmark=value )
  def setresetFreeform( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , resetFreeform=value )
  def setrange( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , range=value )
  def setremoveNode( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , removeNode=value )
  def setrename( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , rename=value )
  def setshowCachedConnections( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , showCachedConnections=value )
  def setshowConstraints( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , showConstraints=value )
  def setshowDeformers( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , showDeformers=value )
  def setshowInvisible( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , showInvisible=value )
  def setshowRelationships( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , showRelationships=value )
  def setshowShapes( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , showShapes=value )
  def setshowUnderworld( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , showUnderworld=value )
  def setshowExpressions( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , showExpressions=value )
  def setselectionConnection( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , selectionConnection=value )
  def setsetNodePosition( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , setNodePosition=value )
  def setscrollUpDownNoZoom( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , scrollUpDownNoZoom=value )
  def setstateString( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , stateString=value )
  def settoAttr( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , toAttr=value )
  def settransitionFrames( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , transitionFrames=value )
  def settoNode( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , toNode=value )
  def setunfoldAll( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , unfoldAll=value )
  def setunfoldAllShapes( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , unfoldAllShapes=value )
  def setunfold( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , unfold=value )
  def setunfoldHidden( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , unfoldHidden=value )
  def setuseFeedbackList( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , useFeedbackList=value )
  def setunlockMainConnection( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , unlockMainConnection=value )
  def setupdateNodeAdded( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , updateNodeAdded=value )
  def setupdateMainConnection( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , updateMainConnection=value )
  def setupstream( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , upstream=value )
  def setupdateSelection( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , updateSelection=value )
  def setvisibility( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , visibility=value )
  def setviewOption( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , viewOption=value )
  def setzoom( self , value ):
    cmds.hyperGraph( self.uiName , e=1 , zoom=value )

  ##### propertyCode #####
  addBookmark = property( getaddBookmark , setaddBookmark )
  addDependGraph = property( getaddDependGraph , setaddDependGraph )
  addDependNode = property( getaddDependNode , setaddDependNode )
  attributeEditor = property( getattributeEditor , setattributeEditor )
  animateTransition = property( getanimateTransition , setanimateTransition )
  backward = property( getbackward , setbackward )
  breakConnectionCommand = property( getbreakConnectionCommand , setbreakConnectionCommand )
  bookmarkName = property( getbookmarkName , setbookmarkName )
  collapseContainer = property( getcollapseContainer , setcollapseContainer )
  connectionDrawStyle = property( getconnectionDrawStyle , setconnectionDrawStyle )
  currentEdge = property( getcurrentEdge , setcurrentEdge )
  clear = property( getclear , setclear )
  currentNode = property( getcurrentNode , setcurrentNode )
  deleteBookmark = property( getdeleteBookmark , setdeleteBookmark )
  dragAndDropBehaviorCommand = property( getdragAndDropBehaviorCommand , setdragAndDropBehaviorCommand )
  debug = property( getdebug , setdebug )
  dependGraph = property( getdependGraph , setdependGraph )
  dependNode = property( getdependNode , setdependNode )
  down = property( getdown , setdown )
  directoryPressCommand = property( getdirectoryPressCommand , setdirectoryPressCommand )
  dropNode = property( getdropNode , setdropNode )
  useDrawOverrideColor = property( getuseDrawOverrideColor , setuseDrawOverrideColor )
  dropTargetNode = property( getdropTargetNode , setdropTargetNode )
  downstream = property( getdownstream , setdownstream )
  enableAutomaticLayout = property( getenableAutomaticLayout , setenableAutomaticLayout )
  expandContainer = property( getexpandContainer , setexpandContainer )
  edgeDblClickCommand = property( getedgeDblClickCommand , setedgeDblClickCommand )
  edgeDimmedDblClickCommand = property( getedgeDimmedDblClickCommand , setedgeDimmedDblClickCommand )
  edgeDropCommand = property( getedgeDropCommand , setedgeDropCommand )
  edgePressCommand = property( getedgePressCommand , setedgePressCommand )
  edgeReleaseCommand = property( getedgeReleaseCommand , setedgeReleaseCommand )
  filter = property( getfilter , setfilter )
  fromAttr = property( getfromAttr , setfromAttr )
  feedbackGadget = property( getfeedbackGadget , setfeedbackGadget )
  feedbackNode = property( getfeedbackNode , setfeedbackNode )
  focusCommand = property( getfocusCommand , setfocusCommand )
  filterDetail = property( getfilterDetail , setfilterDetail )
  frameGraph = property( getframeGraph , setframeGraph )
  frameGraphNoRebuild = property( getframeGraphNoRebuild , setframeGraphNoRebuild )
  fitImageToHeight = property( getfitImageToHeight , setfitImageToHeight )
  fitImageToWidth = property( getfitImageToWidth , setfitImageToWidth )
  forceMainConnection = property( getforceMainConnection , setforceMainConnection )
  fold = property( getfold , setfold )
  forward = property( getforward , setforward )
  frame = property( getframe , setframe )
  frameBranch = property( getframeBranch , setframeBranch )
  freeform = property( getfreeform , setfreeform )
  forceRefresh = property( getforceRefresh , setforceRefresh )
  frameHierarchy = property( getframeHierarchy , setframeHierarchy )
  fromNode = property( getfromNode , setfromNode )
  graphDescription = property( getgraphDescription , setgraphDescription )
  graphLayoutStyle = property( getgraphLayoutStyle , setgraphLayoutStyle )
  getNodeList = property( getgetNodeList , setgetNodeList )
  getNodePosition = property( getgetNodePosition , setgetNodePosition )
  graphType = property( getgraphType , setgraphType )
  highlightConnection = property( gethighlightConnection , sethighlightConnection )
  heatMapDisplay = property( getheatMapDisplay , setheatMapDisplay )
  navigateHome = property( getnavigateHome , setnavigateHome )
  iconSize = property( geticonSize , seticonSize )
  imageForContainer = property( getimageForContainer , setimageForContainer )
  isHotkeyTarget = property( getisHotkeyTarget , setisHotkeyTarget )
  imageEnabled = property( getimageEnabled , setimageEnabled )
  image = property( getimage , setimage )
  imagePosition = property( getimagePosition , setimagePosition )
  imageScale = property( getimageScale , setimageScale )
  initializeScript = property( getinitializeScript , setinitializeScript )
  layout = property( getlayout , setlayout )
  lockMainConnection = property( getlockMainConnection , setlockMainConnection )
  limitGraphTraversal = property( getlimitGraphTraversal , setlimitGraphTraversal )
  look = property( getlook , setlook )
  layoutSubtree = property( getlayoutSubtree , setlayoutSubtree )
  layoutSelected = property( getlayoutSelected , setlayoutSelected )
  mergeConnections = property( getmergeConnections , setmergeConnections )
  mainListConnection = property( getmainListConnection , setmainListConnection )
  nodeConnectCommand = property( getnodeConnectCommand , setnodeConnectCommand )
  nodeDblClickCommand = property( getnodeDblClickCommand , setnodeDblClickCommand )
  nodeDropCommand = property( getnodeDropCommand , setnodeDropCommand )
  newInputConnection = property( getnewInputConnection , setnewInputConnection )
  nodeMenuCommand = property( getnodeMenuCommand , setnodeMenuCommand )
  newOutputConnection = property( getnewOutputConnection , setnewOutputConnection )
  nodePressCommand = property( getnodePressCommand , setnodePressCommand )
  nodeReleaseCommand = property( getnodeReleaseCommand , setnodeReleaseCommand )
  navup = property( getnavup , setnavup )
  nextView = property( getnextView , setnextView )
  opaqueContainers = property( getopaqueContainers , setopaqueContainers )
  orientation = property( getorientation , setorientation )
  panView = property( getpanView , setpanView )
  popupMenuScript = property( getpopupMenuScript , setpopupMenuScript )
  panel = property( getpanel , setpanel )
  previousView = property( getpreviousView , setpreviousView )
  rebuild = property( getrebuild , setrebuild )
  restoreBookmark = property( getrestoreBookmark , setrestoreBookmark )
  resetFreeform = property( getresetFreeform , setresetFreeform )
  range = property( getrange , setrange )
  removeNode = property( getremoveNode , setremoveNode )
  rename = property( getrename , setrename )
  showCachedConnections = property( getshowCachedConnections , setshowCachedConnections )
  showConstraints = property( getshowConstraints , setshowConstraints )
  showDeformers = property( getshowDeformers , setshowDeformers )
  showInvisible = property( getshowInvisible , setshowInvisible )
  showRelationships = property( getshowRelationships , setshowRelationships )
  showShapes = property( getshowShapes , setshowShapes )
  showUnderworld = property( getshowUnderworld , setshowUnderworld )
  showExpressions = property( getshowExpressions , setshowExpressions )
  selectionConnection = property( getselectionConnection , setselectionConnection )
  setNodePosition = property( getsetNodePosition , setsetNodePosition )
  scrollUpDownNoZoom = property( getscrollUpDownNoZoom , setscrollUpDownNoZoom )
  stateString = property( getstateString , setstateString )
  toAttr = property( gettoAttr , settoAttr )
  transitionFrames = property( gettransitionFrames , settransitionFrames )
  toNode = property( gettoNode , settoNode )
  unfoldAll = property( getunfoldAll , setunfoldAll )
  unfoldAllShapes = property( getunfoldAllShapes , setunfoldAllShapes )
  unfold = property( getunfold , setunfold )
  unfoldHidden = property( getunfoldHidden , setunfoldHidden )
  useFeedbackList = property( getuseFeedbackList , setuseFeedbackList )
  unlockMainConnection = property( getunlockMainConnection , setunlockMainConnection )
  updateNodeAdded = property( getupdateNodeAdded , setupdateNodeAdded )
  updateMainConnection = property( getupdateMainConnection , setupdateMainConnection )
  upstream = property( getupstream , setupstream )
  updateSelection = property( getupdateSelection , setupdateSelection )
  visibility = property( getvisibility , setvisibility )
  viewOption = property( getviewOption , setviewOption )
  zoom = property( getzoom , setzoom )

  ##### customCode #####





class HyperPanel( Panel ):

  ##### initialize #####
  def __init__( self , hyperEditor=None , **args ):
    self.uiName = cmds.hyperPanel()

    ##### substitution #####
    if hyperEditor != None:
      self.hyperEditor = hyperEditor

  ##### getFuncCode #####
  def gethyperEditor( self ):
    return cmds.hyperPanel( self.uiName , q=1 , hyperEditor=1 )

  ##### setFuncCode #####
  def sethyperEditor( self , value ):
    cmds.hyperPanel( self.uiName , e=1 , hyperEditor=value )

  ##### propertyCode #####
  hyperEditor = property( gethyperEditor , sethyperEditor )

  ##### customCode #####





class HyperShade( Panel ):

  ##### initialize #####
  def __init__( self , assign=None , collapse=None , clearWorkArea=None , dependGraphArea=None , downStream=None , duplicate=None , fixRenderSize=None , incremental=None , listDownstreamNodes=None , listDownstreamShaderNodes=None , listUpstreamNodes=None , name=None , networks=None , noShapes=None , noSGShapes=None , noTransforms=None , objects=None , renderCreateAndDrop=None , createNode=None , resetGraph=None , resetSwatch=None , reset=None , setAllowsRegraphing=None , shaderNetworksSelectMaterialNodes=None , shaderNetwork=None , snapShot=None , shaderNetworks=None , setWorkArea=None , uncollapse=None , userDefinedLayout=None , upStream=None , workAreaAddCmd=None , workAreaDeleteCmd=None , workAreaSelectCmd=None , **args ):
    self.uiName = cmds.hyperShade()

    ##### substitution #####
    if assign != None:
      self.assign = assign
    if collapse != None:
      self.collapse = collapse
    if clearWorkArea != None:
      self.clearWorkArea = clearWorkArea
    if dependGraphArea != None:
      self.dependGraphArea = dependGraphArea
    if downStream != None:
      self.downStream = downStream
    if duplicate != None:
      self.duplicate = duplicate
    if fixRenderSize != None:
      self.fixRenderSize = fixRenderSize
    if incremental != None:
      self.incremental = incremental
    if listDownstreamNodes != None:
      self.listDownstreamNodes = listDownstreamNodes
    if listDownstreamShaderNodes != None:
      self.listDownstreamShaderNodes = listDownstreamShaderNodes
    if listUpstreamNodes != None:
      self.listUpstreamNodes = listUpstreamNodes
    if name != None:
      self.name = name
    if networks != None:
      self.networks = networks
    if noShapes != None:
      self.noShapes = noShapes
    if noSGShapes != None:
      self.noSGShapes = noSGShapes
    if noTransforms != None:
      self.noTransforms = noTransforms
    if objects != None:
      self.objects = objects
    if renderCreateAndDrop != None:
      self.renderCreateAndDrop = renderCreateAndDrop
    if createNode != None:
      self.createNode = createNode
    if resetGraph != None:
      self.resetGraph = resetGraph
    if resetSwatch != None:
      self.resetSwatch = resetSwatch
    if reset != None:
      self.reset = reset
    if setAllowsRegraphing != None:
      self.setAllowsRegraphing = setAllowsRegraphing
    if shaderNetworksSelectMaterialNodes != None:
      self.shaderNetworksSelectMaterialNodes = shaderNetworksSelectMaterialNodes
    if shaderNetwork != None:
      self.shaderNetwork = shaderNetwork
    if snapShot != None:
      self.snapShot = snapShot
    if shaderNetworks != None:
      self.shaderNetworks = shaderNetworks
    if setWorkArea != None:
      self.setWorkArea = setWorkArea
    if uncollapse != None:
      self.uncollapse = uncollapse
    if userDefinedLayout != None:
      self.userDefinedLayout = userDefinedLayout
    if upStream != None:
      self.upStream = upStream
    if workAreaAddCmd != None:
      self.workAreaAddCmd = workAreaAddCmd
    if workAreaDeleteCmd != None:
      self.workAreaDeleteCmd = workAreaDeleteCmd
    if workAreaSelectCmd != None:
      self.workAreaSelectCmd = workAreaSelectCmd

  ##### getFuncCode #####
  def getassign( self ):
    return cmds.hyperShade( self.uiName , q=1 , assign=1 )
  def getcollapse( self ):
    return cmds.hyperShade( self.uiName , q=1 , collapse=1 )
  def getclearWorkArea( self ):
    return cmds.hyperShade( self.uiName , q=1 , clearWorkArea=1 )
  def getdependGraphArea( self ):
    return cmds.hyperShade( self.uiName , q=1 , dependGraphArea=1 )
  def getdownStream( self ):
    return cmds.hyperShade( self.uiName , q=1 , downStream=1 )
  def getduplicate( self ):
    return cmds.hyperShade( self.uiName , q=1 , duplicate=1 )
  def getfixRenderSize( self ):
    return cmds.hyperShade( self.uiName , q=1 , fixRenderSize=1 )
  def getincremental( self ):
    return cmds.hyperShade( self.uiName , q=1 , incremental=1 )
  def getlistDownstreamNodes( self ):
    return cmds.hyperShade( self.uiName , q=1 , listDownstreamNodes=1 )
  def getlistDownstreamShaderNodes( self ):
    return cmds.hyperShade( self.uiName , q=1 , listDownstreamShaderNodes=1 )
  def getlistUpstreamNodes( self ):
    return cmds.hyperShade( self.uiName , q=1 , listUpstreamNodes=1 )
  def getname( self ):
    return cmds.hyperShade( self.uiName , q=1 , name=1 )
  def getnetworks( self ):
    return cmds.hyperShade( self.uiName , q=1 , networks=1 )
  def getnoShapes( self ):
    return cmds.hyperShade( self.uiName , q=1 , noShapes=1 )
  def getnoSGShapes( self ):
    return cmds.hyperShade( self.uiName , q=1 , noSGShapes=1 )
  def getnoTransforms( self ):
    return cmds.hyperShade( self.uiName , q=1 , noTransforms=1 )
  def getobjects( self ):
    return cmds.hyperShade( self.uiName , q=1 , objects=1 )
  def getrenderCreateAndDrop( self ):
    return cmds.hyperShade( self.uiName , q=1 , renderCreateAndDrop=1 )
  def getcreateNode( self ):
    return cmds.hyperShade( self.uiName , q=1 , createNode=1 )
  def getresetGraph( self ):
    return cmds.hyperShade( self.uiName , q=1 , resetGraph=1 )
  def getresetSwatch( self ):
    return cmds.hyperShade( self.uiName , q=1 , resetSwatch=1 )
  def getreset( self ):
    return cmds.hyperShade( self.uiName , q=1 , reset=1 )
  def getsetAllowsRegraphing( self ):
    return cmds.hyperShade( self.uiName , q=1 , setAllowsRegraphing=1 )
  def getshaderNetworksSelectMaterialNodes( self ):
    return cmds.hyperShade( self.uiName , q=1 , shaderNetworksSelectMaterialNodes=1 )
  def getshaderNetwork( self ):
    return cmds.hyperShade( self.uiName , q=1 , shaderNetwork=1 )
  def getsnapShot( self ):
    return cmds.hyperShade( self.uiName , q=1 , snapShot=1 )
  def getshaderNetworks( self ):
    return cmds.hyperShade( self.uiName , q=1 , shaderNetworks=1 )
  def getsetWorkArea( self ):
    return cmds.hyperShade( self.uiName , q=1 , setWorkArea=1 )
  def getuncollapse( self ):
    return cmds.hyperShade( self.uiName , q=1 , uncollapse=1 )
  def getuserDefinedLayout( self ):
    return cmds.hyperShade( self.uiName , q=1 , userDefinedLayout=1 )
  def getupStream( self ):
    return cmds.hyperShade( self.uiName , q=1 , upStream=1 )
  def getworkAreaAddCmd( self ):
    return cmds.hyperShade( self.uiName , q=1 , workAreaAddCmd=1 )
  def getworkAreaDeleteCmd( self ):
    return cmds.hyperShade( self.uiName , q=1 , workAreaDeleteCmd=1 )
  def getworkAreaSelectCmd( self ):
    return cmds.hyperShade( self.uiName , q=1 , workAreaSelectCmd=1 )

  ##### setFuncCode #####
  def setassign( self , value ):
    cmds.hyperShade( self.uiName , e=1 , assign=value )
  def setcollapse( self , value ):
    cmds.hyperShade( self.uiName , e=1 , collapse=value )
  def setclearWorkArea( self , value ):
    cmds.hyperShade( self.uiName , e=1 , clearWorkArea=value )
  def setdependGraphArea( self , value ):
    cmds.hyperShade( self.uiName , e=1 , dependGraphArea=value )
  def setdownStream( self , value ):
    cmds.hyperShade( self.uiName , e=1 , downStream=value )
  def setduplicate( self , value ):
    cmds.hyperShade( self.uiName , e=1 , duplicate=value )
  def setfixRenderSize( self , value ):
    cmds.hyperShade( self.uiName , e=1 , fixRenderSize=value )
  def setincremental( self , value ):
    cmds.hyperShade( self.uiName , e=1 , incremental=value )
  def setlistDownstreamNodes( self , value ):
    cmds.hyperShade( self.uiName , e=1 , listDownstreamNodes=value )
  def setlistDownstreamShaderNodes( self , value ):
    cmds.hyperShade( self.uiName , e=1 , listDownstreamShaderNodes=value )
  def setlistUpstreamNodes( self , value ):
    cmds.hyperShade( self.uiName , e=1 , listUpstreamNodes=value )
  def setname( self , value ):
    cmds.hyperShade( self.uiName , e=1 , name=value )
  def setnetworks( self , value ):
    cmds.hyperShade( self.uiName , e=1 , networks=value )
  def setnoShapes( self , value ):
    cmds.hyperShade( self.uiName , e=1 , noShapes=value )
  def setnoSGShapes( self , value ):
    cmds.hyperShade( self.uiName , e=1 , noSGShapes=value )
  def setnoTransforms( self , value ):
    cmds.hyperShade( self.uiName , e=1 , noTransforms=value )
  def setobjects( self , value ):
    cmds.hyperShade( self.uiName , e=1 , objects=value )
  def setrenderCreateAndDrop( self , value ):
    cmds.hyperShade( self.uiName , e=1 , renderCreateAndDrop=value )
  def setcreateNode( self , value ):
    cmds.hyperShade( self.uiName , e=1 , createNode=value )
  def setresetGraph( self , value ):
    cmds.hyperShade( self.uiName , e=1 , resetGraph=value )
  def setresetSwatch( self , value ):
    cmds.hyperShade( self.uiName , e=1 , resetSwatch=value )
  def setreset( self , value ):
    cmds.hyperShade( self.uiName , e=1 , reset=value )
  def setsetAllowsRegraphing( self , value ):
    cmds.hyperShade( self.uiName , e=1 , setAllowsRegraphing=value )
  def setshaderNetworksSelectMaterialNodes( self , value ):
    cmds.hyperShade( self.uiName , e=1 , shaderNetworksSelectMaterialNodes=value )
  def setshaderNetwork( self , value ):
    cmds.hyperShade( self.uiName , e=1 , shaderNetwork=value )
  def setsnapShot( self , value ):
    cmds.hyperShade( self.uiName , e=1 , snapShot=value )
  def setshaderNetworks( self , value ):
    cmds.hyperShade( self.uiName , e=1 , shaderNetworks=value )
  def setsetWorkArea( self , value ):
    cmds.hyperShade( self.uiName , e=1 , setWorkArea=value )
  def setuncollapse( self , value ):
    cmds.hyperShade( self.uiName , e=1 , uncollapse=value )
  def setuserDefinedLayout( self , value ):
    cmds.hyperShade( self.uiName , e=1 , userDefinedLayout=value )
  def setupStream( self , value ):
    cmds.hyperShade( self.uiName , e=1 , upStream=value )
  def setworkAreaAddCmd( self , value ):
    cmds.hyperShade( self.uiName , e=1 , workAreaAddCmd=value )
  def setworkAreaDeleteCmd( self , value ):
    cmds.hyperShade( self.uiName , e=1 , workAreaDeleteCmd=value )
  def setworkAreaSelectCmd( self , value ):
    cmds.hyperShade( self.uiName , e=1 , workAreaSelectCmd=value )

  ##### propertyCode #####
  assign = property( getassign , setassign )
  collapse = property( getcollapse , setcollapse )
  clearWorkArea = property( getclearWorkArea , setclearWorkArea )
  dependGraphArea = property( getdependGraphArea , setdependGraphArea )
  downStream = property( getdownStream , setdownStream )
  duplicate = property( getduplicate , setduplicate )
  fixRenderSize = property( getfixRenderSize , setfixRenderSize )
  incremental = property( getincremental , setincremental )
  listDownstreamNodes = property( getlistDownstreamNodes , setlistDownstreamNodes )
  listDownstreamShaderNodes = property( getlistDownstreamShaderNodes , setlistDownstreamShaderNodes )
  listUpstreamNodes = property( getlistUpstreamNodes , setlistUpstreamNodes )
  name = property( getname , setname )
  networks = property( getnetworks , setnetworks )
  noShapes = property( getnoShapes , setnoShapes )
  noSGShapes = property( getnoSGShapes , setnoSGShapes )
  noTransforms = property( getnoTransforms , setnoTransforms )
  objects = property( getobjects , setobjects )
  renderCreateAndDrop = property( getrenderCreateAndDrop , setrenderCreateAndDrop )
  createNode = property( getcreateNode , setcreateNode )
  resetGraph = property( getresetGraph , setresetGraph )
  resetSwatch = property( getresetSwatch , setresetSwatch )
  reset = property( getreset , setreset )
  setAllowsRegraphing = property( getsetAllowsRegraphing , setsetAllowsRegraphing )
  shaderNetworksSelectMaterialNodes = property( getshaderNetworksSelectMaterialNodes , setshaderNetworksSelectMaterialNodes )
  shaderNetwork = property( getshaderNetwork , setshaderNetwork )
  snapShot = property( getsnapShot , setsnapShot )
  shaderNetworks = property( getshaderNetworks , setshaderNetworks )
  setWorkArea = property( getsetWorkArea , setsetWorkArea )
  uncollapse = property( getuncollapse , setuncollapse )
  userDefinedLayout = property( getuserDefinedLayout , setuserDefinedLayout )
  upStream = property( getupStream , setupStream )
  workAreaAddCmd = property( getworkAreaAddCmd , setworkAreaAddCmd )
  workAreaDeleteCmd = property( getworkAreaDeleteCmd , setworkAreaDeleteCmd )
  workAreaSelectCmd = property( getworkAreaSelectCmd , setworkAreaSelectCmd )

  ##### customCode #####





class ModelEditor( Panel ):

  ##### initialize #####
  def __init__( self , activeComponentsXray=None , allObjects=None , activeOnly=None , addObjects=None , addSelected=None , activeView=None , backfaceCulling=None , bufferMode=None , bumpResolution=None , cameras=None , camera=None , colorMap=None , cameraName=None , cullingOverride=None , colorResolution=None , cameraSetup=None , controlVertices=None , default=None , displayAppearance=None , dynamicConstraints=None , deformers=None , dimensions=None , interactiveDisableShadows=None , displayLights=None , displayTextures=None , dynamics=None , editorChanged=None , filter=None , fogColor=None , fogDensity=None , fogEnd=None , fogging=None , fluids=None , forceMainConnection=None , fogMode=None , follicles=None , fogSource=None , fogStart=None , grid=None , handles=None , highlightConnection=None , hairSystems=None , hulls=None , headsUpDisplay=None , interactive=None , interactiveBackFaceCull=None , ikHandles=None , useRGBImagePlane=None , joints=None , jointXray=None , locators=None , lockMainConnection=None , lowQualityLighting=None , lights=None , lineWidth=None , manipulators=None , maxConstantTransparency=None , maximumNumHardwareLights=None , mainListConnection=None , nurbsCurves=None , nCloths=None , nParticles=None , nRigids=None , nurbsSurfaces=None , noUndo=None , occlusionCulling=None , planes=None , polymeshes=None , panel=None , pivots=None , rendererList=None , rendererListUI=None , rendererName=None , removeSelected=None , stereoDrawMode=None , subdivSurfaces=None , shadows=None , selectionHiliteDisplay=None , selectionConnection=None , shadingModel=None , smallObjectCulling=None , smallObjectThreshold=None , setSelected=None , sortTransparent=None , strokes=None , stateString=None , smoothWireframe=None , textureAnisotropic=None , transparencyAlgorithm=None , textureCompression=None , textureDisplay=None , textureEnvironmentMap=None , textureHilight=None , transpInShadows=None , textureMaxSize=None , textureMemoryUsed=None , textureSampling=None , twoSidedLighting=None , textures=None , useBaseRenderer=None , useColorIndex=None , updateColorMode=None , useDefaultMaterial=None , useInteractiveMode=None , unlockMainConnection=None , userNode=None , updateMainConnection=None , useReducedRenderer=None , viewObjects=None , viewSelected=None , wireframeBackingStore=None , wireframeOnShaded=None , xray=None , **args ):
    self.uiName = cmds.modelEditor()

    ##### substitution #####
    if activeComponentsXray != None:
      self.activeComponentsXray = activeComponentsXray
    if allObjects != None:
      self.allObjects = allObjects
    if activeOnly != None:
      self.activeOnly = activeOnly
    if addObjects != None:
      self.addObjects = addObjects
    if addSelected != None:
      self.addSelected = addSelected
    if activeView != None:
      self.activeView = activeView
    if backfaceCulling != None:
      self.backfaceCulling = backfaceCulling
    if bufferMode != None:
      self.bufferMode = bufferMode
    if bumpResolution != None:
      self.bumpResolution = bumpResolution
    if cameras != None:
      self.cameras = cameras
    if camera != None:
      self.camera = camera
    if colorMap != None:
      self.colorMap = colorMap
    if cameraName != None:
      self.cameraName = cameraName
    if cullingOverride != None:
      self.cullingOverride = cullingOverride
    if colorResolution != None:
      self.colorResolution = colorResolution
    if cameraSetup != None:
      self.cameraSetup = cameraSetup
    if controlVertices != None:
      self.controlVertices = controlVertices
    if default != None:
      self.default = default
    if displayAppearance != None:
      self.displayAppearance = displayAppearance
    if dynamicConstraints != None:
      self.dynamicConstraints = dynamicConstraints
    if deformers != None:
      self.deformers = deformers
    if dimensions != None:
      self.dimensions = dimensions
    if interactiveDisableShadows != None:
      self.interactiveDisableShadows = interactiveDisableShadows
    if displayLights != None:
      self.displayLights = displayLights
    if displayTextures != None:
      self.displayTextures = displayTextures
    if dynamics != None:
      self.dynamics = dynamics
    if editorChanged != None:
      self.editorChanged = editorChanged
    if filter != None:
      self.filter = filter
    if fogColor != None:
      self.fogColor = fogColor
    if fogDensity != None:
      self.fogDensity = fogDensity
    if fogEnd != None:
      self.fogEnd = fogEnd
    if fogging != None:
      self.fogging = fogging
    if fluids != None:
      self.fluids = fluids
    if forceMainConnection != None:
      self.forceMainConnection = forceMainConnection
    if fogMode != None:
      self.fogMode = fogMode
    if follicles != None:
      self.follicles = follicles
    if fogSource != None:
      self.fogSource = fogSource
    if fogStart != None:
      self.fogStart = fogStart
    if grid != None:
      self.grid = grid
    if handles != None:
      self.handles = handles
    if highlightConnection != None:
      self.highlightConnection = highlightConnection
    if hairSystems != None:
      self.hairSystems = hairSystems
    if hulls != None:
      self.hulls = hulls
    if headsUpDisplay != None:
      self.headsUpDisplay = headsUpDisplay
    if interactive != None:
      self.interactive = interactive
    if interactiveBackFaceCull != None:
      self.interactiveBackFaceCull = interactiveBackFaceCull
    if ikHandles != None:
      self.ikHandles = ikHandles
    if useRGBImagePlane != None:
      self.useRGBImagePlane = useRGBImagePlane
    if joints != None:
      self.joints = joints
    if jointXray != None:
      self.jointXray = jointXray
    if locators != None:
      self.locators = locators
    if lockMainConnection != None:
      self.lockMainConnection = lockMainConnection
    if lowQualityLighting != None:
      self.lowQualityLighting = lowQualityLighting
    if lights != None:
      self.lights = lights
    if lineWidth != None:
      self.lineWidth = lineWidth
    if manipulators != None:
      self.manipulators = manipulators
    if maxConstantTransparency != None:
      self.maxConstantTransparency = maxConstantTransparency
    if maximumNumHardwareLights != None:
      self.maximumNumHardwareLights = maximumNumHardwareLights
    if mainListConnection != None:
      self.mainListConnection = mainListConnection
    if nurbsCurves != None:
      self.nurbsCurves = nurbsCurves
    if nCloths != None:
      self.nCloths = nCloths
    if nParticles != None:
      self.nParticles = nParticles
    if nRigids != None:
      self.nRigids = nRigids
    if nurbsSurfaces != None:
      self.nurbsSurfaces = nurbsSurfaces
    if noUndo != None:
      self.noUndo = noUndo
    if occlusionCulling != None:
      self.occlusionCulling = occlusionCulling
    if planes != None:
      self.planes = planes
    if polymeshes != None:
      self.polymeshes = polymeshes
    if panel != None:
      self.panel = panel
    if pivots != None:
      self.pivots = pivots
    if rendererList != None:
      self.rendererList = rendererList
    if rendererListUI != None:
      self.rendererListUI = rendererListUI
    if rendererName != None:
      self.rendererName = rendererName
    if removeSelected != None:
      self.removeSelected = removeSelected
    if stereoDrawMode != None:
      self.stereoDrawMode = stereoDrawMode
    if subdivSurfaces != None:
      self.subdivSurfaces = subdivSurfaces
    if shadows != None:
      self.shadows = shadows
    if selectionHiliteDisplay != None:
      self.selectionHiliteDisplay = selectionHiliteDisplay
    if selectionConnection != None:
      self.selectionConnection = selectionConnection
    if shadingModel != None:
      self.shadingModel = shadingModel
    if smallObjectCulling != None:
      self.smallObjectCulling = smallObjectCulling
    if smallObjectThreshold != None:
      self.smallObjectThreshold = smallObjectThreshold
    if setSelected != None:
      self.setSelected = setSelected
    if sortTransparent != None:
      self.sortTransparent = sortTransparent
    if strokes != None:
      self.strokes = strokes
    if stateString != None:
      self.stateString = stateString
    if smoothWireframe != None:
      self.smoothWireframe = smoothWireframe
    if textureAnisotropic != None:
      self.textureAnisotropic = textureAnisotropic
    if transparencyAlgorithm != None:
      self.transparencyAlgorithm = transparencyAlgorithm
    if textureCompression != None:
      self.textureCompression = textureCompression
    if textureDisplay != None:
      self.textureDisplay = textureDisplay
    if textureEnvironmentMap != None:
      self.textureEnvironmentMap = textureEnvironmentMap
    if textureHilight != None:
      self.textureHilight = textureHilight
    if transpInShadows != None:
      self.transpInShadows = transpInShadows
    if textureMaxSize != None:
      self.textureMaxSize = textureMaxSize
    if textureMemoryUsed != None:
      self.textureMemoryUsed = textureMemoryUsed
    if textureSampling != None:
      self.textureSampling = textureSampling
    if twoSidedLighting != None:
      self.twoSidedLighting = twoSidedLighting
    if textures != None:
      self.textures = textures
    if useBaseRenderer != None:
      self.useBaseRenderer = useBaseRenderer
    if useColorIndex != None:
      self.useColorIndex = useColorIndex
    if updateColorMode != None:
      self.updateColorMode = updateColorMode
    if useDefaultMaterial != None:
      self.useDefaultMaterial = useDefaultMaterial
    if useInteractiveMode != None:
      self.useInteractiveMode = useInteractiveMode
    if unlockMainConnection != None:
      self.unlockMainConnection = unlockMainConnection
    if userNode != None:
      self.userNode = userNode
    if updateMainConnection != None:
      self.updateMainConnection = updateMainConnection
    if useReducedRenderer != None:
      self.useReducedRenderer = useReducedRenderer
    if viewObjects != None:
      self.viewObjects = viewObjects
    if viewSelected != None:
      self.viewSelected = viewSelected
    if wireframeBackingStore != None:
      self.wireframeBackingStore = wireframeBackingStore
    if wireframeOnShaded != None:
      self.wireframeOnShaded = wireframeOnShaded
    if xray != None:
      self.xray = xray

  ##### getFuncCode #####
  def getactiveComponentsXray( self ):
    return cmds.modelEditor( self.uiName , q=1 , activeComponentsXray=1 )
  def getallObjects( self ):
    return cmds.modelEditor( self.uiName , q=1 , allObjects=1 )
  def getactiveOnly( self ):
    return cmds.modelEditor( self.uiName , q=1 , activeOnly=1 )
  def getaddObjects( self ):
    return cmds.modelEditor( self.uiName , q=1 , addObjects=1 )
  def getaddSelected( self ):
    return cmds.modelEditor( self.uiName , q=1 , addSelected=1 )
  def getactiveView( self ):
    return cmds.modelEditor( self.uiName , q=1 , activeView=1 )
  def getbackfaceCulling( self ):
    return cmds.modelEditor( self.uiName , q=1 , backfaceCulling=1 )
  def getbufferMode( self ):
    return cmds.modelEditor( self.uiName , q=1 , bufferMode=1 )
  def getbumpResolution( self ):
    return cmds.modelEditor( self.uiName , q=1 , bumpResolution=1 )
  def getcameras( self ):
    return cmds.modelEditor( self.uiName , q=1 , cameras=1 )
  def getcamera( self ):
    return cmds.modelEditor( self.uiName , q=1 , camera=1 )
  def getcolorMap( self ):
    return cmds.modelEditor( self.uiName , q=1 , colorMap=1 )
  def getcameraName( self ):
    return cmds.modelEditor( self.uiName , q=1 , cameraName=1 )
  def getcullingOverride( self ):
    return cmds.modelEditor( self.uiName , q=1 , cullingOverride=1 )
  def getcolorResolution( self ):
    return cmds.modelEditor( self.uiName , q=1 , colorResolution=1 )
  def getcameraSetup( self ):
    return cmds.modelEditor( self.uiName , q=1 , cameraSetup=1 )
  def getcontrolVertices( self ):
    return cmds.modelEditor( self.uiName , q=1 , controlVertices=1 )
  def getdefault( self ):
    return cmds.modelEditor( self.uiName , q=1 , default=1 )
  def getdisplayAppearance( self ):
    return cmds.modelEditor( self.uiName , q=1 , displayAppearance=1 )
  def getdynamicConstraints( self ):
    return cmds.modelEditor( self.uiName , q=1 , dynamicConstraints=1 )
  def getdeformers( self ):
    return cmds.modelEditor( self.uiName , q=1 , deformers=1 )
  def getdimensions( self ):
    return cmds.modelEditor( self.uiName , q=1 , dimensions=1 )
  def getinteractiveDisableShadows( self ):
    return cmds.modelEditor( self.uiName , q=1 , interactiveDisableShadows=1 )
  def getdisplayLights( self ):
    return cmds.modelEditor( self.uiName , q=1 , displayLights=1 )
  def getdisplayTextures( self ):
    return cmds.modelEditor( self.uiName , q=1 , displayTextures=1 )
  def getdynamics( self ):
    return cmds.modelEditor( self.uiName , q=1 , dynamics=1 )
  def geteditorChanged( self ):
    return cmds.modelEditor( self.uiName , q=1 , editorChanged=1 )
  def getfilter( self ):
    return cmds.modelEditor( self.uiName , q=1 , filter=1 )
  def getfogColor( self ):
    return cmds.modelEditor( self.uiName , q=1 , fogColor=1 )
  def getfogDensity( self ):
    return cmds.modelEditor( self.uiName , q=1 , fogDensity=1 )
  def getfogEnd( self ):
    return cmds.modelEditor( self.uiName , q=1 , fogEnd=1 )
  def getfogging( self ):
    return cmds.modelEditor( self.uiName , q=1 , fogging=1 )
  def getfluids( self ):
    return cmds.modelEditor( self.uiName , q=1 , fluids=1 )
  def getforceMainConnection( self ):
    return cmds.modelEditor( self.uiName , q=1 , forceMainConnection=1 )
  def getfogMode( self ):
    return cmds.modelEditor( self.uiName , q=1 , fogMode=1 )
  def getfollicles( self ):
    return cmds.modelEditor( self.uiName , q=1 , follicles=1 )
  def getfogSource( self ):
    return cmds.modelEditor( self.uiName , q=1 , fogSource=1 )
  def getfogStart( self ):
    return cmds.modelEditor( self.uiName , q=1 , fogStart=1 )
  def getgrid( self ):
    return cmds.modelEditor( self.uiName , q=1 , grid=1 )
  def gethandles( self ):
    return cmds.modelEditor( self.uiName , q=1 , handles=1 )
  def gethighlightConnection( self ):
    return cmds.modelEditor( self.uiName , q=1 , highlightConnection=1 )
  def gethairSystems( self ):
    return cmds.modelEditor( self.uiName , q=1 , hairSystems=1 )
  def gethulls( self ):
    return cmds.modelEditor( self.uiName , q=1 , hulls=1 )
  def getheadsUpDisplay( self ):
    return cmds.modelEditor( self.uiName , q=1 , headsUpDisplay=1 )
  def getinteractive( self ):
    return cmds.modelEditor( self.uiName , q=1 , interactive=1 )
  def getinteractiveBackFaceCull( self ):
    return cmds.modelEditor( self.uiName , q=1 , interactiveBackFaceCull=1 )
  def getikHandles( self ):
    return cmds.modelEditor( self.uiName , q=1 , ikHandles=1 )
  def getuseRGBImagePlane( self ):
    return cmds.modelEditor( self.uiName , q=1 , useRGBImagePlane=1 )
  def getjoints( self ):
    return cmds.modelEditor( self.uiName , q=1 , joints=1 )
  def getjointXray( self ):
    return cmds.modelEditor( self.uiName , q=1 , jointXray=1 )
  def getlocators( self ):
    return cmds.modelEditor( self.uiName , q=1 , locators=1 )
  def getlockMainConnection( self ):
    return cmds.modelEditor( self.uiName , q=1 , lockMainConnection=1 )
  def getlowQualityLighting( self ):
    return cmds.modelEditor( self.uiName , q=1 , lowQualityLighting=1 )
  def getlights( self ):
    return cmds.modelEditor( self.uiName , q=1 , lights=1 )
  def getlineWidth( self ):
    return cmds.modelEditor( self.uiName , q=1 , lineWidth=1 )
  def getmanipulators( self ):
    return cmds.modelEditor( self.uiName , q=1 , manipulators=1 )
  def getmaxConstantTransparency( self ):
    return cmds.modelEditor( self.uiName , q=1 , maxConstantTransparency=1 )
  def getmaximumNumHardwareLights( self ):
    return cmds.modelEditor( self.uiName , q=1 , maximumNumHardwareLights=1 )
  def getmainListConnection( self ):
    return cmds.modelEditor( self.uiName , q=1 , mainListConnection=1 )
  def getnurbsCurves( self ):
    return cmds.modelEditor( self.uiName , q=1 , nurbsCurves=1 )
  def getnCloths( self ):
    return cmds.modelEditor( self.uiName , q=1 , nCloths=1 )
  def getnParticles( self ):
    return cmds.modelEditor( self.uiName , q=1 , nParticles=1 )
  def getnRigids( self ):
    return cmds.modelEditor( self.uiName , q=1 , nRigids=1 )
  def getnurbsSurfaces( self ):
    return cmds.modelEditor( self.uiName , q=1 , nurbsSurfaces=1 )
  def getnoUndo( self ):
    return cmds.modelEditor( self.uiName , q=1 , noUndo=1 )
  def getocclusionCulling( self ):
    return cmds.modelEditor( self.uiName , q=1 , occlusionCulling=1 )
  def getplanes( self ):
    return cmds.modelEditor( self.uiName , q=1 , planes=1 )
  def getpolymeshes( self ):
    return cmds.modelEditor( self.uiName , q=1 , polymeshes=1 )
  def getpanel( self ):
    return cmds.modelEditor( self.uiName , q=1 , panel=1 )
  def getpivots( self ):
    return cmds.modelEditor( self.uiName , q=1 , pivots=1 )
  def getrendererList( self ):
    return cmds.modelEditor( self.uiName , q=1 , rendererList=1 )
  def getrendererListUI( self ):
    return cmds.modelEditor( self.uiName , q=1 , rendererListUI=1 )
  def getrendererName( self ):
    return cmds.modelEditor( self.uiName , q=1 , rendererName=1 )
  def getremoveSelected( self ):
    return cmds.modelEditor( self.uiName , q=1 , removeSelected=1 )
  def getstereoDrawMode( self ):
    return cmds.modelEditor( self.uiName , q=1 , stereoDrawMode=1 )
  def getsubdivSurfaces( self ):
    return cmds.modelEditor( self.uiName , q=1 , subdivSurfaces=1 )
  def getshadows( self ):
    return cmds.modelEditor( self.uiName , q=1 , shadows=1 )
  def getselectionHiliteDisplay( self ):
    return cmds.modelEditor( self.uiName , q=1 , selectionHiliteDisplay=1 )
  def getselectionConnection( self ):
    return cmds.modelEditor( self.uiName , q=1 , selectionConnection=1 )
  def getshadingModel( self ):
    return cmds.modelEditor( self.uiName , q=1 , shadingModel=1 )
  def getsmallObjectCulling( self ):
    return cmds.modelEditor( self.uiName , q=1 , smallObjectCulling=1 )
  def getsmallObjectThreshold( self ):
    return cmds.modelEditor( self.uiName , q=1 , smallObjectThreshold=1 )
  def getsetSelected( self ):
    return cmds.modelEditor( self.uiName , q=1 , setSelected=1 )
  def getsortTransparent( self ):
    return cmds.modelEditor( self.uiName , q=1 , sortTransparent=1 )
  def getstrokes( self ):
    return cmds.modelEditor( self.uiName , q=1 , strokes=1 )
  def getstateString( self ):
    return cmds.modelEditor( self.uiName , q=1 , stateString=1 )
  def getsmoothWireframe( self ):
    return cmds.modelEditor( self.uiName , q=1 , smoothWireframe=1 )
  def gettextureAnisotropic( self ):
    return cmds.modelEditor( self.uiName , q=1 , textureAnisotropic=1 )
  def gettransparencyAlgorithm( self ):
    return cmds.modelEditor( self.uiName , q=1 , transparencyAlgorithm=1 )
  def gettextureCompression( self ):
    return cmds.modelEditor( self.uiName , q=1 , textureCompression=1 )
  def gettextureDisplay( self ):
    return cmds.modelEditor( self.uiName , q=1 , textureDisplay=1 )
  def gettextureEnvironmentMap( self ):
    return cmds.modelEditor( self.uiName , q=1 , textureEnvironmentMap=1 )
  def gettextureHilight( self ):
    return cmds.modelEditor( self.uiName , q=1 , textureHilight=1 )
  def gettranspInShadows( self ):
    return cmds.modelEditor( self.uiName , q=1 , transpInShadows=1 )
  def gettextureMaxSize( self ):
    return cmds.modelEditor( self.uiName , q=1 , textureMaxSize=1 )
  def gettextureMemoryUsed( self ):
    return cmds.modelEditor( self.uiName , q=1 , textureMemoryUsed=1 )
  def gettextureSampling( self ):
    return cmds.modelEditor( self.uiName , q=1 , textureSampling=1 )
  def gettwoSidedLighting( self ):
    return cmds.modelEditor( self.uiName , q=1 , twoSidedLighting=1 )
  def gettextures( self ):
    return cmds.modelEditor( self.uiName , q=1 , textures=1 )
  def getuseBaseRenderer( self ):
    return cmds.modelEditor( self.uiName , q=1 , useBaseRenderer=1 )
  def getuseColorIndex( self ):
    return cmds.modelEditor( self.uiName , q=1 , useColorIndex=1 )
  def getupdateColorMode( self ):
    return cmds.modelEditor( self.uiName , q=1 , updateColorMode=1 )
  def getuseDefaultMaterial( self ):
    return cmds.modelEditor( self.uiName , q=1 , useDefaultMaterial=1 )
  def getuseInteractiveMode( self ):
    return cmds.modelEditor( self.uiName , q=1 , useInteractiveMode=1 )
  def getunlockMainConnection( self ):
    return cmds.modelEditor( self.uiName , q=1 , unlockMainConnection=1 )
  def getuserNode( self ):
    return cmds.modelEditor( self.uiName , q=1 , userNode=1 )
  def getupdateMainConnection( self ):
    return cmds.modelEditor( self.uiName , q=1 , updateMainConnection=1 )
  def getuseReducedRenderer( self ):
    return cmds.modelEditor( self.uiName , q=1 , useReducedRenderer=1 )
  def getviewObjects( self ):
    return cmds.modelEditor( self.uiName , q=1 , viewObjects=1 )
  def getviewSelected( self ):
    return cmds.modelEditor( self.uiName , q=1 , viewSelected=1 )
  def getwireframeBackingStore( self ):
    return cmds.modelEditor( self.uiName , q=1 , wireframeBackingStore=1 )
  def getwireframeOnShaded( self ):
    return cmds.modelEditor( self.uiName , q=1 , wireframeOnShaded=1 )
  def getxray( self ):
    return cmds.modelEditor( self.uiName , q=1 , xray=1 )

  ##### setFuncCode #####
  def setactiveComponentsXray( self , value ):
    cmds.modelEditor( self.uiName , e=1 , activeComponentsXray=value )
  def setallObjects( self , value ):
    cmds.modelEditor( self.uiName , e=1 , allObjects=value )
  def setactiveOnly( self , value ):
    cmds.modelEditor( self.uiName , e=1 , activeOnly=value )
  def setaddObjects( self , value ):
    cmds.modelEditor( self.uiName , e=1 , addObjects=value )
  def setaddSelected( self , value ):
    cmds.modelEditor( self.uiName , e=1 , addSelected=value )
  def setactiveView( self , value ):
    cmds.modelEditor( self.uiName , e=1 , activeView=value )
  def setbackfaceCulling( self , value ):
    cmds.modelEditor( self.uiName , e=1 , backfaceCulling=value )
  def setbufferMode( self , value ):
    cmds.modelEditor( self.uiName , e=1 , bufferMode=value )
  def setbumpResolution( self , value ):
    cmds.modelEditor( self.uiName , e=1 , bumpResolution=value )
  def setcameras( self , value ):
    cmds.modelEditor( self.uiName , e=1 , cameras=value )
  def setcamera( self , value ):
    cmds.modelEditor( self.uiName , e=1 , camera=value )
  def setcolorMap( self , value ):
    cmds.modelEditor( self.uiName , e=1 , colorMap=value )
  def setcameraName( self , value ):
    cmds.modelEditor( self.uiName , e=1 , cameraName=value )
  def setcullingOverride( self , value ):
    cmds.modelEditor( self.uiName , e=1 , cullingOverride=value )
  def setcolorResolution( self , value ):
    cmds.modelEditor( self.uiName , e=1 , colorResolution=value )
  def setcameraSetup( self , value ):
    cmds.modelEditor( self.uiName , e=1 , cameraSetup=value )
  def setcontrolVertices( self , value ):
    cmds.modelEditor( self.uiName , e=1 , controlVertices=value )
  def setdefault( self , value ):
    cmds.modelEditor( self.uiName , e=1 , default=value )
  def setdisplayAppearance( self , value ):
    cmds.modelEditor( self.uiName , e=1 , displayAppearance=value )
  def setdynamicConstraints( self , value ):
    cmds.modelEditor( self.uiName , e=1 , dynamicConstraints=value )
  def setdeformers( self , value ):
    cmds.modelEditor( self.uiName , e=1 , deformers=value )
  def setdimensions( self , value ):
    cmds.modelEditor( self.uiName , e=1 , dimensions=value )
  def setinteractiveDisableShadows( self , value ):
    cmds.modelEditor( self.uiName , e=1 , interactiveDisableShadows=value )
  def setdisplayLights( self , value ):
    cmds.modelEditor( self.uiName , e=1 , displayLights=value )
  def setdisplayTextures( self , value ):
    cmds.modelEditor( self.uiName , e=1 , displayTextures=value )
  def setdynamics( self , value ):
    cmds.modelEditor( self.uiName , e=1 , dynamics=value )
  def seteditorChanged( self , value ):
    cmds.modelEditor( self.uiName , e=1 , editorChanged=value )
  def setfilter( self , value ):
    cmds.modelEditor( self.uiName , e=1 , filter=value )
  def setfogColor( self , value ):
    cmds.modelEditor( self.uiName , e=1 , fogColor=value )
  def setfogDensity( self , value ):
    cmds.modelEditor( self.uiName , e=1 , fogDensity=value )
  def setfogEnd( self , value ):
    cmds.modelEditor( self.uiName , e=1 , fogEnd=value )
  def setfogging( self , value ):
    cmds.modelEditor( self.uiName , e=1 , fogging=value )
  def setfluids( self , value ):
    cmds.modelEditor( self.uiName , e=1 , fluids=value )
  def setforceMainConnection( self , value ):
    cmds.modelEditor( self.uiName , e=1 , forceMainConnection=value )
  def setfogMode( self , value ):
    cmds.modelEditor( self.uiName , e=1 , fogMode=value )
  def setfollicles( self , value ):
    cmds.modelEditor( self.uiName , e=1 , follicles=value )
  def setfogSource( self , value ):
    cmds.modelEditor( self.uiName , e=1 , fogSource=value )
  def setfogStart( self , value ):
    cmds.modelEditor( self.uiName , e=1 , fogStart=value )
  def setgrid( self , value ):
    cmds.modelEditor( self.uiName , e=1 , grid=value )
  def sethandles( self , value ):
    cmds.modelEditor( self.uiName , e=1 , handles=value )
  def sethighlightConnection( self , value ):
    cmds.modelEditor( self.uiName , e=1 , highlightConnection=value )
  def sethairSystems( self , value ):
    cmds.modelEditor( self.uiName , e=1 , hairSystems=value )
  def sethulls( self , value ):
    cmds.modelEditor( self.uiName , e=1 , hulls=value )
  def setheadsUpDisplay( self , value ):
    cmds.modelEditor( self.uiName , e=1 , headsUpDisplay=value )
  def setinteractive( self , value ):
    cmds.modelEditor( self.uiName , e=1 , interactive=value )
  def setinteractiveBackFaceCull( self , value ):
    cmds.modelEditor( self.uiName , e=1 , interactiveBackFaceCull=value )
  def setikHandles( self , value ):
    cmds.modelEditor( self.uiName , e=1 , ikHandles=value )
  def setuseRGBImagePlane( self , value ):
    cmds.modelEditor( self.uiName , e=1 , useRGBImagePlane=value )
  def setjoints( self , value ):
    cmds.modelEditor( self.uiName , e=1 , joints=value )
  def setjointXray( self , value ):
    cmds.modelEditor( self.uiName , e=1 , jointXray=value )
  def setlocators( self , value ):
    cmds.modelEditor( self.uiName , e=1 , locators=value )
  def setlockMainConnection( self , value ):
    cmds.modelEditor( self.uiName , e=1 , lockMainConnection=value )
  def setlowQualityLighting( self , value ):
    cmds.modelEditor( self.uiName , e=1 , lowQualityLighting=value )
  def setlights( self , value ):
    cmds.modelEditor( self.uiName , e=1 , lights=value )
  def setlineWidth( self , value ):
    cmds.modelEditor( self.uiName , e=1 , lineWidth=value )
  def setmanipulators( self , value ):
    cmds.modelEditor( self.uiName , e=1 , manipulators=value )
  def setmaxConstantTransparency( self , value ):
    cmds.modelEditor( self.uiName , e=1 , maxConstantTransparency=value )
  def setmaximumNumHardwareLights( self , value ):
    cmds.modelEditor( self.uiName , e=1 , maximumNumHardwareLights=value )
  def setmainListConnection( self , value ):
    cmds.modelEditor( self.uiName , e=1 , mainListConnection=value )
  def setnurbsCurves( self , value ):
    cmds.modelEditor( self.uiName , e=1 , nurbsCurves=value )
  def setnCloths( self , value ):
    cmds.modelEditor( self.uiName , e=1 , nCloths=value )
  def setnParticles( self , value ):
    cmds.modelEditor( self.uiName , e=1 , nParticles=value )
  def setnRigids( self , value ):
    cmds.modelEditor( self.uiName , e=1 , nRigids=value )
  def setnurbsSurfaces( self , value ):
    cmds.modelEditor( self.uiName , e=1 , nurbsSurfaces=value )
  def setnoUndo( self , value ):
    cmds.modelEditor( self.uiName , e=1 , noUndo=value )
  def setocclusionCulling( self , value ):
    cmds.modelEditor( self.uiName , e=1 , occlusionCulling=value )
  def setplanes( self , value ):
    cmds.modelEditor( self.uiName , e=1 , planes=value )
  def setpolymeshes( self , value ):
    cmds.modelEditor( self.uiName , e=1 , polymeshes=value )
  def setpanel( self , value ):
    cmds.modelEditor( self.uiName , e=1 , panel=value )
  def setpivots( self , value ):
    cmds.modelEditor( self.uiName , e=1 , pivots=value )
  def setrendererList( self , value ):
    cmds.modelEditor( self.uiName , e=1 , rendererList=value )
  def setrendererListUI( self , value ):
    cmds.modelEditor( self.uiName , e=1 , rendererListUI=value )
  def setrendererName( self , value ):
    cmds.modelEditor( self.uiName , e=1 , rendererName=value )
  def setremoveSelected( self , value ):
    cmds.modelEditor( self.uiName , e=1 , removeSelected=value )
  def setstereoDrawMode( self , value ):
    cmds.modelEditor( self.uiName , e=1 , stereoDrawMode=value )
  def setsubdivSurfaces( self , value ):
    cmds.modelEditor( self.uiName , e=1 , subdivSurfaces=value )
  def setshadows( self , value ):
    cmds.modelEditor( self.uiName , e=1 , shadows=value )
  def setselectionHiliteDisplay( self , value ):
    cmds.modelEditor( self.uiName , e=1 , selectionHiliteDisplay=value )
  def setselectionConnection( self , value ):
    cmds.modelEditor( self.uiName , e=1 , selectionConnection=value )
  def setshadingModel( self , value ):
    cmds.modelEditor( self.uiName , e=1 , shadingModel=value )
  def setsmallObjectCulling( self , value ):
    cmds.modelEditor( self.uiName , e=1 , smallObjectCulling=value )
  def setsmallObjectThreshold( self , value ):
    cmds.modelEditor( self.uiName , e=1 , smallObjectThreshold=value )
  def setsetSelected( self , value ):
    cmds.modelEditor( self.uiName , e=1 , setSelected=value )
  def setsortTransparent( self , value ):
    cmds.modelEditor( self.uiName , e=1 , sortTransparent=value )
  def setstrokes( self , value ):
    cmds.modelEditor( self.uiName , e=1 , strokes=value )
  def setstateString( self , value ):
    cmds.modelEditor( self.uiName , e=1 , stateString=value )
  def setsmoothWireframe( self , value ):
    cmds.modelEditor( self.uiName , e=1 , smoothWireframe=value )
  def settextureAnisotropic( self , value ):
    cmds.modelEditor( self.uiName , e=1 , textureAnisotropic=value )
  def settransparencyAlgorithm( self , value ):
    cmds.modelEditor( self.uiName , e=1 , transparencyAlgorithm=value )
  def settextureCompression( self , value ):
    cmds.modelEditor( self.uiName , e=1 , textureCompression=value )
  def settextureDisplay( self , value ):
    cmds.modelEditor( self.uiName , e=1 , textureDisplay=value )
  def settextureEnvironmentMap( self , value ):
    cmds.modelEditor( self.uiName , e=1 , textureEnvironmentMap=value )
  def settextureHilight( self , value ):
    cmds.modelEditor( self.uiName , e=1 , textureHilight=value )
  def settranspInShadows( self , value ):
    cmds.modelEditor( self.uiName , e=1 , transpInShadows=value )
  def settextureMaxSize( self , value ):
    cmds.modelEditor( self.uiName , e=1 , textureMaxSize=value )
  def settextureMemoryUsed( self , value ):
    cmds.modelEditor( self.uiName , e=1 , textureMemoryUsed=value )
  def settextureSampling( self , value ):
    cmds.modelEditor( self.uiName , e=1 , textureSampling=value )
  def settwoSidedLighting( self , value ):
    cmds.modelEditor( self.uiName , e=1 , twoSidedLighting=value )
  def settextures( self , value ):
    cmds.modelEditor( self.uiName , e=1 , textures=value )
  def setuseBaseRenderer( self , value ):
    cmds.modelEditor( self.uiName , e=1 , useBaseRenderer=value )
  def setuseColorIndex( self , value ):
    cmds.modelEditor( self.uiName , e=1 , useColorIndex=value )
  def setupdateColorMode( self , value ):
    cmds.modelEditor( self.uiName , e=1 , updateColorMode=value )
  def setuseDefaultMaterial( self , value ):
    cmds.modelEditor( self.uiName , e=1 , useDefaultMaterial=value )
  def setuseInteractiveMode( self , value ):
    cmds.modelEditor( self.uiName , e=1 , useInteractiveMode=value )
  def setunlockMainConnection( self , value ):
    cmds.modelEditor( self.uiName , e=1 , unlockMainConnection=value )
  def setuserNode( self , value ):
    cmds.modelEditor( self.uiName , e=1 , userNode=value )
  def setupdateMainConnection( self , value ):
    cmds.modelEditor( self.uiName , e=1 , updateMainConnection=value )
  def setuseReducedRenderer( self , value ):
    cmds.modelEditor( self.uiName , e=1 , useReducedRenderer=value )
  def setviewObjects( self , value ):
    cmds.modelEditor( self.uiName , e=1 , viewObjects=value )
  def setviewSelected( self , value ):
    cmds.modelEditor( self.uiName , e=1 , viewSelected=value )
  def setwireframeBackingStore( self , value ):
    cmds.modelEditor( self.uiName , e=1 , wireframeBackingStore=value )
  def setwireframeOnShaded( self , value ):
    cmds.modelEditor( self.uiName , e=1 , wireframeOnShaded=value )
  def setxray( self , value ):
    cmds.modelEditor( self.uiName , e=1 , xray=value )

  ##### propertyCode #####
  activeComponentsXray = property( getactiveComponentsXray , setactiveComponentsXray )
  allObjects = property( getallObjects , setallObjects )
  activeOnly = property( getactiveOnly , setactiveOnly )
  addObjects = property( getaddObjects , setaddObjects )
  addSelected = property( getaddSelected , setaddSelected )
  activeView = property( getactiveView , setactiveView )
  backfaceCulling = property( getbackfaceCulling , setbackfaceCulling )
  bufferMode = property( getbufferMode , setbufferMode )
  bumpResolution = property( getbumpResolution , setbumpResolution )
  cameras = property( getcameras , setcameras )
  camera = property( getcamera , setcamera )
  colorMap = property( getcolorMap , setcolorMap )
  cameraName = property( getcameraName , setcameraName )
  cullingOverride = property( getcullingOverride , setcullingOverride )
  colorResolution = property( getcolorResolution , setcolorResolution )
  cameraSetup = property( getcameraSetup , setcameraSetup )
  controlVertices = property( getcontrolVertices , setcontrolVertices )
  default = property( getdefault , setdefault )
  displayAppearance = property( getdisplayAppearance , setdisplayAppearance )
  dynamicConstraints = property( getdynamicConstraints , setdynamicConstraints )
  deformers = property( getdeformers , setdeformers )
  dimensions = property( getdimensions , setdimensions )
  interactiveDisableShadows = property( getinteractiveDisableShadows , setinteractiveDisableShadows )
  displayLights = property( getdisplayLights , setdisplayLights )
  displayTextures = property( getdisplayTextures , setdisplayTextures )
  dynamics = property( getdynamics , setdynamics )
  editorChanged = property( geteditorChanged , seteditorChanged )
  filter = property( getfilter , setfilter )
  fogColor = property( getfogColor , setfogColor )
  fogDensity = property( getfogDensity , setfogDensity )
  fogEnd = property( getfogEnd , setfogEnd )
  fogging = property( getfogging , setfogging )
  fluids = property( getfluids , setfluids )
  forceMainConnection = property( getforceMainConnection , setforceMainConnection )
  fogMode = property( getfogMode , setfogMode )
  follicles = property( getfollicles , setfollicles )
  fogSource = property( getfogSource , setfogSource )
  fogStart = property( getfogStart , setfogStart )
  grid = property( getgrid , setgrid )
  handles = property( gethandles , sethandles )
  highlightConnection = property( gethighlightConnection , sethighlightConnection )
  hairSystems = property( gethairSystems , sethairSystems )
  hulls = property( gethulls , sethulls )
  headsUpDisplay = property( getheadsUpDisplay , setheadsUpDisplay )
  interactive = property( getinteractive , setinteractive )
  interactiveBackFaceCull = property( getinteractiveBackFaceCull , setinteractiveBackFaceCull )
  ikHandles = property( getikHandles , setikHandles )
  useRGBImagePlane = property( getuseRGBImagePlane , setuseRGBImagePlane )
  joints = property( getjoints , setjoints )
  jointXray = property( getjointXray , setjointXray )
  locators = property( getlocators , setlocators )
  lockMainConnection = property( getlockMainConnection , setlockMainConnection )
  lowQualityLighting = property( getlowQualityLighting , setlowQualityLighting )
  lights = property( getlights , setlights )
  lineWidth = property( getlineWidth , setlineWidth )
  manipulators = property( getmanipulators , setmanipulators )
  maxConstantTransparency = property( getmaxConstantTransparency , setmaxConstantTransparency )
  maximumNumHardwareLights = property( getmaximumNumHardwareLights , setmaximumNumHardwareLights )
  mainListConnection = property( getmainListConnection , setmainListConnection )
  nurbsCurves = property( getnurbsCurves , setnurbsCurves )
  nCloths = property( getnCloths , setnCloths )
  nParticles = property( getnParticles , setnParticles )
  nRigids = property( getnRigids , setnRigids )
  nurbsSurfaces = property( getnurbsSurfaces , setnurbsSurfaces )
  noUndo = property( getnoUndo , setnoUndo )
  occlusionCulling = property( getocclusionCulling , setocclusionCulling )
  planes = property( getplanes , setplanes )
  polymeshes = property( getpolymeshes , setpolymeshes )
  panel = property( getpanel , setpanel )
  pivots = property( getpivots , setpivots )
  rendererList = property( getrendererList , setrendererList )
  rendererListUI = property( getrendererListUI , setrendererListUI )
  rendererName = property( getrendererName , setrendererName )
  removeSelected = property( getremoveSelected , setremoveSelected )
  stereoDrawMode = property( getstereoDrawMode , setstereoDrawMode )
  subdivSurfaces = property( getsubdivSurfaces , setsubdivSurfaces )
  shadows = property( getshadows , setshadows )
  selectionHiliteDisplay = property( getselectionHiliteDisplay , setselectionHiliteDisplay )
  selectionConnection = property( getselectionConnection , setselectionConnection )
  shadingModel = property( getshadingModel , setshadingModel )
  smallObjectCulling = property( getsmallObjectCulling , setsmallObjectCulling )
  smallObjectThreshold = property( getsmallObjectThreshold , setsmallObjectThreshold )
  setSelected = property( getsetSelected , setsetSelected )
  sortTransparent = property( getsortTransparent , setsortTransparent )
  strokes = property( getstrokes , setstrokes )
  stateString = property( getstateString , setstateString )
  smoothWireframe = property( getsmoothWireframe , setsmoothWireframe )
  textureAnisotropic = property( gettextureAnisotropic , settextureAnisotropic )
  transparencyAlgorithm = property( gettransparencyAlgorithm , settransparencyAlgorithm )
  textureCompression = property( gettextureCompression , settextureCompression )
  textureDisplay = property( gettextureDisplay , settextureDisplay )
  textureEnvironmentMap = property( gettextureEnvironmentMap , settextureEnvironmentMap )
  textureHilight = property( gettextureHilight , settextureHilight )
  transpInShadows = property( gettranspInShadows , settranspInShadows )
  textureMaxSize = property( gettextureMaxSize , settextureMaxSize )
  textureMemoryUsed = property( gettextureMemoryUsed , settextureMemoryUsed )
  textureSampling = property( gettextureSampling , settextureSampling )
  twoSidedLighting = property( gettwoSidedLighting , settwoSidedLighting )
  textures = property( gettextures , settextures )
  useBaseRenderer = property( getuseBaseRenderer , setuseBaseRenderer )
  useColorIndex = property( getuseColorIndex , setuseColorIndex )
  updateColorMode = property( getupdateColorMode , setupdateColorMode )
  useDefaultMaterial = property( getuseDefaultMaterial , setuseDefaultMaterial )
  useInteractiveMode = property( getuseInteractiveMode , setuseInteractiveMode )
  unlockMainConnection = property( getunlockMainConnection , setunlockMainConnection )
  userNode = property( getuserNode , setuserNode )
  updateMainConnection = property( getupdateMainConnection , setupdateMainConnection )
  useReducedRenderer = property( getuseReducedRenderer , setuseReducedRenderer )
  viewObjects = property( getviewObjects , setviewObjects )
  viewSelected = property( getviewSelected , setviewSelected )
  wireframeBackingStore = property( getwireframeBackingStore , setwireframeBackingStore )
  wireframeOnShaded = property( getwireframeOnShaded , setwireframeOnShaded )
  xray = property( getxray , setxray )

  ##### customCode #####





class ModelPanel( Panel ):

  ##### initialize #####
  def __init__( self , barLayout=None , camera=None , modelEditor=None , **args ):
    self.uiName = cmds.modelPanel()

    ##### substitution #####
    if barLayout != None:
      self.barLayout = barLayout
    if camera != None:
      self.camera = camera
    if modelEditor != None:
      self.modelEditor = modelEditor

  ##### getFuncCode #####
  def getbarLayout( self ):
    return cmds.modelPanel( self.uiName , q=1 , barLayout=1 )
  def getcamera( self ):
    return cmds.modelPanel( self.uiName , q=1 , camera=1 )
  def getmodelEditor( self ):
    return cmds.modelPanel( self.uiName , q=1 , modelEditor=1 )

  ##### setFuncCode #####
  def setbarLayout( self , value ):
    cmds.modelPanel( self.uiName , e=1 , barLayout=value )
  def setcamera( self , value ):
    cmds.modelPanel( self.uiName , e=1 , camera=value )
  def setmodelEditor( self , value ):
    cmds.modelPanel( self.uiName , e=1 , modelEditor=value )

  ##### propertyCode #####
  barLayout = property( getbarLayout , setbarLayout )
  camera = property( getcamera , setcamera )
  modelEditor = property( getmodelEditor , setmodelEditor )

  ##### customCode #####





class NewPanelItems( Panel ):

  ##### initialize #####
  def __init__( self , **args ):
    self.uiName = cmds.newPanelItems()

    ##### substitution #####

  ##### getFuncCode #####

  ##### setFuncCode #####

  ##### propertyCode #####

  ##### customCode #####





class NodeOutliner( Panel ):

  ##### initialize #####
  def __init__( self , addObject=None , attrAlphaOrder=None , addCommand=None , annotation=None , backgroundColor=None , connectivity=None , currentSelection=None , dragCallback=None , dropCallback=None , enable=None , height=None , isObscured=None , lastClickedNode=None , lastMenuChoice=None , longNames=None , manage=None , menuCommand=None , menuMultiOption=None , multiSelect=None , noConnectivity=None , nodesDisplayed=None , niceNames=None , numberOfPopupMenus=None , pressHighlightsUnconnected=None , popupMenuArray=None , preventOverride=None , redraw=None , remove=None , removeAll=None , replace=None , redrawRow=None , selectCommand=None , showConnectedOnly=None , showHidden=None , showInputs=None , showNonConnectable=None , showNonKeyable=None , showOutputs=None , showReadOnly=None , visible=None , width=None , **args ):
    self.uiName = cmds.nodeOutliner()

    ##### substitution #####
    if addObject != None:
      self.addObject = addObject
    if attrAlphaOrder != None:
      self.attrAlphaOrder = attrAlphaOrder
    if addCommand != None:
      self.addCommand = addCommand
    if annotation != None:
      self.annotation = annotation
    if backgroundColor != None:
      self.backgroundColor = backgroundColor
    if connectivity != None:
      self.connectivity = connectivity
    if currentSelection != None:
      self.currentSelection = currentSelection
    if dragCallback != None:
      self.dragCallback = dragCallback
    if dropCallback != None:
      self.dropCallback = dropCallback
    if enable != None:
      self.enable = enable
    if height != None:
      self.height = height
    if isObscured != None:
      self.isObscured = isObscured
    if lastClickedNode != None:
      self.lastClickedNode = lastClickedNode
    if lastMenuChoice != None:
      self.lastMenuChoice = lastMenuChoice
    if longNames != None:
      self.longNames = longNames
    if manage != None:
      self.manage = manage
    if menuCommand != None:
      self.menuCommand = menuCommand
    if menuMultiOption != None:
      self.menuMultiOption = menuMultiOption
    if multiSelect != None:
      self.multiSelect = multiSelect
    if noConnectivity != None:
      self.noConnectivity = noConnectivity
    if nodesDisplayed != None:
      self.nodesDisplayed = nodesDisplayed
    if niceNames != None:
      self.niceNames = niceNames
    if numberOfPopupMenus != None:
      self.numberOfPopupMenus = numberOfPopupMenus
    if pressHighlightsUnconnected != None:
      self.pressHighlightsUnconnected = pressHighlightsUnconnected
    if popupMenuArray != None:
      self.popupMenuArray = popupMenuArray
    if preventOverride != None:
      self.preventOverride = preventOverride
    if redraw != None:
      self.redraw = redraw
    if remove != None:
      self.remove = remove
    if removeAll != None:
      self.removeAll = removeAll
    if replace != None:
      self.replace = replace
    if redrawRow != None:
      self.redrawRow = redrawRow
    if selectCommand != None:
      self.selectCommand = selectCommand
    if showConnectedOnly != None:
      self.showConnectedOnly = showConnectedOnly
    if showHidden != None:
      self.showHidden = showHidden
    if showInputs != None:
      self.showInputs = showInputs
    if showNonConnectable != None:
      self.showNonConnectable = showNonConnectable
    if showNonKeyable != None:
      self.showNonKeyable = showNonKeyable
    if showOutputs != None:
      self.showOutputs = showOutputs
    if showReadOnly != None:
      self.showReadOnly = showReadOnly
    if visible != None:
      self.visible = visible
    if width != None:
      self.width = width

  ##### getFuncCode #####
  def getaddObject( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , addObject=1 )
  def getattrAlphaOrder( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , attrAlphaOrder=1 )
  def getaddCommand( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , addCommand=1 )
  def getannotation( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , annotation=1 )
  def getbackgroundColor( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , backgroundColor=1 )
  def getconnectivity( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , connectivity=1 )
  def getcurrentSelection( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , currentSelection=1 )
  def getdragCallback( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , dragCallback=1 )
  def getdropCallback( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , dropCallback=1 )
  def getenable( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , enable=1 )
  def getheight( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , height=1 )
  def getisObscured( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , isObscured=1 )
  def getlastClickedNode( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , lastClickedNode=1 )
  def getlastMenuChoice( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , lastMenuChoice=1 )
  def getlongNames( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , longNames=1 )
  def getmanage( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , manage=1 )
  def getmenuCommand( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , menuCommand=1 )
  def getmenuMultiOption( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , menuMultiOption=1 )
  def getmultiSelect( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , multiSelect=1 )
  def getnoConnectivity( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , noConnectivity=1 )
  def getnodesDisplayed( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , nodesDisplayed=1 )
  def getniceNames( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , niceNames=1 )
  def getnumberOfPopupMenus( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , numberOfPopupMenus=1 )
  def getpressHighlightsUnconnected( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , pressHighlightsUnconnected=1 )
  def getpopupMenuArray( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , popupMenuArray=1 )
  def getpreventOverride( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , preventOverride=1 )
  def getredraw( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , redraw=1 )
  def getremove( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , remove=1 )
  def getremoveAll( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , removeAll=1 )
  def getreplace( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , replace=1 )
  def getredrawRow( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , redrawRow=1 )
  def getselectCommand( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , selectCommand=1 )
  def getshowConnectedOnly( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , showConnectedOnly=1 )
  def getshowHidden( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , showHidden=1 )
  def getshowInputs( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , showInputs=1 )
  def getshowNonConnectable( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , showNonConnectable=1 )
  def getshowNonKeyable( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , showNonKeyable=1 )
  def getshowOutputs( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , showOutputs=1 )
  def getshowReadOnly( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , showReadOnly=1 )
  def getvisible( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , visible=1 )
  def getwidth( self ):
    return cmds.nodeOutliner( self.uiName , q=1 , width=1 )

  ##### setFuncCode #####
  def setaddObject( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , addObject=value )
  def setattrAlphaOrder( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , attrAlphaOrder=value )
  def setaddCommand( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , addCommand=value )
  def setannotation( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , annotation=value )
  def setbackgroundColor( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , backgroundColor=value )
  def setconnectivity( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , connectivity=value )
  def setcurrentSelection( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , currentSelection=value )
  def setdragCallback( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , dragCallback=value )
  def setdropCallback( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , dropCallback=value )
  def setenable( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , enable=value )
  def setheight( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , height=value )
  def setisObscured( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , isObscured=value )
  def setlastClickedNode( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , lastClickedNode=value )
  def setlastMenuChoice( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , lastMenuChoice=value )
  def setlongNames( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , longNames=value )
  def setmanage( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , manage=value )
  def setmenuCommand( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , menuCommand=value )
  def setmenuMultiOption( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , menuMultiOption=value )
  def setmultiSelect( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , multiSelect=value )
  def setnoConnectivity( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , noConnectivity=value )
  def setnodesDisplayed( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , nodesDisplayed=value )
  def setniceNames( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , niceNames=value )
  def setnumberOfPopupMenus( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , numberOfPopupMenus=value )
  def setpressHighlightsUnconnected( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , pressHighlightsUnconnected=value )
  def setpopupMenuArray( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , popupMenuArray=value )
  def setpreventOverride( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , preventOverride=value )
  def setredraw( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , redraw=value )
  def setremove( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , remove=value )
  def setremoveAll( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , removeAll=value )
  def setreplace( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , replace=value )
  def setredrawRow( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , redrawRow=value )
  def setselectCommand( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , selectCommand=value )
  def setshowConnectedOnly( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , showConnectedOnly=value )
  def setshowHidden( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , showHidden=value )
  def setshowInputs( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , showInputs=value )
  def setshowNonConnectable( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , showNonConnectable=value )
  def setshowNonKeyable( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , showNonKeyable=value )
  def setshowOutputs( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , showOutputs=value )
  def setshowReadOnly( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , showReadOnly=value )
  def setvisible( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , visible=value )
  def setwidth( self , value ):
    cmds.nodeOutliner( self.uiName , e=1 , width=value )

  ##### propertyCode #####
  addObject = property( getaddObject , setaddObject )
  attrAlphaOrder = property( getattrAlphaOrder , setattrAlphaOrder )
  addCommand = property( getaddCommand , setaddCommand )
  annotation = property( getannotation , setannotation )
  backgroundColor = property( getbackgroundColor , setbackgroundColor )
  connectivity = property( getconnectivity , setconnectivity )
  currentSelection = property( getcurrentSelection , setcurrentSelection )
  dragCallback = property( getdragCallback , setdragCallback )
  dropCallback = property( getdropCallback , setdropCallback )
  enable = property( getenable , setenable )
  height = property( getheight , setheight )
  isObscured = property( getisObscured , setisObscured )
  lastClickedNode = property( getlastClickedNode , setlastClickedNode )
  lastMenuChoice = property( getlastMenuChoice , setlastMenuChoice )
  longNames = property( getlongNames , setlongNames )
  manage = property( getmanage , setmanage )
  menuCommand = property( getmenuCommand , setmenuCommand )
  menuMultiOption = property( getmenuMultiOption , setmenuMultiOption )
  multiSelect = property( getmultiSelect , setmultiSelect )
  noConnectivity = property( getnoConnectivity , setnoConnectivity )
  nodesDisplayed = property( getnodesDisplayed , setnodesDisplayed )
  niceNames = property( getniceNames , setniceNames )
  numberOfPopupMenus = property( getnumberOfPopupMenus , setnumberOfPopupMenus )
  pressHighlightsUnconnected = property( getpressHighlightsUnconnected , setpressHighlightsUnconnected )
  popupMenuArray = property( getpopupMenuArray , setpopupMenuArray )
  preventOverride = property( getpreventOverride , setpreventOverride )
  redraw = property( getredraw , setredraw )
  remove = property( getremove , setremove )
  removeAll = property( getremoveAll , setremoveAll )
  replace = property( getreplace , setreplace )
  redrawRow = property( getredrawRow , setredrawRow )
  selectCommand = property( getselectCommand , setselectCommand )
  showConnectedOnly = property( getshowConnectedOnly , setshowConnectedOnly )
  showHidden = property( getshowHidden , setshowHidden )
  showInputs = property( getshowInputs , setshowInputs )
  showNonConnectable = property( getshowNonConnectable , setshowNonConnectable )
  showNonKeyable = property( getshowNonKeyable , setshowNonKeyable )
  showOutputs = property( getshowOutputs , setshowOutputs )
  showReadOnly = property( getshowReadOnly , setshowReadOnly )
  visible = property( getvisible , setvisible )
  width = property( getwidth , setwidth )

  ##### customCode #####





class OutlinerEditor( Panel ):

  ##### initialize #####
  def __init__( self , showAssets=None , attrAlphaOrder=None , showAnimCurvesOnly=None , autoExpandLayers=None , attrFilter=None , animLayerFilterOptions=None , allowMultiSelection=None , autoSelectNewObjects=None , showAttributes=None , alwaysToggleSelect=None , showAttrValues=None , containersIgnoreFilters=None , showCompounds=None , showConnected=None , showDagOnly=None , dropIsParent=None , displayMode=None , doNotSelectNewObjects=None , directSelect=None , editAttrName=None , expandObjects=None , filter=None , forceMainConnection=None , highlightActive=None , ignoreDagHierarchy=None , highlightConnection=None , highlightSecondary=None , isChildSelected=None , showLeafs=None , lockMainConnection=None , longNames=None , mainListConnection=None , masterOutliner=None , niceNames=None , showNumericAttrsOnly=None , object=None , organizeByLayer=None , panel=None , parentObject=None , showAnimLayerWeight=None , showSelected=None , showContainerContents=None , showContainedOnly=None , selectCommand=None , setFilter=None , showShapes=None , setsIgnoreFilters=None , selectionConnection=None , showMuteInfo=None , showNamespace=None , sortOrder=None , showPublishedAsConnected=None , showSetMembers=None , stateString=None , showUnitlessCurves=None , transmitFilters=None , showTextureNodesOnly=None , unlockMainConnection=None , updateMainConnection=None , showUVAttrsOnly=None , expandConnections=None , autoExpand=None , **args ):
    self.uiName = cmds.outlinerEditor()

    ##### substitution #####
    if showAssets != None:
      self.showAssets = showAssets
    if attrAlphaOrder != None:
      self.attrAlphaOrder = attrAlphaOrder
    if showAnimCurvesOnly != None:
      self.showAnimCurvesOnly = showAnimCurvesOnly
    if autoExpandLayers != None:
      self.autoExpandLayers = autoExpandLayers
    if attrFilter != None:
      self.attrFilter = attrFilter
    if animLayerFilterOptions != None:
      self.animLayerFilterOptions = animLayerFilterOptions
    if allowMultiSelection != None:
      self.allowMultiSelection = allowMultiSelection
    if autoSelectNewObjects != None:
      self.autoSelectNewObjects = autoSelectNewObjects
    if showAttributes != None:
      self.showAttributes = showAttributes
    if alwaysToggleSelect != None:
      self.alwaysToggleSelect = alwaysToggleSelect
    if showAttrValues != None:
      self.showAttrValues = showAttrValues
    if containersIgnoreFilters != None:
      self.containersIgnoreFilters = containersIgnoreFilters
    if showCompounds != None:
      self.showCompounds = showCompounds
    if showConnected != None:
      self.showConnected = showConnected
    if showDagOnly != None:
      self.showDagOnly = showDagOnly
    if dropIsParent != None:
      self.dropIsParent = dropIsParent
    if displayMode != None:
      self.displayMode = displayMode
    if doNotSelectNewObjects != None:
      self.doNotSelectNewObjects = doNotSelectNewObjects
    if directSelect != None:
      self.directSelect = directSelect
    if editAttrName != None:
      self.editAttrName = editAttrName
    if expandObjects != None:
      self.expandObjects = expandObjects
    if filter != None:
      self.filter = filter
    if forceMainConnection != None:
      self.forceMainConnection = forceMainConnection
    if highlightActive != None:
      self.highlightActive = highlightActive
    if ignoreDagHierarchy != None:
      self.ignoreDagHierarchy = ignoreDagHierarchy
    if highlightConnection != None:
      self.highlightConnection = highlightConnection
    if highlightSecondary != None:
      self.highlightSecondary = highlightSecondary
    if isChildSelected != None:
      self.isChildSelected = isChildSelected
    if showLeafs != None:
      self.showLeafs = showLeafs
    if lockMainConnection != None:
      self.lockMainConnection = lockMainConnection
    if longNames != None:
      self.longNames = longNames
    if mainListConnection != None:
      self.mainListConnection = mainListConnection
    if masterOutliner != None:
      self.masterOutliner = masterOutliner
    if niceNames != None:
      self.niceNames = niceNames
    if showNumericAttrsOnly != None:
      self.showNumericAttrsOnly = showNumericAttrsOnly
    if object != None:
      self.object = object
    if organizeByLayer != None:
      self.organizeByLayer = organizeByLayer
    if panel != None:
      self.panel = panel
    if parentObject != None:
      self.parentObject = parentObject
    if showAnimLayerWeight != None:
      self.showAnimLayerWeight = showAnimLayerWeight
    if showSelected != None:
      self.showSelected = showSelected
    if showContainerContents != None:
      self.showContainerContents = showContainerContents
    if showContainedOnly != None:
      self.showContainedOnly = showContainedOnly
    if selectCommand != None:
      self.selectCommand = selectCommand
    if setFilter != None:
      self.setFilter = setFilter
    if showShapes != None:
      self.showShapes = showShapes
    if setsIgnoreFilters != None:
      self.setsIgnoreFilters = setsIgnoreFilters
    if selectionConnection != None:
      self.selectionConnection = selectionConnection
    if showMuteInfo != None:
      self.showMuteInfo = showMuteInfo
    if showNamespace != None:
      self.showNamespace = showNamespace
    if sortOrder != None:
      self.sortOrder = sortOrder
    if showPublishedAsConnected != None:
      self.showPublishedAsConnected = showPublishedAsConnected
    if showSetMembers != None:
      self.showSetMembers = showSetMembers
    if stateString != None:
      self.stateString = stateString
    if showUnitlessCurves != None:
      self.showUnitlessCurves = showUnitlessCurves
    if transmitFilters != None:
      self.transmitFilters = transmitFilters
    if showTextureNodesOnly != None:
      self.showTextureNodesOnly = showTextureNodesOnly
    if unlockMainConnection != None:
      self.unlockMainConnection = unlockMainConnection
    if updateMainConnection != None:
      self.updateMainConnection = updateMainConnection
    if showUVAttrsOnly != None:
      self.showUVAttrsOnly = showUVAttrsOnly
    if expandConnections != None:
      self.expandConnections = expandConnections
    if autoExpand != None:
      self.autoExpand = autoExpand

  ##### getFuncCode #####
  def getshowAssets( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , showAssets=1 )
  def getattrAlphaOrder( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , attrAlphaOrder=1 )
  def getshowAnimCurvesOnly( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , showAnimCurvesOnly=1 )
  def getautoExpandLayers( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , autoExpandLayers=1 )
  def getattrFilter( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , attrFilter=1 )
  def getanimLayerFilterOptions( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , animLayerFilterOptions=1 )
  def getallowMultiSelection( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , allowMultiSelection=1 )
  def getautoSelectNewObjects( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , autoSelectNewObjects=1 )
  def getshowAttributes( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , showAttributes=1 )
  def getalwaysToggleSelect( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , alwaysToggleSelect=1 )
  def getshowAttrValues( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , showAttrValues=1 )
  def getcontainersIgnoreFilters( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , containersIgnoreFilters=1 )
  def getshowCompounds( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , showCompounds=1 )
  def getshowConnected( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , showConnected=1 )
  def getshowDagOnly( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , showDagOnly=1 )
  def getdropIsParent( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , dropIsParent=1 )
  def getdisplayMode( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , displayMode=1 )
  def getdoNotSelectNewObjects( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , doNotSelectNewObjects=1 )
  def getdirectSelect( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , directSelect=1 )
  def geteditAttrName( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , editAttrName=1 )
  def getexpandObjects( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , expandObjects=1 )
  def getfilter( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , filter=1 )
  def getforceMainConnection( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , forceMainConnection=1 )
  def gethighlightActive( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , highlightActive=1 )
  def getignoreDagHierarchy( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , ignoreDagHierarchy=1 )
  def gethighlightConnection( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , highlightConnection=1 )
  def gethighlightSecondary( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , highlightSecondary=1 )
  def getisChildSelected( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , isChildSelected=1 )
  def getshowLeafs( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , showLeafs=1 )
  def getlockMainConnection( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , lockMainConnection=1 )
  def getlongNames( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , longNames=1 )
  def getmainListConnection( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , mainListConnection=1 )
  def getmasterOutliner( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , masterOutliner=1 )
  def getniceNames( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , niceNames=1 )
  def getshowNumericAttrsOnly( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , showNumericAttrsOnly=1 )
  def getobject( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , object=1 )
  def getorganizeByLayer( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , organizeByLayer=1 )
  def getpanel( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , panel=1 )
  def getparentObject( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , parentObject=1 )
  def getshowAnimLayerWeight( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , showAnimLayerWeight=1 )
  def getshowSelected( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , showSelected=1 )
  def getshowContainerContents( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , showContainerContents=1 )
  def getshowContainedOnly( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , showContainedOnly=1 )
  def getselectCommand( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , selectCommand=1 )
  def getsetFilter( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , setFilter=1 )
  def getshowShapes( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , showShapes=1 )
  def getsetsIgnoreFilters( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , setsIgnoreFilters=1 )
  def getselectionConnection( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , selectionConnection=1 )
  def getshowMuteInfo( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , showMuteInfo=1 )
  def getshowNamespace( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , showNamespace=1 )
  def getsortOrder( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , sortOrder=1 )
  def getshowPublishedAsConnected( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , showPublishedAsConnected=1 )
  def getshowSetMembers( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , showSetMembers=1 )
  def getstateString( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , stateString=1 )
  def getshowUnitlessCurves( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , showUnitlessCurves=1 )
  def gettransmitFilters( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , transmitFilters=1 )
  def getshowTextureNodesOnly( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , showTextureNodesOnly=1 )
  def getunlockMainConnection( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , unlockMainConnection=1 )
  def getupdateMainConnection( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , updateMainConnection=1 )
  def getshowUVAttrsOnly( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , showUVAttrsOnly=1 )
  def getexpandConnections( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , expandConnections=1 )
  def getautoExpand( self ):
    return cmds.outlinerEditor( self.uiName , q=1 , autoExpand=1 )

  ##### setFuncCode #####
  def setshowAssets( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , showAssets=value )
  def setattrAlphaOrder( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , attrAlphaOrder=value )
  def setshowAnimCurvesOnly( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , showAnimCurvesOnly=value )
  def setautoExpandLayers( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , autoExpandLayers=value )
  def setattrFilter( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , attrFilter=value )
  def setanimLayerFilterOptions( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , animLayerFilterOptions=value )
  def setallowMultiSelection( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , allowMultiSelection=value )
  def setautoSelectNewObjects( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , autoSelectNewObjects=value )
  def setshowAttributes( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , showAttributes=value )
  def setalwaysToggleSelect( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , alwaysToggleSelect=value )
  def setshowAttrValues( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , showAttrValues=value )
  def setcontainersIgnoreFilters( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , containersIgnoreFilters=value )
  def setshowCompounds( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , showCompounds=value )
  def setshowConnected( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , showConnected=value )
  def setshowDagOnly( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , showDagOnly=value )
  def setdropIsParent( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , dropIsParent=value )
  def setdisplayMode( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , displayMode=value )
  def setdoNotSelectNewObjects( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , doNotSelectNewObjects=value )
  def setdirectSelect( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , directSelect=value )
  def seteditAttrName( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , editAttrName=value )
  def setexpandObjects( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , expandObjects=value )
  def setfilter( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , filter=value )
  def setforceMainConnection( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , forceMainConnection=value )
  def sethighlightActive( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , highlightActive=value )
  def setignoreDagHierarchy( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , ignoreDagHierarchy=value )
  def sethighlightConnection( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , highlightConnection=value )
  def sethighlightSecondary( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , highlightSecondary=value )
  def setisChildSelected( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , isChildSelected=value )
  def setshowLeafs( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , showLeafs=value )
  def setlockMainConnection( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , lockMainConnection=value )
  def setlongNames( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , longNames=value )
  def setmainListConnection( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , mainListConnection=value )
  def setmasterOutliner( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , masterOutliner=value )
  def setniceNames( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , niceNames=value )
  def setshowNumericAttrsOnly( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , showNumericAttrsOnly=value )
  def setobject( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , object=value )
  def setorganizeByLayer( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , organizeByLayer=value )
  def setpanel( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , panel=value )
  def setparentObject( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , parentObject=value )
  def setshowAnimLayerWeight( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , showAnimLayerWeight=value )
  def setshowSelected( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , showSelected=value )
  def setshowContainerContents( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , showContainerContents=value )
  def setshowContainedOnly( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , showContainedOnly=value )
  def setselectCommand( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , selectCommand=value )
  def setsetFilter( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , setFilter=value )
  def setshowShapes( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , showShapes=value )
  def setsetsIgnoreFilters( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , setsIgnoreFilters=value )
  def setselectionConnection( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , selectionConnection=value )
  def setshowMuteInfo( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , showMuteInfo=value )
  def setshowNamespace( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , showNamespace=value )
  def setsortOrder( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , sortOrder=value )
  def setshowPublishedAsConnected( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , showPublishedAsConnected=value )
  def setshowSetMembers( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , showSetMembers=value )
  def setstateString( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , stateString=value )
  def setshowUnitlessCurves( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , showUnitlessCurves=value )
  def settransmitFilters( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , transmitFilters=value )
  def setshowTextureNodesOnly( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , showTextureNodesOnly=value )
  def setunlockMainConnection( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , unlockMainConnection=value )
  def setupdateMainConnection( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , updateMainConnection=value )
  def setshowUVAttrsOnly( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , showUVAttrsOnly=value )
  def setexpandConnections( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , expandConnections=value )
  def setautoExpand( self , value ):
    cmds.outlinerEditor( self.uiName , e=1 , autoExpand=value )

  ##### propertyCode #####
  showAssets = property( getshowAssets , setshowAssets )
  attrAlphaOrder = property( getattrAlphaOrder , setattrAlphaOrder )
  showAnimCurvesOnly = property( getshowAnimCurvesOnly , setshowAnimCurvesOnly )
  autoExpandLayers = property( getautoExpandLayers , setautoExpandLayers )
  attrFilter = property( getattrFilter , setattrFilter )
  animLayerFilterOptions = property( getanimLayerFilterOptions , setanimLayerFilterOptions )
  allowMultiSelection = property( getallowMultiSelection , setallowMultiSelection )
  autoSelectNewObjects = property( getautoSelectNewObjects , setautoSelectNewObjects )
  showAttributes = property( getshowAttributes , setshowAttributes )
  alwaysToggleSelect = property( getalwaysToggleSelect , setalwaysToggleSelect )
  showAttrValues = property( getshowAttrValues , setshowAttrValues )
  containersIgnoreFilters = property( getcontainersIgnoreFilters , setcontainersIgnoreFilters )
  showCompounds = property( getshowCompounds , setshowCompounds )
  showConnected = property( getshowConnected , setshowConnected )
  showDagOnly = property( getshowDagOnly , setshowDagOnly )
  dropIsParent = property( getdropIsParent , setdropIsParent )
  displayMode = property( getdisplayMode , setdisplayMode )
  doNotSelectNewObjects = property( getdoNotSelectNewObjects , setdoNotSelectNewObjects )
  directSelect = property( getdirectSelect , setdirectSelect )
  editAttrName = property( geteditAttrName , seteditAttrName )
  expandObjects = property( getexpandObjects , setexpandObjects )
  filter = property( getfilter , setfilter )
  forceMainConnection = property( getforceMainConnection , setforceMainConnection )
  highlightActive = property( gethighlightActive , sethighlightActive )
  ignoreDagHierarchy = property( getignoreDagHierarchy , setignoreDagHierarchy )
  highlightConnection = property( gethighlightConnection , sethighlightConnection )
  highlightSecondary = property( gethighlightSecondary , sethighlightSecondary )
  isChildSelected = property( getisChildSelected , setisChildSelected )
  showLeafs = property( getshowLeafs , setshowLeafs )
  lockMainConnection = property( getlockMainConnection , setlockMainConnection )
  longNames = property( getlongNames , setlongNames )
  mainListConnection = property( getmainListConnection , setmainListConnection )
  masterOutliner = property( getmasterOutliner , setmasterOutliner )
  niceNames = property( getniceNames , setniceNames )
  showNumericAttrsOnly = property( getshowNumericAttrsOnly , setshowNumericAttrsOnly )
  object = property( getobject , setobject )
  organizeByLayer = property( getorganizeByLayer , setorganizeByLayer )
  panel = property( getpanel , setpanel )
  parentObject = property( getparentObject , setparentObject )
  showAnimLayerWeight = property( getshowAnimLayerWeight , setshowAnimLayerWeight )
  showSelected = property( getshowSelected , setshowSelected )
  showContainerContents = property( getshowContainerContents , setshowContainerContents )
  showContainedOnly = property( getshowContainedOnly , setshowContainedOnly )
  selectCommand = property( getselectCommand , setselectCommand )
  setFilter = property( getsetFilter , setsetFilter )
  showShapes = property( getshowShapes , setshowShapes )
  setsIgnoreFilters = property( getsetsIgnoreFilters , setsetsIgnoreFilters )
  selectionConnection = property( getselectionConnection , setselectionConnection )
  showMuteInfo = property( getshowMuteInfo , setshowMuteInfo )
  showNamespace = property( getshowNamespace , setshowNamespace )
  sortOrder = property( getsortOrder , setsortOrder )
  showPublishedAsConnected = property( getshowPublishedAsConnected , setshowPublishedAsConnected )
  showSetMembers = property( getshowSetMembers , setshowSetMembers )
  stateString = property( getstateString , setstateString )
  showUnitlessCurves = property( getshowUnitlessCurves , setshowUnitlessCurves )
  transmitFilters = property( gettransmitFilters , settransmitFilters )
  showTextureNodesOnly = property( getshowTextureNodesOnly , setshowTextureNodesOnly )
  unlockMainConnection = property( getunlockMainConnection , setunlockMainConnection )
  updateMainConnection = property( getupdateMainConnection , setupdateMainConnection )
  showUVAttrsOnly = property( getshowUVAttrsOnly , setshowUVAttrsOnly )
  expandConnections = property( getexpandConnections , setexpandConnections )
  autoExpand = property( getautoExpand , setautoExpand )

  ##### customCode #####





class OutlinerPanel( Panel ):

  ##### initialize #####
  def __init__( self , outlinerEditor=None , **args ):
    self.uiName = cmds.outlinerPanel()

    ##### substitution #####
    if outlinerEditor != None:
      self.outlinerEditor = outlinerEditor

  ##### getFuncCode #####
  def getoutlinerEditor( self ):
    return cmds.outlinerPanel( self.uiName , q=1 , outlinerEditor=1 )

  ##### setFuncCode #####
  def setoutlinerEditor( self , value ):
    cmds.outlinerPanel( self.uiName , e=1 , outlinerEditor=value )

  ##### propertyCode #####
  outlinerEditor = property( getoutlinerEditor , setoutlinerEditor )

  ##### customCode #####





class PanelConfiguration( Panel ):

  ##### initialize #####
  def __init__( self , addPanel=None , configString=None , createStrings=None , defaultImage=None , editStrings=None , image=None , isFixedState=None , labelStrings=None , numberOfPanels=None , removeAllPanels=None , replaceCreateString=None , replaceEditString=None , replaceFixedState=None , replaceLabel=None , removeLastPanel=None , replaceTypeString=None , sceneConfig=None , typeStrings=None , **args ):
    self.uiName = cmds.panelConfiguration()

    ##### substitution #####
    if addPanel != None:
      self.addPanel = addPanel
    if configString != None:
      self.configString = configString
    if createStrings != None:
      self.createStrings = createStrings
    if defaultImage != None:
      self.defaultImage = defaultImage
    if editStrings != None:
      self.editStrings = editStrings
    if image != None:
      self.image = image
    if isFixedState != None:
      self.isFixedState = isFixedState
    if labelStrings != None:
      self.labelStrings = labelStrings
    if numberOfPanels != None:
      self.numberOfPanels = numberOfPanels
    if removeAllPanels != None:
      self.removeAllPanels = removeAllPanels
    if replaceCreateString != None:
      self.replaceCreateString = replaceCreateString
    if replaceEditString != None:
      self.replaceEditString = replaceEditString
    if replaceFixedState != None:
      self.replaceFixedState = replaceFixedState
    if replaceLabel != None:
      self.replaceLabel = replaceLabel
    if removeLastPanel != None:
      self.removeLastPanel = removeLastPanel
    if replaceTypeString != None:
      self.replaceTypeString = replaceTypeString
    if sceneConfig != None:
      self.sceneConfig = sceneConfig
    if typeStrings != None:
      self.typeStrings = typeStrings

  ##### getFuncCode #####
  def getaddPanel( self ):
    return cmds.panelConfiguration( self.uiName , q=1 , addPanel=1 )
  def getconfigString( self ):
    return cmds.panelConfiguration( self.uiName , q=1 , configString=1 )
  def getcreateStrings( self ):
    return cmds.panelConfiguration( self.uiName , q=1 , createStrings=1 )
  def getdefaultImage( self ):
    return cmds.panelConfiguration( self.uiName , q=1 , defaultImage=1 )
  def geteditStrings( self ):
    return cmds.panelConfiguration( self.uiName , q=1 , editStrings=1 )
  def getimage( self ):
    return cmds.panelConfiguration( self.uiName , q=1 , image=1 )
  def getisFixedState( self ):
    return cmds.panelConfiguration( self.uiName , q=1 , isFixedState=1 )
  def getlabelStrings( self ):
    return cmds.panelConfiguration( self.uiName , q=1 , labelStrings=1 )
  def getnumberOfPanels( self ):
    return cmds.panelConfiguration( self.uiName , q=1 , numberOfPanels=1 )
  def getremoveAllPanels( self ):
    return cmds.panelConfiguration( self.uiName , q=1 , removeAllPanels=1 )
  def getreplaceCreateString( self ):
    return cmds.panelConfiguration( self.uiName , q=1 , replaceCreateString=1 )
  def getreplaceEditString( self ):
    return cmds.panelConfiguration( self.uiName , q=1 , replaceEditString=1 )
  def getreplaceFixedState( self ):
    return cmds.panelConfiguration( self.uiName , q=1 , replaceFixedState=1 )
  def getreplaceLabel( self ):
    return cmds.panelConfiguration( self.uiName , q=1 , replaceLabel=1 )
  def getremoveLastPanel( self ):
    return cmds.panelConfiguration( self.uiName , q=1 , removeLastPanel=1 )
  def getreplaceTypeString( self ):
    return cmds.panelConfiguration( self.uiName , q=1 , replaceTypeString=1 )
  def getsceneConfig( self ):
    return cmds.panelConfiguration( self.uiName , q=1 , sceneConfig=1 )
  def gettypeStrings( self ):
    return cmds.panelConfiguration( self.uiName , q=1 , typeStrings=1 )

  ##### setFuncCode #####
  def setaddPanel( self , value ):
    cmds.panelConfiguration( self.uiName , e=1 , addPanel=value )
  def setconfigString( self , value ):
    cmds.panelConfiguration( self.uiName , e=1 , configString=value )
  def setcreateStrings( self , value ):
    cmds.panelConfiguration( self.uiName , e=1 , createStrings=value )
  def setdefaultImage( self , value ):
    cmds.panelConfiguration( self.uiName , e=1 , defaultImage=value )
  def seteditStrings( self , value ):
    cmds.panelConfiguration( self.uiName , e=1 , editStrings=value )
  def setimage( self , value ):
    cmds.panelConfiguration( self.uiName , e=1 , image=value )
  def setisFixedState( self , value ):
    cmds.panelConfiguration( self.uiName , e=1 , isFixedState=value )
  def setlabelStrings( self , value ):
    cmds.panelConfiguration( self.uiName , e=1 , labelStrings=value )
  def setnumberOfPanels( self , value ):
    cmds.panelConfiguration( self.uiName , e=1 , numberOfPanels=value )
  def setremoveAllPanels( self , value ):
    cmds.panelConfiguration( self.uiName , e=1 , removeAllPanels=value )
  def setreplaceCreateString( self , value ):
    cmds.panelConfiguration( self.uiName , e=1 , replaceCreateString=value )
  def setreplaceEditString( self , value ):
    cmds.panelConfiguration( self.uiName , e=1 , replaceEditString=value )
  def setreplaceFixedState( self , value ):
    cmds.panelConfiguration( self.uiName , e=1 , replaceFixedState=value )
  def setreplaceLabel( self , value ):
    cmds.panelConfiguration( self.uiName , e=1 , replaceLabel=value )
  def setremoveLastPanel( self , value ):
    cmds.panelConfiguration( self.uiName , e=1 , removeLastPanel=value )
  def setreplaceTypeString( self , value ):
    cmds.panelConfiguration( self.uiName , e=1 , replaceTypeString=value )
  def setsceneConfig( self , value ):
    cmds.panelConfiguration( self.uiName , e=1 , sceneConfig=value )
  def settypeStrings( self , value ):
    cmds.panelConfiguration( self.uiName , e=1 , typeStrings=value )

  ##### propertyCode #####
  addPanel = property( getaddPanel , setaddPanel )
  configString = property( getconfigString , setconfigString )
  createStrings = property( getcreateStrings , setcreateStrings )
  defaultImage = property( getdefaultImage , setdefaultImage )
  editStrings = property( geteditStrings , seteditStrings )
  image = property( getimage , setimage )
  isFixedState = property( getisFixedState , setisFixedState )
  labelStrings = property( getlabelStrings , setlabelStrings )
  numberOfPanels = property( getnumberOfPanels , setnumberOfPanels )
  removeAllPanels = property( getremoveAllPanels , setremoveAllPanels )
  replaceCreateString = property( getreplaceCreateString , setreplaceCreateString )
  replaceEditString = property( getreplaceEditString , setreplaceEditString )
  replaceFixedState = property( getreplaceFixedState , setreplaceFixedState )
  replaceLabel = property( getreplaceLabel , setreplaceLabel )
  removeLastPanel = property( getremoveLastPanel , setremoveLastPanel )
  replaceTypeString = property( getreplaceTypeString , setreplaceTypeString )
  sceneConfig = property( getsceneConfig , setsceneConfig )
  typeStrings = property( gettypeStrings , settypeStrings )

  ##### customCode #####





class PanelHistory( Panel ):

  ##### initialize #####
  def __init__( self , back=None , clear=None , forward=None , historyDepth=None , isEmpty=None , suspend=None , targetPane=None , wrap=None , **args ):
    self.uiName = cmds.panelHistory()

    ##### substitution #####
    if back != None:
      self.back = back
    if clear != None:
      self.clear = clear
    if forward != None:
      self.forward = forward
    if historyDepth != None:
      self.historyDepth = historyDepth
    if isEmpty != None:
      self.isEmpty = isEmpty
    if suspend != None:
      self.suspend = suspend
    if targetPane != None:
      self.targetPane = targetPane
    if wrap != None:
      self.wrap = wrap

  ##### getFuncCode #####
  def getback( self ):
    return cmds.panelHistory( self.uiName , q=1 , back=1 )
  def getclear( self ):
    return cmds.panelHistory( self.uiName , q=1 , clear=1 )
  def getforward( self ):
    return cmds.panelHistory( self.uiName , q=1 , forward=1 )
  def gethistoryDepth( self ):
    return cmds.panelHistory( self.uiName , q=1 , historyDepth=1 )
  def getisEmpty( self ):
    return cmds.panelHistory( self.uiName , q=1 , isEmpty=1 )
  def getsuspend( self ):
    return cmds.panelHistory( self.uiName , q=1 , suspend=1 )
  def gettargetPane( self ):
    return cmds.panelHistory( self.uiName , q=1 , targetPane=1 )
  def getwrap( self ):
    return cmds.panelHistory( self.uiName , q=1 , wrap=1 )

  ##### setFuncCode #####
  def setback( self , value ):
    cmds.panelHistory( self.uiName , e=1 , back=value )
  def setclear( self , value ):
    cmds.panelHistory( self.uiName , e=1 , clear=value )
  def setforward( self , value ):
    cmds.panelHistory( self.uiName , e=1 , forward=value )
  def sethistoryDepth( self , value ):
    cmds.panelHistory( self.uiName , e=1 , historyDepth=value )
  def setisEmpty( self , value ):
    cmds.panelHistory( self.uiName , e=1 , isEmpty=value )
  def setsuspend( self , value ):
    cmds.panelHistory( self.uiName , e=1 , suspend=value )
  def settargetPane( self , value ):
    cmds.panelHistory( self.uiName , e=1 , targetPane=value )
  def setwrap( self , value ):
    cmds.panelHistory( self.uiName , e=1 , wrap=value )

  ##### propertyCode #####
  back = property( getback , setback )
  clear = property( getclear , setclear )
  forward = property( getforward , setforward )
  historyDepth = property( gethistoryDepth , sethistoryDepth )
  isEmpty = property( getisEmpty , setisEmpty )
  suspend = property( getsuspend , setsuspend )
  targetPane = property( gettargetPane , settargetPane )
  wrap = property( getwrap , setwrap )

  ##### customCode #####





class ScriptedPanel( Panel ):

  ##### initialize #####
  def __init__( self , type=None , **args ):
    self.uiName = cmds.scriptedPanel()

    ##### substitution #####
    if type != None:
      self.type = type

  ##### getFuncCode #####
  def gettype( self ):
    return cmds.scriptedPanel( self.uiName , q=1 , type=1 )

  ##### setFuncCode #####
  def settype( self , value ):
    cmds.scriptedPanel( self.uiName , e=1 , type=value )

  ##### propertyCode #####
  type = property( gettype , settype )

  ##### customCode #####





class ScriptedPanelType( Panel ):

  ##### initialize #####
  def __init__( self , addCallback=None , createCallback=None , customView=None , deleteCallback=None , initCallback=None , obsolete=None , copyStateCallback=None , removeCallback=None , retainOnFileOpen=None , saveStateCallback=None , unique=None , **args ):
    self.uiName = cmds.scriptedPanelType()

    ##### substitution #####
    if addCallback != None:
      self.addCallback = addCallback
    if createCallback != None:
      self.createCallback = createCallback
    if customView != None:
      self.customView = customView
    if deleteCallback != None:
      self.deleteCallback = deleteCallback
    if initCallback != None:
      self.initCallback = initCallback
    if obsolete != None:
      self.obsolete = obsolete
    if copyStateCallback != None:
      self.copyStateCallback = copyStateCallback
    if removeCallback != None:
      self.removeCallback = removeCallback
    if retainOnFileOpen != None:
      self.retainOnFileOpen = retainOnFileOpen
    if saveStateCallback != None:
      self.saveStateCallback = saveStateCallback
    if unique != None:
      self.unique = unique

  ##### getFuncCode #####
  def getaddCallback( self ):
    return cmds.scriptedPanelType( self.uiName , q=1 , addCallback=1 )
  def getcreateCallback( self ):
    return cmds.scriptedPanelType( self.uiName , q=1 , createCallback=1 )
  def getcustomView( self ):
    return cmds.scriptedPanelType( self.uiName , q=1 , customView=1 )
  def getdeleteCallback( self ):
    return cmds.scriptedPanelType( self.uiName , q=1 , deleteCallback=1 )
  def getinitCallback( self ):
    return cmds.scriptedPanelType( self.uiName , q=1 , initCallback=1 )
  def getobsolete( self ):
    return cmds.scriptedPanelType( self.uiName , q=1 , obsolete=1 )
  def getcopyStateCallback( self ):
    return cmds.scriptedPanelType( self.uiName , q=1 , copyStateCallback=1 )
  def getremoveCallback( self ):
    return cmds.scriptedPanelType( self.uiName , q=1 , removeCallback=1 )
  def getretainOnFileOpen( self ):
    return cmds.scriptedPanelType( self.uiName , q=1 , retainOnFileOpen=1 )
  def getsaveStateCallback( self ):
    return cmds.scriptedPanelType( self.uiName , q=1 , saveStateCallback=1 )
  def getunique( self ):
    return cmds.scriptedPanelType( self.uiName , q=1 , unique=1 )

  ##### setFuncCode #####
  def setaddCallback( self , value ):
    cmds.scriptedPanelType( self.uiName , e=1 , addCallback=value )
  def setcreateCallback( self , value ):
    cmds.scriptedPanelType( self.uiName , e=1 , createCallback=value )
  def setcustomView( self , value ):
    cmds.scriptedPanelType( self.uiName , e=1 , customView=value )
  def setdeleteCallback( self , value ):
    cmds.scriptedPanelType( self.uiName , e=1 , deleteCallback=value )
  def setinitCallback( self , value ):
    cmds.scriptedPanelType( self.uiName , e=1 , initCallback=value )
  def setobsolete( self , value ):
    cmds.scriptedPanelType( self.uiName , e=1 , obsolete=value )
  def setcopyStateCallback( self , value ):
    cmds.scriptedPanelType( self.uiName , e=1 , copyStateCallback=value )
  def setremoveCallback( self , value ):
    cmds.scriptedPanelType( self.uiName , e=1 , removeCallback=value )
  def setretainOnFileOpen( self , value ):
    cmds.scriptedPanelType( self.uiName , e=1 , retainOnFileOpen=value )
  def setsaveStateCallback( self , value ):
    cmds.scriptedPanelType( self.uiName , e=1 , saveStateCallback=value )
  def setunique( self , value ):
    cmds.scriptedPanelType( self.uiName , e=1 , unique=value )

  ##### propertyCode #####
  addCallback = property( getaddCallback , setaddCallback )
  createCallback = property( getcreateCallback , setcreateCallback )
  customView = property( getcustomView , setcustomView )
  deleteCallback = property( getdeleteCallback , setdeleteCallback )
  initCallback = property( getinitCallback , setinitCallback )
  obsolete = property( getobsolete , setobsolete )
  copyStateCallback = property( getcopyStateCallback , setcopyStateCallback )
  removeCallback = property( getremoveCallback , setremoveCallback )
  retainOnFileOpen = property( getretainOnFileOpen , setretainOnFileOpen )
  saveStateCallback = property( getsaveStateCallback , setsaveStateCallback )
  unique = property( getunique , setunique )

  ##### customCode #####





class SetEditor( Panel ):

  ##### initialize #####
  def __init__( self , addToList=None , allSets=None , addToSet=None , autoUpdate=None , autoExpand=None , autoScroll=None , applyWeightCommand=None , createBookmark=None , collapseFrames=None , componentListLength=None , expandFrames=None , editPartitions=None , editSets=None , filter=None , forceMainConnection=None , groupComponents=None , hilitedFrames=None , highlightConnection=None , itemToAdd=None , listBookmarks=None , lockMainConnection=None , mode=None , mainListConnection=None , normal=None , panel=None , quickEdit=None , removeFromSet=None , reload=None , showBoneLatticeSets=None , showBlendShapeSets=None , showClusterSets=None , showDeformerSets=None , scrollFrames=None , showJointClusterSets=None , showJointLatticeSets=None , showLatticeSets=None , selectionConnection=None , showLatticeDualBaseSets=None , showNormalSets=None , showRenderSets=None , showSculptSets=None , stateString=None , showWireSets=None , useBookmark=None , unlockMainConnection=None , updateMainConnection=None , **args ):
    self.uiName = cmds.setEditor()

    ##### substitution #####
    if addToList != None:
      self.addToList = addToList
    if allSets != None:
      self.allSets = allSets
    if addToSet != None:
      self.addToSet = addToSet
    if autoUpdate != None:
      self.autoUpdate = autoUpdate
    if autoExpand != None:
      self.autoExpand = autoExpand
    if autoScroll != None:
      self.autoScroll = autoScroll
    if applyWeightCommand != None:
      self.applyWeightCommand = applyWeightCommand
    if createBookmark != None:
      self.createBookmark = createBookmark
    if collapseFrames != None:
      self.collapseFrames = collapseFrames
    if componentListLength != None:
      self.componentListLength = componentListLength
    if expandFrames != None:
      self.expandFrames = expandFrames
    if editPartitions != None:
      self.editPartitions = editPartitions
    if editSets != None:
      self.editSets = editSets
    if filter != None:
      self.filter = filter
    if forceMainConnection != None:
      self.forceMainConnection = forceMainConnection
    if groupComponents != None:
      self.groupComponents = groupComponents
    if hilitedFrames != None:
      self.hilitedFrames = hilitedFrames
    if highlightConnection != None:
      self.highlightConnection = highlightConnection
    if itemToAdd != None:
      self.itemToAdd = itemToAdd
    if listBookmarks != None:
      self.listBookmarks = listBookmarks
    if lockMainConnection != None:
      self.lockMainConnection = lockMainConnection
    if mode != None:
      self.mode = mode
    if mainListConnection != None:
      self.mainListConnection = mainListConnection
    if normal != None:
      self.normal = normal
    if panel != None:
      self.panel = panel
    if quickEdit != None:
      self.quickEdit = quickEdit
    if removeFromSet != None:
      self.removeFromSet = removeFromSet
    if reload != None:
      self.reload = reload
    if showBoneLatticeSets != None:
      self.showBoneLatticeSets = showBoneLatticeSets
    if showBlendShapeSets != None:
      self.showBlendShapeSets = showBlendShapeSets
    if showClusterSets != None:
      self.showClusterSets = showClusterSets
    if showDeformerSets != None:
      self.showDeformerSets = showDeformerSets
    if scrollFrames != None:
      self.scrollFrames = scrollFrames
    if showJointClusterSets != None:
      self.showJointClusterSets = showJointClusterSets
    if showJointLatticeSets != None:
      self.showJointLatticeSets = showJointLatticeSets
    if showLatticeSets != None:
      self.showLatticeSets = showLatticeSets
    if selectionConnection != None:
      self.selectionConnection = selectionConnection
    if showLatticeDualBaseSets != None:
      self.showLatticeDualBaseSets = showLatticeDualBaseSets
    if showNormalSets != None:
      self.showNormalSets = showNormalSets
    if showRenderSets != None:
      self.showRenderSets = showRenderSets
    if showSculptSets != None:
      self.showSculptSets = showSculptSets
    if stateString != None:
      self.stateString = stateString
    if showWireSets != None:
      self.showWireSets = showWireSets
    if useBookmark != None:
      self.useBookmark = useBookmark
    if unlockMainConnection != None:
      self.unlockMainConnection = unlockMainConnection
    if updateMainConnection != None:
      self.updateMainConnection = updateMainConnection

  ##### getFuncCode #####
  def getaddToList( self ):
    return cmds.setEditor( self.uiName , q=1 , addToList=1 )
  def getallSets( self ):
    return cmds.setEditor( self.uiName , q=1 , allSets=1 )
  def getaddToSet( self ):
    return cmds.setEditor( self.uiName , q=1 , addToSet=1 )
  def getautoUpdate( self ):
    return cmds.setEditor( self.uiName , q=1 , autoUpdate=1 )
  def getautoExpand( self ):
    return cmds.setEditor( self.uiName , q=1 , autoExpand=1 )
  def getautoScroll( self ):
    return cmds.setEditor( self.uiName , q=1 , autoScroll=1 )
  def getapplyWeightCommand( self ):
    return cmds.setEditor( self.uiName , q=1 , applyWeightCommand=1 )
  def getcreateBookmark( self ):
    return cmds.setEditor( self.uiName , q=1 , createBookmark=1 )
  def getcollapseFrames( self ):
    return cmds.setEditor( self.uiName , q=1 , collapseFrames=1 )
  def getcomponentListLength( self ):
    return cmds.setEditor( self.uiName , q=1 , componentListLength=1 )
  def getexpandFrames( self ):
    return cmds.setEditor( self.uiName , q=1 , expandFrames=1 )
  def geteditPartitions( self ):
    return cmds.setEditor( self.uiName , q=1 , editPartitions=1 )
  def geteditSets( self ):
    return cmds.setEditor( self.uiName , q=1 , editSets=1 )
  def getfilter( self ):
    return cmds.setEditor( self.uiName , q=1 , filter=1 )
  def getforceMainConnection( self ):
    return cmds.setEditor( self.uiName , q=1 , forceMainConnection=1 )
  def getgroupComponents( self ):
    return cmds.setEditor( self.uiName , q=1 , groupComponents=1 )
  def gethilitedFrames( self ):
    return cmds.setEditor( self.uiName , q=1 , hilitedFrames=1 )
  def gethighlightConnection( self ):
    return cmds.setEditor( self.uiName , q=1 , highlightConnection=1 )
  def getitemToAdd( self ):
    return cmds.setEditor( self.uiName , q=1 , itemToAdd=1 )
  def getlistBookmarks( self ):
    return cmds.setEditor( self.uiName , q=1 , listBookmarks=1 )
  def getlockMainConnection( self ):
    return cmds.setEditor( self.uiName , q=1 , lockMainConnection=1 )
  def getmode( self ):
    return cmds.setEditor( self.uiName , q=1 , mode=1 )
  def getmainListConnection( self ):
    return cmds.setEditor( self.uiName , q=1 , mainListConnection=1 )
  def getnormal( self ):
    return cmds.setEditor( self.uiName , q=1 , normal=1 )
  def getpanel( self ):
    return cmds.setEditor( self.uiName , q=1 , panel=1 )
  def getquickEdit( self ):
    return cmds.setEditor( self.uiName , q=1 , quickEdit=1 )
  def getremoveFromSet( self ):
    return cmds.setEditor( self.uiName , q=1 , removeFromSet=1 )
  def getreload( self ):
    return cmds.setEditor( self.uiName , q=1 , reload=1 )
  def getshowBoneLatticeSets( self ):
    return cmds.setEditor( self.uiName , q=1 , showBoneLatticeSets=1 )
  def getshowBlendShapeSets( self ):
    return cmds.setEditor( self.uiName , q=1 , showBlendShapeSets=1 )
  def getshowClusterSets( self ):
    return cmds.setEditor( self.uiName , q=1 , showClusterSets=1 )
  def getshowDeformerSets( self ):
    return cmds.setEditor( self.uiName , q=1 , showDeformerSets=1 )
  def getscrollFrames( self ):
    return cmds.setEditor( self.uiName , q=1 , scrollFrames=1 )
  def getshowJointClusterSets( self ):
    return cmds.setEditor( self.uiName , q=1 , showJointClusterSets=1 )
  def getshowJointLatticeSets( self ):
    return cmds.setEditor( self.uiName , q=1 , showJointLatticeSets=1 )
  def getshowLatticeSets( self ):
    return cmds.setEditor( self.uiName , q=1 , showLatticeSets=1 )
  def getselectionConnection( self ):
    return cmds.setEditor( self.uiName , q=1 , selectionConnection=1 )
  def getshowLatticeDualBaseSets( self ):
    return cmds.setEditor( self.uiName , q=1 , showLatticeDualBaseSets=1 )
  def getshowNormalSets( self ):
    return cmds.setEditor( self.uiName , q=1 , showNormalSets=1 )
  def getshowRenderSets( self ):
    return cmds.setEditor( self.uiName , q=1 , showRenderSets=1 )
  def getshowSculptSets( self ):
    return cmds.setEditor( self.uiName , q=1 , showSculptSets=1 )
  def getstateString( self ):
    return cmds.setEditor( self.uiName , q=1 , stateString=1 )
  def getshowWireSets( self ):
    return cmds.setEditor( self.uiName , q=1 , showWireSets=1 )
  def getuseBookmark( self ):
    return cmds.setEditor( self.uiName , q=1 , useBookmark=1 )
  def getunlockMainConnection( self ):
    return cmds.setEditor( self.uiName , q=1 , unlockMainConnection=1 )
  def getupdateMainConnection( self ):
    return cmds.setEditor( self.uiName , q=1 , updateMainConnection=1 )

  ##### setFuncCode #####
  def setaddToList( self , value ):
    cmds.setEditor( self.uiName , e=1 , addToList=value )
  def setallSets( self , value ):
    cmds.setEditor( self.uiName , e=1 , allSets=value )
  def setaddToSet( self , value ):
    cmds.setEditor( self.uiName , e=1 , addToSet=value )
  def setautoUpdate( self , value ):
    cmds.setEditor( self.uiName , e=1 , autoUpdate=value )
  def setautoExpand( self , value ):
    cmds.setEditor( self.uiName , e=1 , autoExpand=value )
  def setautoScroll( self , value ):
    cmds.setEditor( self.uiName , e=1 , autoScroll=value )
  def setapplyWeightCommand( self , value ):
    cmds.setEditor( self.uiName , e=1 , applyWeightCommand=value )
  def setcreateBookmark( self , value ):
    cmds.setEditor( self.uiName , e=1 , createBookmark=value )
  def setcollapseFrames( self , value ):
    cmds.setEditor( self.uiName , e=1 , collapseFrames=value )
  def setcomponentListLength( self , value ):
    cmds.setEditor( self.uiName , e=1 , componentListLength=value )
  def setexpandFrames( self , value ):
    cmds.setEditor( self.uiName , e=1 , expandFrames=value )
  def seteditPartitions( self , value ):
    cmds.setEditor( self.uiName , e=1 , editPartitions=value )
  def seteditSets( self , value ):
    cmds.setEditor( self.uiName , e=1 , editSets=value )
  def setfilter( self , value ):
    cmds.setEditor( self.uiName , e=1 , filter=value )
  def setforceMainConnection( self , value ):
    cmds.setEditor( self.uiName , e=1 , forceMainConnection=value )
  def setgroupComponents( self , value ):
    cmds.setEditor( self.uiName , e=1 , groupComponents=value )
  def sethilitedFrames( self , value ):
    cmds.setEditor( self.uiName , e=1 , hilitedFrames=value )
  def sethighlightConnection( self , value ):
    cmds.setEditor( self.uiName , e=1 , highlightConnection=value )
  def setitemToAdd( self , value ):
    cmds.setEditor( self.uiName , e=1 , itemToAdd=value )
  def setlistBookmarks( self , value ):
    cmds.setEditor( self.uiName , e=1 , listBookmarks=value )
  def setlockMainConnection( self , value ):
    cmds.setEditor( self.uiName , e=1 , lockMainConnection=value )
  def setmode( self , value ):
    cmds.setEditor( self.uiName , e=1 , mode=value )
  def setmainListConnection( self , value ):
    cmds.setEditor( self.uiName , e=1 , mainListConnection=value )
  def setnormal( self , value ):
    cmds.setEditor( self.uiName , e=1 , normal=value )
  def setpanel( self , value ):
    cmds.setEditor( self.uiName , e=1 , panel=value )
  def setquickEdit( self , value ):
    cmds.setEditor( self.uiName , e=1 , quickEdit=value )
  def setremoveFromSet( self , value ):
    cmds.setEditor( self.uiName , e=1 , removeFromSet=value )
  def setreload( self , value ):
    cmds.setEditor( self.uiName , e=1 , reload=value )
  def setshowBoneLatticeSets( self , value ):
    cmds.setEditor( self.uiName , e=1 , showBoneLatticeSets=value )
  def setshowBlendShapeSets( self , value ):
    cmds.setEditor( self.uiName , e=1 , showBlendShapeSets=value )
  def setshowClusterSets( self , value ):
    cmds.setEditor( self.uiName , e=1 , showClusterSets=value )
  def setshowDeformerSets( self , value ):
    cmds.setEditor( self.uiName , e=1 , showDeformerSets=value )
  def setscrollFrames( self , value ):
    cmds.setEditor( self.uiName , e=1 , scrollFrames=value )
  def setshowJointClusterSets( self , value ):
    cmds.setEditor( self.uiName , e=1 , showJointClusterSets=value )
  def setshowJointLatticeSets( self , value ):
    cmds.setEditor( self.uiName , e=1 , showJointLatticeSets=value )
  def setshowLatticeSets( self , value ):
    cmds.setEditor( self.uiName , e=1 , showLatticeSets=value )
  def setselectionConnection( self , value ):
    cmds.setEditor( self.uiName , e=1 , selectionConnection=value )
  def setshowLatticeDualBaseSets( self , value ):
    cmds.setEditor( self.uiName , e=1 , showLatticeDualBaseSets=value )
  def setshowNormalSets( self , value ):
    cmds.setEditor( self.uiName , e=1 , showNormalSets=value )
  def setshowRenderSets( self , value ):
    cmds.setEditor( self.uiName , e=1 , showRenderSets=value )
  def setshowSculptSets( self , value ):
    cmds.setEditor( self.uiName , e=1 , showSculptSets=value )
  def setstateString( self , value ):
    cmds.setEditor( self.uiName , e=1 , stateString=value )
  def setshowWireSets( self , value ):
    cmds.setEditor( self.uiName , e=1 , showWireSets=value )
  def setuseBookmark( self , value ):
    cmds.setEditor( self.uiName , e=1 , useBookmark=value )
  def setunlockMainConnection( self , value ):
    cmds.setEditor( self.uiName , e=1 , unlockMainConnection=value )
  def setupdateMainConnection( self , value ):
    cmds.setEditor( self.uiName , e=1 , updateMainConnection=value )

  ##### propertyCode #####
  addToList = property( getaddToList , setaddToList )
  allSets = property( getallSets , setallSets )
  addToSet = property( getaddToSet , setaddToSet )
  autoUpdate = property( getautoUpdate , setautoUpdate )
  autoExpand = property( getautoExpand , setautoExpand )
  autoScroll = property( getautoScroll , setautoScroll )
  applyWeightCommand = property( getapplyWeightCommand , setapplyWeightCommand )
  createBookmark = property( getcreateBookmark , setcreateBookmark )
  collapseFrames = property( getcollapseFrames , setcollapseFrames )
  componentListLength = property( getcomponentListLength , setcomponentListLength )
  expandFrames = property( getexpandFrames , setexpandFrames )
  editPartitions = property( geteditPartitions , seteditPartitions )
  editSets = property( geteditSets , seteditSets )
  filter = property( getfilter , setfilter )
  forceMainConnection = property( getforceMainConnection , setforceMainConnection )
  groupComponents = property( getgroupComponents , setgroupComponents )
  hilitedFrames = property( gethilitedFrames , sethilitedFrames )
  highlightConnection = property( gethighlightConnection , sethighlightConnection )
  itemToAdd = property( getitemToAdd , setitemToAdd )
  listBookmarks = property( getlistBookmarks , setlistBookmarks )
  lockMainConnection = property( getlockMainConnection , setlockMainConnection )
  mode = property( getmode , setmode )
  mainListConnection = property( getmainListConnection , setmainListConnection )
  normal = property( getnormal , setnormal )
  panel = property( getpanel , setpanel )
  quickEdit = property( getquickEdit , setquickEdit )
  removeFromSet = property( getremoveFromSet , setremoveFromSet )
  reload = property( getreload , setreload )
  showBoneLatticeSets = property( getshowBoneLatticeSets , setshowBoneLatticeSets )
  showBlendShapeSets = property( getshowBlendShapeSets , setshowBlendShapeSets )
  showClusterSets = property( getshowClusterSets , setshowClusterSets )
  showDeformerSets = property( getshowDeformerSets , setshowDeformerSets )
  scrollFrames = property( getscrollFrames , setscrollFrames )
  showJointClusterSets = property( getshowJointClusterSets , setshowJointClusterSets )
  showJointLatticeSets = property( getshowJointLatticeSets , setshowJointLatticeSets )
  showLatticeSets = property( getshowLatticeSets , setshowLatticeSets )
  selectionConnection = property( getselectionConnection , setselectionConnection )
  showLatticeDualBaseSets = property( getshowLatticeDualBaseSets , setshowLatticeDualBaseSets )
  showNormalSets = property( getshowNormalSets , setshowNormalSets )
  showRenderSets = property( getshowRenderSets , setshowRenderSets )
  showSculptSets = property( getshowSculptSets , setshowSculptSets )
  stateString = property( getstateString , setstateString )
  showWireSets = property( getshowWireSets , setshowWireSets )
  useBookmark = property( getuseBookmark , setuseBookmark )
  unlockMainConnection = property( getunlockMainConnection , setunlockMainConnection )
  updateMainConnection = property( getupdateMainConnection , setupdateMainConnection )

  ##### customCode #####





class SetFocus( Panel ):

  ##### initialize #####
  def __init__( self , **args ):
    self.uiName = cmds.setFocus()

    ##### substitution #####

  ##### getFuncCode #####

  ##### setFuncCode #####

  ##### propertyCode #####

  ##### customCode #####





class SpreadSheetEditor( Panel ):

  ##### initialize #####
  def __init__( self , allAttr=None , execute=None , filter=None , fixedAttrList=None , forceMainConnection=None , highlightConnection=None , keyableOnly=None , lockMainConnection=None , longNames=None , mainListConnection=None , niceNames=None , panel=None , precision=None , selectedAttr=None , selectionConnection=None , showShapes=None , stateString=None , unlockMainConnection=None , updateMainConnection=None , **args ):
    self.uiName = cmds.spreadSheetEditor()

    ##### substitution #####
    if allAttr != None:
      self.allAttr = allAttr
    if execute != None:
      self.execute = execute
    if filter != None:
      self.filter = filter
    if fixedAttrList != None:
      self.fixedAttrList = fixedAttrList
    if forceMainConnection != None:
      self.forceMainConnection = forceMainConnection
    if highlightConnection != None:
      self.highlightConnection = highlightConnection
    if keyableOnly != None:
      self.keyableOnly = keyableOnly
    if lockMainConnection != None:
      self.lockMainConnection = lockMainConnection
    if longNames != None:
      self.longNames = longNames
    if mainListConnection != None:
      self.mainListConnection = mainListConnection
    if niceNames != None:
      self.niceNames = niceNames
    if panel != None:
      self.panel = panel
    if precision != None:
      self.precision = precision
    if selectedAttr != None:
      self.selectedAttr = selectedAttr
    if selectionConnection != None:
      self.selectionConnection = selectionConnection
    if showShapes != None:
      self.showShapes = showShapes
    if stateString != None:
      self.stateString = stateString
    if unlockMainConnection != None:
      self.unlockMainConnection = unlockMainConnection
    if updateMainConnection != None:
      self.updateMainConnection = updateMainConnection

  ##### getFuncCode #####
  def getallAttr( self ):
    return cmds.spreadSheetEditor( self.uiName , q=1 , allAttr=1 )
  def getexecute( self ):
    return cmds.spreadSheetEditor( self.uiName , q=1 , execute=1 )
  def getfilter( self ):
    return cmds.spreadSheetEditor( self.uiName , q=1 , filter=1 )
  def getfixedAttrList( self ):
    return cmds.spreadSheetEditor( self.uiName , q=1 , fixedAttrList=1 )
  def getforceMainConnection( self ):
    return cmds.spreadSheetEditor( self.uiName , q=1 , forceMainConnection=1 )
  def gethighlightConnection( self ):
    return cmds.spreadSheetEditor( self.uiName , q=1 , highlightConnection=1 )
  def getkeyableOnly( self ):
    return cmds.spreadSheetEditor( self.uiName , q=1 , keyableOnly=1 )
  def getlockMainConnection( self ):
    return cmds.spreadSheetEditor( self.uiName , q=1 , lockMainConnection=1 )
  def getlongNames( self ):
    return cmds.spreadSheetEditor( self.uiName , q=1 , longNames=1 )
  def getmainListConnection( self ):
    return cmds.spreadSheetEditor( self.uiName , q=1 , mainListConnection=1 )
  def getniceNames( self ):
    return cmds.spreadSheetEditor( self.uiName , q=1 , niceNames=1 )
  def getpanel( self ):
    return cmds.spreadSheetEditor( self.uiName , q=1 , panel=1 )
  def getprecision( self ):
    return cmds.spreadSheetEditor( self.uiName , q=1 , precision=1 )
  def getselectedAttr( self ):
    return cmds.spreadSheetEditor( self.uiName , q=1 , selectedAttr=1 )
  def getselectionConnection( self ):
    return cmds.spreadSheetEditor( self.uiName , q=1 , selectionConnection=1 )
  def getshowShapes( self ):
    return cmds.spreadSheetEditor( self.uiName , q=1 , showShapes=1 )
  def getstateString( self ):
    return cmds.spreadSheetEditor( self.uiName , q=1 , stateString=1 )
  def getunlockMainConnection( self ):
    return cmds.spreadSheetEditor( self.uiName , q=1 , unlockMainConnection=1 )
  def getupdateMainConnection( self ):
    return cmds.spreadSheetEditor( self.uiName , q=1 , updateMainConnection=1 )

  ##### setFuncCode #####
  def setallAttr( self , value ):
    cmds.spreadSheetEditor( self.uiName , e=1 , allAttr=value )
  def setexecute( self , value ):
    cmds.spreadSheetEditor( self.uiName , e=1 , execute=value )
  def setfilter( self , value ):
    cmds.spreadSheetEditor( self.uiName , e=1 , filter=value )
  def setfixedAttrList( self , value ):
    cmds.spreadSheetEditor( self.uiName , e=1 , fixedAttrList=value )
  def setforceMainConnection( self , value ):
    cmds.spreadSheetEditor( self.uiName , e=1 , forceMainConnection=value )
  def sethighlightConnection( self , value ):
    cmds.spreadSheetEditor( self.uiName , e=1 , highlightConnection=value )
  def setkeyableOnly( self , value ):
    cmds.spreadSheetEditor( self.uiName , e=1 , keyableOnly=value )
  def setlockMainConnection( self , value ):
    cmds.spreadSheetEditor( self.uiName , e=1 , lockMainConnection=value )
  def setlongNames( self , value ):
    cmds.spreadSheetEditor( self.uiName , e=1 , longNames=value )
  def setmainListConnection( self , value ):
    cmds.spreadSheetEditor( self.uiName , e=1 , mainListConnection=value )
  def setniceNames( self , value ):
    cmds.spreadSheetEditor( self.uiName , e=1 , niceNames=value )
  def setpanel( self , value ):
    cmds.spreadSheetEditor( self.uiName , e=1 , panel=value )
  def setprecision( self , value ):
    cmds.spreadSheetEditor( self.uiName , e=1 , precision=value )
  def setselectedAttr( self , value ):
    cmds.spreadSheetEditor( self.uiName , e=1 , selectedAttr=value )
  def setselectionConnection( self , value ):
    cmds.spreadSheetEditor( self.uiName , e=1 , selectionConnection=value )
  def setshowShapes( self , value ):
    cmds.spreadSheetEditor( self.uiName , e=1 , showShapes=value )
  def setstateString( self , value ):
    cmds.spreadSheetEditor( self.uiName , e=1 , stateString=value )
  def setunlockMainConnection( self , value ):
    cmds.spreadSheetEditor( self.uiName , e=1 , unlockMainConnection=value )
  def setupdateMainConnection( self , value ):
    cmds.spreadSheetEditor( self.uiName , e=1 , updateMainConnection=value )

  ##### propertyCode #####
  allAttr = property( getallAttr , setallAttr )
  execute = property( getexecute , setexecute )
  filter = property( getfilter , setfilter )
  fixedAttrList = property( getfixedAttrList , setfixedAttrList )
  forceMainConnection = property( getforceMainConnection , setforceMainConnection )
  highlightConnection = property( gethighlightConnection , sethighlightConnection )
  keyableOnly = property( getkeyableOnly , setkeyableOnly )
  lockMainConnection = property( getlockMainConnection , setlockMainConnection )
  longNames = property( getlongNames , setlongNames )
  mainListConnection = property( getmainListConnection , setmainListConnection )
  niceNames = property( getniceNames , setniceNames )
  panel = property( getpanel , setpanel )
  precision = property( getprecision , setprecision )
  selectedAttr = property( getselectedAttr , setselectedAttr )
  selectionConnection = property( getselectionConnection , setselectionConnection )
  showShapes = property( getshowShapes , setshowShapes )
  stateString = property( getstateString , setstateString )
  unlockMainConnection = property( getunlockMainConnection , setunlockMainConnection )
  updateMainConnection = property( getupdateMainConnection , setupdateMainConnection )

  ##### customCode #####





class ViewManip( Panel ):

  ##### initialize #####
  def __init__( self , bottomLeft=None , bottomRight=None , compassAngle=None , drawCompass=None , dragSnap=None , frontParameters=None , fitToView=None , goDefault=None , goHome=None , homeParameters=None , levelCamera=None , minOpacity=None , namespace=None , postCommand=None , preCommand=None , preserveSceneUp=None , restoreCenter=None , resetFront=None , resetHome=None , size=None , setFront=None , setHome=None , selectionLockParameters=None , topLeft=None , topRight=None , toggleSelectionLock=None , visible=None , zoomToFitScene=None , **args ):
    self.uiName = cmds.viewManip()

    ##### substitution #####
    if bottomLeft != None:
      self.bottomLeft = bottomLeft
    if bottomRight != None:
      self.bottomRight = bottomRight
    if compassAngle != None:
      self.compassAngle = compassAngle
    if drawCompass != None:
      self.drawCompass = drawCompass
    if dragSnap != None:
      self.dragSnap = dragSnap
    if frontParameters != None:
      self.frontParameters = frontParameters
    if fitToView != None:
      self.fitToView = fitToView
    if goDefault != None:
      self.goDefault = goDefault
    if goHome != None:
      self.goHome = goHome
    if homeParameters != None:
      self.homeParameters = homeParameters
    if levelCamera != None:
      self.levelCamera = levelCamera
    if minOpacity != None:
      self.minOpacity = minOpacity
    if namespace != None:
      self.namespace = namespace
    if postCommand != None:
      self.postCommand = postCommand
    if preCommand != None:
      self.preCommand = preCommand
    if preserveSceneUp != None:
      self.preserveSceneUp = preserveSceneUp
    if restoreCenter != None:
      self.restoreCenter = restoreCenter
    if resetFront != None:
      self.resetFront = resetFront
    if resetHome != None:
      self.resetHome = resetHome
    if size != None:
      self.size = size
    if setFront != None:
      self.setFront = setFront
    if setHome != None:
      self.setHome = setHome
    if selectionLockParameters != None:
      self.selectionLockParameters = selectionLockParameters
    if topLeft != None:
      self.topLeft = topLeft
    if topRight != None:
      self.topRight = topRight
    if toggleSelectionLock != None:
      self.toggleSelectionLock = toggleSelectionLock
    if visible != None:
      self.visible = visible
    if zoomToFitScene != None:
      self.zoomToFitScene = zoomToFitScene

  ##### getFuncCode #####
  def getbottomLeft( self ):
    return cmds.viewManip( self.uiName , q=1 , bottomLeft=1 )
  def getbottomRight( self ):
    return cmds.viewManip( self.uiName , q=1 , bottomRight=1 )
  def getcompassAngle( self ):
    return cmds.viewManip( self.uiName , q=1 , compassAngle=1 )
  def getdrawCompass( self ):
    return cmds.viewManip( self.uiName , q=1 , drawCompass=1 )
  def getdragSnap( self ):
    return cmds.viewManip( self.uiName , q=1 , dragSnap=1 )
  def getfrontParameters( self ):
    return cmds.viewManip( self.uiName , q=1 , frontParameters=1 )
  def getfitToView( self ):
    return cmds.viewManip( self.uiName , q=1 , fitToView=1 )
  def getgoDefault( self ):
    return cmds.viewManip( self.uiName , q=1 , goDefault=1 )
  def getgoHome( self ):
    return cmds.viewManip( self.uiName , q=1 , goHome=1 )
  def gethomeParameters( self ):
    return cmds.viewManip( self.uiName , q=1 , homeParameters=1 )
  def getlevelCamera( self ):
    return cmds.viewManip( self.uiName , q=1 , levelCamera=1 )
  def getminOpacity( self ):
    return cmds.viewManip( self.uiName , q=1 , minOpacity=1 )
  def getnamespace( self ):
    return cmds.viewManip( self.uiName , q=1 , namespace=1 )
  def getpostCommand( self ):
    return cmds.viewManip( self.uiName , q=1 , postCommand=1 )
  def getpreCommand( self ):
    return cmds.viewManip( self.uiName , q=1 , preCommand=1 )
  def getpreserveSceneUp( self ):
    return cmds.viewManip( self.uiName , q=1 , preserveSceneUp=1 )
  def getrestoreCenter( self ):
    return cmds.viewManip( self.uiName , q=1 , restoreCenter=1 )
  def getresetFront( self ):
    return cmds.viewManip( self.uiName , q=1 , resetFront=1 )
  def getresetHome( self ):
    return cmds.viewManip( self.uiName , q=1 , resetHome=1 )
  def getsize( self ):
    return cmds.viewManip( self.uiName , q=1 , size=1 )
  def getsetFront( self ):
    return cmds.viewManip( self.uiName , q=1 , setFront=1 )
  def getsetHome( self ):
    return cmds.viewManip( self.uiName , q=1 , setHome=1 )
  def getselectionLockParameters( self ):
    return cmds.viewManip( self.uiName , q=1 , selectionLockParameters=1 )
  def gettopLeft( self ):
    return cmds.viewManip( self.uiName , q=1 , topLeft=1 )
  def gettopRight( self ):
    return cmds.viewManip( self.uiName , q=1 , topRight=1 )
  def gettoggleSelectionLock( self ):
    return cmds.viewManip( self.uiName , q=1 , toggleSelectionLock=1 )
  def getvisible( self ):
    return cmds.viewManip( self.uiName , q=1 , visible=1 )
  def getzoomToFitScene( self ):
    return cmds.viewManip( self.uiName , q=1 , zoomToFitScene=1 )

  ##### setFuncCode #####
  def setbottomLeft( self , value ):
    cmds.viewManip( self.uiName , e=1 , bottomLeft=value )
  def setbottomRight( self , value ):
    cmds.viewManip( self.uiName , e=1 , bottomRight=value )
  def setcompassAngle( self , value ):
    cmds.viewManip( self.uiName , e=1 , compassAngle=value )
  def setdrawCompass( self , value ):
    cmds.viewManip( self.uiName , e=1 , drawCompass=value )
  def setdragSnap( self , value ):
    cmds.viewManip( self.uiName , e=1 , dragSnap=value )
  def setfrontParameters( self , value ):
    cmds.viewManip( self.uiName , e=1 , frontParameters=value )
  def setfitToView( self , value ):
    cmds.viewManip( self.uiName , e=1 , fitToView=value )
  def setgoDefault( self , value ):
    cmds.viewManip( self.uiName , e=1 , goDefault=value )
  def setgoHome( self , value ):
    cmds.viewManip( self.uiName , e=1 , goHome=value )
  def sethomeParameters( self , value ):
    cmds.viewManip( self.uiName , e=1 , homeParameters=value )
  def setlevelCamera( self , value ):
    cmds.viewManip( self.uiName , e=1 , levelCamera=value )
  def setminOpacity( self , value ):
    cmds.viewManip( self.uiName , e=1 , minOpacity=value )
  def setnamespace( self , value ):
    cmds.viewManip( self.uiName , e=1 , namespace=value )
  def setpostCommand( self , value ):
    cmds.viewManip( self.uiName , e=1 , postCommand=value )
  def setpreCommand( self , value ):
    cmds.viewManip( self.uiName , e=1 , preCommand=value )
  def setpreserveSceneUp( self , value ):
    cmds.viewManip( self.uiName , e=1 , preserveSceneUp=value )
  def setrestoreCenter( self , value ):
    cmds.viewManip( self.uiName , e=1 , restoreCenter=value )
  def setresetFront( self , value ):
    cmds.viewManip( self.uiName , e=1 , resetFront=value )
  def setresetHome( self , value ):
    cmds.viewManip( self.uiName , e=1 , resetHome=value )
  def setsize( self , value ):
    cmds.viewManip( self.uiName , e=1 , size=value )
  def setsetFront( self , value ):
    cmds.viewManip( self.uiName , e=1 , setFront=value )
  def setsetHome( self , value ):
    cmds.viewManip( self.uiName , e=1 , setHome=value )
  def setselectionLockParameters( self , value ):
    cmds.viewManip( self.uiName , e=1 , selectionLockParameters=value )
  def settopLeft( self , value ):
    cmds.viewManip( self.uiName , e=1 , topLeft=value )
  def settopRight( self , value ):
    cmds.viewManip( self.uiName , e=1 , topRight=value )
  def settoggleSelectionLock( self , value ):
    cmds.viewManip( self.uiName , e=1 , toggleSelectionLock=value )
  def setvisible( self , value ):
    cmds.viewManip( self.uiName , e=1 , visible=value )
  def setzoomToFitScene( self , value ):
    cmds.viewManip( self.uiName , e=1 , zoomToFitScene=value )

  ##### propertyCode #####
  bottomLeft = property( getbottomLeft , setbottomLeft )
  bottomRight = property( getbottomRight , setbottomRight )
  compassAngle = property( getcompassAngle , setcompassAngle )
  drawCompass = property( getdrawCompass , setdrawCompass )
  dragSnap = property( getdragSnap , setdragSnap )
  frontParameters = property( getfrontParameters , setfrontParameters )
  fitToView = property( getfitToView , setfitToView )
  goDefault = property( getgoDefault , setgoDefault )
  goHome = property( getgoHome , setgoHome )
  homeParameters = property( gethomeParameters , sethomeParameters )
  levelCamera = property( getlevelCamera , setlevelCamera )
  minOpacity = property( getminOpacity , setminOpacity )
  namespace = property( getnamespace , setnamespace )
  postCommand = property( getpostCommand , setpostCommand )
  preCommand = property( getpreCommand , setpreCommand )
  preserveSceneUp = property( getpreserveSceneUp , setpreserveSceneUp )
  restoreCenter = property( getrestoreCenter , setrestoreCenter )
  resetFront = property( getresetFront , setresetFront )
  resetHome = property( getresetHome , setresetHome )
  size = property( getsize , setsize )
  setFront = property( getsetFront , setsetFront )
  setHome = property( getsetHome , setsetHome )
  selectionLockParameters = property( getselectionLockParameters , setselectionLockParameters )
  topLeft = property( gettopLeft , settopLeft )
  topRight = property( gettopRight , settopRight )
  toggleSelectionLock = property( gettoggleSelectionLock , settoggleSelectionLock )
  visible = property( getvisible , setvisible )
  zoomToFitScene = property( getzoomToFitScene , setzoomToFitScene )

  ##### customCode #####





class Visor( Panel ):

  ##### initialize #####
  def __init__( self , addFolder=None , addNodes=None , allowPanningInX=None , allowPanningInY=None , allowZooming=None , command=None , deleteFolder=None , editFolder=None , folderList=None , menu=None , name=None , nodeType=None , openDirectories=None , openFolder=None , popupMenuScript=None , path=None , refreshAllSwatches=None , rebuild=None , restrictPanAndZoom=None , refreshSwatch=None , refreshSelectedSwatches=None , reset=None , scrollBar=None , showDividers=None , showFiles=None , showFolders=None , selectedGadgets=None , showNodes=None , scrollPercent=None , saveSwatches=None , style=None , stateString=None , transform=None , type=None , **args ):
    self.uiName = cmds.visor()

    ##### substitution #####
    if addFolder != None:
      self.addFolder = addFolder
    if addNodes != None:
      self.addNodes = addNodes
    if allowPanningInX != None:
      self.allowPanningInX = allowPanningInX
    if allowPanningInY != None:
      self.allowPanningInY = allowPanningInY
    if allowZooming != None:
      self.allowZooming = allowZooming
    if command != None:
      self.command = command
    if deleteFolder != None:
      self.deleteFolder = deleteFolder
    if editFolder != None:
      self.editFolder = editFolder
    if folderList != None:
      self.folderList = folderList
    if menu != None:
      self.menu = menu
    if name != None:
      self.name = name
    if nodeType != None:
      self.nodeType = nodeType
    if openDirectories != None:
      self.openDirectories = openDirectories
    if openFolder != None:
      self.openFolder = openFolder
    if popupMenuScript != None:
      self.popupMenuScript = popupMenuScript
    if path != None:
      self.path = path
    if refreshAllSwatches != None:
      self.refreshAllSwatches = refreshAllSwatches
    if rebuild != None:
      self.rebuild = rebuild
    if restrictPanAndZoom != None:
      self.restrictPanAndZoom = restrictPanAndZoom
    if refreshSwatch != None:
      self.refreshSwatch = refreshSwatch
    if refreshSelectedSwatches != None:
      self.refreshSelectedSwatches = refreshSelectedSwatches
    if reset != None:
      self.reset = reset
    if scrollBar != None:
      self.scrollBar = scrollBar
    if showDividers != None:
      self.showDividers = showDividers
    if showFiles != None:
      self.showFiles = showFiles
    if showFolders != None:
      self.showFolders = showFolders
    if selectedGadgets != None:
      self.selectedGadgets = selectedGadgets
    if showNodes != None:
      self.showNodes = showNodes
    if scrollPercent != None:
      self.scrollPercent = scrollPercent
    if saveSwatches != None:
      self.saveSwatches = saveSwatches
    if style != None:
      self.style = style
    if stateString != None:
      self.stateString = stateString
    if transform != None:
      self.transform = transform
    if type != None:
      self.type = type

  ##### getFuncCode #####
  def getaddFolder( self ):
    return cmds.visor( self.uiName , q=1 , addFolder=1 )
  def getaddNodes( self ):
    return cmds.visor( self.uiName , q=1 , addNodes=1 )
  def getallowPanningInX( self ):
    return cmds.visor( self.uiName , q=1 , allowPanningInX=1 )
  def getallowPanningInY( self ):
    return cmds.visor( self.uiName , q=1 , allowPanningInY=1 )
  def getallowZooming( self ):
    return cmds.visor( self.uiName , q=1 , allowZooming=1 )
  def getcommand( self ):
    return cmds.visor( self.uiName , q=1 , command=1 )
  def getdeleteFolder( self ):
    return cmds.visor( self.uiName , q=1 , deleteFolder=1 )
  def geteditFolder( self ):
    return cmds.visor( self.uiName , q=1 , editFolder=1 )
  def getfolderList( self ):
    return cmds.visor( self.uiName , q=1 , folderList=1 )
  def getmenu( self ):
    return cmds.visor( self.uiName , q=1 , menu=1 )
  def getname( self ):
    return cmds.visor( self.uiName , q=1 , name=1 )
  def getnodeType( self ):
    return cmds.visor( self.uiName , q=1 , nodeType=1 )
  def getopenDirectories( self ):
    return cmds.visor( self.uiName , q=1 , openDirectories=1 )
  def getopenFolder( self ):
    return cmds.visor( self.uiName , q=1 , openFolder=1 )
  def getpopupMenuScript( self ):
    return cmds.visor( self.uiName , q=1 , popupMenuScript=1 )
  def getpath( self ):
    return cmds.visor( self.uiName , q=1 , path=1 )
  def getrefreshAllSwatches( self ):
    return cmds.visor( self.uiName , q=1 , refreshAllSwatches=1 )
  def getrebuild( self ):
    return cmds.visor( self.uiName , q=1 , rebuild=1 )
  def getrestrictPanAndZoom( self ):
    return cmds.visor( self.uiName , q=1 , restrictPanAndZoom=1 )
  def getrefreshSwatch( self ):
    return cmds.visor( self.uiName , q=1 , refreshSwatch=1 )
  def getrefreshSelectedSwatches( self ):
    return cmds.visor( self.uiName , q=1 , refreshSelectedSwatches=1 )
  def getreset( self ):
    return cmds.visor( self.uiName , q=1 , reset=1 )
  def getscrollBar( self ):
    return cmds.visor( self.uiName , q=1 , scrollBar=1 )
  def getshowDividers( self ):
    return cmds.visor( self.uiName , q=1 , showDividers=1 )
  def getshowFiles( self ):
    return cmds.visor( self.uiName , q=1 , showFiles=1 )
  def getshowFolders( self ):
    return cmds.visor( self.uiName , q=1 , showFolders=1 )
  def getselectedGadgets( self ):
    return cmds.visor( self.uiName , q=1 , selectedGadgets=1 )
  def getshowNodes( self ):
    return cmds.visor( self.uiName , q=1 , showNodes=1 )
  def getscrollPercent( self ):
    return cmds.visor( self.uiName , q=1 , scrollPercent=1 )
  def getsaveSwatches( self ):
    return cmds.visor( self.uiName , q=1 , saveSwatches=1 )
  def getstyle( self ):
    return cmds.visor( self.uiName , q=1 , style=1 )
  def getstateString( self ):
    return cmds.visor( self.uiName , q=1 , stateString=1 )
  def gettransform( self ):
    return cmds.visor( self.uiName , q=1 , transform=1 )
  def gettype( self ):
    return cmds.visor( self.uiName , q=1 , type=1 )

  ##### setFuncCode #####
  def setaddFolder( self , value ):
    cmds.visor( self.uiName , e=1 , addFolder=value )
  def setaddNodes( self , value ):
    cmds.visor( self.uiName , e=1 , addNodes=value )
  def setallowPanningInX( self , value ):
    cmds.visor( self.uiName , e=1 , allowPanningInX=value )
  def setallowPanningInY( self , value ):
    cmds.visor( self.uiName , e=1 , allowPanningInY=value )
  def setallowZooming( self , value ):
    cmds.visor( self.uiName , e=1 , allowZooming=value )
  def setcommand( self , value ):
    cmds.visor( self.uiName , e=1 , command=value )
  def setdeleteFolder( self , value ):
    cmds.visor( self.uiName , e=1 , deleteFolder=value )
  def seteditFolder( self , value ):
    cmds.visor( self.uiName , e=1 , editFolder=value )
  def setfolderList( self , value ):
    cmds.visor( self.uiName , e=1 , folderList=value )
  def setmenu( self , value ):
    cmds.visor( self.uiName , e=1 , menu=value )
  def setname( self , value ):
    cmds.visor( self.uiName , e=1 , name=value )
  def setnodeType( self , value ):
    cmds.visor( self.uiName , e=1 , nodeType=value )
  def setopenDirectories( self , value ):
    cmds.visor( self.uiName , e=1 , openDirectories=value )
  def setopenFolder( self , value ):
    cmds.visor( self.uiName , e=1 , openFolder=value )
  def setpopupMenuScript( self , value ):
    cmds.visor( self.uiName , e=1 , popupMenuScript=value )
  def setpath( self , value ):
    cmds.visor( self.uiName , e=1 , path=value )
  def setrefreshAllSwatches( self , value ):
    cmds.visor( self.uiName , e=1 , refreshAllSwatches=value )
  def setrebuild( self , value ):
    cmds.visor( self.uiName , e=1 , rebuild=value )
  def setrestrictPanAndZoom( self , value ):
    cmds.visor( self.uiName , e=1 , restrictPanAndZoom=value )
  def setrefreshSwatch( self , value ):
    cmds.visor( self.uiName , e=1 , refreshSwatch=value )
  def setrefreshSelectedSwatches( self , value ):
    cmds.visor( self.uiName , e=1 , refreshSelectedSwatches=value )
  def setreset( self , value ):
    cmds.visor( self.uiName , e=1 , reset=value )
  def setscrollBar( self , value ):
    cmds.visor( self.uiName , e=1 , scrollBar=value )
  def setshowDividers( self , value ):
    cmds.visor( self.uiName , e=1 , showDividers=value )
  def setshowFiles( self , value ):
    cmds.visor( self.uiName , e=1 , showFiles=value )
  def setshowFolders( self , value ):
    cmds.visor( self.uiName , e=1 , showFolders=value )
  def setselectedGadgets( self , value ):
    cmds.visor( self.uiName , e=1 , selectedGadgets=value )
  def setshowNodes( self , value ):
    cmds.visor( self.uiName , e=1 , showNodes=value )
  def setscrollPercent( self , value ):
    cmds.visor( self.uiName , e=1 , scrollPercent=value )
  def setsaveSwatches( self , value ):
    cmds.visor( self.uiName , e=1 , saveSwatches=value )
  def setstyle( self , value ):
    cmds.visor( self.uiName , e=1 , style=value )
  def setstateString( self , value ):
    cmds.visor( self.uiName , e=1 , stateString=value )
  def settransform( self , value ):
    cmds.visor( self.uiName , e=1 , transform=value )
  def settype( self , value ):
    cmds.visor( self.uiName , e=1 , type=value )

  ##### propertyCode #####
  addFolder = property( getaddFolder , setaddFolder )
  addNodes = property( getaddNodes , setaddNodes )
  allowPanningInX = property( getallowPanningInX , setallowPanningInX )
  allowPanningInY = property( getallowPanningInY , setallowPanningInY )
  allowZooming = property( getallowZooming , setallowZooming )
  command = property( getcommand , setcommand )
  deleteFolder = property( getdeleteFolder , setdeleteFolder )
  editFolder = property( geteditFolder , seteditFolder )
  folderList = property( getfolderList , setfolderList )
  menu = property( getmenu , setmenu )
  name = property( getname , setname )
  nodeType = property( getnodeType , setnodeType )
  openDirectories = property( getopenDirectories , setopenDirectories )
  openFolder = property( getopenFolder , setopenFolder )
  popupMenuScript = property( getpopupMenuScript , setpopupMenuScript )
  path = property( getpath , setpath )
  refreshAllSwatches = property( getrefreshAllSwatches , setrefreshAllSwatches )
  rebuild = property( getrebuild , setrebuild )
  restrictPanAndZoom = property( getrestrictPanAndZoom , setrestrictPanAndZoom )
  refreshSwatch = property( getrefreshSwatch , setrefreshSwatch )
  refreshSelectedSwatches = property( getrefreshSelectedSwatches , setrefreshSelectedSwatches )
  reset = property( getreset , setreset )
  scrollBar = property( getscrollBar , setscrollBar )
  showDividers = property( getshowDividers , setshowDividers )
  showFiles = property( getshowFiles , setshowFiles )
  showFolders = property( getshowFolders , setshowFolders )
  selectedGadgets = property( getselectedGadgets , setselectedGadgets )
  showNodes = property( getshowNodes , setshowNodes )
  scrollPercent = property( getscrollPercent , setscrollPercent )
  saveSwatches = property( getsaveSwatches , setsaveSwatches )
  style = property( getstyle , setstyle )
  stateString = property( getstateString , setstateString )
  transform = property( gettransform , settransform )
  type = property( gettype , settype )

  ##### customCode #####





class WebBrowser( Panel ):

  ##### initialize #####
  def __init__( self , annotation=None , backgroundColor=None , back=None , command=None , dragCallback=None , dropCallback=None , enable=None , find=None , forward=None , height=None , home=None , isObscured=None , manage=None , matchCase=None , matchWholeWord=None , numberOfPopupMenus=None , popupMenuArray=None , preventOverride=None , reload=None , searchForward=None , stop=None , urlChangedCb=None , openURL=None , visible=None , width=None , wrap=None , **args ):
    self.uiName = cmds.webBrowser()

    ##### substitution #####
    if annotation != None:
      self.annotation = annotation
    if backgroundColor != None:
      self.backgroundColor = backgroundColor
    if back != None:
      self.back = back
    if command != None:
      self.command = command
    if dragCallback != None:
      self.dragCallback = dragCallback
    if dropCallback != None:
      self.dropCallback = dropCallback
    if enable != None:
      self.enable = enable
    if find != None:
      self.find = find
    if forward != None:
      self.forward = forward
    if height != None:
      self.height = height
    if home != None:
      self.home = home
    if isObscured != None:
      self.isObscured = isObscured
    if manage != None:
      self.manage = manage
    if matchCase != None:
      self.matchCase = matchCase
    if matchWholeWord != None:
      self.matchWholeWord = matchWholeWord
    if numberOfPopupMenus != None:
      self.numberOfPopupMenus = numberOfPopupMenus
    if popupMenuArray != None:
      self.popupMenuArray = popupMenuArray
    if preventOverride != None:
      self.preventOverride = preventOverride
    if reload != None:
      self.reload = reload
    if searchForward != None:
      self.searchForward = searchForward
    if stop != None:
      self.stop = stop
    if urlChangedCb != None:
      self.urlChangedCb = urlChangedCb
    if openURL != None:
      self.openURL = openURL
    if visible != None:
      self.visible = visible
    if width != None:
      self.width = width
    if wrap != None:
      self.wrap = wrap

  ##### getFuncCode #####
  def getannotation( self ):
    return cmds.webBrowser( self.uiName , q=1 , annotation=1 )
  def getbackgroundColor( self ):
    return cmds.webBrowser( self.uiName , q=1 , backgroundColor=1 )
  def getback( self ):
    return cmds.webBrowser( self.uiName , q=1 , back=1 )
  def getcommand( self ):
    return cmds.webBrowser( self.uiName , q=1 , command=1 )
  def getdragCallback( self ):
    return cmds.webBrowser( self.uiName , q=1 , dragCallback=1 )
  def getdropCallback( self ):
    return cmds.webBrowser( self.uiName , q=1 , dropCallback=1 )
  def getenable( self ):
    return cmds.webBrowser( self.uiName , q=1 , enable=1 )
  def getfind( self ):
    return cmds.webBrowser( self.uiName , q=1 , find=1 )
  def getforward( self ):
    return cmds.webBrowser( self.uiName , q=1 , forward=1 )
  def getheight( self ):
    return cmds.webBrowser( self.uiName , q=1 , height=1 )
  def gethome( self ):
    return cmds.webBrowser( self.uiName , q=1 , home=1 )
  def getisObscured( self ):
    return cmds.webBrowser( self.uiName , q=1 , isObscured=1 )
  def getmanage( self ):
    return cmds.webBrowser( self.uiName , q=1 , manage=1 )
  def getmatchCase( self ):
    return cmds.webBrowser( self.uiName , q=1 , matchCase=1 )
  def getmatchWholeWord( self ):
    return cmds.webBrowser( self.uiName , q=1 , matchWholeWord=1 )
  def getnumberOfPopupMenus( self ):
    return cmds.webBrowser( self.uiName , q=1 , numberOfPopupMenus=1 )
  def getpopupMenuArray( self ):
    return cmds.webBrowser( self.uiName , q=1 , popupMenuArray=1 )
  def getpreventOverride( self ):
    return cmds.webBrowser( self.uiName , q=1 , preventOverride=1 )
  def getreload( self ):
    return cmds.webBrowser( self.uiName , q=1 , reload=1 )
  def getsearchForward( self ):
    return cmds.webBrowser( self.uiName , q=1 , searchForward=1 )
  def getstop( self ):
    return cmds.webBrowser( self.uiName , q=1 , stop=1 )
  def geturlChangedCb( self ):
    return cmds.webBrowser( self.uiName , q=1 , urlChangedCb=1 )
  def getopenURL( self ):
    return cmds.webBrowser( self.uiName , q=1 , openURL=1 )
  def getvisible( self ):
    return cmds.webBrowser( self.uiName , q=1 , visible=1 )
  def getwidth( self ):
    return cmds.webBrowser( self.uiName , q=1 , width=1 )
  def getwrap( self ):
    return cmds.webBrowser( self.uiName , q=1 , wrap=1 )

  ##### setFuncCode #####
  def setannotation( self , value ):
    cmds.webBrowser( self.uiName , e=1 , annotation=value )
  def setbackgroundColor( self , value ):
    cmds.webBrowser( self.uiName , e=1 , backgroundColor=value )
  def setback( self , value ):
    cmds.webBrowser( self.uiName , e=1 , back=value )
  def setcommand( self , value ):
    cmds.webBrowser( self.uiName , e=1 , command=value )
  def setdragCallback( self , value ):
    cmds.webBrowser( self.uiName , e=1 , dragCallback=value )
  def setdropCallback( self , value ):
    cmds.webBrowser( self.uiName , e=1 , dropCallback=value )
  def setenable( self , value ):
    cmds.webBrowser( self.uiName , e=1 , enable=value )
  def setfind( self , value ):
    cmds.webBrowser( self.uiName , e=1 , find=value )
  def setforward( self , value ):
    cmds.webBrowser( self.uiName , e=1 , forward=value )
  def setheight( self , value ):
    cmds.webBrowser( self.uiName , e=1 , height=value )
  def sethome( self , value ):
    cmds.webBrowser( self.uiName , e=1 , home=value )
  def setisObscured( self , value ):
    cmds.webBrowser( self.uiName , e=1 , isObscured=value )
  def setmanage( self , value ):
    cmds.webBrowser( self.uiName , e=1 , manage=value )
  def setmatchCase( self , value ):
    cmds.webBrowser( self.uiName , e=1 , matchCase=value )
  def setmatchWholeWord( self , value ):
    cmds.webBrowser( self.uiName , e=1 , matchWholeWord=value )
  def setnumberOfPopupMenus( self , value ):
    cmds.webBrowser( self.uiName , e=1 , numberOfPopupMenus=value )
  def setpopupMenuArray( self , value ):
    cmds.webBrowser( self.uiName , e=1 , popupMenuArray=value )
  def setpreventOverride( self , value ):
    cmds.webBrowser( self.uiName , e=1 , preventOverride=value )
  def setreload( self , value ):
    cmds.webBrowser( self.uiName , e=1 , reload=value )
  def setsearchForward( self , value ):
    cmds.webBrowser( self.uiName , e=1 , searchForward=value )
  def setstop( self , value ):
    cmds.webBrowser( self.uiName , e=1 , stop=value )
  def seturlChangedCb( self , value ):
    cmds.webBrowser( self.uiName , e=1 , urlChangedCb=value )
  def setopenURL( self , value ):
    cmds.webBrowser( self.uiName , e=1 , openURL=value )
  def setvisible( self , value ):
    cmds.webBrowser( self.uiName , e=1 , visible=value )
  def setwidth( self , value ):
    cmds.webBrowser( self.uiName , e=1 , width=value )
  def setwrap( self , value ):
    cmds.webBrowser( self.uiName , e=1 , wrap=value )

  ##### propertyCode #####
  annotation = property( getannotation , setannotation )
  backgroundColor = property( getbackgroundColor , setbackgroundColor )
  back = property( getback , setback )
  command = property( getcommand , setcommand )
  dragCallback = property( getdragCallback , setdragCallback )
  dropCallback = property( getdropCallback , setdropCallback )
  enable = property( getenable , setenable )
  find = property( getfind , setfind )
  forward = property( getforward , setforward )
  height = property( getheight , setheight )
  home = property( gethome , sethome )
  isObscured = property( getisObscured , setisObscured )
  manage = property( getmanage , setmanage )
  matchCase = property( getmatchCase , setmatchCase )
  matchWholeWord = property( getmatchWholeWord , setmatchWholeWord )
  numberOfPopupMenus = property( getnumberOfPopupMenus , setnumberOfPopupMenus )
  popupMenuArray = property( getpopupMenuArray , setpopupMenuArray )
  preventOverride = property( getpreventOverride , setpreventOverride )
  reload = property( getreload , setreload )
  searchForward = property( getsearchForward , setsearchForward )
  stop = property( getstop , setstop )
  urlChangedCb = property( geturlChangedCb , seturlChangedCb )
  openURL = property( getopenURL , setopenURL )
  visible = property( getvisible , setvisible )
  width = property( getwidth , setwidth )
  wrap = property( getwrap , setwrap )

  ##### customCode #####





class WebBrowserPrefs( Panel ):

  ##### initialize #####
  def __init__( self , preference=None , **args ):
    self.uiName = cmds.webBrowserPrefs()

    ##### substitution #####
    if preference != None:
      self.preference = preference

  ##### getFuncCode #####
  def getpreference( self ):
    return cmds.webBrowserPrefs( self.uiName , q=1 , preference=1 )

  ##### setFuncCode #####
  def setpreference( self , value ):
    cmds.webBrowserPrefs( self.uiName , e=1 , preference=value )

  ##### propertyCode #####
  preference = property( getpreference , setpreference )

  ##### customCode #####





print "MODULE IMPORTED... MYAM_PyLib_mayaUI_panel"