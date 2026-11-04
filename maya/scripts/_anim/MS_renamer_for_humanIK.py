# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_renamer_for_humanIK
# 説明
#			rig
#			
# 作成日
#
########################################

import maya.cmds as cmds


def rencore(name):
	sel = cmds.ls(sl=True,uid=True)
	for each in sel:
		cmds.select(cmds.ls(each,uid=True),r=True)
		rencoreX(name)
	cmds.select(cmds.ls(sel,uid=True),r=True)

def rencoreX(name):
	#最初からナンバリングあるものを定義
	numed = ['LeafRightArmRoll'
		, 'LeafLeftArmRoll'
		, 'LeafRightForeArmRoll'
		, 'LeafLeftForeArmRoll'
		, 'LeafRightUpLegRoll'
		, 'LeafLeftUpLegRoll'
		, 'LeafRightLegRoll'
		, 'LeafLeftLegRoll'
		, 'LeftFootExtraFinger'
		, 'LeftFootIndex'
		, 'LeftFootMiddle'
		, 'LeftFootPinky'
		, 'LeftFootRing'
		, 'LeftFootThumb'
		, 'LeftHandExtraFinger'
		, 'LeftHandIndex'
		, 'LeftHandMiddle'
		, 'LeftHandPinky'
		, 'LeftHandRing'
		, 'LeftHandThumb'
		, 'RightFootExtraFinger'
		, 'RightFootIndex'
		, 'RightFootMiddle'
		, 'RightFootPinky'
		, 'RightFootRing'
		, 'RightFootThumb'
		, 'RightHandExtraFinger'
		, 'RightHandIndex'
		, 'RightHandMiddle'
		, 'RightHandPinky'
		, 'RightHandRing'
		, 'RightHandThumb'
	         ]

	#検索モード
	mods = cmds.getModifiers()
	if (mods & 1) > 0:
		search(name)
		return

	#

	if not cmds.ls(sl=True) or name == '':# 非選択
		return

	sel = cmds.ls(sl=True)[0].split('|')[-1]

	if sel==name: # 選択オブジェクトが同じ名前だったら何もしない
		return

	P = cmds.ls(name + '*')
	i = 1
	if not cmds.objExists( name ):
		if name in numed:

			if sel == name + str(i) and len(cmds.ls(name))==1:
				return
			elif not cmds.objExists( name+str(i)):
				cmds.rename(name + str(i))
				return
			else:
				i+=1
		else:
			cmds.rename(name)
			return

	while (True):
		print i
		if sel == name + str(i):
			break
		if not cmds.objExists( name+str(i)):
			cmds.rename(name + str(i))
			break
		elif i > 10:
			break
		else:
			i += 1


def search(name):
	cmds.select(cmds.ls([name + '*', name.lower() + '*']), r=True)


# UI

def layoutA():
	cmds.frameLayout('MS_renamer_for_humanIK_frameLayout', w=217, bgc=[0.2, 0.2, 0.2], fn='boldLabelFont', l=u'MS_renamer_for_humanIK', cll=True,
	                 cl=False)
	cmds.columnLayout()

	cmds.rowLayout(nc=3)

	cmds.columnLayout()
	cmds.separator(h=100)
	layoutRightHand()
	cmds.separator(h=100)
	layoutRightFoot()
	cmds.setParent('..')

	layoutBody()

	cmds.columnLayout()
	cmds.separator(h=100)
	layoutLeftHand()
	cmds.separator(h=100)
	layoutLeftFoot()
	cmds.setParent('..')

	cmds.setParent('..')

	cmds.setParent('..')
	cmds.setParent('..')

def layoutBody():
	cmds.gridLayout(nc=5, cw=30, ch=30)

	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'HD', ann=u'Head', c=lambda *args: rencore('Head'))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))

	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'RSEX', ann=u'RightShoulderExtra', c=lambda *args: rencore('RightShoulderExtra'))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'NK', ann=u'Neck', c=lambda *args: rencore('Neck'))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'LSEX', ann=u'LeftShoulderExtra', c=lambda *args: rencore('LeftShoulderExtra'))

	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'RA', ann=u'RightArm', c=lambda *args: rencore('RightArm'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'RS', ann=u'RightShoulder', c=lambda *args: rencore('RightShoulder'))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'LS', ann=u'LeftShoulder', c=lambda *args: rencore('LeftShoulder'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'LA', ann=u'LeftArm', c=lambda *args: rencore('LeftArm'))

	cmds.button(w=150, bgc=[0.3, 0.3, 0.3], l=u'RAR', ann=u'LeafRightArmRoll',
	            c=lambda *args: rencore('LeafRightArmRoll'))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, bgc=[0.3, 0.3, 0.3], l=u'LAR', ann=u'LeafLeftArmRoll',
	            c=lambda *args: rencore('LeafLeftArmRoll'))

	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'RFA', ann=u'RightForeArm', c=lambda *args: rencore('RightForeArm'))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'SP', ann=u'Spine', c=lambda *args: rencore('Spine'))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'LFA', ann=u'LeftForeArm', c=lambda *args: rencore('LeftForeArm'))

	cmds.button(w=150, bgc=[0.3, 0.3, 0.3], l=u'RFAR', ann=u'LeafRightForeArmRoll', c=lambda *args: rencore('LeafRightForeArmRoll'))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, bgc=[0.3, 0.3, 0.3], l=u'LFAR', ann=u'LeafLeftForeArmRoll', c=lambda *args: rencore('LeafLeftForeArmRoll'))

	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'RH', ann=u'RightHand', c=lambda *args: rencore('RightHand'))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'HP', ann=u'Hips', c=lambda *args: rencore('Hips'))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'HPT', ann=u'HipsTranslation', c=lambda *args: rencore('HipsTranslation'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'LH', ann=u'LeftHand', c=lambda *args: rencore('LeftHand'))

	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'RUL', ann=u'RightUpLeg', c=lambda *args: rencore('RightUpLeg'))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'LUL', ann=u'LeftUpLeg', c=lambda *args: rencore('LeftUpLeg'))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))

	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, bgc=[0.3, 0.3, 0.3], l=u'RULR', ann=u'LeafRightUpLegRoll', c=lambda *args: rencore('LeafRightUpLegRoll'))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, bgc=[0.3, 0.3, 0.3], l=u'LULR', ann=u'LeafLeftUpLegRoll', c=lambda *args: rencore('LeafLeftUpLegRoll'))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))

	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'RL', ann=u'RightLeg', c=lambda *args: rencore('RightLeg'))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'LL', ann=u'LeftLeg', c=lambda *args: rencore('LeftLeg'))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))

	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, bgc=[0.3, 0.3, 0.3], l=u'RLR', ann=u'LeafRightLegRoll', c=lambda *args: rencore('LeafRightLegRoll'))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, bgc=[0.3, 0.3, 0.3], l=u'LLR', ann=u'LeafLeftLegRoll', c=lambda *args: rencore('LeafLeftLegRoll'))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))

	cmds.button(w=150, bgc=[0.3, 0.6, 0.3], l=u'RTB', ann=u'RightToeBase', c=lambda *args: rencore('RightToeBase'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'RF', ann=u'RightFoot', c=lambda *args: rencore('RightFoot'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.8], l=u'Ref', ann=u'Reference', c=lambda *args: rencore('Reference'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'LF', ann=u'LeftFoot', c=lambda *args: rencore('LeftFoot'))
	cmds.button(w=150, bgc=[0.3, 0.6, 0.3], l=u'LTB', ann=u'LeftToeBase', c=lambda *args: rencore('LeftToeBase'))

	cmds.setParent('..')

def layoutLeftFoot():
	cmds.gridLayout(nc=6, cw=20, ch=25 )

	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'LIFEF', ann=u'LeftInFootExtraFinger', c=lambda *args: rencore('LeftInFootExtraFinger'))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'LIFI', ann=u'LeftInFootIndex', c=lambda *args: rencore('LeftInFootIndex'))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'LIFM', ann=u'LeftInFootMiddle', c=lambda *args: rencore('LeftInFootMiddle'))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'LIFR', ann=u'LeftInFootRing', c=lambda *args: rencore('LeftInFootRing'))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'LIFP', ann=u'LeftInFootPinky', c=lambda *args: rencore('LeftInFootPinky'))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'LIFT', ann=u'LeftInFootThumb', c=lambda *args: rencore('LeftInFootThumb'))

	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'LFEF', ann=u'LeftFootExtraFinger', c=lambda *args: rencore('LeftFootExtraFinger'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'LFT', ann=u'LeftFootThumb', c=lambda *args: rencore('LeftFootThumb'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'LFI', ann=u'LeftFootIndex', c=lambda *args: rencore('LeftFootIndex'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'LFM', ann=u'LeftFootMiddle', c=lambda *args: rencore('LeftFootMiddle'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'LFR', ann=u'LeftFootRing', c=lambda *args: rencore('LeftFootRing'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'LFP', ann=u'LeftFootPinky', c=lambda *args: rencore('LeftFootPinky'))

	cmds.setParent('..')

def layoutRightFoot():
	cmds.gridLayout(nc=6, cw=20, ch=25)

	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'RIFI', ann=u'RightInFootIndex', c=lambda *args: rencore('RightInFootIndex'))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'RIFM', ann=u'RightInFootMiddle', c=lambda *args: rencore('RightInFootMiddle'))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'RIFP', ann=u'RightInFootPinky', c=lambda *args: rencore('RightInFootPinky'))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'RIFR', ann=u'RightInFootRing', c=lambda *args: rencore('RightInFootRing'))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'RIFT', ann=u'RightInFootThumb', c=lambda *args: rencore('RightInFootThumb'))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'RIFEF', ann=u'RightInFootExtraFinger', c=lambda *args: rencore('RightInFootExtraFinger'))

	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'RFI', ann=u'RightFootIndex', c=lambda *args: rencore('RightFootIndex'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'RFM', ann=u'RightFootMiddle', c=lambda *args: rencore('RightFootMiddle'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'RFP', ann=u'RightFootPinky', c=lambda *args: rencore('RightFootPinky'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'RFR', ann=u'RightFootRing', c=lambda *args: rencore('RightFootRing'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'RFT', ann=u'RightFootThumb', c=lambda *args: rencore('RightFootThumb'))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'RFEF', ann=u'RightFootExtraFinger', c=lambda *args: rencore('RightFootExtraFinger'))

	cmds.setParent('..')

def layoutRightHand():
	cmds.gridLayout(nc=6, cw=20, ch=25)

	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'RFB', ann=u'RightFingerBase', c=lambda *args: rencore('RightFingerBase'))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'RIHT', ann=u'RightInHandThumb', c=lambda *args: rencore('RightInHandThumb'))

	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'RIHEF', ann=u'RightInHandExtraFinger', c=lambda *args: rencore('RightInHandExtraFinger'))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'RIHP', ann=u'RightInHandPinky', c=lambda *args: rencore('RightInHandPinky'))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'RIHR', ann=u'RightInHandRing', c=lambda *args: rencore('RightInHandRing'))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'RIHM', ann=u'RightInHandMiddle', c=lambda *args: rencore('RightInHandMiddle'))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'RIHI', ann=u'RightInHandIndex', c=lambda *args: rencore('RightInHandIndex'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'RHT', ann=u'RightHandThumb', c=lambda *args: rencore('RightHandThumb'))

	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'RHEF', ann=u'RightHandExtraFinger', c=lambda *args: rencore('RightHandExtraFinger'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'RHP', ann=u'RightHandPinky', c=lambda *args: rencore('RightHandPinky'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'RHR', ann=u'RightHandRing', c=lambda *args: rencore('RightHandRing'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'RHM', ann=u'RightHandMiddle', c=lambda *args: rencore('RightHandMiddle'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'RHI', ann=u'RightHandIndex', c=lambda *args: rencore('RightHandIndex'))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))

	cmds.setParent('..')

def layoutLeftHand():
	cmds.gridLayout(nc=6, cw=20, ch=25)

	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'LFB', ann=u'LeftFingerBase', c=lambda *args: rencore('LeftFingerBase'))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))
	cmds.button(w=150, l=u'', c=lambda *args: rencore(''))

	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'LIHT', ann=u'LeftInHandThumb', c=lambda *args: rencore('LeftInHandThumb'))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'LIHI', ann=u'LeftInHandIndex', c=lambda *args: rencore('LeftInHandIndex'))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'LIHM', ann=u'LeftInHandMiddle', c=lambda *args: rencore('LeftInHandMiddle'))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'LIHR', ann=u'LeftInHandRing', c=lambda *args: rencore('LeftInHandRing'))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'LIHP', ann=u'LeftInHandPinky', c=lambda *args: rencore('LeftInHandPinky'))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'LIHEF', ann=u'LeftInHandExtraFinger', c=lambda *args: rencore('LeftInHandExtraFinger'))


	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'LHT', ann=u'LeftHandThumb', c=lambda *args: rencore('LeftHandThumb'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'LHI', ann=u'LeftHandIndex', c=lambda *args: rencore('LeftHandIndex'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'LHM', ann=u'LeftHandMiddle', c=lambda *args: rencore('LeftHandMiddle'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'LHR', ann=u'LeftHandRing', c=lambda *args: rencore('LeftHandRing'))
	cmds.button(w=150, bgc=[0.5, 0.8, 0.5], l=u'LHP', ann=u'LeftHandPinky', c=lambda *args: rencore('LeftHandPinky'))
	cmds.button(w=150, bgc=[0.5, 0.5, 0.5], l=u'LHEF', ann=u'LeftHandExtraFinger', c=lambda *args: rencore('LeftHandExtraFinger'))

	cmds.setParent('..')





def UI():
	if cmds.window('MS_renamer_for_humanIK_main_window', q=True, ex=True):
		cmds.deleteUI('MS_renamer_for_humanIK_main_window')
	cmds.window('MS_renamer_for_humanIK_main_window', rtf=True, s=True)

	layoutA()

	cmds.showWindow('MS_renamer_for_humanIK_main_window')

# UI()



