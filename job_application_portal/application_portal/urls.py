from django.urls import path
from . import views

urlpatterns = [
    path('', views.detailsView, name='index'),
    path('register', views.registerView.as_view(), name='register'),
    path('login', views.loginView.as_view(), name='login'),
    path('logout', views.logoutView, name='logout'),
    path('details', views.detailsView, name='details'),
    path('thank_you', views.messageView.as_view(), name='thank_you'),
    path('submit', views.submitView, name='submit')
]
