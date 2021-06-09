from django.core.paginator import Paginator,InvalidPage

def getPage(request,objects,filter,obj_per_page=10):
    page_get = request.GET.get("page")
    objectfilter = filter(request.GET, queryset=objects)
    objects = objectfilter.qs
    p = Paginator(objects, obj_per_page)
    try:
        page = p.page(page_get)
    except InvalidPage:
        page = p.page(1)
    return page