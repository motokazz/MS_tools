/*データエクスポート#####１イメージ１ファイル出力*/
function s000192_EOJ_Image_Edit_Export()
{
	doc_name = app.activeDocument;
	layer_count = app.activeDocument.layers.length;
	channel_count = app.activeDocument.channels.length;
	doc_W = app.activeDocument.width;
	doc_H = app.activeDocument.height;
	Image_Res = app.activeDocument.resolution;
	file_head = Folder_Inf.text.split("\\");
	file_head2 = file_head[(file_head.length - 1)];
	if(layer_count + 2 == channel_count)
	{
		for(i = 0; i < (layer_count - 1); i++)
		{
			exp_Image_Name = app.documents.add(doc_W, doc_H, Image_Res, "EOJ_export_PSD");
			app.activeDocument = (doc_name);
			doc_name.layers[(layer_count - i - 2)].duplicate(exp_Image_Name); //----copy image layer----
			doc_name.channels[(i + 3)].duplicate(exp_Image_Name); //----copy mask channel----
			app.activeDocument = (exp_Image_Name);
			if(i<9)
			{
				exp_Image_Name.saveAs(new File(Folder_Inf.text + "\\" + file_head2 + ".0" + (i + 1) + ".psd"));
			}
			else
			{
				exp_Image_Name.saveAs(new File(Folder_Inf.text + "\\" + file_head2 + "." + (i + 1) + ".psd"));
			}
			exp_Image_Name.close(SaveOptions.DONOTSAVECHANGES);
		}
	}
	else{alert("レイヤーとマスクの数が不一致")}
}
/*データエクスポート#####１複数イメージ１ファイル出力「コンタクトシート作成」*/
function s000192_EOJ_Image_Edit_Export2()
{
	doc_name = app.activeDocument;
	layer_count = app.activeDocument.layers.length;
	doc_W = Number(app.activeDocument.width);
	doc_H = Number(app.activeDocument.height);
	if(divExp_Btn2_opt.value == false)
	{
		new_W_count = 512/doc_W;
		new_H_count = Math.ceil((layer_count-1)/new_W_count);
	}
	else
	{
		new_W_count = Number(divExp_Btn2_in.text);
		new_H_count = Math.ceil((layer_count-1)/new_W_count);
	}
	new_W = new_W_count * doc_W;
	new_H = new_H_count * doc_H;
//	if(new_H >256){new_H = 512;}
	app.activeDocument.resizeCanvas(new_W,new_H,AnchorPosition.TOPLEFT);
	count_down = 2;
	for(column = 0; column < (new_H_count); column++)
	{
		for(row = 0; row < (new_W_count); row++)
		{
			if(layer_count >= count_down)
			{
				app.activeDocument.layers[layer_count-count_down].translate((doc_W*row),(doc_H*column));

				activeChannels = new Array(app.activeDocument.channels[count_down+1]);
				app.activeDocument.activeChannels = activeChannels;
				app.backgroundColor.rgb.red = 0;
				app.backgroundColor.rgb.green = 0;
				app.backgroundColor.rgb.blue = 0;
//				app.activeDocument.selection.load(app.activeDocument.channels[count_down+1]);
				app.activeDocument.selection.select([[0,0],[doc_W,0],[doc_W,doc_H],[0,doc_W]]);
				app.activeDocument.selection.translate((doc_W*row),(doc_H*column));
				app.activeDocument.selection.deselect();
				activeChannels = new Array(app.activeDocument.channels[0],app.activeDocument.channels[1],app.activeDocument.channels[2]);
				app.activeDocument.activeChannels = activeChannels;
			}
			count_down++;
		}
	}
	layer_count = app.activeDocument.layers.length;
	for(i = 0; i < (layer_count-2); i++)
	{
		app.activeDocument.layers[0].merge();
	}
	activeChannels = new Array(app.activeDocument.channels[3]);
	app.activeDocument.activeChannels = activeChannels;
	app.foregroundColor.rgb.red = 255;
	app.foregroundColor.rgb.green = 255;
	app.foregroundColor.rgb.blue = 255;
	for(i = 0; i < (layer_count-2); i++)
	{
		app.activeDocument.selection.load(app.activeDocument.channels[4]);
		app.activeDocument.selection.fill(app.foregroundColor);
		app.activeDocument.channels[4].remove();
	}
	file_head = Folder_Inf.text.split("\\");
	file_head2 = file_head[(file_head.length - 1)];
	app.activeDocument.saveAs(new File(Folder_Inf.text + "\\" + file_head2 + ".psd"));
//	app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);
}
/*ドキュメントのリサイズ*/
function s000192_EOJ_Image_Edit_reSize(chk_Type)
{
	switch(chk_Type)
	{
		case 0:
			doc_W = app.activeDocument.width;
			doc_H = app.activeDocument.height;
			Size_X.text = Number(doc_W);
			Size_Y.text = Number(doc_H);
			break;
		case 1:
			doc_W = app.activeDocument.width;
			doc_H = app.activeDocument.height;
			if(doc_W < doc_H)
			{
				Size_Y.text = Number(Size_X.text)*Number(doc_H)/Number(doc_W);
			}
			else
			{
				Size_Y.text = Number(Size_X.text)*Number(doc_H)/Number(doc_W);
			}
			break;
		case 2:
			app.activeDocument.resizeImage(Number(Size_X.text), Number(Size_Y.text), 72, ResampleMethod.NEARESTNEIGHBOR);
				// filter type --> BICUBIC, BICUBICSHARPER, BICUBICSMOOTHER, BILINEAR, NEARESTNEIGHBOR
			WaitForRedraw();
			break;
		default:
			break;
	}
}
/*ドキュメントの拡縮*/
function s000192_EOJ_Image_Edit_selSC2(chk_PM)
{
	app.backgroundColor.rgb.red = 255
	app.backgroundColor.rgb.green = 255
	app.backgroundColor.rgb.blue = 255
	doc_W = app.activeDocument.width
	doc_H = app.activeDocument.height
	add_val = Aft_Edit_sel_Scl2.text;
	bounds_X = 1;
	bounds_Y = 1;
	if(doc_W > doc_H)
	{
		bounds_X = doc_W / doc_H;
	}
	else if(doc_W  < doc_H)
	{
		bounds_Y = doc_H / doc_W;
	}
	else{}
	if(chk_PM == 0)
	{
		x0 = (Number(doc_W)-Number(add_val) * bounds_X);
		y0 = (Number(doc_H)-Number(add_val) * bounds_Y);
		app.activeDocument.resizeCanvas(x0,y0,AnchorPosition.MIDDLECENTER);
	}
	else
	{
		x0 = (Number(doc_W)+Number(add_val) * bounds_X);
		y0 = (Number(doc_H)+Number(add_val) * bounds_Y);
		app.activeDocument.resizeCanvas(x0,y0,AnchorPosition.MIDDLECENTER);
	}
	WaitForRedraw();
}
/*選択範囲の拡縮*/
function s000192_EOJ_Image_Edit_selSC(chk_PM)
{
	app.activeDocument.artLayers.add();//-----layer追加-----
	app.activeDocument.activeLayer.name = "calc_bounds";
	app.activeDocument.selection.fill(app.foregroundColor);
	bounds_size = app.activeDocument.activeLayer.bounds;//-----leyerからselectionのboundingboxサイズ取得-----
	app.activeDocument.activeLayer.remove();
	add_val = Aft_Edit_sel_Scl.text;

	bounds_X = 1;
	bounds_Y = 1;
	if((bounds_size[2] - bounds_size[0]) > (bounds_size[3] - bounds_size[1]))
	{
		bounds_X = (bounds_size[2] - bounds_size[0]) / (bounds_size[3] - bounds_size[1]);
	}
	else if((bounds_size[2] - bounds_size[0]) < (bounds_size[3] - bounds_size[1]))
	{
		bounds_Y = (bounds_size[3] - bounds_size[1]) / (bounds_size[2] - bounds_size[0]);
	}
	else{}
	if(chk_PM == 0)
	{
		app.activeDocument.selection.deselect();
		x0 = (Number(bounds_size[0])+Number(add_val) * bounds_X);
		y0 = (Number(bounds_size[1])+Number(add_val) * bounds_Y);
		x1 = (Number(bounds_size[2])-Number(add_val) * bounds_X);
		y1= (Number(bounds_size[3])-Number(add_val) * bounds_Y);
		app.activeDocument.selection.select([[x0,y0],[x1,y0],[x1,y1],[x0,y1]]);
	}
	else
	{
		app.activeDocument.selection.deselect();
		x0 = (Number(bounds_size[0])-Number(add_val) * bounds_X);
		y0 = (Number(bounds_size[1])-Number(add_val) * bounds_Y);
		x1 = ((Number(bounds_size[2]))+Number(add_val) * bounds_X);
		y1= ((Number(bounds_size[3]))+Number(add_val) * bounds_Y);
		app.activeDocument.selection.select([[x0,y0],[x1,y0],[x1,y1],[x0,y1]]);
	}
	WaitForRedraw();
}
/*１レイヤー表示の１レイヤー毎のON/OFF*/
function s000192_EOJ_Image_Edit_fbplay(chk_fb)
{
	chk_vis = 0;
	if(chk_fb == 0)
	{
		for(i = 0; i<(app.activeDocument.layers.length-1); i++)
		{
			View_ID = app.activeDocument.layers[i].visible;
			if(View_ID == true)
			{
				app.activeDocument.layers[i].visible = false;
				app.activeDocument.layers[i+1].visible = true;
				chk_vis = 1;
				break;
			}
		}
	}
	else
	{
		for(i = (app.activeDocument.layers.length-2); i>=0; i--)
		{
			View_ID = app.activeDocument.layers[i].visible;
			if(View_ID == true)
			{
				app.activeDocument.layers[i].visible = false;
				if(i != 0){
					app.activeDocument.layers[i-1].visible = true;
				}
				chk_vis = 1;
				break;
			}
		}
	}
	if(chk_vis == 0 && chk_fb == 0){app.activeDocument.layers[0].visible = true;}
	else if(chk_vis == 0 && chk_fb == 1){app.activeDocument.layers[app.activeDocument.layers.length - 2].visible = true;}
	WaitForRedraw();
}
/*１レイヤー表示の初期、終了時の対象レイヤーのON/OFF*/
function s000192_EOJ_Image_Edit_play(chk_value)
{
	if(chk_value == true)
	{
		for(i=0; i<(app.activeDocument.layers.length-1); i++)
		{
			app.activeDocument.layers[i].visible=false;
		}
	}
	else
	{
		for(i=0; i<(app.activeDocument.layers.length-1); i++)
		{
			app.activeDocument.layers[i].visible=true;
		}
	}
	WaitForRedraw();
}
/*コピーされたレイヤーの対応マスクから出されたバウンディングサイズを素に正方形もしくは整数比率の四角形の範囲選択or切り出し*/
function s000192_EOJ_Image_Edit_trim(BBmin_X,BBmin_Y,BBmax_X,BBmax_Y,bind_Image_Name)
{
	add_val = 0;
	if((BBmax_X - BBmin_X) <(BBmax_Y - BBmin_Y))
	{
		if( ((BBmax_Y - BBmin_Y)/(BBmax_X - BBmin_X)) - Math.floor((BBmax_Y - BBmin_Y)/(BBmax_X - BBmin_X)) < 0.5)
		{
			add_val = Math.ceil(((BBmax_Y - BBmin_Y) - (BBmax_X - BBmin_X))/2);
			BBmin_X = BBmin_X - (((BBmax_Y - BBmin_Y) - (BBmax_X - BBmin_X)) - add_val);
			BBmax_X = BBmax_X + add_val;
		}
		else
		{
			add_val = Math.ceil((Math.ceil((BBmax_Y - BBmin_Y)/(BBmax_X - BBmin_X)) * (BBmax_X - BBmin_X) - (BBmax_Y - BBmin_Y))/ 2);
			BBmin_Y = BBmin_Y - ((Math.ceil((BBmax_Y - BBmin_Y)/(BBmax_X - BBmin_X)) * (BBmax_X - BBmin_X) - (BBmax_Y - BBmin_Y)) - add_val);
			BBmax_Y = BBmax_Y + add_val;
		}
	}
	else if((BBmax_X - BBmin_X) >(BBmax_Y - BBmin_Y))
	{
//		if( ((BBmax_X - BBmin_X)/(BBmax_Y - BBmin_Y)) - Math.floor((BBmax_X - BBmin_X)/(BBmax_Y - BBmin_Y)) < 0.5)
		if( ((BBmax_X - BBmin_X)/(BBmax_Y - BBmin_Y)) < 1.5)
		{
			add_val = Math.ceil(((BBmax_X - BBmin_X) - (BBmax_Y - BBmin_Y))/2);
			BBmin_Y = BBmin_Y - (((BBmax_X - BBmin_X) - (BBmax_Y - BBmin_Y)) - add_val);
			BBmax_Y = BBmax_Y + add_val;
		}
		else if(((BBmax_X - BBmin_X)/(BBmax_Y - BBmin_Y)) > 2.0 && ((BBmax_X - BBmin_X)/(BBmax_Y - BBmin_Y)) < 4.0)
		{
			add_val = (BBmax_Y - BBmin_Y) * 4 - (BBmax_X - BBmin_X);
			BBmin_X = BBmin_X - Math.ceil(add_val / 2);
			BBmax_X = BBmax_X + (add_val - Math.ceil(add_val / 2));
		}
		else
		{
			add_val = Math.ceil((Math.ceil((BBmax_X - BBmin_X)/(BBmax_Y - BBmin_Y)) * (BBmax_Y - BBmin_Y) - (BBmax_X - BBmin_X))/ 2);
			BBmin_X = BBmin_X - ((Math.ceil((BBmax_X - BBmin_X)/(BBmax_Y - BBmin_Y)) * (BBmax_Y - BBmin_Y) - (BBmax_X - BBmin_X)) - add_val);
			BBmax_X = BBmax_X + add_val;
		}
	}
	else{}
	doc_w = Number(app.activeDocument.width);
	doc_h = Number(app.activeDocument.height);
	if(Number(BBmin_X)<0){ BBmax_X = Number(BBmax_X) + Math.abs(Number(BBmin_X)); BBmin_X = 0;}
	if(Number(BBmin_Y)<0){ BBmax_Y = Number(BBmax_Y) + Math.abs(Number(BBmin_Y)); BBmin_Y = 0;}
	if(Number(BBmax_X)>doc_w){ BBmin_X=Number(BBmin_X)-(Number(BBmax_X)-doc_w); BBmax_X= doc_w;}
	if(Number(BBmax_Y)>doc_h){ BBmin_Y=Number(BBmin_Y)-(Number(BBmax_Y)-doc_h); BBmax_Y= doc_h;}
	if(Cut_Off.value==true){bind_Image_Name.selection.select([[BBmin_X,BBmin_Y],[BBmax_X,BBmin_Y],[BBmax_X,BBmax_Y],[BBmin_X,BBmax_Y]]);}
	else{bind_Image_Name.crop([BBmin_X,BBmin_Y,BBmax_X,BBmax_Y]);}
}
/*フォルダー内の指定フォーマットを順に読み込み新規ドキュメントにイメージ、マスクデータをレイヤー、チャンネルにコピーし閉じる*/
function s000192_EOJ_Image_Edit_bind()
{
	chk_format = "png";
	BBmin_X = 0;
	BBmin_Y = 0;
	BBmax_X = 0;
	BBmax_Y = 0;
	selFolder2 = new Folder(Folder_Inf.text);
	File_Array = selFolder2.getFiles("*.png");
	if(File_Array == ""){File_Array = selFolder2.getFiles("*.tga"); chk_format = "tga";}
	for(i = 0; i < File_Array.length; i++)
	{
		base_Image = open(File(File_Array[i]));
		if(i == 0)
		{
			Image_W = app.activeDocument.width;
			Image_H = app.activeDocument.height;
			Image_Res = app.activeDocument.resolution;
			bind_Image_Name = app.documents.add(Image_W, Image_H, Image_Res, "EOJ_bind_PSD");
			BBmin_X = Image_W;
			BBmin_Y = Image_H;
		}
		app.activeDocument = (base_Image);//-----active road image-----
		base_Image.layers[0].duplicate(bind_Image_Name); //----copy image layer----
		if(chk_format == "png")
		{
			app.doAction("sel_opacity", "EoJ");//png用アクションにて透明部分の選択及び選択範囲の保存アクションを使用
		}
		base_Image.channels[3].duplicate(bind_Image_Name); //----copy mask channel----

		app.activeDocument = (bind_Image_Name);//-----active new image-----
		bind_Image_Name.activeChannels = bind_Image_Name.componentChannels;
		bind_Image_channel = bind_Image_Name.channels.length;
		bind_Image_Name.selection.load(bind_Image_Name.channels[(bind_Image_channel - 1)]);
		bind_Image_Name.selection.invert();
		bind_Image_Name.selection.cut();
		BB_size = bind_Image_Name.activeLayer.bounds;
		if(BBmin_X > BB_size[0]){BBmin_X = BB_size[0];}
		if(BBmin_Y > BB_size[1]){BBmin_Y = BB_size[1];}
		if(BBmax_X < BB_size[2]){BBmax_X = BB_size[2];}
		if(BBmax_Y < BB_size[3]){BBmax_Y = BB_size[3];}

		base_Image.close(SaveOptions.DONOTSAVECHANGES);//-----base image close-----
	}
	bind_Image_Name.revealAll();
	s000192_EOJ_Image_Edit_trim(BBmin_X,BBmin_Y,BBmax_X,BBmax_Y,bind_Image_Name);
	WaitForRedraw();
	//alert("finish");
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
function s000192_EOJ_Image_Edit_UI()
{
	NewWin = new Window("dialog", "EoJ PSP Edit Image          Ver1.20", [200, 300, 500, 785]);
		Folder_Btn = NewWin.add("button", [10,10,80,30], "参照フォルダ");
		Folder_Btn.onClick = function()
		{
			bef_path = "";
			chk_path = new File("c:/s000192_EoJ_PSP_Edit_Image_setpath.txt");
			if(chk_path.exists == true)
			{
				chk_path.open("r");
				bef_path = chk_path.readln();
				chk_path.close();
			}
			readFolder = new Folder(bef_path);
			selFolder = readFolder.selectDlg();
//			selFolder = Folder.selectDialog();
			if ( selFolder != null ) {
				Folder_Inf.text = selFolder.fsName;
				chk_path.open("w");
				chk_path.write(selFolder.fsName);
				chk_path.close();
			}
		}
		Folder_Inf = NewWin.add("edittext", [10,40,290,60]);
		Cut_Chk = NewWin.add("panel", [10,70,290,110], "最終結果");
			Cut_Off = Cut_Chk.add("radiobutton", [10,5,120,30], "範囲選択");
			Cut_On = Cut_Chk.add("radiobutton", [130,5,240,30], "切り出し");
			Cut_Off.value = true;
		Make_Btn = NewWin.add("button", [10,120,150,140], "フォルダー内イメージを合成");
		Make_Btn.onClick = function()
		{
			s000192_EOJ_Image_Edit_bind();
		}
		
		Play_Chk = NewWin.add("panel", [10,160,290,210], "チェック用１レイヤー表示");
			Play_Chk_Mode = Play_Chk.add("checkbox", [10,10,100,30], "チェックモード");
			Play_Chk_Mode.onClick = function()
			{
				s000192_EOJ_Image_Edit_play(Play_Chk_Mode.value);
			}
			Play_Chk_B = Play_Chk.add("button", [100,10,180,30], "Backward ←");
			Play_Chk_B.onClick = function()
			{
				s000192_EOJ_Image_Edit_fbplay(0);
			}
			Play_Chk_F = Play_Chk.add("button", [190,10,270,30], "→ Forward");
			Play_Chk_F.onClick = function()
			{
				s000192_EOJ_Image_Edit_fbplay(1);
			}
			Play_Chk_Mode.value = false;

		Aft_Edit = NewWin.add("panel", [10,220,290,300], "後処理");
			Aft_Edit_sel_Tex = Aft_Edit.add("statictext",[10,10,140,30], "選択範囲加減ピクセル数");
			Aft_Edit_sel_Scl = Aft_Edit.add("edittext",[150,10,180,30], "0");
			Aft_Edit_sel_PBtn = Aft_Edit.add("button",[220,10,240,30], "-");
			Aft_Edit_sel_PBtn.onClick = function()
			{
				s000192_EOJ_Image_Edit_selSC(0);
			}
			Aft_Edit_sel_MBtn = Aft_Edit.add("button",[250,10,270,30], "+");
			Aft_Edit_sel_MBtn.onClick = function()
			{
				s000192_EOJ_Image_Edit_selSC(1);
			}
			Aft_Edit_sel_Tex2 = Aft_Edit.add("statictext",[10,40,140,60], "ドキュメント加減ピクセル数");
			Aft_Edit_sel_Scl2 = Aft_Edit.add("edittext",[150,40,180,60], "0");
			Aft_Edit_sel_PBtn2 = Aft_Edit.add("button",[220,40,240,60], "-");
			Aft_Edit_sel_PBtn2.onClick = function()
			{
				s000192_EOJ_Image_Edit_selSC2(0);
			}
			Aft_Edit_sel_MBtn2 = Aft_Edit.add("button",[250,40,270,60], "+");
			Aft_Edit_sel_MBtn2.onClick = function()
			{
				s000192_EOJ_Image_Edit_selSC2(1);
			}

		Re_Size = NewWin.add("panel", [10,310,290,360], "リサイズ");
			Size_Cal_Btn = Re_Size.add("button",[10,10,90,30], "現サイズ取得");
			Size_Cal_Btn.onClick = function()
			{
				s000192_EOJ_Image_Edit_reSize(0);
			}
			Size_X = Re_Size.add("edittext", [100,10,140,30], "0");
			Size_X.onChange = function()
			{
				s000192_EOJ_Image_Edit_reSize(1);
			}
			Size_Y = Re_Size.add("statictext", [150,10,190,30], "0");
			Re_Size_Btn = Re_Size.add("button",[200,10,270,30], "リサイズ");
			Re_Size_Btn.onClick = function()
			{
				s000192_EOJ_Image_Edit_reSize(2);
			}
		
		Exp_Opt = NewWin.add("panel", [10,370,290,440], "Export option");
			divExp_Btn1 = Exp_Opt.add("radiobutton",[10,5,120,30], "分割出力");
			divExp_Btn2 = Exp_Opt.add("radiobutton",[130,5,240,30], "シート出力");
			divExp_Btn2.value = true;
			divExp_Btn2_opt = Exp_Opt.add("checkbox",[130,30,235,50], "横分割数の指定");
			divExp_Btn2_in = Exp_Opt.add("edittext",[240,30,270,50], "4");
			divExp_Btn2_in.visible = false;
			divExp_Btn1.onClick = function(){divExp_Btn2_opt.enabled = false; divExp_Btn2_in.enabled = false;}
			divExp_Btn2.onClick = function(){divExp_Btn2_opt.enabled = true; divExp_Btn2_in.enabled = true;}
			divExp_Btn2_opt.onClick = function()
			{
				if(divExp_Btn2_opt.value == true){divExp_Btn2_in.visible = true;}
				else{divExp_Btn2_in.visible = false;}
			}

		Redraw_Btn = NewWin.add("button", [10, 460, 70, 480], "Redraw");
		Redraw_Btn.onClick = function(){WaitForRedraw();}
		Export_Btn = NewWin.add("button", [110, 460, 180, 480], "Export");
		Export_Btn.onClick = function()
		{
			if(divExp_Btn1.value == true)
			{
				s000192_EOJ_Image_Edit_Export();
			}
			else
			{
				s000192_EOJ_Image_Edit_Export2();
			}
		}
		Close_Btn = NewWin.add("button", [220, 460, 290, 480], "Close");
		Close_Btn.onClick = function()
		{
			NewWin.close(false);
		}
	NewWin.show();
}

s000192_EOJ_Image_Edit_UI();

