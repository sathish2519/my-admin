from django.shortcuts import render

def dashboard(request):
    return render(request,"dashboard/dashboard.html")
    
def dashboard2(request):
    return render(request,"dashboard/dashboard2.html")
# Create your views here.
