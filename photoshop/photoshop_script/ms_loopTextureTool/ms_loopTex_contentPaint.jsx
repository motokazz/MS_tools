//ms_loopTex_contentPaint.jsx


function loopTexCP(){
    this.beltSize=0.5;
    this.featherSize=0.0;
}

loopTexCP.prototype.checkSelection = function checkSelection(){
    var flag = true;
    try {
        activeDocument.selection.translate(0,0);
    }catch(e){
        flag = false;
    }
    return flag;
}

loopTexCP.prototype.copyToNewDocument=function(){

// =======================================================
var idcopy = charIDToTypeID( "copy" );
executeAction( idcopy, undefined, DialogModes.NO );

// =======================================================
var idMk = charIDToTypeID( "Mk  " );
    var desc10 = new ActionDescriptor();
    var idNw = charIDToTypeID( "Nw  " );
        var desc11 = new ActionDescriptor();
        var idpreset = stringIDToTypeID( "preset" );
        desc11.putString( idpreset, "クリップボード" );
    var idDcmn = charIDToTypeID( "Dcmn" );
    desc10.putObject( idNw, idDcmn, desc11 );
executeAction( idMk, desc10, DialogModes.NO );

// =======================================================
var idpast = charIDToTypeID( "past" );
    var desc12 = new ActionDescriptor();
    var idAntA = charIDToTypeID( "AntA" );
    var idAnnt = charIDToTypeID( "Annt" );
    var idAnno = charIDToTypeID( "Anno" );
    desc12.putEnumerated( idAntA, idAnnt, idAnno );
executeAction( idpast, desc12, DialogModes.NO );

}

loopTexCP.prototype.paintContent = function(){
    // =======================================================
    var idFl = charIDToTypeID( "Fl  " );
    var desc104 = new ActionDescriptor();
    var idUsng = charIDToTypeID( "Usng" );
    var idFlCn = charIDToTypeID( "FlCn" );
    var idcontentAware = stringIDToTypeID( "contentAware" );
    desc104.putEnumerated( idUsng, idFlCn, idcontentAware );
    var idOpct = charIDToTypeID( "Opct" );
    var idPrc = charIDToTypeID( "#Prc" );
    desc104.putUnitDouble( idOpct, idPrc, 100.000000 );
    var idMd = charIDToTypeID( "Md  " );
    var idBlnM = charIDToTypeID( "BlnM" );
    var idNrml = charIDToTypeID( "Nrml" );
    desc104.putEnumerated( idMd, idBlnM, idNrml );
    executeAction( idFl, desc104, DialogModes.NO );
}

loopTexCP.prototype.main = function(){
    if(!this.checkSelection()){
        activeDocument.selection.selectAll();
    }
    this.copyToNewDocument();
    //
    aDoc=activeDocument;
    w = aDoc.width;
    h = aDoc.height;
    wa=w*(0.5-(this.beltSize*0.5));
    wb=w*(0.5+(this.beltSize*0.5));
    ha=h*(0.5-(this.beltSize*0.5));
    hb=h*(0.5+(this.beltSize*0.5));
    
    fs=((wb-wa)*this.featherSize);
    sel=aDoc.selection;
    
    //v
    aDoc.activeLayer.applyOffset(w*0.5,0,OffsetUndefinedAreas.WRAPAROUND);
    selReg=[[wa,0],[wb,0],[wb,h],[wa,h]];
    sel.select(selReg);
    sel.feather (fs);
    this.paintContent();
    sel.deselect();
    
    //h
    aDoc.activeLayer.applyOffset(0,h*0.5,OffsetUndefinedAreas.WRAPAROUND);
    selReg=[[0,ha],[w,ha],[w,hb],[0,hb]];
    sel.select(selReg);
    sel.feather (fs);
    this.paintContent();
    sel.deselect();
    
    //vh
    aDoc.activeLayer.applyOffset(w*0.5,0,OffsetUndefinedAreas.WRAPAROUND);
    selReg=[[wa,ha],[wb,ha],[wb,hb],[wa,hb]];
    sel.select(selReg);
    sel.feather (fs);
    this.paintContent();
    sel.deselect();
    
    //
    aDoc.activeLayer.applyOffset(0,h*0.5,OffsetUndefinedAreas.WRAPAROUND);
    sel.deselect();

}

//aDoc.selection.resizeBoundary(selReg);



//LTCP=new loopTexCP;
//LTCP.main();




