
function confirmEmail() {
  var email = document.forms["contractorForm"]['eAddress'].value;
  var confemail = document.forms["contractorForm"]['confirmEAddress'].value;
  if(email != confemail) {
    alert('Email Not Matching!');
    email.style.borderColor="red";
    confemail.sytle.borderColor="red";
  } else{
    email.style.borderColor="rgb(112,111,111)";
    confemail.sytle.borderColor="rgb(112,111,111)";
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
