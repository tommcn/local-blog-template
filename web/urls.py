from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('view', views.view, name='view'),
    path('add', views.add, name='add'),
    path('info', views.info, name='info'),
    path('blog', views.blog, name='blog'),
]