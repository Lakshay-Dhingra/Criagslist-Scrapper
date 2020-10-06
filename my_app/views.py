from django.shortcuts import render
from . import scrapper
from . import models
from django.utils import timezone

# Create your views here.
def home(request):
    city='delhi'    #default city
    return render(request,'index.html',{'city':city})

def new_search(request):
    search = request.GET['search']
    city = request.GET['city']

    s=models.Search(search=search.lower(),city=city.lower(),created=timezone.now())
    s.save()

    result_list = scrapper.searchResults(city,search)
    context = {'search':search, 'city':city, 'result_list':result_list}
    return render(request,'display_search.html',context)

def about(request):
    return render(request,'about.html')
