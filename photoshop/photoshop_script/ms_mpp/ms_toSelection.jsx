//レイヤーセット、もしくは、選択レイヤーすべてを選択範囲化

function toSelection(){
    this.aDoc=activeDocument;
    this.TEMP="MS_TEMP_TO_SELECTION";
}

toSelection.prototype.asd = function(){
    LS=activeDocument.activeLayer;
    LB=activeDocument.artLayers;
    var layerSetRef = this.aDoc.layerSets.add();
    LS.duplicate(layerSetRef, ElementPlacement.PLACEATEND);
    var temp="catch"
    alert(LB);
}


AAA=new toSelection;
AAA.asd();











