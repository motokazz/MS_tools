
function enableFX(BOOL){
    // レイヤー効果のON・OFF
    try{
        if (BOOL){
                // =======================================================
            var idShw = charIDToTypeID( "Shw " );
                var desc69 = new ActionDescriptor();
                var idnull = charIDToTypeID( "null" );
                    var list10 = new ActionList();
                        var ref69 = new ActionReference();
                        var idLefx = charIDToTypeID( "Lefx" );
                        ref69.putClass( idLefx );
                        var idLyr = charIDToTypeID( "Lyr " );
                        ref69.putName( idLyr, "panelimg" );
                    list10.putReference( ref69 );
                desc69.putList( idnull, list10 );
            executeAction( idShw, desc69, DialogModes.NO );

        }
        else{
            var idHd = charIDToTypeID( "Hd  " );
                var descX = new ActionDescriptor();
                var idnull = charIDToTypeID( "null" );
                    var list9 = new ActionList();
                        var refX = new ActionReference();
                        var idLefx = charIDToTypeID( "Lefx" );
                        refX.putClass( idLefx );
                        var idLyr = charIDToTypeID( "Lyr " );
                        refX.putName( idLyr, "panelimg" );
                    list9.putReference( refX );
                descX.putList( idnull, list9 );
            executeAction( idHd, descX, DialogModes.NO );
        }
    }
    catch(e){
        return;
    }
}



obj=activeDocument.activeLayer;

enableFX(false);

B=obj.bounds;
selReg=[
    [B[0],B[1]]
    ,[B[2],B[1]]
    ,[B[2],B[3]]
    ,[B[0],B[3]]
];

activeDocument.selection.select(selReg);
