
import maya.cmds as cmds

'''
mup_level_basic_enemy_rope_02
mup_level_beanstalk
mup_level_cave_canyons_half1
mup_level_cave_trap_1
mup_level_challenge_bumpers_02
mup_level_challenge_bumpers_easy
mup_level_challenge_cannons
mup_level_challenge_dodgeball
mup_level_challenge_waterfall
mup_level_collection_room
mup_level_collection_room_theme01_city2
mup_level_collection_room_theme03_water
mup_level_collection_room_theme04_sky
mup_level_collection_room_theme05_cave
mup_level_collection_room_theme06_forest
mup_level_enemy_flying_beanstalk
mup_level_giant_1
mup_level_giant_2
mup_level_mine_coaster_04
mup_level_multi_3vs1_shuriken
mup_level_multi_vs_spike_trap_gappy
mup_level_spider_boss_test_01
mup_level_water_jet_platform_beanstalk
mup_level_world_select
mup_level_world0_0_new_intro_1
mup_level_world3_1_Indy_cave_split1
mup_level_world3_1_Indy_cave_split2
mup_level_worldreaction_rope
mup_level_worldreaction_shuriken
mup_level_worldreaction_water
'''



odx = [
'mup_bg_city_flower_tulip'
,'mup_bg_city_flower_tulip_orange'
,'mup_bg_city_flower_tulip_pink'
,'mup_bg_city_flower_tulip_red'
,'mup_bg_city_flower_tulip_white'
,'mup_bg_city_flower_tulip_yellow'
,'mup_bg_city_flower_rose_blue'
,'mup_bg_city_flower_rose_white'
,'mup_bg_city_flower_rose_yellow'
,'mup_bg_trap_mushroom_a'
,'mup_bg_trap_mushroom_a_big'
,'mup_bg_trap_mushroom_a_blue_big'
,'mup_bg_trap_mushroom_a_cyan'
,'mup_bg_trap_mushroom_a_purple'
,'mup_bg_trap_mushroom_a_purple_big'
,'mup_bg_trap_mushroom_a_small'
,'mup_bg_trap_mushroom_a_small_cyan'
,'mup_bg_trap_mushroom_a_small_purple'
,'mup_ch_vulture'
,'mup_bg_canyon_flower_a'
,'mup_bg_canyon_flower_b'
,'mup_bg_canyon_cactus_big'
,'mup_bg_trap_mushroom_b'
]

def set_dynamic_grass():
	sel = cmds.ls(sl=True,l=True)
	for each in sel:
		cmds.setAttr(each+'.LoxFile','dynamic_grass',type='string')

	cmds.select(sel[0],r=True)


def selectObj():
	sel = cmds.textScrollList('MS_aaaaa_list_obj',q=True,si=True)
	cmds.select(sel,r=True)

def createList():
	res=[]
	sel = cmds.ls(type='transform',l=True)

	for each in sel:
		if not cmds.attributeQuery('LoxFile',n=each,ex=True):
			continue
		if not cmds.attributeQuery('Odx',n=each,ex=True):
			continue


		for eachOdx in odx:
			if cmds.getAttr(each+'.Odx') == eachOdx:
				if not cmds.getAttr(each+'.LoxFile') == 'dynamic_grass':
					res.append(each)
					continue
				if not cmds.getAttr(each+'.LookAtHero'):
					res.append(each)
					print cmds.getAttr(each+'.LookAtRange')

	cmds.select(res,r=True)
	return res

def reflesh():
	res = createList()
	cmds.textScrollList('MS_aaaaa_list_obj',e=True,ra=True)
	cmds.textScrollList('MS_aaaaa_list_obj',e=True,append=res)



def UI():
	res=createList()
	if cmds.window('MS_vertexcountFiltering_main_window',q=True,ex=True):
		cmds.deleteUI('MS_vertexcountFiltering_main_window')
	cmds.window('MS_vertexcountFiltering_main_window',rtf=True,s=True)
	cmds.columnLayout()
	cmds.button('reflesh',c=lambda *args:reflesh())
	cmds.textScrollList('MS_aaaaa_list_obj',w=500,h=500,allowMultiSelection=True,append=res,sc=lambda *args:selectObj())
	cmds.button('set_dynamic_grass',c=lambda *args:set_dynamic_grass())
	cmds.setParent('..')
	cmds.showWindow('MS_vertexcountFiltering_main_window')
		
