//msg2_checkTexture.jsx
function checkDocumentName(){
    dname = activeDocument.name;
    return dname;
}

function checkpath(){
    fPath = activeDocument.fullName;
    return fPath
}

function checkKind(dname){
    ret="";
    if (dname.match(/_c\./i)) {
        ret="c";
    }
    return ret;
}

//checkG2Action
function checkNewAction(){
    //新しいアクションを確認
    n = activeDocument.layerSets.length;
    i=0;
    for (i=0;i<n;i++){
        layName = activeDocument.layerSets[i].name;
        if (layName == "G2_Project_color"){
            return true;
            }
        }
    return false;
}

function checkOldAction(){
    //古いアクションを確認
    var ret=-1;
    n = activeDocument.layerSets.length;
    i=0;
    for (i=0;i<n;i++){
        layName = activeDocument.layerSets[i].name;
        if (layName == "gravity2_color"){
            ret=i;
            }
        }
    return ret;
}


//Util
function copy(srcFilename,dstFilename){
srcFileObj = new File(srcFilename);
dstFileObj = new File(dstFilename);
srcFileObj.copy(dstFileObj);
}


//main
function main(){
    dname=checkDocumentName();
    cdk=checkKind(dname);
    if(cdk=="c"){
        if(!checkNewAction()){
            src=checkpath ();
            dst="d:/work/checkTexture/"+dname;
            copy (src, dst);
            }
        }
    activeDocument.close(SaveOptions.DONOTSAVECHANGES);
}


main();
