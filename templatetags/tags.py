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

@register.simple_tag(name="changename")
def changeElementName(element,current_name,name):
    element = str(element)
    element = element.replace("name=" + "\"" + str(current_name) + "\"","name=" + str(name))
    return mark_safe(element)