from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import NetBoxModelBulkEditForm, NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import DynamicModelChoiceField
from utilities.forms.rendering import FieldSet
from dcim.models import Site, Region, SiteGroup

from ..models import PhoneInfo, PhoneMaintainer


__all__ = (
    'PhoneInfoForm',
    'PhoneInfoFilterForm',
    'PhoneInfoBulkEditForm',
)


class PhoneInfoFilterForm(NetBoxModelFilterSetForm):
    model = PhoneInfo
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
    maintainer_id = forms.ModelChoiceField(
        queryset=PhoneMaintainer.objects.all(),
        required=False,
        label=_('Maintainer')
    )
    
    fieldsets = (
        FieldSet(
            'region_id', 'group_id', 'site_id',
            name=_('Location')
        ),
        FieldSet(
            'maintainer_id',
            name=_('Attributes')
        )
    )


class PhoneInfoForm(NetBoxModelForm):

    site = forms.ModelChoiceField(
        queryset=Site.objects.all(),
        required=False,
        label=_('Site')
    )
    maintainer = forms.ModelChoiceField(
        queryset=PhoneMaintainer.objects.all(),
        required=False,
        label=_('Maintainer')
    )

    class Meta:
        model = PhoneInfo
        fields = ('site', 'maintainer', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if 'tags' in self.fields:
            del self.fields['tags']


class PhoneInfoBulkEditForm(NetBoxModelBulkEditForm):
    model = PhoneInfo
    maintainer = forms.ModelChoiceField(
        queryset=PhoneMaintainer.objects.all(),
        required=False,
        label=_('Maintainer')
    )

    class Meta:
        fields = ('maintainer', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'add_tags' in self.fields:
            del self.fields['add_tags']
        if 'remove_tags' in self.fields:
            del self.fields['remove_tags']
