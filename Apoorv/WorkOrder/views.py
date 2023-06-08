from django.shortcuts import render, redirect

# Create your views here.
def workorder(request):
    workorder = workorder.object.all()
    return render(request, 'home', {'workorder': workorder})