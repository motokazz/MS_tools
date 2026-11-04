'''
MS_pyDragDrop
.py(Python File) possible to execute Drag & Drop from WindowsExploror.
'''
import maya.OpenMaya as OpenMaya
import sys
## add Callback
def MS_pyDragDrop(retCode, fileObject ,c):
	path = fileObject.rawPath ()
	comPath=path[:-1]
	name = fileObject.rawName()
	comName=name.replace(".py","")
	if '.py' in name:
		print 'Python file importing..'
		print 'execfile(\''+comPath+'/'+comName+'.py\')'
		print comName+'()'
		#sys.path.append( comPath )
		#exec('import '+comName)
		#exec('reload('+comName+')')
		execfile(comPath+'/'+comName+'.py')
		exec(comName+'()')

	else:
		util = OpenMaya.MScriptUtil()
		util.setBool ( retCode, True)

id = OpenMaya.MSceneMessage_addCheckFileCallback(OpenMaya.MSceneMessage.kBeforeImportCheck, MS_pyDragDrop)

## remove Callback
#OpenMaya.MMessage_removeCallback( id )




