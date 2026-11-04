
outputPath='D:/Mproject/graphic/';
activeDocument.save();
docName = activeDocument.fullName;
exPath= String (docName).replace("/d/","d:/");
dName = activeDocument.name;
dNameDDS=String(dName).replace(".tif",".dds");

var exFilePath=outputPath+dNameDDS;

//ddsconvert
app.system('cmd.exe /c start D:\\Mproject\\GTools\\bin\\tiff_to_dds.exe -in ' + exPath + ' -out ' + exFilePath + ' -target "RGBA"');
var res = activeDocument.height;
wait(res*3);

//toroCommand

comHead="int main(){";
comFoot="return 1;}";
comBody='SetTextureFromFile("'+exFilePath+'");'

var tscrFile = new File( "D:/Mproject/gtools/TEMP.tscr");
tscrFile.open("w");
tscrFile.writeln(comHead + comBody + comFoot);
tscrFile.close();
system('start D:/MProject/ToroTool.exe "D:/Mproject/gtools/TEMP.tscr"');
wait(res*1);

//DDSファイル削除
exdds=new File(exFilePath);
exdds.remove();

//func
function wait(ms){
    var d1 = new Date().getTime(); 
    var d2 = d1;
        while (d2 < d1 + ms) {
            d2 = new Date().getTime(); 
        } 
    return; 
    }
