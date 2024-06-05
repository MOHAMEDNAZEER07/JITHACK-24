from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('index', views.index, name='index'),
    path('predict', views.predict, name='predict'),
    path('logout',views.logout_view, name='logout'),
    path('result', views.result, name='result'),
]