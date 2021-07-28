from django.urls import path    
from .import views
from django.conf import settings    
from django.conf.urls.static import static



urlpatterns = [
   
    path('', views.home_view, name='home_view'),
    path('register/', views.reg_view, name='reg_view'),
    path('login/', views.log_view, name='log_view'),
    path('logout/', views.logout_view, name='logout'),
    #path('file/', views.upload_file, name='upload_file'),
    path('upload/', views.upload_pdfs, name='upload'),
    path('pdfs/', views.pdfs_list, name='list'),
    path('pdfs/<int:pk>/', views.delete_file, name='delete_file')
    
]

if settings.DEBUG:   
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)