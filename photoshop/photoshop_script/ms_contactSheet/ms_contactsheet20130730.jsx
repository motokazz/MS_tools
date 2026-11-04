

//新規ドキュメントサイズ入力
nx=parseInt(prompt("nx",2048));
ny=parseInt(prompt("ny",2048));

//並べる幅、高さ入力
ix=parseInt(prompt("imagex",256));
iy=parseInt(prompt("imagey",256));


//ステップ
nstart=parseInt(prompt("n枚目からスタート",0));
nstep=parseInt(prompt("フレームスキップ（１でスキップ無し））",1));

//フォルダ選択
folderPre=Folder;
folderPre.path="D:/work/contactsheet/";
folderObj=Folder.selectDialog("フォルダを選択してください");
fileList = folderObj.getFiles();

//新規ドキュメント
preferences.rulerUnits = Units.PIXELS;

baseDocName=""
for (i=0; i<(fileList.length/nstep-nstart);i++)
{

        //新規作成
    if(baseDocName==""){
        baseDocName=documents.add(nx,ny);
		alphaChannel=baseDocName.channels.add();
		yoko=0;
		tate=0;
       }
   
	//パターン埋まったら次の新規画像
	if(((yoko*ix)+ix)>nx){
		yoko=0;
		tate++;
	}
	if(((tate*iy)+iy)>ny ){
	
		docObj = baseDocName;
		//docObj.layers["背景"].visible = false;
		docObj.mergeVisibleLayers();
	
		preferences.rulerUnits = Units.PIXELS;
		baseDocName=documents.add(nx,ny);
		alphaChannel=baseDocName.channels.add();
		yoko=0;
		tate=0;
	}

    //読み込み
	fileObj = new File(fileList[i*nstep+nstart]);
	open(fileObj);
	readDocName= activeDocument;
	activeDocument.selection.selectAll();
	activeDocument.selection.copy();
	
    //選択範囲作成
	selReg = [[yoko*ix,tate*iy],[(yoko*ix)+ix,tate*iy],[(yoko*ix)+ix,(tate*iy)+iy],[yoko*ix,(tate*iy)+iy]];

	activeDocument=baseDocName;
    activeDocument
    try{
    activeDocument.artLayers[1];
    }
    catch(e){
        flag=false;
    }
          if(flag==false){
            activeDocument.artLayers.add("new");
            } 
	activeDocument.selection.select(selReg);
	yoko++;
	activeDocument.paste();
	
	
	activeDocument=readDocName;
	//アルファチャンネル存在の有無
	flag=true;
	try{
		activeDocument.activeChannels=[activeDocument.channels[3]]; // アルファチャンネル1を選択
	}
	catch(e){
		flag=false;
	}
	if(flag){
		activeDocument.selection.selectAll(); // アルファチャンネルを選択
		activeDocument.selection.copy();
        
		activeDocument=baseDocName;
        activeDocument.activeChannels[3];
		activeDocument.activeChannels=[activeDocument.channels[3]];
         activeDocument.selection.select(selReg);
		activeDocument.paste();
          activeDocument.activeChannels=new Array(activeDocument.channels[0],activeDocument.channels[1],activeDocument.channels[2]);
	}
	activeDocument=readDocName;
	activeDocument.close(SaveOptions.DONOTSAVECHANGES);
}

docObj = baseDocName;
docObj.layers["背景"].visible = false;
docObj.mergeVisibleLayers();




