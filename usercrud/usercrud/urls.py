from django.urls import path
from django.contrib import admin
from userapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.user_register, name='user_register'),
]