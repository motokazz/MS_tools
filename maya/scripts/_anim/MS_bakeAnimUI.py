# -*- coding: utf-8 -*-

import maya.cmds as cmds
import maya.mel as mel

#
def MS_bakeAnim_selectTime():
	'''
	タイムスライダーから時間を取得
	
	スライダーで範囲選択がある場合はその範囲内を
	そうでない場合は現在のタイムスライダーの範囲を返す
	
	'''
	#グローバル宣言しないとプロシージャ内でタイムスライダーを特定できない。
	gPlayBackSlider=mel.eval( '$tmpVar=$gPlayBackSlider' )
	BUF=[]
	
	TC=cmds.timeControl(gPlayBackSlider,q=True,rng=True ,gt=True);
	
	BUF=TC.strip('"').split(':')
	ST=float(BUF[0])
	ED=float(BUF[1])
	if (ED-ST)<=1:
		ST=cmds.playbackOptions(q=True,min=True)
		ED=cmds.playbackOptions(q=True,max=True)
	return [ST,ED];

#
print MS_bakeAnim_selectTime()
#
def MS_bakeAnim_globalScale(SOURCE):
	print (SOURCE+"\n")
	ATTR=["sx","sy","sz"]
	OBJ=cmds.ls(SOURCE, l=True)
	RET=[]
	LIST=OBJ.split('|')
	for EACHATTR in ATTR:
		VAL=1.0
		LONGNAME=""#フルパス作成のため
		for EACH in LIST:
			LONGNAME=LONGNAME+"|"+EACH
			print (longName+"."+EACHATTR+"\n")
			VAL=VAL*cmds.getAttr(LONGNAME+"."+EACHATTR)
		RET.append(VAL)
	return RET

#
def MS_bakeSimulation():
	TM=MS_bakeAnim_selectTime()
	objs=cmds.ls(sl=True)
	
	VALIES=cmds.channelBox(mainChannelBox,q=True,sma=True)
	VALIES2=cmds.channelBox (mainChannelBox,q=True,ssa=True)
	
	OPTION="bakeResults "
	
	for EACH in VALIES:
		OPTION=OPTION+"-at \""+EACH+"\" "
	for EACH in VALIES2:
		OPTION=OPTION+"-at \""+EACH+"\" "
	
	OPTION =OPTION+"-sm 1 "
	OPTION =OPTION+"-t \""+TM[0]+":"+TM[1]+"\" "
	OPTION =OPTION+"-sb 1 -dic 1 "
	OPTION =OPTION+"-pok 1 -sac 0 "
	OPTION =OPTION+"-cp 0 -s 1 "
	OPTION =OPTION+objs.join(" ")+";"
	print OPTION
	mel.eval (OPTION)
	
#
def MS_copyAnim(SOURCE,DIST):
	SOURCEARRAY=SOURCE.split('<>')
	DISTARRAY=DIST.split('<>')
	
	if len(SOURCEARRAY)!=len(DISTARRAY):
		cmds.confirmDialog(t="Error!",m="source to dist no kazuga chigauyo!\nonasi kazuno object wo erandene.",b=Continue)
	else:
		i=0
		for EACH in SOURCEARRAY:
			if cmds.copyKey(EACH,t=":",f=":",at="tx"):
				cmds.pasteKey(DISTARRAY[i],connect=True,time=0,at="tx")
			if cmds.copyKey(EACH,t=":",f=":",at="ty"):
				cmds.pasteKey(DISTARRAY[i],connect=True,time=0,at="ty")
			if cmds.copyKey(EACH,t=":",f=":",at="tz"):
				cmds.pasteKey(DISTARRAY[i],connect=True,time=0,at="tz")
			
			if mds.copyKey(EACH,t=":",f=":",at="rx"):
				cmds.pasteKey(DISTARRAY[i],connect=True,time=0,at="rx")
			if mds.copyKey(EACH,t=":",f=":",at="ry"):
				cmds.pasteKey(DISTARRAY[i],connect=True,time=0,at="ry")
			if mds.copyKey(EACH,t=":",f=":",at="rz"):
				cmds.pasteKey(DISTARRAY[i],connect=True,time=0,at="rz")
			
			if mds.copyKey(EACH,t=":",f=":",at="sx"):
				cmds.pasteKey(DISTARRAY[i],connect=True,time=0,at="sx")
			if mds.copyKey(EACH,t=":",f=":",at="sy"):
				cmds.pasteKey(DISTARRAY[i],connect=True,time=0,at="sy")
			if mds.copyKey(EACH,t=":",f=":",at="sz"):
				cmds.pasteKey(DISTARRAY[i],connect=True,time=0,at="sz")
			i+=1

#
def MS_copyAnim_pipe():
	temp=cmds.textFieldGrp(SourceName,q=True,tx=True)
	tempb=cmds.textFieldGrp(DistName,q=True,tx=True)
	MS_copyAnim(temp,tempb)


#
def MS_bakeAnim_createDummy(strtm,endtm,source):
	option
	values=cmds.channelBox(mainChannelBox,q=True,sma=True)
	values2=cmds.channelBox(mainChannelBox,q=True,ssa=True)
	attr=values+values2
	if len(attr):
		for each in attr:
			option=option+("-at "+each+" ")
	else:
		option="-at tx -at ty -at tz -at rx -at ry -at rz -at sx -at sy -at sz "
	
	sourceArray=source.split('<>')
	dummyLoc=[]
	for dummy in sourceArray:
		temp=cmds.spaceLocator()
		dummyLoc.append(temp[0])
	#core
	for i in range(strtm,endtm):
		cmds.currentTime(i)
		j=0
		for each in sourceArray:
			expVertex=cmds.filterExpand(each,sm=31)
			if len(expVertex):
				loc=cmds.xform (each,q=True,ws=True,t=True)
				cmds.xform(dummyLoc[j],ws=True, t=(loc[0],loc[1],loc[2]))
				#cmds.setKeyframe(dummyLoc[j],at=True,tx=True,at=("ty","tz"))
			else:
				shape=cmds.listRelatives(each,typ=shape)
				loc=cmds.xform(each,q=True,ws=True,piv=True)
				rot=cmds.xform(each,q=True,ws=True,ro=True)
				scl=MS_bakeAnim_globalScale(each)
				cmds.xform(dummyLoc[j],ws=True, t=(loc[0],loc[1],loc[2]))
				cmds.xform(dummyLoc[j],ws=True,ro=(rot[0],rot[1],rot[2]))
				cmds.xform(dummyLoc[j],ws=True,s=(scl[0],scl[1],scl[2]))
				
				mel.eval("setKeyframe "+option+dummyLoc[j])
				#setKeyframe -at tx -at ty -at tz -at rx -at ry -at rz -at sx -at sy -at sz dummyLoc[j];
			j+=1
	i=0
	for eachdummy in dummyLoc:
		#rename eachdummy "MS_bakeAnim_createDummy1";
		temp=sourceArray[i]
		nameOptimized=temp.split('|:')
		cmds.rename(eachdummy, ("Dummy_"+nameOptimized[len(nameOptimized)-1]))
		i+=1

def MS_bakeAnim_pipe():
	TM=MS_bakeAnim_selectTime()
	source = cmds.textFieldGrp('SourceName',q=True,tx=True)
	dist = cmds.textFieldGrp('DistName',q=True,tx=True)
	sourceArray = source.split('<>')
	distArray = dist.split('<>')
	string $distArray[]=stringToStringArray($dist,"<>");	
	MS_bakeAnim $tm[0] $tm[1] $sourceArray $distArray;
	
}

#
def MS_bakeAnim_createDummy_pipe():
	tm=MS_bakeAnim_selectTime()
	temp=cmds.textFieldGrp('SourceName',q=True,tx=True)
	MS_bakeAnim_createDummy(tm[0],tm[1],temp)
#
def MS_bakeAnim_takeSource():
	obj=cmds.filterExpand(sm=31)
	if not obj:
		obj=cmds.ls(l=True,sl=True)
	lst='<>'.join(obj)
	cmds.textFieldGrp('MS_bakeAnimUISourceName',e=True,tx=lst)
#
def MS_bakeAnim_takeDist():
	obj=cmds.filterExpand(sm=31)
	if not obj:
		obj=cmds.ls(l=True,sl=True)
	lst='<>'.join(obj)
	cmds.textFieldGrp('MS_bakeAnimUIDistName',e=True,tx=lst)
#


def UI():
	if cmds.window('MS_bakeAnimUI',ex=True):
		cmds.deleteUI('MS_bakeAnimUI',window=True)
	window = cmds.window(' MS_bakeAnimUI',title="MS_bakeAnim", iconName='Short Name', widthHeight=(200, 55) )
	cmds.columnLayout()
	cmds.frameLayout (w=200,cll=1,cl=1,l="help")
	cmds.columnLayout()
	cmds.text(rs=1 ,l="1:select SourceObj and \n press [takeSource]button.")
	cmds.text(l="2:select DistObj and \n press [takeDist]button.")
	cmds.text(l="3:select Attribute from \n channelBox.")
	cmds.text(l="   if select nothing when \n bake attribute to [trans][rot][scal].")
	cmds.text(l="4:go.")
	cmds.setParent ('..')
	cmds.setParent ('..')
	cmds.textFieldGrp('MS_bakeAnimUISourceName',en=1,w=200 )
	cmds.button(bgc=[0.8,0.8,1.0],w=100,l="take Source",c=lambda *args:MS_bakeAnim_takeSource())
	
	cmds.textFieldGrp('MS_bakeAnimUIDistName',en=1,w=200)
	
	cmds.button (bgc=(0.8,1.0,0.8),w=100,l="take Dist",c=lambda *args:MS_bakeAnim_takeDist())
	
	cmds.separator(w=1000,h=20)
	
	cmds.button(bgc=[1.0,0.8,0.8],w=100,l="MS_bakeAnim",c=lambda *args:MS_bakeAnim_pipe())
	
	cmds.separator(w=1000,h=20)
	
	cmds.button (bgc=[1.0,0.8,1.0], w=100,l="MS_bakeSimulation",c=lambda *args:MS_bakeSimulation())
	
	cmds.separator(w=1000,h=20)
	
	cmds.button (bgc=[1.0,1.0,0.8],w=100,l="createDummy",c=lambda *args:MS_bakeAnim_createDummy_pipe())
	cmds.separator(w=1000,h=20)
	cmds.button(bgc=[0.8,1.0,1.0],w=100,l="copyAnim",c=lambda *args:MS_copyAnim_pipe())
	cmds.setParent ('..')
	cmds.showWindow (window);
	


