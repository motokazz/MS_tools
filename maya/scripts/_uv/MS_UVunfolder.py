# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_UVunfolder
# 説明
#			
#			
# 作成日
#			
########################################
import maya.cmds as cmds
import maya.mel as mel

def toBorderEdges():
	addFlag=False
	mods = cmds.getModifiers()
	if (mods & 1) > 0: addFlag=True
	if addFlag:
		cmds.select(cmds.polyListComponentConversion(te=True,bo=True),add=True)
	else:
		cmds.select(cmds.polyListComponentConversion(te=True,bo=True),r=True)

def shortestEdgePath():
	RES=[]
	HL = cmds.ls(hl=True)
	pre = cmds.polyListComponentConversion(tv=True)
	COMP = cmds.filterExpand(pre,ex=True,sm=31)
	for each in range(0,len(COMP)-1):
		a=COMP[each].split('[')[-1].split(']')[0]
		b=COMP[each+1].split('[')[-1].split(']')[0]
		
		cmds.polySelect(HL[0],sep=(int(a),int(b)))
		
		ED = cmds.filterExpand(sm=32,ex=True)
		RES.extend(ED)
	cmds.select(RES,r=True)

def selectBorderEdges():
	OBJ=cmds.ls(hl=True,l=True)
	if not OBJ:
		OBJ=cmds.ls(sl=True,l=True)

	cmds.select(cmds.polyListComponentConversion(OBJ,te=True),r=True)
	BO = cmds.polySelectConstraint(uv=False,t=0x8000,m=2,uvConstraint =True , bo=True,rs=True)
	
	cmds.hilite(OBJ,r=True)
	cmds.select(BO,r=True)

	cmds.polySelectConstraint(dis=True , uvConstraint = False)
	mel.eval('texSelConstSet "off";')

def selectHardEdges():
	OBJ=cmds.ls(hl=True,l=True)
	if not OBJ:
		OBJ=cmds.ls(sl=True,l=True)

	cmds.select(cmds.polyListComponentConversion(OBJ,te=True),r=True)
	BO = cmds.polySelectConstraint(uv=False,t=0x8000,m=2,sm=1,rs=True)

	cmds.hilite(OBJ,r=True)
	cmds.select(BO,r=True)
	
	cmds.polySelectConstraint(dis=True , uvConstraint = False)
	mel.eval('texSelConstSet "off";')

def addCutAndUnwrap():
	cmds.polyMapCut()

def addSewAndUnwrap():
	cmds.polyMapSewMove(nf=10,lps=0)

def unwrap(useProjection=False):
	OBJ=cmds.ls(hl=True,l=True)

	if not OBJ:
		OBJ=cmds.ls(sl=True,l=True)
	EDG=cmds.filterExpand(sm=32)

	if useProjection:
		cmds.polySphericalProjection( OBJ , ra=45.0, pc=(0, 0, 0), ps=(20, 20) )

	if EDG:
		cmds.polyProjection( OBJ , type='planar' , ibd = False , mapDirection = 'bestPlane ' , ch = False)
		cmds.polyMapSewMove ( OBJ , nf = 10 , lps = 0 , ch =False )
		cmds.polyMapCut(EDG)

	cmds.u3dUnfold(OBJ,ite=1,p=1,bi=1,tf=1,ms=1024,rs=0)
	selectBorderEdges()



def LayoutA():

	cmds.frameLayout('MS_UVunfolder_frameLayout',w=217,bgc=[0.2,0.2,0.2],fn='boldLabelFont',l='MS_UVunfolder',cll=True,cl=False)
	cmds.columnLayout('MS_UVunfolder_mainLayout',adj=True)
	cmds.separator()
	cmds.text(l='MS_UVunfolder',bgc=[0.9,0.9,0.9],fn='boldLabelFont')

	cmds.gridLayout(nc=6)
	cmds.iconTextButton(w=32,h=32,i='polyAutoProj.png',c=lambda *args:mel.eval('performPolyAutoProj 0'))
	cmds.iconTextButton(w=32,h=32,i='polyContourProj.png',c=lambda *args:mel.eval('ContourProjection'))
	cmds.iconTextButton(w=32,h=32,i='polyCylProj.png',c=lambda *args:mel.eval('performPolyProjection Cylindrical 0'))
	cmds.iconTextButton(w=32,h=32,i='polyPlanProj.png',c=lambda *args:mel.eval('performPolyProjection Planar 0'))
	cmds.iconTextButton(w=32,h=32,i='polySphereProj.png',c=lambda *args:mel.eval('performPolyProjection Spherical 0'))
	cmds.iconTextButton(w=32,h=32,i='textureEditor.png',c=lambda *args:mel.eval('TextureViewWindow'))
	cmds.setParent('..')

	cmds.gridLayout(nc=2)
	cmds.iconTextButton(w=32,h=32,i='polyMapCut.png',c=lambda *args:cmds.polyMapCut())
	cmds.iconTextButton(w=32,h=32,i='polyMoveSew.png',c=lambda *args:cmds.polyMapSewMove(nf=10,lps=0))
	cmds.setParent('..')

	cmds.text(l='select seam')
	cmds.button(l='selectBorder',c=lambda *args:selectBorderEdges())
	cmds.button(l='toBorderEdges',c=lambda *args:toBorderEdges())
	cmds.button(l='selectHardEdges',c=lambda *args:selectHardEdges())
	cmds.button(l='shortestEdgePath',c=lambda *args:shortestEdgePath())
	cmds.text(l='unwrap')

	cmds.button(l='unwrap',w=100,c=lambda *args:unwrap(useProjection=True))

	cmds.separator()
	cmds.setParent('..')
	cmds.setParent('..')

def UI():
	if cmds.window('MS_UVunfolder_window',q=True,ex=True):
		cmds.deleteUI('MS_UVunfolder_window')
	cmds.window('MS_UVunfolder_window',rtf=True,s=True)
	
	LayoutA()
	
	cmds.showWindow('MS_UVunfolder_window')
	