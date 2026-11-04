//msg2_action_checker.jsx
function checkDocumentName(){
    dname = activeDocument.name;
    return dname;
}

function checkNewAction(){
    //新しいアクションを確認
    //var ret=false;
    n = activeDocument.layerSets.length;
    i=0;
    for (i=0;i<n;i++){
        layName = activeDocument.layerSets[i].name;
        if (layName == "G2_Project_color"){
            //alert("old action found"+layName+".");
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
            //alert("old action found"+layName+".");
            ret=i;
            }
        }
    return ret;
}

function deleteOldAction(){
        oldAction = checkOldAction();
        alert (oldAction);
        if (oldAction>=0){
            activeDocument.layerSets[oldAction].remove();
            doG2_color_force10();
        }
}


//
function doG2_color_force10(){
    // =======================================================
    var idPly = charIDToTypeID( "Ply " );
        var desc23 = new ActionDescriptor();
        var idnull = charIDToTypeID( "null" );
            var ref18 = new ActionReference();
            var idActn = charIDToTypeID( "Actn" );
            ref18.putName( idActn, "G2_color_force10" );
            var idASet = charIDToTypeID( "ASet" );
            ref18.putName( idASet, "G2_texture" );
        desc23.putReference( idnull, ref18 );
    executeAction( idPly, desc23, DialogModes.NO );
}

function doG2_color(){
    // =======================================================
    var idPly = charIDToTypeID( "Ply " );
        var desc23 = new ActionDescriptor();
        var idnull = charIDToTypeID( "null" );
            var ref18 = new ActionReference();
            var idActn = charIDToTypeID( "Actn" );
            ref18.putName( idActn, "G2_color_force10" );
            var idASet = charIDToTypeID( "ASet" );
            ref18.putName( idASet, "G2_texture" );
        desc23.putReference( idnull, ref18 );
    executeAction( idPly, desc23, DialogModes.NO );
}

//

function checkKind(dname){
    ret="";
    if (dname.match(/_c\./i)) {
        ret="c";
    }
    return ret;
}


function checkpath(){
    fPath = activeDocument.fullName;
    alert(fPath);
    return fPath
}

function copy(srcFilename,dstFilename){
srcFileObj = new File(srcFilename);
dstFileObj = new File(dstFilename);
srcFileObj.copy(dstFileObj);
}


function createNewPath(fName){
    return "d:/work/"+fName
}

function main(){
    dname=checkDocumentName();
    cdk=checkKind(dname);
    //alert(dname);
    if(cdk=="c"){
        if(!checkNewAction()){
            src=checkpath ();
            dst="d:/work/oldtexture/"+dname;
            copy (src, dst);
                alert("old");
            }
                
        }
}

main();
