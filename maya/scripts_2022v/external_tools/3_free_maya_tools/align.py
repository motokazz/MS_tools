import maya.cmds as mc
import maya.api.OpenMaya as om
import sys

global obj 
obj = None
global xaxis, yaxis, zaxis
xaxis = 1
yaxis = 0
zaxis = 0

def createUI():
    winID='alignTool'
    if mc.window(winID, exists=True):
        mc.deleteUI(winID)
    mc.window(winID, title='Object Aligner', s=True, mxb=False, rtf=True)
    mc.frameLayout( label='Align Tool', mh=10, mw=10)
    mc.frameLayout( label='Repro Selection', mh=10, mw=10)
    global selection, axisColl, invertBox, faceSelTF1, faceSelTF2
    selection = mc.textField( text='No Object saved', ed=False )
    mc.setParent('..')
    mc.frameLayout( label='Face Selection', mh=10, mw=10)
    mc.rowLayout(numberOfColumns=2, columnWidth=(200, 50))
    mc.rowColumnLayout( numberOfColumns=3, cw=[(1,25),(2,25),(3,170)] )
    mc.radioCollection()
    saveicon = mc.internalVar( upd=True )+'icons/save.PNG'
    arrowicon = mc.internalVar( upd=True )+'icons/arrow.PNG'
    mergeicon = mc.internalVar( upd=True )+'icons/merge.PNG'
    #-------------------------------------------------------
    mc.iconTextButton( style='iconOnly', image1=arrowicon, label='select', c='selectFaces(0)' )
    mc.iconTextButton( style='iconOnly', image1=saveicon, label='save', c='storeFaces(0)' )
    faceSelTF1 = mc.textField( text='No Selection saved', ed=False )
    #-------------------------------------------------------
    mc.iconTextButton( style='iconOnly', image1=arrowicon, label='select', c='selectFaces(1)' )
    mc.iconTextButton( style='iconOnly', image1=saveicon, label='save', c='storeFaces(1)' )
    faceSelTF2 = mc.textField( text='No Selection saved', ed=False )
    #-------------------------------------------------------
    mc.setParent('..')
    mc.iconTextButton( style='iconOnly', image1=mergeicon, label='merge', c='merge()' )
    mc.setParent('..')
    mc.separator( h=5 )
    mc.rowLayout(numberOfColumns=5, columnWidth5=(90, 30, 30, 50, 50))
    mc.text('Align ... to X :       ')
    axisColl = mc.radioCollection()
    mc.radioButton( label='X', onc='changeAxis("X")', sl=True )
    mc.radioButton( label='Y', onc='changeAxis("Y")' )
    mc.radioButton( label='Z', onc='changeAxis("Z")' )
    invertBox = mc.checkBox( label='Invert', cc='setInvert()' )
    mc.setParent('..')
    mc.separator( h=5 )
    mc.rowLayout(numberOfColumns=2, columnWidth2=(150, 150))
    mc.button(label='Save Repro', h=30, w=120, command='storeRepro()')
    mc.button(label='Align to Face', h=30, w=120, command='alignToFace()')
    mc.setParent('..')
    mc.separator( h=5 )
    mc.rowLayout(numberOfColumns=2, columnWidth2=(150, 150))
    global combineBut, selectBut
    combineBut = mc.button(label='Combine Output', h=30, w=120, command='combineOutput()', en=False )
    selectBut = mc.button(label='Select Output', h=30, w=120, command='selectOutput()', en=False )
    #delete output button?
    mc.setParent('..')
    mc.showWindow()
    resetVar()

def resetVar():
    global outputObj, outputGroup, faceSel1, faceSel2
    outputObj = []
    outputGroup = []
    faceSel1 = []
    faceSel2 = []

def storeRepro():
    #In den Objekt Modus wechseln
    mc.selectMode( object=True )
    global obj
    obj = mc.ls(sl=True)
    try:
        mc.textField(selection, e=True, text=obj[0])
    except IndexError:
        mc.textField(selection, e=True, text='Select an Object to save')

def storeFaces(index):
    global faceSelTF1, faceSelTF2, faceSel1, faceSel2
    if index == 0:
        mc.select(mc.polyListComponentConversion( mc.ls(sl=True), tf=True ))
        faceSel1 = mc.ls(sl=True)
        mc.textField(faceSelTF1, e=True, text='Selection saved')
    elif index ==1:
        mc.select(mc.polyListComponentConversion( mc.ls(sl=True), tf=True ))
        faceSel2 = mc.ls(sl=True)
        mc.textField(faceSelTF2, e=True, text='Selection saved')
    
def selectFaces(index):
    global faceSel1, faceSel2
    if index == 0:
        try: 
            mc.select(faceSel1)
        except:
            faceSel1 = []
            mc.textField(faceSelTF1, e=True, text='No Selection saved')
    elif index ==1:
        try: 
            mc.select(faceSel2)
        except:
            faceSel2 = []
            mc.textField(faceSelTF2, e=True, text='No Selection saved')   
    
def merge():
    mc.select(faceSel1) 
    mc.select(faceSel2, add=True)

def changeAxis(axis):
    global xaxis, yaxis, zaxis, outputObj, outputGroup, invert
    #Axis abfragen und setzen
    if axis == "X":
        xaxis = 1
        yaxis = 0
        zaxis = 0
    elif axis == "Y":
        xaxis = 0
        yaxis = 1
        zaxis = 0
    elif axis == "Z":
        xaxis = 0
        yaxis = 0
        zaxis = 1
        
    if mc.checkBox(invertBox, q=True, v=True):
        xaxis *= -1
        yaxis *= -1
        zaxis *= -1
      
    #Falls output schon vorhanden ist, neu berechnen
    if outputGroup != []:
        mc.select(sel)
        mc.delete( outputObj )
        mc.delete( outputGroup )
        outputObj = []
        outputGroup = []
        alignToFace()
   
def setInvert():
    changeAxis(mc.radioButton(mc.radioCollection(axisColl, q=True, sl=True), query=True, label=True))
        
def alignToFace():
    global outputObj, outputGroup, sel
    outputGroup = []
    outputObj = []
    
    #In Face Selection umwandeln (falls nicht im Face Modus)
    mc.select(mc.polyListComponentConversion( mc.ls(sl=True), tf=True ))
    sel = mc.ls(sl=True)
    
    #Auf das Movetool wechseln
    mc.setToolTo( 'moveSuperContext' ) 
    
    if sel != []:          
        #Gruppe für Output erstellen
        outputGroup = mc.group( em=True, name='output' )

        #Check ob das Selektierte Objekt geloescht wurde
        try:
            mc.select(obj)
        except:
            mc.textField(selection, e=True, text='Selection Missing')
            global obj
            obj = None
            
        for face in sel:
            newsel = mc.filterExpand(face, sm=34)
            for newface in newsel:    
                mc.select( newface )
                
                #Positions bestimmen
                pos1 = mc.manipMoveContext('Move', q=True, p=True) 
                mc.move(10, 0, 0, relative=True, co=True)
                pos2 = mc.manipMoveContext('Move', q=True, p=True) 
                    
                #Locator Spawnen
                mc.spaceLocator(n='templocator1', p=pos1)
                mc.xform(mc.ls(sl=True), cp=1)
                mc.spaceLocator(n='templocator2', p=pos2)
                mc.xform(mc.ls(sl=True), cp=1)
                #mc.curve(p=[pos1, pos2] )
                    
                #Transform Rueckgaengig machen
                mc.select(newface)
                mc.move(-10, 0, 0, relative=True, co=True)
                
                #Locator Aimen fuer Ausrichtung
                mc.aimConstraint( 'templocator2', 'templocator1', aim=[xaxis,yaxis,zaxis] )
                #Auswahl fuer UpVector machen (x y z)
                 
                #If selection empty
                if obj is None:
                    #Objekt Spawnen, parenten und Transform Matchen
                    mc.polyCylinder( ch=True, r=2, h=0.5 ,sz=1, n='placeholder#')
                else:
                    mc.select(obj)
                    mc.duplicate()
                
                mc.parent( mc.ls(sl=True), outputGroup )
                                         
                mc.matchTransform(mc.ls(sl=True),'templocator1', pos=True, rot=True)
                    
                #Hilfslocator Loeschen
                mc.delete( 'templocator2', 'templocator1' )
        
        #Objekte abspeichern
        outputObj = mc.listRelatives(outputGroup)
        setOutputButtons(True)
                        
        #Get and Select Same
        transnode = mc.listRelatives(sel[0], allParents=True)
        transnode = mc.listRelatives(transnode, allParents=True)
        mc.hilite(transnode)
        mc.select(sel)
    else:
        sys.stdout.write('No Faces selected!')
        setOutputButtons(False)
        
def combineOutput():
    global outputObj, outputGroup
    #Wenn mehr als ein Objekt erstellt wurde...Objekte combinen
    if len(outputObj) > 1:
        mc.select( outputObj )
        mc.polyUnite( mc.ls(sl=True), n='output' )
        mc.delete( ch=True )
        outputObj = mc.ls(sl=True)
        outputGroup = []
        mc.xform( cp=True )
    mc.button(combineBut, e=True, en=False)        
    
def selectOutput():
    global outputObj
    #Ouput selektieren...sofern möglich
    if outputObj != []:
        try:
            mc.select( outputObj )
        except:
            outputObj = []
            setOutputButtons(False)
            sys.stdout.write('Output not found! (maybe they were renamed or deleted)')
    
def setOutputButtons(active):
    mc.button(combineBut, e=True, en=active)
    mc.button(selectBut, e=True, en=active)
        
createUI()