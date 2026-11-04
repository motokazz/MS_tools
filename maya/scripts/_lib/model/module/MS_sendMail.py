# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_sendMail
# 説明
#			
# 作成日\n#			
########################################

import maya.cmds as cmds
import smtplib
from email.MIMEText import MIMEText
from email.Utils import formatdate

def create_message(from_addr, to_addr, subject, body):
	msg = MIMEText(body)
	msg['Subject'] = subject
	msg['From'] = from_addr
	msg['To'] = to_addr
	msg['Date'] = formatdate()
	return msg

def send(from_addr, to_addr, msg):
	# SMTPの引数を省略した場合はlocalhost:25
	connect()
	s = smtplib.SMTP()
	s.sendmail(from_addr, [to_addr], msg.as_string())
	s.close()


def do():
	from_addr = 'spam@example.com'
	to_addr = 'Motokazu_Sakai@hq.scei.sony.co.jp'
	msg = create_message(from_addr, to_addr, 'test subject', 'test body')
	send(from_addr, to_addr, msg)

def layoutA(
	LABEL='MS_sendMail'
	,WIDTH=217
	,BGC=[0.2,0.2,0.2]
	,CL=False
	):
	cmds.frameLayout(LABEL+'_frameLayout',w=WIDTH,bgc=BGC,fn='boldLabelFont',l=LABEL,cll=True,cl=CL)
	cmds.columnLayout()
	
	cmds.text(l=LABEL)
	cmds.textField(LABEL+'_textField_a',w=WIDTH-4,tx='')
	cmds.intField(LABEL+'_floatField_a',w=WIDTH-4,v=0)
	cmds.button(w=WIDTH-4,l=u'do',c=lambda *args:do())
	
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_sendMail_main_window',q=True,ex=True):
		cmds.deleteUI('MS_sendMail_main_window')
	cmds.window('MS_sendMail_main_window',rtf=True,s=True)
	
	layoutA()
	
	cmds.showWindow('MS_sendMail_main_window')
	

