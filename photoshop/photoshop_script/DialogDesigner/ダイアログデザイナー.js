// ダイアログデザイナー
//--------------------------2004.12.26 新瀬 進(http://www.os.rim.or.jp/~furu/)

var openList = "PSDファイル:*.psd, 全てのファイル形式:*";
var fileList = "Javascriptファイル:*.js, テキスト文書:*.txt, 全てのファイル形式:*";

// 調整用グローバル===========================================================
var dialogOffset = new Array(3, 22);

var dialogBd = new Array(3, 3, -10, -29);
var panelBd = new Array(2, 0, -1, -1);
var statictextBd = new Array(0, 0, 6, 0);
var edittextBd = new Array(4, 4, -3, -3);
var buttonBd = new Array(4, 4, -4, -4);
var radiobuttonBd = new Array(-1, 0, 6, 0);
var checkboxBd = new Array(0, 0, 6, 0);
var scrollbarBd = new Array(4, 4, -4, -4);
var sliderBd = new Array(0, 4, 1, 0);

// 環境設定===================================================================
var strtRulerUnits = preferences.rulerUnits; // 単位をピクセルに設定
if(strtRulerUnits != Units.PIXELS){ preferences.rulerUnits = Units.PIXELS; }
var strtCurrentDir = Folder.current.fsName.toString();

// メイン=====================================================================
opt = loadPreference( initPreference() );

if(documents.length == 0){
	var loadFile = new createDialog_LOAD(opt);
	initializeLoad(loadFile);

	runDialog(loadFile);
}

if(documents.length == 0){
  alert("ダイアログ作成用の画像を開いて実行してください");
}else{
	var tmpResource = outPutResource(activeDocument.layerSets, Array(0, 0));

	var saveFile = new createDialog_SAVE(opt);
	initializeSave(saveFile);

	if(runDialog(saveFile)){
		changePreference(saveFile, opt);
		savePreference(opt);
		makeDialogFunction(tmpResource, opt["file"]);
	}
}

// 環境設定を元に戻す=========================================================
Folder.current = strtCurrentDir;
if(strtRulerUnits != Units.PIXELS){ preferences.rulerUnits = strtRulerUnits; }

// ===========================================================================
// ===========================================================================

// パラメータ（初期設定）=====================================================
function initPreference(){
	var configPath = "~\\Photoshop Scripting Temp";
	var configFolder = new Folder(configPath);
	if(!configFolder.exists){ configFolder.create(); }

	var prefer = new Array();
	prefer["cfg"] = configPath + "\\DialogDesigner.cfg";
	prefer["left"] = "0";
	prefer["top"] = "0";
	prefer["center"] = "true";
	prefer["file"] = "";
	return prefer;
}

// ヴィジットの数だけ処理=====================================================
function outPutResource(srcSets, offset){
	var resourceString = "";
	for(var loop=srcSets.length-1; loop>=0; loop--){
		resourceString += widgetSelect(srcSets[loop], offset);
	}
	return resourceString;
}
// ヴィジット毎の設定を出力===================================================
function widgetSelect(srcLayerSet, offset){
	var widget = srcLayerSet.name.split('.');
	var myOffset = new Array();
	var resourceString = "";

	switch(widget[0].toLowerCase()){
		case'dialog':
			resourceString += "createDialog_" + widget[1].toUpperCase() + "().show(); // テスト用\n\n";
			resourceString += "// ===========================================================================\n";
			resourceString += "function createDialog_" + widget[1].toUpperCase() + "(){\n";
			resourceString += "\tvar dialogResource = \"dialog { ";
			resourceString += getTextString(srcLayerSet, "title");
			resourceString += outputBounds(srcLayerSet, dialogBd, offset);
			resourceString += "\"\n";
			myOffset[0] = dialogOffset[0];
			myOffset[1] = dialogOffset[1];

			if(srcLayerSet.layerSets.length > 0){
				resourceString += outPutResource(srcLayerSet.layerSets, myOffset);
			}

			resourceString += "\tdialogResource += \" }\";\n";
			resourceString += "\n\tvar " + widget[1];
			resourceString += " = new Window( dialogResource );\n";
			resourceString += "\t" + widget[1] + ".center();\n";
			resourceString += "\treturn " + widget[1] + ";\n";
			resourceString += "}\n\n";
			resourceString += "// ===========================================================================\n";
			break;

		case'panel':
			resourceString += "\tdialogResource += \" " + widget[1] + ": Panel { ";
			resourceString += getTextString(srcLayerSet, "text");
			resourceString += outputBounds(srcLayerSet, panelBd, offset);
			resourceString += "\"\n";
			myOffset[0] = Number(srcLayerSet.bounds[0]) + panelBd[0];
			myOffset[1] = Number(srcLayerSet.bounds[1]) + panelBd[1];

			if(srcLayerSet.layerSets.length > 0){
				resourceString += outPutResource(srcLayerSet.layerSets, myOffset);
			}

			resourceString += "\tdialogResource += \" },\" \n";
			break;

		case'statictext':
			resourceString += "\tdialogResource += \" " + widget[1] + ": StaticText { ";
			resourceString += getTextString(srcLayerSet, "text");
			resourceString += outputBounds(srcLayerSet, statictextBd, offset);
			resourceString += " }, \"\n";
			break;

		case'edittext':
			resourceString += "\tdialogResource += \" " + widget[1] + ": EditText { ";
			resourceString += outputBounds(srcLayerSet, edittextBd, offset);
			resourceString += " }, \"\n";
			break;

		case'button':
			resourceString += "\tdialogResource += \" " + widget[1] + ": Button { ";
			resourceString += getTextString(srcLayerSet, "text");
			resourceString += outputBounds(srcLayerSet, buttonBd, offset);
			resourceString += " }, \"\n";
			break;

		case'radiobutton':
			resourceString += "\tdialogResource += \" " + widget[1] + ": RadioButton { ";
			resourceString += getTextString(srcLayerSet, "text");
			resourceString += outputBounds(srcLayerSet, radiobuttonBd, offset);
			resourceString += " }, \"\n";
			break;

		case'checkbox':
			resourceString += "\tdialogResource += \" " + widget[1] + ": Checkbox { ";
			resourceString += getTextString(srcLayerSet, "text");
			resourceString += outputBounds(srcLayerSet, checkboxBd, offset);
			resourceString += " }, \"\n";
			break;

		case'scrollbar':
			resourceString += "\tdialogResource += \" " + widget[1] + ": Scrollbar { ";
			resourceString += outputBounds(srcLayerSet, scrollbarBd, offset);
			resourceString += " }, \"\n";
			break;

		case'slider':
			resourceString += "\tdialogResource += \" " + widget[1] + ": Slider { ";
			resourceString += outputBounds(srcLayerSet, sliderBd, offset);
			resourceString += " }, \"\n";
			break;
	}

	return resourceString;
}

// テキストレイヤーから内容を出力=============================================
function getTextString(srcLayerSet, name){
	var srcLayer = srcLayerSet.layers.getByName(name);
	return "text:'" + srcLayer.textItem.contents + "', ";
}

// 調整済みboundsを出力=======================================================
function outputBounds(srcLayerSet, bd, offset){
	var left = Number(srcLayerSet.bounds[0]);
	var top = Number(srcLayerSet.bounds[1]);
	var right = Number(srcLayerSet.bounds[2]);
	var bottom = Number(srcLayerSet.bounds[3]);

	var str = "bounds:[";
	str += String(left + bd[0] - offset[0]) + ", ";
	str += String(top + bd[1] - offset[1]) + ", ";
	str += String(right + bd[2] - offset[0]) + ", ";
	str += String(bottom + bd[3] - offset[1]) + "], ";
	return str;
}

// createBuilderDialogを出力==================================================
function makeDialogFunction(resourceStr, fileName){
	var dialogFile = new File(fileName);

	dialogFile.open("w");
	dialogFile.write(resourceStr);
	dialogFile.close();
}

// SAVEダイアログ=============================================================
function createDialog_SAVE(prefer){
	var dialogResource = "dialog { text:'出力ファイル指定', bounds:[0, 0, 400, 106], "
	dialogResource += " pnl: Panel { text:'出力先のファイルを指定してください。', bounds:[15, 8, 385, 51], "
	dialogResource += " ebox: EditText { bounds:[10, 16, 320, 34],  }, "
	dialogResource += " browse: Button { text:'参照', bounds:[320, 16, 360, 34],  }, "
	dialogResource += " }," 
	dialogResource += " build: Button { text:'保存', bounds:[300, 66, 384, 90],  }, "
	dialogResource += " cancel: Button { text:'キャンセル', bounds:[200, 66, 284, 90],  }, "
	dialogResource += " }";

	var save = new Window( dialogResource );

	var x = Number(prefer["left"]);
	var y = Number(prefer["top"]);
	save.bounds[0] += x;
	save.bounds[1] += y;
	save.bounds[2] += x;
	save.bounds[3] += y;
	save.pnl.ebox.text = prefer["file"];

	return save;
}

// LOADダイアログ=============================================================
function createDialog_LOAD(prefer){
	var dialogResource = "dialog { text:'入力ファイル指定', bounds:[0, 0, 400, 106], "
	dialogResource += " pnl: Panel { text:'デザインファイルを指定してください。', bounds:[15, 8, 385, 51], "
	dialogResource += " ebox: EditText { bounds:[10, 16, 320, 34],  }, "
	dialogResource += " browse: Button { text:'参照', bounds:[320, 16, 360, 34],  }, "
	dialogResource += " }," 
	dialogResource += " build: Button { text:'開く', bounds:[300, 66, 384, 90],  }, "
	dialogResource += " cancel: Button { text:'キャンセル', bounds:[200, 66, 284, 90],  }, "
	dialogResource += " }";

	var load = new Window( dialogResource );

	var x = Number(prefer["left"]);
	var y = Number(prefer["top"]);
	load.bounds[0] += x;
	load.bounds[1] += y;
	load.bounds[2] += x;
	load.bounds[3] += y;

	return load;
}

// SAVEダイアログ（ボタンを押したときなどの動作設定）=========================
function initializeSave(builder){
	with(builder){
		pnl.browse.onClick = function(){
			active = false;
			enabled = false;
			if(pnl.ebox.text){ Folder.current = pnl.ebox.text.replace(/\\[^\\]+$/, ''); }
			var selFile = File.saveDialog( "保存ファイル指定", fileList );
			enabled = true;
			active = true;
			if ( selFile != null ) {
				pnl.ebox.text = selFile.fsName.toString();
			}
		}
		pnl.ebox.onChange = function(){
			cancel.active = true;
			build.active = true;
			cancel.active = false;
			build.active = false;

		}
		cancel.onClick = function(){ this.parent.close( false ); };
		build.onClick = function(){
			var dstDoc = new File(pnl.ebox.text);
			if(dstDoc.exists){
				if(confirm(pnl.ebox.text + "\nは既に存在します。上書きしてよろしいですか？")){ this.parent.close( true ); }
			}else{
				this.parent.close( true );
			}
		}
	}
}

// LOADダイアログ（ボタンを押したときなどの動作設定）=========================
function initializeLoad(builder){
	with(builder){
		pnl.browse.onClick = function(){
			active = false;
			enabled = false;
			if(pnl.ebox.text){ Folder.current = pnl.ebox.text.replace(/\\[^\\]+$/, ''); }
			var selFile = File.openDialog( "画像を開く", openList );
			enabled = true;
			active = true;
			if ( selFile != null ) {
				pnl.ebox.text = selFile.fsName.toString();
			}
		}
		pnl.ebox.onChange = function(){
			cancel.active = true;
			build.active = true;
			cancel.active = false;
			build.active = false;

		}
		cancel.onClick = function(){ this.parent.close( false ); };
		build.onClick = function(){
			var srcDoc = new File(pnl.ebox.text);
			if(srcDoc.exists){
				open(srcDoc);
				this.parent.close( true );
			}else{
				this.parent.close( false );
			}
		};
	}
}

// ダイアログ（起動・実行）===================================================
function runDialog(dialog){
  return dialog.show();
}

// ===========================================================================
// パラメータ（変更）=========================================================
function changePreference(dialog, prefer){
	prefer["left"] = dialog.bounds.left;
	prefer["top"] = dialog.bounds.top;
	prefer["center"] = "false";
	prefer["file"] = dialog.pnl.ebox.text;
}

// パラメータ（ロード）=======================================================
function loadPreference(prefer){
	var str,preStr;

	var preferFile = new File(prefer["cfg"]);
	preferFile.open("r");
	while(true){
		str = preferFile.readln();
		if(preferFile.eof){ break; }

		preStr = str.split('=');
		prefer[preStr[0]] = preStr[1];
	}
	preferFile.close();

	return prefer;
}

// パラメータ（セーブ）=======================================================
function savePreference(prefer){
	var key;

	var preferFile = new File(prefer["cfg"]);
	preferFile.open("w");
	for(key in prefer){
		preferFile.writeln( key + "=" + prefer[key]);
	}
}

