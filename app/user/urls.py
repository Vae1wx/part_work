from django.urls import path
from . import views





urlpatterns = [
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('user/', views.UserList.as_view(), name='user'),
    
]



