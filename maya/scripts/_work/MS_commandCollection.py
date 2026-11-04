# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_commandCollection
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds

help_line=[]		#ヘルプコマンドで返ってきた内容をストック
main_command=''	#検索対象のメインコマンド名をストック
command_line=''	#メインコマンド実行時のコマンド

ui_script=''		#UI作成時のスクリプト


def searchCommands(searchWord='*'):
	searchWord=cmds.textField('MS_commandCollection_searchWord',q=True,tx=True)

	if searchWord=='':
		return

	search_results = cmds.help(searchWord+'*',language='python',list=True)

	if not search_results:
		return

	cmds.textScrollList('MS_commandCollection_searchWordResult'
		,e=True
		,ra=True
		,append=search_results
		,dkc=openHelpDoc
		,dcc=commandWindow
		)


#################
# ヘルプドキュメントを開く
#################

def openHelpDoc():
	word = cmds.textScrollList('MS_commandCollection_searchWordResult',q=True,si=True)
	cmds.help(word,doc=True)

#################
# コマンド作成
#################
def analizeCommandFromHelp(word=''):
	global help_line
	word = cmds.textScrollList('MS_commandCollection_searchWordResult',q=True,si=True)

	pre_help_line = cmds.help(word,language='python').replace('-','').split('\n')

	help_line=[]
	for each in pre_help_line:
		help_line.append(each.split())



def createOptions(*args):

	a=args[0]

	##
	if 'Synopsis' in a[0]:
		cmds.text(l=','.join(a))
		return 'cmds.text(l="'+','.join(a)+'")\n'

	if 'Flags' in a[0] or 'Flags' in a[0] :
		return '\n'

	if len(a)<2:
		cmds.text(l='u2  :  '+a[0])
		return 'cmds.text(l="u2  :  '+a[0]+'")\n'

	##
	attribute_name = a[1].strip()

	control_name='MS_commandCollection_Command_'+attribute_name

	if len(a)==2:
		cmds.checkBoxGrp(control_name,l='[q]'+attribute_name)
		return 'cmds.checkBoxGrp("'+control_name+'",l="'+attribute_name+'")\n'

	if len(a)==3:
		#bool
		if a[2]=='on|off':
			cmds.checkBoxGrp(control_name,l=attribute_name)
			return 'cmds.checkBoxGrp("'+control_name+'",l="'+attribute_name+'")\n'

		elif a[2]=='Int':
			cmds.intSliderGrp(control_name,l=attribute_name,f=True)
			return 'cmds.intSliderGrp("'+control_name+'",l="'+attribute_name+'",f=True)\n'

		elif a[2]=='UnsignedInt':
			cmds.intSliderGrp(control_name,l=attribute_name,f=True)
			return 'cmds.intSliderGrp("'+control_name+'",l="'+attribute_name+'",f=True)\n'

		elif a[2]=='Float':
			cmds.floatSliderGrp(control_name,l=attribute_name,f=True)
			return 'cmds.floatSliderGrp("'+control_name+'",l="'+attribute_name+'",f=True)\n'
		
		elif a[2]=='Angle':
			cmds.floatSliderGrp(control_name,l=attribute_name,f=True)
			return 'cmds.floatSliderGrp("'+control_name+'",l="'+attribute_name+'",f=True)\n'

		elif a[2]=='Length':
			cmds.floatSliderGrp(control_name,l=attribute_name,f=True)
			return 'cmds.floatSliderGrp("'+control_name+'",l="'+attribute_name+'",f=True)\n'

		elif a[2]=='String':
			cmds.textFieldGrp(control_name,l=attribute_name)
			return 'cmds.textFieldGrp("'+control_name+'",l="'+attribute_name+'")\n'
		else:
			cmds.text(l=','.join(a))
			return 'cmds.text(l="'+','.join(a)+'")\n'

	if 3<len(a)<6:
		cmds.rowLayout(nc=len(a))
		cmds.text(l=attribute_name,w=200)
		i=0
		for each in a[2:]:
			if each=='Int':
				cmds.intField(control_name+str(i))
			if each=='Float':
				cmds.floatField(control_name+str(i))
			if each=='Angle':
				cmds.floatField(control_name+str(i))
			if each=='Length':
				cmds.floatField(control_name+str(i))
			if each=='String':
				cmds.floatField(control_name+str(i))

			i+=1

		cmds.setParent('..')

	#cmds.setParent('..')

	return '\n'

def createCommand(ex=True,q=True):
	global command_line
	command_line=''
	command_line+='import maya.cmds as cmds\n'


	#command_line+='print '
	command_line+='cmds.'+main_command+'('

	### target ###



	### option ###
	option=[]
	for each in help_line:
		for a in each:
			if a=='String...':
				option.append('"'+cmds.ls(sl=True,l=True)[0]+'"')
			if a=='[String...]':
				option.append('["'+'","'.join(cmds.ls(sl=True,l=True))+'"]')


		if len(each)<2:
			continue

		control_name='MS_commandCollection_Command_'+each[1]

		if cmds.checkBoxGrp(control_name,q=True,ex=True):
			if cmds.checkBoxGrp(control_name,q=True,v1=True):
				option.append(each[1]+' = True ')
			else:
				option.append(each[1]+' = False ')

		if cmds.floatSliderGrp(control_name,q=True,ex=True):
			var = cmds.floatSliderGrp(control_name,q=True,v=True)
			option.append(each[1]+' = '+str(var))

		if cmds.intSliderGrp(control_name,q=True,ex=True):
			var = cmds.intSliderGrp(control_name,q=True,v=True)
			option.append(each[1]+' = '+str(var))


	command_line+='\n,'.join(option)



	command_line+='\n)'

	if q==True:
		print command_line
	if ex==True:
		exec(command_line)

def layoutCommand():
	
	global ui_script
	ui_script=''

	analizeCommandFromHelp()
	for a in help_line:
		if a:
			ui_script+=createOptions(a)

	print ui_script



#################
# UI
#################


def commandWindow():
	global main_command

	if cmds.window('MS_commandCollection_Command_window',q=True,ex=True):
		cmds.deleteUI('MS_commandCollection_Command_window')
	cmds.window('MS_commandCollection_Command_window',rtf=True,s=True)

	main_command = cmds.textScrollList('MS_commandCollection_searchWordResult',q=True,si=True)[0]

	cmds.scrollLayout('MS_commandCollection_Command_colmnLayout')
	cmds.columnLayout('MS_commandCollection_Command_colmnLayout',adj=True)

	cmds.rowLayout(nc=2)
	cmds.button(w=300,l = main_command ,c=lambda *args:createCommand(ex=True))
	cmds.button(w=100,l = 'command test' ,c=lambda *args:createCommand(ex=False,q=True))
	cmds.setParent('..')

	layoutCommand()

	cmds.setParent('..')
	cmds.setParent('..')
	cmds.showWindow('MS_commandCollection_Command_window')

def LayoutA():
	cmds.frameLayout('MS_commandCollection_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_commandCollection',cll=True,cl=False)
	cmds.columnLayout('MS_commandCollection_mainLayout',adj=True)

	cmds.separator()
	
	cmds.text(l='MS_commandCollection',bgc=[0.9,0.9,0.9],fn='boldLabelFont')

	cmds.textField('MS_commandCollection_searchWord',cc=lambda *args:searchCommands())

	cmds.separator()

	cmds.textScrollList('MS_commandCollection_searchWordResult')
	cmds.text(l=u'del or Backspace : webhelpを開く')

	cmds.setParent('..')
	cmds.setParent('..')


def UI():


	if cmds.window('MS_commandCollection_window',q=True,ex=True):
		cmds.deleteUI('MS_commandCollection_window')
	cmds.window('MS_commandCollection_window',rtf=True,s=True)
	
	LayoutA()

	cmds.showWindow('MS_commandCollection_window')
	