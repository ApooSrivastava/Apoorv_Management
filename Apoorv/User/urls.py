from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home')),
    path('login/', include('login_user')),
    path('logout/', include('logout_user')),
    path('workorder/', include('workorder')),

]