from .models import User,categorys
def categories(request):
    return {
        'categories': categorys.objects.all()
    }