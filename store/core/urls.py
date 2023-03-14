from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items', views.items, name='items'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('register', views.register, name='register'),
    path('browse', views.browse, name='browse'),
]