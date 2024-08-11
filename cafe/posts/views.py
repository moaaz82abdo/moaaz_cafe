from django.shortcuts import render
from .models import Article

# Create your views here.
def home(request):
    return render(request, "index.html")
def addarticle(request):
   if request.method == 'POST' :
      if request.POST.get('name') and request.POST.get('email') and request.POST.get('messege') :
          table = Article()
          table.name = request.POST.get('name')
          table.email = request.POST.get('email')
          table.messege = request.POST.get('messege')
          table.save()
          return render(request, "index.html")
   else: 
       return render(request, "index.html")      
