from django.contrib.auth.models import Group
from Millennium_System import roles
from system_settings.config import values
from espa.models import EspaService

def createDefaultValues(model,default_values,field):
    try:
        objects = default_values
        for object in objects:
            instance = model.objects.filter(service=object) #change service to field
            if not instance.exists():
                model.objects.create(service=object)
    except:
        pass

#AUTHENTICATION
#create initial groups
try:
    groups = roles.INITIAL_GROUPS
    for groupobj in groups:
        group = Group.objects.filter(name=groupobj)
        if not group.exists():
            Group.objects.create(name=groupobj)
except:
    pass

#MODEL VALUES
#create initial espa services
try:
    espaserviceobjects = values.DEFAULT_ESPA_SERVICES
    for espaservice in espaserviceobjects:
        service = EspaService.objects.filter(service=espaservice)
        if not service.exists():
            EspaService.objects.create(service=espaservice)
except:
    pass