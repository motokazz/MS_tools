@echo off
@ipconfig /flushdns
@net stop  "DNS Client"
@net start "DNS Client"
@echo キャッシュをクリアした上でＤＮＳクライアントを再起動しました。再度接続を試みてください
@pause
