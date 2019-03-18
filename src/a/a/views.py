from django.shortcuts import render
from fun import info

def basefun(request):
    if request.method=='POST':
        x=request.POST['character']
        res=info.getCharacters(x)
        #print(res)
        context={
        'res':res,

        }
    if request.method=='GET':
        res=info.getCharacters('A')
        context={
        'res':res,

        }
    return render(request,"index.html",context)
