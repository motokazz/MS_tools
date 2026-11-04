
def MS_pyExec(MSPY):
	import sys
	sys.path.append( 'D:/MS_tools' )
	exec('import '+MSPY)
	exec('reload('+MSPY+')')

