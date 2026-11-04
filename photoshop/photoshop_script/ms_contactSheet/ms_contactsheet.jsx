
function ms_contactsheet(){
    this.nx=2048;
    this.ny=2048;
    this.ix=256;
    this.iy=256;
    this.nstart=0;
    this.nstep=1;
    this.sourceFolder="D:/work/contactsheet/";
}


ms_contactsheet.prototype.exec=function(){
    //folderObj=Folder.selectDialog("フォルダを選択してください");
    folderObj=new Folder(this.sourceFolder);
    fileList = folderObj.getFiles();
    //新規ドキュメント
    preferences.rulerUnits = Units.PIXELS;

    baseDocName="";
    for (i=0; i<(fileList.length/this.nstep-this.nstart);i++)
    {

            //新規作成
        if(baseDocName==""){
            baseDocName=documents.add(this.nx,this.ny);
            alphaChannel=baseDocName.channels.add();
            yoko=0;
            tate=0;
           }
       
        //パターン埋まったら次の新規画像
        if(((yoko*this.ix)+this.ix)>this.nx){
            yoko=0;
            tate++;
        }
        if(((tate*this.iy)+this.iy)>this.ny ){
        
            docObj = baseDocName;
            //docObj.layers["背景"].visible = false;
            docObj.mergeVisibleLayers();
        
            preferences.rulerUnits = Units.PIXELS;
            baseDocName=documents.add(this.nx,this.ny);
            alphaChannel=baseDocName.channels.add();
            yoko=0;
            tate=0;
        }

        //読み込み
        fileObj = new File(fileList[i*this.nstep+this.nstart]);
        open(fileObj);
        readDocName= activeDocument;
        activeDocument.selection.selectAll();
        activeDocument.selection.copy();
        
        //選択範囲作成
        selReg = [[yoko*this.ix,tate*this.iy],[(yoko*this.ix)+this.ix,tate*this.iy],[(yoko*this.ix)+this.ix,(tate*this.iy)+this.iy],[yoko*this.ix,(tate*this.iy)+this.iy]];

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

}

//============
// UI
//============

uDlg = new Window("dialog","ms_contactsheet",[100,100,356,356]);
uDlg.panel0 = uDlg.add("panel",[6,1,251,246],"mainPanel");
uDlg.panel1 = uDlg.add("panel",[14,65,243,126],"BaseSetting");
uDlg.panel2 = uDlg.add("panel",[14,129,243,190],"FrameSetting");
uDlg.panel3 = uDlg.add("panel",[14,17,243,62],"SourceFolder");
uDlg.panel0.button0 = uDlg.panel0.add("button",[7,191,231,223], "ContactSheet");
uDlg.panel1.edittext0 = uDlg.panel1.add("edittext",[167,31,215,47], "256");
uDlg.panel1.edittext1 = uDlg.panel1.add("edittext",[103,31,151,47], "256");
uDlg.panel1.statictext0=uDlg.panel1.add("statictext",[156,34,170,44], "H");
uDlg.panel1.statictext1=uDlg.panel1.add("statictext",[91,34,107,44], "W");
uDlg.panel1.statictext2=uDlg.panel1.add("statictext",[14,34,65,44], "Pattern");
uDlg.panel1.edittext2 = uDlg.panel1.add("edittext",[167,11,215,27], "2048");
uDlg.panel1.edittext3 = uDlg.panel1.add("edittext",[103,11,151,27], "2048");
uDlg.panel1.statictext3=uDlg.panel1.add("statictext",[14,14,77,24], "NewCanvas");
uDlg.panel1.statictext4=uDlg.panel1.add("statictext",[156,14,170,24], "H");
uDlg.panel1.statictext5=uDlg.panel1.add("statictext",[91,14,107,24], "W");
uDlg.panel2.edittext4 = uDlg.panel2.add("edittext",[103,31,151,47], "1");
uDlg.panel2.statictext6=uDlg.panel2.add("statictext",[14,31,77,43], "FrameSkip");
uDlg.panel2.edittext5 = uDlg.panel2.add("edittext",[103,13,151,29], "0");
uDlg.panel2.statictext7=uDlg.panel2.add("statictext",[14,14,83,24], "StartFrame");
uDlg.panel3.button1 = uDlg.panel3.add("button",[191,7,215,31], "e");
uDlg.panel3.edittext6 = uDlg.panel3.add("edittext",[7,7,183,31], "d:/");


uDlg.panel0.button0.onClick=function(){
    cs=new ms_contactsheet;
    cs.nx=parseInt(uDlg.panel1.edittext3.text);
    cs.ny=parseInt(uDlg.panel1.edittext2.text);
    cs.ix=parseInt(uDlg.panel1.edittext0.text);
    cs.iy=parseInt(uDlg.panel1.edittext1.text);
    cs.nstart=parseInt(uDlg.panel2.edittext5.text);
    cs.nstep=parseInt(uDlg.panel2.edittext4.text);
    cs.sourceFolder=uDlg.panel3.edittext6.text;
    cs.exec();
    uDlg.close();
    
}

uDlg.panel3.button1.onClick=function(){
    f=new Folder(uDlg.panel3.edittext6.text);
    folderObj=f.selectDlg("フォルダを選択してください");
    if (folderObj){
        uDlg.panel3.edittext6.text=folderObj.fsName;
    }

}

uDlg.show();


