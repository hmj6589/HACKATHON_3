from django.urls import path
from . import views

app_name="board"

urlpatterns = [
    path('taxi/', views.calculate_taxi_fare, name='taxi'),
    path('create/', views.create, name='create'),
    path('copy/', views.taxi, name="copy"),
    path('map/', views.map, name="map")
]
