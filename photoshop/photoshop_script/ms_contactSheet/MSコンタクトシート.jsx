

//新規ドキュメントサイズ入力
nx=parseInt(prompt("nx",512));
ny=parseInt(prompt("ny",512));

//並べる幅、高さ入力
ix=parseInt(prompt("nx",56));
iy=parseInt(prompt("ny",76));

//テンポラリー初期設定
yoko=0;
tate=0;

//新規ドキュメント
preferences.rulerUnits = Units.PIXELS;
documents.add(nx,ny);
//documents.add(eval(nx),eval(ny));

folderObj = Folder.selectDialog("フォルダを選択してください");
fileList = folderObj.getFiles();
for (i=0; i<fileList.length; i++)
{


fileObj = new File(fileList[i]);
open(fileObj);
activeDocument.selection.selectAll();
activeDocument.selection.copy();
activeDocument.close(SaveOptions.DONOTSAVECHANGES);

//選択範囲作成
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

selReg = [[yoko*ix,tate*iy],[(yoko*ix)+ix,tate*iy],[(yoko*ix)+ix,(tate*iy)+iy],[yoko*ix,(tate*iy)+iy]];
activeDocument.selection.select(selReg);

yoko++;
activeDocument.paste();
}

docObj = activeDocument;
docObj.layers["背景"].visible = false;
docObj.mergeVisibleLayers();




