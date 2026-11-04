
function CreateControlRect(STR){
    layObj = activeDocument.artLayers.add();
    layObj.name =STR;
    drawRect();
}



function CreateControlText(){
    layObj = activeDocument.artLayers.add();
    layObj.kind=LayerKind.TEXT
    layObj.textItem.font='MS-Gothic';
    layObj.textItem.fontSize=12;
    layObj.textItem.contents = 'textLabel';
    //drawRect();
}





function drawRect(){
    RGBColor = new SolidColor();
    RGBColor.red = 232;
    RGBColor.green = 232;
    RGBColor.blue = 232;
    rect=[16,16,48,144];
    selReg = [
    [rect[0],rect[1]]
    ,[rect[3],rect[0]]
    ,[rect[3],rect[2]]
    ,[rect[0],rect[2]]
    ];
    activeDocument.selection.select(selReg);
    activeDocument.selection.fill(RGBColor,ColorBlendMode.NORMAL, 100, false);    
        

    // =======================================================
    var idsetd = charIDToTypeID( "setd" );
        var desc34 = new ActionDescriptor();
        var idnull = charIDToTypeID( "null" );
            var ref26 = new ActionReference();
            var idPrpr = charIDToTypeID( "Prpr" );
            var idLefx = charIDToTypeID( "Lefx" );
            ref26.putProperty( idPrpr, idLefx );
            var idLyr = charIDToTypeID( "Lyr " );
            var idOrdn = charIDToTypeID( "Ordn" );
            var idTrgt = charIDToTypeID( "Trgt" );
            ref26.putEnumerated( idLyr, idOrdn, idTrgt );
        desc34.putReference( idnull, ref26 );
        var idT = charIDToTypeID( "T   " );
            var desc35 = new ActionDescriptor();
            var idScl = charIDToTypeID( "Scl " );
            var idPrc = charIDToTypeID( "#Prc" );
            desc35.putUnitDouble( idScl, idPrc, 100.000000 );
            var idFrFX = charIDToTypeID( "FrFX" );
                var desc36 = new ActionDescriptor();
                var idenab = charIDToTypeID( "enab" );
                desc36.putBoolean( idenab, true );
                var idStyl = charIDToTypeID( "Styl" );
                var idFStl = charIDToTypeID( "FStl" );
                var idOutF = charIDToTypeID( "OutF" );
                desc36.putEnumerated( idStyl, idFStl, idOutF );
                var idPntT = charIDToTypeID( "PntT" );
                var idFrFl = charIDToTypeID( "FrFl" );
                var idSClr = charIDToTypeID( "SClr" );
                desc36.putEnumerated( idPntT, idFrFl, idSClr );
                var idMd = charIDToTypeID( "Md  " );
                var idBlnM = charIDToTypeID( "BlnM" );
                var idNrml = charIDToTypeID( "Nrml" );
                desc36.putEnumerated( idMd, idBlnM, idNrml );
                var idOpct = charIDToTypeID( "Opct" );
                var idPrc = charIDToTypeID( "#Prc" );
                desc36.putUnitDouble( idOpct, idPrc, 100.000000 );
                var idSz = charIDToTypeID( "Sz  " );
                var idPxl = charIDToTypeID( "#Pxl" );
                desc36.putUnitDouble( idSz, idPxl, 1.000000 );
                var idClr = charIDToTypeID( "Clr " );
                    var desc37 = new ActionDescriptor();
                    var idRd = charIDToTypeID( "Rd  " );
                    desc37.putDouble( idRd, 0.000000 );
                    var idGrn = charIDToTypeID( "Grn " );
                    desc37.putDouble( idGrn, 0.000000 );
                    var idBl = charIDToTypeID( "Bl  " );
                    desc37.putDouble( idBl, 0.000000 );
                var idRGBC = charIDToTypeID( "RGBC" );
                desc36.putObject( idClr, idRGBC, desc37 );
            var idFrFX = charIDToTypeID( "FrFX" );
            desc35.putObject( idFrFX, idFrFX, desc36 );
        var idLefx = charIDToTypeID( "Lefx" );
        desc34.putObject( idT, idLefx, desc35 );
    executeAction( idsetd, desc34, DialogModes.NO );
}


