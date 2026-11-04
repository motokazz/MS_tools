// =======================================================
//document
//レイヤー関連のコマンドモジュール
// =======================================================

function mergeVisibleLayers(){//可視レイヤーを結合
    n = activeDocument.layers.length;
    if(n>1){
        AD=activeDocument;
        AD.activeLayer=AD.layers[n-1];
        activeDocument.mergeVisibleLayers();
    }
}

// =======================================================
//layer
// =======================================================
function selectLayerTransparency(){//レイヤーの透明部分を選択
    try{
        var idsetd = charIDToTypeID( "setd" );
        var desc5 = new ActionDescriptor();
        var idnull = charIDToTypeID( "null" );
        var ref3 = new ActionReference();
        var idChnl = charIDToTypeID( "Chnl" );
        var idfsel = charIDToTypeID( "fsel" );
        ref3.putProperty( idChnl, idfsel );
        desc5.putReference( idnull, ref3 );
        var idT = charIDToTypeID( "T   " );
        var ref4 = new ActionReference();
        var idChnl = charIDToTypeID( "Chnl" );
        var idChnl = charIDToTypeID( "Chnl" );
        var idTrsp = charIDToTypeID( "Trsp" );
        ref4.putEnumerated( idChnl, idChnl, idTrsp );
        desc5.putReference( idT, ref4 );
        executeAction( idsetd, desc5, DialogModes.NO );
    }
    catch(e){
        //
    }
}

 // =======================================================
function selectLayer(NAME){//レイヤー名を指定して選択
    var idslct = charIDToTypeID( "slct" );
    var desc15 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
    var ref13 = new ActionReference();
    var idLyr = charIDToTypeID( "Lyr " );
    ref13.putName( idLyr, NAME );//
    desc15.putReference( idnull, ref13 );
    var idMkVs = charIDToTypeID( "MkVs" );
    desc15.putBoolean( idMkVs, false );
    executeAction( idslct, desc15, DialogModes.NO );
}
 // =======================================================
function selectAddLayer(NAME){//レイヤー名を指定して追加選択
    var idslct = charIDToTypeID( "slct" );
    var desc103 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
    var ref97 = new ActionReference();
    var idLyr = charIDToTypeID( "Lyr " );
    ref97.putName( idLyr, aName);
    desc103.putReference( idnull, ref97 );
    var idselectionModifier = stringIDToTypeID( "selectionModifier" );
    var idselectionModifierType = stringIDToTypeID( "selectionModifierType" );
    var idaddToSelection = stringIDToTypeID( "addToSelection" );
    desc103.putEnumerated( idselectionModifier, idselectionModifierType, idaddToSelection );
    var idMkVs = charIDToTypeID( "MkVs" );
    desc103.putBoolean( idMkVs, false );
    executeAction( idslct, desc103, DialogModes.NO );
}
 // =======================================================
function checkLayer(NAME){//レイヤーがあるかどうかのチェック
    layObj = activeDocument.layerSets;
    flag = true;
    try{
        n = layObj[NAME];
    }
    catch(e){
        flag = false;
    }
    if (flag){
        return true;
    }else{
        return false;
    }
}

// =======================================================
function createLayer(){//レイヤー新規作成
    var idMk = charIDToTypeID( "Mk  " );
    var desc17 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
    var ref15 = new ActionReference();
    var idLyr = charIDToTypeID( "Lyr " );
    ref15.putClass( idLyr );
    desc17.putReference( idnull, ref15 );
    executeAction( idMk, desc17, DialogModes.NO );
}
// =======================================================
// =======================================================
//group
// =======================================================
function createGroup(NAME){//新規レイヤーセットを作成
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
 // =======================================================
function selectGroup(NAME){//レイヤーセットを選択
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
// =======================================================
function deleteLayerSet(NAME){// レイヤーセット削除
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

// =======================================================

// =======================================================
//file
// =======================================================
// =======================================================
function fileExists(filename){//ファイル存在確認
    fileObj = new File(filename);
    if(fileObj.exists){
        return true;
    }else{
        return false;
    }
    //return fileObj.exists;    
}
// =======================================================
function fileOpen(filename){//ファイルを開く
    fileObj = new File(filename);
    open(fileObj);
}
// =======================================================
function fileDialog(){//ファイル指定ダイアログ
    filename = File.openDialog("開く画像ファイルを指定してください");
    if (filename){
        return filename;
    }  
}

// =======================================================
function closeDocument(){//ドキュメントを閉じる
    activeDocument.close(SaveOptions.DONOTSAVECHANGES);
}
// =======================================================
// name
// =======================================================
function imageNameConversion(filename){//ファイル名を命名規則に合わせたリストにして返す
    var renamed=new String();
    STR=new String(filename);
    if(STR.match(/_c./)){renamed=STR.replace(/_c./,".");}
    else if(STR.match(/_ca./)){renamed=STR.replace(/_ca./,".");}
    else if(STR.match(/_n./)){renamed=STR.replace(/_n./,".");}
    else if(STR.match(/_na./)){renamed=STR.replace(/_na/,".");}
    else if(STR.match(/_s./)){renamed=STR.replace(/_s./,".");}
    else if(STR.match(/_sa./)){renamed=STR.replace(/_sa./,".");}
    else{renamed=STR;}
    
    //
    filenameArr=new Array();
    filenameArr.push(renamed.replace(".","_c."));
    filenameArr.push(renamed.replace(".","_ca."));
    filenameArr.push(renamed.replace(".","_n."));
    filenameArr.push(renamed.replace(".","_na."));
    filenameArr.push(renamed.replace(".","_s."));
    filenameArr.push(renamed.replace(".","_sa."));
    //
    return filenameArr;
}

// =======================================================
// =======================================================
// =======================================================
// =======================================================
// =======================================================
//core
// =======================================================
function createTexGroups(){//命名規則に沿ったレイヤーセットを作る
    if (checkLayer("_c")==false){
        createGroup("_c");
    }    
    if (checkLayer("_ca")==false){
        createGroup("_ca");
    }
    if (checkLayer("_s")==false){
        createGroup("_s");
    }
    if (checkLayer("_sa")==false){
        createGroup("_sa");
    }
    if (checkLayer("_n")==false){
        createGroup("_n");
    }
    if (checkLayer("_na")==false){
        createGroup("_na");
    }
}








