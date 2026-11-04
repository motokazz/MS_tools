# -*- coding:utf-8 -*-
#ファイルリスト検索

###############
# メインユーティリティ
###############

WALKED_DATA=[]

def walked(SEARCH_PATH):
	global WALKED_DATA
	WALKED_DATA=[]
	for (root,dir,files) in os.walk(SEARCH_PATH):
		WALKED_DATA.append([root,files])
	print (WALKED_DATA)

def searchPath(SEARCH_PATH,SEARCH_FILE='',TARGET_EXT='py'):
	global WALKED_DATA
	for EACH in WALKED_DATA:
		if TARGET_EXT=='py':
			if SEARCH_FILE+'.py' in EACH[1]:
				root=EACH[0].replace('\\','/').replace('//','/')
				if root+'/' == pythonRootPath:
					return SEARCH_FILE+'.py'
				else:
					return root.replace(pythonRootPath,'')+'/'+SEARCH_FILE+'.py'
		elif TARGET_EXT=='mel':
			if SEARCH_FILE+'.mel' in EACH[1]:
				root=EACH[0].replace('\\','/').replace('//','/')
				if root+'/' == melRootPath:
					return SEARCH_FILE+'.mel'
				else:
					return root.replace(melRootPath,'')+'/'+SEARCH_FILE+'.mel'
	return ''

def searchIcon(SEARCH_PATH,SEARCH_FILE=''):
	global WALKED_DATA
	FORMAT=['','.bmp','.png','.xpm']

	if '/' in SEARCH_FILE or '\\' in SEARCH_FILE:

		SPLITTED_PATH = SEARCH_FILE.replace('\\','/').split('/')
		RPATH = '/'.join(SPLITTED_PATH[:-1])
		for EACH in WALKED_DATA:
			if RPATH in EACH[0]:
				root=EACH[0].replace('\\','/').replace('//','/')
				if os.path.exists(root+'/'+SPLITTED_PATH[-1]):
					return root+'/'+SPLITTED_PATH[-1]

	for EACH in WALKED_DATA:
		for EACHFORMAT in FORMAT:
			if SEARCH_FILE+EACHFORMAT in EACH[1]:
				root=EACH[0].replace('\\','/').replace('//','/')
				if os.path.exists(root+'/'+SEARCH_FILE+EACHFORMAT):
					return root+'/'+SEARCH_FILE+EACHFORMAT
	return ''


