from rest_framework import routers

from sneakers.api import SneakersViewSet

router = routers.DefaultRouter()
router.register('api/v0/sneakers', SneakersViewSet, 'sneakers')

urlpatterns = router.urls
