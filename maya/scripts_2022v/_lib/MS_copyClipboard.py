import subprocess
import os, ctypes 

def copyClipboard( text ):
	try:
		p = subprocess.Popen( ['clip'], stdin=subprocess.PIPE, shell=True )
		p.stdin.write( text )
		p.stdin.close()
 
		retcode = p.wait()
		return True
	except Exception as inst:
		return False

def copyText(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

def pasteText():
    CF_UNICODETEXT = 13
    d = ctypes.windll
    d.user32.OpenClipboard(None)
    handle = d.user32.GetClipboardData(CF_UNICODETEXT)
    data = ctypes.c_wchar_p(handle).value
    d.user32.CloseClipboard()
    return data
