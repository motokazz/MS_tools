createDialog_DLG().show(); // テスト用

// ===========================================================================
function createDialog_DLG(){
	var dialogResource = "dialog { text:'ウインドウタイトル', bounds:[0, 0, 400, 106], "
	dialogResource += " }";
// ===========================================================================
	dialogResource += " pnl: Panel { text:'パネル', bounds:[18, 30, 388, 73], "
	dialogResource += " }," 
	dialogResource += " str: StaticText { text:'テキスト', bounds:[20, 141, 61, 152],  }, "
	dialogResource += " ebox: EditText { bounds:[59, 138, 373, 156],  }, "
	dialogResource += " build: Button { text:'実行', bounds:[303, 88, 387, 112],  }, "
	dialogResource += " cancel: Button { text:'キャンセル', bounds:[203, 88, 287, 112],  }, "
	dialogResource += " rb1: RadioButton { text:'ラジオボタン', bounds:[35, 79, 112, 91],  }, "
	dialogResource += " cb1: Checkbox { text:'チェックボックス', bounds:[35, 99, 123, 112],  }, "
	dialogResource += " scb1: Scrollbar { bounds:[35, 46, 339, 66],  }, "
	dialogResource += " sld1: Slider { bounds:[35, 166, 339, 186],  }, "

	var dlg = new Window( dialogResource );
	dlg.center();
	return dlg;
}

