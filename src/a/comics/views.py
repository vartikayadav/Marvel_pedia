from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Comics
from django.core.paginator import Paginator,InvalidPage,EmptyPage
# Create your views here.

def comicsfun(request):
    comics_page=Comics.objects.all()
    paginator=Paginator(comics_page,9)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products = paginator.page(page)
    except(InvalidPage,EmptyPage):
        products=paginator.page(paginator.num_pages)


    return render(request,"comics/comics.html",{"products":products})
def comicsfun2(request,c_slug):
    try:
        products=get_object_or_404(Comics,slug=c_slug)
    except Exception as e:
        raise e
    return render(request,"comics/comics2.html",{"products":products})
