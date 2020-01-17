from rest_framework import routers

from sneakers_colors_sizes_rel.api import SneakersColorsSizesRelViewSet, SneakersColorsSizesRelSearch

router = routers.DefaultRouter()
router.register('api/v0/sneak_col_siz_rel', SneakersColorsSizesRelViewSet, 'sneak_col_siz_rel')

urlpatterns = router.urls
