from django.urls import path
from . import views

urlpatterns = [
    path('', views.ExclusiveListView.as_view()),
    path('<int:pk>/', views.ExclusiveDetailView.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
