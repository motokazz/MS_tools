
// 色設定１=======================================================
var idsetd = charIDToTypeID( "setd" );
    var desc53 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
        var ref28 = new ActionReference();
        var idClr = charIDToTypeID( "Clr " );
        var idFrgC = charIDToTypeID( "FrgC" );
        ref28.putProperty( idClr, idFrgC );
    desc53.putReference( idnull, ref28 );
    var idT = charIDToTypeID( "T   " );
        var desc54 = new ActionDescriptor();
        var idRd = charIDToTypeID( "Rd  " );
        desc54.putDouble( idRd, 73.003891 );
        var idGrn = charIDToTypeID( "Grn " );
        desc54.putDouble( idGrn, 76.000000 );
        var idBl = charIDToTypeID( "Bl  " );
        desc54.putDouble( idBl, 73.003891 );
    var idRGBC = charIDToTypeID( "RGBC" );
    desc53.putObject( idT, idRGBC, desc54 );
    var idSrce = charIDToTypeID( "Srce" );
    desc53.putString( idSrce, """photoshopPicker""" );
executeAction( idsetd, desc53, DialogModes.NO );

// 色設定２=======================================================
var idsetd = charIDToTypeID( "setd" );
    var desc55 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
        var ref29 = new ActionReference();
        var idClr = charIDToTypeID( "Clr " );
        var idBckC = charIDToTypeID( "BckC" );
        ref29.putProperty( idClr, idBckC );
    desc55.putReference( idnull, ref29 );
    var idT = charIDToTypeID( "T   " );
        var desc56 = new ActionDescriptor();
        var idRd = charIDToTypeID( "Rd  " );
        desc56.putDouble( idRd, 60.000000 );
        var idGrn = charIDToTypeID( "Grn " );
        desc56.putDouble( idGrn, 60.000000 );
        var idBl = charIDToTypeID( "Bl  " );
        desc56.putDouble( idBl, 60.000000 );
    var idRGBC = charIDToTypeID( "RGBC" );
    desc55.putObject( idT, idRGBC, desc56 );
    var idSrce = charIDToTypeID( "Srce" );
    desc55.putString( idSrce, """photoshopPicker""" );
executeAction( idsetd, desc55, DialogModes.NO );

// 描画雲模様１=======================================================
var idClds = charIDToTypeID( "Clds" );
    var desc57 = new ActionDescriptor();
executeAction( idClds, desc57, DialogModes.NO );

// スポンジ=======================================================
var idGEfc = charIDToTypeID( "GEfc" );
    var desc58 = new ActionDescriptor();
    var idGEfk = charIDToTypeID( "GEfk" );
    var idGEft = charIDToTypeID( "GEft" );
    var idSpng = charIDToTypeID( "Spng" );
    desc58.putEnumerated( idGEfk, idGEft, idSpng );
    var idBrsS = charIDToTypeID( "BrsS" );
    desc58.putInteger( idBrsS, 0 );
    var idDfnt = charIDToTypeID( "Dfnt" );
    desc58.putInteger( idDfnt, 0 );
    var idSmth = charIDToTypeID( "Smth" );
    desc58.putInteger( idSmth, 1 );
executeAction( idGEfc, desc58, DialogModes.NO );

