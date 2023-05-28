from django.urls import path
from tag import views

urlpatterns = [
    path('tags', views.Tags.as_view(), name='tags'),
    path('add_tag', views.AddTag.as_view(), name='add_tag'),
]


