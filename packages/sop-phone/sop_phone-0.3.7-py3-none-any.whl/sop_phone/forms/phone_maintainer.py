from django import forms
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

from timezone_field import TimeZoneFormField

from utilities.forms import add_blank_choice
from tenancy.forms import ContactModelFilterForm
from utilities.forms.fields import (
    CommentField, SlugField, CSVChoiceField, DynamicModelChoiceField
)
from utilities.forms.rendering import FieldSet
from netbox.forms import (
    NetBoxModelFilterSetForm, NetBoxModelForm, NetBoxModelBulkEditForm,
    NetBoxModelImportForm
)
from dcim.models import Site, Region, SiteGroup

from ..models import *


__all__ = (
    'PhoneMaintainerForm',
    'PhoneMaintainerFilterForm',
    'PhoneMaintainerBulkEditForm',
    'PhoneMaintainerBulkImportForm',
)


class PhoneMaintainerFilterForm(NetBoxModelFilterSetForm, ContactModelFilterForm):
    model = PhoneMaintainer

    site_id = DynamicModelChoiceField(
        queryset=Site.objects.all(),
        required=False,
        label=_('Site')
    )
    region_id = DynamicModelChoiceField(
        queryset=Region.objects.all(),
        required=False,
        label=_('Region')
    )
    group_id = DynamicModelChoiceField(
        queryset=SiteGroup.objects.all(),
        required=False,
        label=_('Site group')
    )
    status = forms.ChoiceField(
        choices=add_blank_choice(PhoneMaintainerStatusChoice),
        initial=None,
        required=False,
        label=_('Status'),
    )

    fieldsets = (
        FieldSet(
            'region_id', 'group_id', 'site_id',
            name=_('Location')
        ),
        FieldSet(
            'contact', 'contact_role', 'contact_group',
            name=_('Contacts')
        ),
        FieldSet(
            'name', 'slug', 'status',
            name=_('Attributes')
        )
    )
    



class PhoneMaintainerBulkEditForm(NetBoxModelBulkEditForm):
    model = PhoneMaintainer

    status = forms.ChoiceField(
        choices=PhoneMaintainerStatusChoice,
        required=True,
    )

    class Meta:
        fields = ('status', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'add_tags' in self.fields:
            del self.fields['add_tags']
        if 'remove_tags' in self.fields:
            del self.fields['remove_tags']


class PhoneMaintainerForm(NetBoxModelForm):
    name = forms.CharField(label=_('Name'))
    slug = SlugField()
    status = forms.ChoiceField(
        choices=PhoneMaintainerStatusChoice,
        required=True
    )
    time_zone = TimeZoneFormField(
        label=_('Time zone'),
        choices=add_blank_choice(TimeZoneFormField().choices),
        required=False
    )
    comments = CommentField()

    fieldsets = (
        FieldSet(
            'name', 'slug', 'status', 'time_zone', 'description',
            name=_('Maintainer')
        ),
        FieldSet(
            'physical_address', 'shipping_address', 'latitude', 'longitude',
            name=_('Contact Info')
        )
    )

    class Meta:
        model = PhoneMaintainer
        fields = (
            'name', 'slug', 'status', 'time_zone', 'description',
            'physical_address', 'shipping_address', 'latitude', 'longitude',
            'comments'
        )
        widgets = {
            'physical_address': forms.Textarea(
                attrs={
                    'rows': 3,
                }
            ),
            'shipping_address': forms.Textarea(
                attrs={
                    'rows': 3,
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'tags' in self.fields:
            del self.fields['tags']


class PhoneMaintainerBulkImportForm(NetBoxModelImportForm):
    status = CSVChoiceField(
        choices=PhoneMaintainerStatusChoice,
        required=True,
    )
    slug = SlugField(required=True)

    class Meta:
        model = PhoneMaintainer
        fields = [
            'name', 'slug', 'status', 'time_zone', 'description',
            'physical_address', 'shipping_address', 'latitude', 'longitude',
            'comments'
        ]
        help_texts = {
            'time_zone': mark_safe(
                '{} (<a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">{}</a>)'.format(
                    _('Time zone'), _('available options')
                )
            )
        }

    def clean(self):
        super().clean()
