//ペイント関連モジュール

//@include "ms_modChannel.jsx"

//pattern
// =======================================================

function modPaint(){
    this.NAME = "";
}


// =======================================================
modPaint.prototype.registrationPattern = function(PATTERNNAME){//RGBチャンネルをパターンとして登録する
    
// ==========
// 登録する
//http://blog.sakurachiro.com/2009/11/add-pattern/
// ==========
    var idMk = charIDToTypeID( "Mk  " );
    var desc1 = new ActionDescriptor();
    var idNull = charIDToTypeID( "null" );
    var ref1 = new ActionReference();
    var myPtrn = charIDToTypeID( "Ptrn" );
    ref1.putClass( myPtrn );
    desc1.putReference( idNull, ref1 );
    var idUsng = charIDToTypeID( "Usng" );
    var ref2 = new ActionReference();
    var idPrpr = charIDToTypeID( "Prpr" );
    var idFsel = charIDToTypeID( "fsel" );
    ref2.putProperty( idPrpr, idFsel );
    var idDcmn = charIDToTypeID( "Dcmn" );
    var idOrdn = charIDToTypeID( "Ordn" );
    var idTrgt = charIDToTypeID( "Trgt" );
    ref2.putEnumerated( idDcmn, idOrdn, idTrgt );
    desc1.putReference( idUsng, ref2 );
    var idNm = charIDToTypeID( "Nm  " );
    var docName = app.activeDocument.name;
    desc1.putString( idNm, PATTERNNAME );
    executeAction( idMk, desc1, DialogModes.NO );
}
// =======================================================
modPaint.prototype.registrationPatternAlpha = function(PATTERNNAME){//αチャンネルをパターンとして登録する
    var modC = new modChannel;
    try{
        modC.selectAlphaChannel();
        this.registrationPattern(PATTERNNAME);
    }
    catch(e){
        this.registrationPatternWhite(PATTERNNAME);
    }
}
// =======================================================
modPaint.prototype.registrationPatternWhite = function(PATTERNNAME){//ホワイトをパターンとして登録する
    this.paintWhite();
    this.registrationPattern(PATTERNNAME);
}

// =======================================================
modPaint.prototype.deletePattern = function(PATTERNNAME){//パターンを消去する
    while(true){
        try{
            var idDlt = charIDToTypeID( "Dlt " );
            var desc9 = new ActionDescriptor();
            var idnull = charIDToTypeID( "null" );
            var list5 = new ActionList();
            var ref5 = new ActionReference();
            var idPtrn = charIDToTypeID( "Ptrn" );
            ref5.putIndex( idPtrn, 18 );
            list5.putReference( ref5 );
            desc9.putList( idnull, list5 );
            var idNm = charIDToTypeID( "Nm  " );
            desc9.putString( idNm, PATTERNNAME );
            executeAction( idDlt, desc9, DialogModes.NO );
        }catch(e){
            break;
        }
    }
}
// =======================================================
modPaint.prototype.paintPattern = function(PATTERNNAME){//パターンで塗る
    // =======================================================
    var idFl = charIDToTypeID( "Fl  " );
    var desc393 = new ActionDescriptor();
    var idUsng = charIDToTypeID( "Usng" );
    var idFlCn = charIDToTypeID( "FlCn" );
    var idPtrn = charIDToTypeID( "Ptrn" );
    desc393.putEnumerated( idUsng, idFlCn, idPtrn );
    var idPtrn = charIDToTypeID( "Ptrn" );
    var desc394 = new ActionDescriptor();
    var idNm = charIDToTypeID( "Nm  " );
    desc394.putString( idNm, PATTERNNAME );
    var idIdnt = charIDToTypeID( "Idnt" );
    desc394.putString( idIdnt, "a144ed60-3a1f-11e3-ac4c-ef478bd1fcf8" );
    var idPtrn = charIDToTypeID( "Ptrn" );
    desc393.putObject( idPtrn, idPtrn, desc394 );
    var idOpct = charIDToTypeID( "Opct" );
    var idPrc = charIDToTypeID( "#Prc" );
    desc393.putUnitDouble( idOpct, idPrc, 100.000000 );
    var idMd = charIDToTypeID( "Md  " );
    var idBlnM = charIDToTypeID( "BlnM" );
    var idNrml = charIDToTypeID( "Nrml" );
    desc393.putEnumerated( idMd, idBlnM, idNrml );
    executeAction( idFl, desc393, DialogModes.NO );
}

// =======================================================
modPaint.prototype.paintWhite = function(){//ホワイトで塗る
    var idFl = charIDToTypeID( "Fl  " );
    var desc3 = new ActionDescriptor();
    var idUsng = charIDToTypeID( "Usng" );
    var idFlCn = charIDToTypeID( "FlCn" );
    var idWht = charIDToTypeID( "Wht " );
    desc3.putEnumerated( idUsng, idFlCn, idWht );
    var idOpct = charIDToTypeID( "Opct" );
    var idPrc = charIDToTypeID( "#Prc" );
    desc3.putUnitDouble( idOpct, idPrc, 100.000000 );
    var idMd = charIDToTypeID( "Md  " );
    var idBlnM = charIDToTypeID( "BlnM" );
    var idNrml = charIDToTypeID( "Nrml" );
    desc3.putEnumerated( idMd, idBlnM, idNrml );
    executeAction( idFl, desc3, DialogModes.NO );
}
