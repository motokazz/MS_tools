
//@include "ms_UICreator_core.jsx"
#target 'photoshop';

//============
//Create Window
//============

uDlg = new Window('dialog','MS_tools_template',[100,100,430,390]);

//uDlg.resizable = true;

uDlg.panel0 = uDlg.add("panel",[14,14,275,179],"グループ 1");
uDlg.panel0.statictext0=uDlg.panel0.add("statictext",[19,5,71,15], "textLabel");

uDlg.panel0.button0 = uDlg.panel0.add("button",[34,26,58,50], "Text");
uDlg.panel0.button1 = uDlg.panel0.add("button",[33,58,57,82], "Button");
uDlg.panel0.button2 = uDlg.panel0.add("button",[34,90,58,114], "EditText");
uDlg.panel0.button3 = uDlg.panel0.add("button",[34,122,58,146], "DropDownList");

uDlg.panel0.button4 = uDlg.panel0.add("button",[80,26,104,50], "CheckBox");
uDlg.panel0.button5 = uDlg.panel0.add("button",[80,58,104,82], "Slider");
uDlg.panel0.button6 = uDlg.panel0.add("button",[80,90,104,114], "RadioButton");
uDlg.panel0.button7 = uDlg.panel0.add("button",[80,122,104,146], "Panel");

uDlg.panel0.button8 = uDlg.panel0.add("button",[128,26,156,50], "ListBox");
uDlg.panel0.button9 = uDlg.panel0.add("button",[128,58,156,82], "ScrollBar");

uDlg.panel0.button0.onClick = function(){CreateControlText();}
uDlg.panel0.button1.onClick = function(){CreateControlRect('button:Button',[200,200,200]);}
uDlg.panel0.button2.onClick = function(){CreateControlRect('edittext:EditText',[255,255,255]);}
uDlg.panel0.button3.onClick = function(){CreateControlRect('dropdownlist:a,b,c');}

//uDlg.panel0.button4.onClick = function(){CreateControlRect('checkbox:CheckBox');}
uDlg.panel0.button4.onClick = function(){CreateControlText('[v]:CheckBox');}

uDlg.panel0.button5.onClick = function(){CreateControlRect('slider:0.5,0,1');}

//uDlg.panel0.button6.onClick = function(){CreateControlRect('radiobutton:RadioButton');}
uDlg.panel0.button6.onClick = function(){CreateControlText('(O):RadioButton');}

uDlg.panel0.button7.onClick = function(){CreatePanel('panel');}
uDlg.panel0.button8.onClick = function(){CreateControlRect('listbox:a,b,c');}
uDlg.panel0.button9.onClick = function(){CreateControlRect('scrollbar:0.5,0,1');}


//Button
uDlg.panel1 = uDlg.add("panel",[0,200,400,380],"foot");
uDlg.panel1.main = uDlg.panel1.add("button",[0,0,305,32], "ms_UICreator_Create");


//===============
//Execute
//===============

uDlg.panel1.main.onClick = function(){ 
    LTCP=new ms_windowTemplate_core;
    LTCP.main();
    uDlg.close();
}


//===========
//ShowWindow
//===========

uDlg.show();




//===========
// Util
//===========

function CreateControlRect( STR , COLOR){
    layObj = activeDocument.artLayers.add();
    layObj.name =STR;
    drawRect(false,COLOR);
}

function CreateControlText(CONTENTS){
    if (!CONTENTS){
        CONTENTS='StaticText';
    }
    layObj = activeDocument.artLayers.add();
    layObj.kind=LayerKind.TEXT
    layObj.textItem.font='MS-Gothic';
    layObj.textItem.fontSize=12;
    layObj.textItem.contents = CONTENTS;
    //drawRect();
}

function CreatePanel(STR){
    try{
        rect = activeDocument.selection.bounds;
    }
    catch(e){
        rect=[16,16,224,224];
    }
    
    laySets = activeDocument.layerSets.add();
    laySets.name = STR

    layObj = laySets.artLayers.add()
    layObj.name='panel';
     drawRect(rect,[230,230,230]);
}



function drawRect( rect , color ){
    try{
        rect = activeDocument.selection.bounds;
    }
    catch(e){
        if (!rect){
            rect=[16,16,144,32];
        }
    }


    RGBColor = new SolidColor();
    if (!color){
        RGBColor.red = 232;
        RGBColor.green = 232;
        RGBColor.blue = 232;
    }else{
        RGBColor.red = color[0];
        RGBColor.green =  color[1];
        RGBColor.blue =  color[2];
    }

    selReg = [
    [rect[0],rect[1]]
    ,[rect[2],rect[1]]
    ,[rect[2],rect[3]]
    ,[rect[0],rect[3]]
    ];
    activeDocument.selection.select(selReg);
    activeDocument.selection.fill(RGBColor,ColorBlendMode.NORMAL, 100, false);
}
        
