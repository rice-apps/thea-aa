"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from main.views import EmissionEventsViewSet, SuperfundSiteViewSet
from django.urls import path
from main.models import EmissionEvents

router = DefaultRouter()
router.register(r'emission', EmissionEventsViewSet)
router.register(r'superfund', SuperfundSiteViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    
    path("api/superfund/retrieve/<str:epa_id>/", SuperfundSiteViewSet.as_view({'get': 'retrieve'})),  # Custom endpoint
    path("api/emissions/retrieve/<str:re_name>/", EmissionEventsViewSet.as_view({'get': 'retrieve'}))   # Custom endpoint
]

#http://127.0.0.1:8000/api/superfund/retrieve/?epa_id=TX0000605401
