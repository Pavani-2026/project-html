

from django.contrib import admin
from django.urls import path
from myapp1 import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.homepage),
    path('about/',views.aboutpage),
    path('contact/',views.contactpage),
]
