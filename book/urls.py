from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='book_list'),
    path('<int:pk>/detail/', views.DetailView.as_view(), name='book_detail'),
]