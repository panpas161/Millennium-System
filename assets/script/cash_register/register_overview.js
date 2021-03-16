window.onload = function (){
    changeTotalColor(document.getElementById("totalrevenue"));

}
function changeTotalColor(element)
{
    var total = element;
    var totalfloat = parseFloat(element.innerText);
    if(totalfloat>0)
    {
        total.style.color="green";
    }
    else if(totalfloat<0)
    {
        total.style.color="red";
    }
    else
    {
        total.style.color="grey";
    }
}