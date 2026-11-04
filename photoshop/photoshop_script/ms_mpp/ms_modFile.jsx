// =======================================================
//ms_modFile.jsx
// =======================================================
// =======================================================
function modFile(){
    this.FILENAME="";

}

modFile.prototype.fileExists=function (){//ファイル存在確認
    fileObj = new File(this.FILENAME);
    if(fileObj.exists){
        return true;
    }else{
        return false;
    }
    //return fileObj.exists;    
}
// =======================================================
modFile.prototype.fileOpen=function(){//ファイルを開く
    fileObj = new File(this.FILENAME);
    open(fileObj);
}

// =======================================================
modFile.prototype.fileDialog=function(){//ファイル指定ダイアログ
    filename = File.openDialog("開く画像ファイルを指定してください");
    if (filename){
        this.FILENAME=filename;
    }  
}

// =======================================================
modFile.prototype.closeDocument=function(){//ドキュメントを閉じる
    activeDocument.close(SaveOptions.DONOTSAVECHANGES);
}
// =======================================================
// name
// =======================================================
modFile.prototype.imageNameConversion=function(){//ファイル名を命名規則に合わせたリストにして返す
    var renamed=new String();
    STR=new String(this.FILENAME);
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
