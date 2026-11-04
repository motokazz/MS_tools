# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_projectDir
# 説明
#
#
# 作成日
#
########################################

import maya.cmds as cmds
import os
import csv

# 設定CSVのパス
path_list_file = os.path.dirname(__file__).replace('\\', '/') + '/MS_projectDir.csv'
setting_file = os.path.dirname(__file__).replace('\\', '/') + '/MS_projectDir_settings.csv'

# ツール設定初期化
CURRENT_PROJECT = ''

# パスリスト初期化
PATH_THUMBNAIL = 'd:/'
PATH_MAYA = 'd:/'
PATH_A = 'd:/'
PATH_B = 'd:/'
PATH_C = 'd:/'

###################
# import path list
###################
# パスリストをインポートする
DICT_PATH = {}
with open(path_list_file, 'r') as f:
	reader = csv.reader(f)
	header = next(reader)
	i = 0
	for each in header:
		if each == 'name': key = i
		if each == 'thumbnail': thumbnail = i
		if each == 'maya': path_maya = i
		if each == 'path_a': path_a = i
		if each == 'path_b': path_b = i
		if each == 'path_c': path_c = i
		i += 1
	for each in reader:
		DICT_PATH.setdefault(each[key], [each[thumbnail].replace('\\','/'), each[path_maya].replace('\\','/'), each[path_a].replace('\\','/'), each[path_b].replace('\\','/'), each[path_c].replace('\\','/')])


# パスリストを基に、パスを設置
def change_PATH(KEY='bg'):
	global PATH_THUMBNAIL
	global PATH_MAYA
	global PATH_A
	global PATH_B
	global PATH_C

	PATH_THUMBNAIL = DICT_PATH[KEY][0]
	PATH_MAYA = DICT_PATH[KEY][1]
	PATH_A = DICT_PATH[KEY][2]
	PATH_B = DICT_PATH[KEY][3]
	PATH_B = DICT_PATH[KEY][4]


###########
# Settings
###########

def loadSetting():
	global CURRENT_PROJECT
	if os.path.exists(setting_file):
		with open(setting_file, 'r') as f:
			reader = csv.reader(f)
			for each in reader:
				try:
					if each[0] == 'current_project':
						CURRENT_PROJECT = each[1]
						change_PATH(CURRENT_PROJECT)
				except:
					pass

def saveSetting():
	with open(setting_file, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(['current_project',CURRENT_PROJECT])

####
# UI
####
def store(item):
	global CURRENT_PROJECT
	CURRENT_PROJECT=item
	saveSetting()
	change_PATH(item)

def recall():
	cmds.optionMenu('MS_projectDir_projects',v= CURRENT_PROJECT,e=True)


def layout():

	cmds.gridLayout(nc=3,cw=100)
	cmds.text(l='Projects')
	cmds.optionMenu('MS_projectDir_projects', changeCommand=store)
	for each in DICT_PATH.keys():
		cmds.menuItem(label=each)
	cmds.button(l='openSetup', c=lambda *args: os.popen('explorer "%s"' % path_list_file.replace('/', '\\')))
	cmds.setParent('..')
	recall()


#起動時にSettingをロード
loadSetting()

