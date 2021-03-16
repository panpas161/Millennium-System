from ..models import Teacher

def getAvailableDays():
    days = [
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'sunday'
    ]
    return days

def getSelectedDays(request):
    days = getAvailableDays()
    selected_days = [None] * len(days)
    for i in range(0, len(days)):
        if days[i] in request.POST:
            selected_days[i] = days[i]
    return selected_days

def getSelectedTeachers(request):
    days = getSelectedDays(request)
    selected_teachers = [None] * len(days)
    for i in range(0, len(selected_teachers)):
        if days[i] is not None:
            selected_teachers[i] = Teacher.objects.get(id=request.POST[days[i] + "teacher"])
    return selected_teachers

def getSelectedDuration(request):
    days = getSelectedDays(request)
    durations = [None] * len(days)
    for i in range(0,len(days)):
        if str(days[i]) + "duration" in request.POST:
            durations[i] = request.POST[str(days[i]) + "duration"]
    return durations

def getSelectedStartTime(request):
    days = getSelectedDays(request)
    start_time_inputs = [None] * len(days)
    for i in range(0,len(days)):
        if str(days[i]) + "start" in request.POST:
            start_time_inputs[i] = request.POST[str(days[i]) + "start"]
    return start_time_inputs

def getSelectedEndTime(request):
    days = getSelectedDays(request)
    end_time_inputs = [None] * len(days)
    for i in range(0,len(days)):
        if str(days[i]) + "end" in request.POST:
            end_time_inputs[i] = request.POST[str(days[i]) + "end"]
    return end_time_inputs