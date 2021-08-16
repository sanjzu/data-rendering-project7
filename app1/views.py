from django.shortcuts import render

# Create your views here.
def sanju(request):
    return render(request,'sanju.html',context={'name':'pavan','age':22})