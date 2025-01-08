from django.shortcuts import render

# Create your views here.
def landing_render(request):
    return render(request, "pages/landing.html")