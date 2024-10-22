from django import forms
from django.utils.translation import gettext_lazy as _

from circuits.models import Provider
from utilities.forms import add_blank_choice
from utilities.forms.fields import SlugField
from dcim.models import Site, Region, SiteGroup
from utilities.forms.fields import DynamicModelChoiceField, CommentField
from netbox.forms import NetBoxModelFilterSetForm, NetBoxModelForm, NetBoxModelBulkEditForm
from utilities.forms.rendering import FieldSet

from ..models import *


__all__ = (
    'PhoneDeliveryForm',
    'PhoneDeliveryFilterForm',
    'PhoneDeliveryBulkEditForm',
)


class PhoneDeliveryFilterForm(NetBoxModelFilterSetForm):
    model = PhoneDelivery

    site_id = DynamicModelChoiceField(
        queryset=Site.objects.all(),
        required=False,
        label=_('Site')
    )
    group_id = DynamicModelChoiceField(
        queryset=SiteGroup.objects.all(),
        required=False,
        label=_('Site group')
    )
    region_id = DynamicModelChoiceField(
        queryset=Region.objects.all(),
        required=False,
        label=_('Region')
    )
    maintainer_id = DynamicModelChoiceField(
        queryset=PhoneMaintainer.objects.all(),
        required=False,
        label=_('Maintainer')
    )
    delivery_id = forms.CharField(
        label=_('Delivery Method'),
        required=False
    )
    provider = forms.ModelChoiceField(
        queryset=Provider.objects.all(),
        required=False,
        label=_('Provider')
    )
    status = forms.MultipleChoiceField(
        choices=add_blank_choice(PhoneDeliveryStatusChoices),
        initial=None,
        required=False,
        label=_('Status')
    )
    channel_count = forms.IntegerField(
        required=False,
        label=_('Channel count'),
        help_text=_('G.711 cidec - 96kbps reserved bandwidth per channel / NUMBER ONLY')
    )
    ndi = forms.IntegerField(
        required=False,
        label=_('MBN / NDI'),
        help_text=_("Main Billing Number / Numéro de Désignation d'Installation - E164 format / NUMBER ONLY")
    )
    dto = forms.IntegerField(
        required=False,
        label=_('DTO'),
        help_text=_('E164 format / NUMBER ONLY')
    )

    fieldsets = (
        FieldSet(
            'region_id', 'group_id', 'site_id',
            name=_('Location')
        ),
        FieldSet(
            'maintainer_id',
            name=_('Information')
        ),
        FieldSet(
            'delivery_id', 'provider', 'status',
            'channel_count', 'ndi', 'dto',
            name=_('Attributes')
        )
    )


class PhoneDeliveryBulkEditForm(NetBoxModelBulkEditForm):
    model = PhoneDelivery

    site = forms.ModelChoiceField(
        queryset=Site.objects.all(),
        required=False,
        label=_('Site')
    )
    delivery = forms.CharField(
        required=False,
        label=_('Delivery Method'),
        help_text=_('SIP TRUNK, T0, T2, ...')
    )
    provider = forms.ModelChoiceField(
        queryset=Provider.objects.all(),
        required=False,
        label=_('Provider')
    )
    status = forms.ChoiceField(
        choices=PhoneDeliveryStatusChoices,
        required=False,
        label=_('Status')
    )

    class Meta:
        fields = ('site', 'delivery', 'provider', 'status', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'add_tags' in self.fields:
            del self.fields['add_tags']
        if 'remove_tags' in self.fields:
            del self.fields['remove_tags']


class PhoneDeliveryForm(NetBoxModelForm):
    '''
    creates a form for a Phone Delivery object
    '''
    site = forms.ModelChoiceField(
        required=True,
        queryset=Site.objects.all(),
        label=_('Site')
    )
    delivery = forms.CharField(
        required=True,
        label=_('Delivery Method'),
        help_text=_('SIP TRUNK, T0, T2, ...')
    )
    provider = forms.ModelChoiceField(
        required=True,
        queryset=Provider.objects.all(),
        label=_('Provider')
    )
    channel_count = forms.IntegerField(
        required=False,
        label=_('Channel Count'),
        help_text=_('G.711 cidec - 96kbps reserved bandwidth per channel / NUMBER ONLY')
    )
    status = forms.ChoiceField(
        choices=PhoneDeliveryStatusChoices,
        required=True,
        label=_('Status'),
    )
    ndi = forms.IntegerField(
        required=False,
        label=_('MBN / NDI'),
        help_text=_("Main Billing Number / Numéro de Désignation d'Installation - E164 format / NUMBER ONLY")
    )
    dto = forms.IntegerField(
        required=False,
        label=_('DTO'),
        help_text=_('E164 format / NUMBER ONLY')
    )
    comments = CommentField()

    fieldsets = (
        FieldSet(
            'delivery', 'provider', 'status', 'channel_count', 'ndi', 'dto', 'description',
            name=_('Delivery')
        ),
        FieldSet(
            'site',
            name=_('Location')
        )
    )

    class Meta:
        model = PhoneDelivery
        fields = ('site', 'delivery', 'provider', 'channel_count', 'status', 'ndi', 'dto', 'description', 'comments')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'tags' in self.fields:
            del self.fields['tags']
