function mppNewDocument(){
    this.SRC="";
    this.DST="";
    this.LNAME="";
    this.TEMP="MS_temp_zzzz";
}    


mppNewDocument.prototype.copySelection=function(){//ドキュメント（SRC）から選択レイヤー（LNAME）の選択範囲をコピー
    // =======================================================
        try{
            var idsetd = charIDToTypeID( "setd" );
            var desc15 = new ActionDescriptor();
            var idnull = charIDToTypeID( "null" );
            var ref16 = new ActionReference();
            var idChnl = charIDToTypeID( "Chnl" );
            var idfsel = charIDToTypeID( "fsel" );
            ref16.putProperty( idChnl, idfsel );
            desc15.putReference( idnull, ref16 );
            var idT = charIDToTypeID( "T   " );
            var ref17 = new ActionReference();
            var idChnl = charIDToTypeID( "Chnl" );
            var idChnl = charIDToTypeID( "Chnl" );
            var idTrsp = charIDToTypeID( "Trsp" );
            ref17.putEnumerated( idChnl, idChnl, idTrsp );
            var idLyr = charIDToTypeID( "Lyr " );
            ref17.putName( idLyr, this.LNAME );
            var idDcmn = charIDToTypeID( "Dcmn" );
            ref17.putName( idDcmn, this.SRC );
            desc15.putReference( idT, ref17 );
            executeAction( idsetd, desc15, DialogModes.NO );
        }
        catch(e){
            activeDocument.selection.selectAll();
        }
    }

mppNewDocument.prototype.copySelectionFromSelected=function(){//選択済み選択範囲を別ドキュメントにコピー。SRC：選択範囲のあるドキュメント。DST：選択範囲を読み込ませるドキュメント。TEMP：選択範囲を一時保存するためのレイヤー
        activeDocument=documents[this.SRC];
        layObj = activeDocument.artLayers.add();
        layObj.name=this.TEMP;
        //paintWhite
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
        //
        activeDocument=documents[this.DST];
        
        var MPP = new mppNewDocument;
        MPP.copySelection(this.SRC,this.TEMP);
        
        activeDocument=documents[this.SRC];
        layObj.remove();
        activeDocument=documents[this.DST];
    }



mppNewDocument.prototype.mppDocument2=function(){//ドキュメント検索OR新規作成

    w = activeDocument.width;
    h = activeDocument.height;    

    try{
        activeDocument=documents[this.DST];
    }
    catch(e){
        // 新規ドキュメント作成=======================================================
        documents.add(w,h,72,this.DST);
    }
}
