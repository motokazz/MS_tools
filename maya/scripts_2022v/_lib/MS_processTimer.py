# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_processTimer
# 説明
#			処理時間を計測するモジュール
#			
# 作成日
#			
########################################
import time

class timer:
	def __init__(self):
		self.startTime = 0
		self.period = []
		self.finishTime = 0
		self.result = 0

	def start(self):
		self.startTime = time.clock()

	def period(self,name=''):
		self.finishTime = time.clock()
		temp = self.startTime - self.finishTime
		self.period.append([name,temp])

	def finish(self):
		self.finishTime = time.clock()
		self.result = self.finishTime - self.startTime
		for each in self.period:
			print each
		print u'処理時間は' + str(self.result) + u'秒でした'





