from rest_framework import routers

from colors.api import ColorsViewSet

router = routers.DefaultRouter()
router.register('api/v0/colors', ColorsViewSet, 'colors')

urlpatterns = router.urls
