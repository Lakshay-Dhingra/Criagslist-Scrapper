from django.shortcuts import render
from . import scrapper

# Create your views here.
def home(request):
    city='delhi'    #default city
    return render(request,'index.html',{'city':city})

def new_search(request):
    search = request.GET['search']
    city = request.GET['city']
    result_list = scrapper.searchResults(city,search)
    context = {'search':search, 'city':city, 'result_list':result_list}
    return render(request,'display_search.html',context)

def about(request):
    return render(request,'about.html')
