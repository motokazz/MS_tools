/*
仕様：あるフォルダー内にcard、chara、flameのフォルダー、card_list.txtを持たせる。
cardフォルダー>>カードの地の絵、要アルファー
charaフォルダー>>キャラのマスク抜きpsdでBGの上に1レイヤーで存在、アルファー不要
flameフォルダー>>フレームのマスク抜きpsdでBGの上に1レイヤーで存在、アルファー不要
manaフォルダー>>フレームのマスク抜きpsdでBGの上に1レイヤーで存在、アルファー不要
hpフォルダー>>フレームのマスク抜きpsdでBGの上に1レイヤーで存在、アルファー不要
attaフォルダー>>フレームのマスク抜きpsdでBGの上に1レイヤーで存在、アルファー不要
card_list.txt>>fire	z001	fire	2	1	1　TAB区切りで
地、キャラID、フレーム、使用マナ数、体力、防御力。ファイル名がおかしい場合はCard_Mix.psdで上書きしていく
要　アクション　EoJカテゴリ　card_outline　（キャラの縁取りアクション）
*/

/*イメージの合成と保存*/
function s000192_EoJ_PSP_MixCard_mix2(base_Image, chara_Image, flame_Image, mana_num, hp_num, atta_num)
{
	base_image = "";
	save_name = "Card_Mix";
	if(base_Image != ""){ base_image = base_Image; }
	else if(chara_Image != ""){ base_image = chara_Image; }
	else if(flame_Image != ""){ base_image = flame_Image; }
	else if(mana_num != ""){ base_image = mana_num; }
	else if(hp_num != ""){ base_image = hp_num; }
	else{ base_image = atta_num; }

	base_pos = base_image.layers[0].bounds;
	new_h = base_image.height;
	new_w = base_image.width;
	new_Res = base_image.resolution;
	new_Image_Name = app.documents.add(new_w, new_h, new_Res, save_name);

	if(base_Image != "")
	{
		app.activeDocument = base_Image;
		base_Image.layers[1].duplicate(new_Image_Name);
		app.activeDocument = base_Image;
		base_Image.layers[0].duplicate(new_Image_Name);
	}
	if(chara_Image != "")
	{
		app.activeDocument = chara_Image;
		chara_Image.layers[0].duplicate(new_Image_Name);
		save_name = app.activeDocument.name.split(".")[0];
		chara_Image.close(SaveOptions.DONOTSAVECHANGES);
		app.activeDocument = new_Image_Name;
		
		if(base_Image.name != "spell.psd")
		{
			if(save_name.split("_")[1] == undefined)
			{
				app.doAction("card_outline", "EoJ");
			}
		}
	}
	if(flame_Image != "")
	{
		app.activeDocument = flame_Image;
		flame_Image.layers[0].duplicate(new_Image_Name)
		flame_Image.close(SaveOptions.DONOTSAVECHANGES);
	}
	if(mana_num != "")
	{
		app.activeDocument = mana_num;
		mana_num.layers[0].duplicate(new_Image_Name)
		mana_num.close(SaveOptions.DONOTSAVECHANGES);
	}
	if(hp_num != "")
	{
		app.activeDocument = hp_num;
		hp_num.layers[0].duplicate(new_Image_Name)
		hp_num.close(SaveOptions.DONOTSAVECHANGES);
	}
	if(atta_num != "")
	{
		app.activeDocument = atta_num;
		atta_num.layers[0].duplicate(new_Image_Name)
		atta_num.close(SaveOptions.DONOTSAVECHANGES);
	}
	if(base_Image != "")
	{
		app.activeDocument = base_Image;
		base_Image.channels[3].duplicate(new_Image_Name);
		base_Image.close(SaveOptions.DONOTSAVECHANGES);
	}

	new_Image_Name.activeChannels = new_Image_Name.componentChannels;	
	new_Image_Name.saveAs(new File(Folder2_Inf.text + "/" + save_name + ".psd"));

	new_Image_Name.flatten();
	new_Image_Name2 = new_Image_Name.duplicate();
	new_Image_Name3 = new_Image_Name.duplicate();
	app.activeDocument = new_Image_Name;
	new_Image_Name.resizeImage(64, 128, 72, ResampleMethod.BICUBICSHARPER);
	// filter type --> BICUBIC, BICUBICSHARPER, BICUBICSMOOTHER, BILINEAR, NEARESTNEIGHBOR
	new_Image_Name.saveAs(new File(Folder_Inf.text + "/L_virtual_card/" + save_name + ".psd"));
	app.activeDocument = new_Image_Name2;
	new_Image_Name2.resizeImage(64, 64, 72, ResampleMethod.BICUBICSHARPER);
	new_Image_Name2.saveAs(new File(Folder_Inf.text + "/S_virtual_card/" + save_name + "_64.psd"));
	app.activeDocument = new_Image_Name3;
	new_Image_Name3.resizeImage(128, 128, 72, ResampleMethod.BICUBICSHARPER);
	new_Image_Name3.saveAs(new File(Folder_Inf.text + "/Shop_virtual_card/" + save_name + ".psd"));

	new_Image_Name.close(SaveOptions.DONOTSAVECHANGES);
	new_Image_Name2.close(SaveOptions.DONOTSAVECHANGES);
	new_Image_Name3.close(SaveOptions.DONOTSAVECHANGES);
}
/*素材イメージの読み込みとテキストデータ内の情報チェック及びエラー出力*/
function s000192_EoJ_PSP_MixCard_mix(file_array, Folder_name)
{
	err_mess = new Array;
	err_index = 0;
	for(i = 0; i < file_array.length; i+=6)
	{
		base_Image = "";
		chara_Image = "";
		flame_Image = "";
		mana_num = "";
		hp_num = "";
		atta_num = "";
	/*カード背景イメージの読み込み*/
		if(file_array[i] == "火")
		{
			base_Image = open(File(Folder_name + "/card/fire.psd"));
		}
		else if(file_array[i] == "水")
		{
			base_Image = open(File(Folder_name + "/card/water.psd"));
		}
		else if(file_array[i] == "木")
		{
			base_Image = open(File(Folder_name + "/card/wood.psd"));
		}
		else if(file_array[i] == "土")
		{
			base_Image = open(File(Folder_name + "/card/earth.psd"));
		}
		else if(file_array[i] == "機巧")
		{
			base_Image = open(File(Folder_name + "/card/metal.psd"));
		}
		else if(file_array[i] == "無")
		{
			base_Image = open(File(Folder_name + "/card/none.psd"));
		}
		else if(file_array[i] == "ス" || file_array[i] == "-")
		{
			base_Image = open(File(Folder_name + "/card/spell.psd"));
		}
		else
		{
			err_mess[err_index] = ("属性指定エラー：\t" + ( i / 6 + 1) + "行目");
			err_index++;
		}
	/*カードキャラクターイメージの読み込み*/
		chk_file = (Folder_name + "/chara/" + file_array[i+1] + ".psd");
		chk_fileObj = new File(chk_file);
		if(chk_fileObj.exists == true)
		{
			chara_Image = open(File(Folder_name + "/chara/" + file_array[i+1] + ".psd"));
		}
		else
		{
			err_mess[err_index] = ("ファイル名エラー：\t" + ( i / 6 + 1) + "行目");
			err_index++;
		}
	/*カードフレームイメージの読み込み*/
		if(file_array[i] == "火")
		{
			flame_Image = open(File(Folder_name + "/flame/fire.psd"));
		}
		else if(file_array[i] == "水")
		{
			flame_Image = open(File(Folder_name + "/flame/water.psd"));
		}
		else if(file_array[i] == "木")
		{
			flame_Image = open(File(Folder_name + "/flame/wood.psd"));
		}
		else if(file_array[i] == "土")
		{
			flame_Image = open(File(Folder_name + "/flame/earth.psd"));
		}
		else if(file_array[i] == "機巧")
		{
			flame_Image = open(File(Folder_name + "/flame/metal.psd"));
		}
		else if(file_array[i] == "無")
		{
			flame_Image = open(File(Folder_name + "/flame/none.psd"));
		}
		else if(file_array[i] == "ス" || file_array[i] == "-")
		{
			flame_Image = open(File(Folder_name + "/flame/spell.psd"));
		}
		else
		{
			err_mess[err_index] = ("フレーム属性指定エラー：\t" + ( i / 6 + 1) + "行目");
			err_index++;
		}
		/*使用マナ数の読み込み*/
		switch( file_array[i+3] )
		{
			case "0":
				mana_num = open(File(Folder_name + "/mana_num/" + file_array[i+3] + ".psd"));
				break;

			case "1":
				mana_num = open(File(Folder_name + "/mana_num/" + file_array[i+3] + ".psd"));
				break;

			case "2":
				mana_num = open(File(Folder_name + "/mana_num/" + file_array[i+3] + ".psd"));
				break;

			case "3":
				mana_num = open(File(Folder_name + "/mana_num/" + file_array[i+3] + ".psd"));
				break;

			case "4":
				mana_num = open(File(Folder_name + "/mana_num/" + file_array[i+3] + ".psd"));
				break;

			case "5":
				mana_num = open(File(Folder_name + "/mana_num/" + file_array[i+3] + ".psd"));
				break;

			case "6":
				mana_num = open(File(Folder_name + "/mana_num/" + file_array[i+3] + ".psd"));
				break;

			case "7":
				mana_num = open(File(Folder_name + "/mana_num/" + file_array[i+3] + ".psd"));
				break;

			case "8":
				mana_num = open(File(Folder_name + "/mana_num/" + file_array[i+3] + ".psd"));
				break;

			case "9":
				mana_num = open(File(Folder_name + "/mana_num/" + file_array[i+3] + ".psd"));
				break;

			case "10":
				mana_num = open(File(Folder_name + "/mana_num/" + file_array[i+3] + ".psd"));
				break;

			case "12":
				mana_num = open(File(Folder_name + "/mana_num/" + file_array[i+3] + ".psd"));
				break;

			case "X":
				mana_num = open(File(Folder_name + "/mana_num/" + file_array[i+3] + ".psd"));
				break;

			default:
				err_mess[err_index] = ("マナ数指定エラー：\t" + ( i / 6 + 1) + "行目");
				err_index++;
				break;
		}
		/*hpの読み込み*/
		switch( file_array[i+4] )
		{
			case "1":
				hp_num = open(File(Folder_name + "/hp_num/" + file_array[i+4] + ".psd"));
				break;

			case "2":
				hp_num = open(File(Folder_name + "/hp_num/" + file_array[i+4] + ".psd"));
				break;

			case "3":
				hp_num = open(File(Folder_name + "/hp_num/" + file_array[i+4] + ".psd"));
				break;

			case "4":
				hp_num = open(File(Folder_name + "/hp_num/" + file_array[i+4] + ".psd"));
				break;

			case "5":
				hp_num = open(File(Folder_name + "/hp_num/" + file_array[i+4] + ".psd"));
				break;

			case "6":
				hp_num = open(File(Folder_name + "/hp_num/" + file_array[i+4] + ".psd"));
				break;

			case "7":
				hp_num = open(File(Folder_name + "/hp_num/" + file_array[i+4] + ".psd"));
				break;

			case "8":
				hp_num = open(File(Folder_name + "/hp_num/" + file_array[i+4] + ".psd"));
				break;

			case "9":
				hp_num = open(File(Folder_name + "/hp_num/" + file_array[i+4] + ".psd"));
				break;

			case "10":
				hp_num = open(File(Folder_name + "/hp_num/" + file_array[i+4] + ".psd"));
				break;

			case "12":
				hp_num = open(File(Folder_name + "/hp_num/" + file_array[i+4] + ".psd"));
				break;

			case "-":
				hp_num = open(File(Folder_name + "/hp_num/" + file_array[i+4] + ".psd"));
				break;

			case "1+":
				hp_num = open(File(Folder_name + "/hp_num/" + file_array[i+4] + ".psd"));
				break;

			default:
				err_mess[err_index] = ("hp指定エラー：\t" + ( i / 6 + 1) + "行目");
				err_index++;
				break;
		}
		/*攻撃力の読み込み*/
		switch( file_array[i+5] )
		{
			case "0":
				atta_num = open(File(Folder_name + "/atta_num/0.psd"));
				break;

			case "1":
				atta_num = open(File(Folder_name + "/atta_num/1.psd"));
				break;

			case "2":
				atta_num = open(File(Folder_name + "/atta_num/2.psd"));
				break;

			case "3":
				atta_num = open(File(Folder_name + "/atta_num/3.psd"));
				break;

			case "4":
				atta_num = open(File(Folder_name + "/atta_num/4.psd"));
				break;

			case "8":
				atta_num = open(File(Folder_name + "/atta_num/8.psd"));
				break;

			case "9":
				atta_num = open(File(Folder_name + "/atta_num/9.psd"));
				break;

			case "-":
				atta_num = open(File(Folder_name + "/atta_num/-.psd"));
				break;

			case "0+":
				atta_num = open(File(Folder_name + "/atta_num/0+.psd"));
				break;

			case "1+":
				atta_num = open(File(Folder_name + "/atta_num/1+.psd"));
				break;

			case "1･X":
				atta_num = open(File(Folder_name + "/atta_num/1X.psd"));
				break;

			case "2+":
				atta_num = open(File(Folder_name + "/atta_num/2+.psd"));
				break;

			case "3+":
				atta_num = open(File(Folder_name + "/atta_num/3+.psd"));
				break;

			case "3･X":
				atta_num = open(File(Folder_name + "/atta_num/3X.psd"));
				break;

			case "5-":
				atta_num = open(File(Folder_name + "/atta_num/5-.psd"));
				break;

			case "5+":
				atta_num = open(File(Folder_name + "/atta_num/5+.psd"));
				break;

			case "7+":
				atta_num = open(File(Folder_name + "/atta_num/7+.psd"));
				break;

			default:
				err_mess[err_index] = ("攻撃力指定エラー：\t" + ( i / 6 + 1) + "行目");
				err_index++;
				break;
		}
	/*イメージ合成、保存関数へデータ渡し*/
		s000192_EoJ_PSP_MixCard_mix2(base_Image, chara_Image, flame_Image, mana_num, hp_num, atta_num);
	}
	alert("終了");
	if(err_mess.length != 0)
	{
		exp_file = (Folder_name + "/err_mess.txt");
		exp_fileObj = new File(exp_file);
		exp_flag = exp_fileObj.open("w");
		for(i = 0; i < err_mess.length; i++)
		{
			err_data = exp_fileObj.writeln(err_mess[i]);
		}
		exp_fileObj.close();
		alert("指定テキストに問題があります。" + Folder_name + "/err_mess.txtを確認して下さい。");
	}
}
/*テキストをarrayに変更。UIの入力項目のチェック*/
function s000192_EoJ_PSP_MixCard_load_text(Folder_name, File_name, OutFolder_name)
{
	if(Folder_name != "" && File_name != "" && OutFolder_name != "")
	{
		file_array = new Array;
		index_no = 0;
		index_skip_line_no = 0;
		filename = (Folder_name + "/" + File_name);
		fileObj = new File(filename);
		flag = fileObj.open("r");
		if (flag == true)
		{
			while (!fileObj.eof)
			{
			
				text = fileObj.readln();
				if(index_skip_line_no > 0)
				{
					readData = text.split("\t");
					if(readData[2] != undefined)
					{
		/*背景、キャラ、フレーム、マナ数、ｈｐ、攻撃力*/
						file_array[index_no] = readData[1];
						file_array[index_no+1] = readData[0];
						file_array[index_no+2] = readData[1];
						file_array[index_no+3] = readData[2];
						file_array[index_no+4] = readData[3];
						file_array[index_no+5] = readData[4];
						index_no+=6;
					}
				}
				index_skip_line_no++;
			}
			fileObj.close();
		}
		s000192_EoJ_PSP_MixCard_mix(file_array, Folder_name)
	}
	else{	alert("参照テキスト及び入力フォルダー、出力フォルダーを設定してください")}
}

/*メインUI*/
function s000192_EoJ_PSP_MixCard()
{
	NewWin = new Window("dialog", "EoJ PSP Mix Card", [200, 300, 500, 500]);
		Folder_Btn = NewWin.add("button", [10,10,80,30], "参照テキスト");
		Folder_Btn.onClick = function()
		{
			selFile = File.openDialog();
			if ( selFile != null ) {
				File_Inf.text = selFile.name;
				Folder_Inf.text = selFile.path;
				Folder2_Btn.enabled = true;
			}
		}
		File_Inf = NewWin.add("edittext", [10,40,290,60]);
		Folder_Inf = NewWin.add("edittext", [10,70,290,90]);

		Folder2_Btn = NewWin.add("button", [10,100,80,120], "出力フォルダ");
		Folder2_Btn.enabled = false;
		Folder2_Btn.onClick = function()
		{
			selFolder2 = Folder.selectDialog("Save_Folder", selFile.path);
			if ( selFolder2 != null ) {
				Folder2_Inf.text = selFolder2.fsName;
			}
		}
		Folder2_Inf = NewWin.add("edittext", [10,130,290,150]);

		Export_Btn = NewWin.add("button", [110, 160, 180, 180], "全て合成");
		Export_Btn.onClick = function()
		{
			s000192_EoJ_PSP_MixCard_load_text(Folder_Inf.text, File_Inf.text, Folder2_Inf.text);
		}
		Close_Btn = NewWin.add("button", [220, 160, 290, 180], "Close");
		Close_Btn.onClick = function()
		{
			NewWin.close(false);
		}
	NewWin.show();
}

s000192_EoJ_PSP_MixCard();
