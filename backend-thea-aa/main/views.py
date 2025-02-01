from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import NotFound
from .models import EmissionEvents, SuperfundSite
from .serializers import EmissionEventSerializer, SuperfundSiteSerializer

class EmissionEventsViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
    serializer_class = EmissionEventSerializer
    queryset = EmissionEvents.objects.all()

    def retrieve(self, request, *args, **kwargs):
        # Get the 're_name' query parameter
        re_name = request.GET.get('re_name', None)

        if not re_name:
            return Response({"detail": "re_name query parameter is required."}, status=400)

        # Try to find the EmissionEvent that matches the re_name
        try:
            event = EmissionEvents.objects.get(re_name=re_name)
        except EmissionEvents.DoesNotExist:
            raise NotFound(detail="EmissionEvent with the specified re_name not found.")

        # Serialize the data and return a single object
        serializer = self.serializer_class(event)
        return Response(serializer.data)


class SuperfundSiteViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
    serializer_class = SuperfundSiteSerializer
    queryset = SuperfundSite.objects.all()

    def retrieve(self, request, *args, **kwargs):
        # Get the 'epa_id' query parameter
        epa_id = request.GET.get('epa_id', None)

        if not epa_id:
            return Response({"detail": "epa_id query parameter is required."}, status=400)

        # Try to find the SuperfundSite that matches the epa_id
        try:
            site = SuperfundSite.objects.get(epa_id=epa_id)
        except SuperfundSite.DoesNotExist:
            raise NotFound(detail="SuperfundSite with the specified epa_id not found.")

        # Serialize the data and return a single object
        serializer = self.serializer_class(site)
        return Response(serializer.data)
