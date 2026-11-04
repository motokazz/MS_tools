//msg2_newActionPlacer.jsx
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
    n = activeDocument.layerSets.length;
    i=0;
    for (i=0;i<n;i++){
        layName = activeDocument.layerSets[i].name;
        if (layName == "gravity2_color"){
            return i;
            }
        }
    return false;
}

function deleteOldAction(){
    while(layerSetsExists("gravity2_color")){
        lsObj = activeDocument.layerSets["gravity2_color"];
        lsObj.remove();
    }
    while(layerSetsExists("gravity2_texture")){
        lsObj = activeDocument.layerSets["gravity2_texture"];
        lsObj.remove();
    }
}

function layerSetsExists(lsName){
    layObj = activeDocument.layerSets;
    flag = true;
    try{
        n = layObj[lsName];
    }
    catch(e){
        flag = false;
    }
    return flag;
}


function checkAdjustment(){
    //adjustmentを確認
    n = activeDocument.layerSets.length;
    i=0;
    for (i=0;i<n;i++){
        layName = activeDocument.layerSets[i].name;
        if (layName == "adjustment"){
            return true;
            }
        }
    return false;
}


function checkAdjustmentVisible(){
    lsObj = activeDocument.layerSets["adjustment"];
    return lsObj.visible;
}

function adjustmentToTop(){
layers = activeDocument.layers;
lsObj = activeDocument.layerSets["adjustment"];
index=0;
lsObj.move(layers[0],ElementPlacement.PLACEBEFORE);
}

function visibleAdjustment(visible){
    lsObj = activeDocument.layerSets["adjustment"];
    lsObj.visible = visible;
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



function saveNew(path){
    var fileobj = new File(path);
    var saveOptions = new TiffSaveOptions;
    saveOptions.imageCompression = TIFFEncoding.NONE;
    activeDocument.saveAs(fileobj, saveOptions, false, Extension.LOWERCASE)
    //activeDocument.saveAs(fileobj);
}

function checkLayerNum(){
    ln=activeDocument.layerSets.length;
    if (ln<1){
        n = activeDocument.layers.length;
        if (n<=1){
            LS=activeDocument.layerSets.add();
            AL=activeDocument.artLayers[0].duplicate();
            LS.name="base";
            AL.moveToEnd(LS);
        }
    }
}

function main(){
    ln=activeDocument.layers.length;
    activeDocument.activeLayer=activeDocument.layers[ln-1];
    dname=checkDocumentName();
    cdk=checkKind(dname);
    adjExists=checkAdjustment();
    
    if (adjExists){
        adjv=checkAdjustmentVisible();
        visibleAdjustment(false);
    }
    
    //alert(dname);
    if(cdk=="c"){//カラーテクスチャだったら
        if(!checkNewAction()){//新しいアクションじゃなかったら
            if( layerSetsExists("gravity2_color") || layerSetsExists("gravity2_texture") ){//古いアクションが使われてたら
                //古いアクションを消して
                deleteOldAction();
                
                //背景だけだったら何とかして
                checkLayerNum();
                
                //新しいアクションを実行して
                doG2_color_force10();
                //adjustmentを一番上にして
                if (adjExists){
                    adjustmentToTop();
                    visibleAdjustment(adjv);
                 }
                //指定フォルダに保存して閉じる
                saveNew("d:/work/checkTexPlaced/"+dname);
                activeDocument.close();
            }
                
        }
    }
}

main();
