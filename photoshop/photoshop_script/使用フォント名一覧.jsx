// UTF-8
// Photoshop CS2以降用スクリプト
// テキストレイヤーのフォント名一覧を表示する
// バージョン 0.9.3 	2009/12/13

// http://www.trojanbear.net/

var findfonts = new Array(99);		//検索して見つかったフォント名（英語表記） グローバル

var doc = activeDocument;
var strMessage = "";



//ドキュメント直下レイヤーの処理
for (var i = 0; i < doc.artLayers.length; i++) {
	var l = doc.artLayers[i];
	addLayer(l);
}


//ドキュメント直下レイヤーセットの処理
for (var k = 0; k < doc.layerSets.length; k++) {

	//レイヤーセット
	layerset1 = doc.layerSets[k];
	
	writeLayerName(layerset1);

}


alert(strMessage,"使用されているフォント名 "  );

//メイン終了



//　レイヤーセット内にレイヤーが含まれる限り書き出し（再帰）
function writeLayerName(layObj){

	var n = layObj.artLayers.length;
	for (var i=0; i<n; i++){
		var layName = layObj.artLayers[i].name;
		//★処理
		addLayer(layObj.artLayers[i]);
	}

	var ns = layObj.layerSets.length;
	for (i=0; i<ns; i++){
		writeLayerName(layObj.layerSets[i]);
	}
}

//レイヤー名を追加
function addLayer(objLayer){

	if (objLayer.kind == LayerKind.TEXT) {
		try{
			var fontName = objLayer.textItem.font;
		}catch(e){
//			alert("エラー番号 " + e.number);
			//8402 レイヤーにテキストが含まれない のエラーが出たら何もしない。
			//ファイルによってはこのパターンもありうる
			if(e.number != 8402){
				throw e;
			}
		}finally{

			//すでに見つけたフォント名でなければ追加
			if ( !( inArray(findfonts,fontName) ) ){ 
				findfonts.push( fontName);
				strMessage += "\n" + fontName;
			}
		}
	}

}


//配列検索用 定義
//Photoshop CS2のJavascriptエンジンはかなり古いので、古い形で定義
function inArray(vntArray, value ){
	for(var i=0;i <= vntArray.length;i++){
		if( vntArray.hasOwnProperty(i) &&vntArray[i] === value){
			return true;
		}
	}
	return false;
}

