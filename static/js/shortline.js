document.getElementById("options").addEventListener("change",function(){
    if(document.getElementById("options").value == "Unsymmmentrical"){
        document.getElementById("sym").style.display = "none";
        document.getElementById("unsym").style.display = "block";
    }
    else{
        document.getElementById("sym").style.display = "block";
        document.getElementById("unsym").style.display = "none";
    }
});

function shortline(){
    window.open("/shortline","_self");
}
function mediumline(){
    window.open("/mediumline","_self");
}
function longline(){
    window.open("/longline","_self");
}
function models()
{
    window.open("/models","_self");
}
function about()
{
    window.open("https://en.wikipedia.org/wiki/Transmission_line","_self");
}
function root()
{
    window.open("/","_self");
}



