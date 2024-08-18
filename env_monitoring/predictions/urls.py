from django.urls import path
from . import views

urlpatterns = [
    path('predict/flood/', views.predict_flood, name='predict_flood'),
    path('predict/landslide/', views.predict_landslide, name='predict_landslide'),
    path('', views.index, name='index'),
]
