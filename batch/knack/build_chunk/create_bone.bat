@echo off
rem ==================================================================
rem
rem ボーンモデル生成バッチ
rem
rem Usage)
rem   create_bone.bat (input toro filepath) (output toro filepath)
rem
rem ==================================================================
setlocal

echo ----------------------------------------------------------------
echo ボーンモデル生成バッチ
echo ----------------------------------------------------------------
echo;

rem 引数チェック
if "%1"=="" goto :args_error
if "%2"=="" goto :args_error

rem セットアップ
set torotool_path=D:\Mproject\ToroTool.exe
set tscr_path=%~dp1zzbone_%~n1.tscr

rem 削除するノード設定
set del_nodes=ise_;cor_;big_;c2p_


rem ToroTool 起動チェック
tasklist | find /I "torotool.exe" >nul
if not errorlevel 1 goto :exist_torotool_error

rem 処理内容表示
echo 変換元ファイル:
echo 	%1
echo 変換先ファイル:
echo 	%2
echo;

rem スクリプトファイル生成
( echo int main(^)
  echo {
  echo Reset(^);
  echo AddScene("%1"^);
  for %%n in (%del_nodes%) do echo NodeNameDelete("%%n"^);
  echo SaveScene("%2"^);
  echo Exit(^);
  echo return 0;
  echo }
) >%tscr_path%
echo 変換＆パック用スクリプトファイル生成しました。
echo 	%tscr_path%
echo;

rem ToroTool 起動
echo ToroTool で変換スクリプトを実行します。
echo %torotool_path% %tscr_path%
echo;
%torotool_path% %tscr_path%

rem 終了
echo 処理を終了しました

goto :done

:args_error
echo 引数エラー
echo;
goto :done

:exist_torotool_error
echo ToroTool 起動中には実行できません。
echo ToroTool を終了してから実行してください。
echo;
goto :done

:done
