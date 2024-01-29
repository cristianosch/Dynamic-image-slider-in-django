from django.shortcuts import render
from .models import Carousel

# Create your views here.
def home_view(request):
    carousel = Carousel.objects.all()
    context  = {
        'carousel' : carousel
    }
    return render(request, "index.html", context)