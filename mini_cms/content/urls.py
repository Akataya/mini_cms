from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:pk>/', views.section, name="section"),
    path('offices/', views.OfficeListView.as_view(), name="offices"),
]
