//ms_modLayerSet.jsx
//@include "ms_modDocument.jsx"

function modLayerSets(){
    this.aDoc= activeDocument;
}

// =======================================================
//ソースドキュメント名、ソースレイヤーセット名を指定して、別のドキュメントにコピー
modLayerSets.prototype.duplicateLayerSetsToDocument = function(SRC_DOC_NAME,LAYERSET_NAME,DST_DOC_NAME){
    
    activeDocument=documents[SRC_DOC_NAME];
    ADOC=activeDocument;
    ADOC.activeLayer = ADOC.layers[LAYERSET_NAME];
    
    var idDplc = charIDToTypeID( "Dplc" );
    var desc103 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
    var ref99 = new ActionReference();
    var idLyr = charIDToTypeID( "Lyr " );
    var idOrdn = charIDToTypeID( "Ordn" );
    var idTrgt = charIDToTypeID( "Trgt" );
    ref99.putEnumerated( idLyr, idOrdn, idTrgt );
    desc103.putReference( idnull, ref99 );
    var idT = charIDToTypeID( "T   " );
    var ref100 = new ActionReference();
    var idDcmn = charIDToTypeID( "Dcmn" );
    ref100.putName( idDcmn, DST_DOC_NAME );//
    desc103.putReference( idT, ref100 );
    var idNm = charIDToTypeID( "Nm  " );
    desc103.putString( idNm, LAYERSET_NAME );//
    var idVrsn = charIDToTypeID( "Vrsn" );
    desc103.putInteger( idVrsn, 5 );
    executeAction( idDplc, desc103, DialogModes.NO );
}

//アクティブドキュメント内の全てのレイヤーセットを指定ドキュメントにコピー
modLayerSets.prototype.duplicateAllLayerSetsToOtherDocument = function(SRC_DOC_NAME,DST_DOC_NAME){
    //var modL=new modLayerSets;
    var modD=new modDocument;
    
   activeDocument=documents[SRC_DOC_NAME];
    
    var AD=activeDocument;
    var LS=AD.layerSets;

    modD.createDocument(DST_DOC_NAME);
    
    //レイヤーを結合
    n = activeDocument.layers.length;
    if(n>1){
        NAD=activeDocument;
        NAD.activeLayer=NAD.layers[n-1];
        activeDocument.mergeVisibleLayers();
    }
    //
    var n=LS.length;

    for(i=0;i<n;i++){
        this.duplicateLayerSetsToDocument(AD.name,LS[n-i-1].name,DST_DOC_NAME);
    }
}

//指定ドキュメントのレイヤーセットをそれぞれ結合
modLayerSets.prototype.mergeAllLayerSets = function (DOC_NAME){
    activeDocument=documents[DOC_NAME];
    var NAD=activeDocument;
    var NLS=NAD.layerSets;
    var nn=NLS.length;
    for(i=0;i<nn;i++){
        NLS[nn-i-1].merge();
    }
}





//新規レイヤーセットを作成
modLayerSets.prototype.createLayerSet = function(NAME){
    // =======================================================
    var idMk = charIDToTypeID( "Mk  " );
    var desc13 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
    var ref12 = new ActionReference();
    var idlayerSection = stringIDToTypeID( "layerSection" );
    ref12.putClass( idlayerSection );
    desc13.putReference( idnull, ref12 );
    var idUsng = charIDToTypeID( "Usng" );
    var desc14 = new ActionDescriptor();
    var idNm = charIDToTypeID( "Nm  " );
    desc14.putString( idNm, NAME);//
    var idlayerSection = stringIDToTypeID( "layerSection" );
    desc13.putObject( idUsng, idlayerSection, desc14 );
    executeAction( idMk, desc13, DialogModes.NO );
}

//レイヤーセットを選択
modLayerSets.prototype.selectLayerSet = function(NAME){
    var idslct = charIDToTypeID( "slct" );
    var desc16 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
    var ref14 = new ActionReference();
    var idLyr = charIDToTypeID( "Lyr " );
    ref14.putName( idLyr, NAME);
    desc16.putReference( idnull, ref14 );
    var idMkVs = charIDToTypeID( "MkVs" );
    desc16.putBoolean( idMkVs, false );
    executeAction( idslct, desc16, DialogModes.NO );
}

// レイヤーセット削除
modLayerSets.prototype.deleteLayerSet = function(NAME){
var idDlt = charIDToTypeID( "Dlt " );
    var desc41 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
        var ref27 = new ActionReference();
        var idLyr = charIDToTypeID( "Lyr " );
        var idOrdn = charIDToTypeID( "Ordn" );
        var idTrgt = charIDToTypeID( "Trgt" );
        ref27.putEnumerated( idLyr, idOrdn, idTrgt );
    desc41.putReference( idnull, ref27 );
executeAction( idDlt, desc41, DialogModes.NO );
}
