from django.urls import path
from . import views

urlpatterns = [
    path('', views.ExclusiveListView.as_view()),
    path('<int:pk>/', views.ExclusiveDetailView.as_view()),
]
