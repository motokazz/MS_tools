# _*_coding:utf-8_*_
########################################
# ファイル名
#			MS_three_char_checker.py
# 説明
#
#
# 作成日
#
########################################

import maya.cmds as cmds

head_poly_count = 2000
body_poly_count = 3000
leg_poly_count = 1500
foot_poly_count = 1000
head_tex_size = (512, 512)
body_tex_size = (512, 512)
leg_tex_size = (512, 512)
foot_tex_size = (256, 256)
enemy_poly_count = 3000

def show_regulation():
    msg = []
    msg.append('head')
    msg.append('poly = %s' % head_poly_count)
    msg.append('texsize = %s , %s' % (head_tex_size[0], head_tex_size[1]))
    msg.append('body')
    msg.append('poly = %s' % body_poly_count)
    msg.append('texsize = %s , %s' % (body_tex_size[0], body_tex_size[1]))
    msg.append('leg')
    msg.append('poly = %s' % leg_poly_count)
    msg.append('texsize = %s , %s' % (leg_tex_size[0], leg_tex_size[1]))
    msg.append('foot')
    msg.append('poly = %s' % foot_poly_count)
    msg.append('texsize = %s , %s' % (foot_tex_size[0], foot_tex_size[1]))
    msg.append('enemy')
    msg.append('poly = %s' % enemy_poly_count)
    cmds.confirmDialog(m='\n'.join(msg))
    
######################################
# UI
######################################
def LayoutA():
    cmds.columnLayout('MS_three_char_exporter_mainLayout', adj=True)
    cmds.separator()
    cmds.button(l='showreg', c=lambda *args: show_regulation())
    cmds.separator()

    cmds.setParent('..')


def UI():
    if cmds.window('MS_three_char_exporter_window', q=True, ex=True):
        cmds.deleteUI('MS_three_char_exporter_window')
    cmds.window('MS_three_char_exporter_window', rtf=True, s=True)

    LayoutA()

    cmds.showWindow('MS_three_char_exporter_window')
