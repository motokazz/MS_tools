# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_tools_init.py
# 説明
#			
#			
# 作成日
#			
########################################

import MS_toolsPath
reload(MS_toolsPath)

path 		= MS_toolsPath.MS_toolsPath()

#MSToolsMAYAのメインパス
maintools_path= path.parentPath

#pythonスクリプト設置パス
python_path	= path.parentPath

#melスクリプト設置パス
mel_path	= path.parentPath

#ツール定義用のCSVのパス
init_path	= path.currentPath+'ini/'

#pickle保存パス
pickle_path	= path.currentPath

#ツールアイコンのパス
icon_path	= path.parentPath

#デフォルトアイコンのパス
deficon_path	= path.currentPath+'deficons/'

#exec_check　ログ出力パス
exec_check_path	= path.parentPath+'_log/'


#UIを記録するか
store_recall_enabled = True

#userSetup.pyにMStoolsのパスを記述して使っているか
use_userSetup_py = False

#exec_checkするか
exec_check_enabled = True

