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
