		- polyDeployment ver2.0 -



・はじめに
　ダウンロードしていただきありがとうございます。
　Melの勉強を兼ねてつくりました。多々エラーなどがあると思いますがご了承ください。
　気に入っていただけた方はメールなり掲示板に書き込んでくれるとありがたいです。
　バグ報告も宜しくお願いします。


・「evColorLightSetting」とは？
　良くリフレクション用のモデルを置くのですが、用意したモデルのテクスチャーと
　そっくりなライトを作れないかと思い制作しました。

・｢ParasolLight｣とは？
　パラソル型のライトを作成します。
　レンダリングされる画はエリアライトに似ており、
　ポイントライトやディレクショナルライトとは違った柔らかい光や影が表現できます。
　

・ファイル説明
　evColorLightSetting.bmp		…　アイコンです。シェルフ等にお使いください。
　evColorLightSetting.mel		…　Melです。これを読み込みます。
　evColorLightSetting_readme.txt		…　今開いてるテキストです。はじめに読みましょう。


・基本的な使い方
　１　ScriptEditorでファイルを開いてください。
　　　実行するとウインドウが立ち上がります。

　２　｢targetModel｣でターゲットとなるモデル(ポリゴン)を選択します。
　　　｢useMaterial｣でターゲットが私用しているマテリアルを選択します。

　３　｢CreateLightSet｣ボタンでLightSetを実行

　４　画像に合ったライトが作成。


・解説

　ParasolLightSet	=パラソルライトを作成します。スライドは個数です。
　
　targetModel		=ターゲットとなるモデル(ポリゴン)を選択します。
　useMaterial		=ターゲットが私用しているマテリアルを選択します。

　Parasol Intensity	=パラソルライトのライトの強さになりますが、ライト数に影響を受けます。
　TotalLightIntensity	=作成されるライトのIntensityの合計値を決めます。
　EmitSpecular		=スペキュラーの影響有りかどうかです。

　Cone Angle		=スポットライトの設定です。
　Penumbra Angle		=スポットライトの設定です。
　Dropolf		=スポットライトの設定です。

　useDmapShadows		=デプスマップシャドウを使うかどうか。
　DmapResolusion		=デプスマップシャドウのサイズです。
　DmapFilterSize		=デプスマップシャドウボケ具合です。

　use Ray Trace Shadows	=レイトレースシャドウを使うかどうか。
　Light Radius		=レイトレースシャドウのボケ具合です。
　Shadow Rays		=レイトレースシャドウのボケの綺麗さです。
　Ray Depth Limit	=レイトレースシャドウの深さです。

　※細かい説明はホームページを参考にしてください。

・今後
　バージョンアップしていきたいところ。
　・ライトの配置時にライトの向きがオブジェクト中心に左右されないオプションを追加したい。
　・パラソルライトの傘の深さを設定
　・処理の改善
　などなど。

　など考えています。
　 
　これからもがんばりますのでよろしくお願いします。


・履歴 
　Ver1.0　｢使いやすく使えるMELを作ろう｣をモットウに
　Ver2.0　｢SpotLight｣｢ParasolLight｣｢RebildLightOption｣｢RayTraceShadow｣を追加


　wrote	Co,
　day	2004.11.16
　URL	http://www.d4.dion.ne.jp/~mosquito/index.html
　mail	mosquito@d4.dion.ne.jp