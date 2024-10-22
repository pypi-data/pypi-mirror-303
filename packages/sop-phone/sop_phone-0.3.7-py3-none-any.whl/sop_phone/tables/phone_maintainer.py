import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable, ChoiceFieldColumn, columns
from tenancy.tables import ContactsColumnMixin

from ..models import PhoneMaintainer


__all__ = (
    'PhoneMaintainerTable',
)

class PhoneMaintainerTable(NetBoxTable, ContactsColumnMixin):
    '''
    table for all Phone Deliveries
    '''
    name = tables.Column(
        verbose_name=_('Name'),
        linkify=True
    )
    status = ChoiceFieldColumn(
        linkify=True
    )
    description = tables.Column()
    comments = columns.MarkdownColumn()

    class Meta(NetBoxTable.Meta):
        model = PhoneMaintainer
        fields = ('pk', 'id', 'actions', 'name', 'status', 'time_zone', 'contacts', 
                    'physical_address', 'shipping_address', 'latitude', 'longitude', 'created', 'last_updated', 'description', 'comments', )
        default_columns = ('pk', 'name', 'status', 'description',)
