//ms_mpp2.jsx
//@include "ms_mppPaint.jsx"
//@include "ms_modPaint.jsx"
//@include "ms_modLayer.jsx"
//@include "ms_modLayerSet.jsx"
//@include "ms_modFile.jsx"

function mpp2(){
    this.AD=activeDocument;
    this.dName=this.AD.name;
    this.NAME = this.dName.split(".")[0];
    this.REF_PATH = "D:/Mproject/MS_WORK/ref/texture/";
}

mpp2.prototype.all=function(){
    this.funcDoc("_c");
    this.funcDoc("_s");
    this.funcDoc("_n");
}

mpp2.prototype.funcDoc=function(OPTION_NAME){//レイヤー機能を利用した新規テクスチャ作成
    var mppP = new mppPaint;
    var modLS = new modLayerSets;
    activeDocument=documents[this.dName];
    NEW_DOC_NAME=this.NAME+OPTION_NAME;
    
    modLS.duplicateAllLayerSetsToOtherDocument(this.dName,NEW_DOC_NAME,OPTION_NAME);
    modLS.mergeAllLayerSets(NEW_DOC_NAME);

    activeDocument = documents[NEW_DOC_NAME];
    var NAD=activeDocument;
    var NLS=NAD.layers;
    var Nn=NLS.length;
    //レイヤー名のテクスチャでペイント
    for(i=0;i<Nn;i++){
        TEX_NAME=NLS[Nn-i-1].name;
        var mppP = new mppPaint;
        NAD.activeLayer=NAD.layers[Nn-i-1];
        mppP.paintFile(this.REF_PATH+TEX_NAME+OPTION_NAME+".tif");
        mppP.paintFile(this.REF_PATH+TEX_NAME+OPTION_NAME+"a.tif");
        var modL = new modLayer;
    }
}


var a = new mpp2;
a.all();















