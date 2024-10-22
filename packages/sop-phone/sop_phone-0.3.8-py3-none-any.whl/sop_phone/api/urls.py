from netbox.api.routers import NetBoxRouter

from .views import *


router = NetBoxRouter()

router.register('phone-deliveries', PhoneDeliveryViewSet)
router.register('phone-dids', PhoneDIDViewSet)
router.register('phone-infos', PhoneInfoViewSet)
router.register('phone-maintainers', PhoneMaintainerViewSet)

urlpatterns = router.urls
