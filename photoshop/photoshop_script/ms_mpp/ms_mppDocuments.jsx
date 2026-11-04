


//create new document
//選択レイヤーを元に新規ドキュメント作成
//nameレイヤー　⇒RGBチャンネル
//aNameレイヤー⇒αチャンネル
// =======================================================



function mppDocument(name,aName){

 //name=RGBグループ
 //aName=αチャンネルのグループ
 
// nameを選択=======================================================
 var idslct = charIDToTypeID( "slct" );
var desc102 = new ActionDescriptor();
var idnull = charIDToTypeID( "null" );
var ref96 = new ActionReference();
var idLyr = charIDToTypeID( "Lyr " );
ref96.putName( idLyr, name);
desc102.putReference( idnull, ref96 );
var idMkVs = charIDToTypeID( "MkVs" );
desc102.putBoolean( idMkVs, false );
executeAction( idslct, desc102, DialogModes.NO );

//aNameを選択=======================================================
var idslct = charIDToTypeID( "slct" );
var desc103 = new ActionDescriptor();
var idnull = charIDToTypeID( "null" );
var ref97 = new ActionReference();
var idLyr = charIDToTypeID( "Lyr " );
ref97.putName( idLyr, aName);
desc103.putReference( idnull, ref97 );
var idselectionModifier = stringIDToTypeID( "selectionModifier" );
var idselectionModifierType = stringIDToTypeID( "selectionModifierType" );
var idaddToSelection = stringIDToTypeID( "addToSelection" );
desc103.putEnumerated( idselectionModifier, idselectionModifierType, idaddToSelection );
var idMkVs = charIDToTypeID( "MkVs" );
desc103.putBoolean( idMkVs, false );
executeAction( idslct, desc103, DialogModes.NO );

//ドキュメント検索OR新規作成
try{
activeDocument=documents[name];
// =======================================================
lsObja = activeDocument.layerSets[name];
lsObjb = activeDocument.layerSets[aName];
dc=documents[name];
lsObja.duplicate(dc);
lsObjb.duplicate(dc);


}
catch(e){
// 選択レイヤーセットを新規ドキュメント（name）に複製=======================================================
var idMk = charIDToTypeID( "Mk  " );
var desc104 = new ActionDescriptor();
var idnull = charIDToTypeID( "null" );
var ref98 = new ActionReference();
var idDcmn = charIDToTypeID( "Dcmn" );
ref98.putClass( idDcmn );
desc104.putReference( idnull, ref98 );
var idNm = charIDToTypeID( "Nm  " );
desc104.putString( idNm, name );
var idUsng = charIDToTypeID( "Usng" );
var ref99 = new ActionReference();
var idLyr = charIDToTypeID( "Lyr " );
var idOrdn = charIDToTypeID( "Ordn" );
var idTrgt = charIDToTypeID( "Trgt" );
ref99.putEnumerated( idLyr, idOrdn, idTrgt );
desc104.putReference( idUsng, ref99 );
var idVrsn = charIDToTypeID( "Vrsn" );
desc104.putInteger( idVrsn, 5 );
executeAction( idMk, desc104, DialogModes.NO );
}

//新ドキュメントIDを記録=======================================================
var NEW = activeDocument.name;




// 新ドキュメント選択=======================================================
//activeDocument=documents[NEW];

}




