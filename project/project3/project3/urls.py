
from django.contrib import admin
from django.urls import path
from myapp3 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.homepage,name="home"),
    path('contact/',views.contactpage,name="contact"),
    path('register/',views.registerpage,name="register"),
    path('login/',views.loginpage,name="login"),
    path('showdetails/',views.showdetails,name="showdetails"),
    path('delete/',views.delete,name="delete"),
    path('update/',views.update,name="update"),
]
