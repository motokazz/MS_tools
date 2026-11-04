
function modDocument(){
    
    }


modDocument.prototype.createDocument=function(DNAME){//ドキュメント検索OR新規作成

    w = activeDocument.width;
    h = activeDocument.height;    

    try{
        activeDocument=documents[DNAME];
    }
    catch(e){
        // 新規ドキュメント作成=======================================================
        documents.add(w,h,72,DNAME);
    }
}
