function s000192_EoJ_PSP_MixUR_Image_Num(index_no)
{
	if(index_no <10){ return ("00" + index_no); }
	else if(index_no >9 && index_no < 100){ return ("0" + index_no); }
	else{ return index_no; }
}
function s000192_EoJ_PSP_MixUR_Image_Mix(chk_box_val)
{
	index_no = 0;
	app.backgroundColor.rgb.red = 0;
	app.backgroundColor.rgb.green = 0;
	app.backgroundColor.rgb.blue = 0;
	app.foregroundColor.rgb.red = 255;
	app.foregroundColor.rgb.green = 255;
	app.foregroundColor.rgb.blue = 255;
	chk_format = "png";
	selFolder2 = new Folder("D:\\cubic_maya\\media\\bmp\\");
	File_Array = selFolder2.getFiles("*.png");
	File_Array2 = selFolder2.getFiles("*.bmp");
	for(i = 0; i < File_Array.length; i++)
	{
		base_Image2 = open(File(File_Array2[i]));
		base_Image = open(File(File_Array[i]));
		if( chk_box_val == true)
		{
			app.activeDocument.layers[0].duplicate(base_Image2);
			app.activeDocument = base_Image2;
			app.activeDocument.activeLayer = base_Image2.layers[0];
		}
		app.doAction("sel_opacity", "EoJ");
	//	app.activeDocument.channels.add();
	//	app.activeDocument.selection.fill(app.foregroundColor);
		if( chk_box_val == false)
		{
			app.activeDocument.channels[3].duplicate(base_Image2);
		}
		else
		{
			app.activeDocument.layers[0].merge();
		}
		app.activeDocument = base_Image2;
		
		ext_no = s000192_EoJ_PSP_MixUR_Image_Num(index_no);
		saveFile = new File(Folder_Inf.text + "\\" + (Folder_Inf.text.substring((Folder_Inf.text.length - 4), Folder_Inf.text.length)) + "." + ext_no + ".tif");
		tifSaveOptions = new TiffSaveOptions();
		tifSaveOptions.alphaChannels = true;

		base_Image2.saveAs(saveFile, tifSaveOptions, true, Extension.LOWERCASE);
		base_Image2.close(SaveOptions.DONOTSAVECHANGES);
		base_Image.close(SaveOptions.DONOTSAVECHANGES);
		index_no++;
	}
}
/*メインUI*/
function s000192_EoJ_PSP_MixUR_Image()
{
	NewWin = new Window("dialog", "EoJ PSP Mix UR Image", [200, 300, 500, 425]);
		Folder_Btn = NewWin.add("button", [10,10,80,30], "出力フォルダ");
		Folder_Btn.onClick = function()
		{
			bef_path = "";
			chk_path = new File("c:/s000192_EoJ_PSP_MixUR_Image_setpath.txt");
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
		Folder_Inf = NewWin.add("edittext", [10,40,290,60]);
		
		Chk_mix = NewWin.add("checkbox", [10, 70, 300, 90], "ON:pngを合成しマスク作成/OFF:pngからマスクのみ作成");
		Chk_mix.value = false;

		Mix_Btn = NewWin.add("button", [10, 100, 90, 120], "全て合成");
		Mix_Btn.onClick = function()
		{
			s000192_EoJ_PSP_MixUR_Image_Mix(Chk_mix.value);
		}

		Close_Btn = NewWin.add("button", [220, 100, 290, 120], "Close");
		Close_Btn.onClick = function()
		{
			NewWin.close(false);
		}
	NewWin.show();
}

s000192_EoJ_PSP_MixUR_Image();