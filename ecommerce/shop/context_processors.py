from .models import category

def menu_links(request):
    n=category.objects.all()
    return {'links':n}
