from django.urls import path
from django.conf import settings



from . import views 

urlpatterns = [
     path('', views.home, name='home'),
     path('getQuestions/', views.ajax_posting, name='ajax_posting'),
]