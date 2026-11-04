

//新規ドキュメントサイズ入力
nx=parseInt(prompt("nx",512));
ny=parseInt(prompt("ny",512));

//並べる幅、高さ入力
ix=parseInt(prompt("nx",128));
iy=parseInt(prompt("ny",128));


//ステップ
nstart=parseInt(prompt("n枚目からスタート",1));
nstep=parseInt(prompt("フレームスキップ（１でスキップ無し））",1));

//テンポラリー初期設定
yoko=0;
tate=0;

//新規ドキュメント
preferences.rulerUnits = Units.PIXELS;
documents.add(nx,ny);
//documents.add(eval(nx),eval(ny));

folderObj = Folder.selectDialog("フォルダを選択してください");
fileList = folderObj.getFiles();
for (i=0; i<(fileList.length/nstep-nstart);i++)
{


	fileObj = new File(fileList[i*nstep+nstart]);
	open(fileObj);
	activeDocument.selection.selectAll();
	activeDocument.selection.copy();
	activeDocument.close(SaveOptions.DONOTSAVECHANGES);

	//パターン埋まったら次の新規画像
	if(((yoko*ix)+ix)>nx){
		yoko=0;
		tate++;
	}
	if(((tate*iy)+iy)>ny){
	
		docObj = activeDocument;
		docObj.layers["背景"].visible = false;
		docObj.mergeVisibleLayers();
	
		preferences.rulerUnits = Units.PIXELS;
		documents.add(nx,ny);
	
		yoko=0;
		tate=0;
	}
	
	//選択範囲作成
	selReg = [[yoko*ix,tate*iy],[(yoko*ix)+ix,tate*iy],[(yoko*ix)+ix,(tate*iy)+iy],[yoko*ix,(tate*iy)+iy]];
	//selReg = [[(yoko/(nstep))*ix,tate*iy],[((yoko/(nstep))*ix)+ix,tate*iy],[((yoko/(nstep+1))*ix)+ix,(tate*iy)+iy],[(yoko/(nstep))*ix,(tate*iy)+iy]];
	activeDocument.selection.select(selReg);

	yoko++;
	activeDocument.paste();
}

docObj = activeDocument;
docObj.layers["背景"].visible = false;
docObj.mergeVisibleLayers();




