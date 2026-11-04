#-*- coding:UTF-8 -*-

#*******************************************************************************
'''

Tool Name     : MYAM_PyLib_mayaUI_layout
Description   : MayaのLayoutグループに属するUI要素をオブジェクト指向ライクに扱うためのモジュール

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

class Layout( object ):

  ##### initialize #####
  def __init__( self , annotation=None , backgroundColor=None , childArray=None , dragCallback=None , dropCallback=None , defineTemplate=None , docTag=None , enable=None , exists=None , height=None , isObscured=None , manage=None , numberOfChildren=None , numberOfPopupMenus=None , parent=None , popupMenuArray=None , preventOverride=None , useTemplate=None , visible=None , width=None , **args ):
    self.uiName = cmds.layout()

    ##### substitution #####
    if annotation != None:
      self.annotation = annotation
    if backgroundColor != None:
      self.backgroundColor = backgroundColor
    if childArray != None:
      self.childArray = childArray
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
    if isObscured != None:
      self.isObscured = isObscured
    if manage != None:
      self.manage = manage
    if numberOfChildren != None:
      self.numberOfChildren = numberOfChildren
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
    return cmds.layout( self.uiName , q=1 , annotation=1 )
  def getbackgroundColor( self ):
    return cmds.layout( self.uiName , q=1 , backgroundColor=1 )
  def getchildArray( self ):
    return cmds.layout( self.uiName , q=1 , childArray=1 )
  def getdragCallback( self ):
    return cmds.layout( self.uiName , q=1 , dragCallback=1 )
  def getdropCallback( self ):
    return cmds.layout( self.uiName , q=1 , dropCallback=1 )
  def getdefineTemplate( self ):
    return cmds.layout( self.uiName , q=1 , defineTemplate=1 )
  def getdocTag( self ):
    return cmds.layout( self.uiName , q=1 , docTag=1 )
  def getenable( self ):
    return cmds.layout( self.uiName , q=1 , enable=1 )
  def getexists( self ):
    return cmds.layout( self.uiName , q=1 , exists=1 )
  def getheight( self ):
    return cmds.layout( self.uiName , q=1 , height=1 )
  def getisObscured( self ):
    return cmds.layout( self.uiName , q=1 , isObscured=1 )
  def getmanage( self ):
    return cmds.layout( self.uiName , q=1 , manage=1 )
  def getnumberOfChildren( self ):
    return cmds.layout( self.uiName , q=1 , numberOfChildren=1 )
  def getnumberOfPopupMenus( self ):
    return cmds.layout( self.uiName , q=1 , numberOfPopupMenus=1 )
  def getparent( self ):
    return cmds.layout( self.uiName , q=1 , parent=1 )
  def getpopupMenuArray( self ):
    return cmds.layout( self.uiName , q=1 , popupMenuArray=1 )
  def getpreventOverride( self ):
    return cmds.layout( self.uiName , q=1 , preventOverride=1 )
  def getuseTemplate( self ):
    return cmds.layout( self.uiName , q=1 , useTemplate=1 )
  def getvisible( self ):
    return cmds.layout( self.uiName , q=1 , visible=1 )
  def getwidth( self ):
    return cmds.layout( self.uiName , q=1 , width=1 )

  ##### setFuncCode #####
  def setannotation( self , value ):
    cmds.layout( self.uiName , e=1 , annotation=value )
  def setbackgroundColor( self , value ):
    cmds.layout( self.uiName , e=1 , backgroundColor=value )
  def setchildArray( self , value ):
    cmds.layout( self.uiName , e=1 , childArray=value )
  def setdragCallback( self , value ):
    cmds.layout( self.uiName , e=1 , dragCallback=value )
  def setdropCallback( self , value ):
    cmds.layout( self.uiName , e=1 , dropCallback=value )
  def setdefineTemplate( self , value ):
    cmds.layout( self.uiName , e=1 , defineTemplate=value )
  def setdocTag( self , value ):
    cmds.layout( self.uiName , e=1 , docTag=value )
  def setenable( self , value ):
    cmds.layout( self.uiName , e=1 , enable=value )
  def setexists( self , value ):
    cmds.layout( self.uiName , e=1 , exists=value )
  def setheight( self , value ):
    cmds.layout( self.uiName , e=1 , height=value )
  def setisObscured( self , value ):
    cmds.layout( self.uiName , e=1 , isObscured=value )
  def setmanage( self , value ):
    cmds.layout( self.uiName , e=1 , manage=value )
  def setnumberOfChildren( self , value ):
    cmds.layout( self.uiName , e=1 , numberOfChildren=value )
  def setnumberOfPopupMenus( self , value ):
    cmds.layout( self.uiName , e=1 , numberOfPopupMenus=value )
  def setparent( self , value ):
    cmds.setParent( parent )
    cmds.layout( self.uiName , e=1 , parent=value )
  def setpopupMenuArray( self , value ):
    cmds.layout( self.uiName , e=1 , popupMenuArray=value )
  def setpreventOverride( self , value ):
    cmds.layout( self.uiName , e=1 , preventOverride=value )
  def setuseTemplate( self , value ):
    cmds.layout( self.uiName , e=1 , useTemplate=value )
  def setvisible( self , value ):
    cmds.layout( self.uiName , e=1 , visible=value )
  def setwidth( self , value ):
    cmds.layout( self.uiName , e=1 , width=value )

  ##### propertyCode #####
  annotation = property( getannotation , setannotation )
  backgroundColor = property( getbackgroundColor , setbackgroundColor )
  childArray = property( getchildArray , setchildArray )
  dragCallback = property( getdragCallback , setdragCallback )
  dropCallback = property( getdropCallback , setdropCallback )
  defineTemplate = property( getdefineTemplate , setdefineTemplate )
  docTag = property( getdocTag , setdocTag )
  enable = property( getenable , setenable )
  exists = property( getexists , setexists )
  height = property( getheight , setheight )
  isObscured = property( getisObscured , setisObscured )
  manage = property( getmanage , setmanage )
  numberOfChildren = property( getnumberOfChildren , setnumberOfChildren )
  numberOfPopupMenus = property( getnumberOfPopupMenus , setnumberOfPopupMenus )
  parent = property( getparent , setparent )
  popupMenuArray = property( getpopupMenuArray , setpopupMenuArray )
  preventOverride = property( getpreventOverride , setpreventOverride )
  useTemplate = property( getuseTemplate , setuseTemplate )
  visible = property( getvisible , setvisible )
  width = property( getwidth , setwidth )

  ##### customCode #####

  def fillColor( self , color ):
    self.existLayouts  = cmds.lsUI( controlLayouts=1 )
    self.existcontrols = cmds.lsUI( controls=1 )

    self.backgroundColor = color

    descendents = self.__listDescendentsUI( self.uiName )

    for descendent in descendents:

      if descendent in self.existLayouts:
        cmds.layout( descendent , e=1 , backgroundColor=color )
      elif descendent in self.existcontrols:
        cmds.control( descendent , e=1 , backgroundColor=color )
      else:
        continue

  def __listDescendentsUI( self , parentUIName ):
    res = []
    children = cmds.layout( parentUIName , q=1 , childArray=1 )

    for child in children:
      if child in self.existLayouts:
        res += self.__listDescendentsUI( child )
      else:
        res.append( child )

    return res




class ColumnLayout( Layout ):

  ##### initialize #####
  def __init__( self , adjustableColumn=None , columnAlign=None , columnAttach=None , columnOffset=None , columnWidth=None , rowSpacing=None , **args ):
    self.uiName = cmds.columnLayout()

    ##### substitution #####
    if adjustableColumn != None:
      self.adjustableColumn = adjustableColumn
    if columnAlign != None:
      self.columnAlign = columnAlign
    if columnAttach != None:
      self.columnAttach = columnAttach
    if columnOffset != None:
      self.columnOffset = columnOffset
    if columnWidth != None:
      self.columnWidth = columnWidth
    if rowSpacing != None:
      self.rowSpacing = rowSpacing

  ##### getFuncCode #####
  def getadjustableColumn( self ):
    return cmds.columnLayout( self.uiName , q=1 , adjustableColumn=1 )
  def getcolumnAlign( self ):
    return cmds.columnLayout( self.uiName , q=1 , columnAlign=1 )
  def getcolumnAttach( self ):
    return cmds.columnLayout( self.uiName , q=1 , columnAttach=1 )
  def getcolumnOffset( self ):
    return cmds.columnLayout( self.uiName , q=1 , columnOffset=1 )
  def getcolumnWidth( self ):
    return cmds.columnLayout( self.uiName , q=1 , columnWidth=1 )
  def getrowSpacing( self ):
    return cmds.columnLayout( self.uiName , q=1 , rowSpacing=1 )

  ##### setFuncCode #####
  def setadjustableColumn( self , value ):
    cmds.columnLayout( self.uiName , e=1 , adjustableColumn=value )
  def setcolumnAlign( self , value ):
    cmds.columnLayout( self.uiName , e=1 , columnAlign=value )
  def setcolumnAttach( self , value ):
    cmds.columnLayout( self.uiName , e=1 , columnAttach=value )
  def setcolumnOffset( self , value ):
    cmds.columnLayout( self.uiName , e=1 , columnOffset=value )
  def setcolumnWidth( self , value ):
    cmds.columnLayout( self.uiName , e=1 , columnWidth=value )
  def setrowSpacing( self , value ):
    cmds.columnLayout( self.uiName , e=1 , rowSpacing=value )

  ##### propertyCode #####
  adjustableColumn = property( getadjustableColumn , setadjustableColumn )
  columnAlign = property( getcolumnAlign , setcolumnAlign )
  columnAttach = property( getcolumnAttach , setcolumnAttach )
  columnOffset = property( getcolumnOffset , setcolumnOffset )
  columnWidth = property( getcolumnWidth , setcolumnWidth )
  rowSpacing = property( getrowSpacing , setrowSpacing )

  ##### customCode #####





class FormLayout( Layout ):

  ##### initialize #####
  def __init__( self , attachControl=None , attachForm=None , attachNone=None , attachOppositeControl=None , attachOppositeForm=None , attachPosition=None , numberOfDivisions=None , **args ):
    self.uiName = cmds.formLayout()

    ##### substitution #####
    if attachControl != None:
      self.attachControl = attachControl
    if attachForm != None:
      self.attachForm = attachForm
    if attachNone != None:
      self.attachNone = attachNone
    if attachOppositeControl != None:
      self.attachOppositeControl = attachOppositeControl
    if attachOppositeForm != None:
      self.attachOppositeForm = attachOppositeForm
    if attachPosition != None:
      self.attachPosition = attachPosition
    if numberOfDivisions != None:
      self.numberOfDivisions = numberOfDivisions

  ##### getFuncCode #####
  def getattachControl( self ):
    return cmds.formLayout( self.uiName , q=1 , attachControl=1 )
  def getattachForm( self ):
    return cmds.formLayout( self.uiName , q=1 , attachForm=1 )
  def getattachNone( self ):
    return cmds.formLayout( self.uiName , q=1 , attachNone=1 )
  def getattachOppositeControl( self ):
    return cmds.formLayout( self.uiName , q=1 , attachOppositeControl=1 )
  def getattachOppositeForm( self ):
    return cmds.formLayout( self.uiName , q=1 , attachOppositeForm=1 )
  def getattachPosition( self ):
    return cmds.formLayout( self.uiName , q=1 , attachPosition=1 )
  def getnumberOfDivisions( self ):
    return cmds.formLayout( self.uiName , q=1 , numberOfDivisions=1 )

  ##### setFuncCode #####
  def setattachControl( self , value ):
    cmds.formLayout( self.uiName , e=1 , attachControl=value )
  def setattachForm( self , value ):
    cmds.formLayout( self.uiName , e=1 , attachForm=value )
  def setattachNone( self , value ):
    cmds.formLayout( self.uiName , e=1 , attachNone=value )
  def setattachOppositeControl( self , value ):
    cmds.formLayout( self.uiName , e=1 , attachOppositeControl=value )
  def setattachOppositeForm( self , value ):
    cmds.formLayout( self.uiName , e=1 , attachOppositeForm=value )
  def setattachPosition( self , value ):
    cmds.formLayout( self.uiName , e=1 , attachPosition=value )
  def setnumberOfDivisions( self , value ):
    cmds.formLayout( self.uiName , e=1 , numberOfDivisions=value )

  ##### propertyCode #####
  attachControl = property( getattachControl , setattachControl )
  attachForm = property( getattachForm , setattachForm )
  attachNone = property( getattachNone , setattachNone )
  attachOppositeControl = property( getattachOppositeControl , setattachOppositeControl )
  attachOppositeForm = property( getattachOppositeForm , setattachOppositeForm )
  attachPosition = property( getattachPosition , setattachPosition )
  numberOfDivisions = property( getnumberOfDivisions , setnumberOfDivisions )

  ##### customCode #####
  ac  = property( getattachControl , setattachControl )
  af  = property( getattachForm , setattachForm )
  an  = property( getattachNone , setattachNone )
  aoc = property( getattachOppositeControl , setattachOppositeControl )
  aof = property( getattachOppositeForm , setattachOppositeForm )
  ap  = property( getattachPosition , setattachPosition )



class FrameLayout( Layout ):

  ##### initialize #####
  def __init__( self , borderStyle=None , borderVisible=None , collapseCommand=None , collapse=None , collapsable=None , expandCommand=None , font=None , label=None , labelAlign=None , labelIndent=None , labelVisible=None , labelWidth=None , marginHeight=None , marginWidth=None , preCollapseCommand=None , preExpandCommand=None , **args ):
    self.uiName = cmds.frameLayout()

    ##### substitution #####
    if borderStyle != None:
      self.borderStyle = borderStyle
    if borderVisible != None:
      self.borderVisible = borderVisible
    if collapseCommand != None:
      self.collapseCommand = collapseCommand
    if collapse != None:
      self.collapse = collapse
    if collapsable != None:
      self.collapsable = collapsable
    if expandCommand != None:
      self.expandCommand = expandCommand
    if font != None:
      self.font = font
    if label != None:
      self.label = label
    if labelAlign != None:
      self.labelAlign = labelAlign
    if labelIndent != None:
      self.labelIndent = labelIndent
    if labelVisible != None:
      self.labelVisible = labelVisible
    if labelWidth != None:
      self.labelWidth = labelWidth
    if marginHeight != None:
      self.marginHeight = marginHeight
    if marginWidth != None:
      self.marginWidth = marginWidth
    if preCollapseCommand != None:
      self.preCollapseCommand = preCollapseCommand
    if preExpandCommand != None:
      self.preExpandCommand = preExpandCommand

  ##### getFuncCode #####
  def getborderStyle( self ):
    return cmds.frameLayout( self.uiName , q=1 , borderStyle=1 )
  def getborderVisible( self ):
    return cmds.frameLayout( self.uiName , q=1 , borderVisible=1 )
  def getcollapseCommand( self ):
    return cmds.frameLayout( self.uiName , q=1 , collapseCommand=1 )
  def getcollapse( self ):
    return cmds.frameLayout( self.uiName , q=1 , collapse=1 )
  def getcollapsable( self ):
    return cmds.frameLayout( self.uiName , q=1 , collapsable=1 )
  def getexpandCommand( self ):
    return cmds.frameLayout( self.uiName , q=1 , expandCommand=1 )
  def getfont( self ):
    return cmds.frameLayout( self.uiName , q=1 , font=1 )
  def getlabel( self ):
    return cmds.frameLayout( self.uiName , q=1 , label=1 )
  def getlabelAlign( self ):
    return cmds.frameLayout( self.uiName , q=1 , labelAlign=1 )
  def getlabelIndent( self ):
    return cmds.frameLayout( self.uiName , q=1 , labelIndent=1 )
  def getlabelVisible( self ):
    return cmds.frameLayout( self.uiName , q=1 , labelVisible=1 )
  def getlabelWidth( self ):
    return cmds.frameLayout( self.uiName , q=1 , labelWidth=1 )
  def getmarginHeight( self ):
    return cmds.frameLayout( self.uiName , q=1 , marginHeight=1 )
  def getmarginWidth( self ):
    return cmds.frameLayout( self.uiName , q=1 , marginWidth=1 )
  def getpreCollapseCommand( self ):
    return cmds.frameLayout( self.uiName , q=1 , preCollapseCommand=1 )
  def getpreExpandCommand( self ):
    return cmds.frameLayout( self.uiName , q=1 , preExpandCommand=1 )

  ##### setFuncCode #####
  def setborderStyle( self , value ):
    cmds.frameLayout( self.uiName , e=1 , borderStyle=value )
  def setborderVisible( self , value ):
    cmds.frameLayout( self.uiName , e=1 , borderVisible=value )
  def setcollapseCommand( self , value ):
    cmds.frameLayout( self.uiName , e=1 , collapseCommand=value )
  def setcollapse( self , value ):
    cmds.frameLayout( self.uiName , e=1 , collapse=value )
  def setcollapsable( self , value ):
    cmds.frameLayout( self.uiName , e=1 , collapsable=value )
  def setexpandCommand( self , value ):
    cmds.frameLayout( self.uiName , e=1 , expandCommand=value )
  def setfont( self , value ):
    cmds.frameLayout( self.uiName , e=1 , font=value )
  def setlabel( self , value ):
    cmds.frameLayout( self.uiName , e=1 , label=value )
  def setlabelAlign( self , value ):
    cmds.frameLayout( self.uiName , e=1 , labelAlign=value )
  def setlabelIndent( self , value ):
    cmds.frameLayout( self.uiName , e=1 , labelIndent=value )
  def setlabelVisible( self , value ):
    cmds.frameLayout( self.uiName , e=1 , labelVisible=value )
  def setlabelWidth( self , value ):
    cmds.frameLayout( self.uiName , e=1 , labelWidth=value )
  def setmarginHeight( self , value ):
    cmds.frameLayout( self.uiName , e=1 , marginHeight=value )
  def setmarginWidth( self , value ):
    cmds.frameLayout( self.uiName , e=1 , marginWidth=value )
  def setpreCollapseCommand( self , value ):
    cmds.frameLayout( self.uiName , e=1 , preCollapseCommand=value )
  def setpreExpandCommand( self , value ):
    cmds.frameLayout( self.uiName , e=1 , preExpandCommand=value )

  ##### propertyCode #####
  borderStyle = property( getborderStyle , setborderStyle )
  borderVisible = property( getborderVisible , setborderVisible )
  collapseCommand = property( getcollapseCommand , setcollapseCommand )
  collapse = property( getcollapse , setcollapse )
  collapsable = property( getcollapsable , setcollapsable )
  expandCommand = property( getexpandCommand , setexpandCommand )
  font = property( getfont , setfont )
  label = property( getlabel , setlabel )
  labelAlign = property( getlabelAlign , setlabelAlign )
  labelIndent = property( getlabelIndent , setlabelIndent )
  labelVisible = property( getlabelVisible , setlabelVisible )
  labelWidth = property( getlabelWidth , setlabelWidth )
  marginHeight = property( getmarginHeight , setmarginHeight )
  marginWidth = property( getmarginWidth , setmarginWidth )
  preCollapseCommand = property( getpreCollapseCommand , setpreCollapseCommand )
  preExpandCommand = property( getpreExpandCommand , setpreExpandCommand )

  ##### customCode #####





class ScrollLayout( Layout ):

  ##### initialize #####
  def __init__( self , childResizable=None , horizontalScrollBarThickness=None , minChildWidth=None , resizeCommand=None , scrollAreaHeight=None , scrollAreaValue=None , scrollAreaWidth=None , scrollByPixel=None , scrollPage=None , verticalScrollBarThickness=None , **args ):
    self.uiName = cmds.scrollLayout( childResizable=True )

    ##### substitution #####
    if childResizable != None:
      self.childResizable = childResizable
    if horizontalScrollBarThickness != None:
      self.horizontalScrollBarThickness = horizontalScrollBarThickness
    if minChildWidth != None:
      self.minChildWidth = minChildWidth
    if resizeCommand != None:
      self.resizeCommand = resizeCommand
    if scrollAreaHeight != None:
      self.scrollAreaHeight = scrollAreaHeight
    if scrollAreaValue != None:
      self.scrollAreaValue = scrollAreaValue
    if scrollAreaWidth != None:
      self.scrollAreaWidth = scrollAreaWidth
    if scrollByPixel != None:
      self.scrollByPixel = scrollByPixel
    if scrollPage != None:
      self.scrollPage = scrollPage
    if verticalScrollBarThickness != None:
      self.verticalScrollBarThickness = verticalScrollBarThickness

  ##### getFuncCode #####
  def getchildResizable( self ):
    return cmds.scrollLayout( self.uiName , q=1 , childResizable=1 )
  def gethorizontalScrollBarThickness( self ):
    return cmds.scrollLayout( self.uiName , q=1 , horizontalScrollBarThickness=1 )
  def getminChildWidth( self ):
    return cmds.scrollLayout( self.uiName , q=1 , minChildWidth=1 )
  def getresizeCommand( self ):
    return cmds.scrollLayout( self.uiName , q=1 , resizeCommand=1 )
  def getscrollAreaHeight( self ):
    return cmds.scrollLayout( self.uiName , q=1 , scrollAreaHeight=1 )
  def getscrollAreaValue( self ):
    return cmds.scrollLayout( self.uiName , q=1 , scrollAreaValue=1 )
  def getscrollAreaWidth( self ):
    return cmds.scrollLayout( self.uiName , q=1 , scrollAreaWidth=1 )
  def getscrollByPixel( self ):
    return cmds.scrollLayout( self.uiName , q=1 , scrollByPixel=1 )
  def getscrollPage( self ):
    return cmds.scrollLayout( self.uiName , q=1 , scrollPage=1 )
  def getverticalScrollBarThickness( self ):
    return cmds.scrollLayout( self.uiName , q=1 , verticalScrollBarThickness=1 )

  ##### setFuncCode #####
  def setchildResizable( self , value ):
    cmds.scrollLayout( self.uiName , e=1 , childResizable=value )
  def sethorizontalScrollBarThickness( self , value ):
    cmds.scrollLayout( self.uiName , e=1 , horizontalScrollBarThickness=value )
  def setminChildWidth( self , value ):
    cmds.scrollLayout( self.uiName , e=1 , minChildWidth=value )
  def setresizeCommand( self , value ):
    cmds.scrollLayout( self.uiName , e=1 , resizeCommand=value )
  def setscrollAreaHeight( self , value ):
    cmds.scrollLayout( self.uiName , e=1 , scrollAreaHeight=value )
  def setscrollAreaValue( self , value ):
    cmds.scrollLayout( self.uiName , e=1 , scrollAreaValue=value )
  def setscrollAreaWidth( self , value ):
    cmds.scrollLayout( self.uiName , e=1 , scrollAreaWidth=value )
  def setscrollByPixel( self , value ):
    cmds.scrollLayout( self.uiName , e=1 , scrollByPixel=value )
  def setscrollPage( self , value ):
    cmds.scrollLayout( self.uiName , e=1 , scrollPage=value )
  def setverticalScrollBarThickness( self , value ):
    cmds.scrollLayout( self.uiName , e=1 , verticalScrollBarThickness=value )

  ##### propertyCode #####
  childResizable = property( getchildResizable , setchildResizable )
  horizontalScrollBarThickness = property( gethorizontalScrollBarThickness , sethorizontalScrollBarThickness )
  minChildWidth = property( getminChildWidth , setminChildWidth )
  resizeCommand = property( getresizeCommand , setresizeCommand )
  scrollAreaHeight = property( getscrollAreaHeight , setscrollAreaHeight )
  scrollAreaValue = property( getscrollAreaValue , setscrollAreaValue )
  scrollAreaWidth = property( getscrollAreaWidth , setscrollAreaWidth )
  scrollByPixel = property( getscrollByPixel , setscrollByPixel )
  scrollPage = property( getscrollPage , setscrollPage )
  verticalScrollBarThickness = property( getverticalScrollBarThickness , setverticalScrollBarThickness )

  ##### customCode #####





class TabLayout( Layout ):

  ##### initialize #####
  def __init__( self , changeCommand=None , childResizable=None , doubleClickCommand=None , horizontalScrollBarThickness=None , image=None , innerMarginHeight=None , innerMarginWidth=None , imageVisible=None , minChildWidth=None , moveTab=None , preSelectCommand=None , selectCommand=None , scrollable=None , selectTab=None , selectTabIndex=None , tabLabel=None , tabLabelIndex=None , tabsVisible=None , verticalScrollBarThickness=None , **args ):
    self.uiName = cmds.tabLayout()

    ##### substitution #####
    if changeCommand != None:
      self.changeCommand = changeCommand
    if childResizable != None:
      self.childResizable = childResizable
    if doubleClickCommand != None:
      self.doubleClickCommand = doubleClickCommand
    if horizontalScrollBarThickness != None:
      self.horizontalScrollBarThickness = horizontalScrollBarThickness
    if image != None:
      self.image = image
    if innerMarginHeight != None:
      self.innerMarginHeight = innerMarginHeight
    if innerMarginWidth != None:
      self.innerMarginWidth = innerMarginWidth
    if imageVisible != None:
      self.imageVisible = imageVisible
    if minChildWidth != None:
      self.minChildWidth = minChildWidth
    if moveTab != None:
      self.moveTab = moveTab
    if preSelectCommand != None:
      self.preSelectCommand = preSelectCommand
    if selectCommand != None:
      self.selectCommand = selectCommand
    if scrollable != None:
      self.scrollable = scrollable
    if selectTab != None:
      self.selectTab = selectTab
    if selectTabIndex != None:
      self.selectTabIndex = selectTabIndex
    if tabLabel != None:
      self.tabLabel = tabLabel
    if tabLabelIndex != None:
      self.tabLabelIndex = tabLabelIndex
    if tabsVisible != None:
      self.tabsVisible = tabsVisible
    if verticalScrollBarThickness != None:
      self.verticalScrollBarThickness = verticalScrollBarThickness

  ##### getFuncCode #####
  def getchangeCommand( self ):
    return cmds.tabLayout( self.uiName , q=1 , changeCommand=1 )
  def getchildResizable( self ):
    return cmds.tabLayout( self.uiName , q=1 , childResizable=1 )
  def getdoubleClickCommand( self ):
    return cmds.tabLayout( self.uiName , q=1 , doubleClickCommand=1 )
  def gethorizontalScrollBarThickness( self ):
    return cmds.tabLayout( self.uiName , q=1 , horizontalScrollBarThickness=1 )
  def getimage( self ):
    return cmds.tabLayout( self.uiName , q=1 , image=1 )
  def getinnerMarginHeight( self ):
    return cmds.tabLayout( self.uiName , q=1 , innerMarginHeight=1 )
  def getinnerMarginWidth( self ):
    return cmds.tabLayout( self.uiName , q=1 , innerMarginWidth=1 )
  def getimageVisible( self ):
    return cmds.tabLayout( self.uiName , q=1 , imageVisible=1 )
  def getminChildWidth( self ):
    return cmds.tabLayout( self.uiName , q=1 , minChildWidth=1 )
  def getmoveTab( self ):
    return cmds.tabLayout( self.uiName , q=1 , moveTab=1 )
  def getpreSelectCommand( self ):
    return cmds.tabLayout( self.uiName , q=1 , preSelectCommand=1 )
  def getselectCommand( self ):
    return cmds.tabLayout( self.uiName , q=1 , selectCommand=1 )
  def getscrollable( self ):
    return cmds.tabLayout( self.uiName , q=1 , scrollable=1 )
  def getselectTab( self ):
    return cmds.tabLayout( self.uiName , q=1 , selectTab=1 )
  def getselectTabIndex( self ):
    return cmds.tabLayout( self.uiName , q=1 , selectTabIndex=1 )
  def gettabLabel( self ):
    return cmds.tabLayout( self.uiName , q=1 , tabLabel=1 )
  def gettabLabelIndex( self ):
    return cmds.tabLayout( self.uiName , q=1 , tabLabelIndex=1 )
  def gettabsVisible( self ):
    return cmds.tabLayout( self.uiName , q=1 , tabsVisible=1 )
  def getverticalScrollBarThickness( self ):
    return cmds.tabLayout( self.uiName , q=1 , verticalScrollBarThickness=1 )

  ##### setFuncCode #####
  def setchangeCommand( self , value ):
    cmds.tabLayout( self.uiName , e=1 , changeCommand=value )
  def setchildResizable( self , value ):
    cmds.tabLayout( self.uiName , e=1 , childResizable=value )
  def setdoubleClickCommand( self , value ):
    cmds.tabLayout( self.uiName , e=1 , doubleClickCommand=value )
  def sethorizontalScrollBarThickness( self , value ):
    cmds.tabLayout( self.uiName , e=1 , horizontalScrollBarThickness=value )
  def setimage( self , value ):
    cmds.tabLayout( self.uiName , e=1 , image=value )
  def setinnerMarginHeight( self , value ):
    cmds.tabLayout( self.uiName , e=1 , innerMarginHeight=value )
  def setinnerMarginWidth( self , value ):
    cmds.tabLayout( self.uiName , e=1 , innerMarginWidth=value )
  def setimageVisible( self , value ):
    cmds.tabLayout( self.uiName , e=1 , imageVisible=value )
  def setminChildWidth( self , value ):
    cmds.tabLayout( self.uiName , e=1 , minChildWidth=value )
  def setmoveTab( self , value ):
    cmds.tabLayout( self.uiName , e=1 , moveTab=value )
  def setpreSelectCommand( self , value ):
    cmds.tabLayout( self.uiName , e=1 , preSelectCommand=value )
  def setselectCommand( self , value ):
    cmds.tabLayout( self.uiName , e=1 , selectCommand=value )
  def setscrollable( self , value ):
    cmds.tabLayout( self.uiName , e=1 , scrollable=value )
  def setselectTab( self , value ):
    cmds.tabLayout( self.uiName , e=1 , selectTab=value )
  def setselectTabIndex( self , value ):
    cmds.tabLayout( self.uiName , e=1 , selectTabIndex=value )
  def settabLabel( self , value ):
    cmds.tabLayout( self.uiName , e=1 , tabLabel=value )
  def settabLabelIndex( self , value ):
    cmds.tabLayout( self.uiName , e=1 , tabLabelIndex=value )
  def settabsVisible( self , value ):
    cmds.tabLayout( self.uiName , e=1 , tabsVisible=value )
  def setverticalScrollBarThickness( self , value ):
    cmds.tabLayout( self.uiName , e=1 , verticalScrollBarThickness=value )

  ##### propertyCode #####
  changeCommand = property( getchangeCommand , setchangeCommand )
  childResizable = property( getchildResizable , setchildResizable )
  doubleClickCommand = property( getdoubleClickCommand , setdoubleClickCommand )
  horizontalScrollBarThickness = property( gethorizontalScrollBarThickness , sethorizontalScrollBarThickness )
  image = property( getimage , setimage )
  innerMarginHeight = property( getinnerMarginHeight , setinnerMarginHeight )
  innerMarginWidth = property( getinnerMarginWidth , setinnerMarginWidth )
  imageVisible = property( getimageVisible , setimageVisible )
  minChildWidth = property( getminChildWidth , setminChildWidth )
  moveTab = property( getmoveTab , setmoveTab )
  preSelectCommand = property( getpreSelectCommand , setpreSelectCommand )
  selectCommand = property( getselectCommand , setselectCommand )
  scrollable = property( getscrollable , setscrollable )
  selectTab = property( getselectTab , setselectTab )
  selectTabIndex = property( getselectTabIndex , setselectTabIndex )
  tabLabel = property( gettabLabel , settabLabel )
  tabLabelIndex = property( gettabLabelIndex , settabLabelIndex )
  tabsVisible = property( gettabsVisible , settabsVisible )
  verticalScrollBarThickness = property( getverticalScrollBarThickness , setverticalScrollBarThickness )

  ##### customCode #####





class HBoxLayout( FormLayout ):

  def __init__( self ):
    FormLayout.__init__( self )
    self.spacing = 0
    self.childResizable = 0
    self.numberOfDivisions = 100

  def arrange( self ):
    children = self.childArray
    childNum = len( children )

    for i in range( ( childNum - 1 ) ):
      if self.childResizable == 0:
        self.af = [ ( children[i+1] , "top"   , 0 ) ]
        self.ac = [ ( children[i+1] , "left"  , self.spacing , children[i] ) ]
        self.an = [ ( children[i+1] , "right" ) ]
        self.an = [ ( children[i+1] , "bottom"  ) ]

      else:
        self.ap = [ ( children[i+1] , "top"   , 0 , 0   ) ]
        self.ac = [ ( children[i+1] , "left"  , self.spacing , children[i] ) ]
        self.an = [ ( children[i+1] , "right" ) ]
        self.ap = [ ( children[i+1] , "bottom" , 0 , 100 ) ]

class VBoxLayout( FormLayout ):

  def __init__( self ):
    FormLayout.__init__( self )
    self.spacing = 0
    self.childResizable = 0
    self.numberOfDivisions = 100

  def arrange( self ):
    children = self.childArray
    childNum = len( children )

    for i in range( ( childNum - 1 ) ):
      if self.childResizable == 0:
        self.ac = [ ( children[i+1] , "top"    , self.spacing , children[i] ) ]
        self.af = [ ( children[i+1] , "left"   , 0 ) ]
        self.an = [ ( children[i+1] , "right"  ) ]
        self.an = [ ( children[i+1] , "bottom" ) ]

      else:
        self.ac = [ ( children[i+1] , "top"   , self.spacing , children[i] ) ]
        self.ap = [ ( children[i+1] , "left"  , 0 , 0   ) ]
        self.ap = [ ( children[i+1] , "right" , 0 , 100 ) ]
        self.an = [ ( children[i+1] , "bottom" ) ]

class HUniformLayout( FormLayout ):

  def __init__( self ):
    FormLayout.__init__( self )
    self.margin  = 0
    self.spacing = 0
    self.childResizable = 0
    self.numberOfDivisions = 100

  def arrange( self ):
    children = self.childArray
    childNum = len( children )

    spanSize = 100 / childNum
    spanGap  = 100 % childNum

    leftOffset  = 0
    rightOffset = 0

    counter = 0

    for child in children:
      leftPos  = spanSize * counter
      rightPos = spanSize * ( counter + 1 )

      if counter == 0:
        leftOffset  = self.margin
        rightOffset = self.spacing / 2

      elif counter == ( childNum - 1 ):
        leftOffset  = self.spacing / 2
        rightOffset = self.margin
        rightPos += spanGap

      else:
        leftOffset  = self.spacing / 2
        rightOffset = self.spacing / 2

      ## Adjustable Height
      if self.childResizable == 0:
        self.af = [ ( child , "top"    , 0 ) ]
        self.ap = [ ( child , "left"   , leftOffset  , leftPos ) ]
        self.ap = [ ( child , "right"  , rightOffset , rightPos ) ]
        self.an = [ ( child , "bottom" ) ]

      else:
        self.ap = [ ( child , "top"    , 0 , 0 ) ]
        self.ap = [ ( child , "left"   , leftOffset  , leftPos ) ]
        self.ap = [ ( child , "right"  , rightOffset , rightPos ) ]
        self.ap = [ ( child , "bottom" , 0 , 100 ) ]

      counter += 1

class VUniformLayout( FormLayout ):

  def __init__( self ):
    FormLayout.__init__( self )
    self.margin  = 0
    self.spacing = 0
    self.childResizable = 0
    self.numberOfDivisions = 100

  def arrange( self ):
    children = self.childArray
    childNum = len( children )

    spanSize = 100 / childNum
    spanGap  = 100 % childNum

    topOffset    = 0
    bottomOffset = 0

    counter = 0

    for child in children:
      topPos    = spanSize * counter
      bottomPos = spanSize * ( counter + 1 )

      if counter == 0:
        topOffset    = self.margin
        bottomOffset = self.spacing / 2

      elif counter == ( childNum - 1 ):
        topOffset    = self.spacing / 2
        bottomOffset = self.margin
        bottomPos += spanGap

      else:
        topOffset    = self.spacing / 2
        bottomOffset = self.spacing / 2

      ## Adjustable Width
      if self.childResizable == 0:
        self.ap = [ ( child , "top"    , topOffset , topPos ) ]
        self.af = [ ( child , "left"   , 0 ) ]
        self.af = [ ( child , "right"  , 0 ) ]
        self.ap = [ ( child , "bottom" , bottomOffset , bottomPos ) ]

      else:
        self.ap = [ ( child , "top"    , topOffset , topPos ) ]
        self.ap = [ ( child , "left"   , 0 , 0 ) ]
        self.ap = [ ( child , "right"  , 0 , 100 ) ]
        self.ap = [ ( child , "bottom" , bottomOffset , bottomPos ) ]

      counter += 1




















#######################
##### NOT USUALLY #####
#######################

class GridLayout( Layout ):

  ##### initialize #####
  def __init__( self , allowEmptyCells=None , autoGrow=None , cellHeight=None , columnsResizable=None , cellWidth=None , cellWidthHeight=None , gridOrder=None , numberOfColumns=None , numberOfRows=None , numberOfRowsColumns=None , position=None , **args ):
    self.uiName = cmds.gridLayout()

    ##### substitution #####
    if allowEmptyCells != None:
      self.allowEmptyCells = allowEmptyCells
    if autoGrow != None:
      self.autoGrow = autoGrow
    if cellHeight != None:
      self.cellHeight = cellHeight
    if columnsResizable != None:
      self.columnsResizable = columnsResizable
    if cellWidth != None:
      self.cellWidth = cellWidth
    if cellWidthHeight != None:
      self.cellWidthHeight = cellWidthHeight
    if gridOrder != None:
      self.gridOrder = gridOrder
    if numberOfColumns != None:
      self.numberOfColumns = numberOfColumns
    if numberOfRows != None:
      self.numberOfRows = numberOfRows
    if numberOfRowsColumns != None:
      self.numberOfRowsColumns = numberOfRowsColumns
    if position != None:
      self.position = position

  ##### getFuncCode #####
  def getallowEmptyCells( self ):
    return cmds.gridLayout( self.uiName , q=1 , allowEmptyCells=1 )
  def getautoGrow( self ):
    return cmds.gridLayout( self.uiName , q=1 , autoGrow=1 )
  def getcellHeight( self ):
    return cmds.gridLayout( self.uiName , q=1 , cellHeight=1 )
  def getcolumnsResizable( self ):
    return cmds.gridLayout( self.uiName , q=1 , columnsResizable=1 )
  def getcellWidth( self ):
    return cmds.gridLayout( self.uiName , q=1 , cellWidth=1 )
  def getcellWidthHeight( self ):
    return cmds.gridLayout( self.uiName , q=1 , cellWidthHeight=1 )
  def getgridOrder( self ):
    return cmds.gridLayout( self.uiName , q=1 , gridOrder=1 )
  def getnumberOfColumns( self ):
    return cmds.gridLayout( self.uiName , q=1 , numberOfColumns=1 )
  def getnumberOfRows( self ):
    return cmds.gridLayout( self.uiName , q=1 , numberOfRows=1 )
  def getnumberOfRowsColumns( self ):
    return cmds.gridLayout( self.uiName , q=1 , numberOfRowsColumns=1 )
  def getposition( self ):
    return cmds.gridLayout( self.uiName , q=1 , position=1 )

  ##### setFuncCode #####
  def setallowEmptyCells( self , value ):
    cmds.gridLayout( self.uiName , e=1 , allowEmptyCells=value )
  def setautoGrow( self , value ):
    cmds.gridLayout( self.uiName , e=1 , autoGrow=value )
  def setcellHeight( self , value ):
    cmds.gridLayout( self.uiName , e=1 , cellHeight=value )
  def setcolumnsResizable( self , value ):
    cmds.gridLayout( self.uiName , e=1 , columnsResizable=value )
  def setcellWidth( self , value ):
    cmds.gridLayout( self.uiName , e=1 , cellWidth=value )
  def setcellWidthHeight( self , value ):
    cmds.gridLayout( self.uiName , e=1 , cellWidthHeight=value )
  def setgridOrder( self , value ):
    cmds.gridLayout( self.uiName , e=1 , gridOrder=value )
  def setnumberOfColumns( self , value ):
    cmds.gridLayout( self.uiName , e=1 , numberOfColumns=value )
  def setnumberOfRows( self , value ):
    cmds.gridLayout( self.uiName , e=1 , numberOfRows=value )
  def setnumberOfRowsColumns( self , value ):
    cmds.gridLayout( self.uiName , e=1 , numberOfRowsColumns=value )
  def setposition( self , value ):
    cmds.gridLayout( self.uiName , e=1 , position=value )

  ##### propertyCode #####
  allowEmptyCells = property( getallowEmptyCells , setallowEmptyCells )
  autoGrow = property( getautoGrow , setautoGrow )
  cellHeight = property( getcellHeight , setcellHeight )
  columnsResizable = property( getcolumnsResizable , setcolumnsResizable )
  cellWidth = property( getcellWidth , setcellWidth )
  cellWidthHeight = property( getcellWidthHeight , setcellWidthHeight )
  gridOrder = property( getgridOrder , setgridOrder )
  numberOfColumns = property( getnumberOfColumns , setnumberOfColumns )
  numberOfRows = property( getnumberOfRows , setnumberOfRows )
  numberOfRowsColumns = property( getnumberOfRowsColumns , setnumberOfRowsColumns )
  position = property( getposition , setposition )

  ##### customCode #####





class MenuBarLayout( Layout ):

  ##### initialize #####
  def __init__( self , menuArray=None , menuBarVisible=None , menuIndex=None , numberOfMenus=None , **args ):
    self.uiName = cmds.menuBarLayout()

    ##### substitution #####
    if menuArray != None:
      self.menuArray = menuArray
    if menuBarVisible != None:
      self.menuBarVisible = menuBarVisible
    if menuIndex != None:
      self.menuIndex = menuIndex
    if numberOfMenus != None:
      self.numberOfMenus = numberOfMenus

  ##### getFuncCode #####
  def getmenuArray( self ):
    return cmds.menuBarLayout( self.uiName , q=1 , menuArray=1 )
  def getmenuBarVisible( self ):
    return cmds.menuBarLayout( self.uiName , q=1 , menuBarVisible=1 )
  def getmenuIndex( self ):
    return cmds.menuBarLayout( self.uiName , q=1 , menuIndex=1 )
  def getnumberOfMenus( self ):
    return cmds.menuBarLayout( self.uiName , q=1 , numberOfMenus=1 )

  ##### setFuncCode #####
  def setmenuArray( self , value ):
    cmds.menuBarLayout( self.uiName , e=1 , menuArray=value )
  def setmenuBarVisible( self , value ):
    cmds.menuBarLayout( self.uiName , e=1 , menuBarVisible=value )
  def setmenuIndex( self , value ):
    cmds.menuBarLayout( self.uiName , e=1 , menuIndex=value )
  def setnumberOfMenus( self , value ):
    cmds.menuBarLayout( self.uiName , e=1 , numberOfMenus=value )

  ##### propertyCode #####
  menuArray = property( getmenuArray , setmenuArray )
  menuBarVisible = property( getmenuBarVisible , setmenuBarVisible )
  menuIndex = property( getmenuIndex , setmenuIndex )
  numberOfMenus = property( getnumberOfMenus , setnumberOfMenus )

  ##### customCode #####





class PaneLayout( Layout ):

  ##### initialize #####
  def __init__( self , activeFrameThickness=None , activePane=None , activePaneIndex=None , configuration=None , numberOfVisiblePanes=None , pane1=None , pane2=None , pane3=None , pane4=None , paneSize=None , paneUnderPointer=None , separatorMovedCommand=None , setPane=None , separatorThickness=None , **args ):
    self.uiName = cmds.paneLayout()

    ##### substitution #####
    if activeFrameThickness != None:
      self.activeFrameThickness = activeFrameThickness
    if activePane != None:
      self.activePane = activePane
    if activePaneIndex != None:
      self.activePaneIndex = activePaneIndex
    if configuration != None:
      self.configuration = configuration
    if numberOfVisiblePanes != None:
      self.numberOfVisiblePanes = numberOfVisiblePanes
    if pane1 != None:
      self.pane1 = pane1
    if pane2 != None:
      self.pane2 = pane2
    if pane3 != None:
      self.pane3 = pane3
    if pane4 != None:
      self.pane4 = pane4
    if paneSize != None:
      self.paneSize = paneSize
    if paneUnderPointer != None:
      self.paneUnderPointer = paneUnderPointer
    if separatorMovedCommand != None:
      self.separatorMovedCommand = separatorMovedCommand
    if setPane != None:
      self.setPane = setPane
    if separatorThickness != None:
      self.separatorThickness = separatorThickness

  ##### getFuncCode #####
  def getactiveFrameThickness( self ):
    return cmds.paneLayout( self.uiName , q=1 , activeFrameThickness=1 )
  def getactivePane( self ):
    return cmds.paneLayout( self.uiName , q=1 , activePane=1 )
  def getactivePaneIndex( self ):
    return cmds.paneLayout( self.uiName , q=1 , activePaneIndex=1 )
  def getconfiguration( self ):
    return cmds.paneLayout( self.uiName , q=1 , configuration=1 )
  def getnumberOfVisiblePanes( self ):
    return cmds.paneLayout( self.uiName , q=1 , numberOfVisiblePanes=1 )
  def getpane1( self ):
    return cmds.paneLayout( self.uiName , q=1 , pane1=1 )
  def getpane2( self ):
    return cmds.paneLayout( self.uiName , q=1 , pane2=1 )
  def getpane3( self ):
    return cmds.paneLayout( self.uiName , q=1 , pane3=1 )
  def getpane4( self ):
    return cmds.paneLayout( self.uiName , q=1 , pane4=1 )
  def getpaneSize( self ):
    return cmds.paneLayout( self.uiName , q=1 , paneSize=1 )
  def getpaneUnderPointer( self ):
    return cmds.paneLayout( self.uiName , q=1 , paneUnderPointer=1 )
  def getseparatorMovedCommand( self ):
    return cmds.paneLayout( self.uiName , q=1 , separatorMovedCommand=1 )
  def getsetPane( self ):
    return cmds.paneLayout( self.uiName , q=1 , setPane=1 )
  def getseparatorThickness( self ):
    return cmds.paneLayout( self.uiName , q=1 , separatorThickness=1 )

  ##### setFuncCode #####
  def setactiveFrameThickness( self , value ):
    cmds.paneLayout( self.uiName , e=1 , activeFrameThickness=value )
  def setactivePane( self , value ):
    cmds.paneLayout( self.uiName , e=1 , activePane=value )
  def setactivePaneIndex( self , value ):
    cmds.paneLayout( self.uiName , e=1 , activePaneIndex=value )
  def setconfiguration( self , value ):
    cmds.paneLayout( self.uiName , e=1 , configuration=value )
  def setnumberOfVisiblePanes( self , value ):
    cmds.paneLayout( self.uiName , e=1 , numberOfVisiblePanes=value )
  def setpane1( self , value ):
    cmds.paneLayout( self.uiName , e=1 , pane1=value )
  def setpane2( self , value ):
    cmds.paneLayout( self.uiName , e=1 , pane2=value )
  def setpane3( self , value ):
    cmds.paneLayout( self.uiName , e=1 , pane3=value )
  def setpane4( self , value ):
    cmds.paneLayout( self.uiName , e=1 , pane4=value )
  def setpaneSize( self , value ):
    cmds.paneLayout( self.uiName , e=1 , paneSize=value )
  def setpaneUnderPointer( self , value ):
    cmds.paneLayout( self.uiName , e=1 , paneUnderPointer=value )
  def setseparatorMovedCommand( self , value ):
    cmds.paneLayout( self.uiName , e=1 , separatorMovedCommand=value )
  def setsetPane( self , value ):
    cmds.paneLayout( self.uiName , e=1 , setPane=value )
  def setseparatorThickness( self , value ):
    cmds.paneLayout( self.uiName , e=1 , separatorThickness=value )

  ##### propertyCode #####
  activeFrameThickness = property( getactiveFrameThickness , setactiveFrameThickness )
  activePane = property( getactivePane , setactivePane )
  activePaneIndex = property( getactivePaneIndex , setactivePaneIndex )
  configuration = property( getconfiguration , setconfiguration )
  numberOfVisiblePanes = property( getnumberOfVisiblePanes , setnumberOfVisiblePanes )
  pane1 = property( getpane1 , setpane1 )
  pane2 = property( getpane2 , setpane2 )
  pane3 = property( getpane3 , setpane3 )
  pane4 = property( getpane4 , setpane4 )
  paneSize = property( getpaneSize , setpaneSize )
  paneUnderPointer = property( getpaneUnderPointer , setpaneUnderPointer )
  separatorMovedCommand = property( getseparatorMovedCommand , setseparatorMovedCommand )
  setPane = property( getsetPane , setsetPane )
  separatorThickness = property( getseparatorThickness , setseparatorThickness )

  ##### customCode #####





class RowColumnLayout( Layout ):

  ##### initialize #####
  def __init__( self , columnAlign=None , columnAttach=None , columnOffset=None , columnSpacing=None , columnWidth=None , numberOfColumns=None , numberOfRows=None , rowAlign=None , rowAttach=None , rowHeight=None , rowOffset=None , rowSpacing=None , **args ):
    if numberOfColumns != None:
      self.uiName = cmds.rowColumnLayout( numberOfColumns = numberOfColumns )

    elif numberOfRows != None:
      self.uiName = cmds.rowColumnLayout( numberOfRows = numberOfRows )

    else:
      raise ValueError , "Need numberOfColumns or numberOfRows"

    ##### substitution #####
    if columnAlign != None:
      self.columnAlign = columnAlign
    if columnAttach != None:
      self.columnAttach = columnAttach
    if columnOffset != None:
      self.columnOffset = columnOffset
    if columnSpacing != None:
      self.columnSpacing = columnSpacing
    if columnWidth != None:
      self.columnWidth = columnWidth
    if numberOfColumns != None:
      self.numberOfColumns = numberOfColumns
    if numberOfRows != None:
      self.numberOfRows = numberOfRows
    if rowAlign != None:
      self.rowAlign = rowAlign
    if rowAttach != None:
      self.rowAttach = rowAttach
    if rowHeight != None:
      self.rowHeight = rowHeight
    if rowOffset != None:
      self.rowOffset = rowOffset
    if rowSpacing != None:
      self.rowSpacing = rowSpacing

  ##### getFuncCode #####
  def getcolumnAlign( self ):
    return cmds.rowColumnLayout( self.uiName , q=1 , columnAlign=1 )
  def getcolumnAttach( self ):
    return cmds.rowColumnLayout( self.uiName , q=1 , columnAttach=1 )
  def getcolumnOffset( self ):
    return cmds.rowColumnLayout( self.uiName , q=1 , columnOffset=1 )
  def getcolumnSpacing( self ):
    return cmds.rowColumnLayout( self.uiName , q=1 , columnSpacing=1 )
  def getcolumnWidth( self ):
    return cmds.rowColumnLayout( self.uiName , q=1 , columnWidth=1 )
  def getnumberOfColumns( self ):
    return cmds.rowColumnLayout( self.uiName , q=1 , numberOfColumns=1 )
  def getnumberOfRows( self ):
    return cmds.rowColumnLayout( self.uiName , q=1 , numberOfRows=1 )
  def getrowAlign( self ):
    return cmds.rowColumnLayout( self.uiName , q=1 , rowAlign=1 )
  def getrowAttach( self ):
    return cmds.rowColumnLayout( self.uiName , q=1 , rowAttach=1 )
  def getrowHeight( self ):
    return cmds.rowColumnLayout( self.uiName , q=1 , rowHeight=1 )
  def getrowOffset( self ):
    return cmds.rowColumnLayout( self.uiName , q=1 , rowOffset=1 )
  def getrowSpacing( self ):
    return cmds.rowColumnLayout( self.uiName , q=1 , rowSpacing=1 )

  ##### setFuncCode #####
  def setcolumnAlign( self , value ):
    cmds.rowColumnLayout( self.uiName , e=1 , columnAlign=value )
  def setcolumnAttach( self , value ):
    cmds.rowColumnLayout( self.uiName , e=1 , columnAttach=value )
  def setcolumnOffset( self , value ):
    cmds.rowColumnLayout( self.uiName , e=1 , columnOffset=value )
  def setcolumnSpacing( self , value ):
    cmds.rowColumnLayout( self.uiName , e=1 , columnSpacing=value )
  def setcolumnWidth( self , value ):
    cmds.rowColumnLayout( self.uiName , e=1 , columnWidth=value )
  def setnumberOfColumns( self , value ):
    cmds.rowColumnLayout( self.uiName , e=1 , numberOfColumns=value )
  def setnumberOfRows( self , value ):
    cmds.rowColumnLayout( self.uiName , e=1 , numberOfRows=value )
  def setrowAlign( self , value ):
    cmds.rowColumnLayout( self.uiName , e=1 , rowAlign=value )
  def setrowAttach( self , value ):
    cmds.rowColumnLayout( self.uiName , e=1 , rowAttach=value )
  def setrowHeight( self , value ):
    cmds.rowColumnLayout( self.uiName , e=1 , rowHeight=value )
  def setrowOffset( self , value ):
    cmds.rowColumnLayout( self.uiName , e=1 , rowOffset=value )
  def setrowSpacing( self , value ):
    cmds.rowColumnLayout( self.uiName , e=1 , rowSpacing=value )

  ##### propertyCode #####
  columnAlign = property( getcolumnAlign , setcolumnAlign )
  columnAttach = property( getcolumnAttach , setcolumnAttach )
  columnOffset = property( getcolumnOffset , setcolumnOffset )
  columnSpacing = property( getcolumnSpacing , setcolumnSpacing )
  columnWidth = property( getcolumnWidth , setcolumnWidth )
  numberOfColumns = property( getnumberOfColumns , setnumberOfColumns )
  numberOfRows = property( getnumberOfRows , setnumberOfRows )
  rowAlign = property( getrowAlign , setrowAlign )
  rowAttach = property( getrowAttach , setrowAttach )
  rowHeight = property( getrowHeight , setrowHeight )
  rowOffset = property( getrowOffset , setrowOffset )
  rowSpacing = property( getrowSpacing , setrowSpacing )

  ##### customCode #####



class RowColumnLayout_Column( RowColumnLayout ):
  def __init__( self , numberOfColumns ):
    self.uiName = cmds.rowColumnLayout( numberOfColumns=numberOfColumns )

class RowColumnLayout_Row( RowColumnLayout ):
  def __init__( self , numberOfRows ):
    self.uiName = cmds.rowColumnLayout( numberOfColumns=numberOfRows )















class RowLayout( Layout ):

  ##### initialize #####
  def __init__( self , adjustableColumn1=None , adjustableColumn2=None , adjustableColumn3=None , adjustableColumn4=None , adjustableColumn5=None , adjustableColumn6=None , adjustableColumn=None , columnAlign=None , columnAttach=None , columnAlign1=None , columnAlign2=None , columnAlign3=None , columnAlign4=None , columnAlign5=None , columnAlign6=None , columnOffset1=None , columnOffset2=None , columnOffset3=None , columnOffset4=None , columnOffset5=None , columnOffset6=None , columnAttach1=None , columnAttach2=None , columnAttach3=None , columnAttach4=None , columnAttach5=None , columnAttach6=None , columnWidth=None , columnWidth1=None , columnWidth2=None , columnWidth3=None , columnWidth4=None , columnWidth5=None , columnWidth6=None , numberOfColumns=None , rowAttach=None , **args ):
    self.uiName = cmds.rowLayout( numberOfColumns=numberOfColumns )

    ##### substitution #####
    if adjustableColumn != None:
      self.adjustableColumn = adjustableColumn
##    if adjustableColumn1 != None:
##      self.adjustableColumn1 = adjustableColumn1
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

    if columnAlign != None:
      self.columnAlign = columnAlign
##    if columnAlign1 != None:
##      self.columnAlign1 = columnAlign1
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

##    if columnOffset1 != None:
##      self.columnOffset1 = columnOffset1
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

    if columnAttach != None:
      self.columnAttach = columnAttach
##    if columnAttach1 != None:
##      self.columnAttach1 = columnAttach1
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

    if columnWidth != None:
      self.columnWidth = columnWidth
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

    if numberOfColumns != None:
      self.numberOfColumns = numberOfColumns

    if rowAttach != None:
      self.rowAttach = rowAttach

  ##### getFuncCode #####
  def getadjustableColumn( self ):
    return cmds.rowLayout( self.uiName , q=1 , adjustableColumn=1 )
##  def getadjustableColumn1( self ):
##    return cmds.rowLayout( self.uiName , q=1 , adjustableColumn1=1 )
##  def getadjustableColumn2( self ):
##    return cmds.rowLayout( self.uiName , q=1 , adjustableColumn2=1 )
##  def getadjustableColumn3( self ):
##    return cmds.rowLayout( self.uiName , q=1 , adjustableColumn3=1 )
##  def getadjustableColumn4( self ):
##    return cmds.rowLayout( self.uiName , q=1 , adjustableColumn4=1 )
##  def getadjustableColumn5( self ):
##    return cmds.rowLayout( self.uiName , q=1 , adjustableColumn5=1 )
##  def getadjustableColumn6( self ):
##    return cmds.rowLayout( self.uiName , q=1 , adjustableColumn6=1 )

  def getcolumnAlign( self ):
    return cmds.rowLayout( self.uiName , q=1 , columnAlign=1 )
##  def getcolumnAlign1( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnAlign1=1 )
##  def getcolumnAlign2( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnAlign2=1 )
##  def getcolumnAlign3( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnAlign3=1 )
##  def getcolumnAlign4( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnAlign4=1 )
##  def getcolumnAlign5( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnAlign5=1 )
##  def getcolumnAlign6( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnAlign6=1 )

##  def getcolumnOffset1( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnOffset1=1 )
##  def getcolumnOffset2( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnOffset2=1 )
##  def getcolumnOffset3( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnOffset3=1 )
##  def getcolumnOffset4( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnOffset4=1 )
##  def getcolumnOffset5( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnOffset5=1 )
##  def getcolumnOffset6( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnOffset6=1 )

  def getcolumnAttach( self ):
    return cmds.rowLayout( self.uiName , q=1 , columnAttach=1 )
##  def getcolumnAttach1( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnAttach1=1 )
##  def getcolumnAttach2( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnAttach2=1 )
##  def getcolumnAttach3( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnAttach3=1 )
##  def getcolumnAttach4( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnAttach4=1 )
##  def getcolumnAttach5( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnAttach5=1 )
##  def getcolumnAttach6( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnAttach6=1 )

  def getcolumnWidth( self ):
    return cmds.rowLayout( self.uiName , q=1 , columnWidth=1 )
##  def getcolumnWidth1( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnWidth1=1 )
##  def getcolumnWidth2( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnWidth2=1 )
##  def getcolumnWidth3( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnWidth3=1 )
##  def getcolumnWidth4( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnWidth4=1 )
##  def getcolumnWidth5( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnWidth5=1 )
##  def getcolumnWidth6( self ):
##    return cmds.rowLayout( self.uiName , q=1 , columnWidth6=1 )

  def getnumberOfColumns( self ):
    return cmds.rowLayout( self.uiName , q=1 , numberOfColumns=1 )

  def getrowAttach( self ):
    return cmds.rowLayout( self.uiName , q=1 , rowAttach=1 )

  ##### setFuncCode #####
  def setadjustableColumn( self , value ):
    cmds.rowLayout( self.uiName , e=1 , adjustableColumn=value )
##  def setadjustableColumn1( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , adjustableColumn1=value )
##  def setadjustableColumn2( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , adjustableColumn2=value )
##  def setadjustableColumn3( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , adjustableColumn3=value )
##  def setadjustableColumn4( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , adjustableColumn4=value )
##  def setadjustableColumn5( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , adjustableColumn5=value )
##  def setadjustableColumn6( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , adjustableColumn6=value )


  def setcolumnAlign( self , value ):
    cmds.rowLayout( self.uiName , e=1 , columnAlign=value )

##  def setcolumnAlign1( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnAlign1=value )
##  def setcolumnAlign2( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnAlign2=value )
##  def setcolumnAlign3( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnAlign3=value )
##  def setcolumnAlign4( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnAlign4=value )
##  def setcolumnAlign5( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnAlign5=value )
##  def setcolumnAlign6( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnAlign6=value )


##  def setcolumnOffset1( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnOffset1=value )
##  def setcolumnOffset2( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnOffset2=value )
##  def setcolumnOffset3( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnOffset3=value )
##  def setcolumnOffset4( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnOffset4=value )
##  def setcolumnOffset5( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnOffset5=value )
##  def setcolumnOffset6( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnOffset6=value )


  def setcolumnAttach( self , value ):
    cmds.rowLayout( self.uiName , e=1 , columnAttach=value )
##  def setcolumnAttach1( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnAttach1=value )
##  def setcolumnAttach2( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnAttach2=value )
##  def setcolumnAttach3( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnAttach3=value )
##  def setcolumnAttach4( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnAttach4=value )
##  def setcolumnAttach5( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnAttach5=value )
##  def setcolumnAttach6( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnAttach6=value )


  def setcolumnWidth( self , value ):
    cmds.rowLayout( self.uiName , e=1 , columnWidth=value )
##  def setcolumnWidth1( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnWidth1=value )
##  def setcolumnWidth2( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnWidth2=value )
##  def setcolumnWidth3( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnWidth3=value )
##  def setcolumnWidth4( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnWidth4=value )
##  def setcolumnWidth5( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnWidth5=value )
##  def setcolumnWidth6( self , value ):
##    cmds.rowLayout( self.uiName , e=1 , columnWidth6=value )

  def setnumberOfColumns( self , value ):
    cmds.rowLayout( self.uiName , e=1 , numberOfColumns=value )

  def setrowAttach( self , value ):
    cmds.rowLayout( self.uiName , e=1 , rowAttach=value )

  ##### propertyCode #####
  adjustableColumn = property( getadjustableColumn , setadjustableColumn )
##  adjustableColumn1 = property( getadjustableColumn1 , setadjustableColumn1 )
##  adjustableColumn2 = property( getadjustableColumn2 , setadjustableColumn2 )
##  adjustableColumn3 = property( getadjustableColumn3 , setadjustableColumn3 )
##  adjustableColumn4 = property( getadjustableColumn4 , setadjustableColumn4 )
##  adjustableColumn5 = property( getadjustableColumn5 , setadjustableColumn5 )
##  adjustableColumn6 = property( getadjustableColumn6 , setadjustableColumn6 )
  columnAlign = property( getcolumnAlign , setcolumnAlign )
##  columnAlign1 = property( getcolumnAlign1 , setcolumnAlign1 )
##  columnAlign2 = property( getcolumnAlign2 , setcolumnAlign2 )
##  columnAlign3 = property( getcolumnAlign3 , setcolumnAlign3 )
##  columnAlign4 = property( getcolumnAlign4 , setcolumnAlign4 )
##  columnAlign5 = property( getcolumnAlign5 , setcolumnAlign5 )
##  columnAlign6 = property( getcolumnAlign6 , setcolumnAlign6 )
##  columnOffset1 = property( getcolumnOffset1 , setcolumnOffset1 )
##  columnOffset2 = property( getcolumnOffset2 , setcolumnOffset2 )
##  columnOffset3 = property( getcolumnOffset3 , setcolumnOffset3 )
##  columnOffset4 = property( getcolumnOffset4 , setcolumnOffset4 )
##  columnOffset5 = property( getcolumnOffset5 , setcolumnOffset5 )
##  columnOffset6 = property( getcolumnOffset6 , setcolumnOffset6 )
  columnAttach = property( getcolumnAttach , setcolumnAttach )
##  columnAttach1 = property( getcolumnAttach1 , setcolumnAttach1 )
##  columnAttach2 = property( getcolumnAttach2 , setcolumnAttach2 )
##  columnAttach3 = property( getcolumnAttach3 , setcolumnAttach3 )
##  columnAttach4 = property( getcolumnAttach4 , setcolumnAttach4 )
##  columnAttach5 = property( getcolumnAttach5 , setcolumnAttach5 )
##  columnAttach6 = property( getcolumnAttach6 , setcolumnAttach6 )
  columnWidth = property( getcolumnWidth , setcolumnWidth )
##  columnWidth1 = property( getcolumnWidth1 , setcolumnWidth1 )
##  columnWidth2 = property( getcolumnWidth2 , setcolumnWidth2 )
##  columnWidth3 = property( getcolumnWidth3 , setcolumnWidth3 )
##  columnWidth4 = property( getcolumnWidth4 , setcolumnWidth4 )
##  columnWidth5 = property( getcolumnWidth5 , setcolumnWidth5 )
##  columnWidth6 = property( getcolumnWidth6 , setcolumnWidth6 )

  numberOfColumns = property( getnumberOfColumns , setnumberOfColumns )

  rowAttach = property( getrowAttach , setrowAttach )

  ##### customCode #####













class ShelfLayout( Layout ):

  ##### initialize #####
  def __init__( self , cellHeight=None , cellWidth=None , cellWidthHeight=None , position=None , style=None , **args ):
    self.uiName = cmds.shelfLayout()

    ##### substitution #####
    if cellHeight != None:
      self.cellHeight = cellHeight
    if cellWidth != None:
      self.cellWidth = cellWidth
    if cellWidthHeight != None:
      self.cellWidthHeight = cellWidthHeight
    if position != None:
      self.position = position
    if style != None:
      self.style = style

  ##### getFuncCode #####
  def getcellHeight( self ):
    return cmds.shelfLayout( self.uiName , q=1 , cellHeight=1 )
  def getcellWidth( self ):
    return cmds.shelfLayout( self.uiName , q=1 , cellWidth=1 )
  def getcellWidthHeight( self ):
    return cmds.shelfLayout( self.uiName , q=1 , cellWidthHeight=1 )
  def getposition( self ):
    return cmds.shelfLayout( self.uiName , q=1 , position=1 )
  def getstyle( self ):
    return cmds.shelfLayout( self.uiName , q=1 , style=1 )

  ##### setFuncCode #####
  def setcellHeight( self , value ):
    cmds.shelfLayout( self.uiName , e=1 , cellHeight=value )
  def setcellWidth( self , value ):
    cmds.shelfLayout( self.uiName , e=1 , cellWidth=value )
  def setcellWidthHeight( self , value ):
    cmds.shelfLayout( self.uiName , e=1 , cellWidthHeight=value )
  def setposition( self , value ):
    cmds.shelfLayout( self.uiName , e=1 , position=value )
  def setstyle( self , value ):
    cmds.shelfLayout( self.uiName , e=1 , style=value )

  ##### propertyCode #####
  cellHeight = property( getcellHeight , setcellHeight )
  cellWidth = property( getcellWidth , setcellWidth )
  cellWidthHeight = property( getcellWidthHeight , setcellWidthHeight )
  position = property( getposition , setposition )
  style = property( getstyle , setstyle )

  ##### customCode #####





class ShelfTabLayout( Layout ):

  ##### initialize #####
  def __init__( self , changeCommand=None , childResizable=None , doubleClickCommand=None , horizontalScrollBarThickness=None , image=None , innerMarginHeight=None , innerMarginWidth=None , imageVisible=None , minChildWidth=None , moveTab=None , preSelectCommand=None , selectCommand=None , scrollable=None , selectTab=None , selectTabIndex=None , tabLabel=None , tabLabelIndex=None , tabsVisible=None , verticalScrollBarThickness=None , **args ):
    self.uiName = cmds.shelfTabLayout()

    ##### substitution #####
    if changeCommand != None:
      self.changeCommand = changeCommand
    if childResizable != None:
      self.childResizable = childResizable
    if doubleClickCommand != None:
      self.doubleClickCommand = doubleClickCommand
    if horizontalScrollBarThickness != None:
      self.horizontalScrollBarThickness = horizontalScrollBarThickness
    if image != None:
      self.image = image
    if innerMarginHeight != None:
      self.innerMarginHeight = innerMarginHeight
    if innerMarginWidth != None:
      self.innerMarginWidth = innerMarginWidth
    if imageVisible != None:
      self.imageVisible = imageVisible
    if minChildWidth != None:
      self.minChildWidth = minChildWidth
    if moveTab != None:
      self.moveTab = moveTab
    if preSelectCommand != None:
      self.preSelectCommand = preSelectCommand
    if selectCommand != None:
      self.selectCommand = selectCommand
    if scrollable != None:
      self.scrollable = scrollable
    if selectTab != None:
      self.selectTab = selectTab
    if selectTabIndex != None:
      self.selectTabIndex = selectTabIndex
    if tabLabel != None:
      self.tabLabel = tabLabel
    if tabLabelIndex != None:
      self.tabLabelIndex = tabLabelIndex
    if tabsVisible != None:
      self.tabsVisible = tabsVisible
    if verticalScrollBarThickness != None:
      self.verticalScrollBarThickness = verticalScrollBarThickness

  ##### getFuncCode #####
  def getchangeCommand( self ):
    return cmds.shelfTabLayout( self.uiName , q=1 , changeCommand=1 )
  def getchildResizable( self ):
    return cmds.shelfTabLayout( self.uiName , q=1 , childResizable=1 )
  def getdoubleClickCommand( self ):
    return cmds.shelfTabLayout( self.uiName , q=1 , doubleClickCommand=1 )
  def gethorizontalScrollBarThickness( self ):
    return cmds.shelfTabLayout( self.uiName , q=1 , horizontalScrollBarThickness=1 )
  def getimage( self ):
    return cmds.shelfTabLayout( self.uiName , q=1 , image=1 )
  def getinnerMarginHeight( self ):
    return cmds.shelfTabLayout( self.uiName , q=1 , innerMarginHeight=1 )
  def getinnerMarginWidth( self ):
    return cmds.shelfTabLayout( self.uiName , q=1 , innerMarginWidth=1 )
  def getimageVisible( self ):
    return cmds.shelfTabLayout( self.uiName , q=1 , imageVisible=1 )
  def getminChildWidth( self ):
    return cmds.shelfTabLayout( self.uiName , q=1 , minChildWidth=1 )
  def getmoveTab( self ):
    return cmds.shelfTabLayout( self.uiName , q=1 , moveTab=1 )
  def getpreSelectCommand( self ):
    return cmds.shelfTabLayout( self.uiName , q=1 , preSelectCommand=1 )
  def getselectCommand( self ):
    return cmds.shelfTabLayout( self.uiName , q=1 , selectCommand=1 )
  def getscrollable( self ):
    return cmds.shelfTabLayout( self.uiName , q=1 , scrollable=1 )
  def getselectTab( self ):
    return cmds.shelfTabLayout( self.uiName , q=1 , selectTab=1 )
  def getselectTabIndex( self ):
    return cmds.shelfTabLayout( self.uiName , q=1 , selectTabIndex=1 )
  def gettabLabel( self ):
    return cmds.shelfTabLayout( self.uiName , q=1 , tabLabel=1 )
  def gettabLabelIndex( self ):
    return cmds.shelfTabLayout( self.uiName , q=1 , tabLabelIndex=1 )
  def gettabsVisible( self ):
    return cmds.shelfTabLayout( self.uiName , q=1 , tabsVisible=1 )
  def getverticalScrollBarThickness( self ):
    return cmds.shelfTabLayout( self.uiName , q=1 , verticalScrollBarThickness=1 )

  ##### setFuncCode #####
  def setchangeCommand( self , value ):
    cmds.shelfTabLayout( self.uiName , e=1 , changeCommand=value )
  def setchildResizable( self , value ):
    cmds.shelfTabLayout( self.uiName , e=1 , childResizable=value )
  def setdoubleClickCommand( self , value ):
    cmds.shelfTabLayout( self.uiName , e=1 , doubleClickCommand=value )
  def sethorizontalScrollBarThickness( self , value ):
    cmds.shelfTabLayout( self.uiName , e=1 , horizontalScrollBarThickness=value )
  def setimage( self , value ):
    cmds.shelfTabLayout( self.uiName , e=1 , image=value )
  def setinnerMarginHeight( self , value ):
    cmds.shelfTabLayout( self.uiName , e=1 , innerMarginHeight=value )
  def setinnerMarginWidth( self , value ):
    cmds.shelfTabLayout( self.uiName , e=1 , innerMarginWidth=value )
  def setimageVisible( self , value ):
    cmds.shelfTabLayout( self.uiName , e=1 , imageVisible=value )
  def setminChildWidth( self , value ):
    cmds.shelfTabLayout( self.uiName , e=1 , minChildWidth=value )
  def setmoveTab( self , value ):
    cmds.shelfTabLayout( self.uiName , e=1 , moveTab=value )
  def setpreSelectCommand( self , value ):
    cmds.shelfTabLayout( self.uiName , e=1 , preSelectCommand=value )
  def setselectCommand( self , value ):
    cmds.shelfTabLayout( self.uiName , e=1 , selectCommand=value )
  def setscrollable( self , value ):
    cmds.shelfTabLayout( self.uiName , e=1 , scrollable=value )
  def setselectTab( self , value ):
    cmds.shelfTabLayout( self.uiName , e=1 , selectTab=value )
  def setselectTabIndex( self , value ):
    cmds.shelfTabLayout( self.uiName , e=1 , selectTabIndex=value )
  def settabLabel( self , value ):
    cmds.shelfTabLayout( self.uiName , e=1 , tabLabel=value )
  def settabLabelIndex( self , value ):
    cmds.shelfTabLayout( self.uiName , e=1 , tabLabelIndex=value )
  def settabsVisible( self , value ):
    cmds.shelfTabLayout( self.uiName , e=1 , tabsVisible=value )
  def setverticalScrollBarThickness( self , value ):
    cmds.shelfTabLayout( self.uiName , e=1 , verticalScrollBarThickness=value )

  ##### propertyCode #####
  changeCommand = property( getchangeCommand , setchangeCommand )
  childResizable = property( getchildResizable , setchildResizable )
  doubleClickCommand = property( getdoubleClickCommand , setdoubleClickCommand )
  horizontalScrollBarThickness = property( gethorizontalScrollBarThickness , sethorizontalScrollBarThickness )
  image = property( getimage , setimage )
  innerMarginHeight = property( getinnerMarginHeight , setinnerMarginHeight )
  innerMarginWidth = property( getinnerMarginWidth , setinnerMarginWidth )
  imageVisible = property( getimageVisible , setimageVisible )
  minChildWidth = property( getminChildWidth , setminChildWidth )
  moveTab = property( getmoveTab , setmoveTab )
  preSelectCommand = property( getpreSelectCommand , setpreSelectCommand )
  selectCommand = property( getselectCommand , setselectCommand )
  scrollable = property( getscrollable , setscrollable )
  selectTab = property( getselectTab , setselectTab )
  selectTabIndex = property( getselectTabIndex , setselectTabIndex )
  tabLabel = property( gettabLabel , settabLabel )
  tabLabelIndex = property( gettabLabelIndex , settabLabelIndex )
  tabsVisible = property( gettabsVisible , settabsVisible )
  verticalScrollBarThickness = property( getverticalScrollBarThickness , setverticalScrollBarThickness )

  ##### customCode #####





















print "MODULE IMPORTED... MYAM_PyLib_mayaUI_layout"