from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import team
def demo(request):
    obj = place.objects.all()
    obj1 = team.objects.all()
    return render(request,"index.html",{'result':obj,'member':obj1})
# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return HttpResponse("hoi")

# Create your views here.
