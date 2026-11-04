# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_createThumbnail
# 説明
#
#
# 作成日
#
########################################

import maya.cmds as cmds
import importlib

from . import MS_projectDir as MS_projectDir
importlib.reload(MS_projectDir)

da=ca=cv=df=dim=dc=dtx=fl=fo=gr=hs=ha=hud=hu=ikh=imp=j=lt=lc=m=mt=ncl=npa=nr=nc=ns=pv=pl=po=ps=pm=sdw=swf=strx=sds=tx=tsl=ui=vs = 0

def createThumbneil(EX_PATH, IMAGE_NAME, SWATCH_MODE='SUMBNAIL', RENDER='playblast', X=64, Y=64):
	# 選択状況取得＆選択をクリア
	SEL = cmds.ls(sl=True)
	cmds.select(cl=True)

	# パス作成
	EX_PATH = EX_PATH.replace('\\', '/')
	playblastPath = EX_PATH + '/' + IMAGE_NAME + '.jpg'

	#camera
	Current_camera_filmfit = cmds.getAttr('perspShape.filmFit')
	cmds.setAttr('perspShape.filmFit' , 2)

	cmds.setAttr("defaultRenderGlobals.imageFormat", 8)
	cmds.currentTime(q=True)
	if RENDER == 'playblast':

		# パネル表示物設定Store
		panelName = cmds.getPanel(wf=True)
		if cmds.modelPanel(panelName,q=True,ex=True):
			StorePanel(panelName)
			#cmds.modelEditor(panelName, e=True, alo=False)
			ClearPanel(panelName)
			cmds.modelEditor(panelName, e=True, pm=True)
			cmds.modelEditor(panelName, e=True, da='smoothShaded')
			cmds.modelEditor(panelName, e=True, dtx=True)


		# PlayBlastで作る



		RENDER_NAME = cmds.playblast(
			cf=playblastPath
			, fr=cmds.currentTime(q=True)
			, fo=True
			, fp=4
			, w=X
			, h=Y
			, clearCache=True
			, offScreen=True
			, format='image'
			, percent=50
			, viewer=False
			, showOrnaments=False
		)

		# パネル表示物設定Recall
		if cmds.modelPanel(panelName,q=True,ex=True):
			RecallPanel(panelName)

	else:
		# MayaRendererで作る
		RENDER_NAME = cmds.render(x=X, y=Y)

		RENDER_NAME = RENDER_NAME.replace('#', '0')
		if SWATCH_MODE == 'SWATCH':
			shutil.copyfile(RENDER_NAME, (EX_PATH + '.mayaSwatches/' + IMAGE_NAME + '.swatch'))

		if SWATCH_MODE == 'SUMBNAIL':
			shutil.move(RENDER_NAME, (EX_PATH + '/' + IMAGE_NAME + '.jpg'))

	# 選択状況復活
	cmds.setAttr('perspShape.filmFit', Current_camera_filmfit)
	cmds.select(SEL, r=True)

def StorePanel(panelName=""):
	global da,ca,cv,df,dim,dc,dtx,fl,fo,gr,hs,ha,hud,hu,ikh,imp,j,lt,lc,m,mt,ncl,npa,nr,nc,ns,pv,pl,po,ps,pm,sdw,swf,strx,sds,tx,tsl,ui,vs
	da = cmds.modelEditor(panelName, q=True, da=True)
	ca = cmds.modelEditor(panelName,q=True,ca=True)
	cv = cmds.modelEditor(panelName,q=True,cv=True)
	df = cmds.modelEditor(panelName,q=True,df=True)
	dim = cmds.modelEditor(panelName,q=True,dim=True)
	dc = cmds.modelEditor(panelName,q=True,dc=True)
	dtx = cmds.modelEditor(panelName,q=True,dtx=True)
	fl = cmds.modelEditor(panelName,q=True,fl=True)
	fo = cmds.modelEditor(panelName,q=True,fo=True)
	gr = cmds.modelEditor(panelName,q=True,gr=True)
	hs = cmds.modelEditor(panelName,q=True,hs=True)
	ha = cmds.modelEditor(panelName,q=True,ha=True)
	hud = cmds.modelEditor(panelName,q=True,hud=True)
	hu = cmds.modelEditor(panelName,q=True,hu=True)
	ikh = cmds.modelEditor(panelName,q=True,ikh=True)
	imp = cmds.modelEditor(panelName,q=True,imp=True)
	j = cmds.modelEditor(panelName,q=True,j=True)
	lt = cmds.modelEditor(panelName,q=True,lt=True)
	lc = cmds.modelEditor(panelName,q=True,lc=True)
	m = cmds.modelEditor(panelName,q=True,m=True)
	mt = cmds.modelEditor(panelName,q=True,mt=True)
	ncl = cmds.modelEditor(panelName,q=True,ncl=True)
	npa = cmds.modelEditor(panelName,q=True,npa=True)
	nr = cmds.modelEditor(panelName,q=True,nr=True)
	nc = cmds.modelEditor(panelName,q=True,nc=True)
	ns = cmds.modelEditor(panelName,q=True,ns=True)
	pv = cmds.modelEditor(panelName,q=True,pv=True)
	pl = cmds.modelEditor(panelName,q=True,pl=True)
	#po = cmds.modelEditor(panelName,q=True,po=True)
	#ps = cmds.modelEditor(panelName,q=True,ps=True)
	pm = cmds.modelEditor(panelName,q=True,pm=True)
	sdw = cmds.modelEditor(panelName,q=True,sdw=True)
	swf = cmds.modelEditor(panelName,q=True,swf=True)
	strx = cmds.modelEditor(panelName,q=True,str=True)
	sds = cmds.modelEditor(panelName,q=True,sds=True)
	tx = cmds.modelEditor(panelName,q=True,tx=True)
	tsl = cmds.modelEditor(panelName,q=True,tsl=True)
	ui = cmds.modelEditor(panelName,q=True,ui=True)
	vs = cmds.modelEditor(panelName,q=True,vs=True)

def RecallPanel(panelName=""):
	global da, ca, cv, df, dim, dc, dtx, fl, fo, gr, hs, ha, hud, hu, ikh, imp, j, lt, lc, m, mt, ncl, npa, nr, nc, ns, pv, pl, po, ps, pm, sdw, swf, strx, sds, tx, tsl, ui, vs
	da = cmds.modelEditor(panelName, e=True, da=da)
	ca = cmds.modelEditor(panelName,e=True,ca=ca)
	cv = cmds.modelEditor(panelName,e=True,cv=cv)
	df = cmds.modelEditor(panelName,e=True,df=df)
	dim = cmds.modelEditor(panelName,e=True,dim=dim)
	dc = cmds.modelEditor(panelName,e=True,dc=dc)
	dtx = cmds.modelEditor(panelName,e=True,dtx=dtx)
	fl = cmds.modelEditor(panelName,e=True,fl=fl)
	fo = cmds.modelEditor(panelName,e=True,fo=fo)
	gr = cmds.modelEditor(panelName,e=True,gr=gr)
	hs = cmds.modelEditor(panelName,e=True,hs=hs)
	ha = cmds.modelEditor(panelName,e=True,ha=ha)
	hud = cmds.modelEditor(panelName,e=True,hud=hud)
	hu = cmds.modelEditor(panelName,e=True,hu=hu)
	ikh = cmds.modelEditor(panelName,e=True,ikh=ikh)
	imp = cmds.modelEditor(panelName,e=True,imp=imp)
	j = cmds.modelEditor(panelName,e=True,j=j)
	lt = cmds.modelEditor(panelName,e=True,lt=lt)
	lc = cmds.modelEditor(panelName,e=True,lc=lc)
	m = cmds.modelEditor(panelName,e=True,m=m)
	mt = cmds.modelEditor(panelName,e=True,mt=mt)
	ncl = cmds.modelEditor(panelName,e=True,ncl=ncl)
	npa = cmds.modelEditor(panelName,e=True,npa=npa)
	nr = cmds.modelEditor(panelName,e=True,nr=nr)
	nc = cmds.modelEditor(panelName,e=True,nc=nc)
	ns = cmds.modelEditor(panelName,e=True,ns=ns)
	pv = cmds.modelEditor(panelName,e=True,pv=pv)
	pl = cmds.modelEditor(panelName,e=True,pl=pl)
	#po = cmds.modelEditor(panelName,e=True,po=po)
	#ps = cmds.modelEditor(panelName,e=True,ps=ps)
	pm = cmds.modelEditor(panelName,e=True,pm=pm)
	sdw = cmds.modelEditor(panelName,e=True,sdw=sdw)
	swf = cmds.modelEditor(panelName,e=True,swf=swf)
	strx = cmds.modelEditor(panelName,e=True,str=strx)
	sds = cmds.modelEditor(panelName,e=True,sds=sds)
	tx = cmds.modelEditor(panelName,e=True,tx=tx)
	tsl = cmds.modelEditor(panelName,e=True,tsl=tsl)
	ui = cmds.modelEditor(panelName,e=True,ui=ui)
	vs = cmds.modelEditor(panelName,e=True,vs=vs)

def ClearPanel(panelName=""):
	cmds.modelEditor(panelName, e=True, ca=False)
	cmds.modelEditor(panelName, e=True, cv=False)
	cmds.modelEditor(panelName, e=True, df=False)
	cmds.modelEditor(panelName, e=True, dim=False)
	cmds.modelEditor(panelName, e=True, dc=False)
	cmds.modelEditor(panelName, e=True, fl=False)
	cmds.modelEditor(panelName, e=True, fo=False)
	cmds.modelEditor(panelName, e=True, gr=False)
	cmds.modelEditor(panelName, e=True, hs=False)
	cmds.modelEditor(panelName, e=True, ha=False)
	cmds.modelEditor(panelName, e=True, hud=False)
	cmds.modelEditor(panelName, e=True, hu=False)
	cmds.modelEditor(panelName, e=True, ikh=False)
	cmds.modelEditor(panelName, e=True, imp=False)
	cmds.modelEditor(panelName, e=True, j=False)
	cmds.modelEditor(panelName, e=True, lt=False)
	cmds.modelEditor(panelName, e=True, lc=False)
	cmds.modelEditor(panelName, e=True, m=False)
	cmds.modelEditor(panelName, e=True, mt=False)
	cmds.modelEditor(panelName, e=True, ncl=False)
	cmds.modelEditor(panelName, e=True, npa=False)
	cmds.modelEditor(panelName, e=True, nr=False)
	cmds.modelEditor(panelName, e=True, nc=False)
	cmds.modelEditor(panelName, e=True, ns=False)
	cmds.modelEditor(panelName, e=True, pv=False)
	cmds.modelEditor(panelName, e=True, pl=False)
	cmds.modelEditor(panelName, e=True, pm=False)
	cmds.modelEditor(panelName, e=True, sdw=False)
	cmds.modelEditor(panelName, e=True, swf=False)
	cmds.modelEditor(panelName, e=True, str=False)
	cmds.modelEditor(panelName, e=True, sds=False)
	cmds.modelEditor(panelName, e=True, tx=False)
	cmds.modelEditor(panelName, e=True, tsl=False)
	cmds.modelEditor(panelName, e=True, ui=False)
	cmds.modelEditor(panelName, e=True, vs=False)

def do():
	IMAGE_NAME = cmds.file(q=True,sn=True).split('/')[-1].split('.')[0]
	if IMAGE_NAME:
		print(MS_projectDir.PATH_THUMBNAIL)
		createThumbneil(MS_projectDir.PATH_THUMBNAIL, IMAGE_NAME, SWATCH_MODE='SUMBNAIL', RENDER='playblast', X=256, Y=256)
	cmds.image('MS_createThumbnail_image', e=True, w=256, h=256,
			   image=MS_projectDir.PATH_THUMBNAIL + '/' + IMAGE_NAME + '.jpg')

def LayoutA():
	cmds.columnLayout('MS_swatchMaker.py _mainLayout',adj = True)
	cmds.separator()
	cmds.text(l='MS_swatchMaker.py', bgc=[0.9, 0.9, 0.9], fn='boldLabelFont')
	cmds.button(l='do', c=lambda *args: do())
	cmds.separator()
	cmds.setParent('..')

def LayoutB():
	cmds.columnLayout('MS_createThumbnail_imageLayout')
	cmds.image('MS_createThumbnail_image',image = '')
	cmds.setParent('..')


def UI():
	if cmds.window('MS_tools_window', q=True, ex=True):
		cmds.deleteUI('MS_tools_window')
	cmds.window('MS_tools_window', rtf=True, s=True)
	cmds.columnLayout()
	MS_projectDir.layout()
	LayoutA()
	LayoutB()
	cmds.setParent('..')
	cmds.showWindow('MS_tools_window')
	MS_projectDir.recall()
