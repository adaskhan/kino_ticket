from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('news/', views.news, name='news'),
    path('feedback/', views.feedback, name='feedback'),
    path('contacts/', views.contacts, name='contacts'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('film/<int:pk>/', views.film, name='film'), # film/5/
    path('session/<int:pk>/', views.session, name='session'),
    path('sort/<int:pk>/', views.sort, name='sort'),
    path('pay/<int:pk>/', views.pay_with_robokassa, name='pay'),
    path('history/', views.history, name='history'),
    path('review/<int:pk>/', views.review, name='review'),
    path('delete/<int:pk>/', views.deleteticket, name='delete'),
    path('seat/<int:pk>/', views.seats, name='seat'),
    path('logout/', views.user_logout, name='logout'),
]
