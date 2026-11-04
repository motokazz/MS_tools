@echo off

echo 発注書をサーバーにあるテンプレートから作成します。

set /p STAGENAME="ステージ名を入力してください　＞　"

copy "\\Fs03\gravity2$\graphic\bg\documents\発注書\BGアセット\テンプレート\bgorder.xlsx" %~dp0\bgorder_%STAGENAME%.xlsx
copy "\\Fs03\gravity2$\graphic\bg\documents\発注書\イメージボード\テンプレート\ConceptArtOrder.xlsx" %~dp0\ConceptArtOrder_%STAGENAME%.xlsx



