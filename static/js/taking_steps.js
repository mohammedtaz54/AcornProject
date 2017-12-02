
var parent = document.getElementById('contractorForm');
var hidden = document.getElementsByClassName("progress");
var click = document.forms["contractorForm"]["niNumber"].value;

for(var i = 0; hidden != 0; i++){
hidden[i].style.display = "none"
};

function validateIt(){


}

function progression() {

    if (hidden[0].style.display === "none") {
        hidden[0].style.display = "block";
    } else {
        hidden[0].style.display = "none";
    }
}

var option = document.forms["contractorForm"]["niNumber"].value;
