# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_convValueToString.py
# 説明
#			型を見て値をストリング化するユーティリティ
#			
# 作成日
#			
########################################
	
def convValueToString(VAR):
	if isinstance(VAR,int):
		VAR_STR=str(int(VAR))+'.0'
	if isinstance(VAR,float):
		VAR_STR=str(VAR)
	if isinstance(VAR,list):
		VAR_STR=str(VAR[0][0])+','+str(VAR[0][1])+','+str(VAR[0][2])
	return VAR_STR
