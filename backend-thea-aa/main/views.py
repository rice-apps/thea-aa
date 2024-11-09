from django.shortcuts import render

from rest_framework.mixins import (
    CreateModeMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from .models import EmissionEvents, SuperfundSite
from.serializers import EmissionEventSerializer, SuperfundSiteSerializer

class EmissionEventsViewSet(GenericViewSet, CreateModeMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
    serializer_class = EmissionEventSerializer
    queryset = EmissionEvents.objects.all()

class SuperfundSiteViewSet(GenericViewSet, CreateModeMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
    serializer_class = SuperfundSiteSerializer
    queryset = SuperfundSite.objects.all()


