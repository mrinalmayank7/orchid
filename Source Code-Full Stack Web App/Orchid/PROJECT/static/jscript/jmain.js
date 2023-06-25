function myFunction() {
  var x = document.getElementById("myInput");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

let search_input = document.querySelector(".searchbar");
let search_button = document.querySelector(".searchbutton");
search_button.disabled = true;
search_input.addEventListener("change", searchdisable);
function searchdisable() {
    if(document.querySelector(".searchbar").value === "") {
        search_button.disabled = true;
    } else {
        search_button.disabled = false;
    }
}
