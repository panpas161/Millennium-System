function getDays()
{
    days = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday"
    ];
    return days;
}
function disableInputs(exception)
{
    days = getDays();
    checkboxInputs = new Array(days.length);
    startTimeInputs = new Array(days.length);
    endTimeInputs = new Array(days.length);
    durationInputs = new Array(days.length);
    remarksInputs = new Array(days.length);
    teacherInputs = new Array(days.length);
    for(i=0;i<days.length;i++)
    {
        checkboxInputs[i] = days[i];
        startTimeInputs[i] = days[i] + "start";
        endTimeInputs[i] = days[i] + "end";
        durationInputs[i] = days[i] + "duration";
        remarksInputs[i] = days[i] + "remarks";
        teacherInputs[i] = days[i] + "teacher";
    }

    for(i=0;i<days.length;i++)
    {
        if(checkboxInputs[i] != exception)
        {
            document.getElementsByName(startTimeInputs[i])[0].disabled = true;
            document.getElementsByName(endTimeInputs[i])[0].disabled = true;
            document.getElementsByName(durationInputs[i])[0].disabled = true;
            document.getElementsByName(remarksInputs[i])[0].disabled = true;
            document.getElementsByName(teacherInputs[i])[0].disabled = true;
        }
        if(checkboxInputs[i] == exception)
        {
            document.getElementsByName(startTimeInputs[i])[0].disabled = false;
            document.getElementsByName(endTimeInputs[i])[0].disabled = false;
            document.getElementsByName(durationInputs[i])[0].disabled = false;
            document.getElementsByName(remarksInputs[i])[0].disabled = false;
            document.getElementsByName(teacherInputs[i])[0].disabled = false;
        }
    }
}
function addCheckboxListeners()
{
    days = getDays();
    for(i=0;i<days.length;i++)
    {
        document.getElementsByName(days[i])[0].addEventListener("change",() => disableInputs(days[i]));

    }
}


//.addEventListener("load",disableInputs);
//window.addEventListener("load",addCheckboxListeners);