// pridedam atsiliepimo peržiūrą žemiau atsiliepimo. Kai rašom atsiliepimą teksto lauke,
// jį rodo ir po juo.
function atsiliepimo_perziura(){
    let atsiliepimas = document.getElementById("id_atsiliepimas")
    let atsiliepimas_preview = document.getElementById("atsiliepimas_preview")
    atsiliepimas_preview.innerText = atsiliepimas.value
}

let atsiliepimas = document.getElementById("id_atsiliepimas")

atsiliepimas.addEventListener("keyup", atsiliepimo_perziura)

document.getElementById("test").style.color = "blue";
document.getElementById("test").style.fontFamily = "Arial";
document.getElementById("test").style.fontSize = "larger";
