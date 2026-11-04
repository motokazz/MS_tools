# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_pickle.py
# 説明
#			pickeのモジュール
#			
# 作成日
#			
########################################
import os
import pickle

def save(path,data):#path にセーブデータのフルパス、data　保存したい変数やクラス
	with open(path,'wb') as f:
		pickle.dump(data,f)

def load(path):#path にデータのフルパス、戻り値は保存されてる変数の内容そのまま。
	with open(path,'rb') as f:
		ret = pickle.load(f)
	return ret


