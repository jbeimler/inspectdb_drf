from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.decorators import api_view
from api.views import GeneralViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter
import inspect

import api.models 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("pages.urls")),    
   re_path(r'^api/(?P<model>\w+)', GeneralViewSet.as_view({'get':'list'}))
]

router = SimpleRouter()
# for name, obj in inspect.getmembers(api.models):
#      router.register(f"{name.lower()}", GeneralViewSet, basename='api2')
router.register("api2", GeneralViewSet, basename="hosts")
print(router.urls)
#urlpatterns = urlpatterns.append(router.urls)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
