@echo off

p4 -p ssl:54.250.7.52:1666 -c motokazu.sakai_Lemon_master_6458 -u motokazu.sakai edit "//Lemon/Master/Assets/LemonArt/BG/ws_style/floor_brick.fbx"

p4 -p ssl:54.250.7.52:1666 -u motokazu.sakai sync -s "c:\Users\motokazu.sakai.ts\Perforce\motokazu.sakai_Lemon_master_6458\Assets\LemonArt\Scripts\FootPrintController.cs"

pause