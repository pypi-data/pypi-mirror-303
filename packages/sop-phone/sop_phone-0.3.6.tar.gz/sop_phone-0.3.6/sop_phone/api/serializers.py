from django.db.models import Prefetch
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from timezone_field.rest_framework import TimeZoneSerializerField

from netbox.api.fields import ChoiceField
from netbox.api.serializers import NetBoxModelSerializer
from dcim.api.serializers import SiteSerializer
from circuits.api.serializers import ProviderSerializer
from dcim.models import Site

from ..models import *


__all__ = (
    'PhoneDeliverySerializer',
    'PhoneDIDSerializer',
    'PhoneInfoSerializer',
    'PhoneMaintainerSerializer',
)


# Briefs Serializers
# -> | for addditional infos
#    | without modifying original


class SiteBriefSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='dcim-api:site-detail')
    
    class Meta:
        model = Site
        fields = ('id', 'url', 'slug', 'name', 'description')


#_______________________________
# Phone Maintainer


class PhoneMaintainerSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:sop_phone-api:phonemaintainer-detail'
    )
    status = ChoiceField(
        choices=PhoneMaintainerStatusChoice
    )
    site = serializers.SerializerMethodField()
    time_zone = TimeZoneSerializerField(required=False, allow_null=True)

    class Meta:
        model = PhoneMaintainer
        fields = (
            'id', 'url', 'slug', 'display', 'name', 'status',
            'time_zone', 'physical_address', 'shipping_address', 'latitude', 'longitude',
            'description', 'created', 'last_updated', 'site',
        )
        brief_fields = ('id', 'url', 'slug', 'name', 'description')

    def get_site(self, obj):
        phone_infos = PhoneInfo.objects.filter(maintainer=obj).prefetch_related(
            Prefetch('site', queryset=Site.objects.all())
        )
        site = [pi.site for pi in phone_infos if pi.site]
        return SiteBriefSerializer(site, many=True, context=self.context).data


#_______________________________
# Phone Info (Informations)


class PhoneInfoSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:sop_phone-api:phoneinfo-detail'
    )
    site = serializers.SerializerMethodField()
    maintainer = serializers.SerializerMethodField()

    class Meta:
        model = PhoneInfo
        fields = ('id', 'url', 'display', 'site', 'maintainer')

    def get_site(self, obj):
        if not obj.site:
            return None
        return SiteSerializer(obj.site, nested=True, many=False, context=self.context).data

    def get_maintainer(self, obj):
        if not obj.maintainer:
            return None
        maintainer_id = PhoneMaintainer.objects.filter(pk=obj.maintainer.id)
        return PhoneMaintainerSerializer(maintainer_id, nested=True, many=True, context=self.context).data


#_______________________________
# Phone DID (DIDs)


class PhoneDIDSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:sop_phone-api:phonedid-detail'
    )
    delivery = serializers.SerializerMethodField(read_only=True)
    site = serializers.SerializerMethodField()

    class Meta:
        model = PhoneDID
        fields = ('id', 'url', 'site', 'delivery', 'start', 'end')

    def get_site(self, obj):
        if not obj.site:
            return None
        return SiteSerializer(obj.site, nested=True, many=False, context=self.context).data

    def get_delivery(self, obj):
        if not obj.delivery:
            return None
        deliv = PhoneDelivery.objects.filter(pk=obj.delivery.id)
        return PhoneDeliverySerializer(deliv, nested=True, many=True, context=self.context).data


#_______________________________
# Phone Delivery


class PhoneDeliverySerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:sop_phone-api:phonedelivery-detail'
    )
    provider = serializers.SerializerMethodField()
    site = serializers.SerializerMethodField()

    class Meta:
        model = PhoneDelivery
        fields = ('id', 'url', 'display', 'site', 'delivery', 'provider',
            'channel_count', 'status', 'ndi', 'dto',
        )
        brief_fields = ('id', 'url', 'display', 'provider', 'delivery',)

    def get_provider(self, obj):
        if not obj.provider:
            return None
        return ProviderSerializer(obj.provider, nested=True, many=False, context=self.context).data


    def get_site(self, obj):
        if not obj.site:
            return None
        return SiteSerializer(obj.site, nested=True, many=False, context=self.context).data
