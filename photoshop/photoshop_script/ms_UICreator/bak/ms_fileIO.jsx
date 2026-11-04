
function save(STR){
    CR = String.fromCharCode(13);
    savename = File.saveDialog("保存するファイル名を入れてください");
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
