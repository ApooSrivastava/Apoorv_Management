from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import login, logout

# from django.contrib.auth import authenticate, login , logout
# from django.contrib.auth.views import login
def home(request):
    if request.user.is_authenticated:
        return render(request, 'User/views.py')
    else:
        return redirect('User/views.py')
    


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = user.objects.get(username=username)
        if user.password == password:
            login(request, user)
            return redirect('WorkOrder')
        else:
            return render(request, 'User/views.py', {'error':'invalid username or password'})
    else:
        return render (request, 'User/views.py')


def logout__user(request):
    logout(request)
    return redirect('User/views.py')
    
