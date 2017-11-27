function eValidate(){
  var email = document.getElementById('eAddress')
  var emailC = document.getElementById('confirmEAddress')
  if(email.value != emailC.value){
    email.style.borderColor = "red";
    emailC.style.borderColor = "red";
  }
  else{
    email.style.borderColor = "rgb(112,111,111)";
    emailC.style.borderColor = "rgb(112,111,111)";
  }
}
