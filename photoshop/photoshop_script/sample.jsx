uDlg = new Window("dialog","サンプル",[200,100,580,245]);
uDlg.okBtn = uDlg.add("button",[180,80,250,80+25], "OK", { name:"ok"});
uDlg.cancelBtn = uDlg.add("button", [90,80,160,80+25], "Cancel", {name: "cancel"});
uDlg.eText = uDlg.add("edittext",[100,10,275,10+25], "名前を入れてください");
uDlg.show();
alert("あなたの名前は「"+uDlg.eText.text+"」です。");