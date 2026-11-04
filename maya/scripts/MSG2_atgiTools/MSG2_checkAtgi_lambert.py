# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_checkAtgi_lambert.py
# 説明
#			
#			
# 作成日
#			
########################################


PRESETS=['lambert count']

def index():
	return PRESETS

def main(DATA):
	TEMP=[]
	for EACHPRESET in PRESETS:
		try:
			CATCH=0
			for EACHDATA in DATA:
				if u'<attribute name="type" type="string">lambert</attribute>' in EACHDATA:
					CATCH+=1
			TEMP.append(str(CATCH))
		except:
			TEMP.append('e')

	return TEMP
	

