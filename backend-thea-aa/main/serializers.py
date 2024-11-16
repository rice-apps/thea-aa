from django.urls import path, include
from .models import EmissionEvents, SuperfundSite
from rest_framework.serializers import routers, serializers, viewsets

class EmissionEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmissionEvents
        fields = ['re_name',
            'physical_location',
            'start_date_time',
            'end_date_time',
            'contaminant',
            'estimated_quantity',
            'emissions_limit',
            'limit_units',
            'hours_elapsed',
            'emissions_rate',
            'flag']
        
class EmissionEventViewSet(viewsets.ModelViewSet):
    queryset = EmissionEvents.objects.all()
    serializer_class = EmissionEventSerializer

class SuperfundSiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SuperfundSite
        fields = []
        
class SuperfundSiteViewSet(viewsets.ModelViewSet):
    queryset = SuperfundSite.objects.all()
    serializer_class = SuperfundSiteSerializer

router = routers.DefaultRouter()
router.register(r'Emission Events', EmissionEventViewSet)
router.register(r'Superfund Sites', SuperfundSiteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]