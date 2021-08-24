from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='Home page'),
    path('contactus',views.contactus,name='Contact'),
    path('contribute',views.contribute,name='contribute')
]