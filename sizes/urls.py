from rest_framework import routers

from sizes.api import SizesViewSet

router = routers.DefaultRouter()
router.register('api/v0/sizes', SizesViewSet, 'sizes')

urlpatterns = router.urls
