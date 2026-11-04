//@include "ms_loopTex_contentPaint.jsx"
//@include "ms_loopTex_resize.jsx"

//=========================================================================

uDlg = new Window('dialog','ms_loopTex_UI',[100,100,430,390]);
//============
//loopTexture
//============
uDlg.loopTextPnl = uDlg.add("panel",[10,10,320,100],"loopTextureTool");
uDlg.loopTextPnl.sTextA = uDlg.loopTextPnl.add("statictext",[10,10,80,20], "beltSize");
uDlg.loopTextPnl.beltSize = uDlg.loopTextPnl.add("slider",[90,10,250,20],0.33,0,1);
uDlg.loopTextPnl.beltSizeV = uDlg.loopTextPnl.add("statictext",[260,10,300,20], "0.0");


uDlg.loopTextPnl.sTextB = uDlg.loopTextPnl.add("statictext",[10,30,80,40], "featherSize");
uDlg.loopTextPnl.featherSize = uDlg.loopTextPnl.add("slider",[90,30,250,40],0,0,1);
uDlg.loopTextPnl.featherSizeV = uDlg.loopTextPnl.add("statictext",[260,30,300,40], "0.0");


uDlg.loopTextPnl.main = uDlg.loopTextPnl.add("button",[0,50,305,80], "ms_loopTex_contentPaint");

uDlg.loopTextPnl.main.onClick = function(){ 
    LTCP=new loopTexCP;
    LTCP.beltSize=uDlg.loopTextPnl.beltSize.value;
    LTCP.featherSize=uDlg.loopTextPnl.featherSize.value;
    LTCP.main();
    uDlg.close();
}

uDlg.loopTextPnl.beltSize.onChange = function(){
    uDlg.loopTextPnl.beltSizeV.text=uDlg.loopTextPnl.beltSize.value;
}

uDlg.loopTextPnl.featherSize.onChange = function(){
    uDlg.loopTextPnl.featherSizeV.text=uDlg.loopTextPnl.featherSize.value;
}

//initialize
uDlg.loopTextPnl.beltSizeV.text=uDlg.loopTextPnl.beltSize.value;
uDlg.loopTextPnl.featherSizeV.text=uDlg.loopTextPnl.featherSize.value;


//============
//resize
//============
uDlg.resizePnl = uDlg.add("panel",[10,110,320,280],"loopTextureResize");

uDlg.resizePnl.resizeXt = uDlg.resizePnl.add("statictext",[10,10,80,30], "resizeX");
uDlg.resizePnl.resizeX = uDlg.resizePnl.add("edittext",[70,10,120,30], "512");


uDlg.resizePnl.resizeXt = uDlg.resizePnl.add("statictext",[10,40,80,60], "resizeY");
uDlg.resizePnl.resizeY = uDlg.resizePnl.add("edittext",[70,40,120,60], "512");

uDlg.resizePnl.rBtn0 = uDlg.resizePnl.add("radiobutton",[150,10,300,30], "BICUBIC");
uDlg.resizePnl.rBtn1 = uDlg.resizePnl.add("radiobutton",[150,30,300,50], "BICUBICSHARPER");
uDlg.resizePnl.rBtn2 = uDlg.resizePnl.add("radiobutton",[150,50,300,70], "BICUBICSMOOTHER");
uDlg.resizePnl.rBtn3 = uDlg.resizePnl.add("radiobutton",[150,70,300,90], "BILINEAR");
uDlg.resizePnl.rBtn4 = uDlg.resizePnl.add("radiobutton",[150,90,300,110], "NEARESTNEIGHBOR");
uDlg.resizePnl.rBtn5 = uDlg.resizePnl.add("radiobutton",[150,110,300,130], "NONE");

uDlg.resizePnl.rsizeExe = uDlg.resizePnl.add("button",[0,130,305,160], "ms_loopTex_resize");
//
ditectRMethod=function(){
    RM = ResampleMethod.BICUBIC;
    if (uDlg.resizePnl.rBtn0.value) { RM = ResampleMethod.BICUBIC; }
    if (uDlg.resizePnl.rBtn1.value) { RM = ResampleMethod.BICUBICSHARPER; }
    if (uDlg.resizePnl.rBtn2.value) { RM = ResampleMethod.BICUBICSMOOTHER; }
    if (uDlg.resizePnl.rBtn3.value) { RM = ResampleMethod.BILINEAR; }
    if (uDlg.resizePnl.rBtn4.value) { RM = ResampleMethod.NEARESTNEIGHBOR; }
    if (uDlg.resizePnl.rBtn5.value) { RM = ResampleMethod.NONE; }
    return RM;
}

uDlg.resizePnl.rsizeExe.onClick = function(){
    LTRZ=new loopTexRZ;
    
    LTRZ.nw=parseInt(uDlg.resizePnl.resizeX.text);
    LTRZ.nh=parseInt(uDlg.resizePnl.resizeY.text);
    LTRZ.rMethod=ditectRMethod();
    
    LTRZ.main();
    
    uDlg.resizePnl.close();
}

//initialize
uDlg.resizePnl.rBtn0.value=true;

uDlg.show();

