# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_convertSmoothMesh
# 説明
#			エキスポート用ユーティリティ
# 作成日
#			
########################################
import maya.cmds as cmds
import maya.mel as mel

class convertSmoothMesh:

	def __init__(self,meshes=[]):
		self.meshes=meshes
		self.triangle=True
		self.Duped=[]
		self.result=[]

	def toPoly(self):#選択オブジェクトを複製してスムースメッシュをポリゴンにコンバートする。
		#self.meshes=cmds.ls(sl=True,l=True)
		if not self.meshes:
			shape=cmds.ls(type='mesh',l=True)
			if shape:
				self.meshes=cmds.listRelatives(shape,p=True)
			else:
				return

		### 複製 ###
		self.Duped=cmds.duplicate(self.meshes,rc=True)
		cmds.select(self.Duped,r=True)

		### 用意されている関数を使用 ###
		mel.eval("performSmoothMeshPreviewToPolygon")

		### コンバイン ###

		#コンストラクションヒストリーを消す
		cmds.delete(self.Duped,ch=True)

		#余計なデフォーマーを消す
		mel.eval('deleteUnusedDeformers()')
		
		Meshes=cmds.listRelatives(self.Duped,type='mesh')
		if len(Meshes)>1:#複数のオブジェクトはコンバインして出力
			self.result=cmds.polyUnite(self.Duped,ch=False)
		else:
			self.result=self.Duped
		
		#トライアングル化
		self.triangle = cmds.checkBox('Traingulate',q=True,v=True)
		if self.triangle:
			cmds.polyTriangulate(self.result,ch=False)
		
		return self.result


	def clean(self):#toPolyで作成したオブジェクトを削除する
		if self.result:
			cmds.delete(self.result)
		for EACHDUPED in self.Duped:
			if cmds.objExists(EACHDUPED):
				cmds.delete(EACHDUPED)
		cmds.select(self.meshes,r=True)


	def OptionLayout(self):
		cmds.frameLayout(l='Mesh Convert Option',cl=True,cll=False)
		cmds.columnLayout(adj=True)
		cmds.checkBox('Traingulate',v=False)
		cmds.setParent('..')
		cmds.setParent('..')


