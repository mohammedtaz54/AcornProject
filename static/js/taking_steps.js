
var parent = document.getElementById('contractorForm');
var hidden = document.getElementsByClassName("progress");
var click = document.forms["contractorForm"]["niNumber"].value;
var personal = document.getElementsByClassName('personalDetails');

for(var i = 0; hidden != 0; i++){
hidden[i].style.display = "none";
if (i === 9) { break; }

}
function validateIt(){
if(personal == ""){
alert("stop")
}
}

function progression() {

    if (hidden[0].style.display === "none") {
        hidden[0].style.display = "block";
    } else {
        hidden[0].style.display = "none";
    }
}

function progression1() {

    if (hidden[1].style.display === "none") {
        hidden[1].style.display = "block";
    } else {
        hidden[1].style.display = "none";
    }
}

function progression2() {

    if (hidden[2].style.display === "none") {
        hidden[2].style.display = "block";
    } else {
        hidden[2].style.display = "none";
    }
}

function progression3() {

    if (hidden[3].style.display === "none") {
        hidden[3].style.display = "block";
    } else {
        hidden[3].style.display = "none";
    }
}

function progression4() {

    if (hidden[4].style.display === "none" && hidden[5].style.display === "none"  && hidden[6].style.display === "none") {
        hidden[4].style.display = "block";
        hidden[5].style.display = "block";
        hidden[6].style.display = "block";
    } else {
        hidden[4].style.display = "none";
        hidden[5].style.display = "none";
        hidden[6].style.display = "none";
    }
}
