def getFaceNormal( face ):  
	try:  
		normal = cmds.polyInfo( face, faceNormals=True )[0]  
		temp   = normal.split(" ")  
		result = [ float( temp[-3] ), float( temp[-2] ), float( temp[-1] ) ]  
		return result  
	except:  
		return False 
