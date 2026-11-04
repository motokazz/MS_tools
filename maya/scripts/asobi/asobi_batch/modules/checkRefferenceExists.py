# _*_coding:utf-8_*_
########################################
# ファイル名
#			checkRefferenceExists.py
# 説明
#			
#			
# 作成日
#			
########################################
def searchPath(SEARCHPATH,searchFile='',searchExt='mb'):
	for (root,dir,files) in os.walk(SEARCHPATH):
		#発見時の処理
		for f in files:
			
			fname=f.split('.')[0]
			if (searchFile+'.'+searchExt) == f:
				root=root.replace('\\','/').replace('//','/')
				print root+'/'+f
				return root+'/'+f
	return False
def searchDir(SEARCHPATH,searchDir=''):
	for (root,dir,files) in os.walk(SEARCHPATH):
		#発見時の処理
		for d in dir:
			print d
			if searchDir == d:
				print d
				root=root.replace('\\','/').replace('//','/')
				return root+'/'+d
	return False



def main(TARGET_NAME=''):
	#forQuery
	if not TARGET_NAME:return False
	return searchDir(u'\\Fs03\gravity2$\graphic\bg\documents\発注書\BGアセット',TARGET_NAME)
