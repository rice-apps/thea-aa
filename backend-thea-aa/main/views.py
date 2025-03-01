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
from collections import defaultdict
from dotenv import load_dotenv
load_dotenv()

class EmissionEventsViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
    serializer_class = EmissionEventSerializer
    queryset = EmissionEvents.objects.all()

    def retrieve(self, request, *args, **kwargs):
        """
        API to retrieve emission events but group data by `registration` ID
        so each unique registration contains a list of contaminants.
        """
        # get the registration ID from the request
        re_name = kwargs.get('re_name') or request.GET.get('re_name', None)

        if not re_name:
            events = EmissionEvents.objects.all()
        else:
            # filter all the objests with the given registration
            events = EmissionEvents.objects.filter(re_name=re_name)

        # if the registration id is invalid
        if not events.exists():
            raise NotFound(detail="No emission events found for this registration.")

        # serialize the filtered data into json 
        serialized_data = EmissionEventSerializer(events, many=True).data
        # print('serialized data', serialized_data)

        GEOCODE_API_KEY = os.getenv('GEOCODE_API_KEY')
        geocode_url = f'https://geocode.maps.co/search?q={serialized_data[0]["physical_location"]}&api_key={GEOCODE_API_KEY}'
        geocode_response = requests.get(geocode_url)
        geocode_response.raise_for_status()
        geocode_data = geocode_response.json()
        default_lat = None
        default_lon = None
        if geocode_data:
            default_lat =  float(geocode_data[0]['lat'])
            default_lon = float(geocode_data[0]['lon'])
        print(default_lat, default_lon)

        # define new entry type where contaminants is a list
        aggregated_data = defaultdict(lambda: {
            "registration": "",
            "re_name": "",
            "physical_location": "",
            "lat": default_lat,
            "lon": default_lon,
            "region_id": "",
            "event_type": "",
            "emission_point_name": "",
            "epn": "",
            "start_date_time": "",
            "end_date_time": "",
            "hours_elapsed": "",
            "emissions_rate": "",
            "authorization_comment": "",
            "cause": "",
            "actions_taken": "",
            "basis_used": "",
            "initial_notice": "",
            "flag": "",
            "contaminants": []  
        })

        # Process each event and group by registration
        for event in serialized_data:
            reg_id = event["registration"]

            if not aggregated_data[reg_id]["registration"]:
                time = float(event["hours_elapsed"])
                if time < 1:

                    formatted_time = str(round(time * 60, 2)) + " Minutes"
                else:
                    formatted_time = str(round(time, 0)) + " Hours"

                print(formatted_time)

                # Populate main details that are unique
                aggregated_data[reg_id].update({
                    "registration": event["registration"],
                    "re_name": event["re_name"],
                    "physical_location": event["physical_location"],
                    "region_id": event["region_id"],
                    "event_type": event["event_type"],
                    "emission_point_name": event["emission_point_name"],
                    "epn": event["epn"],
                    "start_date_time": event["start_date_time"],
                    "end_date_time": event["end_date_time"],
                    "hours_elapsed": formatted_time,
                    "emissions_rate": event["emissions_rate"],
                    "authorization_comment": event["authorization_comment"],
                    "cause": event["cause"],
                    "actions_taken": event["actions_taken"],
                    "basis_used": event["basis_used"],
                    "initial_notice": event["initial_notice"],
                    "flag": event["flag"]
                })

            # Populate each contaminant data into the contaminant list
            aggregated_data[reg_id]["contaminants"].append({
                "name": event["contaminant"],
                "est_quantity": event["contaminant_est_quantity"],
                "quantity_unit": event["contaminant_est_quantity_units"],
                "emission_limit": event["contaminant_emissions_limit"],
                "emission_limit_unit": event["contaminant_emissions_limit_units"],
                "authorization": event["authorization"]
            })

        # Convert defaultdict to list of values
        return Response(list(aggregated_data.values()))


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
