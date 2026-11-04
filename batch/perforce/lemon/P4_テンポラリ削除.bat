
p4 unlock %1
p4 submit -f submitunchanged -d "削除のためのチェックイン" %1
p4 delete %1
p4 submit -f submitunchanged -d "未使用削除" %1


