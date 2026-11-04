#-*- coding:UTF-8 -*-

#*******************************************************************************
'''

Tool Name     : MYAM_PyLib_mayaMessageAdapter
Description   : mayaMessagesプラグインを操作するためのアダプタモジュール

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
import sys

######################
## Import custom modules
######################

######################
## Reload custom modules
######################

######################
##### Main Class #####
######################

class MayaMessagesAdapter( object ):

  def __init__( self ):
    cmds.loadPlugin( 'mayaMessages.mll' , quiet=1 )

##    ## mayaMessages プラグインが登録されていれば
##    if cmds.pluginInfo( "mayaMessages" , q=1 , registered=1 ):
##      cmds.loadPlugin( 'D:/Puppeteer/Maya/2009/plug-ins/mayaMessages.mll' , quiet=1 )
##    else:
##      raise ValueError , 'mayaMessage.mll was not found.'

  ##################
  ##### METHOD #####
  ##################

  def disintegrateMessages( self ):
    currentMayaMessages = self.listMessages()
    splitMayaMessages   = currentMayaMessages.replace("|","").strip().split()
    return splitMayaMessages

  def	setCallback( self , callback=None , command=None , allowMultiple=None ):
    ## Check arguments
    if callback == None:
      raise ValueError , "Argument [callback] was not defined."

    if command == None:
      raise ValueError , "Argument [command] was not defined."

    ## Get current message info
    disintegratedMessages = self.disintegrateMessages()

    ## Delete exist callbacks
    if not allowMultiple:
      print "[REMOVE---]" , allowMultiple , command
      self.remove_command( command )

    ## Do set callback
    res = mel.eval( 'mayaSceneMessageCmd -setCallback "' + callback + '" "' + command + '"' )
    print "[CREATE CALLBACK]" , res , command.replace( "\\" , "" )



  #####
  ## Remove methods
  def remove_callbackId( self , callbackId ):
    print mel.eval( "mayaSceneMessageCmd -remove " + str( callbackId ) + ";" )

  def remove_command( self , removeCommand ):
    disintegratedMessages = self.disintegrateMessages()

    for i in range( 4 , len( disintegratedMessages ) , 4 ):
      ID         = disintegratedMessages[i][1:-1]
      callbackId = disintegratedMessages[i+1]
      val        = disintegratedMessages[i+2]
      command    = disintegratedMessages[i+3]

      if removeCommand == command.replace( "\\" , "" ):
        mel.eval( 'mayaSceneMessageCmd -remove ' + callbackId + ";" )
        print "[DELETE CALLBACK]" , ID , callbackId , val , command

  def remove_callback( self , callback ):
    pass

  def removeAll( self ):
    print mel.eval( "mayaSceneMessageCmd -removeAll;" )



  #####
  ## Print methods
  def printAll( self ):
    print mel.eval( "mayaSceneMessageCmd -printAll;" )

  def printMessageAll( self ):
    print mel.eval( "mayaSceneMessageCmd -printMessageAll;" )

  def printVersion( self ):
    print mel.eval( "mayaSceneMessageCmd -version;" )

  def printHelp( self ):
    print mel.eval( "mayaSceneMessageCmd -help;" )



  #####
  ##
  def listMessages( self ):
    return mel.eval( "mayaSceneMessageCmd -printAll;" )

  def listCallbacks( self ):
    return mel.eval( "mayaSceneMessageCmd -printMessageAll;" )

  def getVersion( self ):
    return mel.eval( "mayaSceneMessageCmd -version;" )





######################
## Imported message
######################
print "MODULE IMPORTED... MYAM_PyLib_mayaMessageAdapter"
