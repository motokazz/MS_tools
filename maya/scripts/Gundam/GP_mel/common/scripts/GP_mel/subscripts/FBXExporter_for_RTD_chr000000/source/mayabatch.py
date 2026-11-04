import os
import sys
 
mayaScene = sys.argv[2]
 
f = open('MayaLocation.txt')
line = f.readline()
f.close

mayaExe = line

mayaExe = '\"' + mayaExe + '\"'

mayaCmd = sys.argv[1].replace("\\", "/")
mayaCmd = "source " + '\\\"' + mayaCmd + "FBXExporter_for_RTD_chr000000.mel"
mayaCmd = '\"' + mayaCmd + '\\\"'
 
CMD = '\"' + mayaExe +' -file ' + mayaScene + ' -command ' + mayaCmd + '\"'

#print CMD
#print mayaCmd
 
os.system(CMD)
