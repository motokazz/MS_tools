import sys
import os
import fileinput
import csv
import re

files = sys.argv[1:]
cDir = os.path.split(sys.argv[0])[0]

#sys.stdout.write(cDir)

dictCsv = open(cDir + '\\replace_dict.csv', 'rb')
reader = csv.reader(dictCsv)

old_word = []
new_word = []

for row in reader:
	if row[0] == '':
		old_word += [row[1]]
		new_word += [row[2]] 

dictCsv.close()
i = 1
for line in fileinput.input(inplace=1 ,backup='.bkup'):
	for oneOldWord, oneNewWord in zip(old_word, new_word):
		if r'"' + oneOldWord + r'"' in line and not oneNewWord:
			origOut = sys.stdout
			sys.stdout = sys.__stdout__  			
			print u'削除されたモーションが使用されています >>', str(fileinput.filename()).split('\\')[-1], 'L:' + str(i),oneOldWord
			sys.stdout = origOut
			continue

		line = line.replace(oneOldWord, oneNewWord)
	sys.stdout.write(line)
	i += 1

fileinput.close()
