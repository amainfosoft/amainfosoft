from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    #path('sending_email',views.sending_email,name='sending_email')
]
