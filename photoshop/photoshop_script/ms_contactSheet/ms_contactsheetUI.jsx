//@include "ms_loopTex_contentPaint.jsx"

uDlg = new Window("dialog","ms_UICreator",[100,100,356,356]);
uDlg.panel0 = uDlg.add("panel",[6,1,251,206],"mainPanel");
uDlg.panel1 = uDlg.add("panel",[14,9,243,78],"BaseSetting");
uDlg.panel2 = uDlg.add("panel",[14,89,243,142],"FrameSetting");
uDlg.panel0.button0 = uDlg.panel0.add("button",[7,149,235,185], "Exec");
uDlg.panel1.edittext0 = uDlg.panel1.add("edittext",[167,33,219,53], "256");
uDlg.panel1.edittext1 = uDlg.panel1.add("edittext",[103,33,155,53], "256");
uDlg.panel1.statictext0=uDlg.panel1.add("statictext",[160,43,170,56], "H");
uDlg.panel1.statictext1=uDlg.panel1.add("statictext",[95,43,107,56], "W");
uDlg.panel1.statictext2=uDlg.panel1.add("statictext",[18,43,65,56], "Pattern");
uDlg.panel1.edittext2 = uDlg.panel1.add("edittext",[167,1,219,21], "2048");
uDlg.panel1.edittext3 = uDlg.panel1.add("edittext",[103,1,155,21], "2048");
uDlg.panel1.checkbox0 = uDlg.panel1.add("checkbox",[18,11,77,24], "NewCanvas");
uDlg.panel1.statictext3=uDlg.panel1.add("statictext",[160,11,170,24], "H");
uDlg.panel1.statictext4=uDlg.panel1.add("statictext",[95,11,107,24], "W");
uDlg.panel2.edittext4 = uDlg.panel2.add("edittext",[103,21,155,41], "1");
uDlg.panel2.statictext5=uDlg.panel2.add("statictext",[18,28,77,43], "FrameSkip");
uDlg.panel2.edittext5 = uDlg.panel2.add("edittext",[103,3,155,23], "0");
uDlg.panel2.statictext6=uDlg.panel2.add("statictext",[18,11,83,24], "StartFrame");

uDlg.panel0.button0.onClick()=function(){
    cs=new ms_contactsheet;
    cs.nx=parseInt(uDlg.panel1.edittext3.value);
    cs.ny=parseInt(uDlg.panel1.edittext2.value);
    cs.ix=parseInt(uDlg.panel1.edittext0.value);
    cs.iy=parseInt(uDlg.panel1.edittext1.value);
    cs.nstart=parseInt(uDlg.panel1.edittext5.value);
    cs.nstep=parseInt(uDlg.panel1.edittext4.value);
    cs.sourceFolder="D:/work/contactsheet/";
    cs.exec();
}

uDlg.show();

