import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable
from ..models import PhoneDID
from ..utils import format_number


__all__ = (
    'PhoneDIDTable',
)


class PhoneDIDTable(NetBoxTable):
    '''
    table for all DID List
    '''
    delivery = tables.Column(
        verbose_name=_('Delivery'), linkify=True
    )
    site = tables.Column(
        verbose_name=_('Site'), linkify=True
    )
    start = tables.Column(
        verbose_name=_('Start number'), linkify=True,
    )
    end = tables.Column(
        verbose_name=_('End number'), linkify=True,
    )

    class Meta(NetBoxTable.Meta):
        model = PhoneDID
        fields = ('actions', 'pk', 'id', 'start', 'end', 'delivery', 'site', 'created', 'last_updated')
        default_columns = ('start', 'end', 'delivery')

    def render_start(self, record):
        return format_number(record.start)

    def render_end(self, record):
        return format_number(record.end)
