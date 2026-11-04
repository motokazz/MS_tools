
//レイヤーのビジビリティ調整～α用のレイヤーをコピー

function visibleAllLayerSet(){//レイヤーセットをすべて可視状態にする。
    n = activeDocument.artLayers.length;
    for (i=0;i<n;i++){
        activeDocument.artLayers[i]=true;
     }
}

function mppLayerToAlpha(aName){//指定レイヤーセットの透明情報をαチャンネルに上書き
//aName="_na";

// 可視化=======================================================
var idShw = charIDToTypeID( "Shw " );
var desc105 = new ActionDescriptor();
var idnull = charIDToTypeID( "null" );
var list27 = new ActionList();
var ref100 = new ActionReference();
var idLyr = charIDToTypeID( "Lyr " );
ref100.putName( idLyr, aName );
list27.putReference( ref100 );
desc105.putList( idnull, list27 );
executeAction( idShw, desc105, DialogModes.NO );

//選択 =======================================================
var idslct = charIDToTypeID( "slct" );
var desc135 = new ActionDescriptor();
var idnull = charIDToTypeID( "null" );
var ref115 = new ActionReference();
var idLyr = charIDToTypeID( "Lyr " );
ref115.putName( idLyr, aName );
desc135.putReference( idnull, ref115 );
var idMkVs = charIDToTypeID( "MkVs" );
desc135.putBoolean( idMkVs, false );
executeAction( idslct, desc135, DialogModes.NO );

//マージ=======================================================
lsObj = activeDocument.layerSets[aName];
lsObj.merge();

// マージしたレイヤーを選択=======================================================
var idslct = charIDToTypeID( "slct" );
var desc108 = new ActionDescriptor();
var idnull = charIDToTypeID( "null" );
var ref104 = new ActionReference();
var idLyr = charIDToTypeID( "Lyr " );
ref104.putName( idLyr, aName );
desc108.putReference( idnull, ref104 );
var idMkVs = charIDToTypeID( "MkVs" );
desc108.putBoolean( idMkVs, false );
executeAction( idslct, desc108, DialogModes.NO );

// レイヤーの透明度を選択範囲=======================================================
var idsetd = charIDToTypeID( "setd" );
var desc109 = new ActionDescriptor();
var idnull = charIDToTypeID( "null" );
var ref105 = new ActionReference();
var idChnl = charIDToTypeID( "Chnl" );
var idfsel = charIDToTypeID( "fsel" );
ref105.putProperty( idChnl, idfsel );
desc109.putReference( idnull, ref105 );
var idT = charIDToTypeID( "T   " );
var ref106 = new ActionReference();
var idChnl = charIDToTypeID( "Chnl" );
var idChnl = charIDToTypeID( "Chnl" );
var idTrsp = charIDToTypeID( "Trsp" );
ref106.putEnumerated( idChnl, idChnl, idTrsp );
desc109.putReference( idT, ref106 );
executeAction( idsetd, desc109, DialogModes.NO );

// 選択範囲をコピー=======================================================
var idcopy = charIDToTypeID( "copy" );
executeAction( idcopy, undefined, DialogModes.NO );

// レイヤー削除=======================================================
activeDocument.layers[aName].remove();

// αチャンネルを追加=======================================================
try{
    activeDocument.Channels[3];
    }
catch(e){
    activeDocument.channels.add();
}

// ペースト=======================================================
var idpast = charIDToTypeID( "past" );
var desc115 = new ActionDescriptor();
var idAntA = charIDToTypeID( "AntA" );
var idAnnt = charIDToTypeID( "Annt" );
var idAnno = charIDToTypeID( "Anno" );
desc115.putEnumerated( idAntA, idAnnt, idAnno );
executeAction( idpast, desc115, DialogModes.NO );

//RGBチャンネルをアクティブに =======================================================
var idslct = charIDToTypeID( "slct" );
var desc159 = new ActionDescriptor();
var idnull = charIDToTypeID( "null" );
var ref128 = new ActionReference();
var idChnl = charIDToTypeID( "Chnl" );
var idChnl = charIDToTypeID( "Chnl" );
var idRGB = charIDToTypeID( "RGB " );
ref128.putEnumerated( idChnl, idChnl, idRGB );
desc159.putReference( idnull, ref128 );
executeAction( idslct, desc159, DialogModes.NO );

//全部マージ=======================================================
activeDocument.activeLayer.merge();
}