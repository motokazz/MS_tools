function s000192_EOJ_MixImage_Export()
{
	if(Folder2_Inf.text != "")
	{
		for(j = 0; j < (Number(Mix_ID_Num.text)); j++)
		{
			if(j>0){s000192_EOJ_MixImage_Read(j);}
			rgb_channel = 0;
			if(View_Grn.value == true)
			{
				rgb_channel = 1;
			}
			else if(View_Ble.value == true)
			{
				rgb_channel = 2;
			}
			else{}
			app.activeDocument.layers[0].visible = false;
			app.activeDocument.activeLayer = app.activeDocument.layers[1];
			app.doAction("select", "EoJ");
			
			app.activeDocument.layers[0].visible = true;
			app.activeDocument.activeLayer = app.activeDocument.layers[0];
			
			app.activeDocument.channels.add();
			app.activeDocument.selection.invert();
			newRGB = new SolidColor();
			newRGB.rgb.red = 255;
			newRGB.rgb.green = 255;
			newRGB.rgb.blue = 255;
			app.activeDocument.selection.fill(newRGB);
			
			app.activeDocument.selection.load(app.activeDocument.channels[rgb_channel]);
			app.activeDocument.selection.fill(newRGB);
			app.activeDocument.layers[0].remove();
			app.activeDocument.layers[0].remove();

			saveFile = new File(Folder2_Inf.text + "\\" + (app.activeDocument.name.substring(0, (app.activeDocument.name.length - 4))) + ".tga");
			targaSaveOptions = new TargaSaveOptions();
			targaSaveOptions.alphaChannels = true;
			targaSaveOptions.resolution = TargaBitsPerPixels.THIRTYTWO;
			targaSaveOptions.rleCompression = true;
			app.documents[0].saveAs(saveFile, targaSaveOptions, true, Extension.LOWERCASE);
			app.documents[0].close(SaveOptions.DONOTSAVECHANGES);
		}
	}
	else{alert("出力フォルダーを選んでください");}
}
function s000192_EOJ_MixImage_selChan(selChan)
{
//	app.activeDocument.activeLayer = app.activeDocument.layers[0];
	switch(selChan)
	{
		case 0:
			for(l = 0; l < 2; l++)
			{
				app.activeDocument.channels[0].visible = true;
				app.activeDocument.channels[1].visible = false;
				app.activeDocument.channels[2].visible = false;
			}
			break;
		case 1:
			for(l = 0; l < 2; l++)
			{
				app.activeDocument.channels[0].visible = false;
				app.activeDocument.channels[1].visible = true;
				app.activeDocument.channels[2].visible = false;
			}
			break;
		case 2:
			for(l = 0; l < 2; l++)
			{
				app.activeDocument.channels[0].visible = false;
				app.activeDocument.channels[1].visible = false;
				app.activeDocument.channels[2].visible = true;
			}
			break;
	}
	WaitForRedraw();
}
function s000192_EOJ_MixImage_Read(Read_ID)
{
	if(Folder_Inf.text != "")
	{
		selFolder_array = ["/rgb/", "/mask1/", "/mask2/"];
		for(i = 0; i < 3; i++)
		{
			selFolder2 = new Folder(Folder_Inf.text + selFolder_array[i]);
			File_Array = selFolder2.getFiles("*.bmp");
			Mix_ID_Num.text = File_Array.length;
			base_Image = open(File(File_Array[Read_ID]));	
			if(i>0)
			{
				app.activeDocument.layers[0].duplicate(app.documents[0]);
				app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);
			}
		}
		WaitForRedraw();
	}
	else{alert("参照フォルダーを選んでください");}
}
function s000192_EOJ_MixImage_selView(selView)
{
	switch(selView)
	{
		case 0:
			app.activeDocument.activeLayer = app.activeDocument.layers[2];
			app.activeDocument.layers[0].visible = false;
			app.activeDocument.layers[1].visible = false;
			break;
		case 1:
			app.activeDocument.activeLayer = app.activeDocument.layers[1];
			app.activeDocument.layers[0].visible = false;
			app.activeDocument.layers[1].visible = true;
			break;
		case 2:
			app.activeDocument.activeLayer = app.activeDocument.layers[0];
			app.activeDocument.layers[0].visible = true;
			app.activeDocument.layers[1].visible = true;
			app.activeDocument.channels[0].visible = true
			app.activeDocument.channels[1].visible = false
			app.activeDocument.channels[2].visible = false
			View_Red.value = true;
			View_Grn.value = false;
			View_Ble.value = false;
			break;
	}
	WaitForRedraw();
}
/*再描画*/
function WaitForRedraw()
{
	var eventWait = charIDToTypeID("Wait")
	var enumRedrawComplete = charIDToTypeID("RdCm")
	var typeState = charIDToTypeID("Stte")
	var keyState = charIDToTypeID("Stte")
	var desc = new ActionDescriptor()
	desc.putEnumerated(keyState, typeState, enumRedrawComplete)
	executeAction(eventWait, desc, DialogModes.NO)
}
/*メインUI*/
function s000192_EOJ_MixImage_UI()
{
	NewWin = new Window("dialog", "EoJ PSP Mix Image", [200, 300, 500, 590]);
		Folder_Btn = NewWin.add("button", [10,10,80,30], "参照フォルダ");
		Folder_Btn.onClick = function()
		{
			selFolder = Folder.selectDialog();
			if ( selFolder != null ) {
				Folder_Inf.text = selFolder.fsName;
			}
		}
		Mix_ID_Num = NewWin.add("statictext", [150,10,200,30], "0");
		Folder_Inf = NewWin.add("edittext", [10,40,290,60]);
		
		Read_Btn = NewWin.add("button", [10,70,150,90], "イメージ読み込み");
		Read_Btn.onClick = function()
		{
			s000192_EOJ_MixImage_Read(0);
		}
		View_Doc = NewWin.add("panel", [10,100,290,140], "表示画面");
			View_RGB = View_Doc.add("radiobutton", [10,5,80,30], "カラー");
				View_RGB.onClick = function(){s000192_EOJ_MixImage_selView(0);}
			View_Mask1 = View_Doc.add("radiobutton", [90,5,160,30], "主マスク");
				View_Mask1.onClick = function(){s000192_EOJ_MixImage_selView(1);}
			View_Mask2 = View_Doc.add("radiobutton", [170,5,240,30], "補助マスク");
				View_Mask2.onClick = function(){s000192_EOJ_MixImage_selView(2);}
			View_Mask2.value = true;

		View_Chn = NewWin.add("panel", [10,150,290,190], "チャンネル選択");
			View_Red = View_Chn.add("radiobutton", [10,5,60,30], "赤");
				View_Red.onClick = function(){s000192_EOJ_MixImage_selChan(0);}
			View_Grn = View_Chn.add("radiobutton", [90,5,140,30], "緑");
				View_Grn.onClick = function(){s000192_EOJ_MixImage_selChan(1);}
			View_Ble = View_Chn.add("radiobutton", [170,5,220,30], "青");
				View_Ble.onClick = function(){s000192_EOJ_MixImage_selChan(2);}
			View_Red.value = true;
		Folder2_Btn = NewWin.add("button", [10,200,80,220], "出力フォルダ");
		Folder2_Btn.onClick = function()
		{
			selFolder2 = Folder.selectDialog();
			if ( selFolder2 != null ) {
				Folder2_Inf.text = selFolder2.fsName;
			}
		}
		Folder2_Inf = NewWin.add("edittext", [10,230,290,250]);

		Redraw_Btn = NewWin.add("button", [10, 260, 70, 280], "Redraw");
		Redraw_Btn.onClick = function(){WaitForRedraw();}
		Export_Btn = NewWin.add("button", [110, 260, 180, 280], "全て合成");
		Export_Btn.onClick = function()
		{
			s000192_EOJ_MixImage_Export();
		}
		Close_Btn = NewWin.add("button", [220, 260, 290, 280], "Close");
		Close_Btn.onClick = function()
		{
			NewWin.close(false);
		}
	NewWin.show();
}

s000192_EOJ_MixImage_UI();


/*一枚のイメージにマスク２枚をコピーして加工の方が見た目の切り替えに支障が出ない？*/