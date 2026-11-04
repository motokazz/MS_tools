# _*_coding:utf-8_*_
########################################
# ファイル名
#			createJAMThumbneil.py
# 説明
#			
#			
# 作成日
#			
########################################
import s2000_tools.MS_lib.MSG2_P4Lib as MSG2_P4Lib
reload(MSG2_P4Lib)

def main(TARGET_NAME):
	#forQuery
	if not TARGET_NAME:return False

	FILEPATH='D:/Projects/Gravite2/graphic/bg/jam/thumbnail/'
	MSG2_P4Lib.P4CheckOut([FILEPATH+TARGET_NAME+'.jpg'])
	if cmds.objExists('|root'):
		NODE='|root'
	else:
		NODE=cmds.ls(type='transform')
	SWATCH_CAMSETS=[[0,0,0,-20,30,0]]
	#MS_swatchMaker.objSwatchMaker( [each] , self.filePath , TARGET_NAME , CAMSETS=swatchCamSets , RENDER_NAME = 'vp2Renderer' , RENDER_OVERRIDE = 'G2Renderer' , REFFERENCE_MODEL = 'D:/Projects/Gravite2/assets/bg/model/kitten_notex.atgi')
	MS_swatchMaker.objSwatchMaker( [NODE] , FILEPATH , TARGET_NAME ,CAMSETS=SWATCH_CAMSETS ,RENDER_NAME = 'vp2Renderer' , RENDER_OVERRIDE = 'G2Renderer')
