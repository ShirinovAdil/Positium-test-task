from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from .models import Country
from .serializers import CountrySerializer


class ListCountry(APIView):

    def get(self, request, format=None):
        country = Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def list_all_country(request):
    return render(request, 'list_all_country.html')