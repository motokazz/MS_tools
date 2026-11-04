

uDlg = new Window("dialog","ms_UICreator",[100,100,700,600]);
uDlg.panel0 = uDlg.add("panel",[14,14,275,179],"ÉOÉãÅ[Év 1");
uDlg.panel0.statictext0=uDlg.panel0.add("statictext",[19,5,71,15], "textLabel");
uDlg.panel0.button0 = uDlg.panel0.add("button",[34,26,58,50], "Text");
uDlg.panel0.button1 = uDlg.panel0.add("button",[33,58,57,82], "Button");
uDlg.panel0.button2 = uDlg.panel0.add("button",[34,90,58,114], "EditText");
uDlg.panel0.button3 = uDlg.panel0.add("button",[34,122,58,146], "DropDownList");
uDlg.panel0.button4 = uDlg.panel0.add("button",[80,26,104,50], "CheckBox");
uDlg.panel0.button5 = uDlg.panel0.add("button",[80,58,104,82], "Slider");
uDlg.panel0.button6 = uDlg.panel0.add("button",[80,90,104,114], "RadioButton");


uDlg.panel0.button0.onClick = function(){CreateControlText();}
uDlg.panel0.button1.onClick = function(){CreateControlRect('button:Button');}
uDlg.panel0.button2.onClick = function(){CreateControlRect('edittext:EditText');}
uDlg.panel0.button3.onClick = function(){CreateControlRect('dropdownlist:a,b,c');}
uDlg.panel0.button4.onClick = function(){CreateControlRect('checkbox:CheckBox');}
uDlg.panel0.button5.onClick = function(){CreateControlRect('slider:0.5,0,1');}
uDlg.panel0.button6.onClick = function(){CreateControlRect('radiobutton:RadioButton');}

uDlg.show();


function CreateControlRect(STR){
    layObj = activeDocument.artLayers.add();
    layObj.name =STR;
    drawRect();
}

function CreateControlText(){
    layObj = activeDocument.artLayers.add();
    layObj.kind=LayerKind.TEXT
    layObj.textItem.font='MS-Gothic';
    layObj.textItem.fontSize=12;
    layObj.textItem.contents = 'textLabel';
    //drawRect();
}

function drawRect( rect , color ){
    
    if (!rect){
        rect=[16,16,32,144];
    }

    RGBColor = new SolidColor();
    if (!color){
        RGBColor.red = 232;
        RGBColor.green = 232;
        RGBColor.blue = 232;
    }
    
    selReg = [
    [rect[0],rect[1]]
    ,[rect[3],rect[0]]
    ,[rect[3],rect[2]]
    ,[rect[0],rect[2]]
    ];
    activeDocument.selection.select(selReg);
    activeDocument.selection.fill(RGBColor,ColorBlendMode.NORMAL, 100, false);
}
        
