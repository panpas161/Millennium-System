from django.contrib.auth.models import Group
from system_settings.config import roles
from system_settings.config import values
from espa.models import EspaService

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