
from django.contrib import admin
from django.urls import path
from myapp2 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.homepage,name='home'),
    path('about/',views.aboutpage,name='about'),
    path('contact/',views.contactpage,name='contact'),
    path('login/',views.loginpage,name="login"),
    path('register/',views.registerpage,name="register"),
]
