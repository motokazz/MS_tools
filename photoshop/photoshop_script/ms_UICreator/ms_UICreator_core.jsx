#target 'photoshop';

function ms_windowTemplate_core(){
    this.saveDir='D:/MS_tools/photoshop/photoshop_script/ms_UICreator/';
    this.sample='ms_UICreator_sample.jsx';

}

saveDir='D:/MS_tools/photoshop/photoshop_script/ms_UICreator/';
sample='ms_UICreator_sample.jsx';

//main
ms_windowTemplate_core.prototype.main=function(){
    AlertText="";
    AlertText+=CWindow();
    AlertText+="\n";
    AlertText+=CreateControlers();
    AlertText+="\n";
    AlertText+="uDlg.show();";
    AlertText+="\n"; 
    save(AlertText);
}

//----------------------------------
//SaveFile
//----------------------------------
function save(STR){
    CR = String.fromCharCode(13);
//savename = File.saveDialog("保存するファイル名を入れてください");
savename = 'D:/MS_tools/photoshop/photoshop_script/ms_UICreator/ms_UICreator_sample.jsx';
if (savename){
    fileObj = new File(savename);
    flag = fileObj.open("w");
    if (flag == true){
        fileObj.write(STR);
        fileObj.close();
    }else{
        alert("ファイルが開けませんでした");
    }
}
}

//----------------------------------
//レイヤーバウンド計算
//----------------------------------

//レイヤーのバウンド範囲を策定
function GetLayersBounds(obj,mX,mY){
    layObj = obj.bounds;
    return (layObj[0].value+","+(layObj[1].value-mX)+","+layObj[2].value+","+(layObj[3].value-mY));
}
//テキストレイヤーのバウンド範囲を策定
function calcTextBounds(objA,objB){
    RectA = objA.bounds;
    RectB = objB.bounds;
    return [
    RectB[0].value-RectA[0].value-4
    ,RectB[1].value-RectA[1].value-6
    ,RectB[2].value-RectA[0].value+5
    ,RectB[3].value-RectA[1].value-6
    ];
}
//2つのバウンドの差を返す、パネル内コントロール作成等に使用
function calcBounds(objA,objB){
    RectA = objA.bounds;
    RectB = objB.bounds;
    return [
    RectB[0].value-RectA[0].value
    ,RectB[1].value-RectA[1].value-2
    ,RectB[2].value-RectA[0].value-2
    ,RectB[3].value-RectA[1].value-4
    ];
}

//----------------------------------
//メインウィンドウ作成
//----------------------------------

function CWindow(){
    preferences.rulerUnits = Units.PIXELS;
    width = activeDocument.width.value+100;
    height = activeDocument.height.value+100;
    return 'uDlg = new Window("dialog","ms_UICreator",[100,100,'+width+','+height+']);';
}

//----------------------------------
//パネル作成
//----------------------------------

function CPanel(obj,controlName,parentName){
    bounds=GetLayersBounds(obj,5,5);
    return 'uDlg.'+controlName+' = uDlg.add("panel",['+bounds+'],"'+parentName+'");\n';
}

//----------------------------------
//イメージGUI作成
//----------------------------------

//Bound形式をSelection形式に変換
function BoundToSelection(BOUND){
    selReg = [
        [BOUND[0],BOUND[1]]
        ,[BOUND[2],BOUND[1]]
        ,[BOUND[2],BOUND[3]]
        ,[BOUND[0],BOUND[3]]
        ];
    return selReg;
}

//選択レイヤー保存
function layerSave(PATH,obj){
    preferences.rulerUnits = Units.PIXELS;
    obj.copy(false);
    B=obj.bounds;

    //ドキュメント新規作成
    ND=documents.add(B[2]-B[0]-5,B[3]-B[1]-5);
    ND.selection.selectAll();
    ND.paste(true);

    //Save
    fileObj = new File(PATH);
    pngOpt = new PNGSaveOptions();
    pngOpt.interlaced = false;
    activeDocument.saveAs(fileObj, pngOpt, true, Extension.LOWERCASE);

    //Close
    ND.close( SaveOptions.DONOTSAVECHANGES);

}

function layerSaveGrouped(PATH,obj,objGrouped){
    preferences.rulerUnits = Units.PIXELS;
    
    BOUND=obj.bounds;
    activeDocument.activeLayer = objGrouped;
    activeDocument.selection.select( BoundToSelection(BOUND));    
    activeDocument.selection.copy(false);

    //ドキュメント新規作成
    ND=documents.add(B[2]-B[0]-5,B[3]-B[1]-5);
    ND.selection.selectAll();
    ND.paste(true);

    //Save
    fileObj = new File(PATH);
    pngOpt = new PNGSaveOptions();
    pngOpt.interlaced = false;
    activeDocument.saveAs(fileObj, pngOpt, true, Extension.LOWERCASE);

    //Close
    ND.close( SaveOptions.DONOTSAVECHANGES);

}

function CImgPanel(obj,controlName,parentName){
    ret=""
    //
    bounds=GetLayersBounds(obj,-5,-5);
    //
    B = obj.bounds;
    w=B[2].value-B[0].value-5;
    h=B[3].value-B[1].value-5;
    //
    PATH=saveDir+controlName+".png"
    layerSave(PATH,obj);
    ret+= 'fileObj = new File("'+PATH+'");\n';
    ret+= 'uDlg.'+controlName+'.add("image",[0,0,'+w+','+h+'],fileObj);\n';

    return ret;
}

function CImgGrouped( obj,objGrouped,controlName,parentName){
    ret=""
    //
    bounds=GetLayersBounds(obj,-5,-5);
    //
    B = obj.bounds;
    w=B[2].value-B[0].value-5;
    h=B[3].value-B[1].value-5;
    //
    PATH=saveDir+controlName+".png"
    layerSaveGrouped(PATH,obj,objGrouped);
    ret+= 'fileObj = new File("'+PATH+'");\n';
    ret+= 'uDlg.'+controlName+'.add("image",[0,0,'+w+','+h+'],fileObj);\n';

    return ret;
}
//----------------------------------
//コントロール作成
//----------------------------------
//テキスト
function CTextInfo(obj,controlName,parentName,rectArray){
    contents=obj.textItem.contents;
    if (contents.indexOf("\n")!=-1 || contents.indexOf("\r")!=-1){
        contents=contents.replace("\n","\"+String.fromCharCode(13)+\"");
        contents=contents.replace("\r","\"+String.fromCharCode(13)+\"");
    }

    bounds=(rectArray[0]+","+rectArray[1]+","+rectArray[2]+","+rectArray[3]);

    if (controlName.match("checkbox")){
        contents=contents.replace("[v]:","");
        return 'uDlg.'+ parentName +'.'+controlName+' = uDlg.'+ parentName +'.add("checkbox",['+ bounds +'], "'+ contents +'");\n'
    }
    else if (controlName.match("radiobutton")){
        contents=contents.replace("(O):","");
        return 'uDlg.'+ parentName +'.'+controlName+' = uDlg.'+ parentName +'.add("radiobutton",['+ bounds +'], "'+ contents +'");\n'
    }else{
        return 'uDlg.'+parentName+'.'+controlName+'=uDlg.'+parentName+'.add("statictext",['+bounds+'], "'+contents+'");\n';
    }
}
//編集可能テキスト
function CEditText(obj,controlName,parentName,rectArray){
    contents=obj.name;
    if (contents.indexOf("edittext:")!=-1){
        contents=contents.replace("edittext:","");
    }
    bounds=(rectArray[0]+","+(rectArray[1]+2)+","+(rectArray[2]-4)+","+(rectArray[3]-2));
    //bounds=GetLayersBounds (obj, -5, -5);
    return 'uDlg.'+ parentName +'.'+controlName+' = uDlg.'+ parentName +'.add("edittext",['+ bounds +'], "'+ contents +'");\n'
}
//ドロップダウンリスト
function CDropdownList(obj,controlName,parentName,rectArray){
    contents=obj.name;
    if (contents.indexOf("dropdownlist:")!=-1){
        contents=contents.replace("dropdownlist:","");
    }
    re = new RegExp(",", "g");
    CA=contents.replace(re ,"\",\"");

    bounds=(rectArray[0]+","+rectArray[1]+","+rectArray[2]+","+rectArray[3]);
    return 'uDlg.'+ parentName +'.'+controlName+' = uDlg.'+ parentName +'.add("dropdownlist",['+ bounds +'], ["'+ CA+'"]);\n'
}

//リストボックス
function CListBox(obj,controlName,parentName,rectArray){
    contents=obj.name;
    if (contents.indexOf("listbox:")!=-1){
        contents=contents.replace("listbox:","");
    }
    re = new RegExp(",", "g");
    CA=contents.replace(re ,"\",\"");

    bounds=(rectArray[0]+","+rectArray[1]+","+rectArray[2]+","+rectArray[3]);
    return 'uDlg.'+ parentName +'.'+controlName+' = uDlg.'+ parentName +'.add("listbox",['+ bounds +'], ["'+ CA+'"]);\n'
}

//スライダー
function CSlider(obj,controlName,parentName,rectArray){
    contents=obj.name;
    if (contents.indexOf("slider:")!=-1){
        contents=contents.replace("slider:","");
    }
    bounds=(rectArray[0]+","+rectArray[1]+","+rectArray[2]+","+rectArray[3]);
    return 'uDlg.'+ parentName +'.'+controlName+' = uDlg.'+ parentName +'.add("slider",['+ bounds +'], "'+ contents +'");\n'
}
//スクロールバー
function CScrollBar(obj,controlName,parentName,rectArray){
    contents=obj.name;
    if (contents.indexOf("scrollbar:")!=-1){
        contents=contents.replace("scrollbar:","");
    }
    bounds=(rectArray[0]+","+rectArray[1]+","+rectArray[2]+","+rectArray[3]);
    return 'uDlg.'+ parentName +'.'+controlName+' = uDlg.'+ parentName +'.add("scrollbar",['+ bounds +'], "'+ contents +'");\n'
}

//ボタン
function CButton(obj,controlName,parentName,rectArray){
    contents=obj.name;
    if (contents.indexOf("button:")!=-1){
        contents=contents.replace("button:","");
    }
    bounds=(rectArray[0]+","+(rectArray[1]+2)+","+(rectArray[2]-4)+","+(rectArray[3]-2));
    return 'uDlg.'+ parentName +'.'+controlName+' = uDlg.'+ parentName +'.add("button",['+ bounds +'], "'+ contents +'");\n'
}
//チェックボックス
function CCheckBox(obj,controlName,parentName,rectArray){
    contents=obj.name;
    if (contents.indexOf("checkbox:")!=-1){
        contents=contents.replace("checkbox:","");
    }
    bounds=(rectArray[0]+","+rectArray[1]+","+rectArray[2]+","+rectArray[3]);
    return 'uDlg.'+ parentName +'.'+controlName+' = uDlg.'+ parentName +'.add("checkbox",['+ bounds +'], "'+ contents +'");\n'
}

//ラジオボタン
function CRadioButton(obj,controlName,parentName,rectArray){
    contents=obj.name;
    if (contents.indexOf("radiobutton:")!=-1){
        contents=contents.replace("radiobutton:","");
    }
    bounds=(rectArray[0]+","+rectArray[1]+","+rectArray[2]+","+rectArray[3]);
    return 'uDlg.'+ parentName +'.'+controlName+' = uDlg.'+ parentName +'.add("radiobutton",['+ bounds +'], "'+ contents +'");\n'
}




//----------------------------------
//レイヤー情報の取得
//----------------------------------
// ドキュメント内の全レイヤーを再帰的に取得
function writeLayerName(layObj){
    var n = layObj.artLayers.length;
    for (var i=0; i<n; i++){
        aLayers.push(layObj.artLayers[i]);
    }

    var ns = layObj.layerSets.length;
    for (var i=0; i<ns; i++){
        LSets.push(layObj.layerSets[i]);
        writeLayerName(layObj.layerSets[i]);
    }
}

// ドキュメント内のセットを取得
function walkLayerSets(){
    LSets=[];

    function walkLayerSets_recursive(layObj){
        var ns = layObj.layerSets.length;
        for (var i=0; i<ns; i++){
            LSets.push(layObj.layerSets[i]);
            walkLayerSets_recursive(layObj.layerSets[i]);
        }
    }

    AD=activeDocument;
    walkLayerSets_recursive(AD);

    return LSets;
}
//----------------------------------
// コントロール作成コア
//----------------------------------
function CreateControlers(){
    ret="";
    panelCommand="";
    
    //コントロール数のトータル
    panel=0;
    statictext=0;
    button=0;
    edittext=0;
    dropdownlist=0;
    checkbox=0;
    slider=0;
    radiobutton=0;
    listbox=0;
    scrollbar=0;

    //
    LS=walkLayerSets();
    nSets = LS.length;
    
    for (j=0;j<nSets;j++){
        lsObj = LS[j];
        n = lsObj.artLayers.length;
        parentName="panel"+panel;
        //controls
        i=0;
        for (i=0;i<n;i++){
            
            try{
                calcedArray=calcBounds(lsObj.artLayers[n-1],lsObj.artLayers[i]);
            }catch(e){
                calcedArray=calcBounds(lsObj.artLayers[n],lsObj.artLayers[i]);
           }
            chstr=lsObj.artLayers[i].name;
            //text
            if(lsObj.artLayers[i].kind==LayerKind.TEXT){
                contents=lsObj.artLayers[i].textItem.contents;
                calcedArray=calcTextBounds(lsObj.artLayers[n-1],lsObj.artLayers[i]);
                if (contents.search(/\[v\]/)>=0){
                    controlName="checkbox"+checkbox;
                    checkbox++;
                }else if (contents.search(/\(O\)/)>=0){
                    controlName="radiobutton"+radiobutton;
                    radiobutton++;
                }else{
                    controlName="statictext"+statictext;
                    statictext++;
                }
                ret+=CTextInfo(lsObj.artLayers[i],controlName,parentName,calcedArray);
                 
            }
            else if(chstr.search("edittext:")>=0){
                //edittext
                controlName="edittext"+edittext;
                ret+=CEditText(lsObj.artLayers[i],controlName,parentName,calcedArray);
                edittext++;
            }

            else if(chstr.search("slider:")>=0){
                //slider
                controlName="slider"+slider;
                ret+=CSlider(lsObj.artLayers[i],controlName,parentName,calcedArray);
                slider++;
            }
            else if(chstr.search("scrollbar:")>=0){
                //scrollbar
                controlName="scrollbar"+scrollbar;
                ret+=CSlider(lsObj.artLayers[i],controlName,parentName,calcedArray);
                scrollbar++;
            }
            else if(chstr.search("checkbox:")>=0){
                //checkbox
                controlName="checkbox"+checkbox;
                ret+=CCheckBox(lsObj.artLayers[i],controlName,parentName,calcedArray);
                checkbox++;
            }
            else if(chstr.search("radiobutton:")>=0){
                //radiobutton
                controlName="radiobutton"+radiobutton;
                ret+=CRadioButton(lsObj.artLayers[i],controlName,parentName,calcedArray);
                radiobutton++;
            }
            else if(chstr.search("button:")>=0){
                //button
                controlName="button"+button;
                ret+=CButton(lsObj.artLayers[i],controlName,parentName,calcedArray);
                button++;
            }
            //PanelDitect
            else if(chstr.search("panel")>=0){
                controlName="panel"+panel;
                panelCommand+=CPanel(lsObj.artLayers[i], controlName , lsObj.name);
                panel++;
            }
        
            if (chstr.search("img")>=0){
                try{
                     CHECK=lsObj.artLayers[i-1].grouped;
                     }
                 catch(e){
                     CHECK=false;
                     }
                 alert(CHECK);
                 if (CHECK){
                     ret+= CImgGrouped( lsObj.artLayers[i],lsObj.artLayers[i-1],controlName,parentName)
                     }
                  else{
                    ret+=CImgPanel( lsObj.artLayers[i],controlName , lsObj.name);
                 }
            }
            
            
        }
    }
    return panelCommand+ret;
}

LTCP=new ms_windowTemplate_core;
LTCP.main();


