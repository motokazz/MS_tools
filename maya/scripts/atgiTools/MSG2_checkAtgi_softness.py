# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_checkAtgi_BB.py
# 説明
#			
#			
# 作成日
#			
########################################
import math

def index():
	return ['softness']

def main(DATA):
	SOFTNESS=0
	try:

		for EACHDATA in DATA:
			if u'<binding source="softness" />' in EACHDATA:
				SOFTNESS+=1

		return [str(SOFTNESS)]

	except:
		return ['err']
	
