function modChannel(){
     this.A="";
     this.reflesh();
}

modChannel.prototype.addAlphaChannel=function(){//アルファチャンネルを選択OR追加
    // αチャンネルを追加=======================================================
    try{
        this.selectAlphaChannel();
    }
    catch(e){
        activeDocument.channels.add();
    }
}

modChannel.prototype.selectRGBChannel=function(){//RGBチャンネルを選択
// =======================================================
    var idslct = charIDToTypeID( "slct" );
    var desc174 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
    var ref171 = new ActionReference();
    var idChnl = charIDToTypeID( "Chnl" );
    var idChnl = charIDToTypeID( "Chnl" );
    var idRGB = charIDToTypeID( "RGB " );
    ref171.putEnumerated( idChnl, idChnl, idRGB );
    desc174.putReference( idnull, ref171 );
    executeAction( idslct, desc174, DialogModes.NO );
}

modChannel.prototype.selectAlphaChannel=function(){//アルファチャンネルを選択
    ACH_NAME=activeDocument.channels[3].name;
// =======================================================
    var idslct = charIDToTypeID( "slct" );
    var desc175 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
    var ref172 = new ActionReference();
    var idChnl = charIDToTypeID( "Chnl" );
    ref172.putName( idChnl, ACH_NAME);
    desc175.putReference( idnull, ref172 );
    executeAction( idslct, desc175, DialogModes.NO );
}

modChannel.prototype.reflesh=function(){//クラスのリフレッシュ
    try{
        this.A=activeDocument.channels[3].name;
    }
    catch(e){
        this.A="";
    }
}



