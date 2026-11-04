//@include "ms_mppMain.jsx"
//@include "ms_mppDocuments.jsx"
//@include "ms_mppLayerToAlpha.jsx"

//=========================================================================

uDlg = new Window('dialog','サンプル',[100,100,480,400]);
//uDlg.okBtn = uDlg.add("button",[130,80,225,80+25], "OK!", { name:"ok"});


uDlg.main = uDlg.add("button",[100,10,300,10+25], "mppMain");

uDlg.btn_c = uDlg.add("button",[100,50,300,50+25], "mppDocuments_c");
uDlg.btn_s = uDlg.add("button",[100,80,300,80+25], "mppDocuments_s");
uDlg.btn_n = uDlg.add("button",[100,110,300,110+25], "mppDocuments_n");

uDlg.btn_all = uDlg.add("button",[100,140,300,140+25], "mppDocuments_all");

//=========================================================================

uDlg.main.onClick = function(){ mppMain();uDlg.close();}

uDlg.btn_c.onClick = function(){ mppDocument("_c","_ca");mppLayerToAlpha("_ca");uDlg.close();}
uDlg.btn_s.onClick = function(){ mppDocument("_s","_sa");mppLayerToAlpha("_sa");uDlg.close();}
uDlg.btn_n.onClick = function(){ mppDocument("_n","_na");mppLayerToAlpha("_na");uDlg.close();}

uDlg.btn_all.onClick = function(){
//元選択ドキュメントIDを記録
    
    var NAME = activeDocument.name;
    mppMain();

    mppDocument("_c","_ca");
    //mppLayerToAlpha("_ca");
// 元ドキュメント選択=======================================================
    activeDocument=documents[NAME];
    deleteLayerSet("_c");
    deleteLayerSet("_ca");
    
    
    mppDocument("_s","_sa");
    mppLayerToAlpha("_sa");
    // 元ドキュメント選択=======================================================
    activeDocument=documents[NAME];
    deleteLayerSet("_s");
    deleteLayerSet("_sa");



    mppDocument("_n","_na");
    mppLayerToAlpha("_na");
    // 元ドキュメント選択=======================================================
    activeDocument=documents[NAME];
    deleteLayerSet("_n");
    deleteLayerSet("_na");
    
    uDlg.close();
}


//=========================================================================

uDlg.show();





