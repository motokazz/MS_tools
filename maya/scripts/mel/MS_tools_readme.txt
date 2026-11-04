～MS_toolsインストール方法～



１・「update_MS_tools.bat」を起動してください。

※MS_toolsは「D:\MS_tools」フォルダを使用します。
　もし、すでに、別の用途でMS_toolsと言う名前のフォルダが存在する場合は、フォルダ名を変更するか、「update_MS_tools.bat」の書き換えを行うようにしてください。

２・メニューのセットアップ
まず、
「C:\Documents and Settings\*********\My Documents\maya\7.0\scripts\userSetup.mel」
があるかどうかを確認してそれぞれのケースに合わせたセットアップを行ってください。


caseA・
「userSetup.mel」がある場合。

	「userSetup.mel」をテキストエディターで開いて、以下の一行を書き加えてください。
	
	source"D:/MS_tools/MS_tools_setup.mel";


caseB・	
「userSetup.mel」が無く「bonustools」も使用していない場合。
	は以下の一行を書き加えた新規の「userSetup.mel」ファイルを作成してください。
	
	source"D:/MS_tools/MS_tools_setup.mel";
	

caseC・
	「userSetup.mel」が無く「bonusTools」を使用してる場合。
	
	「bonusTools」がインストールされているフォルダの中にある「userSetup.mel」を
	「C:\Documents and Settings\*********\My Documents\maya\7.0\scripts\userSetup.mel」
	内にコピーしてください。
	次に、「userSetup.mel」テキストエディターで開いて、以下の一行を書き加えてください。
	
	source"D:/MS_tools/MS_tools_setup.mel";
	
	
	


～アップデート～

MS_toolsフォルダの中にある、「update_MS_tools.bat」をクリックしてください。
※「update_MS_tools.bat」はどこに置いておいても大丈夫です。


