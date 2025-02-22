from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import NotFound
from django.core import serializers
from django.http import HttpResponse
from .models import EmissionEvents, SuperfundSite
from .serializers import EmissionEventSerializer, SuperfundSiteSerializer
import requests
import os
from dotenv import load_dotenv
load_dotenv()

class EmissionEventsViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
    serializer_class = EmissionEventSerializer
    queryset = EmissionEvents.objects.all()

    def retrieve(self, request, *args, **kwargs):
        # Get the 're_name' query parameter

        re_name = request.GET.get('re_name', None)
        print('renam', re_name)

        if not re_name:
            sites = EmissionEvents.objects.all()
            serializer = self.get_serializer(sites, many=True)
            return Response(serializer.data)

        # Try to find the EmissionEvents that match the re_name
        event = EmissionEvents.objects.filter(re_name=re_name)

        # Serialize the data and return a single object

        serializer = self.get_serializer(event, many = True)
        return Response(serializer.data)


class SuperfundSiteViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
    serializer_class = SuperfundSiteSerializer
    queryset = SuperfundSite.objects.all()

    def retrieve(self, request, *args, **kwargs):
        # Get the 'epa_id' query parameter
        epa_id = kwargs.get('epa_id') or request.GET.get('epa_id', None)

        if not epa_id:
            sites = SuperfundSite.objects.all()
            serializer = self.get_serializer(sites, many=True)
            return Response(serializer.data)
        # Try to find the SuperfundSite that matches the epa_id
        try:
            site = SuperfundSite.objects.get(epa_id=epa_id)
        except SuperfundSite.DoesNotExist:
            raise NotFound(detail="SuperfundSite with the specified epa_id not found.")
        print("api", os.getenv('GEOCODE_API_KEY'))
        # Serialize the data and return a single object
        
        
    
        street_address = site.street_address.replace(" ", "+")
        zip_code = site.zip_code
        city = site.city
        county = site.county
        state = "TX"
        GEOCODE_API_KEY = os.getenv('GEOCODE_API_KEY')
        country = "US"
        geocode_url = f'https://geocode.maps.co/search?street={street_address}&city={city}&county={county}&state={state}&postalcode={zip_code}&country={country}&api_key={GEOCODE_API_KEY}'
        geocode_response = requests.get(geocode_url)
        geocode_response.raise_for_status()
        geocode_data = geocode_response.json()
        if geocode_data:
            site.lon =  float(geocode_data[0]['lon'])
            site.lat = float(geocode_data[0]['lat'])
            site.save()
            site.refresh_from_db()
        serializer = self.get_serializer(site)
        return Response(serializer.data)

        # try:
        #     # Fetch Superfund data from external API
        #     superfund_response = requests.get(f'http://127.0.0.1:8000/api/superfund/retrieve/?epa_id={epa_id}')
        #     superfund_response.raise_for_status()
        #     superfund_data = superfund_response.json()

        #     # Fetch geocode data from external API
        #     street_address = superfund_data['street_address'].replace(" ", "+")
        #     zip_code = superfund_data['zip_code']
        #     city = superfund_data['city']
        #     county = superfund_data['county']
        #     state = "TX"
        #     GEOCODE_API_KEY = os.getenv('GEOCODE_API_KEY')
        #     country = "US"
        #     geocode_url = f'https://geocode.maps.co/search?street={street_address}&city={city}&county={county}&state={state}&postalcode={zip_code}&country={country}&api_key={GEOCODE_API_KEY}'
        #     geocode_response = requests.get(geocode_url)
        #     geocode_response.raise_for_status()
        #     geocode_data = geocode_response.json()
        #     print("old", geocode_data)

        #     if geocode_data:
        #         superfund_data['long_lat'] = {
        #             'lat': float(geocode_data[0]['lat']),
        #             'long': float(geocode_data[0]['lon'])
        #         }
        #     print("new", geocode_data)

        #     # Update the site data with the fetched data
        #     site_data = self.serializer_class(site).data
        #     site_data.update(superfund_data)

            
        #     return Response(site_data)
        # except requests.exceptions.RequestException as e:
        #     return Response({'error': str(e)}, status=500)
