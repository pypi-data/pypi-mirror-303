import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable

from ..models import PhoneInfo


__all__ = (
    'PhoneInfoTable',
)


class PhoneInfoTable(NetBoxTable):
    '''
    table for all Phone Info
    '''
    site = tables.Column(
        verbose_name=_('Site'), linkify=True
    )
    maintainer = tables.Column(
        verbose_name=_('Maintainer'), linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = PhoneInfo
        fields = ('pk', 'id', 'site', 'maintainer', 'created', 'last_updated')
        default_columns = ('id', 'site', 'maintainer', 'created', 'last_updated')
