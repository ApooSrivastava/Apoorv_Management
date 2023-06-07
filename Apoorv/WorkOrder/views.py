from django.shortcuts import render

# Create your views here.
def workorder(request):
    workorder = workorder.object.all()
    return render(request, 'User/views.py', {'workorder': workorder})