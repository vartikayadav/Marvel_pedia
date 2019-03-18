from django.shortcuts import render
from django.db.models import Q
from comics.models import Comics
# Create your views here.
def searchResult(request):
    products=None
    query=None
    query=request.GET.get('q')
    products=Comics.objects.all().filter(Q(title__contains=query) | Q(description__contains=query))
    return render(request,"searchapp/search.html",{'query':query,'products':products})
