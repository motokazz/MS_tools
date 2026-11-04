# _*_coding:utf-8_*_
########################################
# ファイル名
#texture_replace.py
# 説明
#
#
# 作成日
#
########################################

import maya.cmds as cmds
import maya.mel
import os
import common.s1907_hypershade
import common.s1907_text_file_import

#引数
#old_texture_name = r"D:/Projects/Gravite2/graphic/bg/textures/wall/wall_kk_13_c.tif"
#new_texture_name = r"D:/Projects/Gravite2/graphic/bg/textures/wall/concrete_kw_01_c.tif"
#normal_setting = "ture"
#color_r = 1.0
#color_g = 0.0
#color_b = 0.5

def main(TARGET):
	try:
		do()
		return 'Success! texture_replace : '+TARGET
	except:
		return 'Error! texture_replace : '+TARGET


def do():

    #未使用マテリアル削除
    common.s1907_hypershade.delete_Unused_Node()

    #設定テキストファイルの読み込み
    text_table = common.s1907_text_file_import.do(r"D:/Projects/Gravite2/tools/maya/maya2014/scripts/python/s1907_replace_texture/replace.txt")
    for text in text_table:

        #テクスチャ置換
        split_table = text.split(",")
        exe_do(split_table[0],split_table[1],split_table[5],split_table[2],split_table[3],split_table[4])


#---------------------------------------------------------------
#テクスチャ置換
#---------------------------------------------------------------
def exe_do(old_texture_name,new_texture_name,normal_setting,color_r,color_g,color_b):

    if os.path.isfile(new_texture_name):

        file_table = cmds.ls(type="file")
        if file_table:
            for file_node in file_table:

                textre_path = cmds.getAttr(file_node + ".fileTextureName")

                if os.path.basename(old_texture_name) == os.path.basename(textre_path):
                    mat_table = cmds.listConnections(file_node)
                    if mat_table:
                        for mat_name in mat_table:

                            #カラーマップの差し替え
                            cmds.setAttr(file_node + ".fileTextureName",new_texture_name,type="string")

                            #カラースケール編集
                            if cmds.objExists(mat_name + ".colorScale"):
                                cmds.setAttr(mat_name + ".colorScale",float(color_r),float(color_g),float(color_b),type="double3")

                            #Noemalが指定がある場合
                            if normal_setting == "ture":
                                norimal_map(mat_name,file_node,new_texture_name)


    #未使用マテリアル削除
    common.s1907_hypershade.delete_Unused_Node()


#--------------------------------------------------------------
# NoemalMapを設定
#--------------------------------------------------------------
def norimal_map(mat_name,color_file_node,new_texture_name):

    #カラーテクスチャ名からノーマルマップ名を取得
    normal_map_path = get_normalmap_path(new_texture_name)

    if normal_map_path:

        cmds.select(mat_name)
        attr_table = cmds.listConnections(color_file_node,plugs=1)
        for attr in attr_table:

            split_table = attr.split(".")
            if split_table[-1] in "color":

                normal_attr_name = split_table[-1].replace("color","normal")
                normal_connect_attr = split_table[0] + r"." + normal_attr_name
                if cmds.objExists(normal_connect_attr):
                    new_file_node = cmds.shadingNode('file',asTexture=True)
                    cmds.setAttr(new_file_node + ".fileTextureName",normal_map_path,type="string")
                    cmds.connectAttr(new_file_node + ".outColor",normal_connect_attr,force=1)

    cmds.select(cl=1)

#--------------------------------------------------------------
# カラーテクスチャ名からノーマルマップ名を取得
#--------------------------------------------------------------
def get_normalmap_path(new_texture_name):

    if r"_c.tif" in new_texture_name:

        check_file = new_texture_name.replace(r"_c.tif",r"_n.tif")
        if os.path.isfile(check_file):
            return check_file
        else:
            check_file = new_texture_name.replace(r"_c.tif",r"_na.tif")
            if os.path.isfile(check_file):
                return check_file

    else:
        if r"_ca.tif" in new_texture_name:

            check_file = new_texture_name.replace(r"_ca.tif",r"_n.tif")
            if os.path.isfile(check_file):
                return check_file
            else:
                check_file = new_texture_name.replace(r"_ca.tif",r"_na.tif")
                if os.path.isfile(check_file):
                    return check_file

