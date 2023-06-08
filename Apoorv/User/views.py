from django.shortcuts import render, redirect

# Create your views here.
# from django.shortcuts import login, logout

# from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
def home(request):
    if request.user.is_authenticated:
        return render(request, 'login_user')
    else:
        return redirect('home')
    


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = user.objects.get(username=username)
        if user.password == password:
            LoginView(request, user)
            return redirect('workorder')
        else:
            return render(request, 'login_user', {'error':'invalid username or password'})
    else:
        return render (request, 'home')


def logout_user(request):
    LogoutView(request)
    return redirect('home')
    
