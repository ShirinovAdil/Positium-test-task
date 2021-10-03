from django.urls import path, include
from gisAPI import views

urlpatterns = [
    path('api/v1/', include("gisAPI.urls")),
    path('home/', views.list_all_country),
]
