import maya.cmds as mc
import sys

def createUI():
    winID='cableTool'
    if mc.window(winID, exists=True):
        mc.deleteUI(winID)
    mc.window(winID, title='Cable Tool', s=True, mxb=False, rtf=True)
    mc.frameLayout( label='Cable Tool', mh=10, mw=10)
    mc.rowLayout(numberOfColumns=3, columnWidth3=(110, 110, 110))
    mc.button(label='Create Cable', h=40, w=100, command='createCable()')
    mc.button(label='Bake Cable', h=40, w=100, command='bakeCable()')
    mc.button(label='Reverse Selected', h=40, w=100, command='reverseCable()')
    mc.setParent('..')
    mc.separator( h=5 )
    mc.setParent('..')
    mc.frameLayout( label='Cable Settings', mh=10, mw=10)
    mc.rowColumnLayout(numberOfColumns=3, columnWidth=[(1, 70), (2, 50), (3, 190)])
    #------------------------Size---
    mc.text('Size', align='left')
    global sizeSlider, sizeField
    sizeField = mc.floatField( min=0.02, max=100, value=1, step=0.2, pre=2, cc='setCableSize("field")', en=False)
    sizeSlider = mc.floatSlider( min=0.02, max=100, value=1, step=0.2, dc='setCableSize("slider")', en=False )
    #------------------------Sweep---    Fehler???
    mc.text('Sweep', align='left')
    global sweepSlider, sweepField
    sweepField = mc.floatField( min=0.02, max=360, value=360, step=0.2, pre=2, cc='setCableSweep("field")', en=False)
    sweepSlider = mc.floatSlider( min=0.02, max=360, value=360, step=1, dc='setCableSweep("slider")', en=False )
    #------------------------U Tesselation---
    mc.text('U Tesselation', align='left')
    global utessSlider, utessField
    utessField = mc.intField( min=1, max=100, value=10, step=1, cc='setUTess("field")', en=False)
    utessSlider = mc.intSlider( min=1, max=100, value=10, step=1, dc='setUTess("slider")', en=False )
    #------------------------V Tesselation---
    mc.text('V Tesselation', align='left')
    global vtessSlider, vtessField
    vtessField = mc.intField( min=1, max=100, value=10, step=1, cc='setVTess("field")', en=False)
    vtessSlider = mc.intSlider( min=1, max=100, value=10, step=1, dc='setVTess("slider")', en=False )
    #------------------------V Tesselation---
    mc.setParent('..')
    mc.setParent('..')
    mc.frameLayout( label='Bake Settings', mh=10, mw=10)
    mc.rowLayout(numberOfColumns=3, columnWidth3=(70, 80, 80))
    mc.text('Delete:', align='left')
    global historyDel, pathDel
    historyDel = mc.checkBox( label='History', align='left', en=False, v=True )
    pathDel = mc.checkBox( label='Path', align='left', en=False )
    mc.showWindow()
    resetVar()
        
def createCable():    
    global paths, tesselation, cable, extrudeNode
    tesselation = {}
    extrudeNode = {}
    
    tempSel = mc.ls(sl=True)
    
    bakeCable()
    
    paths = tempSel
    curveCheck = False
    
    for i in range(len(paths)):
        curveCheck = True
        if mc.objectType(mc.listRelatives(paths[i], s=True ), isType='nurbsCurve') == 0:
            sys.stdout.write('Please select only Curves!')
            curveCheck = False
            break

    if curveCheck:
        createProfile()
        for i in range(len(paths)):
            tempextrude = mc.extrude( profile[0], paths[i], et=2, fpt=True, ucp=1, upn=1, po=1, n='cable'  )
            cable[i] = tempextrude[0]
            extrudeNode[i] = tempextrude[1]
            tesstemp = mc.listConnections(tempextrude[1], d=True, s=False )
            tesselation[i] = tesstemp[0]      
        setSettings()
        activateSettings()
        for i in range(len(cable)):
            mc.select(cable[i], add=True)
    else:
        sys.stdout.write('Please select a Curve!')
    
def createProfile():
    global profile
    profile = mc.circle ( n="cableProfile", nr=(0, 0, 1), c=(0, 0, 0), r=1 )
    
def bakeCable():
    deactivateSettings()
    global cable, profile, paths
    if cable != {} and mc.checkBox(historyDel, q=True, v=True):
        for i in range(len(cable)):
            try:
                mc.select(cable[i])
                mc.delete(ch=True)        
            except:
                sys.stdout.write('Cable dont exist anymore!')
        cable={}
        mc.select(clear=True)
    
    if profile != {} and mc.checkBox(historyDel, q=True, v=True):
        try:
            mc.delete(profile)
        except:
            sys.stdout.write('Profile dont exist anymore!')
        profile={}
        
    if paths != {} and mc.checkBox(pathDel, q=True, v=True):
        print(paths)
        for i in range(len(paths)):
            try:
                mc.delete(paths[i])        
            except:
                sys.stdout.write('Paths dont exist anymore!')
        paths={}
        
def reverseCable():
    mc.selectMode( object=True )
    selection = mc.ls(sl=True)
    
    for i in range(len(selection)):
        mc.select(selection[i])
        mc.polyNormal()
        
    mc.select(selection)  

def resetVar():
    global paths, cable, profile
    paths={}
    cable={}
    profile={}
        
#--------------------------Settings--------------------------

def activateSettings():
    mc.floatField(sizeField, e=True, en=True )
    mc.floatSlider(sizeSlider, e=True, en=True )
    mc.floatField(sweepField, e=True, en=True )
    mc.floatSlider(sweepSlider, e=True, en=True )
    mc.intField(utessField, e=True, en=True )
    mc.intSlider(utessSlider, e=True, en=True )
    mc.intField(vtessField, e=True, en=True )
    mc.intSlider(vtessSlider, e=True, en=True )
    mc.checkBox(historyDel, e=True, en=True)
    mc.checkBox(pathDel, e=True, en=True)
    
def deactivateSettings():
    mc.floatField(sizeField, e=True, en=False )
    mc.floatSlider(sizeSlider, e=True, en=False )
    mc.floatField(sweepField, e=True, en=False )
    mc.floatSlider(sweepSlider, e=True, en=False )
    mc.intField(utessField, e=True, en=False )
    mc.intSlider(utessSlider, e=True, en=False )
    mc.intField(vtessField, e=True, en=False )
    mc.intSlider(vtessSlider, e=True, en=False )
    mc.checkBox(historyDel, e=True, en=False)
    mc.checkBox(pathDel, e=True, en=False)
    
def setSettings():
    setCableSize("slider")
    setCableSweep("slider")
    setUTess("slider")
    setVTess("slider")
    setDefaults()
       
def setDefaults():
    for i in range(len(tesselation)):
        mc.setAttr(tesselation[i]+'.polygonType', 1)
        mc.setAttr(tesselation[i]+'.format', 2)
                  
def setCableSize(type):
    if type == "slider":
        size = mc.floatSlider(sizeSlider, q=True, v=True)
        mc.floatField(sizeField, e=True, v=size )
    else:
        size = mc.floatField(sizeField, q=True, v=True) 
        mc.floatSlider(sizeSlider, e=True, v=size )
        
    mc.setAttr(profile[1]+'.radius', size)  
    
def setCableSweep(type):
    if type == "slider":
        sweep = mc.floatSlider(sweepSlider, q=True, v=True)
        mc.floatField(sweepField, e=True, v=sweep )
    else:
        sweep = mc.floatField(sweepField, q=True, v=True) 
        mc.floatSlider(sweepSlider, e=True, v=sweep )
        
    mc.setAttr(profile[1]+'.sweep', sweep)    
    
def setUTess(type):
    if type == "slider":
        utess = mc.intSlider(utessSlider, q=True, v=True)
        mc.intField(utessField, e=True, v=utess )
    else:
        utess = mc.intField(utessField, q=True, v=True) 
        mc.intSlider(utessSlider, e=True, v=utess )
           
    for i in range(len(tesselation)):
        mc.setAttr(tesselation[i]+'.uNumber', utess) 
    
def setVTess(type):
    if type == "slider":
        vtess = mc.intSlider(vtessSlider, q=True, v=True)
        mc.intField(vtessField, e=True, v=vtess )
    else:
        vtess = mc.intField(vtessField, q=True, v=True) 
        mc.intSlider(vtessSlider, e=True, v=vtess )
    
    for i in range(len(tesselation)):
        mc.setAttr(tesselation[i]+'.vNumber', vtess)        
    
createUI()