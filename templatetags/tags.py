from django import template
from Millennium_System import settings
from django.utils.safestring import mark_safe
register = template.Library()

@register.simple_tag(name="image")
def getImageURL(url):
    return settings.IMAGES_URL + url

@register.simple_tag(name="media")
def getMediaURL(url):
    return settings.MEDIA_URL + url

@register.simple_tag(name="style")
def getStyleURL(url):
    return settings.STYLE_URL + url

@register.simple_tag(name="script")
def getScriptURL(url):
    return settings.SCRIPT_URL + url

@register.simple_tag(name="loadBootstrap")
def getBoostrap():
    return mark_safe("<link rel='stylesheet' href='"  + settings.BOOTSTRAP_URL + "css/bootstrap.css'><script src='" + settings.BOOTSTRAP_URL + "js/bootstrap.js'></script><link rel='stylesheet' href='" + settings.BOOTSTRAP_URL +"css/bootstrap-fixer.css' />")
#     return mark_safe("""<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous"><script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
# """)

@register.simple_tag(name="loadJQuery")
def getJQuery():
    return mark_safe("""<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>""")

@register.simple_tag(name="changename")
def changeElementName(element,current_name,name):
    element = str(element)
    element = element.replace("name=" + "\"" + str(current_name) + "\"","name=" + str(name))
    return mark_safe(element)

@register.simple_tag(name="split")
def splitString(value,delimiter,pos):
    return value.split(delimiter)[pos]

@register.filter
def hash(h, key):
    try:
        return h[key]
    except:
        return None
