from django.urls import path
from . import views
urlpatterns =[
    path('check/', views.check_URL),
    path('', views.check_data),  
]