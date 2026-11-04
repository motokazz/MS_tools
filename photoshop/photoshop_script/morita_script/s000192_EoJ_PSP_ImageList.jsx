function s000192_EoJ_PSP_ImageListOut()
{
	exp_csv = "file_name, 幅, 高さ, 左余白, 右余白, 上余白, 下余白, 左右拡大可能率, 上下拡大可能率\n";
	if(Folder_Inf.text != "")
	{
		selFolder_name = new Folder(Folder_Inf.text);
		File_Array = selFolder_name.getFiles("*.psd");
		File_Array2 = selFolder_name.getFiles("*.tga");
		File_Array3 = File_Array.concat(File_Array2);
		for(i = 0; i < File_Array3.length; i++)
		{
			base_Image = open(File(File_Array3[i]));	
			Img_w = app.activeDocument.width;
			Img_h = app.activeDocument.height;
			Img_name = app.activeDocument.name;

			app.activeDocument.selection.load(app.activeDocument.channels[3]);
			app.activeDocument.layers[0].duplicate();
			app.activeDocument.activeLayer = app.activeDocument.layers[0];
			app.activeDocument.selection.invert();
			app.activeDocument.selection.cut();
			Mask_size = app.activeDocument.layers[0].bounds;
			Scale_w = Img_w / (Mask_size[2] - Mask_size[0]);
			Scale_h = Img_h / (Mask_size[3] - Mask_size[1]);

			exp_csv = exp_csv + (Img_name + "," + Img_w + "," + Img_h + "," + Mask_size[0] + "," + Mask_size[2] + "," + Mask_size[1] + "," + Mask_size[3] + "," + Scale_w + "," + Scale_h + "\n");

			app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);
		}
		out_path = new File(Folder_Inf.text + "/s000192_EoJ_PSP_ImageList.csv");
		out_path.open("w");
		out_path.write(exp_csv);
		out_path.close();
		alert("終了");
	}
	else{alert("参照フォルダーを選んでください");}
}

function s000192_EoJ_PSP_ImageList()
{
	NewWin = new Window("dialog", "EoJ PSP Image List", [200, 300, 500, 410]);
		St_text = NewWin.add("statictext", [10, 15, 290, 35], "参照フォルダーパス");
		Folder_Btn = NewWin.add("button", [210,40,290,60], "参照パス選択");
		Folder_Btn.onClick = function()
		{
			bef_path = "";
			chk_path = new File("c:/s000192_EoJ_PSP_ImageList_setpath.txt");
			if(chk_path.exists == true)
			{
				chk_path.open("r");
				bef_path = chk_path.readln();
				chk_path.close();
			}
			readFolder = new Folder(bef_path);
			selFolder = readFolder.selectDlg();
			if ( selFolder != null ) {
				Folder_Inf.text = selFolder.fsName;
				chk_path.open("w");
				chk_path.write(selFolder.fsName);
				chk_path.close();
			}
		}
		Folder_Inf = NewWin.add("edittext", [10,40,200,60]);

		Out_Btn = NewWin.add("button", [10, 80, 80, 100], "List out");
		Out_Btn.onClick = function()
		{
			s000192_EoJ_PSP_ImageListOut()
		}
		Close_Btn = NewWin.add("button", [220, 80, 290, 100], "Close");
		Close_Btn.onClick = function()
		{
			NewWin.close(false);
		}
	NewWin.show();
}

s000192_EoJ_PSP_ImageList();