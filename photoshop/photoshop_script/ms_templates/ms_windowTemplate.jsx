
//@include "ms_windowTemplate_core.jsx"

//============
//Create Window
//============

uDlg = new Window('dialog','MS_tools_template',[100,100,430,390]);


//--------------
//panel
//--------------

uDlg.templatePnl = uDlg.add("panel",[10,10,320,260],"loopTextureTool");


//--------------
//Control
//--------------

//textLabel
uDlg.templatePnl.TextLabel=uDlg.templatePnl.add("statictext",[10,10,80,20], "textLabel");

//sliderGrp
uDlg.templatePnl.sliderGrpLabel = uDlg.templatePnl.add("statictext",[10,30,90,40], "SliderGrp");
uDlg.templatePnl.sliderGrpSlider = uDlg.templatePnl.add("slider",[100,30,250,40],0.33,0,1);
uDlg.templatePnl.sliderGrpValue = uDlg.templatePnl.add("statictext",[260,30,300,40], "0.0");

//TextFieldGrp
uDlg.templatePnl.TextFieldGrpLabel = uDlg.templatePnl.add("statictext",[10,50,90,70], "TextFieldGrp");
uDlg.templatePnl.TextFieldGrpValue = uDlg.templatePnl.add("edittext",[100,50,150,70], "512");

//RadioButton
uDlg.templatePnl.RadioButton0 = uDlg.templatePnl.add("radiobutton",[150,80,300,100], "BICUBIC");
uDlg.templatePnl.RadioButton1 = uDlg.templatePnl.add("radiobutton",[150,100,300,120], "BICUBICSHARPER");
uDlg.templatePnl.RadioButton2 = uDlg.templatePnl.add("radiobutton",[150,120,300,140], "BICUBICSMOOTHER");
uDlg.templatePnl.RadioButton3 = uDlg.templatePnl.add("radiobutton",[150,140,300,160], "BILINEAR");
uDlg.templatePnl.RadioButton4 = uDlg.templatePnl.add("radiobutton",[150,160,300,180], "NEARESTNEIGHBOR");
uDlg.templatePnl.RadioButton5 = uDlg.templatePnl.add("radiobutton",[150,180,300,200], "NONE");

//Button
uDlg.templatePnl.main = uDlg.templatePnl.add("button",[0,210,305,240], "ms_loopTex_contentPaint");

//=========
//initialize
//=========

//Slider
uDlg.templatePnl.sliderGrpValue.text=uDlg.templatePnl.sliderGrpSlider.value;

//Radio
uDlg.templatePnl.RadioButton0.value=true;


//===============
//ChangeCommand
//===============

uDlg.templatePnl.sliderGrpSlider.onChange = function(){
    uDlg.templatePnl.sliderGrpValue.text=uDlg.templatePnl.sliderGrpSlider.value;
}


//===============
//GetValue
//===============

ditectRMethod=function(){
    RM = "ResampleMethod.BICUBIC";
    if (uDlg.templatePnl.RadioButton0.value) { RM = "ResampleMethod.BICUBIC"; }
    if (uDlg.templatePnl.RadioButton1.value) { RM = "ResampleMethod.BICUBICSHARPER"; }
    if (uDlg.templatePnl.RadioButton2.value) { RM = "ResampleMethod.BICUBICSMOOTHER"; }
    if (uDlg.templatePnl.RadioButton3.value) { RM = "ResampleMethod.BILINEAR"; }
    if (uDlg.templatePnl.RadioButton4.value) { RM = "ResampleMethod.NEARESTNEIGHBOR"; }
    if (uDlg.templatePnl.RadioButton5.value) { RM = "ResampleMethod.NONE"; }
    return RM;
}

//===============
//Execute
//===============

uDlg.templatePnl.main.onClick = function(){ 
    LTCP=new ms_windowTemplate_core;
    //======================================
    //from Slider
    LTCP.sliderGrpValue=uDlg.templatePnl.sliderGrpSlider.value;
    
    //from textField
    LTCP.TextFieldGrpValue=uDlg.templatePnl.TextFieldGrpValue.text;
    
    //fron RadioButton
    LTCP.RadioButtonValue=ditectRMethod();
    //======================================
    LTCP.main();
    //uDlg.close();
}


//===========
//ShowWindow
//===========

uDlg.show();

