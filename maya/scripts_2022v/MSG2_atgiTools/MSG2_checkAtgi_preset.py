# _*_coding:utf-8_*_
########################################
# ファイル名
#			MSG2_checkAtgi_preset.py
# 説明
#			
#			
# 作成日
#			
########################################

PRESETS=['unknown','rock','soil','metal','wood','cloth','grass','vinyl']

def index():
	return PRESETS

def main(DATA):
	TEMP=[]
	for EACHPRESET in PRESETS:
		try:
			CATCH=0
			for EACHDATA in DATA:
				if u'<attribute name="exportable_preset" type="string">'+EACHPRESET+'</attribute>' in EACHDATA:
					CATCH+=1
			TEMP.append(str(CATCH))
		except:
			TEMP.append('e')

	return TEMP
	

