#-*- coding:UTF-8 -*-

#*******************************************************************************
'''

Tool Name     : MYAM_PyLib_mayaUI_window
Description   : MayaのWindowグループに属するUI要素をオブジェクト指向ライクに扱うためのモジュール

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



class Window( object ):

  ##### initialize #####
  def __init__( self , backgroundColor=None , defineTemplate=None , docTag=None , exists=None , frontWindow=None , height=None , iconify=None , iconName=None , interactivePlacement=None , leftEdge=None , menuArray=None , menuBar=None , menuBarVisible=None , menuIndex=None , mainMenuBar=None , minimizeButton=None , minimizeCommand=None , mainWindow=None , maximizeButton=None , numberOfMenus=None , restoreCommand=None , retain=None , resizeToFitChildren=None , sizeable=None , title=None , titleBar=None , titleBarMenu=None , topEdge=None , toolbox=None , topLeftCorner=None , useTemplate=None , visible=None , width=None , widthHeight=None , **args ):
    self.uiName = cmds.window( menuBar=1 )

    ##### substitution #####
    if backgroundColor != None:
      self.backgroundColor = backgroundColor
    if defineTemplate != None:
      self.defineTemplate = defineTemplate
    if docTag != None:
      self.docTag = docTag
    if exists != None:
      self.exists = exists
    if frontWindow != None:
      self.frontWindow = frontWindow
    if height != None:
      self.height = height
    if iconify != None:
      self.iconify = iconify
    if iconName != None:
      self.iconName = iconName
    if interactivePlacement != None:
      self.interactivePlacement = interactivePlacement
    if leftEdge != None:
      self.leftEdge = leftEdge
    if menuArray != None:
      self.menuArray = menuArray
    if menuBar != None:
      self.menuBar = menuBar
    if menuBarVisible != None:
      self.menuBarVisible = menuBarVisible
    if menuIndex != None:
      self.menuIndex = menuIndex
    if mainMenuBar != None:
      self.mainMenuBar = mainMenuBar
    if minimizeButton != None:
      self.minimizeButton = minimizeButton
    if minimizeCommand != None:
      self.minimizeCommand = minimizeCommand
    if mainWindow != None:
      self.mainWindow = mainWindow
    if maximizeButton != None:
      self.maximizeButton = maximizeButton
    if numberOfMenus != None:
      self.numberOfMenus = numberOfMenus
    if restoreCommand != None:
      self.restoreCommand = restoreCommand
    if retain != None:
      self.retain = retain
    if resizeToFitChildren != None:
      self.resizeToFitChildren = resizeToFitChildren
    if sizeable != None:
      self.sizeable = sizeable
    if title != None:
      self.title = title
    if titleBar != None:
      self.titleBar = titleBar
    if titleBarMenu != None:
      self.titleBarMenu = titleBarMenu
    if topEdge != None:
      self.topEdge = topEdge
    if toolbox != None:
      self.toolbox = toolbox
    if topLeftCorner != None:
      self.topLeftCorner = topLeftCorner
    if useTemplate != None:
      self.useTemplate = useTemplate
    if visible != None:
      self.visible = visible
    if width != None:
      self.width = width
    if widthHeight != None:
      self.widthHeight = widthHeight

  ##### getFuncCode #####
  def getbackgroundColor( self ):
    return cmds.window( self.uiName , q=1 , backgroundColor=1 )
  def getdefineTemplate( self ):
    return cmds.window( self.uiName , q=1 , defineTemplate=1 )
  def getdocTag( self ):
    return cmds.window( self.uiName , q=1 , docTag=1 )
  def getexists( self ):
    return cmds.window( self.uiName , q=1 , exists=1 )
  def getfrontWindow( self ):
    return cmds.window( self.uiName , q=1 , frontWindow=1 )
  def getheight( self ):
    return cmds.window( self.uiName , q=1 , height=1 )
  def geticonify( self ):
    return cmds.window( self.uiName , q=1 , iconify=1 )
  def geticonName( self ):
    return cmds.window( self.uiName , q=1 , iconName=1 )
  def getinteractivePlacement( self ):
    return cmds.window( self.uiName , q=1 , interactivePlacement=1 )
  def getleftEdge( self ):
    return cmds.window( self.uiName , q=1 , leftEdge=1 )
  def getmenuArray( self ):
    return cmds.window( self.uiName , q=1 , menuArray=1 )
  def getmenuBar( self ):
    return cmds.window( self.uiName , q=1 , menuBar=1 )
  def getmenuBarVisible( self ):
    return cmds.window( self.uiName , q=1 , menuBarVisible=1 )
  def getmenuIndex( self ):
    return cmds.window( self.uiName , q=1 , menuIndex=1 )
  def getmainMenuBar( self ):
    return cmds.window( self.uiName , q=1 , mainMenuBar=1 )
  def getminimizeButton( self ):
    return cmds.window( self.uiName , q=1 , minimizeButton=1 )
  def getminimizeCommand( self ):
    return cmds.window( self.uiName , q=1 , minimizeCommand=1 )
  def getmainWindow( self ):
    return cmds.window( self.uiName , q=1 , mainWindow=1 )
  def getmaximizeButton( self ):
    return cmds.window( self.uiName , q=1 , maximizeButton=1 )
  def getnumberOfMenus( self ):
    return cmds.window( self.uiName , q=1 , numberOfMenus=1 )
  def getrestoreCommand( self ):
    return cmds.window( self.uiName , q=1 , restoreCommand=1 )
  def getretain( self ):
    return cmds.window( self.uiName , q=1 , retain=1 )
  def getresizeToFitChildren( self ):
    return cmds.window( self.uiName , q=1 , resizeToFitChildren=1 )
  def getsizeable( self ):
    return cmds.window( self.uiName , q=1 , sizeable=1 )
  def gettitle( self ):
    return cmds.window( self.uiName , q=1 , title=1 )
  def gettitleBar( self ):
    return cmds.window( self.uiName , q=1 , titleBar=1 )
  def gettitleBarMenu( self ):
    return cmds.window( self.uiName , q=1 , titleBarMenu=1 )
  def gettopEdge( self ):
    return cmds.window( self.uiName , q=1 , topEdge=1 )
  def gettoolbox( self ):
    return cmds.window( self.uiName , q=1 , toolbox=1 )
  def gettopLeftCorner( self ):
    return cmds.window( self.uiName , q=1 , topLeftCorner=1 )
  def getuseTemplate( self ):
    return cmds.window( self.uiName , q=1 , useTemplate=1 )
  def getvisible( self ):
    return cmds.window( self.uiName , q=1 , visible=1 )
  def getwidth( self ):
    return cmds.window( self.uiName , q=1 , width=1 )
  def getwidthHeight( self ):
    return cmds.window( self.uiName , q=1 , widthHeight=1 )

  ##### setFuncCode #####
  def setbackgroundColor( self , value ):
    cmds.window( self.uiName , e=1 , backgroundColor=value )
  def setdefineTemplate( self , value ):
    cmds.window( self.uiName , e=1 , defineTemplate=value )
  def setdocTag( self , value ):
    cmds.window( self.uiName , e=1 , docTag=value )
  def setexists( self , value ):
    cmds.window( self.uiName , e=1 , exists=value )
  def setfrontWindow( self , value ):
    cmds.window( self.uiName , e=1 , frontWindow=value )
  def setheight( self , value ):
    cmds.window( self.uiName , e=1 , height=value )
  def seticonify( self , value ):
    cmds.window( self.uiName , e=1 , iconify=value )
  def seticonName( self , value ):
    cmds.window( self.uiName , e=1 , iconName=value )
  def setinteractivePlacement( self , value ):
    cmds.window( self.uiName , e=1 , interactivePlacement=value )
  def setleftEdge( self , value ):
    cmds.window( self.uiName , e=1 , leftEdge=value )
  def setmenuArray( self , value ):
    cmds.window( self.uiName , e=1 , menuArray=value )
  def setmenuBar( self , value ):
    cmds.window( self.uiName , e=1 , menuBar=value )
  def setmenuBarVisible( self , value ):
    cmds.window( self.uiName , e=1 , menuBarVisible=value )
  def setmenuIndex( self , value ):
    cmds.window( self.uiName , e=1 , menuIndex=value )
  def setmainMenuBar( self , value ):
    cmds.window( self.uiName , e=1 , mainMenuBar=value )
  def setminimizeButton( self , value ):
    cmds.window( self.uiName , e=1 , minimizeButton=value )
  def setminimizeCommand( self , value ):
    cmds.window( self.uiName , e=1 , minimizeCommand=value )
  def setmainWindow( self , value ):
    cmds.window( self.uiName , e=1 , mainWindow=value )
  def setmaximizeButton( self , value ):
    cmds.window( self.uiName , e=1 , maximizeButton=value )
  def setnumberOfMenus( self , value ):
    cmds.window( self.uiName , e=1 , numberOfMenus=value )
  def setrestoreCommand( self , value ):
    cmds.window( self.uiName , e=1 , restoreCommand=value )
  def setretain( self , value ):
    cmds.window( self.uiName , e=1 , retain=value )
  def setresizeToFitChildren( self , value ):
    cmds.window( self.uiName , e=1 , resizeToFitChildren=value )
  def setsizeable( self , value ):
    cmds.window( self.uiName , e=1 , sizeable=value )
  def settitle( self , value ):
    cmds.window( self.uiName , e=1 , title=value )
  def settitleBar( self , value ):
    cmds.window( self.uiName , e=1 , titleBar=value )
  def settitleBarMenu( self , value ):
    cmds.window( self.uiName , e=1 , titleBarMenu=value )
  def settopEdge( self , value ):
    cmds.window( self.uiName , e=1 , topEdge=value )
  def settoolbox( self , value ):
    cmds.window( self.uiName , e=1 , toolbox=value )
  def settopLeftCorner( self , value ):
    cmds.window( self.uiName , e=1 , topLeftCorner=value )
  def setuseTemplate( self , value ):
    cmds.window( self.uiName , e=1 , useTemplate=value )
  def setvisible( self , value ):
    cmds.window( self.uiName , e=1 , visible=value )
  def setwidth( self , value ):
    cmds.window( self.uiName , e=1 , width=value )
  def setwidthHeight( self , value ):
    cmds.window( self.uiName , e=1 , widthHeight=value )

  ##### propertyCode #####
  backgroundColor = property( getbackgroundColor , setbackgroundColor )
  defineTemplate = property( getdefineTemplate , setdefineTemplate )
  docTag = property( getdocTag , setdocTag )
  exists = property( getexists , setexists )
  frontWindow = property( getfrontWindow , setfrontWindow )
  height = property( getheight , setheight )
  iconify = property( geticonify , seticonify )
  iconName = property( geticonName , seticonName )
  interactivePlacement = property( getinteractivePlacement , setinteractivePlacement )
  leftEdge = property( getleftEdge , setleftEdge )
  menuArray = property( getmenuArray , setmenuArray )
  menuBar = property( getmenuBar , setmenuBar )
  menuBarVisible = property( getmenuBarVisible , setmenuBarVisible )
  menuIndex = property( getmenuIndex , setmenuIndex )
  mainMenuBar = property( getmainMenuBar , setmainMenuBar )
  minimizeButton = property( getminimizeButton , setminimizeButton )
  minimizeCommand = property( getminimizeCommand , setminimizeCommand )
  mainWindow = property( getmainWindow , setmainWindow )
  maximizeButton = property( getmaximizeButton , setmaximizeButton )
  numberOfMenus = property( getnumberOfMenus , setnumberOfMenus )
  restoreCommand = property( getrestoreCommand , setrestoreCommand )
  retain = property( getretain , setretain )
  resizeToFitChildren = property( getresizeToFitChildren , setresizeToFitChildren )
  sizeable = property( getsizeable , setsizeable )
  title = property( gettitle , settitle )
  titleBar = property( gettitleBar , settitleBar )
  titleBarMenu = property( gettitleBarMenu , settitleBarMenu )
  topEdge = property( gettopEdge , settopEdge )
  toolbox = property( gettoolbox , settoolbox )
  topLeftCorner = property( gettopLeftCorner , settopLeftCorner )
  useTemplate = property( getuseTemplate , setuseTemplate )
  visible = property( getvisible , setvisible )
  width = property( getwidth , setwidth )
  widthHeight = property( getwidthHeight , setwidthHeight )

  ##### customCode #####





class ColorEditor( Window ):

  ##### initialize #####
  def __init__( self , alpha=None , hsvValue=None , parent=None , result=None , rgbValue=None , **args ):
    self.uiName = cmds.colorEditor()

    ##### substitution #####
    if alpha != None:
      self.alpha = alpha
    if hsvValue != None:
      self.hsvValue = hsvValue
    if parent != None:
      self.parent = parent
    if result != None:
      self.result = result
    if rgbValue != None:
      self.rgbValue = rgbValue

  ##### getFuncCode #####
  def getalpha( self ):
    return cmds.colorEditor( self.uiName , q=1 , alpha=1 )
  def gethsvValue( self ):
    return cmds.colorEditor( self.uiName , q=1 , hsvValue=1 )
  def getparent( self ):
    return cmds.colorEditor( self.uiName , q=1 , parent=1 )
  def getresult( self ):
    return cmds.colorEditor( self.uiName , q=1 , result=1 )
  def getrgbValue( self ):
    return cmds.colorEditor( self.uiName , q=1 , rgbValue=1 )

  ##### setFuncCode #####
  def setalpha( self , value ):
    cmds.colorEditor( self.uiName , e=1 , alpha=value )
  def sethsvValue( self , value ):
    cmds.colorEditor( self.uiName , e=1 , hsvValue=value )
  def setparent( self , value ):
    cmds.colorEditor( self.uiName , e=1 , parent=value )
  def setresult( self , value ):
    cmds.colorEditor( self.uiName , e=1 , result=value )
  def setrgbValue( self , value ):
    cmds.colorEditor( self.uiName , e=1 , rgbValue=value )

  ##### propertyCode #####
  alpha = property( getalpha , setalpha )
  hsvValue = property( gethsvValue , sethsvValue )
  parent = property( getparent , setparent )
  result = property( getresult , setresult )
  rgbValue = property( getrgbValue , setrgbValue )

  ##### customCode #####





class ConfirmDialog( Window ):

  ##### initialize #####
  def __init__( self , button=None , cancelButton=None , defaultButton=None , dismissString=None , message=None , messageAlign=None , parent=None , **args ):
    self.uiName = cmds.confirmDialog()

    ##### substitution #####
    if button != None:
      self.button = button
    if cancelButton != None:
      self.cancelButton = cancelButton
    if defaultButton != None:
      self.defaultButton = defaultButton
    if dismissString != None:
      self.dismissString = dismissString
    if message != None:
      self.message = message
    if messageAlign != None:
      self.messageAlign = messageAlign
    if parent != None:
      self.parent = parent

  ##### getFuncCode #####
  def getbutton( self ):
    return cmds.confirmDialog( self.uiName , q=1 , button=1 )
  def getcancelButton( self ):
    return cmds.confirmDialog( self.uiName , q=1 , cancelButton=1 )
  def getdefaultButton( self ):
    return cmds.confirmDialog( self.uiName , q=1 , defaultButton=1 )
  def getdismissString( self ):
    return cmds.confirmDialog( self.uiName , q=1 , dismissString=1 )
  def getmessage( self ):
    return cmds.confirmDialog( self.uiName , q=1 , message=1 )
  def getmessageAlign( self ):
    return cmds.confirmDialog( self.uiName , q=1 , messageAlign=1 )
  def getparent( self ):
    return cmds.confirmDialog( self.uiName , q=1 , parent=1 )

  ##### setFuncCode #####
  def setbutton( self , value ):
    cmds.confirmDialog( self.uiName , e=1 , button=value )
  def setcancelButton( self , value ):
    cmds.confirmDialog( self.uiName , e=1 , cancelButton=value )
  def setdefaultButton( self , value ):
    cmds.confirmDialog( self.uiName , e=1 , defaultButton=value )
  def setdismissString( self , value ):
    cmds.confirmDialog( self.uiName , e=1 , dismissString=value )
  def setmessage( self , value ):
    cmds.confirmDialog( self.uiName , e=1 , message=value )
  def setmessageAlign( self , value ):
    cmds.confirmDialog( self.uiName , e=1 , messageAlign=value )
  def setparent( self , value ):
    cmds.confirmDialog( self.uiName , e=1 , parent=value )

  ##### propertyCode #####
  button = property( getbutton , setbutton )
  cancelButton = property( getcancelButton , setcancelButton )
  defaultButton = property( getdefaultButton , setdefaultButton )
  dismissString = property( getdismissString , setdismissString )
  message = property( getmessage , setmessage )
  messageAlign = property( getmessageAlign , setmessageAlign )
  parent = property( getparent , setparent )

  ##### customCode #####





class CreateEditor( Window ):

  ##### initialize #####
  def __init__( self , queueForDelete=None , **args ):
    self.uiName = cmds.createEditor()

    ##### substitution #####
    if queueForDelete != None:
      self.queueForDelete = queueForDelete

  ##### getFuncCode #####
  def getqueueForDelete( self ):
    return cmds.createEditor( self.uiName , q=1 , queueForDelete=1 )

  ##### setFuncCode #####
  def setqueueForDelete( self , value ):
    cmds.createEditor( self.uiName , e=1 , queueForDelete=value )

  ##### propertyCode #####
  queueForDelete = property( getqueueForDelete , setqueueForDelete )

  ##### customCode #####





class DefaultNavigation( Window ):

  ##### initialize #####
  def __init__( self , connectToExisting=None , createNew=None , destination=None , delete=None , disconnect=None , defaultTraversal=None , defaultWorkingNode=None , force=None , ignore=None , navigatorDecisionString=None , quiet=None , relatedNodes=None , source=None , unignore=None , **args ):
    self.uiName = cmds.defaultNavigation()

    ##### substitution #####
    if connectToExisting != None:
      self.connectToExisting = connectToExisting
    if createNew != None:
      self.createNew = createNew
    if destination != None:
      self.destination = destination
    if delete != None:
      self.delete = delete
    if disconnect != None:
      self.disconnect = disconnect
    if defaultTraversal != None:
      self.defaultTraversal = defaultTraversal
    if defaultWorkingNode != None:
      self.defaultWorkingNode = defaultWorkingNode
    if force != None:
      self.force = force
    if ignore != None:
      self.ignore = ignore
    if navigatorDecisionString != None:
      self.navigatorDecisionString = navigatorDecisionString
    if quiet != None:
      self.quiet = quiet
    if relatedNodes != None:
      self.relatedNodes = relatedNodes
    if source != None:
      self.source = source
    if unignore != None:
      self.unignore = unignore

  ##### getFuncCode #####
  def getconnectToExisting( self ):
    return cmds.defaultNavigation( self.uiName , q=1 , connectToExisting=1 )
  def getcreateNew( self ):
    return cmds.defaultNavigation( self.uiName , q=1 , createNew=1 )
  def getdestination( self ):
    return cmds.defaultNavigation( self.uiName , q=1 , destination=1 )
  def getdelete( self ):
    return cmds.defaultNavigation( self.uiName , q=1 , delete=1 )
  def getdisconnect( self ):
    return cmds.defaultNavigation( self.uiName , q=1 , disconnect=1 )
  def getdefaultTraversal( self ):
    return cmds.defaultNavigation( self.uiName , q=1 , defaultTraversal=1 )
  def getdefaultWorkingNode( self ):
    return cmds.defaultNavigation( self.uiName , q=1 , defaultWorkingNode=1 )
  def getforce( self ):
    return cmds.defaultNavigation( self.uiName , q=1 , force=1 )
  def getignore( self ):
    return cmds.defaultNavigation( self.uiName , q=1 , ignore=1 )
  def getnavigatorDecisionString( self ):
    return cmds.defaultNavigation( self.uiName , q=1 , navigatorDecisionString=1 )
  def getquiet( self ):
    return cmds.defaultNavigation( self.uiName , q=1 , quiet=1 )
  def getrelatedNodes( self ):
    return cmds.defaultNavigation( self.uiName , q=1 , relatedNodes=1 )
  def getsource( self ):
    return cmds.defaultNavigation( self.uiName , q=1 , source=1 )
  def getunignore( self ):
    return cmds.defaultNavigation( self.uiName , q=1 , unignore=1 )

  ##### setFuncCode #####
  def setconnectToExisting( self , value ):
    cmds.defaultNavigation( self.uiName , e=1 , connectToExisting=value )
  def setcreateNew( self , value ):
    cmds.defaultNavigation( self.uiName , e=1 , createNew=value )
  def setdestination( self , value ):
    cmds.defaultNavigation( self.uiName , e=1 , destination=value )
  def setdelete( self , value ):
    cmds.defaultNavigation( self.uiName , e=1 , delete=value )
  def setdisconnect( self , value ):
    cmds.defaultNavigation( self.uiName , e=1 , disconnect=value )
  def setdefaultTraversal( self , value ):
    cmds.defaultNavigation( self.uiName , e=1 , defaultTraversal=value )
  def setdefaultWorkingNode( self , value ):
    cmds.defaultNavigation( self.uiName , e=1 , defaultWorkingNode=value )
  def setforce( self , value ):
    cmds.defaultNavigation( self.uiName , e=1 , force=value )
  def setignore( self , value ):
    cmds.defaultNavigation( self.uiName , e=1 , ignore=value )
  def setnavigatorDecisionString( self , value ):
    cmds.defaultNavigation( self.uiName , e=1 , navigatorDecisionString=value )
  def setquiet( self , value ):
    cmds.defaultNavigation( self.uiName , e=1 , quiet=value )
  def setrelatedNodes( self , value ):
    cmds.defaultNavigation( self.uiName , e=1 , relatedNodes=value )
  def setsource( self , value ):
    cmds.defaultNavigation( self.uiName , e=1 , source=value )
  def setunignore( self , value ):
    cmds.defaultNavigation( self.uiName , e=1 , unignore=value )

  ##### propertyCode #####
  connectToExisting = property( getconnectToExisting , setconnectToExisting )
  createNew = property( getcreateNew , setcreateNew )
  destination = property( getdestination , setdestination )
  delete = property( getdelete , setdelete )
  disconnect = property( getdisconnect , setdisconnect )
  defaultTraversal = property( getdefaultTraversal , setdefaultTraversal )
  defaultWorkingNode = property( getdefaultWorkingNode , setdefaultWorkingNode )
  force = property( getforce , setforce )
  ignore = property( getignore , setignore )
  navigatorDecisionString = property( getnavigatorDecisionString , setnavigatorDecisionString )
  quiet = property( getquiet , setquiet )
  relatedNodes = property( getrelatedNodes , setrelatedNodes )
  source = property( getsource , setsource )
  unignore = property( getunignore , setunignore )

  ##### customCode #####





class Editor( Window ):

  ##### initialize #####
  def __init__( self , control=None , filter=None , forceMainConnection=None , highlightConnection=None , lockMainConnection=None , mainListConnection=None , parent=None , panel=None , selectionConnection=None , stateString=None , unlockMainConnection=None , unParent=None , updateMainConnection=None , **args ):
    self.uiName = cmds.editor()

    ##### substitution #####
    if control != None:
      self.control = control
    if filter != None:
      self.filter = filter
    if forceMainConnection != None:
      self.forceMainConnection = forceMainConnection
    if highlightConnection != None:
      self.highlightConnection = highlightConnection
    if lockMainConnection != None:
      self.lockMainConnection = lockMainConnection
    if mainListConnection != None:
      self.mainListConnection = mainListConnection
    if parent != None:
      self.parent = parent
    if panel != None:
      self.panel = panel
    if selectionConnection != None:
      self.selectionConnection = selectionConnection
    if stateString != None:
      self.stateString = stateString
    if unlockMainConnection != None:
      self.unlockMainConnection = unlockMainConnection
    if unParent != None:
      self.unParent = unParent
    if updateMainConnection != None:
      self.updateMainConnection = updateMainConnection

  ##### getFuncCode #####
  def getcontrol( self ):
    return cmds.editor( self.uiName , q=1 , control=1 )
  def getfilter( self ):
    return cmds.editor( self.uiName , q=1 , filter=1 )
  def getforceMainConnection( self ):
    return cmds.editor( self.uiName , q=1 , forceMainConnection=1 )
  def gethighlightConnection( self ):
    return cmds.editor( self.uiName , q=1 , highlightConnection=1 )
  def getlockMainConnection( self ):
    return cmds.editor( self.uiName , q=1 , lockMainConnection=1 )
  def getmainListConnection( self ):
    return cmds.editor( self.uiName , q=1 , mainListConnection=1 )
  def getparent( self ):
    return cmds.editor( self.uiName , q=1 , parent=1 )
  def getpanel( self ):
    return cmds.editor( self.uiName , q=1 , panel=1 )
  def getselectionConnection( self ):
    return cmds.editor( self.uiName , q=1 , selectionConnection=1 )
  def getstateString( self ):
    return cmds.editor( self.uiName , q=1 , stateString=1 )
  def getunlockMainConnection( self ):
    return cmds.editor( self.uiName , q=1 , unlockMainConnection=1 )
  def getunParent( self ):
    return cmds.editor( self.uiName , q=1 , unParent=1 )
  def getupdateMainConnection( self ):
    return cmds.editor( self.uiName , q=1 , updateMainConnection=1 )

  ##### setFuncCode #####
  def setcontrol( self , value ):
    cmds.editor( self.uiName , e=1 , control=value )
  def setfilter( self , value ):
    cmds.editor( self.uiName , e=1 , filter=value )
  def setforceMainConnection( self , value ):
    cmds.editor( self.uiName , e=1 , forceMainConnection=value )
  def sethighlightConnection( self , value ):
    cmds.editor( self.uiName , e=1 , highlightConnection=value )
  def setlockMainConnection( self , value ):
    cmds.editor( self.uiName , e=1 , lockMainConnection=value )
  def setmainListConnection( self , value ):
    cmds.editor( self.uiName , e=1 , mainListConnection=value )
  def setparent( self , value ):
    cmds.editor( self.uiName , e=1 , parent=value )
  def setpanel( self , value ):
    cmds.editor( self.uiName , e=1 , panel=value )
  def setselectionConnection( self , value ):
    cmds.editor( self.uiName , e=1 , selectionConnection=value )
  def setstateString( self , value ):
    cmds.editor( self.uiName , e=1 , stateString=value )
  def setunlockMainConnection( self , value ):
    cmds.editor( self.uiName , e=1 , unlockMainConnection=value )
  def setunParent( self , value ):
    cmds.editor( self.uiName , e=1 , unParent=value )
  def setupdateMainConnection( self , value ):
    cmds.editor( self.uiName , e=1 , updateMainConnection=value )

  ##### propertyCode #####
  control = property( getcontrol , setcontrol )
  filter = property( getfilter , setfilter )
  forceMainConnection = property( getforceMainConnection , setforceMainConnection )
  highlightConnection = property( gethighlightConnection , sethighlightConnection )
  lockMainConnection = property( getlockMainConnection , setlockMainConnection )
  mainListConnection = property( getmainListConnection , setmainListConnection )
  parent = property( getparent , setparent )
  panel = property( getpanel , setpanel )
  selectionConnection = property( getselectionConnection , setselectionConnection )
  stateString = property( getstateString , setstateString )
  unlockMainConnection = property( getunlockMainConnection , setunlockMainConnection )
  unParent = property( getunParent , setunParent )
  updateMainConnection = property( getupdateMainConnection , setupdateMainConnection )

  ##### customCode #####





class EditorTemplate( Window ):

  ##### initialize #####
  def __init__( self , addControl=None , addComponents=None , addDynamicControl=None , addExtraControls=None , annotation=None , addSeparator=None , beginLayout=None , beginNoOptimize=None , beginScrollLayout=None , callCustom=None , collapse=None , debugMode=None , dimControl=None , extraControlsLabel=None , endLayout=None , endNoOptimize=None , endScrollLayout=None , interruptOptimize=None , label=None , listExtraAttributes=None , preventOverride=None , queryControl=None , queryLabel=None , suppress=None , **args ):
    self.uiName = cmds.editorTemplate()

    ##### substitution #####
    if addControl != None:
      self.addControl = addControl
    if addComponents != None:
      self.addComponents = addComponents
    if addDynamicControl != None:
      self.addDynamicControl = addDynamicControl
    if addExtraControls != None:
      self.addExtraControls = addExtraControls
    if annotation != None:
      self.annotation = annotation
    if addSeparator != None:
      self.addSeparator = addSeparator
    if beginLayout != None:
      self.beginLayout = beginLayout
    if beginNoOptimize != None:
      self.beginNoOptimize = beginNoOptimize
    if beginScrollLayout != None:
      self.beginScrollLayout = beginScrollLayout
    if callCustom != None:
      self.callCustom = callCustom
    if collapse != None:
      self.collapse = collapse
    if debugMode != None:
      self.debugMode = debugMode
    if dimControl != None:
      self.dimControl = dimControl
    if extraControlsLabel != None:
      self.extraControlsLabel = extraControlsLabel
    if endLayout != None:
      self.endLayout = endLayout
    if endNoOptimize != None:
      self.endNoOptimize = endNoOptimize
    if endScrollLayout != None:
      self.endScrollLayout = endScrollLayout
    if interruptOptimize != None:
      self.interruptOptimize = interruptOptimize
    if label != None:
      self.label = label
    if listExtraAttributes != None:
      self.listExtraAttributes = listExtraAttributes
    if preventOverride != None:
      self.preventOverride = preventOverride
    if queryControl != None:
      self.queryControl = queryControl
    if queryLabel != None:
      self.queryLabel = queryLabel
    if suppress != None:
      self.suppress = suppress

  ##### getFuncCode #####
  def getaddControl( self ):
    return cmds.editorTemplate( self.uiName , q=1 , addControl=1 )
  def getaddComponents( self ):
    return cmds.editorTemplate( self.uiName , q=1 , addComponents=1 )
  def getaddDynamicControl( self ):
    return cmds.editorTemplate( self.uiName , q=1 , addDynamicControl=1 )
  def getaddExtraControls( self ):
    return cmds.editorTemplate( self.uiName , q=1 , addExtraControls=1 )
  def getannotation( self ):
    return cmds.editorTemplate( self.uiName , q=1 , annotation=1 )
  def getaddSeparator( self ):
    return cmds.editorTemplate( self.uiName , q=1 , addSeparator=1 )
  def getbeginLayout( self ):
    return cmds.editorTemplate( self.uiName , q=1 , beginLayout=1 )
  def getbeginNoOptimize( self ):
    return cmds.editorTemplate( self.uiName , q=1 , beginNoOptimize=1 )
  def getbeginScrollLayout( self ):
    return cmds.editorTemplate( self.uiName , q=1 , beginScrollLayout=1 )
  def getcallCustom( self ):
    return cmds.editorTemplate( self.uiName , q=1 , callCustom=1 )
  def getcollapse( self ):
    return cmds.editorTemplate( self.uiName , q=1 , collapse=1 )
  def getdebugMode( self ):
    return cmds.editorTemplate( self.uiName , q=1 , debugMode=1 )
  def getdimControl( self ):
    return cmds.editorTemplate( self.uiName , q=1 , dimControl=1 )
  def getextraControlsLabel( self ):
    return cmds.editorTemplate( self.uiName , q=1 , extraControlsLabel=1 )
  def getendLayout( self ):
    return cmds.editorTemplate( self.uiName , q=1 , endLayout=1 )
  def getendNoOptimize( self ):
    return cmds.editorTemplate( self.uiName , q=1 , endNoOptimize=1 )
  def getendScrollLayout( self ):
    return cmds.editorTemplate( self.uiName , q=1 , endScrollLayout=1 )
  def getinterruptOptimize( self ):
    return cmds.editorTemplate( self.uiName , q=1 , interruptOptimize=1 )
  def getlabel( self ):
    return cmds.editorTemplate( self.uiName , q=1 , label=1 )
  def getlistExtraAttributes( self ):
    return cmds.editorTemplate( self.uiName , q=1 , listExtraAttributes=1 )
  def getpreventOverride( self ):
    return cmds.editorTemplate( self.uiName , q=1 , preventOverride=1 )
  def getqueryControl( self ):
    return cmds.editorTemplate( self.uiName , q=1 , queryControl=1 )
  def getqueryLabel( self ):
    return cmds.editorTemplate( self.uiName , q=1 , queryLabel=1 )
  def getsuppress( self ):
    return cmds.editorTemplate( self.uiName , q=1 , suppress=1 )

  ##### setFuncCode #####
  def setaddControl( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , addControl=value )
  def setaddComponents( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , addComponents=value )
  def setaddDynamicControl( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , addDynamicControl=value )
  def setaddExtraControls( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , addExtraControls=value )
  def setannotation( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , annotation=value )
  def setaddSeparator( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , addSeparator=value )
  def setbeginLayout( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , beginLayout=value )
  def setbeginNoOptimize( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , beginNoOptimize=value )
  def setbeginScrollLayout( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , beginScrollLayout=value )
  def setcallCustom( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , callCustom=value )
  def setcollapse( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , collapse=value )
  def setdebugMode( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , debugMode=value )
  def setdimControl( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , dimControl=value )
  def setextraControlsLabel( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , extraControlsLabel=value )
  def setendLayout( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , endLayout=value )
  def setendNoOptimize( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , endNoOptimize=value )
  def setendScrollLayout( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , endScrollLayout=value )
  def setinterruptOptimize( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , interruptOptimize=value )
  def setlabel( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , label=value )
  def setlistExtraAttributes( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , listExtraAttributes=value )
  def setpreventOverride( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , preventOverride=value )
  def setqueryControl( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , queryControl=value )
  def setqueryLabel( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , queryLabel=value )
  def setsuppress( self , value ):
    cmds.editorTemplate( self.uiName , e=1 , suppress=value )

  ##### propertyCode #####
  addControl = property( getaddControl , setaddControl )
  addComponents = property( getaddComponents , setaddComponents )
  addDynamicControl = property( getaddDynamicControl , setaddDynamicControl )
  addExtraControls = property( getaddExtraControls , setaddExtraControls )
  annotation = property( getannotation , setannotation )
  addSeparator = property( getaddSeparator , setaddSeparator )
  beginLayout = property( getbeginLayout , setbeginLayout )
  beginNoOptimize = property( getbeginNoOptimize , setbeginNoOptimize )
  beginScrollLayout = property( getbeginScrollLayout , setbeginScrollLayout )
  callCustom = property( getcallCustom , setcallCustom )
  collapse = property( getcollapse , setcollapse )
  debugMode = property( getdebugMode , setdebugMode )
  dimControl = property( getdimControl , setdimControl )
  extraControlsLabel = property( getextraControlsLabel , setextraControlsLabel )
  endLayout = property( getendLayout , setendLayout )
  endNoOptimize = property( getendNoOptimize , setendNoOptimize )
  endScrollLayout = property( getendScrollLayout , setendScrollLayout )
  interruptOptimize = property( getinterruptOptimize , setinterruptOptimize )
  label = property( getlabel , setlabel )
  listExtraAttributes = property( getlistExtraAttributes , setlistExtraAttributes )
  preventOverride = property( getpreventOverride , setpreventOverride )
  queryControl = property( getqueryControl , setqueryControl )
  queryLabel = property( getqueryLabel , setqueryLabel )
  suppress = property( getsuppress , setsuppress )

  ##### customCode #####





class FontDialog( Window ):

  ##### initialize #####
  def __init__( self , FontList=None , **args ):
    self.uiName = cmds.fontDialog()

    ##### substitution #####
    if FontList != None:
      self.FontList = FontList

  ##### getFuncCode #####
  def getFontList( self ):
    return cmds.fontDialog( self.uiName , q=1 , FontList=1 )

  ##### setFuncCode #####
  def setFontList( self , value ):
    cmds.fontDialog( self.uiName , e=1 , FontList=value )

  ##### propertyCode #####
  FontList = property( getFontList , setFontList )

  ##### customCode #####





class LayoutDialog( Window ):

  ##### initialize #####
  def __init__( self , dismiss=None , parent=None , uiScript=None , **args ):
    self.uiName = cmds.layoutDialog()

    ##### substitution #####
    if dismiss != None:
      self.dismiss = dismiss
    if parent != None:
      self.parent = parent
    if uiScript != None:
      self.uiScript = uiScript

  ##### getFuncCode #####
  def getdismiss( self ):
    return cmds.layoutDialog( self.uiName , q=1 , dismiss=1 )
  def getparent( self ):
    return cmds.layoutDialog( self.uiName , q=1 , parent=1 )
  def getuiScript( self ):
    return cmds.layoutDialog( self.uiName , q=1 , uiScript=1 )

  ##### setFuncCode #####
  def setdismiss( self , value ):
    cmds.layoutDialog( self.uiName , e=1 , dismiss=value )
  def setparent( self , value ):
    cmds.layoutDialog( self.uiName , e=1 , parent=value )
  def setuiScript( self , value ):
    cmds.layoutDialog( self.uiName , e=1 , uiScript=value )

  ##### propertyCode #####
  dismiss = property( getdismiss , setdismiss )
  parent = property( getparent , setparent )
  uiScript = property( getuiScript , setuiScript )

  ##### customCode #####





class MinimizeApp( Window ):

  ##### initialize #####
  def __init__( self , **args ):
    self.uiName = cmds.minimizeApp()

    ##### substitution #####

  ##### getFuncCode #####

  ##### setFuncCode #####

  ##### propertyCode #####

  ##### customCode #####





class ProgressWindow( Window ):

  ##### initialize #####
  def __init__( self , endProgress=None , isCancelled=None , isInterruptable=None , maxValue=None , minValue=None , progress=None , step=None , status=None , **args ):
    self.uiName = cmds.progressWindow()

    ##### substitution #####
    if endProgress != None:
      self.endProgress = endProgress
    if isCancelled != None:
      self.isCancelled = isCancelled
    if isInterruptable != None:
      self.isInterruptable = isInterruptable
    if maxValue != None:
      self.maxValue = maxValue
    if minValue != None:
      self.minValue = minValue
    if progress != None:
      self.progress = progress
    if step != None:
      self.step = step
    if status != None:
      self.status = status

  ##### getFuncCode #####
  def getendProgress( self ):
    return cmds.progressWindow( self.uiName , q=1 , endProgress=1 )
  def getisCancelled( self ):
    return cmds.progressWindow( self.uiName , q=1 , isCancelled=1 )
  def getisInterruptable( self ):
    return cmds.progressWindow( self.uiName , q=1 , isInterruptable=1 )
  def getmaxValue( self ):
    return cmds.progressWindow( self.uiName , q=1 , maxValue=1 )
  def getminValue( self ):
    return cmds.progressWindow( self.uiName , q=1 , minValue=1 )
  def getprogress( self ):
    return cmds.progressWindow( self.uiName , q=1 , progress=1 )
  def getstep( self ):
    return cmds.progressWindow( self.uiName , q=1 , step=1 )
  def getstatus( self ):
    return cmds.progressWindow( self.uiName , q=1 , status=1 )

  ##### setFuncCode #####
  def setendProgress( self , value ):
    cmds.progressWindow( self.uiName , e=1 , endProgress=value )
  def setisCancelled( self , value ):
    cmds.progressWindow( self.uiName , e=1 , isCancelled=value )
  def setisInterruptable( self , value ):
    cmds.progressWindow( self.uiName , e=1 , isInterruptable=value )
  def setmaxValue( self , value ):
    cmds.progressWindow( self.uiName , e=1 , maxValue=value )
  def setminValue( self , value ):
    cmds.progressWindow( self.uiName , e=1 , minValue=value )
  def setprogress( self , value ):
    cmds.progressWindow( self.uiName , e=1 , progress=value )
  def setstep( self , value ):
    cmds.progressWindow( self.uiName , e=1 , step=value )
  def setstatus( self , value ):
    cmds.progressWindow( self.uiName , e=1 , status=value )

  ##### propertyCode #####
  endProgress = property( getendProgress , setendProgress )
  isCancelled = property( getisCancelled , setisCancelled )
  isInterruptable = property( getisInterruptable , setisInterruptable )
  maxValue = property( getmaxValue , setmaxValue )
  minValue = property( getminValue , setminValue )
  progress = property( getprogress , setprogress )
  step = property( getstep , setstep )
  status = property( getstatus , setstatus )

  ##### customCode #####





class PromptDialog( Window ):

  ##### initialize #####
  def __init__( self , button=None , cancelButton=None , defaultButton=None , dismissString=None , message=None , messageAlign=None , parent=None , scrollableField=None , style=None , text=None , **args ):
    self.uiName = cmds.promptDialog()

    ##### substitution #####
    if button != None:
      self.button = button
    if cancelButton != None:
      self.cancelButton = cancelButton
    if defaultButton != None:
      self.defaultButton = defaultButton
    if dismissString != None:
      self.dismissString = dismissString
    if message != None:
      self.message = message
    if messageAlign != None:
      self.messageAlign = messageAlign
    if parent != None:
      self.parent = parent
    if scrollableField != None:
      self.scrollableField = scrollableField
    if style != None:
      self.style = style
    if text != None:
      self.text = text

  ##### getFuncCode #####
  def getbutton( self ):
    return cmds.promptDialog( self.uiName , q=1 , button=1 )
  def getcancelButton( self ):
    return cmds.promptDialog( self.uiName , q=1 , cancelButton=1 )
  def getdefaultButton( self ):
    return cmds.promptDialog( self.uiName , q=1 , defaultButton=1 )
  def getdismissString( self ):
    return cmds.promptDialog( self.uiName , q=1 , dismissString=1 )
  def getmessage( self ):
    return cmds.promptDialog( self.uiName , q=1 , message=1 )
  def getmessageAlign( self ):
    return cmds.promptDialog( self.uiName , q=1 , messageAlign=1 )
  def getparent( self ):
    return cmds.promptDialog( self.uiName , q=1 , parent=1 )
  def getscrollableField( self ):
    return cmds.promptDialog( self.uiName , q=1 , scrollableField=1 )
  def getstyle( self ):
    return cmds.promptDialog( self.uiName , q=1 , style=1 )
  def gettext( self ):
    return cmds.promptDialog( self.uiName , q=1 , text=1 )

  ##### setFuncCode #####
  def setbutton( self , value ):
    cmds.promptDialog( self.uiName , e=1 , button=value )
  def setcancelButton( self , value ):
    cmds.promptDialog( self.uiName , e=1 , cancelButton=value )
  def setdefaultButton( self , value ):
    cmds.promptDialog( self.uiName , e=1 , defaultButton=value )
  def setdismissString( self , value ):
    cmds.promptDialog( self.uiName , e=1 , dismissString=value )
  def setmessage( self , value ):
    cmds.promptDialog( self.uiName , e=1 , message=value )
  def setmessageAlign( self , value ):
    cmds.promptDialog( self.uiName , e=1 , messageAlign=value )
  def setparent( self , value ):
    cmds.promptDialog( self.uiName , e=1 , parent=value )
  def setscrollableField( self , value ):
    cmds.promptDialog( self.uiName , e=1 , scrollableField=value )
  def setstyle( self , value ):
    cmds.promptDialog( self.uiName , e=1 , style=value )
  def settext( self , value ):
    cmds.promptDialog( self.uiName , e=1 , text=value )

  ##### propertyCode #####
  button = property( getbutton , setbutton )
  cancelButton = property( getcancelButton , setcancelButton )
  defaultButton = property( getdefaultButton , setdefaultButton )
  dismissString = property( getdismissString , setdismissString )
  message = property( getmessage , setmessage )
  messageAlign = property( getmessageAlign , setmessageAlign )
  parent = property( getparent , setparent )
  scrollableField = property( getscrollableField , setscrollableField )
  style = property( getstyle , setstyle )
  text = property( gettext , settext )

  ##### customCode #####





class ScriptEditorInfo( Window ):

  ##### initialize #####
  def __init__( self , clearHistory=None , clearHistoryFile=None , historyFilename=None , input=None , suppressErrors=None , suppressInfo=None , suppressResults=None , suppressStackWindow=None , suppressWarnings=None , writeHistory=None , **args ):
    self.uiName = cmds.scriptEditorInfo()

    ##### substitution #####
    if clearHistory != None:
      self.clearHistory = clearHistory
    if clearHistoryFile != None:
      self.clearHistoryFile = clearHistoryFile
    if historyFilename != None:
      self.historyFilename = historyFilename
    if input != None:
      self.input = input
    if suppressErrors != None:
      self.suppressErrors = suppressErrors
    if suppressInfo != None:
      self.suppressInfo = suppressInfo
    if suppressResults != None:
      self.suppressResults = suppressResults
    if suppressStackWindow != None:
      self.suppressStackWindow = suppressStackWindow
    if suppressWarnings != None:
      self.suppressWarnings = suppressWarnings
    if writeHistory != None:
      self.writeHistory = writeHistory

  ##### getFuncCode #####
  def getclearHistory( self ):
    return cmds.scriptEditorInfo( self.uiName , q=1 , clearHistory=1 )
  def getclearHistoryFile( self ):
    return cmds.scriptEditorInfo( self.uiName , q=1 , clearHistoryFile=1 )
  def gethistoryFilename( self ):
    return cmds.scriptEditorInfo( self.uiName , q=1 , historyFilename=1 )
  def getinput( self ):
    return cmds.scriptEditorInfo( self.uiName , q=1 , input=1 )
  def getsuppressErrors( self ):
    return cmds.scriptEditorInfo( self.uiName , q=1 , suppressErrors=1 )
  def getsuppressInfo( self ):
    return cmds.scriptEditorInfo( self.uiName , q=1 , suppressInfo=1 )
  def getsuppressResults( self ):
    return cmds.scriptEditorInfo( self.uiName , q=1 , suppressResults=1 )
  def getsuppressStackWindow( self ):
    return cmds.scriptEditorInfo( self.uiName , q=1 , suppressStackWindow=1 )
  def getsuppressWarnings( self ):
    return cmds.scriptEditorInfo( self.uiName , q=1 , suppressWarnings=1 )
  def getwriteHistory( self ):
    return cmds.scriptEditorInfo( self.uiName , q=1 , writeHistory=1 )

  ##### setFuncCode #####
  def setclearHistory( self , value ):
    cmds.scriptEditorInfo( self.uiName , e=1 , clearHistory=value )
  def setclearHistoryFile( self , value ):
    cmds.scriptEditorInfo( self.uiName , e=1 , clearHistoryFile=value )
  def sethistoryFilename( self , value ):
    cmds.scriptEditorInfo( self.uiName , e=1 , historyFilename=value )
  def setinput( self , value ):
    cmds.scriptEditorInfo( self.uiName , e=1 , input=value )
  def setsuppressErrors( self , value ):
    cmds.scriptEditorInfo( self.uiName , e=1 , suppressErrors=value )
  def setsuppressInfo( self , value ):
    cmds.scriptEditorInfo( self.uiName , e=1 , suppressInfo=value )
  def setsuppressResults( self , value ):
    cmds.scriptEditorInfo( self.uiName , e=1 , suppressResults=value )
  def setsuppressStackWindow( self , value ):
    cmds.scriptEditorInfo( self.uiName , e=1 , suppressStackWindow=value )
  def setsuppressWarnings( self , value ):
    cmds.scriptEditorInfo( self.uiName , e=1 , suppressWarnings=value )
  def setwriteHistory( self , value ):
    cmds.scriptEditorInfo( self.uiName , e=1 , writeHistory=value )

  ##### propertyCode #####
  clearHistory = property( getclearHistory , setclearHistory )
  clearHistoryFile = property( getclearHistoryFile , setclearHistoryFile )
  historyFilename = property( gethistoryFilename , sethistoryFilename )
  input = property( getinput , setinput )
  suppressErrors = property( getsuppressErrors , setsuppressErrors )
  suppressInfo = property( getsuppressInfo , setsuppressInfo )
  suppressResults = property( getsuppressResults , setsuppressResults )
  suppressStackWindow = property( getsuppressStackWindow , setsuppressStackWindow )
  suppressWarnings = property( getsuppressWarnings , setsuppressWarnings )
  writeHistory = property( getwriteHistory , setwriteHistory )

  ##### customCode #####





class ShowSelectionInTitle( Window ):

  ##### initialize #####
  def __init__( self , **args ):
    self.uiName = cmds.showSelectionInTitle()

    ##### substitution #####

  ##### getFuncCode #####

  ##### setFuncCode #####

  ##### propertyCode #####

  ##### customCode #####





class ShowWindow( Window ):

  ##### initialize #####
  def __init__( self , **args ):
    self.uiName = cmds.showWindow()

    ##### substitution #####

  ##### getFuncCode #####

  ##### setFuncCode #####

  ##### propertyCode #####

  ##### customCode #####





class ToggleWindowVisibility( Window ):

  ##### initialize #####
  def __init__( self , **args ):
    self.uiName = cmds.toggleWindowVisibility()

    ##### substitution #####

  ##### getFuncCode #####

  ##### setFuncCode #####

  ##### propertyCode #####

  ##### customCode #####





class WindowPref( Window ):

  ##### initialize #####
  def __init__( self , enableAll=None , loadAll=None , parentMain=None , remove=None , removeAll=None , saveAll=None , **args ):
    self.uiName = cmds.windowPref()

    ##### substitution #####
    if enableAll != None:
      self.enableAll = enableAll
    if loadAll != None:
      self.loadAll = loadAll
    if parentMain != None:
      self.parentMain = parentMain
    if remove != None:
      self.remove = remove
    if removeAll != None:
      self.removeAll = removeAll
    if saveAll != None:
      self.saveAll = saveAll

  ##### getFuncCode #####
  def getenableAll( self ):
    return cmds.windowPref( self.uiName , q=1 , enableAll=1 )
  def getloadAll( self ):
    return cmds.windowPref( self.uiName , q=1 , loadAll=1 )
  def getparentMain( self ):
    return cmds.windowPref( self.uiName , q=1 , parentMain=1 )
  def getremove( self ):
    return cmds.windowPref( self.uiName , q=1 , remove=1 )
  def getremoveAll( self ):
    return cmds.windowPref( self.uiName , q=1 , removeAll=1 )
  def getsaveAll( self ):
    return cmds.windowPref( self.uiName , q=1 , saveAll=1 )

  ##### setFuncCode #####
  def setenableAll( self , value ):
    cmds.windowPref( self.uiName , e=1 , enableAll=value )
  def setloadAll( self , value ):
    cmds.windowPref( self.uiName , e=1 , loadAll=value )
  def setparentMain( self , value ):
    cmds.windowPref( self.uiName , e=1 , parentMain=value )
  def setremove( self , value ):
    cmds.windowPref( self.uiName , e=1 , remove=value )
  def setremoveAll( self , value ):
    cmds.windowPref( self.uiName , e=1 , removeAll=value )
  def setsaveAll( self , value ):
    cmds.windowPref( self.uiName , e=1 , saveAll=value )

  ##### propertyCode #####
  enableAll = property( getenableAll , setenableAll )
  loadAll = property( getloadAll , setloadAll )
  parentMain = property( getparentMain , setparentMain )
  remove = property( getremove , setremove )
  removeAll = property( getremoveAll , setremoveAll )
  saveAll = property( getsaveAll , setsaveAll )

  ##### customCode #####





print "MODULE IMPORTED... MYAM_PyLib_mayaUI_window"