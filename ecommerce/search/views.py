from django.shortcuts import render
from django.db.models import Q
from shop.models import Product
def searchresults(request):
    query=""
    products=None
    if(request.method=="POST"):
        query=request.POST['q']
        if(query):
            products=Product.objects.filter(Q(name__icontains=query)|Q(description__icontains=query))
    return render(request,'search.html',{'products':products,'query':query})
