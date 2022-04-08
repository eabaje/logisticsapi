from loadboardapi.viewset import *
from rest_framework import routers

router=routers.DefaultRouter()
router.register('driver',DriverViewSet)