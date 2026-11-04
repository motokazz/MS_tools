// =======================================================
//D:\Mproject\gtools\photoshop\scripts\ms_multiPathPaint.jsx
//ファイルの命名規則に従いパターンを読み込む
//読み込んだパターンをペイントする
// =======================================================
//document
// =======================================================
//@include "ms_modChannel.jsx"
//@include "ms_modFile.jsx"
//@include "ms_modPaint.jsx"
//@include "ms_modLayer.jsx"



function mppPaint(){
    this.NAME='';
}

// =======================================================
mppPaint.prototype.patternName = function(){//成分別パターン登録
    var modP = new modPaint;
    STR=new String(this.NAME);
    if (STR.match(/_c\./)){modP.registrationPattern("MS_temp_c");modP.registrationPatternWhite("MS_temp_ca");}
    if (STR.match(/_ca\./)){modP.registrationPattern("MS_temp_c");modP.registrationPatternAlpha("MS_temp_ca");}
    if (STR.match(/_n\./)){modP.registrationPattern("MS_temp_n");modP.registrationPatternWhite("MS_temp_na");}
    if (STR.match(/_na\./)){modP.registrationPattern("MS_temp_n");modP.registrationPatternAlpha("MS_temp_na");}
    if (STR.match(/_s\./)){modP.registrationPattern("MS_temp_s");modP.registrationPatternWhite("MS_temp_sa");}
    if (STR.match(/_sa\./)){modP.registrationPattern("MS_temp_s");modP.registrationPatternAlpha("MS_temp_sa");}
}
// =======================================================
mppPaint.prototype.clearPattern = function(){//パターンをクリア
    var modP = new modPaint;
    modP.deletePattern("MS_temp_c");
    modP.deletePattern("MS_temp_ca");
    modP.deletePattern("MS_temp_n");
    modP.deletePattern("MS_temp_na");
    modP.deletePattern("MS_temp_s");
    modP.deletePattern("MS_temp_sa");
}
// =======================================================
mppPaint.prototype.importPatternFromFile = function(){//ファイルから成分別パターンをインポート
    this.clearPattern();
    var modF = new modFile;
    var modL=new modLayer;
    modF.fileDialog();
    var rowFileName=modF.imageNameConversion();
    for (var i=0;i<rowFileName.length;i++){
        modF.FILENAME=rowFileName[i];
        if (modF.fileExists()){
            modF.fileOpen();
            modL.mergeVisibleLayers ();
            this.NAME=modF.FILENAME
            this.patternName();
            modF.closeDocument ();
        }
    }
}

mppPaint.prototype.paintFile = function(PATH){//ファイルを読み込んでペイント
    var TEMP_PATTERN = "MS_temp";
    var TEMP_PATTERN_A ="MS_temp_a";
    var modP = new modPaint;
    var modF = new modFile;
    var modL = new modLayer;
    var modC = new modChannel;
    modP.deletePattern(TEMP_PATTERN);
    modP.deletePattern(TEMP_PATTERN_A);

    modF.FILENAME=PATH;
    if (modF.fileExists()){
        
        modL.selectLayerTransparency();
        modF.fileOpen();
        modL.mergeVisibleLayers ();
        modP.registrationPattern(TEMP_PATTERN);
        modP.registrationPatternAlpha(TEMP_PATTERN_A);
        modF.closeDocument ();
        //paint
        modC.selectRGBChannel();
        modP.paintPattern(TEMP_PATTERN);
        modC.addAlphaChannel();
        modP.paintPattern(TEMP_PATTERN_A);
        modC.selectRGBChannel();
    }
    modP.deletePattern(TEMP_PATTERN);
    modP.deletePattern(TEMP_PATTERN_A);
}

//レイヤーを指定パターンでペイント
mppPaint.prototype.paintLayer = function( LAYER_NAME , OPTION ){
    activeDocument.activeLayer = activeDocument.layers[LAYER_NAME];
    var modC = new modChannel;
    var modP = new modPaint;
    modC.selectRGBChannel();
    modP.paintPattern("MS_temp_"+this.OPTION);
    modC.addAlphaChannel();
    modP.paintPattern("MS_temp_"+this.OPTION+"a");
    modC.selectRGBChannel();
}



