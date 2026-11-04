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
	return ['BBX','BBY','BBZ','BBTOTAL']

def main(DATA):
	TEMP=[]
	LEVEL=-1
	TRNLIST=[]
	SIZES=[]#頂点ごとの倍率？
	
	X=[]
	Y=[]
	Z=[]

	try:

		for EACHDATA in DATA:

			if u'<node' in EACHDATA:
				LEVEL+=1
				TRNLIST.append([0,0,0,1,1,1])

			if u'</node' in EACHDATA:
				TRNLIST.pop(LEVEL)
				LEVEL-=1

			if u'<translate>' in EACHDATA:
				TEMPTRN=EACHDATA.replace(u'<',u';').replace(u'>',u';').split(u';')[2].split(' ')
				TRNLIST[LEVEL][0]=float(TEMPTRN[0])
				TRNLIST[LEVEL][1]=float(TEMPTRN[1])
				TRNLIST[LEVEL][2]=float(TEMPTRN[2])

			if u'<scale>' in EACHDATA:
				TEMPSCL=EACHDATA.replace(u'<',u';').replace(u'>',u';').split(u';')[2].split(' ')
				TRNLIST[LEVEL][3]=float(TEMPSCL[0])
				TRNLIST[LEVEL][4]=float(TEMPSCL[1])
				TRNLIST[LEVEL][5]=float(TEMPSCL[2])

			
			if u'<sizes>' in EACHDATA: #頂点ごとの倍率？
				SIZES=EACHDATA.replace(u'<',u';').replace(u'>',u';').split(u';')[2].split(' ')

			if u'<array name="position"' in EACHDATA:
				ARRAY = EACHDATA.replace(u'<',u';').replace(u'>',u';').split(u';')[2].split(' ')
				#
				TX,TY,TZ=0,0,0
				SX,SY,SZ=1,1,1

				for eachtrn in TRNLIST:
					TX+=eachtrn[0]
					TY+=eachtrn[1]
					TZ+=eachtrn[2]
					SX*=eachtrn[3]
					SX*=eachtrn[4]
					SX*=eachtrn[5]
				
				i=0
				for each in zip(*[iter(ARRAY)]*3):
					try:
						SIZE=float(SIZES[i])
					except:
						continue
					X.append((float(each[0])+TX)*SX*SIZE)
					Y.append((float(each[1])+TY)*SY*SIZE)
					Z.append((float(each[2])+TZ)*SZ*SIZE)
					i+=1
				
		if not X:X=[0,1]
		if not Y:Y=[0,1]
		if not Z:Z=[0,1]

		TOTAL=abs(max(X)-min(X))*(max(Y)-min(Y))*(max(Z)-min(Z))

		return [ str(abs(max(X)-min(X))) , str(abs(max(Y)-min(Y))) , str(abs(max(Z)-min(Z))) , str( math.pow(TOTAL,1.0/3) ) ]

	except:
		return ['0','0','0']
	
