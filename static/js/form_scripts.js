function sendData(){
	if (validPostcode(document.forms["contractorForm"]["postCode"].value) === true){
	  let form = document.forms.namedItem("contractorForm");
	  let data = new FormData(form);

	  let xhr = new XMLHttpRequest();
	  xhr.open("POST", '/Form', true);
	  xhr.onload = function(){
	    if (xhr.readyState === 4 && xhr.status === 200){
	      console.log(xhr.responseText);
	      if (xhr.responseText.includes("<head>")) window.location ="/FormCompletion";
	      if (xhr.responseText.includes("Email already used")) alert("Sorry, that email address has already been used");
	    } else {
	      console.log(xhr.responseText);
	    }
	  };
	  xhr.send(data);
	  return false;
  }
  else {
	  return "Bad Postcode"
  }
}

function confirmEmail() {
  let email = document.forms["contractorForm"]['eAddress'].value;
  let confirmEmail = document.forms["contractorForm"]['confirmEAddress'].value;
  if(email != confirmEmail) {
    alert("Sorry, but your emails don't seem to match.");
    document.forms["contractorForm"]['eAddress'].style.borderColor="red";
    document.forms["contractorForm"]['confirmEAddress'].style.borderColor="red";
} else {
    document.forms["contractorForm"]['eAddress'].style.borderColor="rgb(112,111,111)";
    document.forms["contractorForm"]['confirmEAddress'].style.borderColor="rgb(112,111,111)";
    }
}

function validPostcode(postcodeinQ) {
    let postcode = postcodeinQ.replace(/\s/g, "");
    let regex = /^[A-Z]{1,2}[0-9]{1,2}[A-Z]{0,1} ?[0-9][A-Z]{2}$/i;
    return regex.test(postcode);
}

function confirmPasswords() {
  let pass = document.forms["contractorForm"]['password'].value;
  let confirmPassword = document.forms["contractorForm"]['confirmPassword'].value;
  if(pass != confirmPassword) {
    alert("Sorry, but your passwords don't seem to match.");
    document.forms["contractorForm"]['password'].style.borderColor="red";
    document.forms["contractorForm"]['confirmPassword'].style.borderColor="red";
} else {
    document.forms["contractorForm"]['password'].style.borderColor="rgb(112,111,111)";
    document.forms["contractorForm"]['confirmPassword'].style.borderColor="rgb(112,111,111)";
    }
}

function agreement() {
  if (document.getElementById("checkBox").checked == true){
    let date = new Date();
    let timeStamp = date.getDate()+"/"+(date.getMonth()+1)+"/"+date.getFullYear()+" "+date.getHours()+":"+date.getMinutes();
    let firstName = document.forms["contractorForm"]['firstName'].value;
    let surname = document.forms["contractorForm"]['surname'].value;
    document.getElementById("signature").innerHTML= firstName+" "+surname+" "+timeStamp;
  }
  else {
    document.getElementById("signature").innerHTML = " ";
  }
}

function hide(){
  let removeIt = document.getElementById('removed');
  let removeIt1 = document.getElementById('removed1');
  let removeIt2 = document.getElementById('removed2');
  let option = document.forms["contractorForm"]["eligibility"].value
  let option1 = document.forms["contractorForm"]["criminalConviction"].value
  let option2 = document.forms["contractorForm"]["disability"].value

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
