function addForm() {
  fieldlist = ["'title'", "'firstName'", "'surname'", "'gender'", "'dob'", "'niNumber'", "'eAddress'", "'contactNumber'",
                   "'postCode'", "'addressLine1'", "'addressLine2'", "'addressLine3'", "'town'", "'emergContact'",
                   "'emergContactNumber'", "'workReq'", "'quali'", "'nameOfCompany'", "'eligibility'",
                   "'proofOfEligibility'", "'licence'", "'criminalConviction'", "'criminalDetails'", "'disability'",
                   "'disabilityDetails'", "'refereeName1'", "'refereeJob1'", "'refereeComp1'", "'refereeAddress1'",
                   "'refereeNum1'","'refereeEmail1'", "'refereeName2'", "'refereeJob2'", "'refereeComp2'", "'refereeNum2'",
                   "'refereeAddress2'", "'refereeEmail2', 'userName', 'passWord'"]
  params =""
  for (i in fieldlist) {
    params += i+"="+document.forms["contractorForm"][i].value+"&";
  }
  cvFile = document.forms["contractorForm"]['CV'];
  picFile = document.forms["contractorForm"]['profileImage'];
  xhttp.open('POST', '/Form', true); // true is asynchronous
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.onload = function() {
    if (xhttp.readyState === 4 && xhttp.status === 200) {
        console.log(xhttp.responseText);
      } else {
        console.error(xhttp.statusText);
      }
    };
    xhttp.send(params);
    xhttp.send(cvFile);
    xhttp.send(picFile);
    return false;
}

function submitLogin(){
  userName = document.forms["loginDetails"]['userName'];
  password = document.forms["loginDetails"]['passWord'];
  uniqueID = document.forms["loginDetails"]['uniqueID'];
  dataValues = 'userName='+userName+'&password='+password+'&uniqueID='+uniqueID;
  xhttp.open('POST', '/Login', true); // true is asynchronous
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.onload = function() {
  if (xhttp.readyState === 4 && xhttp.status === 200) {
      console.log(xhttp.responseText);
    } else {
      console.error(xhttp.statusText);
    }
  };
  xhttp.send(dataValues);
  return false;
}

function adminLogin() {
  username = document.getElementById('userName').value;
  password = document.getElementById('password').value;
  if(username == 'admin' && password == 'admin'){
    xhttp.open('POST', '/Admin', true); // true is asynchronous
  }
}

function confirmEmail() {
  var email = document.forms["contractorForm"]['eAddress'].value;
  var confemail = document.forms["contractorForm"]['confirmEAddress'].value;
  if(email != confemail) {
    alert('Email Not Matching!');
    email.style.borderColor="red";
    confemail.style.borderColor="red";
  } else{
    email.style.borderColor="rgb(112,111,111)";
    confemail.style.borderColor="rgb(112,111,111)";
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
