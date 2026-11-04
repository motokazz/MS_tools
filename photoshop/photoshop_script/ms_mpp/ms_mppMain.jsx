//@include "ms_mppPaint.jsx"
//@include "ms_mppNewDocument.jsx"
//@include "ms_modChannel.jsx"
//@include "ms_modPaint.jsx"

preferences.rulerUnits = Units.PIXELS;

function doc_a(){
    this.aDoc=activeDocument.name;
    //
    docName=aDoc.split(".");
    this.ADNAME=docName[0];
    this.ADEXT=docName[1];
    //
    this.OPTION="";//成分名　c、s、n
}

doc_a.prototype.createNew=function(){
    var MPP = new mppNewDocument;
    MPP.SRC=this.aDoc;
    
    var modC = new modChannel;
    
    var modP = new modPaint;      
    
    MPP.DST=this.ADNAME+"_"+this.OPTION+"."+docName[1]
    MPP.mppDocument2();
    
    //
    MPP.copySelectionFromSelected();
    //
    modC.selectRGBChannel();
    modP.paintPattern("MS_temp_"+this.OPTION);
    modC.addAlphaChannel();
    modP.paintPattern("MS_temp_"+this.OPTION+"a");
    modC.selectRGBChannel();
}




function mppMain(){
    try{
    aDoc=activeDocument.name;
    alayer=activeDocument.activeLayer.name;
    }
    catch(e){
        alert("Error NoDcument!");
       exit();
       }
   
    var MPP = new mppPaint;
    MPP.importPatternFromFile();
    
    var DOC = new doc_a;
    
    //_c
    DOC.OPTION = "c";
    DOC.createNew();
    
    //_s
    DOC.OPTION = "s";
    DOC.createNew();
    
    //_n
    DOC.OPTION = "n";
    DOC.createNew();
    
    //post
    MPP.clearPattern();
    
    activeDocument=documents[DOC.aDoc];

}




