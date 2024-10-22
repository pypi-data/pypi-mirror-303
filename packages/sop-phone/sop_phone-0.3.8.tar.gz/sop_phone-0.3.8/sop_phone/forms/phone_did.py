from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from netbox.forms import NetBoxModelFilterSetForm, NetBoxModelBulkEditForm, NetBoxModelForm, NetBoxModelImportForm
from utilities.forms.fields import DynamicModelChoiceField, DynamicModelChoiceField, CSVModelChoiceField
from utilities.forms.rendering import FieldSet
from dcim.models import Site, Region, SiteGroup

from ..models import *


__all__ = (
    'PhoneDIDForm',
    'PhoneDIDFilterForm',
    'PhoneDIDBulkEditForm',
    'PhoneDIDBulkImportForm',
)


class PhoneDIDBulkEditForm(NetBoxModelBulkEditForm):
    model = PhoneDID

    site = DynamicModelChoiceField(
        queryset=Site.objects.all()
    )
    # this field depends on the site field
    # -> you can only enter deliveries that 
    # -> share the same site as the field site   
    delivery = DynamicModelChoiceField(
        queryset=PhoneDelivery.objects.all(),
        help_text=_('Specify how this range is delivered.'),
        query_params={
            'site_id': '$site'
        }
    )

    class Meta:
        fields = ('site', 'delivery', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'add_tags' in self.fields:
            del self.fields['add_tags']
        if 'remove_tags' in self.fields:
            del self.fields['remove_tags']


class PhoneDIDFilterForm(NetBoxModelFilterSetForm):
    model = PhoneDID
    
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
    maintainer_id = forms.ModelChoiceField(
        queryset=PhoneMaintainer.objects.all(),
        required=False,
        label=_('Maintainer')
    )
    delivery_id = forms.ModelChoiceField(
        queryset=PhoneDelivery.objects.all(),
        required=False,
        label=_('Delivery')
    )
    partial_number = forms.IntegerField(
        label=_('Partial number'),
        required=False,
        help_text=_('E164 format')
    )
    start = forms.IntegerField(
        label=_('Start number'),
        required=False,
        help_text=_('E164 format'),
    )
    end = forms.IntegerField(
        label=_('End number'),
        required=False,
        help_text=_('E164 format')
    )

    fieldsets = (
        FieldSet(
            'region_id', 'group_id', 'site_id',
            name=_('Location')
        ),
        FieldSet(
            'maintainer_id', 'delivery_id',
            name=_('Information')
        ),
        FieldSet(
            'partial_number', 'start', 'end',
            name=_('Attributes')
        )
    )

    def clean(self):
        super().clean()


class PhoneDIDForm(NetBoxModelForm):

    site = DynamicModelChoiceField(
        label=_('Site'),
        queryset=Site.objects.all(),
        required=True,
    )
    start = forms.IntegerField(
        label=_('Start number'),
        required=True,
        help_text=_('E164 format / NUMBER ONLY'),
    )
    end = forms.IntegerField(
        label=_('End number'),
        required=False,
        help_text=_('E164 format - can be left blank if the range is only one number. / NUMBER ONLY'),
    )
    # this field depends on the site field
    # -> you can only enter deliveries that 
    # -> share the same site as the field site
    delivery = DynamicModelChoiceField(
        label=_('Delivery'),
        queryset=PhoneDelivery.objects.all(),
        required=False,
        help_text=_('Specify how this range is delivered.'),
        query_params={
            'site_id': '$site'
        }
    )
    fieldsets = (
        FieldSet(
            'site',
            name=_('Location')
        ),
        FieldSet(
            'start', 'end', 'delivery',
            name=_('DIDs')
        )
    )

    class Meta:
        model = PhoneDID
        fields = ('site', 'start', 'end', 'delivery')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'tags' in self.fields:
            del self.fields['tags']

    def clean(self):

        super().clean()


class PhoneDIDBulkImportForm(NetBoxModelImportForm):
    delivery = CSVModelChoiceField(
        queryset=PhoneDelivery.objects.all(),
        to_field_name='id',
        required=False,
    )
    site = CSVModelChoiceField(
        queryset=Site.objects.all(),
        to_field_name='slug',
        required=True,
    )
    start = forms.IntegerField(
        label=_('Start number'),
        help_text='E164 format',
        required=True
    )
    end = forms.IntegerField(
        label=_('End number'),
        help_text='E164 format - can be left blank if the range is only one number.',
        required=False
    )

    class Meta:
        model = PhoneDID
        fields = ['delivery', 'site', 'start', 'end']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'tags' in self.fields:
            del self.fields['tags']

    def clean(self):
        super().clean()
        if not self.cleaned_data.get('end'):
            self.cleaned_data['end'] = self.cleaned_data['start']
