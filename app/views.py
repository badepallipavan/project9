from django.shortcuts import render

# Create your views here.
def pavan(request):
    return render(request,'pavan.html',context={'name':'pavan','age':10})

def pavan2(request):
    return render(request,'pavan2.html',context={'name':'pavan2','age':12})