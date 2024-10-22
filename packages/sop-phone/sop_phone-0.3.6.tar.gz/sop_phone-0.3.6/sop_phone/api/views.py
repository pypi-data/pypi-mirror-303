from netbox.api.viewsets import NetBoxModelViewSet
from netbox.api.metadata import ContentTypeMetadata

from ..models import *
from ..filtersets import *
from .serializers import *


__all__ = (
    'PhoneDeliveryViewSet',
    'PhoneDIDViewSet',
    'PhoneInfoViewSet',
    'PhoneMaintainerViewSet',
)

class PhoneMaintainerViewSet(NetBoxModelViewSet):
    metadata_class = ContentTypeMetadata
    queryset = PhoneMaintainer.objects.all()
    serializer_class = PhoneMaintainerSerializer
    filterset_class = PhoneMaintainerFilterSet


class PhoneInfoViewSet(NetBoxModelViewSet):
    metadata_class = ContentTypeMetadata
    queryset = PhoneInfo.objects.all()
    serializer_class = PhoneInfoSerializer
    filterset_class = PhoneInfoFilterSet


class PhoneDIDViewSet(NetBoxModelViewSet):
    metadata_class = ContentTypeMetadata
    queryset = PhoneDID.objects.all()
    serializer_class = PhoneDIDSerializer
    filterset_class = PhoneDIDFilterSet


class PhoneDeliveryViewSet(NetBoxModelViewSet):
    metadata_class = ContentTypeMetadata
    queryset = PhoneDelivery.objects.all()
    serializer_class = PhoneDeliverySerializer
    filterset_class = PhoneDeliveryFilterSet
