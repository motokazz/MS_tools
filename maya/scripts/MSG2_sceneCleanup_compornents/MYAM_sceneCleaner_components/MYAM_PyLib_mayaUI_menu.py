#-*- coding:UTF-8 -*-

#*******************************************************************************
'''

Tool Name     : MYAM_PyLib_mayaUI_menu
Description   : MayaのMenuグループに属するUI要素をオブジェクト指向ライクに扱うためのモジュール

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





###################
##### Usually #####
###################

class Menu( object ):

  ##### initialize #####
  def __init__( self , allowOptionBoxes=None , deleteAllItems=None , defineTemplate=None , docTag=None , enable=None , exists=None , familyImage=None , helpMenu=None , itemArray=None , label=None , mnemonic=None , numberOfItems=None , parent=None , postMenuCommand=None , postMenuCommandOnce=None , tearOff=None , useTemplate=None , visible=None , **args ):
    self.uiName = cmds.menu( tearOff=1 )

    ##### substitution #####
    if allowOptionBoxes != None:
      self.allowOptionBoxes = allowOptionBoxes
    if deleteAllItems != None:
      self.deleteAllItems = deleteAllItems
    if defineTemplate != None:
      self.defineTemplate = defineTemplate
    if docTag != None:
      self.docTag = docTag
    if enable != None:
      self.enable = enable
    if exists != None:
      self.exists = exists
    if familyImage != None:
      self.familyImage = familyImage
    if helpMenu != None:
      self.helpMenu = helpMenu
    if itemArray != None:
      self.itemArray = itemArray
    if label != None:
      self.label = label
    if mnemonic != None:
      self.mnemonic = mnemonic
    if numberOfItems != None:
      self.numberOfItems = numberOfItems
    if parent != None:
      self.parent = parent
    if postMenuCommand != None:
      self.postMenuCommand = postMenuCommand
    if postMenuCommandOnce != None:
      self.postMenuCommandOnce = postMenuCommandOnce
    if tearOff != None:
      self.tearOff = tearOff
    if useTemplate != None:
      self.useTemplate = useTemplate
    if visible != None:
      self.visible = visible

  ##### getFuncCode #####
  def getallowOptionBoxes( self ):
    return cmds.menu( self.uiName , q=1 , allowOptionBoxes=1 )
  def getdeleteAllItems( self ):
    return cmds.menu( self.uiName , q=1 , deleteAllItems=1 )
  def getdefineTemplate( self ):
    return cmds.menu( self.uiName , q=1 , defineTemplate=1 )
  def getdocTag( self ):
    return cmds.menu( self.uiName , q=1 , docTag=1 )
  def getenable( self ):
    return cmds.menu( self.uiName , q=1 , enable=1 )
  def getexists( self ):
    return cmds.menu( self.uiName , q=1 , exists=1 )
  def getfamilyImage( self ):
    return cmds.menu( self.uiName , q=1 , familyImage=1 )
  def gethelpMenu( self ):
    return cmds.menu( self.uiName , q=1 , helpMenu=1 )
  def getitemArray( self ):
    return cmds.menu( self.uiName , q=1 , itemArray=1 )
  def getlabel( self ):
    return cmds.menu( self.uiName , q=1 , label=1 )
  def getmnemonic( self ):
    return cmds.menu( self.uiName , q=1 , mnemonic=1 )
  def getnumberOfItems( self ):
    return cmds.menu( self.uiName , q=1 , numberOfItems=1 )
  def getparent( self ):
    return cmds.menu( self.uiName , q=1 , parent=1 )
  def getpostMenuCommand( self ):
    return cmds.menu( self.uiName , q=1 , postMenuCommand=1 )
  def getpostMenuCommandOnce( self ):
    return cmds.menu( self.uiName , q=1 , postMenuCommandOnce=1 )
  def gettearOff( self ):
    return cmds.menu( self.uiName , q=1 , tearOff=1 )
  def getuseTemplate( self ):
    return cmds.menu( self.uiName , q=1 , useTemplate=1 )
  def getvisible( self ):
    return cmds.menu( self.uiName , q=1 , visible=1 )

  ##### setFuncCode #####
  def setallowOptionBoxes( self , value ):
    cmds.menu( self.uiName , e=1 , allowOptionBoxes=value )
  def setdeleteAllItems( self , value ):
    cmds.menu( self.uiName , e=1 , deleteAllItems=value )
  def setdefineTemplate( self , value ):
    cmds.menu( self.uiName , e=1 , defineTemplate=value )
  def setdocTag( self , value ):
    cmds.menu( self.uiName , e=1 , docTag=value )
  def setenable( self , value ):
    cmds.menu( self.uiName , e=1 , enable=value )
  def setexists( self , value ):
    cmds.menu( self.uiName , e=1 , exists=value )
  def setfamilyImage( self , value ):
    cmds.menu( self.uiName , e=1 , familyImage=value )
  def sethelpMenu( self , value ):
    cmds.menu( self.uiName , e=1 , helpMenu=value )
  def setitemArray( self , value ):
    cmds.menu( self.uiName , e=1 , itemArray=value )
  def setlabel( self , value ):
    cmds.menu( self.uiName , e=1 , label=value )
  def setmnemonic( self , value ):
    cmds.menu( self.uiName , e=1 , mnemonic=value )
  def setnumberOfItems( self , value ):
    cmds.menu( self.uiName , e=1 , numberOfItems=value )
  def setparent( self , value ):
    cmds.menu( self.uiName , e=1 , parent=value )
  def setpostMenuCommand( self , value ):
    cmds.menu( self.uiName , e=1 , postMenuCommand=value )
  def setpostMenuCommandOnce( self , value ):
    cmds.menu( self.uiName , e=1 , postMenuCommandOnce=value )
  def settearOff( self , value ):
    cmds.menu( self.uiName , e=1 , tearOff=value )
  def setuseTemplate( self , value ):
    cmds.menu( self.uiName , e=1 , useTemplate=value )
  def setvisible( self , value ):
    cmds.menu( self.uiName , e=1 , visible=value )

  ##### propertyCode #####
  allowOptionBoxes = property( getallowOptionBoxes , setallowOptionBoxes )
  deleteAllItems = property( getdeleteAllItems , setdeleteAllItems )
  defineTemplate = property( getdefineTemplate , setdefineTemplate )
  docTag = property( getdocTag , setdocTag )
  enable = property( getenable , setenable )
  exists = property( getexists , setexists )
  familyImage = property( getfamilyImage , setfamilyImage )
  helpMenu = property( gethelpMenu , sethelpMenu )
  itemArray = property( getitemArray , setitemArray )
  label = property( getlabel , setlabel )
  mnemonic = property( getmnemonic , setmnemonic )
  numberOfItems = property( getnumberOfItems , setnumberOfItems )
  parent = property( getparent , setparent )
  postMenuCommand = property( getpostMenuCommand , setpostMenuCommand )
  postMenuCommandOnce = property( getpostMenuCommandOnce , setpostMenuCommandOnce )
  tearOff = property( gettearOff , settearOff )
  useTemplate = property( getuseTemplate , setuseTemplate )
  visible = property( getvisible , setvisible )

  ##### customCode #####





class MenuItem( object ):

  ##### initialize #####
  def __init__( self , altModifier=None , annotation=None , allowOptionBoxes=None , boldFont=None , command=None , checkBox=None , collection=None , commandModifier=None , ctrlModifier=None , divider=None , data=None , dragDoubleClickCommand=None , dragMenuCommand=None , defineTemplate=None , docTag=None , echoCommand=None , enableCommandRepeat=None , enable=None , exists=None , familyImage=None , image=None , insertAfter=None , isCheckBox=None , isOptionBox=None , imageOverlayLabel=None , isRadioButton=None , italicized=None , keyEquivalent=None , label=None , mnemonic=None , optionBox=None , optionModifier=None , parent=None , postMenuCommand=None , postMenuCommandOnce=None , radioButton=None , radialPosition=None , shiftModifier=None , subMenu=None , tearOff=None , useTemplate=None , **args ):
    self.uiName = cmds.menuItem()

    ##### substitution #####
    if altModifier != None:
      self.altModifier = altModifier
    if annotation != None:
      self.annotation = annotation
    if allowOptionBoxes != None:
      self.allowOptionBoxes = allowOptionBoxes
    if boldFont != None:
      self.boldFont = boldFont
    if command != None:
      self.command = command
    if checkBox != None:
      self.checkBox = checkBox
    if collection != None:
      self.collection = collection
    if commandModifier != None:
      self.commandModifier = commandModifier
    if ctrlModifier != None:
      self.ctrlModifier = ctrlModifier
    if divider != None:
      self.divider = divider
    if data != None:
      self.data = data
    if dragDoubleClickCommand != None:
      self.dragDoubleClickCommand = dragDoubleClickCommand
    if dragMenuCommand != None:
      self.dragMenuCommand = dragMenuCommand
    if defineTemplate != None:
      self.defineTemplate = defineTemplate
    if docTag != None:
      self.docTag = docTag
    if echoCommand != None:
      self.echoCommand = echoCommand
    if enableCommandRepeat != None:
      self.enableCommandRepeat = enableCommandRepeat
    if enable != None:
      self.enable = enable
    if exists != None:
      self.exists = exists
    if familyImage != None:
      self.familyImage = familyImage
    if image != None:
      self.image = image
    if insertAfter != None:
      self.insertAfter = insertAfter
    if isCheckBox != None:
      self.isCheckBox = isCheckBox
    if isOptionBox != None:
      self.isOptionBox = isOptionBox
    if imageOverlayLabel != None:
      self.imageOverlayLabel = imageOverlayLabel
    if isRadioButton != None:
      self.isRadioButton = isRadioButton
    if italicized != None:
      self.italicized = italicized
    if keyEquivalent != None:
      self.keyEquivalent = keyEquivalent
    if label != None:
      self.label = label
    if mnemonic != None:
      self.mnemonic = mnemonic
    if optionBox != None:
      self.optionBox = optionBox
    if optionModifier != None:
      self.optionModifier = optionModifier
    if parent != None:
      self.parent = parent
    if postMenuCommand != None:
      self.postMenuCommand = postMenuCommand
    if postMenuCommandOnce != None:
      self.postMenuCommandOnce = postMenuCommandOnce
    if radioButton != None:
      self.radioButton = radioButton
    if radialPosition != None:
      self.radialPosition = radialPosition
    if shiftModifier != None:
      self.shiftModifier = shiftModifier
    if subMenu != None:
      self.subMenu = subMenu
    if tearOff != None:
      self.tearOff = tearOff
    if useTemplate != None:
      self.useTemplate = useTemplate

  ##### getFuncCode #####
  def getaltModifier( self ):
    return cmds.menuItem( self.uiName , q=1 , altModifier=1 )
  def getannotation( self ):
    return cmds.menuItem( self.uiName , q=1 , annotation=1 )
  def getallowOptionBoxes( self ):
    return cmds.menuItem( self.uiName , q=1 , allowOptionBoxes=1 )
  def getboldFont( self ):
    return cmds.menuItem( self.uiName , q=1 , boldFont=1 )
  def getcommand( self ):
    return cmds.menuItem( self.uiName , q=1 , command=1 )
  def getcheckBox( self ):
    return cmds.menuItem( self.uiName , q=1 , checkBox=1 )
  def getcollection( self ):
    return cmds.menuItem( self.uiName , q=1 , collection=1 )
  def getcommandModifier( self ):
    return cmds.menuItem( self.uiName , q=1 , commandModifier=1 )
  def getctrlModifier( self ):
    return cmds.menuItem( self.uiName , q=1 , ctrlModifier=1 )
  def getdivider( self ):
    return cmds.menuItem( self.uiName , q=1 , divider=1 )
  def getdata( self ):
    return cmds.menuItem( self.uiName , q=1 , data=1 )
  def getdragDoubleClickCommand( self ):
    return cmds.menuItem( self.uiName , q=1 , dragDoubleClickCommand=1 )
  def getdragMenuCommand( self ):
    return cmds.menuItem( self.uiName , q=1 , dragMenuCommand=1 )
  def getdefineTemplate( self ):
    return cmds.menuItem( self.uiName , q=1 , defineTemplate=1 )
  def getdocTag( self ):
    return cmds.menuItem( self.uiName , q=1 , docTag=1 )
  def getechoCommand( self ):
    return cmds.menuItem( self.uiName , q=1 , echoCommand=1 )
  def getenableCommandRepeat( self ):
    return cmds.menuItem( self.uiName , q=1 , enableCommandRepeat=1 )
  def getenable( self ):
    return cmds.menuItem( self.uiName , q=1 , enable=1 )
  def getexists( self ):
    return cmds.menuItem( self.uiName , q=1 , exists=1 )
  def getfamilyImage( self ):
    return cmds.menuItem( self.uiName , q=1 , familyImage=1 )
  def getimage( self ):
    return cmds.menuItem( self.uiName , q=1 , image=1 )
  def getinsertAfter( self ):
    return cmds.menuItem( self.uiName , q=1 , insertAfter=1 )
  def getisCheckBox( self ):
    return cmds.menuItem( self.uiName , q=1 , isCheckBox=1 )
  def getisOptionBox( self ):
    return cmds.menuItem( self.uiName , q=1 , isOptionBox=1 )
  def getimageOverlayLabel( self ):
    return cmds.menuItem( self.uiName , q=1 , imageOverlayLabel=1 )
  def getisRadioButton( self ):
    return cmds.menuItem( self.uiName , q=1 , isRadioButton=1 )
  def getitalicized( self ):
    return cmds.menuItem( self.uiName , q=1 , italicized=1 )
  def getkeyEquivalent( self ):
    return cmds.menuItem( self.uiName , q=1 , keyEquivalent=1 )
  def getlabel( self ):
    return cmds.menuItem( self.uiName , q=1 , label=1 )
  def getmnemonic( self ):
    return cmds.menuItem( self.uiName , q=1 , mnemonic=1 )
  def getoptionBox( self ):
    return cmds.menuItem( self.uiName , q=1 , optionBox=1 )
  def getoptionModifier( self ):
    return cmds.menuItem( self.uiName , q=1 , optionModifier=1 )
  def getparent( self ):
    return cmds.menuItem( self.uiName , q=1 , parent=1 )
  def getpostMenuCommand( self ):
    return cmds.menuItem( self.uiName , q=1 , postMenuCommand=1 )
  def getpostMenuCommandOnce( self ):
    return cmds.menuItem( self.uiName , q=1 , postMenuCommandOnce=1 )
  def getradioButton( self ):
    return cmds.menuItem( self.uiName , q=1 , radioButton=1 )
  def getradialPosition( self ):
    return cmds.menuItem( self.uiName , q=1 , radialPosition=1 )
  def getshiftModifier( self ):
    return cmds.menuItem( self.uiName , q=1 , shiftModifier=1 )
  def getsubMenu( self ):
    return cmds.menuItem( self.uiName , q=1 , subMenu=1 )
  def gettearOff( self ):
    return cmds.menuItem( self.uiName , q=1 , tearOff=1 )
  def getuseTemplate( self ):
    return cmds.menuItem( self.uiName , q=1 , useTemplate=1 )

  ##### setFuncCode #####
  def setaltModifier( self , value ):
    cmds.menuItem( self.uiName , e=1 , altModifier=value )
  def setannotation( self , value ):
    cmds.menuItem( self.uiName , e=1 , annotation=value )
  def setallowOptionBoxes( self , value ):
    cmds.menuItem( self.uiName , e=1 , allowOptionBoxes=value )
  def setboldFont( self , value ):
    cmds.menuItem( self.uiName , e=1 , boldFont=value )
  def setcommand( self , value ):
    cmds.menuItem( self.uiName , e=1 , command=value )
  def setcheckBox( self , value ):
    cmds.menuItem( self.uiName , e=1 , checkBox=value )
  def setcollection( self , value ):
    cmds.menuItem( self.uiName , e=1 , collection=value )
  def setcommandModifier( self , value ):
    cmds.menuItem( self.uiName , e=1 , commandModifier=value )
  def setctrlModifier( self , value ):
    cmds.menuItem( self.uiName , e=1 , ctrlModifier=value )
  def setdivider( self , value ):
    cmds.menuItem( self.uiName , e=1 , divider=value )
  def setdata( self , value ):
    cmds.menuItem( self.uiName , e=1 , data=value )
  def setdragDoubleClickCommand( self , value ):
    cmds.menuItem( self.uiName , e=1 , dragDoubleClickCommand=value )
  def setdragMenuCommand( self , value ):
    cmds.menuItem( self.uiName , e=1 , dragMenuCommand=value )
  def setdefineTemplate( self , value ):
    cmds.menuItem( self.uiName , e=1 , defineTemplate=value )
  def setdocTag( self , value ):
    cmds.menuItem( self.uiName , e=1 , docTag=value )
  def setechoCommand( self , value ):
    cmds.menuItem( self.uiName , e=1 , echoCommand=value )
  def setenableCommandRepeat( self , value ):
    cmds.menuItem( self.uiName , e=1 , enableCommandRepeat=value )
  def setenable( self , value ):
    cmds.menuItem( self.uiName , e=1 , enable=value )
  def setexists( self , value ):
    cmds.menuItem( self.uiName , e=1 , exists=value )
  def setfamilyImage( self , value ):
    cmds.menuItem( self.uiName , e=1 , familyImage=value )
  def setimage( self , value ):
    cmds.menuItem( self.uiName , e=1 , image=value )
  def setinsertAfter( self , value ):
    cmds.menuItem( self.uiName , e=1 , insertAfter=value )
  def setisCheckBox( self , value ):
    cmds.menuItem( self.uiName , e=1 , isCheckBox=value )
  def setisOptionBox( self , value ):
    cmds.menuItem( self.uiName , e=1 , isOptionBox=value )
  def setimageOverlayLabel( self , value ):
    cmds.menuItem( self.uiName , e=1 , imageOverlayLabel=value )
  def setisRadioButton( self , value ):
    cmds.menuItem( self.uiName , e=1 , isRadioButton=value )
  def setitalicized( self , value ):
    cmds.menuItem( self.uiName , e=1 , italicized=value )
  def setkeyEquivalent( self , value ):
    cmds.menuItem( self.uiName , e=1 , keyEquivalent=value )
  def setlabel( self , value ):
    cmds.menuItem( self.uiName , e=1 , label=value )
  def setmnemonic( self , value ):
    cmds.menuItem( self.uiName , e=1 , mnemonic=value )
  def setoptionBox( self , value ):
    cmds.menuItem( self.uiName , e=1 , optionBox=value )
  def setoptionModifier( self , value ):
    cmds.menuItem( self.uiName , e=1 , optionModifier=value )
  def setparent( self , value ):
    cmds.menuItem( self.uiName , e=1 , parent=value )
  def setpostMenuCommand( self , value ):
    cmds.menuItem( self.uiName , e=1 , postMenuCommand=value )
  def setpostMenuCommandOnce( self , value ):
    cmds.menuItem( self.uiName , e=1 , postMenuCommandOnce=value )
  def setradioButton( self , value ):
    cmds.menuItem( self.uiName , e=1 , radioButton=value )
  def setradialPosition( self , value ):
    cmds.menuItem( self.uiName , e=1 , radialPosition=value )
  def setshiftModifier( self , value ):
    cmds.menuItem( self.uiName , e=1 , shiftModifier=value )
  def setsubMenu( self , value ):
    cmds.menuItem( self.uiName , e=1 , subMenu=value )
  def settearOff( self , value ):
    cmds.menuItem( self.uiName , e=1 , tearOff=value )
  def setuseTemplate( self , value ):
    cmds.menuItem( self.uiName , e=1 , useTemplate=value )

  ##### propertyCode #####
  altModifier = property( getaltModifier , setaltModifier )
  annotation = property( getannotation , setannotation )
  allowOptionBoxes = property( getallowOptionBoxes , setallowOptionBoxes )
  boldFont = property( getboldFont , setboldFont )
  command = property( getcommand , setcommand )
  checkBox = property( getcheckBox , setcheckBox )
  collection = property( getcollection , setcollection )
  commandModifier = property( getcommandModifier , setcommandModifier )
  ctrlModifier = property( getctrlModifier , setctrlModifier )
  divider = property( getdivider , setdivider )
  data = property( getdata , setdata )
  dragDoubleClickCommand = property( getdragDoubleClickCommand , setdragDoubleClickCommand )
  dragMenuCommand = property( getdragMenuCommand , setdragMenuCommand )
  defineTemplate = property( getdefineTemplate , setdefineTemplate )
  docTag = property( getdocTag , setdocTag )
  echoCommand = property( getechoCommand , setechoCommand )
  enableCommandRepeat = property( getenableCommandRepeat , setenableCommandRepeat )
  enable = property( getenable , setenable )
  exists = property( getexists , setexists )
  familyImage = property( getfamilyImage , setfamilyImage )
  image = property( getimage , setimage )
  insertAfter = property( getinsertAfter , setinsertAfter )
  isCheckBox = property( getisCheckBox , setisCheckBox )
  isOptionBox = property( getisOptionBox , setisOptionBox )
  imageOverlayLabel = property( getimageOverlayLabel , setimageOverlayLabel )
  isRadioButton = property( getisRadioButton , setisRadioButton )
  italicized = property( getitalicized , setitalicized )
  keyEquivalent = property( getkeyEquivalent , setkeyEquivalent )
  label = property( getlabel , setlabel )
  mnemonic = property( getmnemonic , setmnemonic )
  optionBox = property( getoptionBox , setoptionBox )
  optionModifier = property( getoptionModifier , setoptionModifier )
  parent = property( getparent , setparent )
  postMenuCommand = property( getpostMenuCommand , setpostMenuCommand )
  postMenuCommandOnce = property( getpostMenuCommandOnce , setpostMenuCommandOnce )
  radioButton = property( getradioButton , setradioButton )
  radialPosition = property( getradialPosition , setradialPosition )
  shiftModifier = property( getshiftModifier , setshiftModifier )
  subMenu = property( getsubMenu , setsubMenu )
  tearOff = property( gettearOff , settearOff )
  useTemplate = property( getuseTemplate , setuseTemplate )

  ##### customCode #####

class MenuItem_divider( MenuItem ):
  def __init__( self ):
    self.uiName = cmds.menuItem( divider=1 )

class MenuItem_checkBox( MenuItem ):
  def __init__( self ):
    self.uiName = cmds.menuItem( checkBox=1 )

class MenuItem_radioButton( MenuItem ):
  def __init__( self ):
    self.uiName = cmds.menuItem( radioButton=1 )

class MenuItem_optionBox( MenuItem ):
  def __init__( self ):
    self.uiName = cmds.menuItem( optionBox=1 )

class MenuItem_subMenu( MenuItem ):
  def __init__( self ):
    self.uiName = cmds.menuItem( subMenu=1 , tearOff=1 )





class RadioMenuItemCollection( object ):

  ##### initialize #####
  def __init__( self , defineTemplate=None , exists=None , gl=None , parent=None , useTemplate=None , **args ):
    self.uiName = cmds.radioMenuItemCollection()

    ##### substitution #####
    if defineTemplate != None:
      self.defineTemplate = defineTemplate
    if exists != None:
      self.exists = exists
    if gl != None:
      self.gl = gl
    if parent != None:
      self.parent = parent
    if useTemplate != None:
      self.useTemplate = useTemplate

  ##### getFuncCode #####
  def getdefineTemplate( self ):
    return cmds.radioMenuItemCollection( self.uiName , q=1 , defineTemplate=1 )
  def getexists( self ):
    return cmds.radioMenuItemCollection( self.uiName , q=1 , exists=1 )
  def getgl( self ):
    return cmds.radioMenuItemCollection( self.uiName , q=1 , gl=1 )
  def getparent( self ):
    return cmds.radioMenuItemCollection( self.uiName , q=1 , parent=1 )
  def getuseTemplate( self ):
    return cmds.radioMenuItemCollection( self.uiName , q=1 , useTemplate=1 )

  ##### setFuncCode #####
  def setdefineTemplate( self , value ):
    cmds.radioMenuItemCollection( self.uiName , e=1 , defineTemplate=value )
  def setexists( self , value ):
    cmds.radioMenuItemCollection( self.uiName , e=1 , exists=value )
  def setgl( self , value ):
    cmds.radioMenuItemCollection( self.uiName , e=1 , gl=value )
  def setparent( self , value ):
    cmds.radioMenuItemCollection( self.uiName , e=1 , parent=value )
  def setuseTemplate( self , value ):
    cmds.radioMenuItemCollection( self.uiName , e=1 , useTemplate=value )

  ##### propertyCode #####
  defineTemplate = property( getdefineTemplate , setdefineTemplate )
  exists = property( getexists , setexists )
  gl = property( getgl , setgl )
  parent = property( getparent , setparent )
  useTemplate = property( getuseTemplate , setuseTemplate )

  ##### customCode #####





class OptionMenu( object ):

  ##### initialize #####
  def __init__( self , alwaysCallChangeCommand=None , annotation=None , backgroundColor=None , changeCommand=None , dragCallback=None , dropCallback=None , defineTemplate=None , docTag=None , enable=None , exists=None , height=None , itemListLong=None , itemListShort=None , isObscured=None , label=None , manage=None , numberOfItems=None , numberOfPopupMenus=None , parent=None , popupMenuArray=None , preventOverride=None , select=None , useTemplate=None , value=None , visible=None , width=None , **args ):
    self.uiName = cmds.optionMenu()

    ##### substitution #####
    if alwaysCallChangeCommand != None:
      self.alwaysCallChangeCommand = alwaysCallChangeCommand
    if annotation != None:
      self.annotation = annotation
    if backgroundColor != None:
      self.backgroundColor = backgroundColor
    if changeCommand != None:
      self.changeCommand = changeCommand
    if dragCallback != None:
      self.dragCallback = dragCallback
    if dropCallback != None:
      self.dropCallback = dropCallback
    if defineTemplate != None:
      self.defineTemplate = defineTemplate
    if docTag != None:
      self.docTag = docTag
    if enable != None:
      self.enable = enable
    if exists != None:
      self.exists = exists
    if height != None:
      self.height = height
    if itemListLong != None:
      self.itemListLong = itemListLong
    if itemListShort != None:
      self.itemListShort = itemListShort
    if isObscured != None:
      self.isObscured = isObscured
    if label != None:
      self.label = label
    if manage != None:
      self.manage = manage
    if numberOfItems != None:
      self.numberOfItems = numberOfItems
    if numberOfPopupMenus != None:
      self.numberOfPopupMenus = numberOfPopupMenus
    if parent != None:
      self.parent = parent
    if popupMenuArray != None:
      self.popupMenuArray = popupMenuArray
    if preventOverride != None:
      self.preventOverride = preventOverride
    if select != None:
      self.select = select
    if useTemplate != None:
      self.useTemplate = useTemplate
    if value != None:
      self.value = value
    if visible != None:
      self.visible = visible
    if width != None:
      self.width = width

  ##### getFuncCode #####
  def getalwaysCallChangeCommand( self ):
    return cmds.optionMenu( self.uiName , q=1 , alwaysCallChangeCommand=1 )
  def getannotation( self ):
    return cmds.optionMenu( self.uiName , q=1 , annotation=1 )
  def getbackgroundColor( self ):
    return cmds.optionMenu( self.uiName , q=1 , backgroundColor=1 )
  def getchangeCommand( self ):
    return cmds.optionMenu( self.uiName , q=1 , changeCommand=1 )
  def getdragCallback( self ):
    return cmds.optionMenu( self.uiName , q=1 , dragCallback=1 )
  def getdropCallback( self ):
    return cmds.optionMenu( self.uiName , q=1 , dropCallback=1 )
  def getdefineTemplate( self ):
    return cmds.optionMenu( self.uiName , q=1 , defineTemplate=1 )
  def getdocTag( self ):
    return cmds.optionMenu( self.uiName , q=1 , docTag=1 )
  def getenable( self ):
    return cmds.optionMenu( self.uiName , q=1 , enable=1 )
  def getexists( self ):
    return cmds.optionMenu( self.uiName , q=1 , exists=1 )
  def getheight( self ):
    return cmds.optionMenu( self.uiName , q=1 , height=1 )
  def getitemListLong( self ):
    return cmds.optionMenu( self.uiName , q=1 , itemListLong=1 )
  def getitemListShort( self ):
    return cmds.optionMenu( self.uiName , q=1 , itemListShort=1 )
  def getisObscured( self ):
    return cmds.optionMenu( self.uiName , q=1 , isObscured=1 )
  def getlabel( self ):
    return cmds.optionMenu( self.uiName , q=1 , label=1 )
  def getmanage( self ):
    return cmds.optionMenu( self.uiName , q=1 , manage=1 )
  def getnumberOfItems( self ):
    return cmds.optionMenu( self.uiName , q=1 , numberOfItems=1 )
  def getnumberOfPopupMenus( self ):
    return cmds.optionMenu( self.uiName , q=1 , numberOfPopupMenus=1 )
  def getparent( self ):
    return cmds.optionMenu( self.uiName , q=1 , parent=1 )
  def getpopupMenuArray( self ):
    return cmds.optionMenu( self.uiName , q=1 , popupMenuArray=1 )
  def getpreventOverride( self ):
    return cmds.optionMenu( self.uiName , q=1 , preventOverride=1 )
  def getselect( self ):
    return cmds.optionMenu( self.uiName , q=1 , select=1 )
  def getuseTemplate( self ):
    return cmds.optionMenu( self.uiName , q=1 , useTemplate=1 )
  def getvalue( self ):
    return cmds.optionMenu( self.uiName , q=1 , value=1 )
  def getvisible( self ):
    return cmds.optionMenu( self.uiName , q=1 , visible=1 )
  def getwidth( self ):
    return cmds.optionMenu( self.uiName , q=1 , width=1 )

  ##### setFuncCode #####
  def setalwaysCallChangeCommand( self , value ):
    cmds.optionMenu( self.uiName , e=1 , alwaysCallChangeCommand=value )
  def setannotation( self , value ):
    cmds.optionMenu( self.uiName , e=1 , annotation=value )
  def setbackgroundColor( self , value ):
    cmds.optionMenu( self.uiName , e=1 , backgroundColor=value )
  def setchangeCommand( self , value ):
    cmds.optionMenu( self.uiName , e=1 , changeCommand=value )
  def setdragCallback( self , value ):
    cmds.optionMenu( self.uiName , e=1 , dragCallback=value )
  def setdropCallback( self , value ):
    cmds.optionMenu( self.uiName , e=1 , dropCallback=value )
  def setdefineTemplate( self , value ):
    cmds.optionMenu( self.uiName , e=1 , defineTemplate=value )
  def setdocTag( self , value ):
    cmds.optionMenu( self.uiName , e=1 , docTag=value )
  def setenable( self , value ):
    cmds.optionMenu( self.uiName , e=1 , enable=value )
  def setexists( self , value ):
    cmds.optionMenu( self.uiName , e=1 , exists=value )
  def setheight( self , value ):
    cmds.optionMenu( self.uiName , e=1 , height=value )
  def setitemListLong( self , value ):
    cmds.optionMenu( self.uiName , e=1 , itemListLong=value )
  def setitemListShort( self , value ):
    cmds.optionMenu( self.uiName , e=1 , itemListShort=value )
  def setisObscured( self , value ):
    cmds.optionMenu( self.uiName , e=1 , isObscured=value )
  def setlabel( self , value ):
    cmds.optionMenu( self.uiName , e=1 , label=value )
  def setmanage( self , value ):
    cmds.optionMenu( self.uiName , e=1 , manage=value )
  def setnumberOfItems( self , value ):
    cmds.optionMenu( self.uiName , e=1 , numberOfItems=value )
  def setnumberOfPopupMenus( self , value ):
    cmds.optionMenu( self.uiName , e=1 , numberOfPopupMenus=value )
  def setparent( self , value ):
    cmds.optionMenu( self.uiName , e=1 , parent=value )
  def setpopupMenuArray( self , value ):
    cmds.optionMenu( self.uiName , e=1 , popupMenuArray=value )
  def setpreventOverride( self , value ):
    cmds.optionMenu( self.uiName , e=1 , preventOverride=value )
  def setselect( self , value ):
    cmds.optionMenu( self.uiName , e=1 , select=value )
  def setuseTemplate( self , value ):
    cmds.optionMenu( self.uiName , e=1 , useTemplate=value )
  def setvalue( self , value ):
    cmds.optionMenu( self.uiName , e=1 , value=value )
  def setvisible( self , value ):
    cmds.optionMenu( self.uiName , e=1 , visible=value )
  def setwidth( self , value ):
    cmds.optionMenu( self.uiName , e=1 , width=value )

  ##### propertyCode #####
  alwaysCallChangeCommand = property( getalwaysCallChangeCommand , setalwaysCallChangeCommand )
  annotation = property( getannotation , setannotation )
  backgroundColor = property( getbackgroundColor , setbackgroundColor )
  changeCommand = property( getchangeCommand , setchangeCommand )
  dragCallback = property( getdragCallback , setdragCallback )
  dropCallback = property( getdropCallback , setdropCallback )
  defineTemplate = property( getdefineTemplate , setdefineTemplate )
  docTag = property( getdocTag , setdocTag )
  enable = property( getenable , setenable )
  exists = property( getexists , setexists )
  height = property( getheight , setheight )
  itemListLong = property( getitemListLong , setitemListLong )
  itemListShort = property( getitemListShort , setitemListShort )
  isObscured = property( getisObscured , setisObscured )
  label = property( getlabel , setlabel )
  manage = property( getmanage , setmanage )
  numberOfItems = property( getnumberOfItems , setnumberOfItems )
  numberOfPopupMenus = property( getnumberOfPopupMenus , setnumberOfPopupMenus )
  parent = property( getparent , setparent )
  popupMenuArray = property( getpopupMenuArray , setpopupMenuArray )
  preventOverride = property( getpreventOverride , setpreventOverride )
  select = property( getselect , setselect )
  useTemplate = property( getuseTemplate , setuseTemplate )
  value = property( getvalue , setvalue )
  visible = property( getvisible , setvisible )
  width = property( getwidth , setwidth )

  ##### customCode #####
  def set( self , setItems ):
    self.clear()
    if setItems != [] and setItems != None:
      for item in setItems:
        cmds.menuItem( parent=self.uiName , label=item )

  def add( self , addItems=[] ):
    for addItem in addItems:
      cmds.menuItem( parent=self.uiName , label=addItem )

  def replace( self , srcLabel , dstLabel ):
    existItems = cmds.optionMenu( self.uiName , q=1 , itemListLong=1 )
    if existItems != None:
      for existItem in existItems:
        menuLabel = cmds.menuItem( existItem , q=1 , label=1 )
        if menuLabel == srcLabel:
          cmds.menuItem( existItem , e=1 , label=dstLabel )

  def delete( self , deleteLabel ):
    existItems = cmds.optionMenu( self.uiName , q=1 , itemListLong=1 )
    if existItems != None:
      for existItem in existItems:
        menuLabel = cmds.menuItem( existItem , q=1 , label=1 )
        if menuLabel == deleteLabel:
          cmds.deleteUI( existItem , menuItem=1 )

  def clear( self ):
    existItems = cmds.optionMenu( self.uiName , q=1 , itemListLong=1 )

    if existItems != None:
      for existItem in existItems:
        cmds.deleteUI( existItem , menuItem=1 )

  def getAllLabels( self ):
    existItems = cmds.optionMenu( self.uiName , q=1 , itemListLong=1 )
    labelList = []

    for item in existItems:
      labelList.append( cmds.menuItem( item , q=1 , label=1 ) )

    return labelList





class PopupMenu( object ):

  ##### initialize #####
  def __init__( self , altModifier=None , allowOptionBoxes=None , button=None , ctrlModifier=None , deleteAllItems=None , defineTemplate=None , exists=None , itemArray=None , markingMenu=None , numberOfItems=None , parent=None , postMenuCommand=None , postMenuCommandOnce=None , shiftModifier=None , useTemplate=None , **args ):
    self.uiName = cmds.popupMenu()

    ##### substitution #####
    if altModifier != None:
      self.altModifier = altModifier
    if allowOptionBoxes != None:
      self.allowOptionBoxes = allowOptionBoxes
    if button != None:
      self.button = button
    if ctrlModifier != None:
      self.ctrlModifier = ctrlModifier
    if deleteAllItems != None:
      self.deleteAllItems = deleteAllItems
    if defineTemplate != None:
      self.defineTemplate = defineTemplate
    if exists != None:
      self.exists = exists
    if itemArray != None:
      self.itemArray = itemArray
    if markingMenu != None:
      self.markingMenu = markingMenu
    if numberOfItems != None:
      self.numberOfItems = numberOfItems
    if parent != None:
      self.parent = parent
    if postMenuCommand != None:
      self.postMenuCommand = postMenuCommand
    if postMenuCommandOnce != None:
      self.postMenuCommandOnce = postMenuCommandOnce
    if shiftModifier != None:
      self.shiftModifier = shiftModifier
    if useTemplate != None:
      self.useTemplate = useTemplate

  ##### getFuncCode #####
  def getaltModifier( self ):
    return cmds.popupMenu( self.uiName , q=1 , altModifier=1 )
  def getallowOptionBoxes( self ):
    return cmds.popupMenu( self.uiName , q=1 , allowOptionBoxes=1 )
  def getbutton( self ):
    return cmds.popupMenu( self.uiName , q=1 , button=1 )
  def getctrlModifier( self ):
    return cmds.popupMenu( self.uiName , q=1 , ctrlModifier=1 )
  def getdeleteAllItems( self ):
    return cmds.popupMenu( self.uiName , q=1 , deleteAllItems=1 )
  def getdefineTemplate( self ):
    return cmds.popupMenu( self.uiName , q=1 , defineTemplate=1 )
  def getexists( self ):
    return cmds.popupMenu( self.uiName , q=1 , exists=1 )
  def getitemArray( self ):
    return cmds.popupMenu( self.uiName , q=1 , itemArray=1 )
  def getmarkingMenu( self ):
    return cmds.popupMenu( self.uiName , q=1 , markingMenu=1 )
  def getnumberOfItems( self ):
    return cmds.popupMenu( self.uiName , q=1 , numberOfItems=1 )
  def getparent( self ):
    return cmds.popupMenu( self.uiName , q=1 , parent=1 )
  def getpostMenuCommand( self ):
    return cmds.popupMenu( self.uiName , q=1 , postMenuCommand=1 )
  def getpostMenuCommandOnce( self ):
    return cmds.popupMenu( self.uiName , q=1 , postMenuCommandOnce=1 )
  def getshiftModifier( self ):
    return cmds.popupMenu( self.uiName , q=1 , shiftModifier=1 )
  def getuseTemplate( self ):
    return cmds.popupMenu( self.uiName , q=1 , useTemplate=1 )

  ##### setFuncCode #####
  def setaltModifier( self , value ):
    cmds.popupMenu( self.uiName , e=1 , altModifier=value )
  def setallowOptionBoxes( self , value ):
    cmds.popupMenu( self.uiName , e=1 , allowOptionBoxes=value )
  def setbutton( self , value ):
    cmds.popupMenu( self.uiName , e=1 , button=value )
  def setctrlModifier( self , value ):
    cmds.popupMenu( self.uiName , e=1 , ctrlModifier=value )
  def setdeleteAllItems( self , value ):
    cmds.popupMenu( self.uiName , e=1 , deleteAllItems=value )
  def setdefineTemplate( self , value ):
    cmds.popupMenu( self.uiName , e=1 , defineTemplate=value )
  def setexists( self , value ):
    cmds.popupMenu( self.uiName , e=1 , exists=value )
  def setitemArray( self , value ):
    cmds.popupMenu( self.uiName , e=1 , itemArray=value )
  def setmarkingMenu( self , value ):
    cmds.popupMenu( self.uiName , e=1 , markingMenu=value )
  def setnumberOfItems( self , value ):
    cmds.popupMenu( self.uiName , e=1 , numberOfItems=value )
  def setparent( self , value ):
    cmds.popupMenu( self.uiName , e=1 , parent=value )
  def setpostMenuCommand( self , value ):
    cmds.popupMenu( self.uiName , e=1 , postMenuCommand=value )
  def setpostMenuCommandOnce( self , value ):
    cmds.popupMenu( self.uiName , e=1 , postMenuCommandOnce=value )
  def setshiftModifier( self , value ):
    cmds.popupMenu( self.uiName , e=1 , shiftModifier=value )
  def setuseTemplate( self , value ):
    cmds.popupMenu( self.uiName , e=1 , useTemplate=value )

  ##### propertyCode #####
  altModifier = property( getaltModifier , setaltModifier )
  allowOptionBoxes = property( getallowOptionBoxes , setallowOptionBoxes )
  button = property( getbutton , setbutton )
  ctrlModifier = property( getctrlModifier , setctrlModifier )
  deleteAllItems = property( getdeleteAllItems , setdeleteAllItems )
  defineTemplate = property( getdefineTemplate , setdefineTemplate )
  exists = property( getexists , setexists )
  itemArray = property( getitemArray , setitemArray )
  markingMenu = property( getmarkingMenu , setmarkingMenu )
  numberOfItems = property( getnumberOfItems , setnumberOfItems )
  parent = property( getparent , setparent )
  postMenuCommand = property( getpostMenuCommand , setpostMenuCommand )
  postMenuCommandOnce = property( getpostMenuCommandOnce , setpostMenuCommandOnce )
  shiftModifier = property( getshiftModifier , setshiftModifier )
  useTemplate = property( getuseTemplate , setuseTemplate )

  ##### customCode #####

  def set( self , setItems ):
    self.clear()
    if setItems != [] and setItems != None:
      for item in setItems:
        cmds.menuItem( parent=self.uiName , label=item )

  def add( self , addItems=[] ):
    for addItem in addItems:
      cmds.menuItem( parent=self.uiName , label=addItem )

  def replace( self , srcLabel , dstLabel ):
    existItems = cmds.optionMenu( self.uiName , q=1 , itemListLong=1 )
    if existItems != None:
      for existItem in existItems:
        menuLabel = cmds.menuItem( existItem , q=1 , label=1 )
        if menuLabel == srcLabel:
          cmds.menuItem( existItem , e=1 , label=dstLabel )

  def delete( self , deleteLabel ):
    existItems = cmds.optionMenu( self.uiName , q=1 , itemListLong=1 )
    if existItems != None:
      for existItem in existItems:
        menuLabel = cmds.menuItem( existItem , q=1 , label=1 )
        if menuLabel == deleteLabel:
          cmds.deleteUI( existItem , menuItem=1 )

  def clear( self ):
    existItems = cmds.optionMenu( self.uiName , q=1 , itemListLong=1 )

    if existItems != None:
      for existItem in existItems:
        cmds.deleteUI( existItem , menuItem=1 )

  def getAllLabels( self ):
    existItems = cmds.optionMenu( self.uiName , q=1 , itemListLong=1 )
    labelList = []

    for item in existItems:
      labelList.append( cmds.menuItem( item , q=1 , label=1 ) )

    return labelList









class MarkingMenu( PopupMenu ):
  def __init__( self ):
    self.uiName = cmds.popupMenu( markingMenu=1 )


























#######################
##### NOT USUALLY #####
#######################

class ArtBuildPaintMenu( object ):

  ##### initialize #####
  def __init__( self , **args ):
    self.uiName = cmds.artBuildPaintMenu()

    ##### substitution #####

  ##### getFuncCode #####

  ##### setFuncCode #####

  ##### propertyCode #####

  ##### customCode #####





class AttrEnumOptionMenu( object ):

  ##### initialize #####
  def __init__( self , annotation=None , attribute=None , backgroundColor=None , changeCommand=None , dragCallback=None , dropCallback=None , defineTemplate=None , docTag=None , enumeratedItem=None , enable=None , exists=None , height=None , isObscured=None , label=None , manage=None , numberOfPopupMenus=None , parent=None , popupMenuArray=None , preventOverride=None , useTemplate=None , visible=None , width=None , **args ):
    self.uiName = cmds.attrEnumOptionMenu()

    ##### substitution #####
    if annotation != None:
      self.annotation = annotation
    if attribute != None:
      self.attribute = attribute
    if backgroundColor != None:
      self.backgroundColor = backgroundColor
    if changeCommand != None:
      self.changeCommand = changeCommand
    if dragCallback != None:
      self.dragCallback = dragCallback
    if dropCallback != None:
      self.dropCallback = dropCallback
    if defineTemplate != None:
      self.defineTemplate = defineTemplate
    if docTag != None:
      self.docTag = docTag
    if enumeratedItem != None:
      self.enumeratedItem = enumeratedItem
    if enable != None:
      self.enable = enable
    if exists != None:
      self.exists = exists
    if height != None:
      self.height = height
    if isObscured != None:
      self.isObscured = isObscured
    if label != None:
      self.label = label
    if manage != None:
      self.manage = manage
    if numberOfPopupMenus != None:
      self.numberOfPopupMenus = numberOfPopupMenus
    if parent != None:
      self.parent = parent
    if popupMenuArray != None:
      self.popupMenuArray = popupMenuArray
    if preventOverride != None:
      self.preventOverride = preventOverride
    if useTemplate != None:
      self.useTemplate = useTemplate
    if visible != None:
      self.visible = visible
    if width != None:
      self.width = width

  ##### getFuncCode #####
  def getannotation( self ):
    return cmds.attrEnumOptionMenu( self.uiName , q=1 , annotation=1 )
  def getattribute( self ):
    return cmds.attrEnumOptionMenu( self.uiName , q=1 , attribute=1 )
  def getbackgroundColor( self ):
    return cmds.attrEnumOptionMenu( self.uiName , q=1 , backgroundColor=1 )
  def getchangeCommand( self ):
    return cmds.attrEnumOptionMenu( self.uiName , q=1 , changeCommand=1 )
  def getdragCallback( self ):
    return cmds.attrEnumOptionMenu( self.uiName , q=1 , dragCallback=1 )
  def getdropCallback( self ):
    return cmds.attrEnumOptionMenu( self.uiName , q=1 , dropCallback=1 )
  def getdefineTemplate( self ):
    return cmds.attrEnumOptionMenu( self.uiName , q=1 , defineTemplate=1 )
  def getdocTag( self ):
    return cmds.attrEnumOptionMenu( self.uiName , q=1 , docTag=1 )
  def getenumeratedItem( self ):
    return cmds.attrEnumOptionMenu( self.uiName , q=1 , enumeratedItem=1 )
  def getenable( self ):
    return cmds.attrEnumOptionMenu( self.uiName , q=1 , enable=1 )
  def getexists( self ):
    return cmds.attrEnumOptionMenu( self.uiName , q=1 , exists=1 )
  def getheight( self ):
    return cmds.attrEnumOptionMenu( self.uiName , q=1 , height=1 )
  def getisObscured( self ):
    return cmds.attrEnumOptionMenu( self.uiName , q=1 , isObscured=1 )
  def getlabel( self ):
    return cmds.attrEnumOptionMenu( self.uiName , q=1 , label=1 )
  def getmanage( self ):
    return cmds.attrEnumOptionMenu( self.uiName , q=1 , manage=1 )
  def getnumberOfPopupMenus( self ):
    return cmds.attrEnumOptionMenu( self.uiName , q=1 , numberOfPopupMenus=1 )
  def getparent( self ):
    return cmds.attrEnumOptionMenu( self.uiName , q=1 , parent=1 )
  def getpopupMenuArray( self ):
    return cmds.attrEnumOptionMenu( self.uiName , q=1 , popupMenuArray=1 )
  def getpreventOverride( self ):
    return cmds.attrEnumOptionMenu( self.uiName , q=1 , preventOverride=1 )
  def getuseTemplate( self ):
    return cmds.attrEnumOptionMenu( self.uiName , q=1 , useTemplate=1 )
  def getvisible( self ):
    return cmds.attrEnumOptionMenu( self.uiName , q=1 , visible=1 )
  def getwidth( self ):
    return cmds.attrEnumOptionMenu( self.uiName , q=1 , width=1 )

  ##### setFuncCode #####
  def setannotation( self , value ):
    cmds.attrEnumOptionMenu( self.uiName , e=1 , annotation=value )
  def setattribute( self , value ):
    cmds.attrEnumOptionMenu( self.uiName , e=1 , attribute=value )
  def setbackgroundColor( self , value ):
    cmds.attrEnumOptionMenu( self.uiName , e=1 , backgroundColor=value )
  def setchangeCommand( self , value ):
    cmds.attrEnumOptionMenu( self.uiName , e=1 , changeCommand=value )
  def setdragCallback( self , value ):
    cmds.attrEnumOptionMenu( self.uiName , e=1 , dragCallback=value )
  def setdropCallback( self , value ):
    cmds.attrEnumOptionMenu( self.uiName , e=1 , dropCallback=value )
  def setdefineTemplate( self , value ):
    cmds.attrEnumOptionMenu( self.uiName , e=1 , defineTemplate=value )
  def setdocTag( self , value ):
    cmds.attrEnumOptionMenu( self.uiName , e=1 , docTag=value )
  def setenumeratedItem( self , value ):
    cmds.attrEnumOptionMenu( self.uiName , e=1 , enumeratedItem=value )
  def setenable( self , value ):
    cmds.attrEnumOptionMenu( self.uiName , e=1 , enable=value )
  def setexists( self , value ):
    cmds.attrEnumOptionMenu( self.uiName , e=1 , exists=value )
  def setheight( self , value ):
    cmds.attrEnumOptionMenu( self.uiName , e=1 , height=value )
  def setisObscured( self , value ):
    cmds.attrEnumOptionMenu( self.uiName , e=1 , isObscured=value )
  def setlabel( self , value ):
    cmds.attrEnumOptionMenu( self.uiName , e=1 , label=value )
  def setmanage( self , value ):
    cmds.attrEnumOptionMenu( self.uiName , e=1 , manage=value )
  def setnumberOfPopupMenus( self , value ):
    cmds.attrEnumOptionMenu( self.uiName , e=1 , numberOfPopupMenus=value )
  def setparent( self , value ):
    cmds.attrEnumOptionMenu( self.uiName , e=1 , parent=value )
  def setpopupMenuArray( self , value ):
    cmds.attrEnumOptionMenu( self.uiName , e=1 , popupMenuArray=value )
  def setpreventOverride( self , value ):
    cmds.attrEnumOptionMenu( self.uiName , e=1 , preventOverride=value )
  def setuseTemplate( self , value ):
    cmds.attrEnumOptionMenu( self.uiName , e=1 , useTemplate=value )
  def setvisible( self , value ):
    cmds.attrEnumOptionMenu( self.uiName , e=1 , visible=value )
  def setwidth( self , value ):
    cmds.attrEnumOptionMenu( self.uiName , e=1 , width=value )

  ##### propertyCode #####
  annotation = property( getannotation , setannotation )
  attribute = property( getattribute , setattribute )
  backgroundColor = property( getbackgroundColor , setbackgroundColor )
  changeCommand = property( getchangeCommand , setchangeCommand )
  dragCallback = property( getdragCallback , setdragCallback )
  dropCallback = property( getdropCallback , setdropCallback )
  defineTemplate = property( getdefineTemplate , setdefineTemplate )
  docTag = property( getdocTag , setdocTag )
  enumeratedItem = property( getenumeratedItem , setenumeratedItem )
  enable = property( getenable , setenable )
  exists = property( getexists , setexists )
  height = property( getheight , setheight )
  isObscured = property( getisObscured , setisObscured )
  label = property( getlabel , setlabel )
  manage = property( getmanage , setmanage )
  numberOfPopupMenus = property( getnumberOfPopupMenus , setnumberOfPopupMenus )
  parent = property( getparent , setparent )
  popupMenuArray = property( getpopupMenuArray , setpopupMenuArray )
  preventOverride = property( getpreventOverride , setpreventOverride )
  useTemplate = property( getuseTemplate , setuseTemplate )
  visible = property( getvisible , setvisible )
  width = property( getwidth , setwidth )

  ##### customCode #####





class AttrEnumOptionMenuGrp( object ):

  ##### initialize #####
  def __init__( self , adjustableColumn2=None , adjustableColumn3=None , adjustableColumn4=None , adjustableColumn5=None , adjustableColumn6=None , adjustableColumn=None , annotation=None , attribute=None , backgroundColor=None , columnAlign=None , columnAttach=None , columnAlign2=None , columnAlign3=None , columnAlign4=None , columnAlign5=None , columnAlign6=None , columnOffset2=None , columnOffset3=None , columnOffset4=None , columnOffset5=None , columnOffset6=None , columnAttach2=None , columnAttach3=None , columnAttach4=None , columnAttach5=None , columnAttach6=None , columnWidth=None , columnWidth1=None , columnWidth2=None , columnWidth3=None , columnWidth4=None , columnWidth5=None , columnWidth6=None , dragCallback=None , dropCallback=None , defineTemplate=None , docTag=None , enumeratedItem=None , enable=None , exists=None , height=None , isObscured=None , label=None , manage=None , numberOfPopupMenus=None , parent=None , popupMenuArray=None , preventOverride=None , rowAttach=None , useTemplate=None , visible=None , width=None , **args ):
    self.uiName = cmds.attrEnumOptionMenuGrp()

    ##### substitution #####
    if adjustableColumn2 != None:
      self.adjustableColumn2 = adjustableColumn2
    if adjustableColumn3 != None:
      self.adjustableColumn3 = adjustableColumn3
    if adjustableColumn4 != None:
      self.adjustableColumn4 = adjustableColumn4
    if adjustableColumn5 != None:
      self.adjustableColumn5 = adjustableColumn5
    if adjustableColumn6 != None:
      self.adjustableColumn6 = adjustableColumn6
    if adjustableColumn != None:
      self.adjustableColumn = adjustableColumn
    if annotation != None:
      self.annotation = annotation
    if attribute != None:
      self.attribute = attribute
    if backgroundColor != None:
      self.backgroundColor = backgroundColor
    if columnAlign != None:
      self.columnAlign = columnAlign
    if columnAttach != None:
      self.columnAttach = columnAttach
    if columnAlign2 != None:
      self.columnAlign2 = columnAlign2
    if columnAlign3 != None:
      self.columnAlign3 = columnAlign3
    if columnAlign4 != None:
      self.columnAlign4 = columnAlign4
    if columnAlign5 != None:
      self.columnAlign5 = columnAlign5
    if columnAlign6 != None:
      self.columnAlign6 = columnAlign6
    if columnOffset2 != None:
      self.columnOffset2 = columnOffset2
    if columnOffset3 != None:
      self.columnOffset3 = columnOffset3
    if columnOffset4 != None:
      self.columnOffset4 = columnOffset4
    if columnOffset5 != None:
      self.columnOffset5 = columnOffset5
    if columnOffset6 != None:
      self.columnOffset6 = columnOffset6
    if columnAttach2 != None:
      self.columnAttach2 = columnAttach2
    if columnAttach3 != None:
      self.columnAttach3 = columnAttach3
    if columnAttach4 != None:
      self.columnAttach4 = columnAttach4
    if columnAttach5 != None:
      self.columnAttach5 = columnAttach5
    if columnAttach6 != None:
      self.columnAttach6 = columnAttach6
    if columnWidth != None:
      self.columnWidth = columnWidth
    if columnWidth1 != None:
      self.columnWidth1 = columnWidth1
    if columnWidth2 != None:
      self.columnWidth2 = columnWidth2
    if columnWidth3 != None:
      self.columnWidth3 = columnWidth3
    if columnWidth4 != None:
      self.columnWidth4 = columnWidth4
    if columnWidth5 != None:
      self.columnWidth5 = columnWidth5
    if columnWidth6 != None:
      self.columnWidth6 = columnWidth6
    if dragCallback != None:
      self.dragCallback = dragCallback
    if dropCallback != None:
      self.dropCallback = dropCallback
    if defineTemplate != None:
      self.defineTemplate = defineTemplate
    if docTag != None:
      self.docTag = docTag
    if enumeratedItem != None:
      self.enumeratedItem = enumeratedItem
    if enable != None:
      self.enable = enable
    if exists != None:
      self.exists = exists
    if height != None:
      self.height = height
    if isObscured != None:
      self.isObscured = isObscured
    if label != None:
      self.label = label
    if manage != None:
      self.manage = manage
    if numberOfPopupMenus != None:
      self.numberOfPopupMenus = numberOfPopupMenus
    if parent != None:
      self.parent = parent
    if popupMenuArray != None:
      self.popupMenuArray = popupMenuArray
    if preventOverride != None:
      self.preventOverride = preventOverride
    if rowAttach != None:
      self.rowAttach = rowAttach
    if useTemplate != None:
      self.useTemplate = useTemplate
    if visible != None:
      self.visible = visible
    if width != None:
      self.width = width

  ##### getFuncCode #####
  def getadjustableColumn2( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , adjustableColumn2=1 )
  def getadjustableColumn3( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , adjustableColumn3=1 )
  def getadjustableColumn4( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , adjustableColumn4=1 )
  def getadjustableColumn5( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , adjustableColumn5=1 )
  def getadjustableColumn6( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , adjustableColumn6=1 )
  def getadjustableColumn( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , adjustableColumn=1 )
  def getannotation( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , annotation=1 )
  def getattribute( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , attribute=1 )
  def getbackgroundColor( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , backgroundColor=1 )
  def getcolumnAlign( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnAlign=1 )
  def getcolumnAttach( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnAttach=1 )
  def getcolumnAlign2( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnAlign2=1 )
  def getcolumnAlign3( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnAlign3=1 )
  def getcolumnAlign4( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnAlign4=1 )
  def getcolumnAlign5( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnAlign5=1 )
  def getcolumnAlign6( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnAlign6=1 )
  def getcolumnOffset2( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnOffset2=1 )
  def getcolumnOffset3( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnOffset3=1 )
  def getcolumnOffset4( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnOffset4=1 )
  def getcolumnOffset5( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnOffset5=1 )
  def getcolumnOffset6( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnOffset6=1 )
  def getcolumnAttach2( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnAttach2=1 )
  def getcolumnAttach3( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnAttach3=1 )
  def getcolumnAttach4( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnAttach4=1 )
  def getcolumnAttach5( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnAttach5=1 )
  def getcolumnAttach6( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnAttach6=1 )
  def getcolumnWidth( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnWidth=1 )
  def getcolumnWidth1( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnWidth1=1 )
  def getcolumnWidth2( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnWidth2=1 )
  def getcolumnWidth3( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnWidth3=1 )
  def getcolumnWidth4( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnWidth4=1 )
  def getcolumnWidth5( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnWidth5=1 )
  def getcolumnWidth6( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , columnWidth6=1 )
  def getdragCallback( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , dragCallback=1 )
  def getdropCallback( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , dropCallback=1 )
  def getdefineTemplate( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , defineTemplate=1 )
  def getdocTag( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , docTag=1 )
  def getenumeratedItem( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , enumeratedItem=1 )
  def getenable( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , enable=1 )
  def getexists( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , exists=1 )
  def getheight( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , height=1 )
  def getisObscured( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , isObscured=1 )
  def getlabel( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , label=1 )
  def getmanage( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , manage=1 )
  def getnumberOfPopupMenus( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , numberOfPopupMenus=1 )
  def getparent( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , parent=1 )
  def getpopupMenuArray( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , popupMenuArray=1 )
  def getpreventOverride( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , preventOverride=1 )
  def getrowAttach( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , rowAttach=1 )
  def getuseTemplate( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , useTemplate=1 )
  def getvisible( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , visible=1 )
  def getwidth( self ):
    return cmds.attrEnumOptionMenuGrp( self.uiName , q=1 , width=1 )

  ##### setFuncCode #####
  def setadjustableColumn2( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , adjustableColumn2=value )
  def setadjustableColumn3( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , adjustableColumn3=value )
  def setadjustableColumn4( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , adjustableColumn4=value )
  def setadjustableColumn5( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , adjustableColumn5=value )
  def setadjustableColumn6( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , adjustableColumn6=value )
  def setadjustableColumn( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , adjustableColumn=value )
  def setannotation( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , annotation=value )
  def setattribute( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , attribute=value )
  def setbackgroundColor( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , backgroundColor=value )
  def setcolumnAlign( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnAlign=value )
  def setcolumnAttach( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnAttach=value )
  def setcolumnAlign2( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnAlign2=value )
  def setcolumnAlign3( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnAlign3=value )
  def setcolumnAlign4( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnAlign4=value )
  def setcolumnAlign5( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnAlign5=value )
  def setcolumnAlign6( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnAlign6=value )
  def setcolumnOffset2( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnOffset2=value )
  def setcolumnOffset3( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnOffset3=value )
  def setcolumnOffset4( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnOffset4=value )
  def setcolumnOffset5( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnOffset5=value )
  def setcolumnOffset6( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnOffset6=value )
  def setcolumnAttach2( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnAttach2=value )
  def setcolumnAttach3( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnAttach3=value )
  def setcolumnAttach4( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnAttach4=value )
  def setcolumnAttach5( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnAttach5=value )
  def setcolumnAttach6( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnAttach6=value )
  def setcolumnWidth( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnWidth=value )
  def setcolumnWidth1( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnWidth1=value )
  def setcolumnWidth2( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnWidth2=value )
  def setcolumnWidth3( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnWidth3=value )
  def setcolumnWidth4( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnWidth4=value )
  def setcolumnWidth5( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnWidth5=value )
  def setcolumnWidth6( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , columnWidth6=value )
  def setdragCallback( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , dragCallback=value )
  def setdropCallback( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , dropCallback=value )
  def setdefineTemplate( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , defineTemplate=value )
  def setdocTag( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , docTag=value )
  def setenumeratedItem( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , enumeratedItem=value )
  def setenable( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , enable=value )
  def setexists( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , exists=value )
  def setheight( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , height=value )
  def setisObscured( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , isObscured=value )
  def setlabel( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , label=value )
  def setmanage( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , manage=value )
  def setnumberOfPopupMenus( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , numberOfPopupMenus=value )
  def setparent( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , parent=value )
  def setpopupMenuArray( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , popupMenuArray=value )
  def setpreventOverride( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , preventOverride=value )
  def setrowAttach( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , rowAttach=value )
  def setuseTemplate( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , useTemplate=value )
  def setvisible( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , visible=value )
  def setwidth( self , value ):
    cmds.attrEnumOptionMenuGrp( self.uiName , e=1 , width=value )

  ##### propertyCode #####
  adjustableColumn2 = property( getadjustableColumn2 , setadjustableColumn2 )
  adjustableColumn3 = property( getadjustableColumn3 , setadjustableColumn3 )
  adjustableColumn4 = property( getadjustableColumn4 , setadjustableColumn4 )
  adjustableColumn5 = property( getadjustableColumn5 , setadjustableColumn5 )
  adjustableColumn6 = property( getadjustableColumn6 , setadjustableColumn6 )
  adjustableColumn = property( getadjustableColumn , setadjustableColumn )
  annotation = property( getannotation , setannotation )
  attribute = property( getattribute , setattribute )
  backgroundColor = property( getbackgroundColor , setbackgroundColor )
  columnAlign = property( getcolumnAlign , setcolumnAlign )
  columnAttach = property( getcolumnAttach , setcolumnAttach )
  columnAlign2 = property( getcolumnAlign2 , setcolumnAlign2 )
  columnAlign3 = property( getcolumnAlign3 , setcolumnAlign3 )
  columnAlign4 = property( getcolumnAlign4 , setcolumnAlign4 )
  columnAlign5 = property( getcolumnAlign5 , setcolumnAlign5 )
  columnAlign6 = property( getcolumnAlign6 , setcolumnAlign6 )
  columnOffset2 = property( getcolumnOffset2 , setcolumnOffset2 )
  columnOffset3 = property( getcolumnOffset3 , setcolumnOffset3 )
  columnOffset4 = property( getcolumnOffset4 , setcolumnOffset4 )
  columnOffset5 = property( getcolumnOffset5 , setcolumnOffset5 )
  columnOffset6 = property( getcolumnOffset6 , setcolumnOffset6 )
  columnAttach2 = property( getcolumnAttach2 , setcolumnAttach2 )
  columnAttach3 = property( getcolumnAttach3 , setcolumnAttach3 )
  columnAttach4 = property( getcolumnAttach4 , setcolumnAttach4 )
  columnAttach5 = property( getcolumnAttach5 , setcolumnAttach5 )
  columnAttach6 = property( getcolumnAttach6 , setcolumnAttach6 )
  columnWidth = property( getcolumnWidth , setcolumnWidth )
  columnWidth1 = property( getcolumnWidth1 , setcolumnWidth1 )
  columnWidth2 = property( getcolumnWidth2 , setcolumnWidth2 )
  columnWidth3 = property( getcolumnWidth3 , setcolumnWidth3 )
  columnWidth4 = property( getcolumnWidth4 , setcolumnWidth4 )
  columnWidth5 = property( getcolumnWidth5 , setcolumnWidth5 )
  columnWidth6 = property( getcolumnWidth6 , setcolumnWidth6 )
  dragCallback = property( getdragCallback , setdragCallback )
  dropCallback = property( getdropCallback , setdropCallback )
  defineTemplate = property( getdefineTemplate , setdefineTemplate )
  docTag = property( getdocTag , setdocTag )
  enumeratedItem = property( getenumeratedItem , setenumeratedItem )
  enable = property( getenable , setenable )
  exists = property( getexists , setexists )
  height = property( getheight , setheight )
  isObscured = property( getisObscured , setisObscured )
  label = property( getlabel , setlabel )
  manage = property( getmanage , setmanage )
  numberOfPopupMenus = property( getnumberOfPopupMenus , setnumberOfPopupMenus )
  parent = property( getparent , setparent )
  popupMenuArray = property( getpopupMenuArray , setpopupMenuArray )
  preventOverride = property( getpreventOverride , setpreventOverride )
  rowAttach = property( getrowAttach , setrowAttach )
  useTemplate = property( getuseTemplate , setuseTemplate )
  visible = property( getvisible , setvisible )
  width = property( getwidth , setwidth )

  ##### customCode #####





class AttributeMenu( object ):

  ##### initialize #####
  def __init__( self , beginMenu=None , editor=None , finishMenu=None , inputs=None , plug=None , regPulldownMenuCommand=None , unregPulldownMenuCommand=None , **args ):
    self.uiName = cmds.attributeMenu()

    ##### substitution #####
    if beginMenu != None:
      self.beginMenu = beginMenu
    if editor != None:
      self.editor = editor
    if finishMenu != None:
      self.finishMenu = finishMenu
    if inputs != None:
      self.inputs = inputs
    if plug != None:
      self.plug = plug
    if regPulldownMenuCommand != None:
      self.regPulldownMenuCommand = regPulldownMenuCommand
    if unregPulldownMenuCommand != None:
      self.unregPulldownMenuCommand = unregPulldownMenuCommand

  ##### getFuncCode #####
  def getbeginMenu( self ):
    return cmds.attributeMenu( self.uiName , q=1 , beginMenu=1 )
  def geteditor( self ):
    return cmds.attributeMenu( self.uiName , q=1 , editor=1 )
  def getfinishMenu( self ):
    return cmds.attributeMenu( self.uiName , q=1 , finishMenu=1 )
  def getinputs( self ):
    return cmds.attributeMenu( self.uiName , q=1 , inputs=1 )
  def getplug( self ):
    return cmds.attributeMenu( self.uiName , q=1 , plug=1 )
  def getregPulldownMenuCommand( self ):
    return cmds.attributeMenu( self.uiName , q=1 , regPulldownMenuCommand=1 )
  def getunregPulldownMenuCommand( self ):
    return cmds.attributeMenu( self.uiName , q=1 , unregPulldownMenuCommand=1 )

  ##### setFuncCode #####
  def setbeginMenu( self , value ):
    cmds.attributeMenu( self.uiName , e=1 , beginMenu=value )
  def seteditor( self , value ):
    cmds.attributeMenu( self.uiName , e=1 , editor=value )
  def setfinishMenu( self , value ):
    cmds.attributeMenu( self.uiName , e=1 , finishMenu=value )
  def setinputs( self , value ):
    cmds.attributeMenu( self.uiName , e=1 , inputs=value )
  def setplug( self , value ):
    cmds.attributeMenu( self.uiName , e=1 , plug=value )
  def setregPulldownMenuCommand( self , value ):
    cmds.attributeMenu( self.uiName , e=1 , regPulldownMenuCommand=value )
  def setunregPulldownMenuCommand( self , value ):
    cmds.attributeMenu( self.uiName , e=1 , unregPulldownMenuCommand=value )

  ##### propertyCode #####
  beginMenu = property( getbeginMenu , setbeginMenu )
  editor = property( geteditor , seteditor )
  finishMenu = property( getfinishMenu , setfinishMenu )
  inputs = property( getinputs , setinputs )
  plug = property( getplug , setplug )
  regPulldownMenuCommand = property( getregPulldownMenuCommand , setregPulldownMenuCommand )
  unregPulldownMenuCommand = property( getunregPulldownMenuCommand , setunregPulldownMenuCommand )

  ##### customCode #####





class HotBox( object ):

  ##### initialize #####
  def __init__( self , showAllToggleMenus=None , animationOnlyMenus=None , animationToggleMenus=None , clothOnlyMenus=None , clothToggleMenus=None , commonOnlyMenus=None , customMenuSetsToggleMenus=None , commonToggleMenus=None , displayCenterOnly=None , displayHotbox=None , dynamicsOnlyMenus=None , displayStyle=None , dynamicsToggleMenus=None , displayZonesOnly=None , liveOnlyMenus=None , liveToggleMenus=None , menuSetOnly=None , menuSetToggle=None , noClickCommand=None , noClickDelay=None , noKeyPress=None , polygonsOnlyMenus=None , polygonsToggleMenus=None , PaneOnlyMenus=None , PaneToggleMenus=None , release=None , rmbPopups=None , renderingOnlyMenus=None , renderingToggleMenus=None , surfacesOnlyMenus=None , surfacesToggleMenus=None , transparenyLevel=None , updateMenus=None , **args ):
    self.uiName = cmds.hotBox()

    ##### substitution #####
    if showAllToggleMenus != None:
      self.showAllToggleMenus = showAllToggleMenus
    if animationOnlyMenus != None:
      self.animationOnlyMenus = animationOnlyMenus
    if animationToggleMenus != None:
      self.animationToggleMenus = animationToggleMenus
    if clothOnlyMenus != None:
      self.clothOnlyMenus = clothOnlyMenus
    if clothToggleMenus != None:
      self.clothToggleMenus = clothToggleMenus
    if commonOnlyMenus != None:
      self.commonOnlyMenus = commonOnlyMenus
    if customMenuSetsToggleMenus != None:
      self.customMenuSetsToggleMenus = customMenuSetsToggleMenus
    if commonToggleMenus != None:
      self.commonToggleMenus = commonToggleMenus
    if displayCenterOnly != None:
      self.displayCenterOnly = displayCenterOnly
    if displayHotbox != None:
      self.displayHotbox = displayHotbox
    if dynamicsOnlyMenus != None:
      self.dynamicsOnlyMenus = dynamicsOnlyMenus
    if displayStyle != None:
      self.displayStyle = displayStyle
    if dynamicsToggleMenus != None:
      self.dynamicsToggleMenus = dynamicsToggleMenus
    if displayZonesOnly != None:
      self.displayZonesOnly = displayZonesOnly
    if liveOnlyMenus != None:
      self.liveOnlyMenus = liveOnlyMenus
    if liveToggleMenus != None:
      self.liveToggleMenus = liveToggleMenus
    if menuSetOnly != None:
      self.menuSetOnly = menuSetOnly
    if menuSetToggle != None:
      self.menuSetToggle = menuSetToggle
    if noClickCommand != None:
      self.noClickCommand = noClickCommand
    if noClickDelay != None:
      self.noClickDelay = noClickDelay
    if noKeyPress != None:
      self.noKeyPress = noKeyPress
    if polygonsOnlyMenus != None:
      self.polygonsOnlyMenus = polygonsOnlyMenus
    if polygonsToggleMenus != None:
      self.polygonsToggleMenus = polygonsToggleMenus
    if PaneOnlyMenus != None:
      self.PaneOnlyMenus = PaneOnlyMenus
    if PaneToggleMenus != None:
      self.PaneToggleMenus = PaneToggleMenus
    if release != None:
      self.release = release
    if rmbPopups != None:
      self.rmbPopups = rmbPopups
    if renderingOnlyMenus != None:
      self.renderingOnlyMenus = renderingOnlyMenus
    if renderingToggleMenus != None:
      self.renderingToggleMenus = renderingToggleMenus
    if surfacesOnlyMenus != None:
      self.surfacesOnlyMenus = surfacesOnlyMenus
    if surfacesToggleMenus != None:
      self.surfacesToggleMenus = surfacesToggleMenus
    if transparenyLevel != None:
      self.transparenyLevel = transparenyLevel
    if updateMenus != None:
      self.updateMenus = updateMenus

  ##### getFuncCode #####
  def getshowAllToggleMenus( self ):
    return cmds.hotBox( self.uiName , q=1 , showAllToggleMenus=1 )
  def getanimationOnlyMenus( self ):
    return cmds.hotBox( self.uiName , q=1 , animationOnlyMenus=1 )
  def getanimationToggleMenus( self ):
    return cmds.hotBox( self.uiName , q=1 , animationToggleMenus=1 )
  def getclothOnlyMenus( self ):
    return cmds.hotBox( self.uiName , q=1 , clothOnlyMenus=1 )
  def getclothToggleMenus( self ):
    return cmds.hotBox( self.uiName , q=1 , clothToggleMenus=1 )
  def getcommonOnlyMenus( self ):
    return cmds.hotBox( self.uiName , q=1 , commonOnlyMenus=1 )
  def getcustomMenuSetsToggleMenus( self ):
    return cmds.hotBox( self.uiName , q=1 , customMenuSetsToggleMenus=1 )
  def getcommonToggleMenus( self ):
    return cmds.hotBox( self.uiName , q=1 , commonToggleMenus=1 )
  def getdisplayCenterOnly( self ):
    return cmds.hotBox( self.uiName , q=1 , displayCenterOnly=1 )
  def getdisplayHotbox( self ):
    return cmds.hotBox( self.uiName , q=1 , displayHotbox=1 )
  def getdynamicsOnlyMenus( self ):
    return cmds.hotBox( self.uiName , q=1 , dynamicsOnlyMenus=1 )
  def getdisplayStyle( self ):
    return cmds.hotBox( self.uiName , q=1 , displayStyle=1 )
  def getdynamicsToggleMenus( self ):
    return cmds.hotBox( self.uiName , q=1 , dynamicsToggleMenus=1 )
  def getdisplayZonesOnly( self ):
    return cmds.hotBox( self.uiName , q=1 , displayZonesOnly=1 )
  def getliveOnlyMenus( self ):
    return cmds.hotBox( self.uiName , q=1 , liveOnlyMenus=1 )
  def getliveToggleMenus( self ):
    return cmds.hotBox( self.uiName , q=1 , liveToggleMenus=1 )
  def getmenuSetOnly( self ):
    return cmds.hotBox( self.uiName , q=1 , menuSetOnly=1 )
  def getmenuSetToggle( self ):
    return cmds.hotBox( self.uiName , q=1 , menuSetToggle=1 )
  def getnoClickCommand( self ):
    return cmds.hotBox( self.uiName , q=1 , noClickCommand=1 )
  def getnoClickDelay( self ):
    return cmds.hotBox( self.uiName , q=1 , noClickDelay=1 )
  def getnoKeyPress( self ):
    return cmds.hotBox( self.uiName , q=1 , noKeyPress=1 )
  def getpolygonsOnlyMenus( self ):
    return cmds.hotBox( self.uiName , q=1 , polygonsOnlyMenus=1 )
  def getpolygonsToggleMenus( self ):
    return cmds.hotBox( self.uiName , q=1 , polygonsToggleMenus=1 )
  def getPaneOnlyMenus( self ):
    return cmds.hotBox( self.uiName , q=1 , PaneOnlyMenus=1 )
  def getPaneToggleMenus( self ):
    return cmds.hotBox( self.uiName , q=1 , PaneToggleMenus=1 )
  def getrelease( self ):
    return cmds.hotBox( self.uiName , q=1 , release=1 )
  def getrmbPopups( self ):
    return cmds.hotBox( self.uiName , q=1 , rmbPopups=1 )
  def getrenderingOnlyMenus( self ):
    return cmds.hotBox( self.uiName , q=1 , renderingOnlyMenus=1 )
  def getrenderingToggleMenus( self ):
    return cmds.hotBox( self.uiName , q=1 , renderingToggleMenus=1 )
  def getsurfacesOnlyMenus( self ):
    return cmds.hotBox( self.uiName , q=1 , surfacesOnlyMenus=1 )
  def getsurfacesToggleMenus( self ):
    return cmds.hotBox( self.uiName , q=1 , surfacesToggleMenus=1 )
  def gettransparenyLevel( self ):
    return cmds.hotBox( self.uiName , q=1 , transparenyLevel=1 )
  def getupdateMenus( self ):
    return cmds.hotBox( self.uiName , q=1 , updateMenus=1 )

  ##### setFuncCode #####
  def setshowAllToggleMenus( self , value ):
    cmds.hotBox( self.uiName , e=1 , showAllToggleMenus=value )
  def setanimationOnlyMenus( self , value ):
    cmds.hotBox( self.uiName , e=1 , animationOnlyMenus=value )
  def setanimationToggleMenus( self , value ):
    cmds.hotBox( self.uiName , e=1 , animationToggleMenus=value )
  def setclothOnlyMenus( self , value ):
    cmds.hotBox( self.uiName , e=1 , clothOnlyMenus=value )
  def setclothToggleMenus( self , value ):
    cmds.hotBox( self.uiName , e=1 , clothToggleMenus=value )
  def setcommonOnlyMenus( self , value ):
    cmds.hotBox( self.uiName , e=1 , commonOnlyMenus=value )
  def setcustomMenuSetsToggleMenus( self , value ):
    cmds.hotBox( self.uiName , e=1 , customMenuSetsToggleMenus=value )
  def setcommonToggleMenus( self , value ):
    cmds.hotBox( self.uiName , e=1 , commonToggleMenus=value )
  def setdisplayCenterOnly( self , value ):
    cmds.hotBox( self.uiName , e=1 , displayCenterOnly=value )
  def setdisplayHotbox( self , value ):
    cmds.hotBox( self.uiName , e=1 , displayHotbox=value )
  def setdynamicsOnlyMenus( self , value ):
    cmds.hotBox( self.uiName , e=1 , dynamicsOnlyMenus=value )
  def setdisplayStyle( self , value ):
    cmds.hotBox( self.uiName , e=1 , displayStyle=value )
  def setdynamicsToggleMenus( self , value ):
    cmds.hotBox( self.uiName , e=1 , dynamicsToggleMenus=value )
  def setdisplayZonesOnly( self , value ):
    cmds.hotBox( self.uiName , e=1 , displayZonesOnly=value )
  def setliveOnlyMenus( self , value ):
    cmds.hotBox( self.uiName , e=1 , liveOnlyMenus=value )
  def setliveToggleMenus( self , value ):
    cmds.hotBox( self.uiName , e=1 , liveToggleMenus=value )
  def setmenuSetOnly( self , value ):
    cmds.hotBox( self.uiName , e=1 , menuSetOnly=value )
  def setmenuSetToggle( self , value ):
    cmds.hotBox( self.uiName , e=1 , menuSetToggle=value )
  def setnoClickCommand( self , value ):
    cmds.hotBox( self.uiName , e=1 , noClickCommand=value )
  def setnoClickDelay( self , value ):
    cmds.hotBox( self.uiName , e=1 , noClickDelay=value )
  def setnoKeyPress( self , value ):
    cmds.hotBox( self.uiName , e=1 , noKeyPress=value )
  def setpolygonsOnlyMenus( self , value ):
    cmds.hotBox( self.uiName , e=1 , polygonsOnlyMenus=value )
  def setpolygonsToggleMenus( self , value ):
    cmds.hotBox( self.uiName , e=1 , polygonsToggleMenus=value )
  def setPaneOnlyMenus( self , value ):
    cmds.hotBox( self.uiName , e=1 , PaneOnlyMenus=value )
  def setPaneToggleMenus( self , value ):
    cmds.hotBox( self.uiName , e=1 , PaneToggleMenus=value )
  def setrelease( self , value ):
    cmds.hotBox( self.uiName , e=1 , release=value )
  def setrmbPopups( self , value ):
    cmds.hotBox( self.uiName , e=1 , rmbPopups=value )
  def setrenderingOnlyMenus( self , value ):
    cmds.hotBox( self.uiName , e=1 , renderingOnlyMenus=value )
  def setrenderingToggleMenus( self , value ):
    cmds.hotBox( self.uiName , e=1 , renderingToggleMenus=value )
  def setsurfacesOnlyMenus( self , value ):
    cmds.hotBox( self.uiName , e=1 , surfacesOnlyMenus=value )
  def setsurfacesToggleMenus( self , value ):
    cmds.hotBox( self.uiName , e=1 , surfacesToggleMenus=value )
  def settransparenyLevel( self , value ):
    cmds.hotBox( self.uiName , e=1 , transparenyLevel=value )
  def setupdateMenus( self , value ):
    cmds.hotBox( self.uiName , e=1 , updateMenus=value )

  ##### propertyCode #####
  showAllToggleMenus = property( getshowAllToggleMenus , setshowAllToggleMenus )
  animationOnlyMenus = property( getanimationOnlyMenus , setanimationOnlyMenus )
  animationToggleMenus = property( getanimationToggleMenus , setanimationToggleMenus )
  clothOnlyMenus = property( getclothOnlyMenus , setclothOnlyMenus )
  clothToggleMenus = property( getclothToggleMenus , setclothToggleMenus )
  commonOnlyMenus = property( getcommonOnlyMenus , setcommonOnlyMenus )
  customMenuSetsToggleMenus = property( getcustomMenuSetsToggleMenus , setcustomMenuSetsToggleMenus )
  commonToggleMenus = property( getcommonToggleMenus , setcommonToggleMenus )
  displayCenterOnly = property( getdisplayCenterOnly , setdisplayCenterOnly )
  displayHotbox = property( getdisplayHotbox , setdisplayHotbox )
  dynamicsOnlyMenus = property( getdynamicsOnlyMenus , setdynamicsOnlyMenus )
  displayStyle = property( getdisplayStyle , setdisplayStyle )
  dynamicsToggleMenus = property( getdynamicsToggleMenus , setdynamicsToggleMenus )
  displayZonesOnly = property( getdisplayZonesOnly , setdisplayZonesOnly )
  liveOnlyMenus = property( getliveOnlyMenus , setliveOnlyMenus )
  liveToggleMenus = property( getliveToggleMenus , setliveToggleMenus )
  menuSetOnly = property( getmenuSetOnly , setmenuSetOnly )
  menuSetToggle = property( getmenuSetToggle , setmenuSetToggle )
  noClickCommand = property( getnoClickCommand , setnoClickCommand )
  noClickDelay = property( getnoClickDelay , setnoClickDelay )
  noKeyPress = property( getnoKeyPress , setnoKeyPress )
  polygonsOnlyMenus = property( getpolygonsOnlyMenus , setpolygonsOnlyMenus )
  polygonsToggleMenus = property( getpolygonsToggleMenus , setpolygonsToggleMenus )
  PaneOnlyMenus = property( getPaneOnlyMenus , setPaneOnlyMenus )
  PaneToggleMenus = property( getPaneToggleMenus , setPaneToggleMenus )
  release = property( getrelease , setrelease )
  rmbPopups = property( getrmbPopups , setrmbPopups )
  renderingOnlyMenus = property( getrenderingOnlyMenus , setrenderingOnlyMenus )
  renderingToggleMenus = property( getrenderingToggleMenus , setrenderingToggleMenus )
  surfacesOnlyMenus = property( getsurfacesOnlyMenus , setsurfacesOnlyMenus )
  surfacesToggleMenus = property( getsurfacesToggleMenus , setsurfacesToggleMenus )
  transparenyLevel = property( gettransparenyLevel , settransparenyLevel )
  updateMenus = property( getupdateMenus , setupdateMenus )

  ##### customCode #####





class MenuEditor( object ):

  ##### initialize #####
  def __init__( self , annotation=None , backgroundColor=None , command=None , childArray=None , checkBoxPresent=None , checkBoxState=None , cellHeight=None , cellWidth=None , cellWidthHeight=None , delete=None , dragCallback=None , dropCallback=None , defineTemplate=None , docTag=None , enable=None , exists=None , height=None , image=None , iconMenuCallback=None , isObscured=None , label=None , manage=None , menuItemTypes=None , numberOfChildren=None , numberOfPopupMenus=None , optionBoxCommand=None , optionBoxPresent=None , parent=None , popupMenuArray=None , preventOverride=None , radioButtonPresent=None , radioButtonState=None , subMenuEditorsOpen=None , subMenuEditorWindow=None , subMenuAt=None , subMenuOf=None , separator=None , style=None , topLevelMenu=None , useTemplate=None , visible=None , width=None , **args ):
    self.uiName = cmds.menuEditor()

    ##### substitution #####
    if annotation != None:
      self.annotation = annotation
    if backgroundColor != None:
      self.backgroundColor = backgroundColor
    if command != None:
      self.command = command
    if childArray != None:
      self.childArray = childArray
    if checkBoxPresent != None:
      self.checkBoxPresent = checkBoxPresent
    if checkBoxState != None:
      self.checkBoxState = checkBoxState
    if cellHeight != None:
      self.cellHeight = cellHeight
    if cellWidth != None:
      self.cellWidth = cellWidth
    if cellWidthHeight != None:
      self.cellWidthHeight = cellWidthHeight
    if delete != None:
      self.delete = delete
    if dragCallback != None:
      self.dragCallback = dragCallback
    if dropCallback != None:
      self.dropCallback = dropCallback
    if defineTemplate != None:
      self.defineTemplate = defineTemplate
    if docTag != None:
      self.docTag = docTag
    if enable != None:
      self.enable = enable
    if exists != None:
      self.exists = exists
    if height != None:
      self.height = height
    if image != None:
      self.image = image
    if iconMenuCallback != None:
      self.iconMenuCallback = iconMenuCallback
    if isObscured != None:
      self.isObscured = isObscured
    if label != None:
      self.label = label
    if manage != None:
      self.manage = manage
    if menuItemTypes != None:
      self.menuItemTypes = menuItemTypes
    if numberOfChildren != None:
      self.numberOfChildren = numberOfChildren
    if numberOfPopupMenus != None:
      self.numberOfPopupMenus = numberOfPopupMenus
    if optionBoxCommand != None:
      self.optionBoxCommand = optionBoxCommand
    if optionBoxPresent != None:
      self.optionBoxPresent = optionBoxPresent
    if parent != None:
      self.parent = parent
    if popupMenuArray != None:
      self.popupMenuArray = popupMenuArray
    if preventOverride != None:
      self.preventOverride = preventOverride
    if radioButtonPresent != None:
      self.radioButtonPresent = radioButtonPresent
    if radioButtonState != None:
      self.radioButtonState = radioButtonState
    if subMenuEditorsOpen != None:
      self.subMenuEditorsOpen = subMenuEditorsOpen
    if subMenuEditorWindow != None:
      self.subMenuEditorWindow = subMenuEditorWindow
    if subMenuAt != None:
      self.subMenuAt = subMenuAt
    if subMenuOf != None:
      self.subMenuOf = subMenuOf
    if separator != None:
      self.separator = separator
    if style != None:
      self.style = style
    if topLevelMenu != None:
      self.topLevelMenu = topLevelMenu
    if useTemplate != None:
      self.useTemplate = useTemplate
    if visible != None:
      self.visible = visible
    if width != None:
      self.width = width

  ##### getFuncCode #####
  def getannotation( self ):
    return cmds.menuEditor( self.uiName , q=1 , annotation=1 )
  def getbackgroundColor( self ):
    return cmds.menuEditor( self.uiName , q=1 , backgroundColor=1 )
  def getcommand( self ):
    return cmds.menuEditor( self.uiName , q=1 , command=1 )
  def getchildArray( self ):
    return cmds.menuEditor( self.uiName , q=1 , childArray=1 )
  def getcheckBoxPresent( self ):
    return cmds.menuEditor( self.uiName , q=1 , checkBoxPresent=1 )
  def getcheckBoxState( self ):
    return cmds.menuEditor( self.uiName , q=1 , checkBoxState=1 )
  def getcellHeight( self ):
    return cmds.menuEditor( self.uiName , q=1 , cellHeight=1 )
  def getcellWidth( self ):
    return cmds.menuEditor( self.uiName , q=1 , cellWidth=1 )
  def getcellWidthHeight( self ):
    return cmds.menuEditor( self.uiName , q=1 , cellWidthHeight=1 )
  def getdelete( self ):
    return cmds.menuEditor( self.uiName , q=1 , delete=1 )
  def getdragCallback( self ):
    return cmds.menuEditor( self.uiName , q=1 , dragCallback=1 )
  def getdropCallback( self ):
    return cmds.menuEditor( self.uiName , q=1 , dropCallback=1 )
  def getdefineTemplate( self ):
    return cmds.menuEditor( self.uiName , q=1 , defineTemplate=1 )
  def getdocTag( self ):
    return cmds.menuEditor( self.uiName , q=1 , docTag=1 )
  def getenable( self ):
    return cmds.menuEditor( self.uiName , q=1 , enable=1 )
  def getexists( self ):
    return cmds.menuEditor( self.uiName , q=1 , exists=1 )
  def getheight( self ):
    return cmds.menuEditor( self.uiName , q=1 , height=1 )
  def getimage( self ):
    return cmds.menuEditor( self.uiName , q=1 , image=1 )
  def geticonMenuCallback( self ):
    return cmds.menuEditor( self.uiName , q=1 , iconMenuCallback=1 )
  def getisObscured( self ):
    return cmds.menuEditor( self.uiName , q=1 , isObscured=1 )
  def getlabel( self ):
    return cmds.menuEditor( self.uiName , q=1 , label=1 )
  def getmanage( self ):
    return cmds.menuEditor( self.uiName , q=1 , manage=1 )
  def getmenuItemTypes( self ):
    return cmds.menuEditor( self.uiName , q=1 , menuItemTypes=1 )
  def getnumberOfChildren( self ):
    return cmds.menuEditor( self.uiName , q=1 , numberOfChildren=1 )
  def getnumberOfPopupMenus( self ):
    return cmds.menuEditor( self.uiName , q=1 , numberOfPopupMenus=1 )
  def getoptionBoxCommand( self ):
    return cmds.menuEditor( self.uiName , q=1 , optionBoxCommand=1 )
  def getoptionBoxPresent( self ):
    return cmds.menuEditor( self.uiName , q=1 , optionBoxPresent=1 )
  def getparent( self ):
    return cmds.menuEditor( self.uiName , q=1 , parent=1 )
  def getpopupMenuArray( self ):
    return cmds.menuEditor( self.uiName , q=1 , popupMenuArray=1 )
  def getpreventOverride( self ):
    return cmds.menuEditor( self.uiName , q=1 , preventOverride=1 )
  def getradioButtonPresent( self ):
    return cmds.menuEditor( self.uiName , q=1 , radioButtonPresent=1 )
  def getradioButtonState( self ):
    return cmds.menuEditor( self.uiName , q=1 , radioButtonState=1 )
  def getsubMenuEditorsOpen( self ):
    return cmds.menuEditor( self.uiName , q=1 , subMenuEditorsOpen=1 )
  def getsubMenuEditorWindow( self ):
    return cmds.menuEditor( self.uiName , q=1 , subMenuEditorWindow=1 )
  def getsubMenuAt( self ):
    return cmds.menuEditor( self.uiName , q=1 , subMenuAt=1 )
  def getsubMenuOf( self ):
    return cmds.menuEditor( self.uiName , q=1 , subMenuOf=1 )
  def getseparator( self ):
    return cmds.menuEditor( self.uiName , q=1 , separator=1 )
  def getstyle( self ):
    return cmds.menuEditor( self.uiName , q=1 , style=1 )
  def gettopLevelMenu( self ):
    return cmds.menuEditor( self.uiName , q=1 , topLevelMenu=1 )
  def getuseTemplate( self ):
    return cmds.menuEditor( self.uiName , q=1 , useTemplate=1 )
  def getvisible( self ):
    return cmds.menuEditor( self.uiName , q=1 , visible=1 )
  def getwidth( self ):
    return cmds.menuEditor( self.uiName , q=1 , width=1 )

  ##### setFuncCode #####
  def setannotation( self , value ):
    cmds.menuEditor( self.uiName , e=1 , annotation=value )
  def setbackgroundColor( self , value ):
    cmds.menuEditor( self.uiName , e=1 , backgroundColor=value )
  def setcommand( self , value ):
    cmds.menuEditor( self.uiName , e=1 , command=value )
  def setchildArray( self , value ):
    cmds.menuEditor( self.uiName , e=1 , childArray=value )
  def setcheckBoxPresent( self , value ):
    cmds.menuEditor( self.uiName , e=1 , checkBoxPresent=value )
  def setcheckBoxState( self , value ):
    cmds.menuEditor( self.uiName , e=1 , checkBoxState=value )
  def setcellHeight( self , value ):
    cmds.menuEditor( self.uiName , e=1 , cellHeight=value )
  def setcellWidth( self , value ):
    cmds.menuEditor( self.uiName , e=1 , cellWidth=value )
  def setcellWidthHeight( self , value ):
    cmds.menuEditor( self.uiName , e=1 , cellWidthHeight=value )
  def setdelete( self , value ):
    cmds.menuEditor( self.uiName , e=1 , delete=value )
  def setdragCallback( self , value ):
    cmds.menuEditor( self.uiName , e=1 , dragCallback=value )
  def setdropCallback( self , value ):
    cmds.menuEditor( self.uiName , e=1 , dropCallback=value )
  def setdefineTemplate( self , value ):
    cmds.menuEditor( self.uiName , e=1 , defineTemplate=value )
  def setdocTag( self , value ):
    cmds.menuEditor( self.uiName , e=1 , docTag=value )
  def setenable( self , value ):
    cmds.menuEditor( self.uiName , e=1 , enable=value )
  def setexists( self , value ):
    cmds.menuEditor( self.uiName , e=1 , exists=value )
  def setheight( self , value ):
    cmds.menuEditor( self.uiName , e=1 , height=value )
  def setimage( self , value ):
    cmds.menuEditor( self.uiName , e=1 , image=value )
  def seticonMenuCallback( self , value ):
    cmds.menuEditor( self.uiName , e=1 , iconMenuCallback=value )
  def setisObscured( self , value ):
    cmds.menuEditor( self.uiName , e=1 , isObscured=value )
  def setlabel( self , value ):
    cmds.menuEditor( self.uiName , e=1 , label=value )
  def setmanage( self , value ):
    cmds.menuEditor( self.uiName , e=1 , manage=value )
  def setmenuItemTypes( self , value ):
    cmds.menuEditor( self.uiName , e=1 , menuItemTypes=value )
  def setnumberOfChildren( self , value ):
    cmds.menuEditor( self.uiName , e=1 , numberOfChildren=value )
  def setnumberOfPopupMenus( self , value ):
    cmds.menuEditor( self.uiName , e=1 , numberOfPopupMenus=value )
  def setoptionBoxCommand( self , value ):
    cmds.menuEditor( self.uiName , e=1 , optionBoxCommand=value )
  def setoptionBoxPresent( self , value ):
    cmds.menuEditor( self.uiName , e=1 , optionBoxPresent=value )
  def setparent( self , value ):
    cmds.menuEditor( self.uiName , e=1 , parent=value )
  def setpopupMenuArray( self , value ):
    cmds.menuEditor( self.uiName , e=1 , popupMenuArray=value )
  def setpreventOverride( self , value ):
    cmds.menuEditor( self.uiName , e=1 , preventOverride=value )
  def setradioButtonPresent( self , value ):
    cmds.menuEditor( self.uiName , e=1 , radioButtonPresent=value )
  def setradioButtonState( self , value ):
    cmds.menuEditor( self.uiName , e=1 , radioButtonState=value )
  def setsubMenuEditorsOpen( self , value ):
    cmds.menuEditor( self.uiName , e=1 , subMenuEditorsOpen=value )
  def setsubMenuEditorWindow( self , value ):
    cmds.menuEditor( self.uiName , e=1 , subMenuEditorWindow=value )
  def setsubMenuAt( self , value ):
    cmds.menuEditor( self.uiName , e=1 , subMenuAt=value )
  def setsubMenuOf( self , value ):
    cmds.menuEditor( self.uiName , e=1 , subMenuOf=value )
  def setseparator( self , value ):
    cmds.menuEditor( self.uiName , e=1 , separator=value )
  def setstyle( self , value ):
    cmds.menuEditor( self.uiName , e=1 , style=value )
  def settopLevelMenu( self , value ):
    cmds.menuEditor( self.uiName , e=1 , topLevelMenu=value )
  def setuseTemplate( self , value ):
    cmds.menuEditor( self.uiName , e=1 , useTemplate=value )
  def setvisible( self , value ):
    cmds.menuEditor( self.uiName , e=1 , visible=value )
  def setwidth( self , value ):
    cmds.menuEditor( self.uiName , e=1 , width=value )

  ##### propertyCode #####
  annotation = property( getannotation , setannotation )
  backgroundColor = property( getbackgroundColor , setbackgroundColor )
  command = property( getcommand , setcommand )
  childArray = property( getchildArray , setchildArray )
  checkBoxPresent = property( getcheckBoxPresent , setcheckBoxPresent )
  checkBoxState = property( getcheckBoxState , setcheckBoxState )
  cellHeight = property( getcellHeight , setcellHeight )
  cellWidth = property( getcellWidth , setcellWidth )
  cellWidthHeight = property( getcellWidthHeight , setcellWidthHeight )
  delete = property( getdelete , setdelete )
  dragCallback = property( getdragCallback , setdragCallback )
  dropCallback = property( getdropCallback , setdropCallback )
  defineTemplate = property( getdefineTemplate , setdefineTemplate )
  docTag = property( getdocTag , setdocTag )
  enable = property( getenable , setenable )
  exists = property( getexists , setexists )
  height = property( getheight , setheight )
  image = property( getimage , setimage )
  iconMenuCallback = property( geticonMenuCallback , seticonMenuCallback )
  isObscured = property( getisObscured , setisObscured )
  label = property( getlabel , setlabel )
  manage = property( getmanage , setmanage )
  menuItemTypes = property( getmenuItemTypes , setmenuItemTypes )
  numberOfChildren = property( getnumberOfChildren , setnumberOfChildren )
  numberOfPopupMenus = property( getnumberOfPopupMenus , setnumberOfPopupMenus )
  optionBoxCommand = property( getoptionBoxCommand , setoptionBoxCommand )
  optionBoxPresent = property( getoptionBoxPresent , setoptionBoxPresent )
  parent = property( getparent , setparent )
  popupMenuArray = property( getpopupMenuArray , setpopupMenuArray )
  preventOverride = property( getpreventOverride , setpreventOverride )
  radioButtonPresent = property( getradioButtonPresent , setradioButtonPresent )
  radioButtonState = property( getradioButtonState , setradioButtonState )
  subMenuEditorsOpen = property( getsubMenuEditorsOpen , setsubMenuEditorsOpen )
  subMenuEditorWindow = property( getsubMenuEditorWindow , setsubMenuEditorWindow )
  subMenuAt = property( getsubMenuAt , setsubMenuAt )
  subMenuOf = property( getsubMenuOf , setsubMenuOf )
  separator = property( getseparator , setseparator )
  style = property( getstyle , setstyle )
  topLevelMenu = property( gettopLevelMenu , settopLevelMenu )
  useTemplate = property( getuseTemplate , setuseTemplate )
  visible = property( getvisible , setvisible )
  width = property( getwidth , setwidth )

  ##### customCode #####





class MenuSet( object ):

  ##### initialize #####
  def __init__( self , addMenu=None , allMenuSets=None , currentMenuSet=None , exists=None , hotBoxVisible=None , insertMenu=None , label=None , menuArray=None , moveMenu=None , moveMenuSet=None , numberOfMenus=None , numberOfMenuSets=None , permanent=None , removeMenu=None , removeMenuSet=None , **args ):
    self.uiName = cmds.menuSet()

    ##### substitution #####
    if addMenu != None:
      self.addMenu = addMenu
    if allMenuSets != None:
      self.allMenuSets = allMenuSets
    if currentMenuSet != None:
      self.currentMenuSet = currentMenuSet
    if exists != None:
      self.exists = exists
    if hotBoxVisible != None:
      self.hotBoxVisible = hotBoxVisible
    if insertMenu != None:
      self.insertMenu = insertMenu
    if label != None:
      self.label = label
    if menuArray != None:
      self.menuArray = menuArray
    if moveMenu != None:
      self.moveMenu = moveMenu
    if moveMenuSet != None:
      self.moveMenuSet = moveMenuSet
    if numberOfMenus != None:
      self.numberOfMenus = numberOfMenus
    if numberOfMenuSets != None:
      self.numberOfMenuSets = numberOfMenuSets
    if permanent != None:
      self.permanent = permanent
    if removeMenu != None:
      self.removeMenu = removeMenu
    if removeMenuSet != None:
      self.removeMenuSet = removeMenuSet

  ##### getFuncCode #####
  def getaddMenu( self ):
    return cmds.menuSet( self.uiName , q=1 , addMenu=1 )
  def getallMenuSets( self ):
    return cmds.menuSet( self.uiName , q=1 , allMenuSets=1 )
  def getcurrentMenuSet( self ):
    return cmds.menuSet( self.uiName , q=1 , currentMenuSet=1 )
  def getexists( self ):
    return cmds.menuSet( self.uiName , q=1 , exists=1 )
  def gethotBoxVisible( self ):
    return cmds.menuSet( self.uiName , q=1 , hotBoxVisible=1 )
  def getinsertMenu( self ):
    return cmds.menuSet( self.uiName , q=1 , insertMenu=1 )
  def getlabel( self ):
    return cmds.menuSet( self.uiName , q=1 , label=1 )
  def getmenuArray( self ):
    return cmds.menuSet( self.uiName , q=1 , menuArray=1 )
  def getmoveMenu( self ):
    return cmds.menuSet( self.uiName , q=1 , moveMenu=1 )
  def getmoveMenuSet( self ):
    return cmds.menuSet( self.uiName , q=1 , moveMenuSet=1 )
  def getnumberOfMenus( self ):
    return cmds.menuSet( self.uiName , q=1 , numberOfMenus=1 )
  def getnumberOfMenuSets( self ):
    return cmds.menuSet( self.uiName , q=1 , numberOfMenuSets=1 )
  def getpermanent( self ):
    return cmds.menuSet( self.uiName , q=1 , permanent=1 )
  def getremoveMenu( self ):
    return cmds.menuSet( self.uiName , q=1 , removeMenu=1 )
  def getremoveMenuSet( self ):
    return cmds.menuSet( self.uiName , q=1 , removeMenuSet=1 )

  ##### setFuncCode #####
  def setaddMenu( self , value ):
    cmds.menuSet( self.uiName , e=1 , addMenu=value )
  def setallMenuSets( self , value ):
    cmds.menuSet( self.uiName , e=1 , allMenuSets=value )
  def setcurrentMenuSet( self , value ):
    cmds.menuSet( self.uiName , e=1 , currentMenuSet=value )
  def setexists( self , value ):
    cmds.menuSet( self.uiName , e=1 , exists=value )
  def sethotBoxVisible( self , value ):
    cmds.menuSet( self.uiName , e=1 , hotBoxVisible=value )
  def setinsertMenu( self , value ):
    cmds.menuSet( self.uiName , e=1 , insertMenu=value )
  def setlabel( self , value ):
    cmds.menuSet( self.uiName , e=1 , label=value )
  def setmenuArray( self , value ):
    cmds.menuSet( self.uiName , e=1 , menuArray=value )
  def setmoveMenu( self , value ):
    cmds.menuSet( self.uiName , e=1 , moveMenu=value )
  def setmoveMenuSet( self , value ):
    cmds.menuSet( self.uiName , e=1 , moveMenuSet=value )
  def setnumberOfMenus( self , value ):
    cmds.menuSet( self.uiName , e=1 , numberOfMenus=value )
  def setnumberOfMenuSets( self , value ):
    cmds.menuSet( self.uiName , e=1 , numberOfMenuSets=value )
  def setpermanent( self , value ):
    cmds.menuSet( self.uiName , e=1 , permanent=value )
  def setremoveMenu( self , value ):
    cmds.menuSet( self.uiName , e=1 , removeMenu=value )
  def setremoveMenuSet( self , value ):
    cmds.menuSet( self.uiName , e=1 , removeMenuSet=value )

  ##### propertyCode #####
  addMenu = property( getaddMenu , setaddMenu )
  allMenuSets = property( getallMenuSets , setallMenuSets )
  currentMenuSet = property( getcurrentMenuSet , setcurrentMenuSet )
  exists = property( getexists , setexists )
  hotBoxVisible = property( gethotBoxVisible , sethotBoxVisible )
  insertMenu = property( getinsertMenu , setinsertMenu )
  label = property( getlabel , setlabel )
  menuArray = property( getmenuArray , setmenuArray )
  moveMenu = property( getmoveMenu , setmoveMenu )
  moveMenuSet = property( getmoveMenuSet , setmoveMenuSet )
  numberOfMenus = property( getnumberOfMenus , setnumberOfMenus )
  numberOfMenuSets = property( getnumberOfMenuSets , setnumberOfMenuSets )
  permanent = property( getpermanent , setpermanent )
  removeMenu = property( getremoveMenu , setremoveMenu )
  removeMenuSet = property( getremoveMenuSet , setremoveMenuSet )

  ##### customCode #####





class MenuSetPref( object ):

  ##### initialize #####
  def __init__( self , force=None , loadAll=None , removeAll=None , saveAll=None , saveBackup=None , version=None , **args ):
    self.uiName = cmds.menuSetPref()

    ##### substitution #####
    if force != None:
      self.force = force
    if loadAll != None:
      self.loadAll = loadAll
    if removeAll != None:
      self.removeAll = removeAll
    if saveAll != None:
      self.saveAll = saveAll
    if saveBackup != None:
      self.saveBackup = saveBackup
    if version != None:
      self.version = version

  ##### getFuncCode #####
  def getforce( self ):
    return cmds.menuSetPref( self.uiName , q=1 , force=1 )
  def getloadAll( self ):
    return cmds.menuSetPref( self.uiName , q=1 , loadAll=1 )
  def getremoveAll( self ):
    return cmds.menuSetPref( self.uiName , q=1 , removeAll=1 )
  def getsaveAll( self ):
    return cmds.menuSetPref( self.uiName , q=1 , saveAll=1 )
  def getsaveBackup( self ):
    return cmds.menuSetPref( self.uiName , q=1 , saveBackup=1 )
  def getversion( self ):
    return cmds.menuSetPref( self.uiName , q=1 , version=1 )

  ##### setFuncCode #####
  def setforce( self , value ):
    cmds.menuSetPref( self.uiName , e=1 , force=value )
  def setloadAll( self , value ):
    cmds.menuSetPref( self.uiName , e=1 , loadAll=value )
  def setremoveAll( self , value ):
    cmds.menuSetPref( self.uiName , e=1 , removeAll=value )
  def setsaveAll( self , value ):
    cmds.menuSetPref( self.uiName , e=1 , saveAll=value )
  def setsaveBackup( self , value ):
    cmds.menuSetPref( self.uiName , e=1 , saveBackup=value )
  def setversion( self , value ):
    cmds.menuSetPref( self.uiName , e=1 , version=value )

  ##### propertyCode #####
  force = property( getforce , setforce )
  loadAll = property( getloadAll , setloadAll )
  removeAll = property( getremoveAll , setremoveAll )
  saveAll = property( getsaveAll , setsaveAll )
  saveBackup = property( getsaveBackup , setsaveBackup )
  version = property( getversion , setversion )

  ##### customCode #####





##class OptionMenuGrp( object ):
##
##  ##### initialize #####
##  def __init__( self , adjustableColumn2=None , adjustableColumn3=None , adjustableColumn4=None , adjustableColumn5=None , adjustableColumn6=None , adjustableColumn=None , annotation=None , backgroundColor=None , columnAlign=None , columnAttach=None , changeCommand=None , columnAlign2=None , columnAlign3=None , columnAlign4=None , columnAlign5=None , columnAlign6=None , columnOffset2=None , columnOffset3=None , columnOffset4=None , columnOffset5=None , columnOffset6=None , columnAttach2=None , columnAttach3=None , columnAttach4=None , columnAttach5=None , columnAttach6=None , columnWidth=None , columnWidth1=None , columnWidth2=None , columnWidth3=None , columnWidth4=None , columnWidth5=None , columnWidth6=None , dragCallback=None , dropCallback=None , defineTemplate=None , docTag=None , extraLabel=None , enable=None , exists=None , height=None , itemListLong=None , itemListShort=None , isObscured=None , label=None , manage=None , numberOfItems=None , numberOfPopupMenus=None , parent=None , popupMenuArray=None , preventOverride=None , rowAttach=None , select=None , useTemplate=None , value=None , visible=None , width=None , **args ):
##    self.uiName = cmds.optionMenuGrp()
##
##    ##### substitution #####
##    if adjustableColumn2 != None:
##      self.adjustableColumn2 = adjustableColumn2
##    if adjustableColumn3 != None:
##      self.adjustableColumn3 = adjustableColumn3
##    if adjustableColumn4 != None:
##      self.adjustableColumn4 = adjustableColumn4
##    if adjustableColumn5 != None:
##      self.adjustableColumn5 = adjustableColumn5
##    if adjustableColumn6 != None:
##      self.adjustableColumn6 = adjustableColumn6
##    if adjustableColumn != None:
##      self.adjustableColumn = adjustableColumn
##    if annotation != None:
##      self.annotation = annotation
##    if backgroundColor != None:
##      self.backgroundColor = backgroundColor
##    if columnAlign != None:
##      self.columnAlign = columnAlign
##    if columnAttach != None:
##      self.columnAttach = columnAttach
##    if changeCommand != None:
##      self.changeCommand = changeCommand
##    if columnAlign2 != None:
##      self.columnAlign2 = columnAlign2
##    if columnAlign3 != None:
##      self.columnAlign3 = columnAlign3
##    if columnAlign4 != None:
##      self.columnAlign4 = columnAlign4
##    if columnAlign5 != None:
##      self.columnAlign5 = columnAlign5
##    if columnAlign6 != None:
##      self.columnAlign6 = columnAlign6
##    if columnOffset2 != None:
##      self.columnOffset2 = columnOffset2
##    if columnOffset3 != None:
##      self.columnOffset3 = columnOffset3
##    if columnOffset4 != None:
##      self.columnOffset4 = columnOffset4
##    if columnOffset5 != None:
##      self.columnOffset5 = columnOffset5
##    if columnOffset6 != None:
##      self.columnOffset6 = columnOffset6
##    if columnAttach2 != None:
##      self.columnAttach2 = columnAttach2
##    if columnAttach3 != None:
##      self.columnAttach3 = columnAttach3
##    if columnAttach4 != None:
##      self.columnAttach4 = columnAttach4
##    if columnAttach5 != None:
##      self.columnAttach5 = columnAttach5
##    if columnAttach6 != None:
##      self.columnAttach6 = columnAttach6
##    if columnWidth != None:
##      self.columnWidth = columnWidth
##    if columnWidth1 != None:
##      self.columnWidth1 = columnWidth1
##    if columnWidth2 != None:
##      self.columnWidth2 = columnWidth2
##    if columnWidth3 != None:
##      self.columnWidth3 = columnWidth3
##    if columnWidth4 != None:
##      self.columnWidth4 = columnWidth4
##    if columnWidth5 != None:
##      self.columnWidth5 = columnWidth5
##    if columnWidth6 != None:
##      self.columnWidth6 = columnWidth6
##    if dragCallback != None:
##      self.dragCallback = dragCallback
##    if dropCallback != None:
##      self.dropCallback = dropCallback
##    if defineTemplate != None:
##      self.defineTemplate = defineTemplate
##    if docTag != None:
##      self.docTag = docTag
##    if extraLabel != None:
##      self.extraLabel = extraLabel
##    if enable != None:
##      self.enable = enable
##    if exists != None:
##      self.exists = exists
##    if height != None:
##      self.height = height
##    if itemListLong != None:
##      self.itemListLong = itemListLong
##    if itemListShort != None:
##      self.itemListShort = itemListShort
##    if isObscured != None:
##      self.isObscured = isObscured
##    if label != None:
##      self.label = label
##    if manage != None:
##      self.manage = manage
##    if numberOfItems != None:
##      self.numberOfItems = numberOfItems
##    if numberOfPopupMenus != None:
##      self.numberOfPopupMenus = numberOfPopupMenus
##    if parent != None:
##      self.parent = parent
##    if popupMenuArray != None:
##      self.popupMenuArray = popupMenuArray
##    if preventOverride != None:
##      self.preventOverride = preventOverride
##    if rowAttach != None:
##      self.rowAttach = rowAttach
##    if select != None:
##      self.select = select
##    if useTemplate != None:
##      self.useTemplate = useTemplate
##    if value != None:
##      self.value = value
##    if visible != None:
##      self.visible = visible
##    if width != None:
##      self.width = width
##
##  ##### getFuncCode #####
##  def getadjustableColumn2( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , adjustableColumn2=1 )
##  def getadjustableColumn3( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , adjustableColumn3=1 )
##  def getadjustableColumn4( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , adjustableColumn4=1 )
##  def getadjustableColumn5( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , adjustableColumn5=1 )
##  def getadjustableColumn6( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , adjustableColumn6=1 )
##  def getadjustableColumn( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , adjustableColumn=1 )
##  def getannotation( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , annotation=1 )
##  def getbackgroundColor( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , backgroundColor=1 )
##  def getcolumnAlign( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnAlign=1 )
##  def getcolumnAttach( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnAttach=1 )
##  def getchangeCommand( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , changeCommand=1 )
##  def getcolumnAlign2( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnAlign2=1 )
##  def getcolumnAlign3( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnAlign3=1 )
##  def getcolumnAlign4( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnAlign4=1 )
##  def getcolumnAlign5( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnAlign5=1 )
##  def getcolumnAlign6( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnAlign6=1 )
##  def getcolumnOffset2( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnOffset2=1 )
##  def getcolumnOffset3( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnOffset3=1 )
##  def getcolumnOffset4( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnOffset4=1 )
##  def getcolumnOffset5( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnOffset5=1 )
##  def getcolumnOffset6( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnOffset6=1 )
##  def getcolumnAttach2( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnAttach2=1 )
##  def getcolumnAttach3( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnAttach3=1 )
##  def getcolumnAttach4( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnAttach4=1 )
##  def getcolumnAttach5( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnAttach5=1 )
##  def getcolumnAttach6( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnAttach6=1 )
##  def getcolumnWidth( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnWidth=1 )
##  def getcolumnWidth1( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnWidth1=1 )
##  def getcolumnWidth2( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnWidth2=1 )
##  def getcolumnWidth3( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnWidth3=1 )
##  def getcolumnWidth4( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnWidth4=1 )
##  def getcolumnWidth5( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnWidth5=1 )
##  def getcolumnWidth6( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , columnWidth6=1 )
##  def getdragCallback( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , dragCallback=1 )
##  def getdropCallback( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , dropCallback=1 )
##  def getdefineTemplate( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , defineTemplate=1 )
##  def getdocTag( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , docTag=1 )
##  def getextraLabel( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , extraLabel=1 )
##  def getenable( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , enable=1 )
##  def getexists( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , exists=1 )
##  def getheight( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , height=1 )
##  def getitemListLong( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , itemListLong=1 )
##  def getitemListShort( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , itemListShort=1 )
##  def getisObscured( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , isObscured=1 )
##  def getlabel( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , label=1 )
##  def getmanage( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , manage=1 )
##  def getnumberOfItems( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , numberOfItems=1 )
##  def getnumberOfPopupMenus( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , numberOfPopupMenus=1 )
##  def getparent( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , parent=1 )
##  def getpopupMenuArray( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , popupMenuArray=1 )
##  def getpreventOverride( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , preventOverride=1 )
##  def getrowAttach( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , rowAttach=1 )
##  def getselect( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , select=1 )
##  def getuseTemplate( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , useTemplate=1 )
##  def getvalue( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , value=1 )
##  def getvisible( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , visible=1 )
##  def getwidth( self ):
##    return cmds.optionMenuGrp( self.uiName , q=1 , width=1 )
##
##  ##### setFuncCode #####
##  def setadjustableColumn2( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , adjustableColumn2=value )
##  def setadjustableColumn3( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , adjustableColumn3=value )
##  def setadjustableColumn4( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , adjustableColumn4=value )
##  def setadjustableColumn5( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , adjustableColumn5=value )
##  def setadjustableColumn6( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , adjustableColumn6=value )
##  def setadjustableColumn( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , adjustableColumn=value )
##  def setannotation( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , annotation=value )
##  def setbackgroundColor( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , backgroundColor=value )
##  def setcolumnAlign( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnAlign=value )
##  def setcolumnAttach( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnAttach=value )
##  def setchangeCommand( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , changeCommand=value )
##  def setcolumnAlign2( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnAlign2=value )
##  def setcolumnAlign3( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnAlign3=value )
##  def setcolumnAlign4( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnAlign4=value )
##  def setcolumnAlign5( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnAlign5=value )
##  def setcolumnAlign6( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnAlign6=value )
##  def setcolumnOffset2( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnOffset2=value )
##  def setcolumnOffset3( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnOffset3=value )
##  def setcolumnOffset4( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnOffset4=value )
##  def setcolumnOffset5( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnOffset5=value )
##  def setcolumnOffset6( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnOffset6=value )
##  def setcolumnAttach2( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnAttach2=value )
##  def setcolumnAttach3( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnAttach3=value )
##  def setcolumnAttach4( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnAttach4=value )
##  def setcolumnAttach5( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnAttach5=value )
##  def setcolumnAttach6( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnAttach6=value )
##  def setcolumnWidth( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnWidth=value )
##  def setcolumnWidth1( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnWidth1=value )
##  def setcolumnWidth2( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnWidth2=value )
##  def setcolumnWidth3( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnWidth3=value )
##  def setcolumnWidth4( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnWidth4=value )
##  def setcolumnWidth5( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnWidth5=value )
##  def setcolumnWidth6( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , columnWidth6=value )
##  def setdragCallback( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , dragCallback=value )
##  def setdropCallback( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , dropCallback=value )
##  def setdefineTemplate( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , defineTemplate=value )
##  def setdocTag( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , docTag=value )
##  def setextraLabel( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , extraLabel=value )
##  def setenable( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , enable=value )
##  def setexists( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , exists=value )
##  def setheight( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , height=value )
##  def setitemListLong( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , itemListLong=value )
##  def setitemListShort( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , itemListShort=value )
##  def setisObscured( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , isObscured=value )
##  def setlabel( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , label=value )
##  def setmanage( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , manage=value )
##  def setnumberOfItems( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , numberOfItems=value )
##  def setnumberOfPopupMenus( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , numberOfPopupMenus=value )
##  def setparent( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , parent=value )
##  def setpopupMenuArray( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , popupMenuArray=value )
##  def setpreventOverride( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , preventOverride=value )
##  def setrowAttach( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , rowAttach=value )
##  def setselect( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , select=value )
##  def setuseTemplate( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , useTemplate=value )
##  def setvalue( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , value=value )
##  def setvisible( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , visible=value )
##  def setwidth( self , value ):
##    cmds.optionMenuGrp( self.uiName , e=1 , width=value )
##
##  ##### propertyCode #####
##  adjustableColumn2 = property( getadjustableColumn2 , setadjustableColumn2 )
##  adjustableColumn3 = property( getadjustableColumn3 , setadjustableColumn3 )
##  adjustableColumn4 = property( getadjustableColumn4 , setadjustableColumn4 )
##  adjustableColumn5 = property( getadjustableColumn5 , setadjustableColumn5 )
##  adjustableColumn6 = property( getadjustableColumn6 , setadjustableColumn6 )
##  adjustableColumn = property( getadjustableColumn , setadjustableColumn )
##  annotation = property( getannotation , setannotation )
##  backgroundColor = property( getbackgroundColor , setbackgroundColor )
##  columnAlign = property( getcolumnAlign , setcolumnAlign )
##  columnAttach = property( getcolumnAttach , setcolumnAttach )
##  changeCommand = property( getchangeCommand , setchangeCommand )
##  columnAlign2 = property( getcolumnAlign2 , setcolumnAlign2 )
##  columnAlign3 = property( getcolumnAlign3 , setcolumnAlign3 )
##  columnAlign4 = property( getcolumnAlign4 , setcolumnAlign4 )
##  columnAlign5 = property( getcolumnAlign5 , setcolumnAlign5 )
##  columnAlign6 = property( getcolumnAlign6 , setcolumnAlign6 )
##  columnOffset2 = property( getcolumnOffset2 , setcolumnOffset2 )
##  columnOffset3 = property( getcolumnOffset3 , setcolumnOffset3 )
##  columnOffset4 = property( getcolumnOffset4 , setcolumnOffset4 )
##  columnOffset5 = property( getcolumnOffset5 , setcolumnOffset5 )
##  columnOffset6 = property( getcolumnOffset6 , setcolumnOffset6 )
##  columnAttach2 = property( getcolumnAttach2 , setcolumnAttach2 )
##  columnAttach3 = property( getcolumnAttach3 , setcolumnAttach3 )
##  columnAttach4 = property( getcolumnAttach4 , setcolumnAttach4 )
##  columnAttach5 = property( getcolumnAttach5 , setcolumnAttach5 )
##  columnAttach6 = property( getcolumnAttach6 , setcolumnAttach6 )
##  columnWidth = property( getcolumnWidth , setcolumnWidth )
##  columnWidth1 = property( getcolumnWidth1 , setcolumnWidth1 )
##  columnWidth2 = property( getcolumnWidth2 , setcolumnWidth2 )
##  columnWidth3 = property( getcolumnWidth3 , setcolumnWidth3 )
##  columnWidth4 = property( getcolumnWidth4 , setcolumnWidth4 )
##  columnWidth5 = property( getcolumnWidth5 , setcolumnWidth5 )
##  columnWidth6 = property( getcolumnWidth6 , setcolumnWidth6 )
##  dragCallback = property( getdragCallback , setdragCallback )
##  dropCallback = property( getdropCallback , setdropCallback )
##  defineTemplate = property( getdefineTemplate , setdefineTemplate )
##  docTag = property( getdocTag , setdocTag )
##  extraLabel = property( getextraLabel , setextraLabel )
##  enable = property( getenable , setenable )
##  exists = property( getexists , setexists )
##  height = property( getheight , setheight )
##  itemListLong = property( getitemListLong , setitemListLong )
##  itemListShort = property( getitemListShort , setitemListShort )
##  isObscured = property( getisObscured , setisObscured )
##  label = property( getlabel , setlabel )
##  manage = property( getmanage , setmanage )
##  numberOfItems = property( getnumberOfItems , setnumberOfItems )
##  numberOfPopupMenus = property( getnumberOfPopupMenus , setnumberOfPopupMenus )
##  parent = property( getparent , setparent )
##  popupMenuArray = property( getpopupMenuArray , setpopupMenuArray )
##  preventOverride = property( getpreventOverride , setpreventOverride )
##  rowAttach = property( getrowAttach , setrowAttach )
##  select = property( getselect , setselect )
##  useTemplate = property( getuseTemplate , setuseTemplate )
##  value = property( getvalue , setvalue )
##  visible = property( getvisible , setvisible )
##  width = property( getwidth , setwidth )
##
##  ##### customCode #####





class SaveMenu( object ):

  ##### initialize #####
  def __init__( self , **args ):
    self.uiName = cmds.saveMenu()

    ##### substitution #####

  ##### getFuncCode #####

  ##### setFuncCode #####

  ##### propertyCode #####

  ##### customCode #####





print "MODULE IMPORTED... MYAM_PyLib_mayaUI_menu_truth"