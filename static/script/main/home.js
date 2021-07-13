function changeTab(tabString)
{
    var tabs = ["registar","students","robotics","agrotika","efet","securityex","voucher","laek","jobcarrier"];
    var i;
    for(i=0;i<tabs.length;i++)
    {
        if(document.getElementById(tabs[i]).style.display == "block")
        {
            document.getElementById(tabs[i]).style.display = "none";
        }
    }
        document.getElementById(tabString).style.display = "block";
}
function autoHideMessages()
{
    successmessage = document.getElementById("successmessage");
    setTimeout(function ()
        {
            successmessage.style.display = "none";
        },3000
    )
}
function hideMessages()
{
    successmessage = document.getElementById("successmessage");
    successmessage.style.display= "none";
}
window.onload = autoHideMessages();