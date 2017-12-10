function sendData(){
  var form = document.forms.namedItem("contractorForm");
  var data = new FormData(form);

  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/Form', true);
  xhr.onload = function(){
    if (xhr.readyState === 4 && xhr.status === 200){
      console.log(xhr.responseText);
    } else {
      console.log(xhr.responseText);
    }
  };
  xhr.send(data);
  return false;
}

function confirmEmail() {
  var email = document.forms["contractorForm"]['eAddress'].value;
  var confemail = document.forms["contractorForm"]['confirmEAddress'].value;
  if(email != confemail) {
    alert("Sorry, but your emails don't seem to match.");
    document.forms["contractorForm"]['eAddress'].style.borderColor="red";
    document.forms["contractorForm"]['confirmEAddress'].style.borderColor="red";
  }
}

function confirmPasswords() {
  var pass = document.forms["contractorForm"]['password'].value;
  var confpass = document.forms["contractorForm"]['confirmPassword'].value;
  if(pass != confpass) {
    alert("Sorry, but your passwords don't seem to match.");
    document.forms["contractorForm"]['password'].style.borderColor="red";
    document.forms["contractorForm"]['confirmPassword'].style.borderColor="red";
  }
}

function agreement() {
  if (document.getElementById("checkBox").checked == true){
    var date = new Date();
    var timestamp = date.getDate()+"/"+(date.getMonth()+1)+"/"+date.getFullYear()+" "+date.getHours()+":"+date.getMinutes();
    var firstname = document.forms["contractorForm"]['firstName'].value;
    var surname = document.forms["contractorForm"]['surname'].value;
    document.getElementById("signature").innerHTML= firstname+" "+surname+" "+timestamp;
  }
  else {
    document.getElementById("signature").innerHTML = " ";
  }
}

function hide(){
  var removeIt = document.getElementById('removed');
  var removeIt1 = document.getElementById('removed1');
  var removeIt2 = document.getElementById('removed2');
  var option = document.forms["contractorForm"]["eligibility"].value
  var option1 = document.forms["contractorForm"]["criminalConviction"].value
  var option2 = document.forms["contractorForm"]["disability"].value

  if(option == "No"){
      removeIt.style.visibility = "hidden";
  }
  else if(option == "Yes"){
    removeIt.style.visibility = "visible";
  }
  if(option1 == "No"){
      removeIt1.style.visibility = "hidden";
  }
  else if(option1 == "Yes"){
    removeIt1.style.visibility = "visible";
  }
  if(option2 == "No"){
      removeIt2.style.visibility = "hidden";
  }
  else if(option2 == "Yes"){
    removeIt2.style.visibility = "visible";
  }
}
