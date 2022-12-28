from django.urls import path, include
from rest_framework import routers
from .views import familyViewset

router = routers.DefaultRouter()
router.register(r'api/get-family', familyViewset)

urlpatterns = [
    path('', include(router.urls)),
]
