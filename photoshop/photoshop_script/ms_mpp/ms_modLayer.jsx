// =======================================================
//ms_modLayer.jsx
//レイヤー関連のコマンドモジュール
// =======================================================

function modLayer(){
}
//可視レイヤーを結合
modLayer.prototype.mergeVisibleLayers = function(){
    n = activeDocument.layers.length;
    if(n>1){
        AD=activeDocument;
        AD.activeLayer=AD.layers[n-1];
        activeDocument.mergeVisibleLayers();
    }
}

//レイヤーの透明部分を選択
modLayer.prototype.selectLayerTransparency = function(){
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

//レイヤー名を指定して選択
modLayer.prototype.selectLayer = function(NAME){
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
//レイヤー名を指定して追加選択
modLayer.prototype.selectAddLayer = function(NAME){
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
//レイヤーがあるかどうかのチェック
modLayer.prototype.checkLayer = function(NAME){
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

//レイヤー新規作成
modLayer.prototype.createLayer = function(){
    var idMk = charIDToTypeID( "Mk  " );
    var desc17 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
    var ref15 = new ActionReference();
    var idLyr = charIDToTypeID( "Lyr " );
    ref15.putClass( idLyr );
    desc17.putReference( idnull, ref15 );
    executeAction( idMk, desc17, DialogModes.NO );
}
//選択レイヤーを複製、（単一）
modLayer.prototype.duplicateSelectedLayers = function(){
    var idDplc = charIDToTypeID( "Dplc" );
    var desc68 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
    var ref61 = new ActionReference();
    var idLyr = charIDToTypeID( "Lyr " );
    var idOrdn = charIDToTypeID( "Ordn" );
    var idTrgt = charIDToTypeID( "Trgt" );
    ref61.putEnumerated( idLyr, idOrdn, idTrgt );
    desc68.putReference( idnull, ref61 );
    var idVrsn = charIDToTypeID( "Vrsn" );
    desc68.putInteger( idVrsn, 5 );
    executeAction( idDplc, desc68, DialogModes.NO );
}
//複数の選択レイヤー情報を取得、文字配列を返す。
modLayer.prototype.getSelectedLayers = function(){
    //--------------------------------------レイヤからグループ
    var idGrp = stringIDToTypeID( "groupLayersEvent" );
    var descGrp = new ActionDescriptor();
    var refGrp = new ActionReference();
    refGrp.putEnumerated(charIDToTypeID( "Lyr " ),charIDToTypeID( "Ordn" ),charIDToTypeID( "Trgt" ));
    descGrp.putReference(charIDToTypeID( "null" ), refGrp );
    executeAction( idGrp, descGrp, DialogModes.ALL );//外部関数にして呼び出しすると妙に遅いので注意だ
    //================== トレーラーのレイヤを取得
    var resultLayers=new Array();
    for (var ix=0;ix<app.activeDocument.activeLayer.layers.length;ix++){resultLayers.push(app.activeDocument.activeLayer.layers[ix])}
    // =================== UNDOバッファを使用して復帰
    var id8 = charIDToTypeID( "slct" );
    var desc5 = new ActionDescriptor();
    var id9 = charIDToTypeID( "null" );
    var ref2 = new ActionReference();
    var id10 = charIDToTypeID( "HstS" );
    var id11 = charIDToTypeID( "Ordn" );
    var id12 = charIDToTypeID( "Prvs" );  
    ref2.putEnumerated( id10, id11, id12 );
    desc5.putReference( id9, ref2 );
    executeAction( id8, desc5, DialogModes.NO );
    //配列を返す
    return resultLayers;
    //選択レイヤの復帰はUNDOが勝手にやるので何もしない
}

// 選択レイヤーの透明部分をロック
modLayer.prototype.transparencyLock= function (){
    try{
    var idsetd = charIDToTypeID( "setd" );
    var desc66 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
    var ref67 = new ActionReference();
    var idLyr = charIDToTypeID( "Lyr " );
    var idOrdn = charIDToTypeID( "Ordn" );
    var idTrgt = charIDToTypeID( "Trgt" );
    ref67.putEnumerated( idLyr, idOrdn, idTrgt );
    desc66.putReference( idnull, ref67 );
    var idT = charIDToTypeID( "T   " );
    var desc67 = new ActionDescriptor();
    var idlayerLocking = stringIDToTypeID( "layerLocking" );
    var desc68 = new ActionDescriptor();
    var idprotectTransparency = stringIDToTypeID( "protectTransparency" );
    desc68.putBoolean( idprotectTransparency, true );
    var idlayerLocking = stringIDToTypeID( "layerLocking" );
    desc67.putObject( idlayerLocking, idlayerLocking, desc68 );
    var idLyr = charIDToTypeID( "Lyr " );
    desc66.putObject( idT, idLyr, desc67 );
    executeAction( idsetd, desc66, DialogModes.NO );
    }
    catch(e){
    }
}
// 選択レイヤーの透明部分をアンロック
modLayer.prototype.transparencyUnlock= function (){
    var idsetd = charIDToTypeID( "setd" );
    var desc76 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
    var ref86 = new ActionReference();
    var idLyr = charIDToTypeID( "Lyr " );
    var idOrdn = charIDToTypeID( "Ordn" );
    var idTrgt = charIDToTypeID( "Trgt" );
    ref86.putEnumerated( idLyr, idOrdn, idTrgt );
    desc76.putReference( idnull, ref86 );
    var idT = charIDToTypeID( "T   " );
    var desc77 = new ActionDescriptor();
    var idlayerLocking = stringIDToTypeID( "layerLocking" );
    var desc78 = new ActionDescriptor();
    var idprotectNone = stringIDToTypeID( "protectNone" );
    desc78.putBoolean( idprotectNone, true );
    var idlayerLocking = stringIDToTypeID( "layerLocking" );
    desc77.putObject( idlayerLocking, idlayerLocking, desc78 );
    var idLyr = charIDToTypeID( "Lyr " );
    desc76.putObject( idT, idLyr, desc77 );
    executeAction( idsetd, desc76, DialogModes.NO );
}




