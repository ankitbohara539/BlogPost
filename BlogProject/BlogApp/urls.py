from .import views
from django.urls import path

urlpatterns = [
    path('', views.loginpage, name='login'),  
    path('logout/', views.logout_page, name='logout'),  
    path('home/', views.home, name='home'),  
    path('userbase/', views.userbase, name='userbase'), 
    path('blog/', views.blog_cards, name='blog_cards'),
    path('register/', views.register, name ='register'), 
    path('about/', views.about, name ='about'),  

   

    # blog urls

    path('blog_list/', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/new/', views.blog_create, name='blog_create'),
    path('blog/<int:pk>/edit/', views.blog_edit, name='blog_edit'),
    path('blog/<int:pk>/delete/', views.blog_delete, name='blog_delete'),
    path('blogs/<int:pk>/', views.blogdetail, name='blogdetail'),
]