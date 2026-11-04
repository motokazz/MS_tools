# _*_coding:utf-8_*_
########################################
# �t�@�C����
#			MS_execCheck.py
# ����
#			�N���m�F���X�g�쐬
#�g�p���@
#���L�R�}���h���e�X�N���v�g�̐擪�ɋL�q
'''
#execCheckList
import MS_module.MS_execCheck
reload(MS_module.MS_execCheck)
MS_module.MS_execCheck.execCheckSafe('SCRIPT_NAME')

'''
#			
########################################

import os

import datetime

def SAVE(ROW,FILE_PATH):
	f=open(FILE_PATH,'w')#'r'�ǂݍ��݁F'w'�������݁F'a'�ǋL�F'+'�ǂݏ�������' 't'�e�L�X�g���[�h�F'b'�o�C�i���[���[�h
	f.write(ROW)
	f.close()
	return True
	
##### �t�@�C�����[�h #####
def LOAD(FILE_PATH):
	DATA=[]
	if not os.path.exists(FILE_PATH):
		return DATA#��̃��X�g��Ԃ�
	try:
		f=open(FILE_PATH)
		for ROW in f:
			DATA.append(ROW)
		f.close()
		return DATA
	except:
		return DATA


def execCheckSafe(SCRIPT_NAME,EXPORT_DIR='//fs03/js-sd/M_PROJECT/users/msakai/scriptCheckList'):
	#�G���[�Ŏ~�܂�Ȃ��Z�[�t���[�h�B
	return
	try:
		execCheckList(SCRIPT_NAME)
	except:
		print ('warnning:MS_execCheck error')

def execCheckList(SCRIPT_NAME,EXPORT_DIR='//fs03/js-sd/M_PROJECT/users/msakai/scriptCheckList'):
	#����N���m�F
	FIRSTCHECK=True
	
	#�t�@�C����
	FILENAME='checkList_'+SCRIPT_NAME+'.csv'
	FILEPATH=EXPORT_DIR+'/'+FILENAME
	
	#���[�U�[���擾
	USERNAME=os.environ.get('USERNAME')
	#�N������
	TIME=str(datetime.datetime.now())
	REPLACELIST=[[' ','_'],['-','/']]
	for EACH in REPLACELIST:
		TIME=TIME.replace(EACH[0],EACH[1])
	#�N���񐔏����ݒ�
	QUANTITY=''
	#
	if os.path.isdir(EXPORT_DIR):
		NEWDATA=''
		NEWDATA2=[]
		DATA=LOAD(FILEPATH)
		for EACHDATA in DATA:
			DATA2=EACHDATA.replace('/n','').split(',')
			#print (DATA2)
			if DATA2[0]=='':
				continue
			if USERNAME in DATA2[0]:
				#�N����
				#print (DATA2[2])
				try:
					PREQ=int(DATA2[2])+1
				except:
					PREQ=1
				QUANTITY=str(PREQ)
				FIRSTCHECK=False
				NEWDATA+=DATA2[0]+','+TIME+','+QUANTITY+',\n'
			else:
				NEWDATA+=EACHDATA
			
		if FIRSTCHECK:
			NEWDATA2=[USERNAME,TIME,'1']
			NEWDATA+=(','.join(NEWDATA2)+'\n')
		
		SAVE(NEWDATA,FILEPATH)
		
		
	else:
		#print ('not found directry = '+EXPORT_DIR)
		return False
		
		
	
