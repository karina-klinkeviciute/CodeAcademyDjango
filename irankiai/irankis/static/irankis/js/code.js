
function atsiliepimo_perziura(){
    let atsiliepimas = document.getElementById("id_atsiliepimas")

let atsiliepimas_preview = document.getElementById("atsiliepimas_preview")
atsiliepimas_preview.innerText = atsiliepimas.innerText
}

atsiliepimas.onchange = atsiliepimo_perziura()

document.getElementById("test").style.color = "blue";
document.getElementById("test").style.fontFamily = "Arial";
document.getElementById("test").style.fontSize = "larger";
