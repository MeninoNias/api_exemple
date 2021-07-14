from django.urls import path, include
from rest_framework import routers

from api.views import NoticiaViewSet

router = routers.DefaultRouter()
router.register(r'noticias', NoticiaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
