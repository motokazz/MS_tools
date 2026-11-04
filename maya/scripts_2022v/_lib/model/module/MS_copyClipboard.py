import subprocess

def copyClipboard( text ):
	try:
		p = subprocess.Popen( ['clip'], stdin=subprocess.PIPE, shell=True )
		p.stdin.write( text )
		p.stdin.close()
 
		retcode = p.wait()
		return True
	except Exception, inst:
		return False
	   