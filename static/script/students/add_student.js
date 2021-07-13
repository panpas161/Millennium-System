function VoucherDisplay(vouchermodel)
{
    voucherlabel = document.getElementById("voucherlabel");
    voucherform = document.getElementById("voucherform");
    checkbox = document.getElementById("vouchersame")
    if(checkbox.checked == true)
    {
        voucherlabel.style.display = "none";
        voucherform.style.display = "none";
        voucherform.innerHTML = ""
    }
    else
    {
        voucherlabel.style.display = "";
        voucherform.style.display = "";
        voucherform.innerHTML = vouchermodel;
    }
}
