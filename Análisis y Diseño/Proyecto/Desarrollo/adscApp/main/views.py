from django.shortcuts import render
from . import models
# Create your views here.
#Home Page
def home(request):
    banners=models.Banners.objects.all()
    services=models.Servicio.objects.all()[:2]
    return render(request, 'home.html',{'banners':banners,'services':services})
