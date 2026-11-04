#-*- coding:UTF-8 -*-

#*******************************************************************************
'''

Tool Name     : MYAM_PyLib_mayaUI_control
Description   : MayaのControlグループに属するUI要素をオブジェクト指向ライクに扱うためのモジュール

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

class Control( object ):

  ##### initialize #####
  def __init__( self , annotation=None , backgroundColor=None , dragCallback=None , dropCallback=None , defineTemplate=None , docTag=None , enable=None , exists=None , height=None , isObscured=None , manage=None , numberOfPopupMenus=None , parent=None , popupMenuArray=None , preventOverride=None , useTemplate=None , visible=None , width=None , **args ):
    self.uiName = cmds.control()

    ##### substitution #####
    if annotation != None:
      self.annotation = annotation
    if backgroundColor != None:
      self.backgroundColor = backgroundColor
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
    return cmds.control( self.uiName , q=1 , annotation=1 )
  def getbackgroundColor( self ):
    return cmds.control( self.uiName , q=1 , backgroundColor=1 )
  def getdragCallback( self ):
    return cmds.control( self.uiName , q=1 , dragCallback=1 )
  def getdropCallback( self ):
    return cmds.control( self.uiName , q=1 , dropCallback=1 )
  def getdefineTemplate( self ):
    return cmds.control( self.uiName , q=1 , defineTemplate=1 )
  def getdocTag( self ):
    return cmds.control( self.uiName , q=1 , docTag=1 )
  def getenable( self ):
    return cmds.control( self.uiName , q=1 , enable=1 )
  def getexists( self ):
    return cmds.control( self.uiName , q=1 , exists=1 )
  def getheight( self ):
    return cmds.control( self.uiName , q=1 , height=1 )
  def getisObscured( self ):
    return cmds.control( self.uiName , q=1 , isObscured=1 )
  def getmanage( self ):
    return cmds.control( self.uiName , q=1 , manage=1 )
  def getnumberOfPopupMenus( self ):
    return cmds.control( self.uiName , q=1 , numberOfPopupMenus=1 )
  def getparent( self ):
    return cmds.control( self.uiName , q=1 , parent=1 )
  def getpopupMenuArray( self ):
    return cmds.control( self.uiName , q=1 , popupMenuArray=1 )
  def getpreventOverride( self ):
    return cmds.control( self.uiName , q=1 , preventOverride=1 )
  def getuseTemplate( self ):
    return cmds.control( self.uiName , q=1 , useTemplate=1 )
  def getvisible( self ):
    return cmds.control( self.uiName , q=1 , visible=1 )
  def getwidth( self ):
    return cmds.control( self.uiName , q=1 , width=1 )

  ##### setFuncCode #####
  def setannotation( self , value ):
    cmds.control( self.uiName , e=1 , annotation=value )
  def setbackgroundColor( self , value ):
    cmds.control( self.uiName , e=1 , backgroundColor=value )
  def setdragCallback( self , value ):
    cmds.control( self.uiName , e=1 , dragCallback=value )
  def setdropCallback( self , value ):
    cmds.control( self.uiName , e=1 , dropCallback=value )
  def setdefineTemplate( self , value ):
    cmds.control( self.uiName , e=1 , defineTemplate=value )
  def setdocTag( self , value ):
    cmds.control( self.uiName , e=1 , docTag=value )
  def setenable( self , value ):
    cmds.control( self.uiName , e=1 , enable=value )
  def setexists( self , value ):
    cmds.control( self.uiName , e=1 , exists=value )
  def setheight( self , value ):
    cmds.control( self.uiName , e=1 , height=value )
  def setisObscured( self , value ):
    cmds.control( self.uiName , e=1 , isObscured=value )
  def setmanage( self , value ):
    cmds.control( self.uiName , e=1 , manage=value )
  def setnumberOfPopupMenus( self , value ):
    cmds.control( self.uiName , e=1 , numberOfPopupMenus=value )
  def setparent( self , value ):
    cmds.control( self.uiName , e=1 , parent=value )
  def setpopupMenuArray( self , value ):
    cmds.control( self.uiName , e=1 , popupMenuArray=value )
  def setpreventOverride( self , value ):
    cmds.control( self.uiName , e=1 , preventOverride=value )
  def setuseTemplate( self , value ):
    cmds.control( self.uiName , e=1 , useTemplate=value )
  def setvisible( self , value ):
    cmds.control( self.uiName , e=1 , visible=value )
  def setwidth( self , value ):
    cmds.control( self.uiName , e=1 , width=value )

  ##### propertyCode #####
  annotation = property( getannotation , setannotation )
  backgroundColor = property( getbackgroundColor , setbackgroundColor )
  dragCallback = property( getdragCallback , setdragCallback )
  dropCallback = property( getdropCallback , setdropCallback )
  defineTemplate = property( getdefineTemplate , setdefineTemplate )
  docTag = property( getdocTag , setdocTag )
  enable = property( getenable , setenable )
  exists = property( getexists , setexists )
  height = property( getheight , setheight )
  isObscured = property( getisObscured , setisObscured )
  manage = property( getmanage , setmanage )
  numberOfPopupMenus = property( getnumberOfPopupMenus , setnumberOfPopupMenus )
  parent = property( getparent , setparent )
  popupMenuArray = property( getpopupMenuArray , setpopupMenuArray )
  preventOverride = property( getpreventOverride , setpreventOverride )
  useTemplate = property( getuseTemplate , setuseTemplate )
  visible = property( getvisible , setvisible )
  width = property( getwidth , setwidth )

  ##### customCode #####





class Button( Control ):

  ##### initialize #####
  def __init__( self , actionIsSubstitute=None , align=None , actOnPress=None , command=None , label=None , recomputeSize=None , **args ):
    self.uiName = cmds.button()

    ##### substitution #####
    if actionIsSubstitute != None:
      self.actionIsSubstitute = actionIsSubstitute
    if align != None:
      self.align = align
    if actOnPress != None:
      self.actOnPress = actOnPress
    if command != None:
      self.command = command
    if label != None:
      self.label = label
    if recomputeSize != None:
      self.recomputeSize = recomputeSize

  ##### getFuncCode #####
  def getactionIsSubstitute( self ):
    return cmds.button( self.uiName , q=1 , actionIsSubstitute=1 )
  def getalign( self ):
    return cmds.button( self.uiName , q=1 , align=1 )
  def getactOnPress( self ):
    return cmds.button( self.uiName , q=1 , actOnPress=1 )
  def getcommand( self ):
    return cmds.button( self.uiName , q=1 , command=1 )
  def getlabel( self ):
    return cmds.button( self.uiName , q=1 , label=1 )
  def getrecomputeSize( self ):
    return cmds.button( self.uiName , q=1 , recomputeSize=1 )

  ##### setFuncCode #####
  def setactionIsSubstitute( self , value ):
    cmds.button( self.uiName , e=1 , actionIsSubstitute=value )
  def setalign( self , value ):
    cmds.button( self.uiName , e=1 , align=value )
  def setactOnPress( self , value ):
    cmds.button( self.uiName , e=1 , actOnPress=value )
  def setcommand( self , value ):
    cmds.button( self.uiName , e=1 , command=value )
  def setlabel( self , value ):
    cmds.button( self.uiName , e=1 , label=value )
  def setrecomputeSize( self , value ):
    cmds.button( self.uiName , e=1 , recomputeSize=value )

  ##### propertyCode #####
  actionIsSubstitute = property( getactionIsSubstitute , setactionIsSubstitute )
  align = property( getalign , setalign )
  actOnPress = property( getactOnPress , setactOnPress )
  command = property( getcommand , setcommand )
  label = property( getlabel , setlabel )
  recomputeSize = property( getrecomputeSize , setrecomputeSize )

  ##### customCode #####





class CheckBox( Control ):

  ##### initialize #####
  def __init__( self , align=None , changeCommand=None , editable=None , label=None , offCommand=None , onCommand=None , recomputeSize=None , value=None , **args ):
    self.uiName = cmds.checkBox()

    ##### substitution #####
    if align != None:
      self.align = align
    if changeCommand != None:
      self.changeCommand = changeCommand
    if editable != None:
      self.editable = editable
    if label != None:
      self.label = label
    if offCommand != None:
      self.offCommand = offCommand
    if onCommand != None:
      self.onCommand = onCommand
    if recomputeSize != None:
      self.recomputeSize = recomputeSize
    if value != None:
      self.value = value

  ##### getFuncCode #####
  def getalign( self ):
    return cmds.checkBox( self.uiName , q=1 , align=1 )
  def getchangeCommand( self ):
    return cmds.checkBox( self.uiName , q=1 , changeCommand=1 )
  def geteditable( self ):
    return cmds.checkBox( self.uiName , q=1 , editable=1 )
  def getlabel( self ):
    return cmds.checkBox( self.uiName , q=1 , label=1 )
  def getoffCommand( self ):
    return cmds.checkBox( self.uiName , q=1 , offCommand=1 )
  def getonCommand( self ):
    return cmds.checkBox( self.uiName , q=1 , onCommand=1 )
  def getrecomputeSize( self ):
    return cmds.checkBox( self.uiName , q=1 , recomputeSize=1 )
  def getvalue( self ):
    return cmds.checkBox( self.uiName , q=1 , value=1 )

  ##### setFuncCode #####
  def setalign( self , value ):
    cmds.checkBox( self.uiName , e=1 , align=value )
  def setchangeCommand( self , value ):
    cmds.checkBox( self.uiName , e=1 , changeCommand=value )
  def seteditable( self , value ):
    cmds.checkBox( self.uiName , e=1 , editable=value )
  def setlabel( self , value ):
    cmds.checkBox( self.uiName , e=1 , label=value )
  def setoffCommand( self , value ):
    cmds.checkBox( self.uiName , e=1 , offCommand=value )
  def setonCommand( self , value ):
    cmds.checkBox( self.uiName , e=1 , onCommand=value )
  def setrecomputeSize( self , value ):
    cmds.checkBox( self.uiName , e=1 , recomputeSize=value )
  def setvalue( self , value ):
    cmds.checkBox( self.uiName , e=1 , value=value )

  ##### propertyCode #####
  align = property( getalign , setalign )
  changeCommand = property( getchangeCommand , setchangeCommand )
  editable = property( geteditable , seteditable )
  label = property( getlabel , setlabel )
  offCommand = property( getoffCommand , setoffCommand )
  onCommand = property( getonCommand , setonCommand )
  recomputeSize = property( getrecomputeSize , setrecomputeSize )
  value = property( getvalue , setvalue )

  ##### customCode #####





class FloatField( Control ):

  ##### initialize #####
  def __init__( self , changeCommand=None , dragCommand=None , enterCommand=None , editable=None , maxValue=None , minValue=None , precision=None , receiveFocusCommand=None , step=None , value=None , **args ):
    self.uiName = cmds.floatField()

    ##### substitution #####
    if changeCommand != None:
      self.changeCommand = changeCommand
    if dragCommand != None:
      self.dragCommand = dragCommand
    if enterCommand != None:
      self.enterCommand = enterCommand
    if editable != None:
      self.editable = editable
    if maxValue != None:
      self.maxValue = maxValue
    if minValue != None:
      self.minValue = minValue
    if precision != None:
      self.precision = precision
    if receiveFocusCommand != None:
      self.receiveFocusCommand = receiveFocusCommand
    if step != None:
      self.step = step
    if value != None:
      self.value = value

  ##### getFuncCode #####
  def getchangeCommand( self ):
    return cmds.floatField( self.uiName , q=1 , changeCommand=1 )
  def getdragCommand( self ):
    return cmds.floatField( self.uiName , q=1 , dragCommand=1 )
  def getenterCommand( self ):
    return cmds.floatField( self.uiName , q=1 , enterCommand=1 )
  def geteditable( self ):
    return cmds.floatField( self.uiName , q=1 , editable=1 )
  def getmaxValue( self ):
    return cmds.floatField( self.uiName , q=1 , maxValue=1 )
  def getminValue( self ):
    return cmds.floatField( self.uiName , q=1 , minValue=1 )
  def getprecision( self ):
    return cmds.floatField( self.uiName , q=1 , precision=1 )
  def getreceiveFocusCommand( self ):
    return cmds.floatField( self.uiName , q=1 , receiveFocusCommand=1 )
  def getstep( self ):
    return cmds.floatField( self.uiName , q=1 , step=1 )
  def getvalue( self ):
    return cmds.floatField( self.uiName , q=1 , value=1 )

  ##### setFuncCode #####
  def setchangeCommand( self , value ):
    cmds.floatField( self.uiName , e=1 , changeCommand=value )
  def setdragCommand( self , value ):
    cmds.floatField( self.uiName , e=1 , dragCommand=value )
  def setenterCommand( self , value ):
    cmds.floatField( self.uiName , e=1 , enterCommand=value )
  def seteditable( self , value ):
    cmds.floatField( self.uiName , e=1 , editable=value )
  def setmaxValue( self , value ):
    cmds.floatField( self.uiName , e=1 , maxValue=value )
  def setminValue( self , value ):
    cmds.floatField( self.uiName , e=1 , minValue=value )
  def setprecision( self , value ):
    cmds.floatField( self.uiName , e=1 , precision=value )
  def setreceiveFocusCommand( self , value ):
    cmds.floatField( self.uiName , e=1 , receiveFocusCommand=value )
  def setstep( self , value ):
    cmds.floatField( self.uiName , e=1 , step=value )
  def setvalue( self , value ):
    cmds.floatField( self.uiName , e=1 , value=value )

  ##### propertyCode #####
  changeCommand = property( getchangeCommand , setchangeCommand )
  dragCommand = property( getdragCommand , setdragCommand )
  enterCommand = property( getenterCommand , setenterCommand )
  editable = property( geteditable , seteditable )
  maxValue = property( getmaxValue , setmaxValue )
  minValue = property( getminValue , setminValue )
  precision = property( getprecision , setprecision )
  receiveFocusCommand = property( getreceiveFocusCommand , setreceiveFocusCommand )
  step = property( getstep , setstep )
  value = property( getvalue , setvalue )

  ##### customCode #####





class FloatSlider( Control ):

  ##### initialize #####
  def __init__( self , changeCommand=None , dragCommand=None , horizontal=None , maxValue=None , minValue=None , step=None , value=None , **args ):
    self.uiName = cmds.floatSlider()

    ##### substitution #####
    if changeCommand != None:
      self.changeCommand = changeCommand
    if dragCommand != None:
      self.dragCommand = dragCommand
    if horizontal != None:
      self.horizontal = horizontal
    if maxValue != None:
      self.maxValue = maxValue
    if minValue != None:
      self.minValue = minValue
    if step != None:
      self.step = step
    if value != None:
      self.value = value

  ##### getFuncCode #####
  def getchangeCommand( self ):
    return cmds.floatSlider( self.uiName , q=1 , changeCommand=1 )
  def getdragCommand( self ):
    return cmds.floatSlider( self.uiName , q=1 , dragCommand=1 )
  def gethorizontal( self ):
    return cmds.floatSlider( self.uiName , q=1 , horizontal=1 )
  def getmaxValue( self ):
    return cmds.floatSlider( self.uiName , q=1 , maxValue=1 )
  def getminValue( self ):
    return cmds.floatSlider( self.uiName , q=1 , minValue=1 )
  def getstep( self ):
    return cmds.floatSlider( self.uiName , q=1 , step=1 )
  def getvalue( self ):
    return cmds.floatSlider( self.uiName , q=1 , value=1 )

  ##### setFuncCode #####
  def setchangeCommand( self , value ):
    cmds.floatSlider( self.uiName , e=1 , changeCommand=value )
  def setdragCommand( self , value ):
    cmds.floatSlider( self.uiName , e=1 , dragCommand=value )
  def sethorizontal( self , value ):
    cmds.floatSlider( self.uiName , e=1 , horizontal=value )
  def setmaxValue( self , value ):
    cmds.floatSlider( self.uiName , e=1 , maxValue=value )
  def setminValue( self , value ):
    cmds.floatSlider( self.uiName , e=1 , minValue=value )
  def setstep( self , value ):
    cmds.floatSlider( self.uiName , e=1 , step=value )
  def setvalue( self , value ):
    cmds.floatSlider( self.uiName , e=1 , value=value )

  ##### propertyCode #####
  changeCommand = property( getchangeCommand , setchangeCommand )
  dragCommand = property( getdragCommand , setdragCommand )
  horizontal = property( gethorizontal , sethorizontal )
  maxValue = property( getmaxValue , setmaxValue )
  minValue = property( getminValue , setminValue )
  step = property( getstep , setstep )
  value = property( getvalue , setvalue )

  ##### customCode #####





class FloatSlider2( Control ):

  ##### initialize #####
  def __init__( self , changeCommand1=None , changeCommand2=None , maximum=None , minimum=None , positionControl1=None , positionControl2=None , polarity=None , value1=None , value2=None , values=None , **args ):
    self.uiName = cmds.floatSlider2()

    ##### substitution #####
    if changeCommand1 != None:
      self.changeCommand1 = changeCommand1
    if changeCommand2 != None:
      self.changeCommand2 = changeCommand2
    if maximum != None:
      self.maximum = maximum
    if minimum != None:
      self.minimum = minimum
    if positionControl1 != None:
      self.positionControl1 = positionControl1
    if positionControl2 != None:
      self.positionControl2 = positionControl2
    if polarity != None:
      self.polarity = polarity
    if value1 != None:
      self.value1 = value1
    if value2 != None:
      self.value2 = value2
    if values != None:
      self.values = values

  ##### getFuncCode #####
  def getchangeCommand1( self ):
    return cmds.floatSlider2( self.uiName , q=1 , changeCommand1=1 )
  def getchangeCommand2( self ):
    return cmds.floatSlider2( self.uiName , q=1 , changeCommand2=1 )
  def getmaximum( self ):
    return cmds.floatSlider2( self.uiName , q=1 , maximum=1 )
  def getminimum( self ):
    return cmds.floatSlider2( self.uiName , q=1 , minimum=1 )
  def getpositionControl1( self ):
    return cmds.floatSlider2( self.uiName , q=1 , positionControl1=1 )
  def getpositionControl2( self ):
    return cmds.floatSlider2( self.uiName , q=1 , positionControl2=1 )
  def getpolarity( self ):
    return cmds.floatSlider2( self.uiName , q=1 , polarity=1 )
  def getvalue1( self ):
    return cmds.floatSlider2( self.uiName , q=1 , value1=1 )
  def getvalue2( self ):
    return cmds.floatSlider2( self.uiName , q=1 , value2=1 )
  def getvalues( self ):
    return cmds.floatSlider2( self.uiName , q=1 , values=1 )

  ##### setFuncCode #####
  def setchangeCommand1( self , value ):
    cmds.floatSlider2( self.uiName , e=1 , changeCommand1=value )
  def setchangeCommand2( self , value ):
    cmds.floatSlider2( self.uiName , e=1 , changeCommand2=value )
  def setmaximum( self , value ):
    cmds.floatSlider2( self.uiName , e=1 , maximum=value )
  def setminimum( self , value ):
    cmds.floatSlider2( self.uiName , e=1 , minimum=value )
  def setpositionControl1( self , value ):
    cmds.floatSlider2( self.uiName , e=1 , positionControl1=value )
  def setpositionControl2( self , value ):
    cmds.floatSlider2( self.uiName , e=1 , positionControl2=value )
  def setpolarity( self , value ):
    cmds.floatSlider2( self.uiName , e=1 , polarity=value )
  def setvalue1( self , value ):
    cmds.floatSlider2( self.uiName , e=1 , value1=value )
  def setvalue2( self , value ):
    cmds.floatSlider2( self.uiName , e=1 , value2=value )
  def setvalues( self , value ):
    cmds.floatSlider2( self.uiName , e=1 , values=value )

  ##### propertyCode #####
  changeCommand1 = property( getchangeCommand1 , setchangeCommand1 )
  changeCommand2 = property( getchangeCommand2 , setchangeCommand2 )
  maximum = property( getmaximum , setmaximum )
  minimum = property( getminimum , setminimum )
  positionControl1 = property( getpositionControl1 , setpositionControl1 )
  positionControl2 = property( getpositionControl2 , setpositionControl2 )
  polarity = property( getpolarity , setpolarity )
  value1 = property( getvalue1 , setvalue1 )
  value2 = property( getvalue2 , setvalue2 )
  values = property( getvalues , setvalues )

  ##### customCode #####





class IconTextButton( Control ):

  ##### initialize #####
  def __init__( self , actionIsSubstitute=None , align=None , command=None , doubleClickCommand=None , disabledImage=None , font=None , highlightImage=None , handleNodeDropCallback=None , image=None , image1=None , image2=None , image3=None , imageOverlayLabel=None , label=None , labelEditingCallback=None , labelOffset=None , marginHeight=None , marginWidth=None , commandRepeatable=None , selectionImage=None , style=None , sourceType=None , **args ):
    self.uiName = cmds.iconTextButton()

    ##### substitution #####
    if actionIsSubstitute != None:
      self.actionIsSubstitute = actionIsSubstitute
    if align != None:
      self.align = align
    if command != None:
      self.command = command
    if doubleClickCommand != None:
      self.doubleClickCommand = doubleClickCommand
    if disabledImage != None:
      self.disabledImage = disabledImage
    if font != None:
      self.font = font
    if highlightImage != None:
      self.highlightImage = highlightImage
    if handleNodeDropCallback != None:
      self.handleNodeDropCallback = handleNodeDropCallback
    if image != None:
      self.image = image
    if image1 != None:
      self.image1 = image1
    if image2 != None:
      self.image2 = image2
    if image3 != None:
      self.image3 = image3
    if imageOverlayLabel != None:
      self.imageOverlayLabel = imageOverlayLabel
    if label != None:
      self.label = label
    if labelEditingCallback != None:
      self.labelEditingCallback = labelEditingCallback
    if labelOffset != None:
      self.labelOffset = labelOffset
    if marginHeight != None:
      self.marginHeight = marginHeight
    if marginWidth != None:
      self.marginWidth = marginWidth
    if commandRepeatable != None:
      self.commandRepeatable = commandRepeatable
    if selectionImage != None:
      self.selectionImage = selectionImage
    if style != None:
      self.style = style
    if sourceType != None:
      self.sourceType = sourceType

  ##### getFuncCode #####
  def getactionIsSubstitute( self ):
    return cmds.iconTextButton( self.uiName , q=1 , actionIsSubstitute=1 )
  def getalign( self ):
    return cmds.iconTextButton( self.uiName , q=1 , align=1 )
  def getcommand( self ):
    return cmds.iconTextButton( self.uiName , q=1 , command=1 )
  def getdoubleClickCommand( self ):
    return cmds.iconTextButton( self.uiName , q=1 , doubleClickCommand=1 )
  def getdisabledImage( self ):
    return cmds.iconTextButton( self.uiName , q=1 , disabledImage=1 )
  def getfont( self ):
    return cmds.iconTextButton( self.uiName , q=1 , font=1 )
  def gethighlightImage( self ):
    return cmds.iconTextButton( self.uiName , q=1 , highlightImage=1 )
  def gethandleNodeDropCallback( self ):
    return cmds.iconTextButton( self.uiName , q=1 , handleNodeDropCallback=1 )
  def getimage( self ):
    return cmds.iconTextButton( self.uiName , q=1 , image=1 )
  def getimage1( self ):
    return cmds.iconTextButton( self.uiName , q=1 , image1=1 )
  def getimage2( self ):
    return cmds.iconTextButton( self.uiName , q=1 , image2=1 )
  def getimage3( self ):
    return cmds.iconTextButton( self.uiName , q=1 , image3=1 )
  def getimageOverlayLabel( self ):
    return cmds.iconTextButton( self.uiName , q=1 , imageOverlayLabel=1 )
  def getlabel( self ):
    return cmds.iconTextButton( self.uiName , q=1 , label=1 )
  def getlabelEditingCallback( self ):
    return cmds.iconTextButton( self.uiName , q=1 , labelEditingCallback=1 )
  def getlabelOffset( self ):
    return cmds.iconTextButton( self.uiName , q=1 , labelOffset=1 )
  def getmarginHeight( self ):
    return cmds.iconTextButton( self.uiName , q=1 , marginHeight=1 )
  def getmarginWidth( self ):
    return cmds.iconTextButton( self.uiName , q=1 , marginWidth=1 )
  def getcommandRepeatable( self ):
    return cmds.iconTextButton( self.uiName , q=1 , commandRepeatable=1 )
  def getselectionImage( self ):
    return cmds.iconTextButton( self.uiName , q=1 , selectionImage=1 )
  def getstyle( self ):
    return cmds.iconTextButton( self.uiName , q=1 , style=1 )
  def getsourceType( self ):
    return cmds.iconTextButton( self.uiName , q=1 , sourceType=1 )

  ##### setFuncCode #####
  def setactionIsSubstitute( self , value ):
    cmds.iconTextButton( self.uiName , e=1 , actionIsSubstitute=value )
  def setalign( self , value ):
    cmds.iconTextButton( self.uiName , e=1 , align=value )
  def setcommand( self , value ):
    cmds.iconTextButton( self.uiName , e=1 , command=value )
  def setdoubleClickCommand( self , value ):
    cmds.iconTextButton( self.uiName , e=1 , doubleClickCommand=value )
  def setdisabledImage( self , value ):
    cmds.iconTextButton( self.uiName , e=1 , disabledImage=value )
  def setfont( self , value ):
    cmds.iconTextButton( self.uiName , e=1 , font=value )
  def sethighlightImage( self , value ):
    cmds.iconTextButton( self.uiName , e=1 , highlightImage=value )
  def sethandleNodeDropCallback( self , value ):
    cmds.iconTextButton( self.uiName , e=1 , handleNodeDropCallback=value )
  def setimage( self , value ):
    cmds.iconTextButton( self.uiName , e=1 , image=value )
  def setimage1( self , value ):
    cmds.iconTextButton( self.uiName , e=1 , image1=value )
  def setimage2( self , value ):
    cmds.iconTextButton( self.uiName , e=1 , image2=value )
  def setimage3( self , value ):
    cmds.iconTextButton( self.uiName , e=1 , image3=value )
  def setimageOverlayLabel( self , value ):
    cmds.iconTextButton( self.uiName , e=1 , imageOverlayLabel=value )
  def setlabel( self , value ):
    cmds.iconTextButton( self.uiName , e=1 , label=value )
  def setlabelEditingCallback( self , value ):
    cmds.iconTextButton( self.uiName , e=1 , labelEditingCallback=value )
  def setlabelOffset( self , value ):
    cmds.iconTextButton( self.uiName , e=1 , labelOffset=value )
  def setmarginHeight( self , value ):
    cmds.iconTextButton( self.uiName , e=1 , marginHeight=value )
  def setmarginWidth( self , value ):
    cmds.iconTextButton( self.uiName , e=1 , marginWidth=value )
  def setcommandRepeatable( self , value ):
    cmds.iconTextButton( self.uiName , e=1 , commandRepeatable=value )
  def setselectionImage( self , value ):
    cmds.iconTextButton( self.uiName , e=1 , selectionImage=value )
  def setstyle( self , value ):
    cmds.iconTextButton( self.uiName , e=1 , style=value )
  def setsourceType( self , value ):
    cmds.iconTextButton( self.uiName , e=1 , sourceType=value )

  ##### propertyCode #####
  actionIsSubstitute = property( getactionIsSubstitute , setactionIsSubstitute )
  align = property( getalign , setalign )
  command = property( getcommand , setcommand )
  doubleClickCommand = property( getdoubleClickCommand , setdoubleClickCommand )
  disabledImage = property( getdisabledImage , setdisabledImage )
  font = property( getfont , setfont )
  highlightImage = property( gethighlightImage , sethighlightImage )
  handleNodeDropCallback = property( gethandleNodeDropCallback , sethandleNodeDropCallback )
  image = property( getimage , setimage )
  image1 = property( getimage1 , setimage1 )
  image2 = property( getimage2 , setimage2 )
  image3 = property( getimage3 , setimage3 )
  imageOverlayLabel = property( getimageOverlayLabel , setimageOverlayLabel )
  label = property( getlabel , setlabel )
  labelEditingCallback = property( getlabelEditingCallback , setlabelEditingCallback )
  labelOffset = property( getlabelOffset , setlabelOffset )
  marginHeight = property( getmarginHeight , setmarginHeight )
  marginWidth = property( getmarginWidth , setmarginWidth )
  commandRepeatable = property( getcommandRepeatable , setcommandRepeatable )
  selectionImage = property( getselectionImage , setselectionImage )
  style = property( getstyle , setstyle )
  sourceType = property( getsourceType , setsourceType )

  ##### customCode #####





class IconTextCheckBox( Control ):

  ##### initialize #####
  def __init__( self , align=None , changeCommand=None , disabledImage=None , font=None , highlightImage=None , image=None , image1=None , image2=None , image3=None , imageOverlayLabel=None , label=None , labelOffset=None , marginHeight=None , marginWidth=None , offCommand=None , onCommand=None , selectionHighlightImage=None , selectionImage=None , style=None , value=None , **args ):
    self.uiName = cmds.iconTextCheckBox()

    ##### substitution #####
    if align != None:
      self.align = align
    if changeCommand != None:
      self.changeCommand = changeCommand
    if disabledImage != None:
      self.disabledImage = disabledImage
    if font != None:
      self.font = font
    if highlightImage != None:
      self.highlightImage = highlightImage
    if image != None:
      self.image = image
    if image1 != None:
      self.image1 = image1
    if image2 != None:
      self.image2 = image2
    if image3 != None:
      self.image3 = image3
    if imageOverlayLabel != None:
      self.imageOverlayLabel = imageOverlayLabel
    if label != None:
      self.label = label
    if labelOffset != None:
      self.labelOffset = labelOffset
    if marginHeight != None:
      self.marginHeight = marginHeight
    if marginWidth != None:
      self.marginWidth = marginWidth
    if offCommand != None:
      self.offCommand = offCommand
    if onCommand != None:
      self.onCommand = onCommand
    if selectionHighlightImage != None:
      self.selectionHighlightImage = selectionHighlightImage
    if selectionImage != None:
      self.selectionImage = selectionImage
    if style != None:
      self.style = style
    if value != None:
      self.value = value

  ##### getFuncCode #####
  def getalign( self ):
    return cmds.iconTextCheckBox( self.uiName , q=1 , align=1 )
  def getchangeCommand( self ):
    return cmds.iconTextCheckBox( self.uiName , q=1 , changeCommand=1 )
  def getdisabledImage( self ):
    return cmds.iconTextCheckBox( self.uiName , q=1 , disabledImage=1 )
  def getfont( self ):
    return cmds.iconTextCheckBox( self.uiName , q=1 , font=1 )
  def gethighlightImage( self ):
    return cmds.iconTextCheckBox( self.uiName , q=1 , highlightImage=1 )
  def getimage( self ):
    return cmds.iconTextCheckBox( self.uiName , q=1 , image=1 )
  def getimage1( self ):
    return cmds.iconTextCheckBox( self.uiName , q=1 , image1=1 )
  def getimage2( self ):
    return cmds.iconTextCheckBox( self.uiName , q=1 , image2=1 )
  def getimage3( self ):
    return cmds.iconTextCheckBox( self.uiName , q=1 , image3=1 )
  def getimageOverlayLabel( self ):
    return cmds.iconTextCheckBox( self.uiName , q=1 , imageOverlayLabel=1 )
  def getlabel( self ):
    return cmds.iconTextCheckBox( self.uiName , q=1 , label=1 )
  def getlabelOffset( self ):
    return cmds.iconTextCheckBox( self.uiName , q=1 , labelOffset=1 )
  def getmarginHeight( self ):
    return cmds.iconTextCheckBox( self.uiName , q=1 , marginHeight=1 )
  def getmarginWidth( self ):
    return cmds.iconTextCheckBox( self.uiName , q=1 , marginWidth=1 )
  def getoffCommand( self ):
    return cmds.iconTextCheckBox( self.uiName , q=1 , offCommand=1 )
  def getonCommand( self ):
    return cmds.iconTextCheckBox( self.uiName , q=1 , onCommand=1 )
  def getselectionHighlightImage( self ):
    return cmds.iconTextCheckBox( self.uiName , q=1 , selectionHighlightImage=1 )
  def getselectionImage( self ):
    return cmds.iconTextCheckBox( self.uiName , q=1 , selectionImage=1 )
  def getstyle( self ):
    return cmds.iconTextCheckBox( self.uiName , q=1 , style=1 )
  def getvalue( self ):
    return cmds.iconTextCheckBox( self.uiName , q=1 , value=1 )

  ##### setFuncCode #####
  def setalign( self , value ):
    cmds.iconTextCheckBox( self.uiName , e=1 , align=value )
  def setchangeCommand( self , value ):
    cmds.iconTextCheckBox( self.uiName , e=1 , changeCommand=value )
  def setdisabledImage( self , value ):
    cmds.iconTextCheckBox( self.uiName , e=1 , disabledImage=value )
  def setfont( self , value ):
    cmds.iconTextCheckBox( self.uiName , e=1 , font=value )
  def sethighlightImage( self , value ):
    cmds.iconTextCheckBox( self.uiName , e=1 , highlightImage=value )
  def setimage( self , value ):
    cmds.iconTextCheckBox( self.uiName , e=1 , image=value )
  def setimage1( self , value ):
    cmds.iconTextCheckBox( self.uiName , e=1 , image1=value )
  def setimage2( self , value ):
    cmds.iconTextCheckBox( self.uiName , e=1 , image2=value )
  def setimage3( self , value ):
    cmds.iconTextCheckBox( self.uiName , e=1 , image3=value )
  def setimageOverlayLabel( self , value ):
    cmds.iconTextCheckBox( self.uiName , e=1 , imageOverlayLabel=value )
  def setlabel( self , value ):
    cmds.iconTextCheckBox( self.uiName , e=1 , label=value )
  def setlabelOffset( self , value ):
    cmds.iconTextCheckBox( self.uiName , e=1 , labelOffset=value )
  def setmarginHeight( self , value ):
    cmds.iconTextCheckBox( self.uiName , e=1 , marginHeight=value )
  def setmarginWidth( self , value ):
    cmds.iconTextCheckBox( self.uiName , e=1 , marginWidth=value )
  def setoffCommand( self , value ):
    cmds.iconTextCheckBox( self.uiName , e=1 , offCommand=value )
  def setonCommand( self , value ):
    cmds.iconTextCheckBox( self.uiName , e=1 , onCommand=value )
  def setselectionHighlightImage( self , value ):
    cmds.iconTextCheckBox( self.uiName , e=1 , selectionHighlightImage=value )
  def setselectionImage( self , value ):
    cmds.iconTextCheckBox( self.uiName , e=1 , selectionImage=value )
  def setstyle( self , value ):
    cmds.iconTextCheckBox( self.uiName , e=1 , style=value )
  def setvalue( self , value ):
    cmds.iconTextCheckBox( self.uiName , e=1 , value=value )

  ##### propertyCode #####
  align = property( getalign , setalign )
  changeCommand = property( getchangeCommand , setchangeCommand )
  disabledImage = property( getdisabledImage , setdisabledImage )
  font = property( getfont , setfont )
  highlightImage = property( gethighlightImage , sethighlightImage )
  image = property( getimage , setimage )
  image1 = property( getimage1 , setimage1 )
  image2 = property( getimage2 , setimage2 )
  image3 = property( getimage3 , setimage3 )
  imageOverlayLabel = property( getimageOverlayLabel , setimageOverlayLabel )
  label = property( getlabel , setlabel )
  labelOffset = property( getlabelOffset , setlabelOffset )
  marginHeight = property( getmarginHeight , setmarginHeight )
  marginWidth = property( getmarginWidth , setmarginWidth )
  offCommand = property( getoffCommand , setoffCommand )
  onCommand = property( getonCommand , setonCommand )
  selectionHighlightImage = property( getselectionHighlightImage , setselectionHighlightImage )
  selectionImage = property( getselectionImage , setselectionImage )
  style = property( getstyle , setstyle )
  value = property( getvalue , setvalue )

  ##### customCode #####





class IconTextRadioButton( Control ):

  ##### initialize #####
  def __init__( self , align=None , changeCommand=None , collection=None , disabledImage=None , font=None , highlightImage=None , image=None , image1=None , image2=None , image3=None , imageOverlayLabel=None , label=None , labelOffset=None , marginHeight=None , marginWidth=None , offCommand=None , onCommand=None , selectionHighlightImage=None , selectionImage=None , select=None , style=None , **args ):
    self.uiName = cmds.iconTextRadioButton()

    ##### substitution #####
    if align != None:
      self.align = align
    if changeCommand != None:
      self.changeCommand = changeCommand
    if collection != None:
      self.collection = collection
    if disabledImage != None:
      self.disabledImage = disabledImage
    if font != None:
      self.font = font
    if highlightImage != None:
      self.highlightImage = highlightImage
    if image != None:
      self.image = image
    if image1 != None:
      self.image1 = image1
    if image2 != None:
      self.image2 = image2
    if image3 != None:
      self.image3 = image3
    if imageOverlayLabel != None:
      self.imageOverlayLabel = imageOverlayLabel
    if label != None:
      self.label = label
    if labelOffset != None:
      self.labelOffset = labelOffset
    if marginHeight != None:
      self.marginHeight = marginHeight
    if marginWidth != None:
      self.marginWidth = marginWidth
    if offCommand != None:
      self.offCommand = offCommand
    if onCommand != None:
      self.onCommand = onCommand
    if selectionHighlightImage != None:
      self.selectionHighlightImage = selectionHighlightImage
    if selectionImage != None:
      self.selectionImage = selectionImage
    if select != None:
      self.select = select
    if style != None:
      self.style = style

  ##### getFuncCode #####
  def getalign( self ):
    return cmds.iconTextRadioButton( self.uiName , q=1 , align=1 )
  def getchangeCommand( self ):
    return cmds.iconTextRadioButton( self.uiName , q=1 , changeCommand=1 )
  def getcollection( self ):
    return cmds.iconTextRadioButton( self.uiName , q=1 , collection=1 )
  def getdisabledImage( self ):
    return cmds.iconTextRadioButton( self.uiName , q=1 , disabledImage=1 )
  def getfont( self ):
    return cmds.iconTextRadioButton( self.uiName , q=1 , font=1 )
  def gethighlightImage( self ):
    return cmds.iconTextRadioButton( self.uiName , q=1 , highlightImage=1 )
  def getimage( self ):
    return cmds.iconTextRadioButton( self.uiName , q=1 , image=1 )
  def getimage1( self ):
    return cmds.iconTextRadioButton( self.uiName , q=1 , image1=1 )
  def getimage2( self ):
    return cmds.iconTextRadioButton( self.uiName , q=1 , image2=1 )
  def getimage3( self ):
    return cmds.iconTextRadioButton( self.uiName , q=1 , image3=1 )
  def getimageOverlayLabel( self ):
    return cmds.iconTextRadioButton( self.uiName , q=1 , imageOverlayLabel=1 )
  def getlabel( self ):
    return cmds.iconTextRadioButton( self.uiName , q=1 , label=1 )
  def getlabelOffset( self ):
    return cmds.iconTextRadioButton( self.uiName , q=1 , labelOffset=1 )
  def getmarginHeight( self ):
    return cmds.iconTextRadioButton( self.uiName , q=1 , marginHeight=1 )
  def getmarginWidth( self ):
    return cmds.iconTextRadioButton( self.uiName , q=1 , marginWidth=1 )
  def getoffCommand( self ):
    return cmds.iconTextRadioButton( self.uiName , q=1 , offCommand=1 )
  def getonCommand( self ):
    return cmds.iconTextRadioButton( self.uiName , q=1 , onCommand=1 )
  def getselectionHighlightImage( self ):
    return cmds.iconTextRadioButton( self.uiName , q=1 , selectionHighlightImage=1 )
  def getselectionImage( self ):
    return cmds.iconTextRadioButton( self.uiName , q=1 , selectionImage=1 )
  def getselect( self ):
    return cmds.iconTextRadioButton( self.uiName , q=1 , select=1 )
  def getstyle( self ):
    return cmds.iconTextRadioButton( self.uiName , q=1 , style=1 )

  ##### setFuncCode #####
  def setalign( self , value ):
    cmds.iconTextRadioButton( self.uiName , e=1 , align=value )
  def setchangeCommand( self , value ):
    cmds.iconTextRadioButton( self.uiName , e=1 , changeCommand=value )
  def setcollection( self , value ):
    cmds.iconTextRadioButton( self.uiName , e=1 , collection=value )
  def setdisabledImage( self , value ):
    cmds.iconTextRadioButton( self.uiName , e=1 , disabledImage=value )
  def setfont( self , value ):
    cmds.iconTextRadioButton( self.uiName , e=1 , font=value )
  def sethighlightImage( self , value ):
    cmds.iconTextRadioButton( self.uiName , e=1 , highlightImage=value )
  def setimage( self , value ):
    cmds.iconTextRadioButton( self.uiName , e=1 , image=value )
  def setimage1( self , value ):
    cmds.iconTextRadioButton( self.uiName , e=1 , image1=value )
  def setimage2( self , value ):
    cmds.iconTextRadioButton( self.uiName , e=1 , image2=value )
  def setimage3( self , value ):
    cmds.iconTextRadioButton( self.uiName , e=1 , image3=value )
  def setimageOverlayLabel( self , value ):
    cmds.iconTextRadioButton( self.uiName , e=1 , imageOverlayLabel=value )
  def setlabel( self , value ):
    cmds.iconTextRadioButton( self.uiName , e=1 , label=value )
  def setlabelOffset( self , value ):
    cmds.iconTextRadioButton( self.uiName , e=1 , labelOffset=value )
  def setmarginHeight( self , value ):
    cmds.iconTextRadioButton( self.uiName , e=1 , marginHeight=value )
  def setmarginWidth( self , value ):
    cmds.iconTextRadioButton( self.uiName , e=1 , marginWidth=value )
  def setoffCommand( self , value ):
    cmds.iconTextRadioButton( self.uiName , e=1 , offCommand=value )
  def setonCommand( self , value ):
    cmds.iconTextRadioButton( self.uiName , e=1 , onCommand=value )
  def setselectionHighlightImage( self , value ):
    cmds.iconTextRadioButton( self.uiName , e=1 , selectionHighlightImage=value )
  def setselectionImage( self , value ):
    cmds.iconTextRadioButton( self.uiName , e=1 , selectionImage=value )
  def setselect( self , value ):
    cmds.iconTextRadioButton( self.uiName , e=1 , select=value )
  def setstyle( self , value ):
    cmds.iconTextRadioButton( self.uiName , e=1 , style=value )

  ##### propertyCode #####
  align = property( getalign , setalign )
  changeCommand = property( getchangeCommand , setchangeCommand )
  collection = property( getcollection , setcollection )
  disabledImage = property( getdisabledImage , setdisabledImage )
  font = property( getfont , setfont )
  highlightImage = property( gethighlightImage , sethighlightImage )
  image = property( getimage , setimage )
  image1 = property( getimage1 , setimage1 )
  image2 = property( getimage2 , setimage2 )
  image3 = property( getimage3 , setimage3 )
  imageOverlayLabel = property( getimageOverlayLabel , setimageOverlayLabel )
  label = property( getlabel , setlabel )
  labelOffset = property( getlabelOffset , setlabelOffset )
  marginHeight = property( getmarginHeight , setmarginHeight )
  marginWidth = property( getmarginWidth , setmarginWidth )
  offCommand = property( getoffCommand , setoffCommand )
  onCommand = property( getonCommand , setonCommand )
  selectionHighlightImage = property( getselectionHighlightImage , setselectionHighlightImage )
  selectionImage = property( getselectionImage , setselectionImage )
  select = property( getselect , setselect )
  style = property( getstyle , setstyle )

  ##### customCode #####





class IconTextRadioCollection( Control ):

  ##### initialize #####
  def __init__( self , collectionItemArray=None , disableCommands=None , gl=None , numberOfCollectionItems=None , select=None , **args ):
    self.uiName = cmds.iconTextRadioCollection()

    ##### substitution #####
    if collectionItemArray != None:
      self.collectionItemArray = collectionItemArray
    if disableCommands != None:
      self.disableCommands = disableCommands
    if gl != None:
      self.gl = gl
    if numberOfCollectionItems != None:
      self.numberOfCollectionItems = numberOfCollectionItems
    if select != None:
      self.select = select

  ##### getFuncCode #####
  def getcollectionItemArray( self ):
    return cmds.iconTextRadioCollection( self.uiName , q=1 , collectionItemArray=1 )
  def getdisableCommands( self ):
    return cmds.iconTextRadioCollection( self.uiName , q=1 , disableCommands=1 )
  def getgl( self ):
    return cmds.iconTextRadioCollection( self.uiName , q=1 , gl=1 )
  def getnumberOfCollectionItems( self ):
    return cmds.iconTextRadioCollection( self.uiName , q=1 , numberOfCollectionItems=1 )
  def getselect( self ):
    return cmds.iconTextRadioCollection( self.uiName , q=1 , select=1 )

  ##### setFuncCode #####
  def setcollectionItemArray( self , value ):
    cmds.iconTextRadioCollection( self.uiName , e=1 , collectionItemArray=value )
  def setdisableCommands( self , value ):
    cmds.iconTextRadioCollection( self.uiName , e=1 , disableCommands=value )
  def setgl( self , value ):
    cmds.iconTextRadioCollection( self.uiName , e=1 , gl=value )
  def setnumberOfCollectionItems( self , value ):
    cmds.iconTextRadioCollection( self.uiName , e=1 , numberOfCollectionItems=value )
  def setselect( self , value ):
    cmds.iconTextRadioCollection( self.uiName , e=1 , select=value )

  ##### propertyCode #####
  collectionItemArray = property( getcollectionItemArray , setcollectionItemArray )
  disableCommands = property( getdisableCommands , setdisableCommands )
  gl = property( getgl , setgl )
  numberOfCollectionItems = property( getnumberOfCollectionItems , setnumberOfCollectionItems )
  select = property( getselect , setselect )

  ##### customCode #####





class IconTextScrollList( Control ):

  ##### initialize #####
  def __init__( self , append=None , allowMultiSelection=None , changeCommand=None , deselectAll=None , doubleClickCommand=None , dragFeedbackVisible=None , editable=None , editIndexed=None , numberOfIcons=None , numberOfRows=None , removeAll=None , selectCommand=None , selectItem=None , selectIndexedItem=None , **args ):
    self.uiName = cmds.iconTextScrollList()

    ##### substitution #####
    if append != None:
      self.append = append
    if allowMultiSelection != None:
      self.allowMultiSelection = allowMultiSelection
    if changeCommand != None:
      self.changeCommand = changeCommand
    if deselectAll != None:
      self.deselectAll = deselectAll
    if doubleClickCommand != None:
      self.doubleClickCommand = doubleClickCommand
    if dragFeedbackVisible != None:
      self.dragFeedbackVisible = dragFeedbackVisible
    if editable != None:
      self.editable = editable
    if editIndexed != None:
      self.editIndexed = editIndexed
    if numberOfIcons != None:
      self.numberOfIcons = numberOfIcons
    if numberOfRows != None:
      self.numberOfRows = numberOfRows
    if removeAll != None:
      self.removeAll = removeAll
    if selectCommand != None:
      self.selectCommand = selectCommand
    if selectItem != None:
      self.selectItem = selectItem
    if selectIndexedItem != None:
      self.selectIndexedItem = selectIndexedItem

  ##### getFuncCode #####
  def getappend( self ):
    return cmds.iconTextScrollList( self.uiName , q=1 , append=1 )
  def getallowMultiSelection( self ):
    return cmds.iconTextScrollList( self.uiName , q=1 , allowMultiSelection=1 )
  def getchangeCommand( self ):
    return cmds.iconTextScrollList( self.uiName , q=1 , changeCommand=1 )
  def getdeselectAll( self ):
    return cmds.iconTextScrollList( self.uiName , q=1 , deselectAll=1 )
  def getdoubleClickCommand( self ):
    return cmds.iconTextScrollList( self.uiName , q=1 , doubleClickCommand=1 )
  def getdragFeedbackVisible( self ):
    return cmds.iconTextScrollList( self.uiName , q=1 , dragFeedbackVisible=1 )
  def geteditable( self ):
    return cmds.iconTextScrollList( self.uiName , q=1 , editable=1 )
  def geteditIndexed( self ):
    return cmds.iconTextScrollList( self.uiName , q=1 , editIndexed=1 )
  def getnumberOfIcons( self ):
    return cmds.iconTextScrollList( self.uiName , q=1 , numberOfIcons=1 )
  def getnumberOfRows( self ):
    return cmds.iconTextScrollList( self.uiName , q=1 , numberOfRows=1 )
  def getremoveAll( self ):
    return cmds.iconTextScrollList( self.uiName , q=1 , removeAll=1 )
  def getselectCommand( self ):
    return cmds.iconTextScrollList( self.uiName , q=1 , selectCommand=1 )
  def getselectItem( self ):
    return cmds.iconTextScrollList( self.uiName , q=1 , selectItem=1 )
  def getselectIndexedItem( self ):
    return cmds.iconTextScrollList( self.uiName , q=1 , selectIndexedItem=1 )

  ##### setFuncCode #####
  def setappend( self , value ):
    cmds.iconTextScrollList( self.uiName , e=1 , append=value )
  def setallowMultiSelection( self , value ):
    cmds.iconTextScrollList( self.uiName , e=1 , allowMultiSelection=value )
  def setchangeCommand( self , value ):
    cmds.iconTextScrollList( self.uiName , e=1 , changeCommand=value )
  def setdeselectAll( self , value ):
    cmds.iconTextScrollList( self.uiName , e=1 , deselectAll=value )
  def setdoubleClickCommand( self , value ):
    cmds.iconTextScrollList( self.uiName , e=1 , doubleClickCommand=value )
  def setdragFeedbackVisible( self , value ):
    cmds.iconTextScrollList( self.uiName , e=1 , dragFeedbackVisible=value )
  def seteditable( self , value ):
    cmds.iconTextScrollList( self.uiName , e=1 , editable=value )
  def seteditIndexed( self , value ):
    cmds.iconTextScrollList( self.uiName , e=1 , editIndexed=value )
  def setnumberOfIcons( self , value ):
    cmds.iconTextScrollList( self.uiName , e=1 , numberOfIcons=value )
  def setnumberOfRows( self , value ):
    cmds.iconTextScrollList( self.uiName , e=1 , numberOfRows=value )
  def setremoveAll( self , value ):
    cmds.iconTextScrollList( self.uiName , e=1 , removeAll=value )
  def setselectCommand( self , value ):
    cmds.iconTextScrollList( self.uiName , e=1 , selectCommand=value )
  def setselectItem( self , value ):
    cmds.iconTextScrollList( self.uiName , e=1 , selectItem=value )
  def setselectIndexedItem( self , value ):
    cmds.iconTextScrollList( self.uiName , e=1 , selectIndexedItem=value )

  ##### propertyCode #####
  append = property( getappend , setappend )
  allowMultiSelection = property( getallowMultiSelection , setallowMultiSelection )
  changeCommand = property( getchangeCommand , setchangeCommand )
  deselectAll = property( getdeselectAll , setdeselectAll )
  doubleClickCommand = property( getdoubleClickCommand , setdoubleClickCommand )
  dragFeedbackVisible = property( getdragFeedbackVisible , setdragFeedbackVisible )
  editable = property( geteditable , seteditable )
  editIndexed = property( geteditIndexed , seteditIndexed )
  numberOfIcons = property( getnumberOfIcons , setnumberOfIcons )
  numberOfRows = property( getnumberOfRows , setnumberOfRows )
  removeAll = property( getremoveAll , setremoveAll )
  selectCommand = property( getselectCommand , setselectCommand )
  selectItem = property( getselectItem , setselectItem )
  selectIndexedItem = property( getselectIndexedItem , setselectIndexedItem )

  ##### customCode #####





class IconTextStaticLabel( Control ):

  ##### initialize #####
  def __init__( self , align=None , disabledImage=None , font=None , image=None , image1=None , image2=None , image3=None , imageOverlayLabel=None , label=None , labelOffset=None , marginHeight=None , marginWidth=None , style=None , **args ):
    self.uiName = cmds.iconTextStaticLabel()

    ##### substitution #####
    if align != None:
      self.align = align
    if disabledImage != None:
      self.disabledImage = disabledImage
    if font != None:
      self.font = font
    if image != None:
      self.image = image
    if image1 != None:
      self.image1 = image1
    if image2 != None:
      self.image2 = image2
    if image3 != None:
      self.image3 = image3
    if imageOverlayLabel != None:
      self.imageOverlayLabel = imageOverlayLabel
    if label != None:
      self.label = label
    if labelOffset != None:
      self.labelOffset = labelOffset
    if marginHeight != None:
      self.marginHeight = marginHeight
    if marginWidth != None:
      self.marginWidth = marginWidth
    if style != None:
      self.style = style

  ##### getFuncCode #####
  def getalign( self ):
    return cmds.iconTextStaticLabel( self.uiName , q=1 , align=1 )
  def getdisabledImage( self ):
    return cmds.iconTextStaticLabel( self.uiName , q=1 , disabledImage=1 )
  def getfont( self ):
    return cmds.iconTextStaticLabel( self.uiName , q=1 , font=1 )
  def getimage( self ):
    return cmds.iconTextStaticLabel( self.uiName , q=1 , image=1 )
  def getimage1( self ):
    return cmds.iconTextStaticLabel( self.uiName , q=1 , image1=1 )
  def getimage2( self ):
    return cmds.iconTextStaticLabel( self.uiName , q=1 , image2=1 )
  def getimage3( self ):
    return cmds.iconTextStaticLabel( self.uiName , q=1 , image3=1 )
  def getimageOverlayLabel( self ):
    return cmds.iconTextStaticLabel( self.uiName , q=1 , imageOverlayLabel=1 )
  def getlabel( self ):
    return cmds.iconTextStaticLabel( self.uiName , q=1 , label=1 )
  def getlabelOffset( self ):
    return cmds.iconTextStaticLabel( self.uiName , q=1 , labelOffset=1 )
  def getmarginHeight( self ):
    return cmds.iconTextStaticLabel( self.uiName , q=1 , marginHeight=1 )
  def getmarginWidth( self ):
    return cmds.iconTextStaticLabel( self.uiName , q=1 , marginWidth=1 )
  def getstyle( self ):
    return cmds.iconTextStaticLabel( self.uiName , q=1 , style=1 )

  ##### setFuncCode #####
  def setalign( self , value ):
    cmds.iconTextStaticLabel( self.uiName , e=1 , align=value )
  def setdisabledImage( self , value ):
    cmds.iconTextStaticLabel( self.uiName , e=1 , disabledImage=value )
  def setfont( self , value ):
    cmds.iconTextStaticLabel( self.uiName , e=1 , font=value )
  def setimage( self , value ):
    cmds.iconTextStaticLabel( self.uiName , e=1 , image=value )
  def setimage1( self , value ):
    cmds.iconTextStaticLabel( self.uiName , e=1 , image1=value )
  def setimage2( self , value ):
    cmds.iconTextStaticLabel( self.uiName , e=1 , image2=value )
  def setimage3( self , value ):
    cmds.iconTextStaticLabel( self.uiName , e=1 , image3=value )
  def setimageOverlayLabel( self , value ):
    cmds.iconTextStaticLabel( self.uiName , e=1 , imageOverlayLabel=value )
  def setlabel( self , value ):
    cmds.iconTextStaticLabel( self.uiName , e=1 , label=value )
  def setlabelOffset( self , value ):
    cmds.iconTextStaticLabel( self.uiName , e=1 , labelOffset=value )
  def setmarginHeight( self , value ):
    cmds.iconTextStaticLabel( self.uiName , e=1 , marginHeight=value )
  def setmarginWidth( self , value ):
    cmds.iconTextStaticLabel( self.uiName , e=1 , marginWidth=value )
  def setstyle( self , value ):
    cmds.iconTextStaticLabel( self.uiName , e=1 , style=value )

  ##### propertyCode #####
  align = property( getalign , setalign )
  disabledImage = property( getdisabledImage , setdisabledImage )
  font = property( getfont , setfont )
  image = property( getimage , setimage )
  image1 = property( getimage1 , setimage1 )
  image2 = property( getimage2 , setimage2 )
  image3 = property( getimage3 , setimage3 )
  imageOverlayLabel = property( getimageOverlayLabel , setimageOverlayLabel )
  label = property( getlabel , setlabel )
  labelOffset = property( getlabelOffset , setlabelOffset )
  marginHeight = property( getmarginHeight , setmarginHeight )
  marginWidth = property( getmarginWidth , setmarginWidth )
  style = property( getstyle , setstyle )

  ##### customCode #####





class Image( Control ):

  ##### initialize #####
  def __init__( self , image=None , **args ):
    self.uiName = cmds.image()

    ##### substitution #####
    if image != None:
      self.image = image

  ##### getFuncCode #####
  def getimage( self ):
    return cmds.image( self.uiName , q=1 , image=1 )

  ##### setFuncCode #####
  def setimage( self , value ):
    cmds.image( self.uiName , e=1 , image=value )

  ##### propertyCode #####
  image = property( getimage , setimage )

  ##### customCode #####





class IntField( Control ):

  ##### initialize #####
  def __init__( self , changeCommand=None , dragCommand=None , enterCommand=None , editable=None , maxValue=None , minValue=None , receiveFocusCommand=None , step=None , value=None , **args ):
    self.uiName = cmds.intField()

    ##### substitution #####
    if changeCommand != None:
      self.changeCommand = changeCommand
    if dragCommand != None:
      self.dragCommand = dragCommand
    if enterCommand != None:
      self.enterCommand = enterCommand
    if editable != None:
      self.editable = editable
    if maxValue != None:
      self.maxValue = maxValue
    if minValue != None:
      self.minValue = minValue
    if receiveFocusCommand != None:
      self.receiveFocusCommand = receiveFocusCommand
    if step != None:
      self.step = step
    if value != None:
      self.value = value

  ##### getFuncCode #####
  def getchangeCommand( self ):
    return cmds.intField( self.uiName , q=1 , changeCommand=1 )
  def getdragCommand( self ):
    return cmds.intField( self.uiName , q=1 , dragCommand=1 )
  def getenterCommand( self ):
    return cmds.intField( self.uiName , q=1 , enterCommand=1 )
  def geteditable( self ):
    return cmds.intField( self.uiName , q=1 , editable=1 )
  def getmaxValue( self ):
    return cmds.intField( self.uiName , q=1 , maxValue=1 )
  def getminValue( self ):
    return cmds.intField( self.uiName , q=1 , minValue=1 )
  def getreceiveFocusCommand( self ):
    return cmds.intField( self.uiName , q=1 , receiveFocusCommand=1 )
  def getstep( self ):
    return cmds.intField( self.uiName , q=1 , step=1 )
  def getvalue( self ):
    return cmds.intField( self.uiName , q=1 , value=1 )

  ##### setFuncCode #####
  def setchangeCommand( self , value ):
    cmds.intField( self.uiName , e=1 , changeCommand=value )
  def setdragCommand( self , value ):
    cmds.intField( self.uiName , e=1 , dragCommand=value )
  def setenterCommand( self , value ):
    cmds.intField( self.uiName , e=1 , enterCommand=value )
  def seteditable( self , value ):
    cmds.intField( self.uiName , e=1 , editable=value )
  def setmaxValue( self , value ):
    cmds.intField( self.uiName , e=1 , maxValue=value )
  def setminValue( self , value ):
    cmds.intField( self.uiName , e=1 , minValue=value )
  def setreceiveFocusCommand( self , value ):
    cmds.intField( self.uiName , e=1 , receiveFocusCommand=value )
  def setstep( self , value ):
    cmds.intField( self.uiName , e=1 , step=value )
  def setvalue( self , value ):
    cmds.intField( self.uiName , e=1 , value=value )

  ##### propertyCode #####
  changeCommand = property( getchangeCommand , setchangeCommand )
  dragCommand = property( getdragCommand , setdragCommand )
  enterCommand = property( getenterCommand , setenterCommand )
  editable = property( geteditable , seteditable )
  maxValue = property( getmaxValue , setmaxValue )
  minValue = property( getminValue , setminValue )
  receiveFocusCommand = property( getreceiveFocusCommand , setreceiveFocusCommand )
  step = property( getstep , setstep )
  value = property( getvalue , setvalue )

  ##### customCode #####





class IntScrollBar( Control ):

  ##### initialize #####
  def __init__( self , changeCommand=None , dragCommand=None , horizontal=None , largeStep=None , maxValue=None , minValue=None , step=None , value=None , **args ):
    self.uiName = cmds.intScrollBar()

    ##### substitution #####
    if changeCommand != None:
      self.changeCommand = changeCommand
    if dragCommand != None:
      self.dragCommand = dragCommand
    if horizontal != None:
      self.horizontal = horizontal
    if largeStep != None:
      self.largeStep = largeStep
    if maxValue != None:
      self.maxValue = maxValue
    if minValue != None:
      self.minValue = minValue
    if step != None:
      self.step = step
    if value != None:
      self.value = value

  ##### getFuncCode #####
  def getchangeCommand( self ):
    return cmds.intScrollBar( self.uiName , q=1 , changeCommand=1 )
  def getdragCommand( self ):
    return cmds.intScrollBar( self.uiName , q=1 , dragCommand=1 )
  def gethorizontal( self ):
    return cmds.intScrollBar( self.uiName , q=1 , horizontal=1 )
  def getlargeStep( self ):
    return cmds.intScrollBar( self.uiName , q=1 , largeStep=1 )
  def getmaxValue( self ):
    return cmds.intScrollBar( self.uiName , q=1 , maxValue=1 )
  def getminValue( self ):
    return cmds.intScrollBar( self.uiName , q=1 , minValue=1 )
  def getstep( self ):
    return cmds.intScrollBar( self.uiName , q=1 , step=1 )
  def getvalue( self ):
    return cmds.intScrollBar( self.uiName , q=1 , value=1 )

  ##### setFuncCode #####
  def setchangeCommand( self , value ):
    cmds.intScrollBar( self.uiName , e=1 , changeCommand=value )
  def setdragCommand( self , value ):
    cmds.intScrollBar( self.uiName , e=1 , dragCommand=value )
  def sethorizontal( self , value ):
    cmds.intScrollBar( self.uiName , e=1 , horizontal=value )
  def setlargeStep( self , value ):
    cmds.intScrollBar( self.uiName , e=1 , largeStep=value )
  def setmaxValue( self , value ):
    cmds.intScrollBar( self.uiName , e=1 , maxValue=value )
  def setminValue( self , value ):
    cmds.intScrollBar( self.uiName , e=1 , minValue=value )
  def setstep( self , value ):
    cmds.intScrollBar( self.uiName , e=1 , step=value )
  def setvalue( self , value ):
    cmds.intScrollBar( self.uiName , e=1 , value=value )

  ##### propertyCode #####
  changeCommand = property( getchangeCommand , setchangeCommand )
  dragCommand = property( getdragCommand , setdragCommand )
  horizontal = property( gethorizontal , sethorizontal )
  largeStep = property( getlargeStep , setlargeStep )
  maxValue = property( getmaxValue , setmaxValue )
  minValue = property( getminValue , setminValue )
  step = property( getstep , setstep )
  value = property( getvalue , setvalue )

  ##### customCode #####





class IntSlider( Control ):

  ##### initialize #####
  def __init__( self , changeCommand=None , dragCommand=None , horizontal=None , maxValue=None , minValue=None , step=None , value=None , **args ):
    self.uiName = cmds.intSlider()

    ##### substitution #####
    if changeCommand != None:
      self.changeCommand = changeCommand
    if dragCommand != None:
      self.dragCommand = dragCommand
    if horizontal != None:
      self.horizontal = horizontal
    if maxValue != None:
      self.maxValue = maxValue
    if minValue != None:
      self.minValue = minValue
    if step != None:
      self.step = step
    if value != None:
      self.value = value

  ##### getFuncCode #####
  def getchangeCommand( self ):
    return cmds.intSlider( self.uiName , q=1 , changeCommand=1 )
  def getdragCommand( self ):
    return cmds.intSlider( self.uiName , q=1 , dragCommand=1 )
  def gethorizontal( self ):
    return cmds.intSlider( self.uiName , q=1 , horizontal=1 )
  def getmaxValue( self ):
    return cmds.intSlider( self.uiName , q=1 , maxValue=1 )
  def getminValue( self ):
    return cmds.intSlider( self.uiName , q=1 , minValue=1 )
  def getstep( self ):
    return cmds.intSlider( self.uiName , q=1 , step=1 )
  def getvalue( self ):
    return cmds.intSlider( self.uiName , q=1 , value=1 )

  ##### setFuncCode #####
  def setchangeCommand( self , value ):
    cmds.intSlider( self.uiName , e=1 , changeCommand=value )
  def setdragCommand( self , value ):
    cmds.intSlider( self.uiName , e=1 , dragCommand=value )
  def sethorizontal( self , value ):
    cmds.intSlider( self.uiName , e=1 , horizontal=value )
  def setmaxValue( self , value ):
    cmds.intSlider( self.uiName , e=1 , maxValue=value )
  def setminValue( self , value ):
    cmds.intSlider( self.uiName , e=1 , minValue=value )
  def setstep( self , value ):
    cmds.intSlider( self.uiName , e=1 , step=value )
  def setvalue( self , value ):
    cmds.intSlider( self.uiName , e=1 , value=value )

  ##### propertyCode #####
  changeCommand = property( getchangeCommand , setchangeCommand )
  dragCommand = property( getdragCommand , setdragCommand )
  horizontal = property( gethorizontal , sethorizontal )
  maxValue = property( getmaxValue , setmaxValue )
  minValue = property( getminValue , setminValue )
  step = property( getstep , setstep )
  value = property( getvalue , setvalue )

  ##### customCode #####





class LayerButton( Control ):

  ##### initialize #####
  def __init__( self , command=None , changeCommand=None , color=None , current=None , doubleClickCommand=None , identification=None , label=None , layerState=None , layerVisible=None , labelWidth=None , name=None , renameCommand=None , select=None , transparent=None , typeCommand=None , visibleCommand=None , **args ):
    self.uiName = cmds.layerButton()

    ##### substitution #####
    if command != None:
      self.command = command
    if changeCommand != None:
      self.changeCommand = changeCommand
    if color != None:
      self.color = color
    if current != None:
      self.current = current
    if doubleClickCommand != None:
      self.doubleClickCommand = doubleClickCommand
    if identification != None:
      self.identification = identification
    if label != None:
      self.label = label
    if layerState != None:
      self.layerState = layerState
    if layerVisible != None:
      self.layerVisible = layerVisible
    if labelWidth != None:
      self.labelWidth = labelWidth
    if name != None:
      self.name = name
    if renameCommand != None:
      self.renameCommand = renameCommand
    if select != None:
      self.select = select
    if transparent != None:
      self.transparent = transparent
    if typeCommand != None:
      self.typeCommand = typeCommand
    if visibleCommand != None:
      self.visibleCommand = visibleCommand

  ##### getFuncCode #####
  def getcommand( self ):
    return cmds.layerButton( self.uiName , q=1 , command=1 )
  def getchangeCommand( self ):
    return cmds.layerButton( self.uiName , q=1 , changeCommand=1 )
  def getcolor( self ):
    return cmds.layerButton( self.uiName , q=1 , color=1 )
  def getcurrent( self ):
    return cmds.layerButton( self.uiName , q=1 , current=1 )
  def getdoubleClickCommand( self ):
    return cmds.layerButton( self.uiName , q=1 , doubleClickCommand=1 )
  def getidentification( self ):
    return cmds.layerButton( self.uiName , q=1 , identification=1 )
  def getlabel( self ):
    return cmds.layerButton( self.uiName , q=1 , label=1 )
  def getlayerState( self ):
    return cmds.layerButton( self.uiName , q=1 , layerState=1 )
  def getlayerVisible( self ):
    return cmds.layerButton( self.uiName , q=1 , layerVisible=1 )
  def getlabelWidth( self ):
    return cmds.layerButton( self.uiName , q=1 , labelWidth=1 )
  def getname( self ):
    return cmds.layerButton( self.uiName , q=1 , name=1 )
  def getrenameCommand( self ):
    return cmds.layerButton( self.uiName , q=1 , renameCommand=1 )
  def getselect( self ):
    return cmds.layerButton( self.uiName , q=1 , select=1 )
  def gettransparent( self ):
    return cmds.layerButton( self.uiName , q=1 , transparent=1 )
  def gettypeCommand( self ):
    return cmds.layerButton( self.uiName , q=1 , typeCommand=1 )
  def getvisibleCommand( self ):
    return cmds.layerButton( self.uiName , q=1 , visibleCommand=1 )

  ##### setFuncCode #####
  def setcommand( self , value ):
    cmds.layerButton( self.uiName , e=1 , command=value )
  def setchangeCommand( self , value ):
    cmds.layerButton( self.uiName , e=1 , changeCommand=value )
  def setcolor( self , value ):
    cmds.layerButton( self.uiName , e=1 , color=value )
  def setcurrent( self , value ):
    cmds.layerButton( self.uiName , e=1 , current=value )
  def setdoubleClickCommand( self , value ):
    cmds.layerButton( self.uiName , e=1 , doubleClickCommand=value )
  def setidentification( self , value ):
    cmds.layerButton( self.uiName , e=1 , identification=value )
  def setlabel( self , value ):
    cmds.layerButton( self.uiName , e=1 , label=value )
  def setlayerState( self , value ):
    cmds.layerButton( self.uiName , e=1 , layerState=value )
  def setlayerVisible( self , value ):
    cmds.layerButton( self.uiName , e=1 , layerVisible=value )
  def setlabelWidth( self , value ):
    cmds.layerButton( self.uiName , e=1 , labelWidth=value )
  def setname( self , value ):
    cmds.layerButton( self.uiName , e=1 , name=value )
  def setrenameCommand( self , value ):
    cmds.layerButton( self.uiName , e=1 , renameCommand=value )
  def setselect( self , value ):
    cmds.layerButton( self.uiName , e=1 , select=value )
  def settransparent( self , value ):
    cmds.layerButton( self.uiName , e=1 , transparent=value )
  def settypeCommand( self , value ):
    cmds.layerButton( self.uiName , e=1 , typeCommand=value )
  def setvisibleCommand( self , value ):
    cmds.layerButton( self.uiName , e=1 , visibleCommand=value )

  ##### propertyCode #####
  command = property( getcommand , setcommand )
  changeCommand = property( getchangeCommand , setchangeCommand )
  color = property( getcolor , setcolor )
  current = property( getcurrent , setcurrent )
  doubleClickCommand = property( getdoubleClickCommand , setdoubleClickCommand )
  identification = property( getidentification , setidentification )
  label = property( getlabel , setlabel )
  layerState = property( getlayerState , setlayerState )
  layerVisible = property( getlayerVisible , setlayerVisible )
  labelWidth = property( getlabelWidth , setlabelWidth )
  name = property( getname , setname )
  renameCommand = property( getrenameCommand , setrenameCommand )
  select = property( getselect , setselect )
  transparent = property( gettransparent , settransparent )
  typeCommand = property( gettypeCommand , settypeCommand )
  visibleCommand = property( getvisibleCommand , setvisibleCommand )

  ##### customCode #####





class Picture( Control ):

  ##### initialize #####
  def __init__( self , image=None , tile=None , **args ):
    self.uiName = cmds.picture()

    ##### substitution #####
    if image != None:
      self.image = image
    if tile != None:
      self.tile = tile

  ##### getFuncCode #####
  def getimage( self ):
    return cmds.picture( self.uiName , q=1 , image=1 )
  def gettile( self ):
    return cmds.picture( self.uiName , q=1 , tile=1 )

  ##### setFuncCode #####
  def setimage( self , value ):
    cmds.picture( self.uiName , e=1 , image=value )
  def settile( self , value ):
    cmds.picture( self.uiName , e=1 , tile=value )

  ##### propertyCode #####
  image = property( getimage , setimage )
  tile = property( gettile , settile )

  ##### customCode #####





class ProgressBar( Control ):

  ##### initialize #####
  def __init__( self , beginProgress=None , endProgress=None , isCancelled=None , isInterruptable=None , isMainProgressBar=None , maxValue=None , minValue=None , progress=None , step=None , status=None , **args ):
    self.uiName = cmds.progressBar()

    ##### substitution #####
    if beginProgress != None:
      self.beginProgress = beginProgress
    if endProgress != None:
      self.endProgress = endProgress
    if isCancelled != None:
      self.isCancelled = isCancelled
    if isInterruptable != None:
      self.isInterruptable = isInterruptable
    if isMainProgressBar != None:
      self.isMainProgressBar = isMainProgressBar
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
  def getbeginProgress( self ):
    return cmds.progressBar( self.uiName , q=1 , beginProgress=1 )
  def getendProgress( self ):
    return cmds.progressBar( self.uiName , q=1 , endProgress=1 )
  def getisCancelled( self ):
    return cmds.progressBar( self.uiName , q=1 , isCancelled=1 )
  def getisInterruptable( self ):
    return cmds.progressBar( self.uiName , q=1 , isInterruptable=1 )
  def getisMainProgressBar( self ):
    return cmds.progressBar( self.uiName , q=1 , isMainProgressBar=1 )
  def getmaxValue( self ):
    return cmds.progressBar( self.uiName , q=1 , maxValue=1 )
  def getminValue( self ):
    return cmds.progressBar( self.uiName , q=1 , minValue=1 )
  def getprogress( self ):
    return cmds.progressBar( self.uiName , q=1 , progress=1 )
  def getstep( self ):
    return cmds.progressBar( self.uiName , q=1 , step=1 )
  def getstatus( self ):
    return cmds.progressBar( self.uiName , q=1 , status=1 )

  ##### setFuncCode #####
  def setbeginProgress( self , value ):
    cmds.progressBar( self.uiName , e=1 , beginProgress=value )
  def setendProgress( self , value ):
    cmds.progressBar( self.uiName , e=1 , endProgress=value )
  def setisCancelled( self , value ):
    cmds.progressBar( self.uiName , e=1 , isCancelled=value )
  def setisInterruptable( self , value ):
    cmds.progressBar( self.uiName , e=1 , isInterruptable=value )
  def setisMainProgressBar( self , value ):
    cmds.progressBar( self.uiName , e=1 , isMainProgressBar=value )
  def setmaxValue( self , value ):
    cmds.progressBar( self.uiName , e=1 , maxValue=value )
  def setminValue( self , value ):
    cmds.progressBar( self.uiName , e=1 , minValue=value )
  def setprogress( self , value ):
    cmds.progressBar( self.uiName , e=1 , progress=value )
  def setstep( self , value ):
    cmds.progressBar( self.uiName , e=1 , step=value )
  def setstatus( self , value ):
    cmds.progressBar( self.uiName , e=1 , status=value )

  ##### propertyCode #####
  beginProgress = property( getbeginProgress , setbeginProgress )
  endProgress = property( getendProgress , setendProgress )
  isCancelled = property( getisCancelled , setisCancelled )
  isInterruptable = property( getisInterruptable , setisInterruptable )
  isMainProgressBar = property( getisMainProgressBar , setisMainProgressBar )
  maxValue = property( getmaxValue , setmaxValue )
  minValue = property( getminValue , setminValue )
  progress = property( getprogress , setprogress )
  step = property( getstep , setstep )
  status = property( getstatus , setstatus )

  ##### customCode #####

  def reset( self ):
    self.progress    = 0
    self.endProgress = 1



class RadioButton( Control ):

  ##### initialize #####
  def __init__( self , align=None , changeCommand=None , collection=None , data=None , editable=None , label=None , offCommand=None , onCommand=None , recomputeSize=None , select=None , **args ):
    self.uiName = cmds.radioButton()

    ##### substitution #####
    if align != None:
      self.align = align
    if changeCommand != None:
      self.changeCommand = changeCommand
    if collection != None:
      self.collection = collection
    if data != None:
      self.data = data
    if editable != None:
      self.editable = editable
    if label != None:
      self.label = label
    if offCommand != None:
      self.offCommand = offCommand
    if onCommand != None:
      self.onCommand = onCommand
    if recomputeSize != None:
      self.recomputeSize = recomputeSize
    if select != None:
      self.select = select

  ##### getFuncCode #####
  def getalign( self ):
    return cmds.radioButton( self.uiName , q=1 , align=1 )
  def getchangeCommand( self ):
    return cmds.radioButton( self.uiName , q=1 , changeCommand=1 )
  def getcollection( self ):
    return cmds.radioButton( self.uiName , q=1 , collection=1 )
  def getdata( self ):
    return cmds.radioButton( self.uiName , q=1 , data=1 )
  def geteditable( self ):
    return cmds.radioButton( self.uiName , q=1 , editable=1 )
  def getlabel( self ):
    return cmds.radioButton( self.uiName , q=1 , label=1 )
  def getoffCommand( self ):
    return cmds.radioButton( self.uiName , q=1 , offCommand=1 )
  def getonCommand( self ):
    return cmds.radioButton( self.uiName , q=1 , onCommand=1 )
  def getrecomputeSize( self ):
    return cmds.radioButton( self.uiName , q=1 , recomputeSize=1 )
  def getselect( self ):
    return cmds.radioButton( self.uiName , q=1 , select=1 )

  ##### setFuncCode #####
  def setalign( self , value ):
    cmds.radioButton( self.uiName , e=1 , align=value )
  def setchangeCommand( self , value ):
    cmds.radioButton( self.uiName , e=1 , changeCommand=value )
  def setcollection( self , value ):
    cmds.radioButton( self.uiName , e=1 , collection=value )
  def setdata( self , value ):
    cmds.radioButton( self.uiName , e=1 , data=value )
  def seteditable( self , value ):
    cmds.radioButton( self.uiName , e=1 , editable=value )
  def setlabel( self , value ):
    cmds.radioButton( self.uiName , e=1 , label=value )
  def setoffCommand( self , value ):
    cmds.radioButton( self.uiName , e=1 , offCommand=value )
  def setonCommand( self , value ):
    cmds.radioButton( self.uiName , e=1 , onCommand=value )
  def setrecomputeSize( self , value ):
    cmds.radioButton( self.uiName , e=1 , recomputeSize=value )
  def setselect( self , value ):
    cmds.radioButton( self.uiName , e=1 , select=value )

  ##### propertyCode #####
  align = property( getalign , setalign )
  changeCommand = property( getchangeCommand , setchangeCommand )
  collection = property( getcollection , setcollection )
  data = property( getdata , setdata )
  editable = property( geteditable , seteditable )
  label = property( getlabel , setlabel )
  offCommand = property( getoffCommand , setoffCommand )
  onCommand = property( getonCommand , setonCommand )
  recomputeSize = property( getrecomputeSize , setrecomputeSize )
  select = property( getselect , setselect )

  ##### customCode #####





class RadioCollection( Control ):

  ##### initialize #####
  def __init__( self , collectionItemArray=None , gl=None , numberOfCollectionItems=None , select=None , **args ):
    self.uiName = cmds.radioCollection()

    ##### substitution #####
    if collectionItemArray != None:
      self.collectionItemArray = collectionItemArray
    if gl != None:
      self.gl = gl
    if numberOfCollectionItems != None:
      self.numberOfCollectionItems = numberOfCollectionItems
    if select != None:
      self.select = select

  ##### getFuncCode #####
  def getcollectionItemArray( self ):
    return cmds.radioCollection( self.uiName , q=1 , collectionItemArray=1 )
  def getgl( self ):
    return cmds.radioCollection( self.uiName , q=1 , gl=1 )
  def getnumberOfCollectionItems( self ):
    return cmds.radioCollection( self.uiName , q=1 , numberOfCollectionItems=1 )
  def getselect( self ):
    return cmds.radioCollection( self.uiName , q=1 , select=1 )

  ##### setFuncCode #####
  def setcollectionItemArray( self , value ):
    cmds.radioCollection( self.uiName , e=1 , collectionItemArray=value )
  def setgl( self , value ):
    cmds.radioCollection( self.uiName , e=1 , gl=value )
  def setnumberOfCollectionItems( self , value ):
    cmds.radioCollection( self.uiName , e=1 , numberOfCollectionItems=value )
  def setselect( self , value ):
    cmds.radioCollection( self.uiName , e=1 , select=value )

  ##### propertyCode #####
  collectionItemArray = property( getcollectionItemArray , setcollectionItemArray )
  gl = property( getgl , setgl )
  numberOfCollectionItems = property( getnumberOfCollectionItems , setnumberOfCollectionItems )
  select = property( getselect , setselect )

  ##### customCode #####





class ScrollField( Control ):

  ##### initialize #####
  def __init__( self , command=None , changeCommand=None , clear=None , enterCommand=None , editable=None , font=None , insertionPosition=None , insertText=None , keyPressCommand=None , numberOfLines=None , selection=None , text=None , wordWrap=None , **args ):
    self.uiName = cmds.scrollField()

    ##### substitution #####
    if command != None:
      self.command = command
    if changeCommand != None:
      self.changeCommand = changeCommand
    if clear != None:
      self.clear = clear
    if enterCommand != None:
      self.enterCommand = enterCommand
    if editable != None:
      self.editable = editable
    if font != None:
      self.font = font
    if insertionPosition != None:
      self.insertionPosition = insertionPosition
    if insertText != None:
      self.insertText = insertText
    if keyPressCommand != None:
      self.keyPressCommand = keyPressCommand
    if numberOfLines != None:
      self.numberOfLines = numberOfLines
    if selection != None:
      self.selection = selection
    if text != None:
      self.text = text
    if wordWrap != None:
      self.wordWrap = wordWrap

  ##### getFuncCode #####
  def getcommand( self ):
    return cmds.scrollField( self.uiName , q=1 , command=1 )
  def getchangeCommand( self ):
    return cmds.scrollField( self.uiName , q=1 , changeCommand=1 )
  def getclear( self ):
    return cmds.scrollField( self.uiName , q=1 , clear=1 )
  def getenterCommand( self ):
    return cmds.scrollField( self.uiName , q=1 , enterCommand=1 )
  def geteditable( self ):
    return cmds.scrollField( self.uiName , q=1 , editable=1 )
  def getfont( self ):
    return cmds.scrollField( self.uiName , q=1 , font=1 )
  def getinsertionPosition( self ):
    return cmds.scrollField( self.uiName , q=1 , insertionPosition=1 )
  def getinsertText( self ):
    return cmds.scrollField( self.uiName , q=1 , insertText=1 )
  def getkeyPressCommand( self ):
    return cmds.scrollField( self.uiName , q=1 , keyPressCommand=1 )
  def getnumberOfLines( self ):
    return cmds.scrollField( self.uiName , q=1 , numberOfLines=1 )
  def getselection( self ):
    return cmds.scrollField( self.uiName , q=1 , selection=1 )
  def gettext( self ):
    return cmds.scrollField( self.uiName , q=1 , text=1 )
  def getwordWrap( self ):
    return cmds.scrollField( self.uiName , q=1 , wordWrap=1 )

  ##### setFuncCode #####
  def setcommand( self , value ):
    cmds.scrollField( self.uiName , e=1 , command=value )
  def setchangeCommand( self , value ):
    cmds.scrollField( self.uiName , e=1 , changeCommand=value )
  def setclear( self , value ):
    cmds.scrollField( self.uiName , e=1 , clear=value )
  def setenterCommand( self , value ):
    cmds.scrollField( self.uiName , e=1 , enterCommand=value )
  def seteditable( self , value ):
    cmds.scrollField( self.uiName , e=1 , editable=value )
  def setfont( self , value ):
    cmds.scrollField( self.uiName , e=1 , font=value )
  def setinsertionPosition( self , value ):
    cmds.scrollField( self.uiName , e=1 , insertionPosition=value )
  def setinsertText( self , value ):
    cmds.scrollField( self.uiName , e=1 , insertText=value )
  def setkeyPressCommand( self , value ):
    cmds.scrollField( self.uiName , e=1 , keyPressCommand=value )
  def setnumberOfLines( self , value ):
    cmds.scrollField( self.uiName , e=1 , numberOfLines=value )
  def setselection( self , value ):
    cmds.scrollField( self.uiName , e=1 , selection=value )
  def settext( self , value ):
    cmds.scrollField( self.uiName , e=1 , text=value )
  def setwordWrap( self , value ):
    cmds.scrollField( self.uiName , e=1 , wordWrap=value )

  ##### propertyCode #####
  command = property( getcommand , setcommand )
  changeCommand = property( getchangeCommand , setchangeCommand )
  clear = property( getclear , setclear )
  enterCommand = property( getenterCommand , setenterCommand )
  editable = property( geteditable , seteditable )
  font = property( getfont , setfont )
  insertionPosition = property( getinsertionPosition , setinsertionPosition )
  insertText = property( getinsertText , setinsertText )
  keyPressCommand = property( getkeyPressCommand , setkeyPressCommand )
  numberOfLines = property( getnumberOfLines , setnumberOfLines )
  selection = property( getselection , setselection )
  text = property( gettext , settext )
  wordWrap = property( getwordWrap , setwordWrap )

  ##### customCode #####





class Separator( Control ):

  ##### initialize #####
  def __init__( self , horizontal=None , style=None , **args ):
    self.uiName = cmds.separator()

    ##### substitution #####
    if horizontal != None:
      self.horizontal = horizontal
    if style != None:
      self.style = style

  ##### getFuncCode #####
  def gethorizontal( self ):
    return cmds.separator( self.uiName , q=1 , horizontal=1 )
  def getstyle( self ):
    return cmds.separator( self.uiName , q=1 , style=1 )

  ##### setFuncCode #####
  def sethorizontal( self , value ):
    cmds.separator( self.uiName , e=1 , horizontal=value )
  def setstyle( self , value ):
    cmds.separator( self.uiName , e=1 , style=value )

  ##### propertyCode #####
  horizontal = property( gethorizontal , sethorizontal )
  style = property( getstyle , setstyle )

  ##### customCode #####





class Text( Control ):

  ##### initialize #####
  def __init__( self , align=None , font=None , label=None , recomputeSize=None , **args ):
    self.uiName = cmds.text()

    ##### substitution #####
    if align != None:
      self.align = align
    if font != None:
      self.font = font
    if label != None:
      self.label = label
    if recomputeSize != None:
      self.recomputeSize = recomputeSize

  ##### getFuncCode #####
  def getalign( self ):
    return cmds.text( self.uiName , q=1 , align=1 )
  def getfont( self ):
    return cmds.text( self.uiName , q=1 , font=1 )
  def getlabel( self ):
    return cmds.text( self.uiName , q=1 , label=1 )
  def getrecomputeSize( self ):
    return cmds.text( self.uiName , q=1 , recomputeSize=1 )

  ##### setFuncCode #####
  def setalign( self , value ):
    cmds.text( self.uiName , e=1 , align=value )
  def setfont( self , value ):
    cmds.text( self.uiName , e=1 , font=value )
  def setlabel( self , value ):
    cmds.text( self.uiName , e=1 , label=value )
  def setrecomputeSize( self , value ):
    cmds.text( self.uiName , e=1 , recomputeSize=value )

  ##### propertyCode #####
  align = property( getalign , setalign )
  font = property( getfont , setfont )
  label = property( getlabel , setlabel )
  recomputeSize = property( getrecomputeSize , setrecomputeSize )

  ##### customCode #####





class Spacer( Control ):

  ##### initialize #####
  def __init__( self , **args ):
    self.uiName = cmds.text( label="" )

    ##### substitution #####

  ##### getFuncCode #####

  ##### setFuncCode #####

  ##### propertyCode #####

  ##### customCode #####





class TextField( Control ):

  ##### initialize #####
  def __init__( self , alwaysInvokeEnterCommandOnReturn=None , changeCommand=None , enterCommand=None , editable=None , fileName=None , font=None , insertionPosition=None , insertText=None , receiveFocusCommand=None , text=None , **args ):
    self.uiName = cmds.textField()

    ##### substitution #####
    if alwaysInvokeEnterCommandOnReturn != None:
      self.alwaysInvokeEnterCommandOnReturn = alwaysInvokeEnterCommandOnReturn
    if changeCommand != None:
      self.changeCommand = changeCommand
    if enterCommand != None:
      self.enterCommand = enterCommand
    if editable != None:
      self.editable = editable
    if fileName != None:
      self.fileName = fileName
    if font != None:
      self.font = font
    if insertionPosition != None:
      self.insertionPosition = insertionPosition
    if insertText != None:
      self.insertText = insertText
    if receiveFocusCommand != None:
      self.receiveFocusCommand = receiveFocusCommand
    if text != None:
      self.text = text

  ##### getFuncCode #####
  def getalwaysInvokeEnterCommandOnReturn( self ):
    return cmds.textField( self.uiName , q=1 , alwaysInvokeEnterCommandOnReturn=1 )
  def getchangeCommand( self ):
    return cmds.textField( self.uiName , q=1 , changeCommand=1 )
  def getenterCommand( self ):
    return cmds.textField( self.uiName , q=1 , enterCommand=1 )
  def geteditable( self ):
    return cmds.textField( self.uiName , q=1 , editable=1 )
  def getfileName( self ):
    return cmds.textField( self.uiName , q=1 , fileName=1 )
  def getfont( self ):
    return cmds.textField( self.uiName , q=1 , font=1 )
  def getinsertionPosition( self ):
    return cmds.textField( self.uiName , q=1 , insertionPosition=1 )
  def getinsertText( self ):
    return cmds.textField( self.uiName , q=1 , insertText=1 )
  def getreceiveFocusCommand( self ):
    return cmds.textField( self.uiName , q=1 , receiveFocusCommand=1 )
  def gettext( self ):
    return cmds.textField( self.uiName , q=1 , text=1 )

  ##### setFuncCode #####
  def setalwaysInvokeEnterCommandOnReturn( self , value ):
    cmds.textField( self.uiName , e=1 , alwaysInvokeEnterCommandOnReturn=value )
  def setchangeCommand( self , value ):
    cmds.textField( self.uiName , e=1 , changeCommand=value )
  def setenterCommand( self , value ):
    cmds.textField( self.uiName , e=1 , enterCommand=value )
  def seteditable( self , value ):
    cmds.textField( self.uiName , e=1 , editable=value )
  def setfileName( self , value ):
    cmds.textField( self.uiName , e=1 , fileName=value )
  def setfont( self , value ):
    cmds.textField( self.uiName , e=1 , font=value )
  def setinsertionPosition( self , value ):
    cmds.textField( self.uiName , e=1 , insertionPosition=value )
  def setinsertText( self , value ):
    cmds.textField( self.uiName , e=1 , insertText=value )
  def setreceiveFocusCommand( self , value ):
    cmds.textField( self.uiName , e=1 , receiveFocusCommand=value )
  def settext( self , value ):
    cmds.textField( self.uiName , e=1 , text=value )

  ##### propertyCode #####
  alwaysInvokeEnterCommandOnReturn = property( getalwaysInvokeEnterCommandOnReturn , setalwaysInvokeEnterCommandOnReturn )
  changeCommand = property( getchangeCommand , setchangeCommand )
  enterCommand = property( getenterCommand , setenterCommand )
  editable = property( geteditable , seteditable )
  fileName = property( getfileName , setfileName )
  font = property( getfont , setfont )
  insertionPosition = property( getinsertionPosition , setinsertionPosition )
  insertText = property( getinsertText , setinsertText )
  receiveFocusCommand = property( getreceiveFocusCommand , setreceiveFocusCommand )
  text = property( gettext , settext )

  ##### customCode #####





class TextScrollList( Control ):

  ##### initialize #####
  def __init__( self , append=None , allowAutomaticSelection=None , allItems=None , allowMultiSelection=None , appendPosition=None , deselectAll=None , doubleClickCommand=None , deselectItem=None , deselectIndexedItem=None , deleteKeyCommand=None , font=None , numberOfItems=None , numberOfRows=None , numberOfSelectedItems=None , removeAll=None , removeItem=None , removeIndexedItem=None , selectCommand=None , showIndexedItem=None , selectItem=None , selectIndexedItem=None , **args ):
    self.uiName = cmds.textScrollList()

    ##### substitution #####
    if append != None:
      self.append = append
    if allowAutomaticSelection != None:
      self.allowAutomaticSelection = allowAutomaticSelection
    if allItems != None:
      self.allItems = allItems
    if allowMultiSelection != None:
      self.allowMultiSelection = allowMultiSelection
    if appendPosition != None:
      self.appendPosition = appendPosition
    if deselectAll != None:
      self.deselectAll = deselectAll
    if doubleClickCommand != None:
      self.doubleClickCommand = doubleClickCommand
    if deselectItem != None:
      self.deselectItem = deselectItem
    if deselectIndexedItem != None:
      self.deselectIndexedItem = deselectIndexedItem
    if deleteKeyCommand != None:
      self.deleteKeyCommand = deleteKeyCommand
    if font != None:
      self.font = font
    if numberOfItems != None:
      self.numberOfItems = numberOfItems
    if numberOfRows != None:
      self.numberOfRows = numberOfRows
    if numberOfSelectedItems != None:
      self.numberOfSelectedItems = numberOfSelectedItems
    if removeAll != None:
      self.removeAll = removeAll
    if removeItem != None:
      self.removeItem = removeItem
    if removeIndexedItem != None:
      self.removeIndexedItem = removeIndexedItem
    if selectCommand != None:
      self.selectCommand = selectCommand
    if showIndexedItem != None:
      self.showIndexedItem = showIndexedItem
    if selectItem != None:
      self.selectItem = selectItem
    if selectIndexedItem != None:
      self.selectIndexedItem = selectIndexedItem

  ##### getFuncCode #####
  def getappend( self ):
    return cmds.textScrollList( self.uiName , q=1 , append=1 )
  def getallowAutomaticSelection( self ):
    return cmds.textScrollList( self.uiName , q=1 , allowAutomaticSelection=1 )
  def getallItems( self ):
    return cmds.textScrollList( self.uiName , q=1 , allItems=1 )
  def getallowMultiSelection( self ):
    return cmds.textScrollList( self.uiName , q=1 , allowMultiSelection=1 )
  def getappendPosition( self ):
    return cmds.textScrollList( self.uiName , q=1 , appendPosition=1 )
  def getdeselectAll( self ):
    return cmds.textScrollList( self.uiName , q=1 , deselectAll=1 )
  def getdoubleClickCommand( self ):
    return cmds.textScrollList( self.uiName , q=1 , doubleClickCommand=1 )
  def getdeselectItem( self ):
    return cmds.textScrollList( self.uiName , q=1 , deselectItem=1 )
  def getdeselectIndexedItem( self ):
    return cmds.textScrollList( self.uiName , q=1 , deselectIndexedItem=1 )
  def getdeleteKeyCommand( self ):
    return cmds.textScrollList( self.uiName , q=1 , deleteKeyCommand=1 )
  def getfont( self ):
    return cmds.textScrollList( self.uiName , q=1 , font=1 )
  def getnumberOfItems( self ):
    return cmds.textScrollList( self.uiName , q=1 , numberOfItems=1 )
  def getnumberOfRows( self ):
    return cmds.textScrollList( self.uiName , q=1 , numberOfRows=1 )
  def getnumberOfSelectedItems( self ):
    return cmds.textScrollList( self.uiName , q=1 , numberOfSelectedItems=1 )
  def getremoveAll( self ):
    return cmds.textScrollList( self.uiName , q=1 , removeAll=1 )
  def getremoveItem( self ):
    return cmds.textScrollList( self.uiName , q=1 , removeItem=1 )
  def getremoveIndexedItem( self ):
    return cmds.textScrollList( self.uiName , q=1 , removeIndexedItem=1 )
  def getselectCommand( self ):
    return cmds.textScrollList( self.uiName , q=1 , selectCommand=1 )
  def getshowIndexedItem( self ):
    return cmds.textScrollList( self.uiName , q=1 , showIndexedItem=1 )
  def getselectItem( self ):
    return cmds.textScrollList( self.uiName , q=1 , selectItem=1 )
  def getselectIndexedItem( self ):
    return cmds.textScrollList( self.uiName , q=1 , selectIndexedItem=1 )

  ##### setFuncCode #####
  def setappend( self , value ):
    cmds.textScrollList( self.uiName , e=1 , append=value )
  def setallowAutomaticSelection( self , value ):
    cmds.textScrollList( self.uiName , e=1 , allowAutomaticSelection=value )
  def setallItems( self , value ):
    cmds.textScrollList( self.uiName , e=1 , allItems=value )
  def setallowMultiSelection( self , value ):
    cmds.textScrollList( self.uiName , e=1 , allowMultiSelection=value )
  def setappendPosition( self , value ):
    cmds.textScrollList( self.uiName , e=1 , appendPosition=value )
  def setdeselectAll( self , value ):
    cmds.textScrollList( self.uiName , e=1 , deselectAll=value )
  def setdoubleClickCommand( self , value ):
    cmds.textScrollList( self.uiName , e=1 , doubleClickCommand=value )
  def setdeselectItem( self , value ):
    cmds.textScrollList( self.uiName , e=1 , deselectItem=value )
  def setdeselectIndexedItem( self , value ):
    cmds.textScrollList( self.uiName , e=1 , deselectIndexedItem=value )
  def setdeleteKeyCommand( self , value ):
    cmds.textScrollList( self.uiName , e=1 , deleteKeyCommand=value )
  def setfont( self , value ):
    cmds.textScrollList( self.uiName , e=1 , font=value )
  def setnumberOfItems( self , value ):
    cmds.textScrollList( self.uiName , e=1 , numberOfItems=value )
  def setnumberOfRows( self , value ):
    cmds.textScrollList( self.uiName , e=1 , numberOfRows=value )
  def setnumberOfSelectedItems( self , value ):
    cmds.textScrollList( self.uiName , e=1 , numberOfSelectedItems=value )
  def setremoveAll( self , value ):
    cmds.textScrollList( self.uiName , e=1 , removeAll=value )
  def setremoveItem( self , value ):
    cmds.textScrollList( self.uiName , e=1 , removeItem=value )
  def setremoveIndexedItem( self , value ):
    cmds.textScrollList( self.uiName , e=1 , removeIndexedItem=value )
  def setselectCommand( self , value ):
    cmds.textScrollList( self.uiName , e=1 , selectCommand=value )
  def setshowIndexedItem( self , value ):
    cmds.textScrollList( self.uiName , e=1 , showIndexedItem=value )
  def setselectItem( self , value ):
    cmds.textScrollList( self.uiName , e=1 , selectItem=value )
  def setselectIndexedItem( self , value ):
    cmds.textScrollList( self.uiName , e=1 , selectIndexedItem=value )

  ##### propertyCode #####
  append = property( getappend , setappend )
  allowAutomaticSelection = property( getallowAutomaticSelection , setallowAutomaticSelection )
  allItems = property( getallItems , setallItems )
  allowMultiSelection = property( getallowMultiSelection , setallowMultiSelection )
  appendPosition = property( getappendPosition , setappendPosition )
  deselectAll = property( getdeselectAll , setdeselectAll )
  doubleClickCommand = property( getdoubleClickCommand , setdoubleClickCommand )
  deselectItem = property( getdeselectItem , setdeselectItem )
  deselectIndexedItem = property( getdeselectIndexedItem , setdeselectIndexedItem )
  deleteKeyCommand = property( getdeleteKeyCommand , setdeleteKeyCommand )
  font = property( getfont , setfont )
  numberOfItems = property( getnumberOfItems , setnumberOfItems )
  numberOfRows = property( getnumberOfRows , setnumberOfRows )
  numberOfSelectedItems = property( getnumberOfSelectedItems , setnumberOfSelectedItems )
  removeAll = property( getremoveAll , setremoveAll )
  removeItem = property( getremoveItem , setremoveItem )
  removeIndexedItem = property( getremoveIndexedItem , setremoveIndexedItem )
  selectCommand = property( getselectCommand , setselectCommand )
  showIndexedItem = property( getshowIndexedItem , setshowIndexedItem )
  selectItem = property( getselectItem , setselectItem )
  selectIndexedItem = property( getselectIndexedItem , setselectIndexedItem )

  ##### customCode #####
  def set( self , setItems ):
    self.clear()
    self.add( setItems )

  def add( self , addItems ):
    for addItem in addItems:
      self.append = addItem

  def replace( self , srcItem , dstItem ):
    existItems = self.allItems

    if existItems != None:
      counter = 0
      for existItem in existItems:
        if srcItem == existItem:
          self.removeIndexedItem = counter+1
          self.appendPosition    = [ counter+1 , dstItem ]
        counter  += 1

  def delete( self , deleteItem ):
    existItems = self.allItems
    deleteIndices = []

    if existItems != None:
      counter = 0
      for existItem in existItems:
        if existItem == deleteItem:
          deleteIndices.append( counter+1 )
        counter  += 1
    self.removeIndexedItem = sorted( deleteIndices , reverse=1 )

  def clear( self ):
    TSLItems = self.allItems
    if TSLItems != None:
      self.removeAll = 1

  def sort( self , reverse=0 ):
    TSLItems = self.allItems
    if TSLItems != None:
      self.set( sorted( TSLItems , reverse=reverse ) )




















#######################
##### NOT USUALLY #####
#######################

class Canvas( Control ):

  ##### initialize #####
  def __init__( self , hsvValue=None , pressCommand=None , rgbValue=None , **args ):
    self.uiName = cmds.canvas()

    ##### substitution #####
    if hsvValue != None:
      self.hsvValue = hsvValue
    if pressCommand != None:
      self.pressCommand = pressCommand
    if rgbValue != None:
      self.rgbValue = rgbValue

  ##### getFuncCode #####
  def gethsvValue( self ):
    return cmds.canvas( self.uiName , q=1 , hsvValue=1 )
  def getpressCommand( self ):
    return cmds.canvas( self.uiName , q=1 , pressCommand=1 )
  def getrgbValue( self ):
    return cmds.canvas( self.uiName , q=1 , rgbValue=1 )

  ##### setFuncCode #####
  def sethsvValue( self , value ):
    cmds.canvas( self.uiName , e=1 , hsvValue=value )
  def setpressCommand( self , value ):
    cmds.canvas( self.uiName , e=1 , pressCommand=value )
  def setrgbValue( self , value ):
    cmds.canvas( self.uiName , e=1 , rgbValue=value )

  ##### propertyCode #####
  hsvValue = property( gethsvValue , sethsvValue )
  pressCommand = property( getpressCommand , setpressCommand )
  rgbValue = property( getrgbValue , setrgbValue )

  ##### customCode #####





class ChannelBox( Control ):

  ##### initialize #####
  def __init__( self , attrColor=None , attributeEditorMode=None , attrFilter=None , attrRegex=None , attrBgColor=None , containerAtTop=None , enableLabelSelection=None , execute=None , fixedAttrList=None , fieldWidth=None , historyObjectList=None , hyperbolic=None , longNames=None , labelWidth=None , maxHeight=None , mainListConnection=None , useManips=None , mainObjectList=None , maxWidth=None , niceNames=None , nodeRegex=None , outputObjectList=None , precision=None , selectedHistoryAttributes=None , selectedMainAttributes=None , showNamespace=None , selectedOutputAttributes=None , shapeObjectList=None , speed=None , selectedShapeAttributes=None , showTransforms=None , takeFocus=None , update=None , **args ):
    self.uiName = cmds.channelBox()

    ##### substitution #####
    if attrColor != None:
      self.attrColor = attrColor
    if attributeEditorMode != None:
      self.attributeEditorMode = attributeEditorMode
    if attrFilter != None:
      self.attrFilter = attrFilter
    if attrRegex != None:
      self.attrRegex = attrRegex
    if attrBgColor != None:
      self.attrBgColor = attrBgColor
    if containerAtTop != None:
      self.containerAtTop = containerAtTop
    if enableLabelSelection != None:
      self.enableLabelSelection = enableLabelSelection
    if execute != None:
      self.execute = execute
    if fixedAttrList != None:
      self.fixedAttrList = fixedAttrList
    if fieldWidth != None:
      self.fieldWidth = fieldWidth
    if historyObjectList != None:
      self.historyObjectList = historyObjectList
    if hyperbolic != None:
      self.hyperbolic = hyperbolic
    if longNames != None:
      self.longNames = longNames
    if labelWidth != None:
      self.labelWidth = labelWidth
    if maxHeight != None:
      self.maxHeight = maxHeight
    if mainListConnection != None:
      self.mainListConnection = mainListConnection
    if useManips != None:
      self.useManips = useManips
    if mainObjectList != None:
      self.mainObjectList = mainObjectList
    if maxWidth != None:
      self.maxWidth = maxWidth
    if niceNames != None:
      self.niceNames = niceNames
    if nodeRegex != None:
      self.nodeRegex = nodeRegex
    if outputObjectList != None:
      self.outputObjectList = outputObjectList
    if precision != None:
      self.precision = precision
    if selectedHistoryAttributes != None:
      self.selectedHistoryAttributes = selectedHistoryAttributes
    if selectedMainAttributes != None:
      self.selectedMainAttributes = selectedMainAttributes
    if showNamespace != None:
      self.showNamespace = showNamespace
    if selectedOutputAttributes != None:
      self.selectedOutputAttributes = selectedOutputAttributes
    if shapeObjectList != None:
      self.shapeObjectList = shapeObjectList
    if speed != None:
      self.speed = speed
    if selectedShapeAttributes != None:
      self.selectedShapeAttributes = selectedShapeAttributes
    if showTransforms != None:
      self.showTransforms = showTransforms
    if takeFocus != None:
      self.takeFocus = takeFocus
    if update != None:
      self.update = update

  ##### getFuncCode #####
  def getattrColor( self ):
    return cmds.channelBox( self.uiName , q=1 , attrColor=1 )
  def getattributeEditorMode( self ):
    return cmds.channelBox( self.uiName , q=1 , attributeEditorMode=1 )
  def getattrFilter( self ):
    return cmds.channelBox( self.uiName , q=1 , attrFilter=1 )
  def getattrRegex( self ):
    return cmds.channelBox( self.uiName , q=1 , attrRegex=1 )
  def getattrBgColor( self ):
    return cmds.channelBox( self.uiName , q=1 , attrBgColor=1 )
  def getcontainerAtTop( self ):
    return cmds.channelBox( self.uiName , q=1 , containerAtTop=1 )
  def getenableLabelSelection( self ):
    return cmds.channelBox( self.uiName , q=1 , enableLabelSelection=1 )
  def getexecute( self ):
    return cmds.channelBox( self.uiName , q=1 , execute=1 )
  def getfixedAttrList( self ):
    return cmds.channelBox( self.uiName , q=1 , fixedAttrList=1 )
  def getfieldWidth( self ):
    return cmds.channelBox( self.uiName , q=1 , fieldWidth=1 )
  def gethistoryObjectList( self ):
    return cmds.channelBox( self.uiName , q=1 , historyObjectList=1 )
  def gethyperbolic( self ):
    return cmds.channelBox( self.uiName , q=1 , hyperbolic=1 )
  def getlongNames( self ):
    return cmds.channelBox( self.uiName , q=1 , longNames=1 )
  def getlabelWidth( self ):
    return cmds.channelBox( self.uiName , q=1 , labelWidth=1 )
  def getmaxHeight( self ):
    return cmds.channelBox( self.uiName , q=1 , maxHeight=1 )
  def getmainListConnection( self ):
    return cmds.channelBox( self.uiName , q=1 , mainListConnection=1 )
  def getuseManips( self ):
    return cmds.channelBox( self.uiName , q=1 , useManips=1 )
  def getmainObjectList( self ):
    return cmds.channelBox( self.uiName , q=1 , mainObjectList=1 )
  def getmaxWidth( self ):
    return cmds.channelBox( self.uiName , q=1 , maxWidth=1 )
  def getniceNames( self ):
    return cmds.channelBox( self.uiName , q=1 , niceNames=1 )
  def getnodeRegex( self ):
    return cmds.channelBox( self.uiName , q=1 , nodeRegex=1 )
  def getoutputObjectList( self ):
    return cmds.channelBox( self.uiName , q=1 , outputObjectList=1 )
  def getprecision( self ):
    return cmds.channelBox( self.uiName , q=1 , precision=1 )
  def getselectedHistoryAttributes( self ):
    return cmds.channelBox( self.uiName , q=1 , selectedHistoryAttributes=1 )
  def getselectedMainAttributes( self ):
    return cmds.channelBox( self.uiName , q=1 , selectedMainAttributes=1 )
  def getshowNamespace( self ):
    return cmds.channelBox( self.uiName , q=1 , showNamespace=1 )
  def getselectedOutputAttributes( self ):
    return cmds.channelBox( self.uiName , q=1 , selectedOutputAttributes=1 )
  def getshapeObjectList( self ):
    return cmds.channelBox( self.uiName , q=1 , shapeObjectList=1 )
  def getspeed( self ):
    return cmds.channelBox( self.uiName , q=1 , speed=1 )
  def getselectedShapeAttributes( self ):
    return cmds.channelBox( self.uiName , q=1 , selectedShapeAttributes=1 )
  def getshowTransforms( self ):
    return cmds.channelBox( self.uiName , q=1 , showTransforms=1 )
  def gettakeFocus( self ):
    return cmds.channelBox( self.uiName , q=1 , takeFocus=1 )
  def getupdate( self ):
    return cmds.channelBox( self.uiName , q=1 , update=1 )

  ##### setFuncCode #####
  def setattrColor( self , value ):
    cmds.channelBox( self.uiName , e=1 , attrColor=value )
  def setattributeEditorMode( self , value ):
    cmds.channelBox( self.uiName , e=1 , attributeEditorMode=value )
  def setattrFilter( self , value ):
    cmds.channelBox( self.uiName , e=1 , attrFilter=value )
  def setattrRegex( self , value ):
    cmds.channelBox( self.uiName , e=1 , attrRegex=value )
  def setattrBgColor( self , value ):
    cmds.channelBox( self.uiName , e=1 , attrBgColor=value )
  def setcontainerAtTop( self , value ):
    cmds.channelBox( self.uiName , e=1 , containerAtTop=value )
  def setenableLabelSelection( self , value ):
    cmds.channelBox( self.uiName , e=1 , enableLabelSelection=value )
  def setexecute( self , value ):
    cmds.channelBox( self.uiName , e=1 , execute=value )
  def setfixedAttrList( self , value ):
    cmds.channelBox( self.uiName , e=1 , fixedAttrList=value )
  def setfieldWidth( self , value ):
    cmds.channelBox( self.uiName , e=1 , fieldWidth=value )
  def sethistoryObjectList( self , value ):
    cmds.channelBox( self.uiName , e=1 , historyObjectList=value )
  def sethyperbolic( self , value ):
    cmds.channelBox( self.uiName , e=1 , hyperbolic=value )
  def setlongNames( self , value ):
    cmds.channelBox( self.uiName , e=1 , longNames=value )
  def setlabelWidth( self , value ):
    cmds.channelBox( self.uiName , e=1 , labelWidth=value )
  def setmaxHeight( self , value ):
    cmds.channelBox( self.uiName , e=1 , maxHeight=value )
  def setmainListConnection( self , value ):
    cmds.channelBox( self.uiName , e=1 , mainListConnection=value )
  def setuseManips( self , value ):
    cmds.channelBox( self.uiName , e=1 , useManips=value )
  def setmainObjectList( self , value ):
    cmds.channelBox( self.uiName , e=1 , mainObjectList=value )
  def setmaxWidth( self , value ):
    cmds.channelBox( self.uiName , e=1 , maxWidth=value )
  def setniceNames( self , value ):
    cmds.channelBox( self.uiName , e=1 , niceNames=value )
  def setnodeRegex( self , value ):
    cmds.channelBox( self.uiName , e=1 , nodeRegex=value )
  def setoutputObjectList( self , value ):
    cmds.channelBox( self.uiName , e=1 , outputObjectList=value )
  def setprecision( self , value ):
    cmds.channelBox( self.uiName , e=1 , precision=value )
  def setselectedHistoryAttributes( self , value ):
    cmds.channelBox( self.uiName , e=1 , selectedHistoryAttributes=value )
  def setselectedMainAttributes( self , value ):
    cmds.channelBox( self.uiName , e=1 , selectedMainAttributes=value )
  def setshowNamespace( self , value ):
    cmds.channelBox( self.uiName , e=1 , showNamespace=value )
  def setselectedOutputAttributes( self , value ):
    cmds.channelBox( self.uiName , e=1 , selectedOutputAttributes=value )
  def setshapeObjectList( self , value ):
    cmds.channelBox( self.uiName , e=1 , shapeObjectList=value )
  def setspeed( self , value ):
    cmds.channelBox( self.uiName , e=1 , speed=value )
  def setselectedShapeAttributes( self , value ):
    cmds.channelBox( self.uiName , e=1 , selectedShapeAttributes=value )
  def setshowTransforms( self , value ):
    cmds.channelBox( self.uiName , e=1 , showTransforms=value )
  def settakeFocus( self , value ):
    cmds.channelBox( self.uiName , e=1 , takeFocus=value )
  def setupdate( self , value ):
    cmds.channelBox( self.uiName , e=1 , update=value )

  ##### propertyCode #####
  attrColor = property( getattrColor , setattrColor )
  attributeEditorMode = property( getattributeEditorMode , setattributeEditorMode )
  attrFilter = property( getattrFilter , setattrFilter )
  attrRegex = property( getattrRegex , setattrRegex )
  attrBgColor = property( getattrBgColor , setattrBgColor )
  containerAtTop = property( getcontainerAtTop , setcontainerAtTop )
  enableLabelSelection = property( getenableLabelSelection , setenableLabelSelection )
  execute = property( getexecute , setexecute )
  fixedAttrList = property( getfixedAttrList , setfixedAttrList )
  fieldWidth = property( getfieldWidth , setfieldWidth )
  historyObjectList = property( gethistoryObjectList , sethistoryObjectList )
  hyperbolic = property( gethyperbolic , sethyperbolic )
  longNames = property( getlongNames , setlongNames )
  labelWidth = property( getlabelWidth , setlabelWidth )
  maxHeight = property( getmaxHeight , setmaxHeight )
  mainListConnection = property( getmainListConnection , setmainListConnection )
  useManips = property( getuseManips , setuseManips )
  mainObjectList = property( getmainObjectList , setmainObjectList )
  maxWidth = property( getmaxWidth , setmaxWidth )
  niceNames = property( getniceNames , setniceNames )
  nodeRegex = property( getnodeRegex , setnodeRegex )
  outputObjectList = property( getoutputObjectList , setoutputObjectList )
  precision = property( getprecision , setprecision )
  selectedHistoryAttributes = property( getselectedHistoryAttributes , setselectedHistoryAttributes )
  selectedMainAttributes = property( getselectedMainAttributes , setselectedMainAttributes )
  showNamespace = property( getshowNamespace , setshowNamespace )
  selectedOutputAttributes = property( getselectedOutputAttributes , setselectedOutputAttributes )
  shapeObjectList = property( getshapeObjectList , setshapeObjectList )
  speed = property( getspeed , setspeed )
  selectedShapeAttributes = property( getselectedShapeAttributes , setselectedShapeAttributes )
  showTransforms = property( getshowTransforms , setshowTransforms )
  takeFocus = property( gettakeFocus , settakeFocus )
  update = property( getupdate , setupdate )

  ##### customCode #####





class CmdScrollFieldExecuter( Control ):

  ##### initialize #####
  def __init__( self , appendText=None , currentLine=None , clear=None , copySelection=None , cutSelection=None , executeAll=None , execute=None , hasFocus=None , hasSelection=None , indentSelection=None , insertText=None , load=None , loadContents=None , pasteSelection=None , redo=None , receiveFocusCommand=None , replaceAll=None , removeStoredContents=None , searchAndSelect=None , searchDown=None , select=None , selectAll=None , showLineNumbers=None , selectedText=None , searchMatchCase=None , source=None , searchString=None , sourceType=None , storeContents=None , saveSelection=None , saveSelectionToShelf=None , text=None , textLength=None , undo=None , unindentSelection=None , **args ):
    self.uiName = cmds.cmdScrollFieldExecuter()

    ##### substitution #####
    if appendText != None:
      self.appendText = appendText
    if currentLine != None:
      self.currentLine = currentLine
    if clear != None:
      self.clear = clear
    if copySelection != None:
      self.copySelection = copySelection
    if cutSelection != None:
      self.cutSelection = cutSelection
    if executeAll != None:
      self.executeAll = executeAll
    if execute != None:
      self.execute = execute
    if hasFocus != None:
      self.hasFocus = hasFocus
    if hasSelection != None:
      self.hasSelection = hasSelection
    if indentSelection != None:
      self.indentSelection = indentSelection
    if insertText != None:
      self.insertText = insertText
    if load != None:
      self.load = load
    if loadContents != None:
      self.loadContents = loadContents
    if pasteSelection != None:
      self.pasteSelection = pasteSelection
    if redo != None:
      self.redo = redo
    if receiveFocusCommand != None:
      self.receiveFocusCommand = receiveFocusCommand
    if replaceAll != None:
      self.replaceAll = replaceAll
    if removeStoredContents != None:
      self.removeStoredContents = removeStoredContents
    if searchAndSelect != None:
      self.searchAndSelect = searchAndSelect
    if searchDown != None:
      self.searchDown = searchDown
    if select != None:
      self.select = select
    if selectAll != None:
      self.selectAll = selectAll
    if showLineNumbers != None:
      self.showLineNumbers = showLineNumbers
    if selectedText != None:
      self.selectedText = selectedText
    if searchMatchCase != None:
      self.searchMatchCase = searchMatchCase
    if source != None:
      self.source = source
    if searchString != None:
      self.searchString = searchString
    if sourceType != None:
      self.sourceType = sourceType
    if storeContents != None:
      self.storeContents = storeContents
    if saveSelection != None:
      self.saveSelection = saveSelection
    if saveSelectionToShelf != None:
      self.saveSelectionToShelf = saveSelectionToShelf
    if text != None:
      self.text = text
    if textLength != None:
      self.textLength = textLength
    if undo != None:
      self.undo = undo
    if unindentSelection != None:
      self.unindentSelection = unindentSelection

  ##### getFuncCode #####
  def getappendText( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , appendText=1 )
  def getcurrentLine( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , currentLine=1 )
  def getclear( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , clear=1 )
  def getcopySelection( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , copySelection=1 )
  def getcutSelection( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , cutSelection=1 )
  def getexecuteAll( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , executeAll=1 )
  def getexecute( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , execute=1 )
  def gethasFocus( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , hasFocus=1 )
  def gethasSelection( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , hasSelection=1 )
  def getindentSelection( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , indentSelection=1 )
  def getinsertText( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , insertText=1 )
  def getload( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , load=1 )
  def getloadContents( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , loadContents=1 )
  def getpasteSelection( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , pasteSelection=1 )
  def getredo( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , redo=1 )
  def getreceiveFocusCommand( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , receiveFocusCommand=1 )
  def getreplaceAll( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , replaceAll=1 )
  def getremoveStoredContents( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , removeStoredContents=1 )
  def getsearchAndSelect( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , searchAndSelect=1 )
  def getsearchDown( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , searchDown=1 )
  def getselect( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , select=1 )
  def getselectAll( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , selectAll=1 )
  def getshowLineNumbers( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , showLineNumbers=1 )
  def getselectedText( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , selectedText=1 )
  def getsearchMatchCase( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , searchMatchCase=1 )
  def getsource( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , source=1 )
  def getsearchString( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , searchString=1 )
  def getsourceType( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , sourceType=1 )
  def getstoreContents( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , storeContents=1 )
  def getsaveSelection( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , saveSelection=1 )
  def getsaveSelectionToShelf( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , saveSelectionToShelf=1 )
  def gettext( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , text=1 )
  def gettextLength( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , textLength=1 )
  def getundo( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , undo=1 )
  def getunindentSelection( self ):
    return cmds.cmdScrollFieldExecuter( self.uiName , q=1 , unindentSelection=1 )

  ##### setFuncCode #####
  def setappendText( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , appendText=value )
  def setcurrentLine( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , currentLine=value )
  def setclear( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , clear=value )
  def setcopySelection( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , copySelection=value )
  def setcutSelection( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , cutSelection=value )
  def setexecuteAll( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , executeAll=value )
  def setexecute( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , execute=value )
  def sethasFocus( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , hasFocus=value )
  def sethasSelection( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , hasSelection=value )
  def setindentSelection( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , indentSelection=value )
  def setinsertText( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , insertText=value )
  def setload( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , load=value )
  def setloadContents( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , loadContents=value )
  def setpasteSelection( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , pasteSelection=value )
  def setredo( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , redo=value )
  def setreceiveFocusCommand( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , receiveFocusCommand=value )
  def setreplaceAll( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , replaceAll=value )
  def setremoveStoredContents( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , removeStoredContents=value )
  def setsearchAndSelect( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , searchAndSelect=value )
  def setsearchDown( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , searchDown=value )
  def setselect( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , select=value )
  def setselectAll( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , selectAll=value )
  def setshowLineNumbers( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , showLineNumbers=value )
  def setselectedText( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , selectedText=value )
  def setsearchMatchCase( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , searchMatchCase=value )
  def setsource( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , source=value )
  def setsearchString( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , searchString=value )
  def setsourceType( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , sourceType=value )
  def setstoreContents( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , storeContents=value )
  def setsaveSelection( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , saveSelection=value )
  def setsaveSelectionToShelf( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , saveSelectionToShelf=value )
  def settext( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , text=value )
  def settextLength( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , textLength=value )
  def setundo( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , undo=value )
  def setunindentSelection( self , value ):
    cmds.cmdScrollFieldExecuter( self.uiName , e=1 , unindentSelection=value )

  ##### propertyCode #####
  appendText = property( getappendText , setappendText )
  currentLine = property( getcurrentLine , setcurrentLine )
  clear = property( getclear , setclear )
  copySelection = property( getcopySelection , setcopySelection )
  cutSelection = property( getcutSelection , setcutSelection )
  executeAll = property( getexecuteAll , setexecuteAll )
  execute = property( getexecute , setexecute )
  hasFocus = property( gethasFocus , sethasFocus )
  hasSelection = property( gethasSelection , sethasSelection )
  indentSelection = property( getindentSelection , setindentSelection )
  insertText = property( getinsertText , setinsertText )
  load = property( getload , setload )
  loadContents = property( getloadContents , setloadContents )
  pasteSelection = property( getpasteSelection , setpasteSelection )
  redo = property( getredo , setredo )
  receiveFocusCommand = property( getreceiveFocusCommand , setreceiveFocusCommand )
  replaceAll = property( getreplaceAll , setreplaceAll )
  removeStoredContents = property( getremoveStoredContents , setremoveStoredContents )
  searchAndSelect = property( getsearchAndSelect , setsearchAndSelect )
  searchDown = property( getsearchDown , setsearchDown )
  select = property( getselect , setselect )
  selectAll = property( getselectAll , setselectAll )
  showLineNumbers = property( getshowLineNumbers , setshowLineNumbers )
  selectedText = property( getselectedText , setselectedText )
  searchMatchCase = property( getsearchMatchCase , setsearchMatchCase )
  source = property( getsource , setsource )
  searchString = property( getsearchString , setsearchString )
  sourceType = property( getsourceType , setsourceType )
  storeContents = property( getstoreContents , setstoreContents )
  saveSelection = property( getsaveSelection , setsaveSelection )
  saveSelectionToShelf = property( getsaveSelectionToShelf , setsaveSelectionToShelf )
  text = property( gettext , settext )
  textLength = property( gettextLength , settextLength )
  undo = property( getundo , setundo )
  unindentSelection = property( getunindentSelection , setunindentSelection )

  ##### customCode #####





class CmdScrollFieldReporter( Control ):

  ##### initialize #####
  def __init__( self , clear=None , copySelection=None , cutSelection=None , echoAllCommands=None , filterSourceType=None , hasFocus=None , lineNumbers=None , pasteSelection=None , receiveFocusCommand=None , suppressErrors=None , suppressInfo=None , select=None , selectAll=None , suppressResults=None , suppressStackTrace=None , stackTrace=None , saveSelection=None , saveSelectionToShelf=None , suppressWarnings=None , text=None , textLength=None , **args ):
    self.uiName = cmds.cmdScrollFieldReporter()

    ##### substitution #####
    if clear != None:
      self.clear = clear
    if copySelection != None:
      self.copySelection = copySelection
    if cutSelection != None:
      self.cutSelection = cutSelection
    if echoAllCommands != None:
      self.echoAllCommands = echoAllCommands
    if filterSourceType != None:
      self.filterSourceType = filterSourceType
    if hasFocus != None:
      self.hasFocus = hasFocus
    if lineNumbers != None:
      self.lineNumbers = lineNumbers
    if pasteSelection != None:
      self.pasteSelection = pasteSelection
    if receiveFocusCommand != None:
      self.receiveFocusCommand = receiveFocusCommand
    if suppressErrors != None:
      self.suppressErrors = suppressErrors
    if suppressInfo != None:
      self.suppressInfo = suppressInfo
    if select != None:
      self.select = select
    if selectAll != None:
      self.selectAll = selectAll
    if suppressResults != None:
      self.suppressResults = suppressResults
    if suppressStackTrace != None:
      self.suppressStackTrace = suppressStackTrace
    if stackTrace != None:
      self.stackTrace = stackTrace
    if saveSelection != None:
      self.saveSelection = saveSelection
    if saveSelectionToShelf != None:
      self.saveSelectionToShelf = saveSelectionToShelf
    if suppressWarnings != None:
      self.suppressWarnings = suppressWarnings
    if text != None:
      self.text = text
    if textLength != None:
      self.textLength = textLength

  ##### getFuncCode #####
  def getclear( self ):
    return cmds.cmdScrollFieldReporter( self.uiName , q=1 , clear=1 )
  def getcopySelection( self ):
    return cmds.cmdScrollFieldReporter( self.uiName , q=1 , copySelection=1 )
  def getcutSelection( self ):
    return cmds.cmdScrollFieldReporter( self.uiName , q=1 , cutSelection=1 )
  def getechoAllCommands( self ):
    return cmds.cmdScrollFieldReporter( self.uiName , q=1 , echoAllCommands=1 )
  def getfilterSourceType( self ):
    return cmds.cmdScrollFieldReporter( self.uiName , q=1 , filterSourceType=1 )
  def gethasFocus( self ):
    return cmds.cmdScrollFieldReporter( self.uiName , q=1 , hasFocus=1 )
  def getlineNumbers( self ):
    return cmds.cmdScrollFieldReporter( self.uiName , q=1 , lineNumbers=1 )
  def getpasteSelection( self ):
    return cmds.cmdScrollFieldReporter( self.uiName , q=1 , pasteSelection=1 )
  def getreceiveFocusCommand( self ):
    return cmds.cmdScrollFieldReporter( self.uiName , q=1 , receiveFocusCommand=1 )
  def getsuppressErrors( self ):
    return cmds.cmdScrollFieldReporter( self.uiName , q=1 , suppressErrors=1 )
  def getsuppressInfo( self ):
    return cmds.cmdScrollFieldReporter( self.uiName , q=1 , suppressInfo=1 )
  def getselect( self ):
    return cmds.cmdScrollFieldReporter( self.uiName , q=1 , select=1 )
  def getselectAll( self ):
    return cmds.cmdScrollFieldReporter( self.uiName , q=1 , selectAll=1 )
  def getsuppressResults( self ):
    return cmds.cmdScrollFieldReporter( self.uiName , q=1 , suppressResults=1 )
  def getsuppressStackTrace( self ):
    return cmds.cmdScrollFieldReporter( self.uiName , q=1 , suppressStackTrace=1 )
  def getstackTrace( self ):
    return cmds.cmdScrollFieldReporter( self.uiName , q=1 , stackTrace=1 )
  def getsaveSelection( self ):
    return cmds.cmdScrollFieldReporter( self.uiName , q=1 , saveSelection=1 )
  def getsaveSelectionToShelf( self ):
    return cmds.cmdScrollFieldReporter( self.uiName , q=1 , saveSelectionToShelf=1 )
  def getsuppressWarnings( self ):
    return cmds.cmdScrollFieldReporter( self.uiName , q=1 , suppressWarnings=1 )
  def gettext( self ):
    return cmds.cmdScrollFieldReporter( self.uiName , q=1 , text=1 )
  def gettextLength( self ):
    return cmds.cmdScrollFieldReporter( self.uiName , q=1 , textLength=1 )

  ##### setFuncCode #####
  def setclear( self , value ):
    cmds.cmdScrollFieldReporter( self.uiName , e=1 , clear=value )
  def setcopySelection( self , value ):
    cmds.cmdScrollFieldReporter( self.uiName , e=1 , copySelection=value )
  def setcutSelection( self , value ):
    cmds.cmdScrollFieldReporter( self.uiName , e=1 , cutSelection=value )
  def setechoAllCommands( self , value ):
    cmds.cmdScrollFieldReporter( self.uiName , e=1 , echoAllCommands=value )
  def setfilterSourceType( self , value ):
    cmds.cmdScrollFieldReporter( self.uiName , e=1 , filterSourceType=value )
  def sethasFocus( self , value ):
    cmds.cmdScrollFieldReporter( self.uiName , e=1 , hasFocus=value )
  def setlineNumbers( self , value ):
    cmds.cmdScrollFieldReporter( self.uiName , e=1 , lineNumbers=value )
  def setpasteSelection( self , value ):
    cmds.cmdScrollFieldReporter( self.uiName , e=1 , pasteSelection=value )
  def setreceiveFocusCommand( self , value ):
    cmds.cmdScrollFieldReporter( self.uiName , e=1 , receiveFocusCommand=value )
  def setsuppressErrors( self , value ):
    cmds.cmdScrollFieldReporter( self.uiName , e=1 , suppressErrors=value )
  def setsuppressInfo( self , value ):
    cmds.cmdScrollFieldReporter( self.uiName , e=1 , suppressInfo=value )
  def setselect( self , value ):
    cmds.cmdScrollFieldReporter( self.uiName , e=1 , select=value )
  def setselectAll( self , value ):
    cmds.cmdScrollFieldReporter( self.uiName , e=1 , selectAll=value )
  def setsuppressResults( self , value ):
    cmds.cmdScrollFieldReporter( self.uiName , e=1 , suppressResults=value )
  def setsuppressStackTrace( self , value ):
    cmds.cmdScrollFieldReporter( self.uiName , e=1 , suppressStackTrace=value )
  def setstackTrace( self , value ):
    cmds.cmdScrollFieldReporter( self.uiName , e=1 , stackTrace=value )
  def setsaveSelection( self , value ):
    cmds.cmdScrollFieldReporter( self.uiName , e=1 , saveSelection=value )
  def setsaveSelectionToShelf( self , value ):
    cmds.cmdScrollFieldReporter( self.uiName , e=1 , saveSelectionToShelf=value )
  def setsuppressWarnings( self , value ):
    cmds.cmdScrollFieldReporter( self.uiName , e=1 , suppressWarnings=value )
  def settext( self , value ):
    cmds.cmdScrollFieldReporter( self.uiName , e=1 , text=value )
  def settextLength( self , value ):
    cmds.cmdScrollFieldReporter( self.uiName , e=1 , textLength=value )

  ##### propertyCode #####
  clear = property( getclear , setclear )
  copySelection = property( getcopySelection , setcopySelection )
  cutSelection = property( getcutSelection , setcutSelection )
  echoAllCommands = property( getechoAllCommands , setechoAllCommands )
  filterSourceType = property( getfilterSourceType , setfilterSourceType )
  hasFocus = property( gethasFocus , sethasFocus )
  lineNumbers = property( getlineNumbers , setlineNumbers )
  pasteSelection = property( getpasteSelection , setpasteSelection )
  receiveFocusCommand = property( getreceiveFocusCommand , setreceiveFocusCommand )
  suppressErrors = property( getsuppressErrors , setsuppressErrors )
  suppressInfo = property( getsuppressInfo , setsuppressInfo )
  select = property( getselect , setselect )
  selectAll = property( getselectAll , setselectAll )
  suppressResults = property( getsuppressResults , setsuppressResults )
  suppressStackTrace = property( getsuppressStackTrace , setsuppressStackTrace )
  stackTrace = property( getstackTrace , setstackTrace )
  saveSelection = property( getsaveSelection , setsaveSelection )
  saveSelectionToShelf = property( getsaveSelectionToShelf , setsaveSelectionToShelf )
  suppressWarnings = property( getsuppressWarnings , setsuppressWarnings )
  text = property( gettext , settext )
  textLength = property( gettextLength , settextLength )

  ##### customCode #####





class CmdShell( Control ):

  ##### initialize #####
  def __init__( self , command=None , clear=None , numberOfHistoryLines=None , numberOfSavedLines=None , prompt=None , **args ):
    self.uiName = cmds.cmdShell()

    ##### substitution #####
    if command != None:
      self.command = command
    if clear != None:
      self.clear = clear
    if numberOfHistoryLines != None:
      self.numberOfHistoryLines = numberOfHistoryLines
    if numberOfSavedLines != None:
      self.numberOfSavedLines = numberOfSavedLines
    if prompt != None:
      self.prompt = prompt

  ##### getFuncCode #####
  def getcommand( self ):
    return cmds.cmdShell( self.uiName , q=1 , command=1 )
  def getclear( self ):
    return cmds.cmdShell( self.uiName , q=1 , clear=1 )
  def getnumberOfHistoryLines( self ):
    return cmds.cmdShell( self.uiName , q=1 , numberOfHistoryLines=1 )
  def getnumberOfSavedLines( self ):
    return cmds.cmdShell( self.uiName , q=1 , numberOfSavedLines=1 )
  def getprompt( self ):
    return cmds.cmdShell( self.uiName , q=1 , prompt=1 )

  ##### setFuncCode #####
  def setcommand( self , value ):
    cmds.cmdShell( self.uiName , e=1 , command=value )
  def setclear( self , value ):
    cmds.cmdShell( self.uiName , e=1 , clear=value )
  def setnumberOfHistoryLines( self , value ):
    cmds.cmdShell( self.uiName , e=1 , numberOfHistoryLines=value )
  def setnumberOfSavedLines( self , value ):
    cmds.cmdShell( self.uiName , e=1 , numberOfSavedLines=value )
  def setprompt( self , value ):
    cmds.cmdShell( self.uiName , e=1 , prompt=value )

  ##### propertyCode #####
  command = property( getcommand , setcommand )
  clear = property( getclear , setclear )
  numberOfHistoryLines = property( getnumberOfHistoryLines , setnumberOfHistoryLines )
  numberOfSavedLines = property( getnumberOfSavedLines , setnumberOfSavedLines )
  prompt = property( getprompt , setprompt )

  ##### customCode #####





class CommandLine( Control ):

  ##### initialize #####
  def __init__( self , command=None , enterCommand=None , inputAnnotation=None , numberOfHistoryLines=None , outputAnnotation=None , sourceType=None , **args ):
    self.uiName = cmds.commandLine()

    ##### substitution #####
    if command != None:
      self.command = command
    if enterCommand != None:
      self.enterCommand = enterCommand
    if inputAnnotation != None:
      self.inputAnnotation = inputAnnotation
    if numberOfHistoryLines != None:
      self.numberOfHistoryLines = numberOfHistoryLines
    if outputAnnotation != None:
      self.outputAnnotation = outputAnnotation
    if sourceType != None:
      self.sourceType = sourceType

  ##### getFuncCode #####
  def getcommand( self ):
    return cmds.commandLine( self.uiName , q=1 , command=1 )
  def getenterCommand( self ):
    return cmds.commandLine( self.uiName , q=1 , enterCommand=1 )
  def getinputAnnotation( self ):
    return cmds.commandLine( self.uiName , q=1 , inputAnnotation=1 )
  def getnumberOfHistoryLines( self ):
    return cmds.commandLine( self.uiName , q=1 , numberOfHistoryLines=1 )
  def getoutputAnnotation( self ):
    return cmds.commandLine( self.uiName , q=1 , outputAnnotation=1 )
  def getsourceType( self ):
    return cmds.commandLine( self.uiName , q=1 , sourceType=1 )

  ##### setFuncCode #####
  def setcommand( self , value ):
    cmds.commandLine( self.uiName , e=1 , command=value )
  def setenterCommand( self , value ):
    cmds.commandLine( self.uiName , e=1 , enterCommand=value )
  def setinputAnnotation( self , value ):
    cmds.commandLine( self.uiName , e=1 , inputAnnotation=value )
  def setnumberOfHistoryLines( self , value ):
    cmds.commandLine( self.uiName , e=1 , numberOfHistoryLines=value )
  def setoutputAnnotation( self , value ):
    cmds.commandLine( self.uiName , e=1 , outputAnnotation=value )
  def setsourceType( self , value ):
    cmds.commandLine( self.uiName , e=1 , sourceType=value )

  ##### propertyCode #####
  command = property( getcommand , setcommand )
  enterCommand = property( getenterCommand , setenterCommand )
  inputAnnotation = property( getinputAnnotation , setinputAnnotation )
  numberOfHistoryLines = property( getnumberOfHistoryLines , setnumberOfHistoryLines )
  outputAnnotation = property( getoutputAnnotation , setoutputAnnotation )
  sourceType = property( getsourceType , setsourceType )

  ##### customCode #####





class FloatScrollBar( Control ):

  ##### initialize #####
  def __init__( self , changeCommand=None , dragCommand=None , horizontal=None , largeStep=None , maxValue=None , minValue=None , step=None , value=None , **args ):
    self.uiName = cmds.floatScrollBar()

    ##### substitution #####
    if changeCommand != None:
      self.changeCommand = changeCommand
    if dragCommand != None:
      self.dragCommand = dragCommand
    if horizontal != None:
      self.horizontal = horizontal
    if largeStep != None:
      self.largeStep = largeStep
    if maxValue != None:
      self.maxValue = maxValue
    if minValue != None:
      self.minValue = minValue
    if step != None:
      self.step = step
    if value != None:
      self.value = value

  ##### getFuncCode #####
  def getchangeCommand( self ):
    return cmds.floatScrollBar( self.uiName , q=1 , changeCommand=1 )
  def getdragCommand( self ):
    return cmds.floatScrollBar( self.uiName , q=1 , dragCommand=1 )
  def gethorizontal( self ):
    return cmds.floatScrollBar( self.uiName , q=1 , horizontal=1 )
  def getlargeStep( self ):
    return cmds.floatScrollBar( self.uiName , q=1 , largeStep=1 )
  def getmaxValue( self ):
    return cmds.floatScrollBar( self.uiName , q=1 , maxValue=1 )
  def getminValue( self ):
    return cmds.floatScrollBar( self.uiName , q=1 , minValue=1 )
  def getstep( self ):
    return cmds.floatScrollBar( self.uiName , q=1 , step=1 )
  def getvalue( self ):
    return cmds.floatScrollBar( self.uiName , q=1 , value=1 )

  ##### setFuncCode #####
  def setchangeCommand( self , value ):
    cmds.floatScrollBar( self.uiName , e=1 , changeCommand=value )
  def setdragCommand( self , value ):
    cmds.floatScrollBar( self.uiName , e=1 , dragCommand=value )
  def sethorizontal( self , value ):
    cmds.floatScrollBar( self.uiName , e=1 , horizontal=value )
  def setlargeStep( self , value ):
    cmds.floatScrollBar( self.uiName , e=1 , largeStep=value )
  def setmaxValue( self , value ):
    cmds.floatScrollBar( self.uiName , e=1 , maxValue=value )
  def setminValue( self , value ):
    cmds.floatScrollBar( self.uiName , e=1 , minValue=value )
  def setstep( self , value ):
    cmds.floatScrollBar( self.uiName , e=1 , step=value )
  def setvalue( self , value ):
    cmds.floatScrollBar( self.uiName , e=1 , value=value )

  ##### propertyCode #####
  changeCommand = property( getchangeCommand , setchangeCommand )
  dragCommand = property( getdragCommand , setdragCommand )
  horizontal = property( gethorizontal , sethorizontal )
  largeStep = property( getlargeStep , setlargeStep )
  maxValue = property( getmaxValue , setmaxValue )
  minValue = property( getminValue , setminValue )
  step = property( getstep , setstep )
  value = property( getvalue , setvalue )

  ##### customCode #####





class GradientControl( Control ):

  ##### initialize #####
  def __init__( self , adaptiveScaling=None , attribute=None , numberOfControls=None , refreshOnRelease=None , selectedColorControl=None , selectedInterpControl=None , staticNumberOfControls=None , staticPositions=None , selectedPositionControl=None , upperLimitControl=None , verticalLayout=None , **args ):
    self.uiName = cmds.gradientControl()

    ##### substitution #####
    if adaptiveScaling != None:
      self.adaptiveScaling = adaptiveScaling
    if attribute != None:
      self.attribute = attribute
    if numberOfControls != None:
      self.numberOfControls = numberOfControls
    if refreshOnRelease != None:
      self.refreshOnRelease = refreshOnRelease
    if selectedColorControl != None:
      self.selectedColorControl = selectedColorControl
    if selectedInterpControl != None:
      self.selectedInterpControl = selectedInterpControl
    if staticNumberOfControls != None:
      self.staticNumberOfControls = staticNumberOfControls
    if staticPositions != None:
      self.staticPositions = staticPositions
    if selectedPositionControl != None:
      self.selectedPositionControl = selectedPositionControl
    if upperLimitControl != None:
      self.upperLimitControl = upperLimitControl
    if verticalLayout != None:
      self.verticalLayout = verticalLayout

  ##### getFuncCode #####
  def getadaptiveScaling( self ):
    return cmds.gradientControl( self.uiName , q=1 , adaptiveScaling=1 )
  def getattribute( self ):
    return cmds.gradientControl( self.uiName , q=1 , attribute=1 )
  def getnumberOfControls( self ):
    return cmds.gradientControl( self.uiName , q=1 , numberOfControls=1 )
  def getrefreshOnRelease( self ):
    return cmds.gradientControl( self.uiName , q=1 , refreshOnRelease=1 )
  def getselectedColorControl( self ):
    return cmds.gradientControl( self.uiName , q=1 , selectedColorControl=1 )
  def getselectedInterpControl( self ):
    return cmds.gradientControl( self.uiName , q=1 , selectedInterpControl=1 )
  def getstaticNumberOfControls( self ):
    return cmds.gradientControl( self.uiName , q=1 , staticNumberOfControls=1 )
  def getstaticPositions( self ):
    return cmds.gradientControl( self.uiName , q=1 , staticPositions=1 )
  def getselectedPositionControl( self ):
    return cmds.gradientControl( self.uiName , q=1 , selectedPositionControl=1 )
  def getupperLimitControl( self ):
    return cmds.gradientControl( self.uiName , q=1 , upperLimitControl=1 )
  def getverticalLayout( self ):
    return cmds.gradientControl( self.uiName , q=1 , verticalLayout=1 )

  ##### setFuncCode #####
  def setadaptiveScaling( self , value ):
    cmds.gradientControl( self.uiName , e=1 , adaptiveScaling=value )
  def setattribute( self , value ):
    cmds.gradientControl( self.uiName , e=1 , attribute=value )
  def setnumberOfControls( self , value ):
    cmds.gradientControl( self.uiName , e=1 , numberOfControls=value )
  def setrefreshOnRelease( self , value ):
    cmds.gradientControl( self.uiName , e=1 , refreshOnRelease=value )
  def setselectedColorControl( self , value ):
    cmds.gradientControl( self.uiName , e=1 , selectedColorControl=value )
  def setselectedInterpControl( self , value ):
    cmds.gradientControl( self.uiName , e=1 , selectedInterpControl=value )
  def setstaticNumberOfControls( self , value ):
    cmds.gradientControl( self.uiName , e=1 , staticNumberOfControls=value )
  def setstaticPositions( self , value ):
    cmds.gradientControl( self.uiName , e=1 , staticPositions=value )
  def setselectedPositionControl( self , value ):
    cmds.gradientControl( self.uiName , e=1 , selectedPositionControl=value )
  def setupperLimitControl( self , value ):
    cmds.gradientControl( self.uiName , e=1 , upperLimitControl=value )
  def setverticalLayout( self , value ):
    cmds.gradientControl( self.uiName , e=1 , verticalLayout=value )

  ##### propertyCode #####
  adaptiveScaling = property( getadaptiveScaling , setadaptiveScaling )
  attribute = property( getattribute , setattribute )
  numberOfControls = property( getnumberOfControls , setnumberOfControls )
  refreshOnRelease = property( getrefreshOnRelease , setrefreshOnRelease )
  selectedColorControl = property( getselectedColorControl , setselectedColorControl )
  selectedInterpControl = property( getselectedInterpControl , setselectedInterpControl )
  staticNumberOfControls = property( getstaticNumberOfControls , setstaticNumberOfControls )
  staticPositions = property( getstaticPositions , setstaticPositions )
  selectedPositionControl = property( getselectedPositionControl , setselectedPositionControl )
  upperLimitControl = property( getupperLimitControl , setupperLimitControl )
  verticalLayout = property( getverticalLayout , setverticalLayout )

  ##### customCode #####





class GradientControlNoAttr( Control ):

  ##### initialize #####
  def __init__( self , asString=None , changeCommand=None , currentKeyInterpValue=None , currentKey=None , currentKeyChanged=None , currentKeyColorValue=None , currentKeyCurveValue=None , dragCommand=None , optionVar=None , rampAsColor=None , valueAtPoint=None , **args ):
    self.uiName = cmds.gradientControlNoAttr()

    ##### substitution #####
    if asString != None:
      self.asString = asString
    if changeCommand != None:
      self.changeCommand = changeCommand
    if currentKeyInterpValue != None:
      self.currentKeyInterpValue = currentKeyInterpValue
    if currentKey != None:
      self.currentKey = currentKey
    if currentKeyChanged != None:
      self.currentKeyChanged = currentKeyChanged
    if currentKeyColorValue != None:
      self.currentKeyColorValue = currentKeyColorValue
    if currentKeyCurveValue != None:
      self.currentKeyCurveValue = currentKeyCurveValue
    if dragCommand != None:
      self.dragCommand = dragCommand
    if optionVar != None:
      self.optionVar = optionVar
    if rampAsColor != None:
      self.rampAsColor = rampAsColor
    if valueAtPoint != None:
      self.valueAtPoint = valueAtPoint

  ##### getFuncCode #####
  def getasString( self ):
    return cmds.gradientControlNoAttr( self.uiName , q=1 , asString=1 )
  def getchangeCommand( self ):
    return cmds.gradientControlNoAttr( self.uiName , q=1 , changeCommand=1 )
  def getcurrentKeyInterpValue( self ):
    return cmds.gradientControlNoAttr( self.uiName , q=1 , currentKeyInterpValue=1 )
  def getcurrentKey( self ):
    return cmds.gradientControlNoAttr( self.uiName , q=1 , currentKey=1 )
  def getcurrentKeyChanged( self ):
    return cmds.gradientControlNoAttr( self.uiName , q=1 , currentKeyChanged=1 )
  def getcurrentKeyColorValue( self ):
    return cmds.gradientControlNoAttr( self.uiName , q=1 , currentKeyColorValue=1 )
  def getcurrentKeyCurveValue( self ):
    return cmds.gradientControlNoAttr( self.uiName , q=1 , currentKeyCurveValue=1 )
  def getdragCommand( self ):
    return cmds.gradientControlNoAttr( self.uiName , q=1 , dragCommand=1 )
  def getoptionVar( self ):
    return cmds.gradientControlNoAttr( self.uiName , q=1 , optionVar=1 )
  def getrampAsColor( self ):
    return cmds.gradientControlNoAttr( self.uiName , q=1 , rampAsColor=1 )
  def getvalueAtPoint( self ):
    return cmds.gradientControlNoAttr( self.uiName , q=1 , valueAtPoint=1 )

  ##### setFuncCode #####
  def setasString( self , value ):
    cmds.gradientControlNoAttr( self.uiName , e=1 , asString=value )
  def setchangeCommand( self , value ):
    cmds.gradientControlNoAttr( self.uiName , e=1 , changeCommand=value )
  def setcurrentKeyInterpValue( self , value ):
    cmds.gradientControlNoAttr( self.uiName , e=1 , currentKeyInterpValue=value )
  def setcurrentKey( self , value ):
    cmds.gradientControlNoAttr( self.uiName , e=1 , currentKey=value )
  def setcurrentKeyChanged( self , value ):
    cmds.gradientControlNoAttr( self.uiName , e=1 , currentKeyChanged=value )
  def setcurrentKeyColorValue( self , value ):
    cmds.gradientControlNoAttr( self.uiName , e=1 , currentKeyColorValue=value )
  def setcurrentKeyCurveValue( self , value ):
    cmds.gradientControlNoAttr( self.uiName , e=1 , currentKeyCurveValue=value )
  def setdragCommand( self , value ):
    cmds.gradientControlNoAttr( self.uiName , e=1 , dragCommand=value )
  def setoptionVar( self , value ):
    cmds.gradientControlNoAttr( self.uiName , e=1 , optionVar=value )
  def setrampAsColor( self , value ):
    cmds.gradientControlNoAttr( self.uiName , e=1 , rampAsColor=value )
  def setvalueAtPoint( self , value ):
    cmds.gradientControlNoAttr( self.uiName , e=1 , valueAtPoint=value )

  ##### propertyCode #####
  asString = property( getasString , setasString )
  changeCommand = property( getchangeCommand , setchangeCommand )
  currentKeyInterpValue = property( getcurrentKeyInterpValue , setcurrentKeyInterpValue )
  currentKey = property( getcurrentKey , setcurrentKey )
  currentKeyChanged = property( getcurrentKeyChanged , setcurrentKeyChanged )
  currentKeyColorValue = property( getcurrentKeyColorValue , setcurrentKeyColorValue )
  currentKeyCurveValue = property( getcurrentKeyCurveValue , setcurrentKeyCurveValue )
  dragCommand = property( getdragCommand , setdragCommand )
  optionVar = property( getoptionVar , setoptionVar )
  rampAsColor = property( getrampAsColor , setrampAsColor )
  valueAtPoint = property( getvalueAtPoint , setvalueAtPoint )

  ##### customCode #####





class HelpLine( Control ):

  ##### initialize #####
  def __init__( self , **args ):
    self.uiName = cmds.helpLine()

    ##### substitution #####

  ##### getFuncCode #####

  ##### setFuncCode #####

  ##### propertyCode #####

  ##### customCode #####





class HudButton( Control ):

  ##### initialize #####
  def __init__( self , allowOverlap=None , block=None , blockAlignment=None , blockSize=None , buttonShape=None , buttonWidth=None , label=None , labelFontSize=None , padding=None , pressCommand=None , releaseCommand=None , section=None , **args ):
    self.uiName = cmds.hudButton()

    ##### substitution #####
    if allowOverlap != None:
      self.allowOverlap = allowOverlap
    if block != None:
      self.block = block
    if blockAlignment != None:
      self.blockAlignment = blockAlignment
    if blockSize != None:
      self.blockSize = blockSize
    if buttonShape != None:
      self.buttonShape = buttonShape
    if buttonWidth != None:
      self.buttonWidth = buttonWidth
    if label != None:
      self.label = label
    if labelFontSize != None:
      self.labelFontSize = labelFontSize
    if padding != None:
      self.padding = padding
    if pressCommand != None:
      self.pressCommand = pressCommand
    if releaseCommand != None:
      self.releaseCommand = releaseCommand
    if section != None:
      self.section = section

  ##### getFuncCode #####
  def getallowOverlap( self ):
    return cmds.hudButton( self.uiName , q=1 , allowOverlap=1 )
  def getblock( self ):
    return cmds.hudButton( self.uiName , q=1 , block=1 )
  def getblockAlignment( self ):
    return cmds.hudButton( self.uiName , q=1 , blockAlignment=1 )
  def getblockSize( self ):
    return cmds.hudButton( self.uiName , q=1 , blockSize=1 )
  def getbuttonShape( self ):
    return cmds.hudButton( self.uiName , q=1 , buttonShape=1 )
  def getbuttonWidth( self ):
    return cmds.hudButton( self.uiName , q=1 , buttonWidth=1 )
  def getlabel( self ):
    return cmds.hudButton( self.uiName , q=1 , label=1 )
  def getlabelFontSize( self ):
    return cmds.hudButton( self.uiName , q=1 , labelFontSize=1 )
  def getpadding( self ):
    return cmds.hudButton( self.uiName , q=1 , padding=1 )
  def getpressCommand( self ):
    return cmds.hudButton( self.uiName , q=1 , pressCommand=1 )
  def getreleaseCommand( self ):
    return cmds.hudButton( self.uiName , q=1 , releaseCommand=1 )
  def getsection( self ):
    return cmds.hudButton( self.uiName , q=1 , section=1 )

  ##### setFuncCode #####
  def setallowOverlap( self , value ):
    cmds.hudButton( self.uiName , e=1 , allowOverlap=value )
  def setblock( self , value ):
    cmds.hudButton( self.uiName , e=1 , block=value )
  def setblockAlignment( self , value ):
    cmds.hudButton( self.uiName , e=1 , blockAlignment=value )
  def setblockSize( self , value ):
    cmds.hudButton( self.uiName , e=1 , blockSize=value )
  def setbuttonShape( self , value ):
    cmds.hudButton( self.uiName , e=1 , buttonShape=value )
  def setbuttonWidth( self , value ):
    cmds.hudButton( self.uiName , e=1 , buttonWidth=value )
  def setlabel( self , value ):
    cmds.hudButton( self.uiName , e=1 , label=value )
  def setlabelFontSize( self , value ):
    cmds.hudButton( self.uiName , e=1 , labelFontSize=value )
  def setpadding( self , value ):
    cmds.hudButton( self.uiName , e=1 , padding=value )
  def setpressCommand( self , value ):
    cmds.hudButton( self.uiName , e=1 , pressCommand=value )
  def setreleaseCommand( self , value ):
    cmds.hudButton( self.uiName , e=1 , releaseCommand=value )
  def setsection( self , value ):
    cmds.hudButton( self.uiName , e=1 , section=value )

  ##### propertyCode #####
  allowOverlap = property( getallowOverlap , setallowOverlap )
  block = property( getblock , setblock )
  blockAlignment = property( getblockAlignment , setblockAlignment )
  blockSize = property( getblockSize , setblockSize )
  buttonShape = property( getbuttonShape , setbuttonShape )
  buttonWidth = property( getbuttonWidth , setbuttonWidth )
  label = property( getlabel , setlabel )
  labelFontSize = property( getlabelFontSize , setlabelFontSize )
  padding = property( getpadding , setpadding )
  pressCommand = property( getpressCommand , setpressCommand )
  releaseCommand = property( getreleaseCommand , setreleaseCommand )
  section = property( getsection , setsection )

  ##### customCode #####





class HudSlider( Control ):

  ##### initialize #####
  def __init__( self , allowOverlap=None , block=None , blockAlignment=None , blockSize=None , dragCommand=None , decimalPrecision=None , internalPadding=None , label=None , labelFontSize=None , labelWidth=None , maxValue=None , minValue=None , padding=None , pressCommand=None , releaseCommand=None , section=None , sliderIncrement=None , sliderLength=None , type=None , value=None , valueAlignment=None , valueFontSize=None , valueWidth=None , **args ):
    self.uiName = cmds.hudSlider()

    ##### substitution #####
    if allowOverlap != None:
      self.allowOverlap = allowOverlap
    if block != None:
      self.block = block
    if blockAlignment != None:
      self.blockAlignment = blockAlignment
    if blockSize != None:
      self.blockSize = blockSize
    if dragCommand != None:
      self.dragCommand = dragCommand
    if decimalPrecision != None:
      self.decimalPrecision = decimalPrecision
    if internalPadding != None:
      self.internalPadding = internalPadding
    if label != None:
      self.label = label
    if labelFontSize != None:
      self.labelFontSize = labelFontSize
    if labelWidth != None:
      self.labelWidth = labelWidth
    if maxValue != None:
      self.maxValue = maxValue
    if minValue != None:
      self.minValue = minValue
    if padding != None:
      self.padding = padding
    if pressCommand != None:
      self.pressCommand = pressCommand
    if releaseCommand != None:
      self.releaseCommand = releaseCommand
    if section != None:
      self.section = section
    if sliderIncrement != None:
      self.sliderIncrement = sliderIncrement
    if sliderLength != None:
      self.sliderLength = sliderLength
    if type != None:
      self.type = type
    if value != None:
      self.value = value
    if valueAlignment != None:
      self.valueAlignment = valueAlignment
    if valueFontSize != None:
      self.valueFontSize = valueFontSize
    if valueWidth != None:
      self.valueWidth = valueWidth

  ##### getFuncCode #####
  def getallowOverlap( self ):
    return cmds.hudSlider( self.uiName , q=1 , allowOverlap=1 )
  def getblock( self ):
    return cmds.hudSlider( self.uiName , q=1 , block=1 )
  def getblockAlignment( self ):
    return cmds.hudSlider( self.uiName , q=1 , blockAlignment=1 )
  def getblockSize( self ):
    return cmds.hudSlider( self.uiName , q=1 , blockSize=1 )
  def getdragCommand( self ):
    return cmds.hudSlider( self.uiName , q=1 , dragCommand=1 )
  def getdecimalPrecision( self ):
    return cmds.hudSlider( self.uiName , q=1 , decimalPrecision=1 )
  def getinternalPadding( self ):
    return cmds.hudSlider( self.uiName , q=1 , internalPadding=1 )
  def getlabel( self ):
    return cmds.hudSlider( self.uiName , q=1 , label=1 )
  def getlabelFontSize( self ):
    return cmds.hudSlider( self.uiName , q=1 , labelFontSize=1 )
  def getlabelWidth( self ):
    return cmds.hudSlider( self.uiName , q=1 , labelWidth=1 )
  def getmaxValue( self ):
    return cmds.hudSlider( self.uiName , q=1 , maxValue=1 )
  def getminValue( self ):
    return cmds.hudSlider( self.uiName , q=1 , minValue=1 )
  def getpadding( self ):
    return cmds.hudSlider( self.uiName , q=1 , padding=1 )
  def getpressCommand( self ):
    return cmds.hudSlider( self.uiName , q=1 , pressCommand=1 )
  def getreleaseCommand( self ):
    return cmds.hudSlider( self.uiName , q=1 , releaseCommand=1 )
  def getsection( self ):
    return cmds.hudSlider( self.uiName , q=1 , section=1 )
  def getsliderIncrement( self ):
    return cmds.hudSlider( self.uiName , q=1 , sliderIncrement=1 )
  def getsliderLength( self ):
    return cmds.hudSlider( self.uiName , q=1 , sliderLength=1 )
  def gettype( self ):
    return cmds.hudSlider( self.uiName , q=1 , type=1 )
  def getvalue( self ):
    return cmds.hudSlider( self.uiName , q=1 , value=1 )
  def getvalueAlignment( self ):
    return cmds.hudSlider( self.uiName , q=1 , valueAlignment=1 )
  def getvalueFontSize( self ):
    return cmds.hudSlider( self.uiName , q=1 , valueFontSize=1 )
  def getvalueWidth( self ):
    return cmds.hudSlider( self.uiName , q=1 , valueWidth=1 )

  ##### setFuncCode #####
  def setallowOverlap( self , value ):
    cmds.hudSlider( self.uiName , e=1 , allowOverlap=value )
  def setblock( self , value ):
    cmds.hudSlider( self.uiName , e=1 , block=value )
  def setblockAlignment( self , value ):
    cmds.hudSlider( self.uiName , e=1 , blockAlignment=value )
  def setblockSize( self , value ):
    cmds.hudSlider( self.uiName , e=1 , blockSize=value )
  def setdragCommand( self , value ):
    cmds.hudSlider( self.uiName , e=1 , dragCommand=value )
  def setdecimalPrecision( self , value ):
    cmds.hudSlider( self.uiName , e=1 , decimalPrecision=value )
  def setinternalPadding( self , value ):
    cmds.hudSlider( self.uiName , e=1 , internalPadding=value )
  def setlabel( self , value ):
    cmds.hudSlider( self.uiName , e=1 , label=value )
  def setlabelFontSize( self , value ):
    cmds.hudSlider( self.uiName , e=1 , labelFontSize=value )
  def setlabelWidth( self , value ):
    cmds.hudSlider( self.uiName , e=1 , labelWidth=value )
  def setmaxValue( self , value ):
    cmds.hudSlider( self.uiName , e=1 , maxValue=value )
  def setminValue( self , value ):
    cmds.hudSlider( self.uiName , e=1 , minValue=value )
  def setpadding( self , value ):
    cmds.hudSlider( self.uiName , e=1 , padding=value )
  def setpressCommand( self , value ):
    cmds.hudSlider( self.uiName , e=1 , pressCommand=value )
  def setreleaseCommand( self , value ):
    cmds.hudSlider( self.uiName , e=1 , releaseCommand=value )
  def setsection( self , value ):
    cmds.hudSlider( self.uiName , e=1 , section=value )
  def setsliderIncrement( self , value ):
    cmds.hudSlider( self.uiName , e=1 , sliderIncrement=value )
  def setsliderLength( self , value ):
    cmds.hudSlider( self.uiName , e=1 , sliderLength=value )
  def settype( self , value ):
    cmds.hudSlider( self.uiName , e=1 , type=value )
  def setvalue( self , value ):
    cmds.hudSlider( self.uiName , e=1 , value=value )
  def setvalueAlignment( self , value ):
    cmds.hudSlider( self.uiName , e=1 , valueAlignment=value )
  def setvalueFontSize( self , value ):
    cmds.hudSlider( self.uiName , e=1 , valueFontSize=value )
  def setvalueWidth( self , value ):
    cmds.hudSlider( self.uiName , e=1 , valueWidth=value )

  ##### propertyCode #####
  allowOverlap = property( getallowOverlap , setallowOverlap )
  block = property( getblock , setblock )
  blockAlignment = property( getblockAlignment , setblockAlignment )
  blockSize = property( getblockSize , setblockSize )
  dragCommand = property( getdragCommand , setdragCommand )
  decimalPrecision = property( getdecimalPrecision , setdecimalPrecision )
  internalPadding = property( getinternalPadding , setinternalPadding )
  label = property( getlabel , setlabel )
  labelFontSize = property( getlabelFontSize , setlabelFontSize )
  labelWidth = property( getlabelWidth , setlabelWidth )
  maxValue = property( getmaxValue , setmaxValue )
  minValue = property( getminValue , setminValue )
  padding = property( getpadding , setpadding )
  pressCommand = property( getpressCommand , setpressCommand )
  releaseCommand = property( getreleaseCommand , setreleaseCommand )
  section = property( getsection , setsection )
  sliderIncrement = property( getsliderIncrement , setsliderIncrement )
  sliderLength = property( getsliderLength , setsliderLength )
  type = property( gettype , settype )
  value = property( getvalue , setvalue )
  valueAlignment = property( getvalueAlignment , setvalueAlignment )
  valueFontSize = property( getvalueFontSize , setvalueFontSize )
  valueWidth = property( getvalueWidth , setvalueWidth )

  ##### customCode #####





class HudSliderButton( Control ):

  ##### initialize #####
  def __init__( self , allowOverlap=None , block=None , blockAlignment=None , buttonLabelFontSize=None , buttonLabel=None , buttonPressCommand=None , buttonReleaseCommand=None , blockSize=None , buttonShape=None , buttonWidth=None , decimalPrecision=None , internalPadding=None , maxValue=None , minValue=None , padding=None , section=None , sliderDragCommand=None , sliderLabelFontSize=None , sliderIncrement=None , sliderLabel=None , sliderLength=None , sliderLabelWidth=None , sliderPressCommand=None , sliderReleaseCommand=None , type=None , value=None , valueAlignment=None , valueFontSize=None , valueWidth=None , **args ):
    self.uiName = cmds.hudSliderButton()

    ##### substitution #####
    if allowOverlap != None:
      self.allowOverlap = allowOverlap
    if block != None:
      self.block = block
    if blockAlignment != None:
      self.blockAlignment = blockAlignment
    if buttonLabelFontSize != None:
      self.buttonLabelFontSize = buttonLabelFontSize
    if buttonLabel != None:
      self.buttonLabel = buttonLabel
    if buttonPressCommand != None:
      self.buttonPressCommand = buttonPressCommand
    if buttonReleaseCommand != None:
      self.buttonReleaseCommand = buttonReleaseCommand
    if blockSize != None:
      self.blockSize = blockSize
    if buttonShape != None:
      self.buttonShape = buttonShape
    if buttonWidth != None:
      self.buttonWidth = buttonWidth
    if decimalPrecision != None:
      self.decimalPrecision = decimalPrecision
    if internalPadding != None:
      self.internalPadding = internalPadding
    if maxValue != None:
      self.maxValue = maxValue
    if minValue != None:
      self.minValue = minValue
    if padding != None:
      self.padding = padding
    if section != None:
      self.section = section
    if sliderDragCommand != None:
      self.sliderDragCommand = sliderDragCommand
    if sliderLabelFontSize != None:
      self.sliderLabelFontSize = sliderLabelFontSize
    if sliderIncrement != None:
      self.sliderIncrement = sliderIncrement
    if sliderLabel != None:
      self.sliderLabel = sliderLabel
    if sliderLength != None:
      self.sliderLength = sliderLength
    if sliderLabelWidth != None:
      self.sliderLabelWidth = sliderLabelWidth
    if sliderPressCommand != None:
      self.sliderPressCommand = sliderPressCommand
    if sliderReleaseCommand != None:
      self.sliderReleaseCommand = sliderReleaseCommand
    if type != None:
      self.type = type
    if value != None:
      self.value = value
    if valueAlignment != None:
      self.valueAlignment = valueAlignment
    if valueFontSize != None:
      self.valueFontSize = valueFontSize
    if valueWidth != None:
      self.valueWidth = valueWidth

  ##### getFuncCode #####
  def getallowOverlap( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , allowOverlap=1 )
  def getblock( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , block=1 )
  def getblockAlignment( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , blockAlignment=1 )
  def getbuttonLabelFontSize( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , buttonLabelFontSize=1 )
  def getbuttonLabel( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , buttonLabel=1 )
  def getbuttonPressCommand( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , buttonPressCommand=1 )
  def getbuttonReleaseCommand( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , buttonReleaseCommand=1 )
  def getblockSize( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , blockSize=1 )
  def getbuttonShape( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , buttonShape=1 )
  def getbuttonWidth( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , buttonWidth=1 )
  def getdecimalPrecision( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , decimalPrecision=1 )
  def getinternalPadding( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , internalPadding=1 )
  def getmaxValue( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , maxValue=1 )
  def getminValue( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , minValue=1 )
  def getpadding( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , padding=1 )
  def getsection( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , section=1 )
  def getsliderDragCommand( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , sliderDragCommand=1 )
  def getsliderLabelFontSize( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , sliderLabelFontSize=1 )
  def getsliderIncrement( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , sliderIncrement=1 )
  def getsliderLabel( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , sliderLabel=1 )
  def getsliderLength( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , sliderLength=1 )
  def getsliderLabelWidth( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , sliderLabelWidth=1 )
  def getsliderPressCommand( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , sliderPressCommand=1 )
  def getsliderReleaseCommand( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , sliderReleaseCommand=1 )
  def gettype( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , type=1 )
  def getvalue( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , value=1 )
  def getvalueAlignment( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , valueAlignment=1 )
  def getvalueFontSize( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , valueFontSize=1 )
  def getvalueWidth( self ):
    return cmds.hudSliderButton( self.uiName , q=1 , valueWidth=1 )

  ##### setFuncCode #####
  def setallowOverlap( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , allowOverlap=value )
  def setblock( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , block=value )
  def setblockAlignment( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , blockAlignment=value )
  def setbuttonLabelFontSize( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , buttonLabelFontSize=value )
  def setbuttonLabel( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , buttonLabel=value )
  def setbuttonPressCommand( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , buttonPressCommand=value )
  def setbuttonReleaseCommand( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , buttonReleaseCommand=value )
  def setblockSize( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , blockSize=value )
  def setbuttonShape( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , buttonShape=value )
  def setbuttonWidth( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , buttonWidth=value )
  def setdecimalPrecision( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , decimalPrecision=value )
  def setinternalPadding( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , internalPadding=value )
  def setmaxValue( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , maxValue=value )
  def setminValue( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , minValue=value )
  def setpadding( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , padding=value )
  def setsection( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , section=value )
  def setsliderDragCommand( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , sliderDragCommand=value )
  def setsliderLabelFontSize( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , sliderLabelFontSize=value )
  def setsliderIncrement( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , sliderIncrement=value )
  def setsliderLabel( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , sliderLabel=value )
  def setsliderLength( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , sliderLength=value )
  def setsliderLabelWidth( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , sliderLabelWidth=value )
  def setsliderPressCommand( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , sliderPressCommand=value )
  def setsliderReleaseCommand( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , sliderReleaseCommand=value )
  def settype( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , type=value )
  def setvalue( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , value=value )
  def setvalueAlignment( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , valueAlignment=value )
  def setvalueFontSize( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , valueFontSize=value )
  def setvalueWidth( self , value ):
    cmds.hudSliderButton( self.uiName , e=1 , valueWidth=value )

  ##### propertyCode #####
  allowOverlap = property( getallowOverlap , setallowOverlap )
  block = property( getblock , setblock )
  blockAlignment = property( getblockAlignment , setblockAlignment )
  buttonLabelFontSize = property( getbuttonLabelFontSize , setbuttonLabelFontSize )
  buttonLabel = property( getbuttonLabel , setbuttonLabel )
  buttonPressCommand = property( getbuttonPressCommand , setbuttonPressCommand )
  buttonReleaseCommand = property( getbuttonReleaseCommand , setbuttonReleaseCommand )
  blockSize = property( getblockSize , setblockSize )
  buttonShape = property( getbuttonShape , setbuttonShape )
  buttonWidth = property( getbuttonWidth , setbuttonWidth )
  decimalPrecision = property( getdecimalPrecision , setdecimalPrecision )
  internalPadding = property( getinternalPadding , setinternalPadding )
  maxValue = property( getmaxValue , setmaxValue )
  minValue = property( getminValue , setminValue )
  padding = property( getpadding , setpadding )
  section = property( getsection , setsection )
  sliderDragCommand = property( getsliderDragCommand , setsliderDragCommand )
  sliderLabelFontSize = property( getsliderLabelFontSize , setsliderLabelFontSize )
  sliderIncrement = property( getsliderIncrement , setsliderIncrement )
  sliderLabel = property( getsliderLabel , setsliderLabel )
  sliderLength = property( getsliderLength , setsliderLength )
  sliderLabelWidth = property( getsliderLabelWidth , setsliderLabelWidth )
  sliderPressCommand = property( getsliderPressCommand , setsliderPressCommand )
  sliderReleaseCommand = property( getsliderReleaseCommand , setsliderReleaseCommand )
  type = property( gettype , settype )
  value = property( getvalue , setvalue )
  valueAlignment = property( getvalueAlignment , setvalueAlignment )
  valueFontSize = property( getvalueFontSize , setvalueFontSize )
  valueWidth = property( getvalueWidth , setvalueWidth )

  ##### customCode #####





class MessageLine( Control ):

  ##### initialize #####
  def __init__( self , **args ):
    self.uiName = cmds.messageLine()

    ##### substitution #####

  ##### getFuncCode #####

  ##### setFuncCode #####

  ##### propertyCode #####

  ##### customCode #####





class NameField( Control ):

  ##### initialize #####
  def __init__( self , changeCommand=None , nameChangeCommand=None , object=None , receiveFocusCommand=None , **args ):
    self.uiName = cmds.nameField()

    ##### substitution #####
    if changeCommand != None:
      self.changeCommand = changeCommand
    if nameChangeCommand != None:
      self.nameChangeCommand = nameChangeCommand
    if object != None:
      self.object = object
    if receiveFocusCommand != None:
      self.receiveFocusCommand = receiveFocusCommand

  ##### getFuncCode #####
  def getchangeCommand( self ):
    return cmds.nameField( self.uiName , q=1 , changeCommand=1 )
  def getnameChangeCommand( self ):
    return cmds.nameField( self.uiName , q=1 , nameChangeCommand=1 )
  def getobject( self ):
    return cmds.nameField( self.uiName , q=1 , object=1 )
  def getreceiveFocusCommand( self ):
    return cmds.nameField( self.uiName , q=1 , receiveFocusCommand=1 )

  ##### setFuncCode #####
  def setchangeCommand( self , value ):
    cmds.nameField( self.uiName , e=1 , changeCommand=value )
  def setnameChangeCommand( self , value ):
    cmds.nameField( self.uiName , e=1 , nameChangeCommand=value )
  def setobject( self , value ):
    cmds.nameField( self.uiName , e=1 , object=value )
  def setreceiveFocusCommand( self , value ):
    cmds.nameField( self.uiName , e=1 , receiveFocusCommand=value )

  ##### propertyCode #####
  changeCommand = property( getchangeCommand , setchangeCommand )
  nameChangeCommand = property( getnameChangeCommand , setnameChangeCommand )
  object = property( getobject , setobject )
  receiveFocusCommand = property( getreceiveFocusCommand , setreceiveFocusCommand )

  ##### customCode #####





class PalettePort( Control ):

  ##### initialize #####
  def __init__( self , actualTotal=None , changeCommand=None , colorEdited=None , colorEditable=None , dimensions=None , editable=None , hsvValue=None , redraw=None , rgbValue=None , setCurCell=None , transparent=None , topDown=None , **args ):
    self.uiName = cmds.palettePort()

    ##### substitution #####
    if actualTotal != None:
      self.actualTotal = actualTotal
    if changeCommand != None:
      self.changeCommand = changeCommand
    if colorEdited != None:
      self.colorEdited = colorEdited
    if colorEditable != None:
      self.colorEditable = colorEditable
    if dimensions != None:
      self.dimensions = dimensions
    if editable != None:
      self.editable = editable
    if hsvValue != None:
      self.hsvValue = hsvValue
    if redraw != None:
      self.redraw = redraw
    if rgbValue != None:
      self.rgbValue = rgbValue
    if setCurCell != None:
      self.setCurCell = setCurCell
    if transparent != None:
      self.transparent = transparent
    if topDown != None:
      self.topDown = topDown

  ##### getFuncCode #####
  def getactualTotal( self ):
    return cmds.palettePort( self.uiName , q=1 , actualTotal=1 )
  def getchangeCommand( self ):
    return cmds.palettePort( self.uiName , q=1 , changeCommand=1 )
  def getcolorEdited( self ):
    return cmds.palettePort( self.uiName , q=1 , colorEdited=1 )
  def getcolorEditable( self ):
    return cmds.palettePort( self.uiName , q=1 , colorEditable=1 )
  def getdimensions( self ):
    return cmds.palettePort( self.uiName , q=1 , dimensions=1 )
  def geteditable( self ):
    return cmds.palettePort( self.uiName , q=1 , editable=1 )
  def gethsvValue( self ):
    return cmds.palettePort( self.uiName , q=1 , hsvValue=1 )
  def getredraw( self ):
    return cmds.palettePort( self.uiName , q=1 , redraw=1 )
  def getrgbValue( self ):
    return cmds.palettePort( self.uiName , q=1 , rgbValue=1 )
  def getsetCurCell( self ):
    return cmds.palettePort( self.uiName , q=1 , setCurCell=1 )
  def gettransparent( self ):
    return cmds.palettePort( self.uiName , q=1 , transparent=1 )
  def gettopDown( self ):
    return cmds.palettePort( self.uiName , q=1 , topDown=1 )

  ##### setFuncCode #####
  def setactualTotal( self , value ):
    cmds.palettePort( self.uiName , e=1 , actualTotal=value )
  def setchangeCommand( self , value ):
    cmds.palettePort( self.uiName , e=1 , changeCommand=value )
  def setcolorEdited( self , value ):
    cmds.palettePort( self.uiName , e=1 , colorEdited=value )
  def setcolorEditable( self , value ):
    cmds.palettePort( self.uiName , e=1 , colorEditable=value )
  def setdimensions( self , value ):
    cmds.palettePort( self.uiName , e=1 , dimensions=value )
  def seteditable( self , value ):
    cmds.palettePort( self.uiName , e=1 , editable=value )
  def sethsvValue( self , value ):
    cmds.palettePort( self.uiName , e=1 , hsvValue=value )
  def setredraw( self , value ):
    cmds.palettePort( self.uiName , e=1 , redraw=value )
  def setrgbValue( self , value ):
    cmds.palettePort( self.uiName , e=1 , rgbValue=value )
  def setsetCurCell( self , value ):
    cmds.palettePort( self.uiName , e=1 , setCurCell=value )
  def settransparent( self , value ):
    cmds.palettePort( self.uiName , e=1 , transparent=value )
  def settopDown( self , value ):
    cmds.palettePort( self.uiName , e=1 , topDown=value )

  ##### propertyCode #####
  actualTotal = property( getactualTotal , setactualTotal )
  changeCommand = property( getchangeCommand , setchangeCommand )
  colorEdited = property( getcolorEdited , setcolorEdited )
  colorEditable = property( getcolorEditable , setcolorEditable )
  dimensions = property( getdimensions , setdimensions )
  editable = property( geteditable , seteditable )
  hsvValue = property( gethsvValue , sethsvValue )
  redraw = property( getredraw , setredraw )
  rgbValue = property( getrgbValue , setrgbValue )
  setCurCell = property( getsetCurCell , setsetCurCell )
  transparent = property( gettransparent , settransparent )
  topDown = property( gettopDown , settopDown )

  ##### customCode #####





class RangeControl( Control ):

  ##### initialize #####
  def __init__( self , changedCommand=None , maxRange=None , minRange=None , widthHeight=None , **args ):
    self.uiName = cmds.rangeControl()

    ##### substitution #####
    if changedCommand != None:
      self.changedCommand = changedCommand
    if maxRange != None:
      self.maxRange = maxRange
    if minRange != None:
      self.minRange = minRange
    if widthHeight != None:
      self.widthHeight = widthHeight

  ##### getFuncCode #####
  def getchangedCommand( self ):
    return cmds.rangeControl( self.uiName , q=1 , changedCommand=1 )
  def getmaxRange( self ):
    return cmds.rangeControl( self.uiName , q=1 , maxRange=1 )
  def getminRange( self ):
    return cmds.rangeControl( self.uiName , q=1 , minRange=1 )
  def getwidthHeight( self ):
    return cmds.rangeControl( self.uiName , q=1 , widthHeight=1 )

  ##### setFuncCode #####
  def setchangedCommand( self , value ):
    cmds.rangeControl( self.uiName , e=1 , changedCommand=value )
  def setmaxRange( self , value ):
    cmds.rangeControl( self.uiName , e=1 , maxRange=value )
  def setminRange( self , value ):
    cmds.rangeControl( self.uiName , e=1 , minRange=value )
  def setwidthHeight( self , value ):
    cmds.rangeControl( self.uiName , e=1 , widthHeight=value )

  ##### propertyCode #####
  changedCommand = property( getchangedCommand , setchangedCommand )
  maxRange = property( getmaxRange , setmaxRange )
  minRange = property( getminRange , setminRange )
  widthHeight = property( getwidthHeight , setwidthHeight )

  ##### customCode #####





class ScriptTable( Control ):

  ##### initialize #####
  def __init__( self , columns=None , cellChangedCmd=None , clearRow=None , clearTable=None , columnWidth=None , deleteRow=None , getCellCmd=None , insertRow=None , label=None , rows=None , selectedRow=None , underPointerRow=None , **args ):
    self.uiName = cmds.scriptTable()

    ##### substitution #####
    if columns != None:
      self.columns = columns
    if cellChangedCmd != None:
      self.cellChangedCmd = cellChangedCmd
    if clearRow != None:
      self.clearRow = clearRow
    if clearTable != None:
      self.clearTable = clearTable
    if columnWidth != None:
      self.columnWidth = columnWidth
    if deleteRow != None:
      self.deleteRow = deleteRow
    if getCellCmd != None:
      self.getCellCmd = getCellCmd
    if insertRow != None:
      self.insertRow = insertRow
    if label != None:
      self.label = label
    if rows != None:
      self.rows = rows
    if selectedRow != None:
      self.selectedRow = selectedRow
    if underPointerRow != None:
      self.underPointerRow = underPointerRow

  ##### getFuncCode #####
  def getcolumns( self ):
    return cmds.scriptTable( self.uiName , q=1 , columns=1 )
  def getcellChangedCmd( self ):
    return cmds.scriptTable( self.uiName , q=1 , cellChangedCmd=1 )
  def getclearRow( self ):
    return cmds.scriptTable( self.uiName , q=1 , clearRow=1 )
  def getclearTable( self ):
    return cmds.scriptTable( self.uiName , q=1 , clearTable=1 )
  def getcolumnWidth( self ):
    return cmds.scriptTable( self.uiName , q=1 , columnWidth=1 )
  def getdeleteRow( self ):
    return cmds.scriptTable( self.uiName , q=1 , deleteRow=1 )
  def getgetCellCmd( self ):
    return cmds.scriptTable( self.uiName , q=1 , getCellCmd=1 )
  def getinsertRow( self ):
    return cmds.scriptTable( self.uiName , q=1 , insertRow=1 )
  def getlabel( self ):
    return cmds.scriptTable( self.uiName , q=1 , label=1 )
  def getrows( self ):
    return cmds.scriptTable( self.uiName , q=1 , rows=1 )
  def getselectedRow( self ):
    return cmds.scriptTable( self.uiName , q=1 , selectedRow=1 )
  def getunderPointerRow( self ):
    return cmds.scriptTable( self.uiName , q=1 , underPointerRow=1 )

  ##### setFuncCode #####
  def setcolumns( self , value ):
    cmds.scriptTable( self.uiName , e=1 , columns=value )
  def setcellChangedCmd( self , value ):
    cmds.scriptTable( self.uiName , e=1 , cellChangedCmd=value )
  def setclearRow( self , value ):
    cmds.scriptTable( self.uiName , e=1 , clearRow=value )
  def setclearTable( self , value ):
    cmds.scriptTable( self.uiName , e=1 , clearTable=value )
  def setcolumnWidth( self , value ):
    cmds.scriptTable( self.uiName , e=1 , columnWidth=value )
  def setdeleteRow( self , value ):
    cmds.scriptTable( self.uiName , e=1 , deleteRow=value )
  def setgetCellCmd( self , value ):
    cmds.scriptTable( self.uiName , e=1 , getCellCmd=value )
  def setinsertRow( self , value ):
    cmds.scriptTable( self.uiName , e=1 , insertRow=value )
  def setlabel( self , value ):
    cmds.scriptTable( self.uiName , e=1 , label=value )
  def setrows( self , value ):
    cmds.scriptTable( self.uiName , e=1 , rows=value )
  def setselectedRow( self , value ):
    cmds.scriptTable( self.uiName , e=1 , selectedRow=value )
  def setunderPointerRow( self , value ):
    cmds.scriptTable( self.uiName , e=1 , underPointerRow=value )

  ##### propertyCode #####
  columns = property( getcolumns , setcolumns )
  cellChangedCmd = property( getcellChangedCmd , setcellChangedCmd )
  clearRow = property( getclearRow , setclearRow )
  clearTable = property( getclearTable , setclearTable )
  columnWidth = property( getcolumnWidth , setcolumnWidth )
  deleteRow = property( getdeleteRow , setdeleteRow )
  getCellCmd = property( getgetCellCmd , setgetCellCmd )
  insertRow = property( getinsertRow , setinsertRow )
  label = property( getlabel , setlabel )
  rows = property( getrows , setrows )
  selectedRow = property( getselectedRow , setselectedRow )
  underPointerRow = property( getunderPointerRow , setunderPointerRow )

  ##### customCode #####





class ShelfButton( Control ):

  ##### initialize #####
  def __init__( self , actionIsSubstitute=None , align=None , command=None , doubleClickCommand=None , disabledImage=None , enableCommandRepeat=None , font=None , highlightImage=None , handleNodeDropCallback=None , image=None , image1=None , image2=None , image3=None , imageOverlayLabel=None , label=None , labelEditingCallback=None , labelOffset=None , marginHeight=None , menuItem=None , marginWidth=None , commandRepeatable=None , selectionImage=None , style=None , sourceType=None , **args ):
    self.uiName = cmds.shelfButton()

    ##### substitution #####
    if actionIsSubstitute != None:
      self.actionIsSubstitute = actionIsSubstitute
    if align != None:
      self.align = align
    if command != None:
      self.command = command
    if doubleClickCommand != None:
      self.doubleClickCommand = doubleClickCommand
    if disabledImage != None:
      self.disabledImage = disabledImage
    if enableCommandRepeat != None:
      self.enableCommandRepeat = enableCommandRepeat
    if font != None:
      self.font = font
    if highlightImage != None:
      self.highlightImage = highlightImage
    if handleNodeDropCallback != None:
      self.handleNodeDropCallback = handleNodeDropCallback
    if image != None:
      self.image = image
    if image1 != None:
      self.image1 = image1
    if image2 != None:
      self.image2 = image2
    if image3 != None:
      self.image3 = image3
    if imageOverlayLabel != None:
      self.imageOverlayLabel = imageOverlayLabel
    if label != None:
      self.label = label
    if labelEditingCallback != None:
      self.labelEditingCallback = labelEditingCallback
    if labelOffset != None:
      self.labelOffset = labelOffset
    if marginHeight != None:
      self.marginHeight = marginHeight
    if menuItem != None:
      self.menuItem = menuItem
    if marginWidth != None:
      self.marginWidth = marginWidth
    if commandRepeatable != None:
      self.commandRepeatable = commandRepeatable
    if selectionImage != None:
      self.selectionImage = selectionImage
    if style != None:
      self.style = style
    if sourceType != None:
      self.sourceType = sourceType

  ##### getFuncCode #####
  def getactionIsSubstitute( self ):
    return cmds.shelfButton( self.uiName , q=1 , actionIsSubstitute=1 )
  def getalign( self ):
    return cmds.shelfButton( self.uiName , q=1 , align=1 )
  def getcommand( self ):
    return cmds.shelfButton( self.uiName , q=1 , command=1 )
  def getdoubleClickCommand( self ):
    return cmds.shelfButton( self.uiName , q=1 , doubleClickCommand=1 )
  def getdisabledImage( self ):
    return cmds.shelfButton( self.uiName , q=1 , disabledImage=1 )
  def getenableCommandRepeat( self ):
    return cmds.shelfButton( self.uiName , q=1 , enableCommandRepeat=1 )
  def getfont( self ):
    return cmds.shelfButton( self.uiName , q=1 , font=1 )
  def gethighlightImage( self ):
    return cmds.shelfButton( self.uiName , q=1 , highlightImage=1 )
  def gethandleNodeDropCallback( self ):
    return cmds.shelfButton( self.uiName , q=1 , handleNodeDropCallback=1 )
  def getimage( self ):
    return cmds.shelfButton( self.uiName , q=1 , image=1 )
  def getimage1( self ):
    return cmds.shelfButton( self.uiName , q=1 , image1=1 )
  def getimage2( self ):
    return cmds.shelfButton( self.uiName , q=1 , image2=1 )
  def getimage3( self ):
    return cmds.shelfButton( self.uiName , q=1 , image3=1 )
  def getimageOverlayLabel( self ):
    return cmds.shelfButton( self.uiName , q=1 , imageOverlayLabel=1 )
  def getlabel( self ):
    return cmds.shelfButton( self.uiName , q=1 , label=1 )
  def getlabelEditingCallback( self ):
    return cmds.shelfButton( self.uiName , q=1 , labelEditingCallback=1 )
  def getlabelOffset( self ):
    return cmds.shelfButton( self.uiName , q=1 , labelOffset=1 )
  def getmarginHeight( self ):
    return cmds.shelfButton( self.uiName , q=1 , marginHeight=1 )
  def getmenuItem( self ):
    return cmds.shelfButton( self.uiName , q=1 , menuItem=1 )
  def getmarginWidth( self ):
    return cmds.shelfButton( self.uiName , q=1 , marginWidth=1 )
  def getcommandRepeatable( self ):
    return cmds.shelfButton( self.uiName , q=1 , commandRepeatable=1 )
  def getselectionImage( self ):
    return cmds.shelfButton( self.uiName , q=1 , selectionImage=1 )
  def getstyle( self ):
    return cmds.shelfButton( self.uiName , q=1 , style=1 )
  def getsourceType( self ):
    return cmds.shelfButton( self.uiName , q=1 , sourceType=1 )

  ##### setFuncCode #####
  def setactionIsSubstitute( self , value ):
    cmds.shelfButton( self.uiName , e=1 , actionIsSubstitute=value )
  def setalign( self , value ):
    cmds.shelfButton( self.uiName , e=1 , align=value )
  def setcommand( self , value ):
    cmds.shelfButton( self.uiName , e=1 , command=value )
  def setdoubleClickCommand( self , value ):
    cmds.shelfButton( self.uiName , e=1 , doubleClickCommand=value )
  def setdisabledImage( self , value ):
    cmds.shelfButton( self.uiName , e=1 , disabledImage=value )
  def setenableCommandRepeat( self , value ):
    cmds.shelfButton( self.uiName , e=1 , enableCommandRepeat=value )
  def setfont( self , value ):
    cmds.shelfButton( self.uiName , e=1 , font=value )
  def sethighlightImage( self , value ):
    cmds.shelfButton( self.uiName , e=1 , highlightImage=value )
  def sethandleNodeDropCallback( self , value ):
    cmds.shelfButton( self.uiName , e=1 , handleNodeDropCallback=value )
  def setimage( self , value ):
    cmds.shelfButton( self.uiName , e=1 , image=value )
  def setimage1( self , value ):
    cmds.shelfButton( self.uiName , e=1 , image1=value )
  def setimage2( self , value ):
    cmds.shelfButton( self.uiName , e=1 , image2=value )
  def setimage3( self , value ):
    cmds.shelfButton( self.uiName , e=1 , image3=value )
  def setimageOverlayLabel( self , value ):
    cmds.shelfButton( self.uiName , e=1 , imageOverlayLabel=value )
  def setlabel( self , value ):
    cmds.shelfButton( self.uiName , e=1 , label=value )
  def setlabelEditingCallback( self , value ):
    cmds.shelfButton( self.uiName , e=1 , labelEditingCallback=value )
  def setlabelOffset( self , value ):
    cmds.shelfButton( self.uiName , e=1 , labelOffset=value )
  def setmarginHeight( self , value ):
    cmds.shelfButton( self.uiName , e=1 , marginHeight=value )
  def setmenuItem( self , value ):
    cmds.shelfButton( self.uiName , e=1 , menuItem=value )
  def setmarginWidth( self , value ):
    cmds.shelfButton( self.uiName , e=1 , marginWidth=value )
  def setcommandRepeatable( self , value ):
    cmds.shelfButton( self.uiName , e=1 , commandRepeatable=value )
  def setselectionImage( self , value ):
    cmds.shelfButton( self.uiName , e=1 , selectionImage=value )
  def setstyle( self , value ):
    cmds.shelfButton( self.uiName , e=1 , style=value )
  def setsourceType( self , value ):
    cmds.shelfButton( self.uiName , e=1 , sourceType=value )

  ##### propertyCode #####
  actionIsSubstitute = property( getactionIsSubstitute , setactionIsSubstitute )
  align = property( getalign , setalign )
  command = property( getcommand , setcommand )
  doubleClickCommand = property( getdoubleClickCommand , setdoubleClickCommand )
  disabledImage = property( getdisabledImage , setdisabledImage )
  enableCommandRepeat = property( getenableCommandRepeat , setenableCommandRepeat )
  font = property( getfont , setfont )
  highlightImage = property( gethighlightImage , sethighlightImage )
  handleNodeDropCallback = property( gethandleNodeDropCallback , sethandleNodeDropCallback )
  image = property( getimage , setimage )
  image1 = property( getimage1 , setimage1 )
  image2 = property( getimage2 , setimage2 )
  image3 = property( getimage3 , setimage3 )
  imageOverlayLabel = property( getimageOverlayLabel , setimageOverlayLabel )
  label = property( getlabel , setlabel )
  labelEditingCallback = property( getlabelEditingCallback , setlabelEditingCallback )
  labelOffset = property( getlabelOffset , setlabelOffset )
  marginHeight = property( getmarginHeight , setmarginHeight )
  menuItem = property( getmenuItem , setmenuItem )
  marginWidth = property( getmarginWidth , setmarginWidth )
  commandRepeatable = property( getcommandRepeatable , setcommandRepeatable )
  selectionImage = property( getselectionImage , setselectionImage )
  style = property( getstyle , setstyle )
  sourceType = property( getsourceType , setsourceType )

  ##### customCode #####





class ShellField( Control ):

  ##### initialize #####
  def __init__( self , command=None , clear=None , numberOfHistoryLines=None , numberOfSavedLines=None , output=None , prompt=None , userInput=None , **args ):
    self.uiName = cmds.shellField()

    ##### substitution #####
    if command != None:
      self.command = command
    if clear != None:
      self.clear = clear
    if numberOfHistoryLines != None:
      self.numberOfHistoryLines = numberOfHistoryLines
    if numberOfSavedLines != None:
      self.numberOfSavedLines = numberOfSavedLines
    if output != None:
      self.output = output
    if prompt != None:
      self.prompt = prompt
    if userInput != None:
      self.userInput = userInput

  ##### getFuncCode #####
  def getcommand( self ):
    return cmds.shellField( self.uiName , q=1 , command=1 )
  def getclear( self ):
    return cmds.shellField( self.uiName , q=1 , clear=1 )
  def getnumberOfHistoryLines( self ):
    return cmds.shellField( self.uiName , q=1 , numberOfHistoryLines=1 )
  def getnumberOfSavedLines( self ):
    return cmds.shellField( self.uiName , q=1 , numberOfSavedLines=1 )
  def getoutput( self ):
    return cmds.shellField( self.uiName , q=1 , output=1 )
  def getprompt( self ):
    return cmds.shellField( self.uiName , q=1 , prompt=1 )
  def getuserInput( self ):
    return cmds.shellField( self.uiName , q=1 , userInput=1 )

  ##### setFuncCode #####
  def setcommand( self , value ):
    cmds.shellField( self.uiName , e=1 , command=value )
  def setclear( self , value ):
    cmds.shellField( self.uiName , e=1 , clear=value )
  def setnumberOfHistoryLines( self , value ):
    cmds.shellField( self.uiName , e=1 , numberOfHistoryLines=value )
  def setnumberOfSavedLines( self , value ):
    cmds.shellField( self.uiName , e=1 , numberOfSavedLines=value )
  def setoutput( self , value ):
    cmds.shellField( self.uiName , e=1 , output=value )
  def setprompt( self , value ):
    cmds.shellField( self.uiName , e=1 , prompt=value )
  def setuserInput( self , value ):
    cmds.shellField( self.uiName , e=1 , userInput=value )

  ##### propertyCode #####
  command = property( getcommand , setcommand )
  clear = property( getclear , setclear )
  numberOfHistoryLines = property( getnumberOfHistoryLines , setnumberOfHistoryLines )
  numberOfSavedLines = property( getnumberOfSavedLines , setnumberOfSavedLines )
  output = property( getoutput , setoutput )
  prompt = property( getprompt , setprompt )
  userInput = property( getuserInput , setuserInput )

  ##### customCode #####





class SoundControl( Control ):

  ##### initialize #####
  def __init__( self , beginScrub=None , displaySound=None , endScrub=None , maxTime=None , minTime=None , pressCommand=None , resample=None , releaseCommand=None , repeatChunkSize=None , repeatOnHold=None , sound=None , waveform=None , **args ):
    self.uiName = cmds.soundControl()

    ##### substitution #####
    if beginScrub != None:
      self.beginScrub = beginScrub
    if displaySound != None:
      self.displaySound = displaySound
    if endScrub != None:
      self.endScrub = endScrub
    if maxTime != None:
      self.maxTime = maxTime
    if minTime != None:
      self.minTime = minTime
    if pressCommand != None:
      self.pressCommand = pressCommand
    if resample != None:
      self.resample = resample
    if releaseCommand != None:
      self.releaseCommand = releaseCommand
    if repeatChunkSize != None:
      self.repeatChunkSize = repeatChunkSize
    if repeatOnHold != None:
      self.repeatOnHold = repeatOnHold
    if sound != None:
      self.sound = sound
    if waveform != None:
      self.waveform = waveform

  ##### getFuncCode #####
  def getbeginScrub( self ):
    return cmds.soundControl( self.uiName , q=1 , beginScrub=1 )
  def getdisplaySound( self ):
    return cmds.soundControl( self.uiName , q=1 , displaySound=1 )
  def getendScrub( self ):
    return cmds.soundControl( self.uiName , q=1 , endScrub=1 )
  def getmaxTime( self ):
    return cmds.soundControl( self.uiName , q=1 , maxTime=1 )
  def getminTime( self ):
    return cmds.soundControl( self.uiName , q=1 , minTime=1 )
  def getpressCommand( self ):
    return cmds.soundControl( self.uiName , q=1 , pressCommand=1 )
  def getresample( self ):
    return cmds.soundControl( self.uiName , q=1 , resample=1 )
  def getreleaseCommand( self ):
    return cmds.soundControl( self.uiName , q=1 , releaseCommand=1 )
  def getrepeatChunkSize( self ):
    return cmds.soundControl( self.uiName , q=1 , repeatChunkSize=1 )
  def getrepeatOnHold( self ):
    return cmds.soundControl( self.uiName , q=1 , repeatOnHold=1 )
  def getsound( self ):
    return cmds.soundControl( self.uiName , q=1 , sound=1 )
  def getwaveform( self ):
    return cmds.soundControl( self.uiName , q=1 , waveform=1 )

  ##### setFuncCode #####
  def setbeginScrub( self , value ):
    cmds.soundControl( self.uiName , e=1 , beginScrub=value )
  def setdisplaySound( self , value ):
    cmds.soundControl( self.uiName , e=1 , displaySound=value )
  def setendScrub( self , value ):
    cmds.soundControl( self.uiName , e=1 , endScrub=value )
  def setmaxTime( self , value ):
    cmds.soundControl( self.uiName , e=1 , maxTime=value )
  def setminTime( self , value ):
    cmds.soundControl( self.uiName , e=1 , minTime=value )
  def setpressCommand( self , value ):
    cmds.soundControl( self.uiName , e=1 , pressCommand=value )
  def setresample( self , value ):
    cmds.soundControl( self.uiName , e=1 , resample=value )
  def setreleaseCommand( self , value ):
    cmds.soundControl( self.uiName , e=1 , releaseCommand=value )
  def setrepeatChunkSize( self , value ):
    cmds.soundControl( self.uiName , e=1 , repeatChunkSize=value )
  def setrepeatOnHold( self , value ):
    cmds.soundControl( self.uiName , e=1 , repeatOnHold=value )
  def setsound( self , value ):
    cmds.soundControl( self.uiName , e=1 , sound=value )
  def setwaveform( self , value ):
    cmds.soundControl( self.uiName , e=1 , waveform=value )

  ##### propertyCode #####
  beginScrub = property( getbeginScrub , setbeginScrub )
  displaySound = property( getdisplaySound , setdisplaySound )
  endScrub = property( getendScrub , setendScrub )
  maxTime = property( getmaxTime , setmaxTime )
  minTime = property( getminTime , setminTime )
  pressCommand = property( getpressCommand , setpressCommand )
  resample = property( getresample , setresample )
  releaseCommand = property( getreleaseCommand , setreleaseCommand )
  repeatChunkSize = property( getrepeatChunkSize , setrepeatChunkSize )
  repeatOnHold = property( getrepeatOnHold , setrepeatOnHold )
  sound = property( getsound , setsound )
  waveform = property( getwaveform , setwaveform )

  ##### customCode #####





class SwatchDisplayPort( Control ):

  ##### initialize #####
  def __init__( self , borderColor=None , borderWidth=None , pressCommand=None , renderSize=None , shadingNode=None , widthHeight=None , **args ):
    self.uiName = cmds.swatchDisplayPort()

    ##### substitution #####
    if borderColor != None:
      self.borderColor = borderColor
    if borderWidth != None:
      self.borderWidth = borderWidth
    if pressCommand != None:
      self.pressCommand = pressCommand
    if renderSize != None:
      self.renderSize = renderSize
    if shadingNode != None:
      self.shadingNode = shadingNode
    if widthHeight != None:
      self.widthHeight = widthHeight

  ##### getFuncCode #####
  def getborderColor( self ):
    return cmds.swatchDisplayPort( self.uiName , q=1 , borderColor=1 )
  def getborderWidth( self ):
    return cmds.swatchDisplayPort( self.uiName , q=1 , borderWidth=1 )
  def getpressCommand( self ):
    return cmds.swatchDisplayPort( self.uiName , q=1 , pressCommand=1 )
  def getrenderSize( self ):
    return cmds.swatchDisplayPort( self.uiName , q=1 , renderSize=1 )
  def getshadingNode( self ):
    return cmds.swatchDisplayPort( self.uiName , q=1 , shadingNode=1 )
  def getwidthHeight( self ):
    return cmds.swatchDisplayPort( self.uiName , q=1 , widthHeight=1 )

  ##### setFuncCode #####
  def setborderColor( self , value ):
    cmds.swatchDisplayPort( self.uiName , e=1 , borderColor=value )
  def setborderWidth( self , value ):
    cmds.swatchDisplayPort( self.uiName , e=1 , borderWidth=value )
  def setpressCommand( self , value ):
    cmds.swatchDisplayPort( self.uiName , e=1 , pressCommand=value )
  def setrenderSize( self , value ):
    cmds.swatchDisplayPort( self.uiName , e=1 , renderSize=value )
  def setshadingNode( self , value ):
    cmds.swatchDisplayPort( self.uiName , e=1 , shadingNode=value )
  def setwidthHeight( self , value ):
    cmds.swatchDisplayPort( self.uiName , e=1 , widthHeight=value )

  ##### propertyCode #####
  borderColor = property( getborderColor , setborderColor )
  borderWidth = property( getborderWidth , setborderWidth )
  pressCommand = property( getpressCommand , setpressCommand )
  renderSize = property( getrenderSize , setrenderSize )
  shadingNode = property( getshadingNode , setshadingNode )
  widthHeight = property( getwidthHeight , setwidthHeight )

  ##### customCode #####





class SwitchTable( Control ):

  ##### initialize #####
  def __init__( self , label1=None , label2=None , switchNode=None , selectedRow=None , underPointerRow=None , **args ):
    self.uiName = cmds.switchTable()

    ##### substitution #####
    if label1 != None:
      self.label1 = label1
    if label2 != None:
      self.label2 = label2
    if switchNode != None:
      self.switchNode = switchNode
    if selectedRow != None:
      self.selectedRow = selectedRow
    if underPointerRow != None:
      self.underPointerRow = underPointerRow

  ##### getFuncCode #####
  def getlabel1( self ):
    return cmds.switchTable( self.uiName , q=1 , label1=1 )
  def getlabel2( self ):
    return cmds.switchTable( self.uiName , q=1 , label2=1 )
  def getswitchNode( self ):
    return cmds.switchTable( self.uiName , q=1 , switchNode=1 )
  def getselectedRow( self ):
    return cmds.switchTable( self.uiName , q=1 , selectedRow=1 )
  def getunderPointerRow( self ):
    return cmds.switchTable( self.uiName , q=1 , underPointerRow=1 )

  ##### setFuncCode #####
  def setlabel1( self , value ):
    cmds.switchTable( self.uiName , e=1 , label1=value )
  def setlabel2( self , value ):
    cmds.switchTable( self.uiName , e=1 , label2=value )
  def setswitchNode( self , value ):
    cmds.switchTable( self.uiName , e=1 , switchNode=value )
  def setselectedRow( self , value ):
    cmds.switchTable( self.uiName , e=1 , selectedRow=value )
  def setunderPointerRow( self , value ):
    cmds.switchTable( self.uiName , e=1 , underPointerRow=value )

  ##### propertyCode #####
  label1 = property( getlabel1 , setlabel1 )
  label2 = property( getlabel2 , setlabel2 )
  switchNode = property( getswitchNode , setswitchNode )
  selectedRow = property( getselectedRow , setselectedRow )
  underPointerRow = property( getunderPointerRow , setunderPointerRow )

  ##### customCode #####





class SymbolButton( Control ):

  ##### initialize #####
  def __init__( self , command=None , image=None , **args ):
    self.uiName = cmds.symbolButton()

    ##### substitution #####
    if command != None:
      self.command = command
    if image != None:
      self.image = image

  ##### getFuncCode #####
  def getcommand( self ):
    return cmds.symbolButton( self.uiName , q=1 , command=1 )
  def getimage( self ):
    return cmds.symbolButton( self.uiName , q=1 , image=1 )

  ##### setFuncCode #####
  def setcommand( self , value ):
    cmds.symbolButton( self.uiName , e=1 , command=value )
  def setimage( self , value ):
    cmds.symbolButton( self.uiName , e=1 , image=value )

  ##### propertyCode #####
  command = property( getcommand , setcommand )
  image = property( getimage , setimage )

  ##### customCode #####





class SymbolCheckBox( Control ):

  ##### initialize #####
  def __init__( self , changeCommand=None , disableOffImage=None , disableOnImage=None , image=None , innerMargin=None , offCommand=None , offImage=None , onCommand=None , onImage=None , value=None , **args ):
    self.uiName = cmds.symbolCheckBox()

    ##### substitution #####
    if changeCommand != None:
      self.changeCommand = changeCommand
    if disableOffImage != None:
      self.disableOffImage = disableOffImage
    if disableOnImage != None:
      self.disableOnImage = disableOnImage
    if image != None:
      self.image = image
    if innerMargin != None:
      self.innerMargin = innerMargin
    if offCommand != None:
      self.offCommand = offCommand
    if offImage != None:
      self.offImage = offImage
    if onCommand != None:
      self.onCommand = onCommand
    if onImage != None:
      self.onImage = onImage
    if value != None:
      self.value = value

  ##### getFuncCode #####
  def getchangeCommand( self ):
    return cmds.symbolCheckBox( self.uiName , q=1 , changeCommand=1 )
  def getdisableOffImage( self ):
    return cmds.symbolCheckBox( self.uiName , q=1 , disableOffImage=1 )
  def getdisableOnImage( self ):
    return cmds.symbolCheckBox( self.uiName , q=1 , disableOnImage=1 )
  def getimage( self ):
    return cmds.symbolCheckBox( self.uiName , q=1 , image=1 )
  def getinnerMargin( self ):
    return cmds.symbolCheckBox( self.uiName , q=1 , innerMargin=1 )
  def getoffCommand( self ):
    return cmds.symbolCheckBox( self.uiName , q=1 , offCommand=1 )
  def getoffImage( self ):
    return cmds.symbolCheckBox( self.uiName , q=1 , offImage=1 )
  def getonCommand( self ):
    return cmds.symbolCheckBox( self.uiName , q=1 , onCommand=1 )
  def getonImage( self ):
    return cmds.symbolCheckBox( self.uiName , q=1 , onImage=1 )
  def getvalue( self ):
    return cmds.symbolCheckBox( self.uiName , q=1 , value=1 )

  ##### setFuncCode #####
  def setchangeCommand( self , value ):
    cmds.symbolCheckBox( self.uiName , e=1 , changeCommand=value )
  def setdisableOffImage( self , value ):
    cmds.symbolCheckBox( self.uiName , e=1 , disableOffImage=value )
  def setdisableOnImage( self , value ):
    cmds.symbolCheckBox( self.uiName , e=1 , disableOnImage=value )
  def setimage( self , value ):
    cmds.symbolCheckBox( self.uiName , e=1 , image=value )
  def setinnerMargin( self , value ):
    cmds.symbolCheckBox( self.uiName , e=1 , innerMargin=value )
  def setoffCommand( self , value ):
    cmds.symbolCheckBox( self.uiName , e=1 , offCommand=value )
  def setoffImage( self , value ):
    cmds.symbolCheckBox( self.uiName , e=1 , offImage=value )
  def setonCommand( self , value ):
    cmds.symbolCheckBox( self.uiName , e=1 , onCommand=value )
  def setonImage( self , value ):
    cmds.symbolCheckBox( self.uiName , e=1 , onImage=value )
  def setvalue( self , value ):
    cmds.symbolCheckBox( self.uiName , e=1 , value=value )

  ##### propertyCode #####
  changeCommand = property( getchangeCommand , setchangeCommand )
  disableOffImage = property( getdisableOffImage , setdisableOffImage )
  disableOnImage = property( getdisableOnImage , setdisableOnImage )
  image = property( getimage , setimage )
  innerMargin = property( getinnerMargin , setinnerMargin )
  offCommand = property( getoffCommand , setoffCommand )
  offImage = property( getoffImage , setoffImage )
  onCommand = property( getonCommand , setonCommand )
  onImage = property( getonImage , setonImage )
  value = property( getvalue , setvalue )

  ##### customCode #####





class TimeControl( Control ):

  ##### initialize #####
  def __init__( self , animCurveNames=None , animLayerFilterOptions=None , animLayerShowWeight=None , beginScrub=None , displaySound=None , endScrub=None , forceRefresh=None , globalTime=None , mainListConnection=None , pressCommand=None , resample=None , rangeArray=None , releaseCommand=None , repeatChunkSize=None , range=None , repeatOnHold=None , rangeVisible=None , sound=None , showKeys=None , snap=None , tickSize=None , waveform=None , **args ):
    self.uiName = cmds.timeControl()

    ##### substitution #####
    if animCurveNames != None:
      self.animCurveNames = animCurveNames
    if animLayerFilterOptions != None:
      self.animLayerFilterOptions = animLayerFilterOptions
    if animLayerShowWeight != None:
      self.animLayerShowWeight = animLayerShowWeight
    if beginScrub != None:
      self.beginScrub = beginScrub
    if displaySound != None:
      self.displaySound = displaySound
    if endScrub != None:
      self.endScrub = endScrub
    if forceRefresh != None:
      self.forceRefresh = forceRefresh
    if globalTime != None:
      self.globalTime = globalTime
    if mainListConnection != None:
      self.mainListConnection = mainListConnection
    if pressCommand != None:
      self.pressCommand = pressCommand
    if resample != None:
      self.resample = resample
    if rangeArray != None:
      self.rangeArray = rangeArray
    if releaseCommand != None:
      self.releaseCommand = releaseCommand
    if repeatChunkSize != None:
      self.repeatChunkSize = repeatChunkSize
    if range != None:
      self.range = range
    if repeatOnHold != None:
      self.repeatOnHold = repeatOnHold
    if rangeVisible != None:
      self.rangeVisible = rangeVisible
    if sound != None:
      self.sound = sound
    if showKeys != None:
      self.showKeys = showKeys
    if snap != None:
      self.snap = snap
    if tickSize != None:
      self.tickSize = tickSize
    if waveform != None:
      self.waveform = waveform

  ##### getFuncCode #####
  def getanimCurveNames( self ):
    return cmds.timeControl( self.uiName , q=1 , animCurveNames=1 )
  def getanimLayerFilterOptions( self ):
    return cmds.timeControl( self.uiName , q=1 , animLayerFilterOptions=1 )
  def getanimLayerShowWeight( self ):
    return cmds.timeControl( self.uiName , q=1 , animLayerShowWeight=1 )
  def getbeginScrub( self ):
    return cmds.timeControl( self.uiName , q=1 , beginScrub=1 )
  def getdisplaySound( self ):
    return cmds.timeControl( self.uiName , q=1 , displaySound=1 )
  def getendScrub( self ):
    return cmds.timeControl( self.uiName , q=1 , endScrub=1 )
  def getforceRefresh( self ):
    return cmds.timeControl( self.uiName , q=1 , forceRefresh=1 )
  def getglobalTime( self ):
    return cmds.timeControl( self.uiName , q=1 , globalTime=1 )
  def getmainListConnection( self ):
    return cmds.timeControl( self.uiName , q=1 , mainListConnection=1 )
  def getpressCommand( self ):
    return cmds.timeControl( self.uiName , q=1 , pressCommand=1 )
  def getresample( self ):
    return cmds.timeControl( self.uiName , q=1 , resample=1 )
  def getrangeArray( self ):
    return cmds.timeControl( self.uiName , q=1 , rangeArray=1 )
  def getreleaseCommand( self ):
    return cmds.timeControl( self.uiName , q=1 , releaseCommand=1 )
  def getrepeatChunkSize( self ):
    return cmds.timeControl( self.uiName , q=1 , repeatChunkSize=1 )
  def getrange( self ):
    return cmds.timeControl( self.uiName , q=1 , range=1 )
  def getrepeatOnHold( self ):
    return cmds.timeControl( self.uiName , q=1 , repeatOnHold=1 )
  def getrangeVisible( self ):
    return cmds.timeControl( self.uiName , q=1 , rangeVisible=1 )
  def getsound( self ):
    return cmds.timeControl( self.uiName , q=1 , sound=1 )
  def getshowKeys( self ):
    return cmds.timeControl( self.uiName , q=1 , showKeys=1 )
  def getsnap( self ):
    return cmds.timeControl( self.uiName , q=1 , snap=1 )
  def gettickSize( self ):
    return cmds.timeControl( self.uiName , q=1 , tickSize=1 )
  def getwaveform( self ):
    return cmds.timeControl( self.uiName , q=1 , waveform=1 )

  ##### setFuncCode #####
  def setanimCurveNames( self , value ):
    cmds.timeControl( self.uiName , e=1 , animCurveNames=value )
  def setanimLayerFilterOptions( self , value ):
    cmds.timeControl( self.uiName , e=1 , animLayerFilterOptions=value )
  def setanimLayerShowWeight( self , value ):
    cmds.timeControl( self.uiName , e=1 , animLayerShowWeight=value )
  def setbeginScrub( self , value ):
    cmds.timeControl( self.uiName , e=1 , beginScrub=value )
  def setdisplaySound( self , value ):
    cmds.timeControl( self.uiName , e=1 , displaySound=value )
  def setendScrub( self , value ):
    cmds.timeControl( self.uiName , e=1 , endScrub=value )
  def setforceRefresh( self , value ):
    cmds.timeControl( self.uiName , e=1 , forceRefresh=value )
  def setglobalTime( self , value ):
    cmds.timeControl( self.uiName , e=1 , globalTime=value )
  def setmainListConnection( self , value ):
    cmds.timeControl( self.uiName , e=1 , mainListConnection=value )
  def setpressCommand( self , value ):
    cmds.timeControl( self.uiName , e=1 , pressCommand=value )
  def setresample( self , value ):
    cmds.timeControl( self.uiName , e=1 , resample=value )
  def setrangeArray( self , value ):
    cmds.timeControl( self.uiName , e=1 , rangeArray=value )
  def setreleaseCommand( self , value ):
    cmds.timeControl( self.uiName , e=1 , releaseCommand=value )
  def setrepeatChunkSize( self , value ):
    cmds.timeControl( self.uiName , e=1 , repeatChunkSize=value )
  def setrange( self , value ):
    cmds.timeControl( self.uiName , e=1 , range=value )
  def setrepeatOnHold( self , value ):
    cmds.timeControl( self.uiName , e=1 , repeatOnHold=value )
  def setrangeVisible( self , value ):
    cmds.timeControl( self.uiName , e=1 , rangeVisible=value )
  def setsound( self , value ):
    cmds.timeControl( self.uiName , e=1 , sound=value )
  def setshowKeys( self , value ):
    cmds.timeControl( self.uiName , e=1 , showKeys=value )
  def setsnap( self , value ):
    cmds.timeControl( self.uiName , e=1 , snap=value )
  def settickSize( self , value ):
    cmds.timeControl( self.uiName , e=1 , tickSize=value )
  def setwaveform( self , value ):
    cmds.timeControl( self.uiName , e=1 , waveform=value )

  ##### propertyCode #####
  animCurveNames = property( getanimCurveNames , setanimCurveNames )
  animLayerFilterOptions = property( getanimLayerFilterOptions , setanimLayerFilterOptions )
  animLayerShowWeight = property( getanimLayerShowWeight , setanimLayerShowWeight )
  beginScrub = property( getbeginScrub , setbeginScrub )
  displaySound = property( getdisplaySound , setdisplaySound )
  endScrub = property( getendScrub , setendScrub )
  forceRefresh = property( getforceRefresh , setforceRefresh )
  globalTime = property( getglobalTime , setglobalTime )
  mainListConnection = property( getmainListConnection , setmainListConnection )
  pressCommand = property( getpressCommand , setpressCommand )
  resample = property( getresample , setresample )
  rangeArray = property( getrangeArray , setrangeArray )
  releaseCommand = property( getreleaseCommand , setreleaseCommand )
  repeatChunkSize = property( getrepeatChunkSize , setrepeatChunkSize )
  range = property( getrange , setrange )
  repeatOnHold = property( getrepeatOnHold , setrepeatOnHold )
  rangeVisible = property( getrangeVisible , setrangeVisible )
  sound = property( getsound , setsound )
  showKeys = property( getshowKeys , setshowKeys )
  snap = property( getsnap , setsnap )
  tickSize = property( gettickSize , settickSize )
  waveform = property( getwaveform , setwaveform )

  ##### customCode #####





class TimePort( Control ):

  ##### initialize #####
  def __init__( self , globalTime=None , snap=None , **args ):
    self.uiName = cmds.timePort()

    ##### substitution #####
    if globalTime != None:
      self.globalTime = globalTime
    if snap != None:
      self.snap = snap

  ##### getFuncCode #####
  def getglobalTime( self ):
    return cmds.timePort( self.uiName , q=1 , globalTime=1 )
  def getsnap( self ):
    return cmds.timePort( self.uiName , q=1 , snap=1 )

  ##### setFuncCode #####
  def setglobalTime( self , value ):
    cmds.timePort( self.uiName , e=1 , globalTime=value )
  def setsnap( self , value ):
    cmds.timePort( self.uiName , e=1 , snap=value )

  ##### propertyCode #####
  globalTime = property( getglobalTime , setglobalTime )
  snap = property( getsnap , setsnap )

  ##### customCode #####





class ToolButton( Control ):

  ##### initialize #####
  def __init__( self , allowMultipleTools=None , changeCommand=None , collection=None , doubleClickCommand=None , image1=None , image2=None , image3=None , imageOverlayLabel=None , offCommand=None , onCommand=None , popupIndicatorVisible=None , select=None , style=None , tool=None , toolArray=None , toolCount=None , toolImage1=None , toolImage2=None , toolImage3=None , **args ):
    self.uiName = cmds.toolButton()

    ##### substitution #####
    if allowMultipleTools != None:
      self.allowMultipleTools = allowMultipleTools
    if changeCommand != None:
      self.changeCommand = changeCommand
    if collection != None:
      self.collection = collection
    if doubleClickCommand != None:
      self.doubleClickCommand = doubleClickCommand
    if image1 != None:
      self.image1 = image1
    if image2 != None:
      self.image2 = image2
    if image3 != None:
      self.image3 = image3
    if imageOverlayLabel != None:
      self.imageOverlayLabel = imageOverlayLabel
    if offCommand != None:
      self.offCommand = offCommand
    if onCommand != None:
      self.onCommand = onCommand
    if popupIndicatorVisible != None:
      self.popupIndicatorVisible = popupIndicatorVisible
    if select != None:
      self.select = select
    if style != None:
      self.style = style
    if tool != None:
      self.tool = tool
    if toolArray != None:
      self.toolArray = toolArray
    if toolCount != None:
      self.toolCount = toolCount
    if toolImage1 != None:
      self.toolImage1 = toolImage1
    if toolImage2 != None:
      self.toolImage2 = toolImage2
    if toolImage3 != None:
      self.toolImage3 = toolImage3

  ##### getFuncCode #####
  def getallowMultipleTools( self ):
    return cmds.toolButton( self.uiName , q=1 , allowMultipleTools=1 )
  def getchangeCommand( self ):
    return cmds.toolButton( self.uiName , q=1 , changeCommand=1 )
  def getcollection( self ):
    return cmds.toolButton( self.uiName , q=1 , collection=1 )
  def getdoubleClickCommand( self ):
    return cmds.toolButton( self.uiName , q=1 , doubleClickCommand=1 )
  def getimage1( self ):
    return cmds.toolButton( self.uiName , q=1 , image1=1 )
  def getimage2( self ):
    return cmds.toolButton( self.uiName , q=1 , image2=1 )
  def getimage3( self ):
    return cmds.toolButton( self.uiName , q=1 , image3=1 )
  def getimageOverlayLabel( self ):
    return cmds.toolButton( self.uiName , q=1 , imageOverlayLabel=1 )
  def getoffCommand( self ):
    return cmds.toolButton( self.uiName , q=1 , offCommand=1 )
  def getonCommand( self ):
    return cmds.toolButton( self.uiName , q=1 , onCommand=1 )
  def getpopupIndicatorVisible( self ):
    return cmds.toolButton( self.uiName , q=1 , popupIndicatorVisible=1 )
  def getselect( self ):
    return cmds.toolButton( self.uiName , q=1 , select=1 )
  def getstyle( self ):
    return cmds.toolButton( self.uiName , q=1 , style=1 )
  def gettool( self ):
    return cmds.toolButton( self.uiName , q=1 , tool=1 )
  def gettoolArray( self ):
    return cmds.toolButton( self.uiName , q=1 , toolArray=1 )
  def gettoolCount( self ):
    return cmds.toolButton( self.uiName , q=1 , toolCount=1 )
  def gettoolImage1( self ):
    return cmds.toolButton( self.uiName , q=1 , toolImage1=1 )
  def gettoolImage2( self ):
    return cmds.toolButton( self.uiName , q=1 , toolImage2=1 )
  def gettoolImage3( self ):
    return cmds.toolButton( self.uiName , q=1 , toolImage3=1 )

  ##### setFuncCode #####
  def setallowMultipleTools( self , value ):
    cmds.toolButton( self.uiName , e=1 , allowMultipleTools=value )
  def setchangeCommand( self , value ):
    cmds.toolButton( self.uiName , e=1 , changeCommand=value )
  def setcollection( self , value ):
    cmds.toolButton( self.uiName , e=1 , collection=value )
  def setdoubleClickCommand( self , value ):
    cmds.toolButton( self.uiName , e=1 , doubleClickCommand=value )
  def setimage1( self , value ):
    cmds.toolButton( self.uiName , e=1 , image1=value )
  def setimage2( self , value ):
    cmds.toolButton( self.uiName , e=1 , image2=value )
  def setimage3( self , value ):
    cmds.toolButton( self.uiName , e=1 , image3=value )
  def setimageOverlayLabel( self , value ):
    cmds.toolButton( self.uiName , e=1 , imageOverlayLabel=value )
  def setoffCommand( self , value ):
    cmds.toolButton( self.uiName , e=1 , offCommand=value )
  def setonCommand( self , value ):
    cmds.toolButton( self.uiName , e=1 , onCommand=value )
  def setpopupIndicatorVisible( self , value ):
    cmds.toolButton( self.uiName , e=1 , popupIndicatorVisible=value )
  def setselect( self , value ):
    cmds.toolButton( self.uiName , e=1 , select=value )
  def setstyle( self , value ):
    cmds.toolButton( self.uiName , e=1 , style=value )
  def settool( self , value ):
    cmds.toolButton( self.uiName , e=1 , tool=value )
  def settoolArray( self , value ):
    cmds.toolButton( self.uiName , e=1 , toolArray=value )
  def settoolCount( self , value ):
    cmds.toolButton( self.uiName , e=1 , toolCount=value )
  def settoolImage1( self , value ):
    cmds.toolButton( self.uiName , e=1 , toolImage1=value )
  def settoolImage2( self , value ):
    cmds.toolButton( self.uiName , e=1 , toolImage2=value )
  def settoolImage3( self , value ):
    cmds.toolButton( self.uiName , e=1 , toolImage3=value )

  ##### propertyCode #####
  allowMultipleTools = property( getallowMultipleTools , setallowMultipleTools )
  changeCommand = property( getchangeCommand , setchangeCommand )
  collection = property( getcollection , setcollection )
  doubleClickCommand = property( getdoubleClickCommand , setdoubleClickCommand )
  image1 = property( getimage1 , setimage1 )
  image2 = property( getimage2 , setimage2 )
  image3 = property( getimage3 , setimage3 )
  imageOverlayLabel = property( getimageOverlayLabel , setimageOverlayLabel )
  offCommand = property( getoffCommand , setoffCommand )
  onCommand = property( getonCommand , setonCommand )
  popupIndicatorVisible = property( getpopupIndicatorVisible , setpopupIndicatorVisible )
  select = property( getselect , setselect )
  style = property( getstyle , setstyle )
  tool = property( gettool , settool )
  toolArray = property( gettoolArray , settoolArray )
  toolCount = property( gettoolCount , settoolCount )
  toolImage1 = property( gettoolImage1 , settoolImage1 )
  toolImage2 = property( gettoolImage2 , settoolImage2 )
  toolImage3 = property( gettoolImage3 , settoolImage3 )

  ##### customCode #####





class ToolCollection( Control ):

  ##### initialize #####
  def __init__( self , collectionItemArray=None , gl=None , numberOfCollectionItems=None , select=None , **args ):
    self.uiName = cmds.toolCollection()

    ##### substitution #####
    if collectionItemArray != None:
      self.collectionItemArray = collectionItemArray
    if gl != None:
      self.gl = gl
    if numberOfCollectionItems != None:
      self.numberOfCollectionItems = numberOfCollectionItems
    if select != None:
      self.select = select

  ##### getFuncCode #####
  def getcollectionItemArray( self ):
    return cmds.toolCollection( self.uiName , q=1 , collectionItemArray=1 )
  def getgl( self ):
    return cmds.toolCollection( self.uiName , q=1 , gl=1 )
  def getnumberOfCollectionItems( self ):
    return cmds.toolCollection( self.uiName , q=1 , numberOfCollectionItems=1 )
  def getselect( self ):
    return cmds.toolCollection( self.uiName , q=1 , select=1 )

  ##### setFuncCode #####
  def setcollectionItemArray( self , value ):
    cmds.toolCollection( self.uiName , e=1 , collectionItemArray=value )
  def setgl( self , value ):
    cmds.toolCollection( self.uiName , e=1 , gl=value )
  def setnumberOfCollectionItems( self , value ):
    cmds.toolCollection( self.uiName , e=1 , numberOfCollectionItems=value )
  def setselect( self , value ):
    cmds.toolCollection( self.uiName , e=1 , select=value )

  ##### propertyCode #####
  collectionItemArray = property( getcollectionItemArray , setcollectionItemArray )
  gl = property( getgl , setgl )
  numberOfCollectionItems = property( getnumberOfCollectionItems , setnumberOfCollectionItems )
  select = property( getselect , setselect )

  ##### customCode #####





class TreeView( Control ):

  ##### initialize #####
  def __init__( self , attachButtonRight=None , addItem=None , allowReparenting=None , borderHighliteColor=None , borderHighlite=None , buttonStyle=None , buttonState=None , buttonTransparencyColor=None , buttonTextIcon=None , buttonTransparencyOverride=None , buttonTooltip=None , buttonVisible=None , children=None , contextMenuCommand=None , clearSelection=None , dragAndDropCommand=None , displayLabel=None , displayLabelSuffix=None , drawSelectionBackground=None , enableButton=None , expandCollapseCommand=None , expandItem=None , editLabelCommand=None , enableLabel=None , flatButton=None , fontFace=None , font=None , hideButtons=None , highliteColor=None , highlite=None , image=None , itemIndex=None , itemExists=None , isItemExpanded=None , isLeaf=None , itemParent=None , itemRenamedCommand=None , itemVisible=None , labelBackgroundColor=None , numberOfButtons=None , ornament=None , ornamentColor=None , pressCommand=None , removeAll=None , rightPressCommand=None , reverseTreeOrder=None , selectCommand=None , selectionChangedCommand=None , selectionColor=None , selectItem=None , select=None , textColor=None , **args ):
    self.uiName = cmds.treeView()

    ##### substitution #####
    if attachButtonRight != None:
      self.attachButtonRight = attachButtonRight
    if addItem != None:
      self.addItem = addItem
    if allowReparenting != None:
      self.allowReparenting = allowReparenting
    if borderHighliteColor != None:
      self.borderHighliteColor = borderHighliteColor
    if borderHighlite != None:
      self.borderHighlite = borderHighlite
    if buttonStyle != None:
      self.buttonStyle = buttonStyle
    if buttonState != None:
      self.buttonState = buttonState
    if buttonTransparencyColor != None:
      self.buttonTransparencyColor = buttonTransparencyColor
    if buttonTextIcon != None:
      self.buttonTextIcon = buttonTextIcon
    if buttonTransparencyOverride != None:
      self.buttonTransparencyOverride = buttonTransparencyOverride
    if buttonTooltip != None:
      self.buttonTooltip = buttonTooltip
    if buttonVisible != None:
      self.buttonVisible = buttonVisible
    if children != None:
      self.children = children
    if contextMenuCommand != None:
      self.contextMenuCommand = contextMenuCommand
    if clearSelection != None:
      self.clearSelection = clearSelection
    if dragAndDropCommand != None:
      self.dragAndDropCommand = dragAndDropCommand
    if displayLabel != None:
      self.displayLabel = displayLabel
    if displayLabelSuffix != None:
      self.displayLabelSuffix = displayLabelSuffix
    if drawSelectionBackground != None:
      self.drawSelectionBackground = drawSelectionBackground
    if enableButton != None:
      self.enableButton = enableButton
    if expandCollapseCommand != None:
      self.expandCollapseCommand = expandCollapseCommand
    if expandItem != None:
      self.expandItem = expandItem
    if editLabelCommand != None:
      self.editLabelCommand = editLabelCommand
    if enableLabel != None:
      self.enableLabel = enableLabel
    if flatButton != None:
      self.flatButton = flatButton
    if fontFace != None:
      self.fontFace = fontFace
    if font != None:
      self.font = font
    if hideButtons != None:
      self.hideButtons = hideButtons
    if highliteColor != None:
      self.highliteColor = highliteColor
    if highlite != None:
      self.highlite = highlite
    if image != None:
      self.image = image
    if itemIndex != None:
      self.itemIndex = itemIndex
    if itemExists != None:
      self.itemExists = itemExists
    if isItemExpanded != None:
      self.isItemExpanded = isItemExpanded
    if isLeaf != None:
      self.isLeaf = isLeaf
    if itemParent != None:
      self.itemParent = itemParent
    if itemRenamedCommand != None:
      self.itemRenamedCommand = itemRenamedCommand
    if itemVisible != None:
      self.itemVisible = itemVisible
    if labelBackgroundColor != None:
      self.labelBackgroundColor = labelBackgroundColor
    if numberOfButtons != None:
      self.numberOfButtons = numberOfButtons
    if ornament != None:
      self.ornament = ornament
    if ornamentColor != None:
      self.ornamentColor = ornamentColor
    if pressCommand != None:
      self.pressCommand = pressCommand
    if removeAll != None:
      self.removeAll = removeAll
    if rightPressCommand != None:
      self.rightPressCommand = rightPressCommand
    if reverseTreeOrder != None:
      self.reverseTreeOrder = reverseTreeOrder
    if selectCommand != None:
      self.selectCommand = selectCommand
    if selectionChangedCommand != None:
      self.selectionChangedCommand = selectionChangedCommand
    if selectionColor != None:
      self.selectionColor = selectionColor
    if selectItem != None:
      self.selectItem = selectItem
    if select != None:
      self.select = select
    if textColor != None:
      self.textColor = textColor

  ##### getFuncCode #####
  def getattachButtonRight( self ):
    return cmds.treeView( self.uiName , q=1 , attachButtonRight=1 )
  def getaddItem( self ):
    return cmds.treeView( self.uiName , q=1 , addItem=1 )
  def getallowReparenting( self ):
    return cmds.treeView( self.uiName , q=1 , allowReparenting=1 )
  def getborderHighliteColor( self ):
    return cmds.treeView( self.uiName , q=1 , borderHighliteColor=1 )
  def getborderHighlite( self ):
    return cmds.treeView( self.uiName , q=1 , borderHighlite=1 )
  def getbuttonStyle( self ):
    return cmds.treeView( self.uiName , q=1 , buttonStyle=1 )
  def getbuttonState( self ):
    return cmds.treeView( self.uiName , q=1 , buttonState=1 )
  def getbuttonTransparencyColor( self ):
    return cmds.treeView( self.uiName , q=1 , buttonTransparencyColor=1 )
  def getbuttonTextIcon( self ):
    return cmds.treeView( self.uiName , q=1 , buttonTextIcon=1 )
  def getbuttonTransparencyOverride( self ):
    return cmds.treeView( self.uiName , q=1 , buttonTransparencyOverride=1 )
  def getbuttonTooltip( self ):
    return cmds.treeView( self.uiName , q=1 , buttonTooltip=1 )
  def getbuttonVisible( self ):
    return cmds.treeView( self.uiName , q=1 , buttonVisible=1 )
  def getchildren( self ):
    return cmds.treeView( self.uiName , q=1 , children=1 )
  def getcontextMenuCommand( self ):
    return cmds.treeView( self.uiName , q=1 , contextMenuCommand=1 )
  def getclearSelection( self ):
    return cmds.treeView( self.uiName , q=1 , clearSelection=1 )
  def getdragAndDropCommand( self ):
    return cmds.treeView( self.uiName , q=1 , dragAndDropCommand=1 )
  def getdisplayLabel( self ):
    return cmds.treeView( self.uiName , q=1 , displayLabel=1 )
  def getdisplayLabelSuffix( self ):
    return cmds.treeView( self.uiName , q=1 , displayLabelSuffix=1 )
  def getdrawSelectionBackground( self ):
    return cmds.treeView( self.uiName , q=1 , drawSelectionBackground=1 )
  def getenableButton( self ):
    return cmds.treeView( self.uiName , q=1 , enableButton=1 )
  def getexpandCollapseCommand( self ):
    return cmds.treeView( self.uiName , q=1 , expandCollapseCommand=1 )
  def getexpandItem( self ):
    return cmds.treeView( self.uiName , q=1 , expandItem=1 )
  def geteditLabelCommand( self ):
    return cmds.treeView( self.uiName , q=1 , editLabelCommand=1 )
  def getenableLabel( self ):
    return cmds.treeView( self.uiName , q=1 , enableLabel=1 )
  def getflatButton( self ):
    return cmds.treeView( self.uiName , q=1 , flatButton=1 )
  def getfontFace( self ):
    return cmds.treeView( self.uiName , q=1 , fontFace=1 )
  def getfont( self ):
    return cmds.treeView( self.uiName , q=1 , font=1 )
  def gethideButtons( self ):
    return cmds.treeView( self.uiName , q=1 , hideButtons=1 )
  def gethighliteColor( self ):
    return cmds.treeView( self.uiName , q=1 , highliteColor=1 )
  def gethighlite( self ):
    return cmds.treeView( self.uiName , q=1 , highlite=1 )
  def getimage( self ):
    return cmds.treeView( self.uiName , q=1 , image=1 )
  def getitemIndex( self ):
    return cmds.treeView( self.uiName , q=1 , itemIndex=1 )
  def getitemExists( self ):
    return cmds.treeView( self.uiName , q=1 , itemExists=1 )
  def getisItemExpanded( self ):
    return cmds.treeView( self.uiName , q=1 , isItemExpanded=1 )
  def getisLeaf( self ):
    return cmds.treeView( self.uiName , q=1 , isLeaf=1 )
  def getitemParent( self ):
    return cmds.treeView( self.uiName , q=1 , itemParent=1 )
  def getitemRenamedCommand( self ):
    return cmds.treeView( self.uiName , q=1 , itemRenamedCommand=1 )
  def getitemVisible( self ):
    return cmds.treeView( self.uiName , q=1 , itemVisible=1 )
  def getlabelBackgroundColor( self ):
    return cmds.treeView( self.uiName , q=1 , labelBackgroundColor=1 )
  def getnumberOfButtons( self ):
    return cmds.treeView( self.uiName , q=1 , numberOfButtons=1 )
  def getornament( self ):
    return cmds.treeView( self.uiName , q=1 , ornament=1 )
  def getornamentColor( self ):
    return cmds.treeView( self.uiName , q=1 , ornamentColor=1 )
  def getpressCommand( self ):
    return cmds.treeView( self.uiName , q=1 , pressCommand=1 )
  def getremoveAll( self ):
    return cmds.treeView( self.uiName , q=1 , removeAll=1 )
  def getrightPressCommand( self ):
    return cmds.treeView( self.uiName , q=1 , rightPressCommand=1 )
  def getreverseTreeOrder( self ):
    return cmds.treeView( self.uiName , q=1 , reverseTreeOrder=1 )
  def getselectCommand( self ):
    return cmds.treeView( self.uiName , q=1 , selectCommand=1 )
  def getselectionChangedCommand( self ):
    return cmds.treeView( self.uiName , q=1 , selectionChangedCommand=1 )
  def getselectionColor( self ):
    return cmds.treeView( self.uiName , q=1 , selectionColor=1 )
  def getselectItem( self ):
    return cmds.treeView( self.uiName , q=1 , selectItem=1 )
  def getselect( self ):
    return cmds.treeView( self.uiName , q=1 , select=1 )
  def gettextColor( self ):
    return cmds.treeView( self.uiName , q=1 , textColor=1 )

  ##### setFuncCode #####
  def setattachButtonRight( self , value ):
    cmds.treeView( self.uiName , e=1 , attachButtonRight=value )
  def setaddItem( self , value ):
    cmds.treeView( self.uiName , e=1 , addItem=value )
  def setallowReparenting( self , value ):
    cmds.treeView( self.uiName , e=1 , allowReparenting=value )
  def setborderHighliteColor( self , value ):
    cmds.treeView( self.uiName , e=1 , borderHighliteColor=value )
  def setborderHighlite( self , value ):
    cmds.treeView( self.uiName , e=1 , borderHighlite=value )
  def setbuttonStyle( self , value ):
    cmds.treeView( self.uiName , e=1 , buttonStyle=value )
  def setbuttonState( self , value ):
    cmds.treeView( self.uiName , e=1 , buttonState=value )
  def setbuttonTransparencyColor( self , value ):
    cmds.treeView( self.uiName , e=1 , buttonTransparencyColor=value )
  def setbuttonTextIcon( self , value ):
    cmds.treeView( self.uiName , e=1 , buttonTextIcon=value )
  def setbuttonTransparencyOverride( self , value ):
    cmds.treeView( self.uiName , e=1 , buttonTransparencyOverride=value )
  def setbuttonTooltip( self , value ):
    cmds.treeView( self.uiName , e=1 , buttonTooltip=value )
  def setbuttonVisible( self , value ):
    cmds.treeView( self.uiName , e=1 , buttonVisible=value )
  def setchildren( self , value ):
    cmds.treeView( self.uiName , e=1 , children=value )
  def setcontextMenuCommand( self , value ):
    cmds.treeView( self.uiName , e=1 , contextMenuCommand=value )
  def setclearSelection( self , value ):
    cmds.treeView( self.uiName , e=1 , clearSelection=value )
  def setdragAndDropCommand( self , value ):
    cmds.treeView( self.uiName , e=1 , dragAndDropCommand=value )
  def setdisplayLabel( self , value ):
    cmds.treeView( self.uiName , e=1 , displayLabel=value )
  def setdisplayLabelSuffix( self , value ):
    cmds.treeView( self.uiName , e=1 , displayLabelSuffix=value )
  def setdrawSelectionBackground( self , value ):
    cmds.treeView( self.uiName , e=1 , drawSelectionBackground=value )
  def setenableButton( self , value ):
    cmds.treeView( self.uiName , e=1 , enableButton=value )
  def setexpandCollapseCommand( self , value ):
    cmds.treeView( self.uiName , e=1 , expandCollapseCommand=value )
  def setexpandItem( self , value ):
    cmds.treeView( self.uiName , e=1 , expandItem=value )
  def seteditLabelCommand( self , value ):
    cmds.treeView( self.uiName , e=1 , editLabelCommand=value )
  def setenableLabel( self , value ):
    cmds.treeView( self.uiName , e=1 , enableLabel=value )
  def setflatButton( self , value ):
    cmds.treeView( self.uiName , e=1 , flatButton=value )
  def setfontFace( self , value ):
    cmds.treeView( self.uiName , e=1 , fontFace=value )
  def setfont( self , value ):
    cmds.treeView( self.uiName , e=1 , font=value )
  def sethideButtons( self , value ):
    cmds.treeView( self.uiName , e=1 , hideButtons=value )
  def sethighliteColor( self , value ):
    cmds.treeView( self.uiName , e=1 , highliteColor=value )
  def sethighlite( self , value ):
    cmds.treeView( self.uiName , e=1 , highlite=value )
  def setimage( self , value ):
    cmds.treeView( self.uiName , e=1 , image=value )
  def setitemIndex( self , value ):
    cmds.treeView( self.uiName , e=1 , itemIndex=value )
  def setitemExists( self , value ):
    cmds.treeView( self.uiName , e=1 , itemExists=value )
  def setisItemExpanded( self , value ):
    cmds.treeView( self.uiName , e=1 , isItemExpanded=value )
  def setisLeaf( self , value ):
    cmds.treeView( self.uiName , e=1 , isLeaf=value )
  def setitemParent( self , value ):
    cmds.treeView( self.uiName , e=1 , itemParent=value )
  def setitemRenamedCommand( self , value ):
    cmds.treeView( self.uiName , e=1 , itemRenamedCommand=value )
  def setitemVisible( self , value ):
    cmds.treeView( self.uiName , e=1 , itemVisible=value )
  def setlabelBackgroundColor( self , value ):
    cmds.treeView( self.uiName , e=1 , labelBackgroundColor=value )
  def setnumberOfButtons( self , value ):
    cmds.treeView( self.uiName , e=1 , numberOfButtons=value )
  def setornament( self , value ):
    cmds.treeView( self.uiName , e=1 , ornament=value )
  def setornamentColor( self , value ):
    cmds.treeView( self.uiName , e=1 , ornamentColor=value )
  def setpressCommand( self , value ):
    cmds.treeView( self.uiName , e=1 , pressCommand=value )
  def setremoveAll( self , value ):
    cmds.treeView( self.uiName , e=1 , removeAll=value )
  def setrightPressCommand( self , value ):
    cmds.treeView( self.uiName , e=1 , rightPressCommand=value )
  def setreverseTreeOrder( self , value ):
    cmds.treeView( self.uiName , e=1 , reverseTreeOrder=value )
  def setselectCommand( self , value ):
    cmds.treeView( self.uiName , e=1 , selectCommand=value )
  def setselectionChangedCommand( self , value ):
    cmds.treeView( self.uiName , e=1 , selectionChangedCommand=value )
  def setselectionColor( self , value ):
    cmds.treeView( self.uiName , e=1 , selectionColor=value )
  def setselectItem( self , value ):
    cmds.treeView( self.uiName , e=1 , selectItem=value )
  def setselect( self , value ):
    cmds.treeView( self.uiName , e=1 , select=value )
  def settextColor( self , value ):
    cmds.treeView( self.uiName , e=1 , textColor=value )

  ##### propertyCode #####
  attachButtonRight = property( getattachButtonRight , setattachButtonRight )
  addItem = property( getaddItem , setaddItem )
  allowReparenting = property( getallowReparenting , setallowReparenting )
  borderHighliteColor = property( getborderHighliteColor , setborderHighliteColor )
  borderHighlite = property( getborderHighlite , setborderHighlite )
  buttonStyle = property( getbuttonStyle , setbuttonStyle )
  buttonState = property( getbuttonState , setbuttonState )
  buttonTransparencyColor = property( getbuttonTransparencyColor , setbuttonTransparencyColor )
  buttonTextIcon = property( getbuttonTextIcon , setbuttonTextIcon )
  buttonTransparencyOverride = property( getbuttonTransparencyOverride , setbuttonTransparencyOverride )
  buttonTooltip = property( getbuttonTooltip , setbuttonTooltip )
  buttonVisible = property( getbuttonVisible , setbuttonVisible )
  children = property( getchildren , setchildren )
  contextMenuCommand = property( getcontextMenuCommand , setcontextMenuCommand )
  clearSelection = property( getclearSelection , setclearSelection )
  dragAndDropCommand = property( getdragAndDropCommand , setdragAndDropCommand )
  displayLabel = property( getdisplayLabel , setdisplayLabel )
  displayLabelSuffix = property( getdisplayLabelSuffix , setdisplayLabelSuffix )
  drawSelectionBackground = property( getdrawSelectionBackground , setdrawSelectionBackground )
  enableButton = property( getenableButton , setenableButton )
  expandCollapseCommand = property( getexpandCollapseCommand , setexpandCollapseCommand )
  expandItem = property( getexpandItem , setexpandItem )
  editLabelCommand = property( geteditLabelCommand , seteditLabelCommand )
  enableLabel = property( getenableLabel , setenableLabel )
  flatButton = property( getflatButton , setflatButton )
  fontFace = property( getfontFace , setfontFace )
  font = property( getfont , setfont )
  hideButtons = property( gethideButtons , sethideButtons )
  highliteColor = property( gethighliteColor , sethighliteColor )
  highlite = property( gethighlite , sethighlite )
  image = property( getimage , setimage )
  itemIndex = property( getitemIndex , setitemIndex )
  itemExists = property( getitemExists , setitemExists )
  isItemExpanded = property( getisItemExpanded , setisItemExpanded )
  isLeaf = property( getisLeaf , setisLeaf )
  itemParent = property( getitemParent , setitemParent )
  itemRenamedCommand = property( getitemRenamedCommand , setitemRenamedCommand )
  itemVisible = property( getitemVisible , setitemVisible )
  labelBackgroundColor = property( getlabelBackgroundColor , setlabelBackgroundColor )
  numberOfButtons = property( getnumberOfButtons , setnumberOfButtons )
  ornament = property( getornament , setornament )
  ornamentColor = property( getornamentColor , setornamentColor )
  pressCommand = property( getpressCommand , setpressCommand )
  removeAll = property( getremoveAll , setremoveAll )
  rightPressCommand = property( getrightPressCommand , setrightPressCommand )
  reverseTreeOrder = property( getreverseTreeOrder , setreverseTreeOrder )
  selectCommand = property( getselectCommand , setselectCommand )
  selectionChangedCommand = property( getselectionChangedCommand , setselectionChangedCommand )
  selectionColor = property( getselectionColor , setselectionColor )
  selectItem = property( getselectItem , setselectItem )
  select = property( getselect , setselect )
  textColor = property( gettextColor , settextColor )

  ##### customCode #####





print "MODULE IMPORTED... MYAM_PyLib_mayaUI_control"