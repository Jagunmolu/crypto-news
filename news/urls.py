from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from news import views

urlpatterns = [
    path('', views.PostListView.as_view()),
    path('<int:pk>/', views.PostDetailView.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)