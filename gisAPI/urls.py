from django.urls import path
from .views import ListCountry

app_name = "gisAPI"

urlpatterns = [
    path('country/', ListCountry.as_view(), name="country_endpoint"),
]
