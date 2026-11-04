function ms_windowTemplate_core(){
    this.sliderGrpValue=0.5;
    this.TextFieldGrpValue="0";
    this.RadioButtonValue=0;
}

//main
ms_windowTemplate_core.prototype.main=function(){
    
	AlertText="";
	AlertText+=String(this.sliderGrpValue)+"\n";
	AlertText+=String(this.TextFieldGrpValue)+"\n";
	AlertText+=String(this.RadioButtonValue)+"\n";
    AlertText+="fin";

    alert(AlertText);

}
