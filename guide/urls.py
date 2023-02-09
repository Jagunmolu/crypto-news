from django.urls import path

from . import views

urlpatterns = [
    path('', views.GuideListView.as_view()),
    path('<int:pk>/', views.GuideDetailView.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
