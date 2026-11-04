//@include "ms_mppPaint.jsx"
//@include "ms_modPaint.jsx"
//@include "ms_modLayer.jsx"
//@include "ms_modLayerSet.jsx"
//@include "ms_modFile.jsx"

var REF_PATH = "D:/Mproject/MS_WORK/ref/texture/";
DOC_NAME="test_mpp01_c.tif";
OPTION_NAME="_c";

function mpp2(){
}

funcDoc=function(REF_PATH,DOC_NAME,OPTION_NAME){//レイヤー機能を利用した新規テクスチャ作成
    var mppP = new mppPaint;
    var modLS = new modLayerSets;

    var AD=activeDocument;

    modLS.duplicateAllLayerSetsToOtherDocument(AD.name,DOC_NAME,OPTION);
    modLS.mergeAllLayerSets(DOC_NAME);

    activeDocument = documents[DOC_NAME];
    var NAD=activeDocument;
    var NLS=NAD.layers;
    var Nn=NLS.length;

    for(i=0;i<Nn;i++){
        FILENAME=NLS[Nn-i-1].name;
        var mppP = new mppPaint;
        mppP.paintFile(REF_PATH+FILENAME+OPTION_NAME+".tif");
        var modL = new modLayer;
    }
}
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        