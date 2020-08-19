from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ExploreListView.as_view(), name='explore')
]