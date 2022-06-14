from django.urls import path
from . import views


app_name = 'news'

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('story-detail/<uuid:id>/<slug:slug>/', views.story_detail, name="story_detail"),
]
