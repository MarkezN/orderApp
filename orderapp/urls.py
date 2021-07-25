from django.urls import path    
from . import views


urlpatterns = [
   
    path('', views.home_view, name='home_view'),
    path('register/', views.reg_view, name='reg_view'),
    path('login/', views.log_view, name='log_view'),
    path('logout/', views.logout_view, name='logout'),
    
]