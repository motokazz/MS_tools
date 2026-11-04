import maya.cmds as mc

def createUI():
    winID='MultiobjectTool'
    if mc.window(winID, exists=True):
        mc.deleteUI(winID)
    mc.window(winID, title='Multiobject Tool', s=True, mxb=False, rtf=True)
    mc.frameLayout( label='Multiobject Tool', mh=10, mw=10)
    mc.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, 110), (2, 210)], rs=(1,10), cs=(2,20))
    global selectName, selectField, combineButton, seperateButton, clearButton
    mc.button(label='Select by Selection', h=20, w=110, command='storeSelection()')
    selectField = mc.textField( w=210, ed=False, text='No Objects selected')
    mc.button(label='Select by Name', h=20, w=110, command='selectObjects()')
    selectName = mc.textField(w=210)
    mc.setParent('..')
    mc.separator( h=5 )
    mc.frameLayout( label='Functions', mh=10, mw=10)
    mc.rowLayout(numberOfColumns=3, columnWidth3=(110, 110, 110))
    combineButton = mc.button(label='Combine', h=40, w=100, command='combine()', en=False)
    seperateButton = mc.button(label='Seperate', h=40, w=100, command='seperate()', en=False)
    clearButton = mc.button(label='Clear Selection', h=40, w=100, command='clear()', en=False)
    mc.setParent('..')
    mc.showWindow()
    
def selectObjects():
    global selection
    if mc.textField(selectName, q=True, text=True) != '':
        mc.select('*'+mc.textField(selectName, q=True, text=True)+'*')
        selection = mc.ls( sl=True )
        activateButtons()
        mc.textField(selectField, e=True, text='Selection by Name active')
    else:
        mc.textField(selectField, e=True, text='No Objects found') 
        deactivateButtons()
        
def storeSelection():
    mc.selectMode( object=True )
    global selection
    selection = mc.ls(sl=True)
    if selection != []:
        mc.textField(selectField, e=True, text='Selection by Selection active')
        activateButtons()
    else:
        mc.textField(selectField, e=True, text='No Objects selected')
        deactivateButtons()
    
def combine():
    try:
        mc.select( selection )
        if mc.textField(selectName, q=True, text=True) == '':
            mc.polyUnite( mc.ls(sl=True), n=selection[0] )
        else:
            mc.polyUnite( mc.ls(sl=True), n=mc.textField(selectName, q=True, text=True) )
        
        mc.delete( ch=True )
        mc.xform( cp=1 )
        
        global selection
        selection = mc.ls( sl=True )
    except:
        print('Nothing to Combine')  
      
def seperate():
    try:
        mc.select( selection )
        mc.polySeparate( mc.ls(sl=True), n=mc.textField(selectName, q=True, text=True) )
        mc.delete( ch=True )
        mc.xform( cp=1 )
        
        global selection
        selection = mc.ls( sl=True )
    except:
        print('Nothing to Seperate')  
        
def clear():
    mc.select( clear=True )
    global selection
    selection = mc.ls( sl=True )
    mc.textField(selectField, e=True, text='No Objects selected')
    mc.textField(selectName, e=True, text='')
    deactivateButtons()
    
    
def activateButtons():
    mc.button(combineButton, e=True, en=True )
    mc.button(seperateButton, e=True, en=True )
    mc.button(clearButton, e=True, en=True )

    
def deactivateButtons():
    mc.button(combineButton, e=True, en=False )
    mc.button(seperateButton, e=True, en=False )
    mc.button(clearButton, e=True, en=False )

    
createUI()