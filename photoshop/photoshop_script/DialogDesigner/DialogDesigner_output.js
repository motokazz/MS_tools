createDialog_DLG().show(); // テスト用

// ===========================================================================
function createDialog_DLG(){
	var dialogResource = "dialog { text:'出力ファイル指定', bounds:[0, 0, 400, 106], "
	dialogResource += " pnl: Panel { text:'出力先のファイルを指定してください。', bounds:[15, 8, 385, 51], "
	dialogResource += " ebox: EditText { bounds:[10, 16, 320, 34],  }, "
	dialogResource += " browse: Button { text:'参照', bounds:[320, 16, 360, 34],  }, "
	dialogResource += " }," 
	dialogResource += " build: Button { text:'実行', bounds:[300, 66, 384, 90],  }, "
	dialogResource += " cancel: Button { text:'キャンセル', bounds:[200, 66, 284, 90],  }, "
	dialogResource += " }";

	var dlg = new Window( dialogResource );
	dlg.center();
	return dlg;
}

// ===========================================================================
