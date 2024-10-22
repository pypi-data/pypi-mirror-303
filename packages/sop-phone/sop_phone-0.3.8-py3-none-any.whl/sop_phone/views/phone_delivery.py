from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404

from utilities.views import GetRelatedModelsMixin, register_model_view

from netbox.views import generic
from dcim.models import Site

from ..forms.phone_delivery import *
from ..tables.phone_delivery import *
from ..tables.phone_did import *
from ..filtersets import PhoneDeliveryFilterSet
from ..models import *
from ..utils import count_all_did, format_number


__all__ =  (
    'PhoneDeliveryEditView',
    'PhoneDeliveryDetailView',
    'PhoneDeliveryDeleteView',
    'PhoneDeliveryBulkEditView',
    'PhoneDeliveryDeleteView',
    'PhoneDeliveryListView',
    'PhoneDeliverySiteView'
)


class PhoneDeliveryListView(generic.ObjectListView):
    queryset = PhoneDelivery.objects.all()
    table = PhoneDeliveryTable
    filterset = PhoneDeliveryFilterSet
    filterset_form = PhoneDeliveryFilterForm


class PhoneDeliveryBulkEditView(generic.BulkEditView):
    queryset = PhoneDelivery.objects.all()
    table = PhoneDeliveryTable
    form = PhoneDeliveryBulkEditForm
    filterset = PhoneDeliveryFilterSet


class PhoneDeliveryBulkDeleteView(generic.BulkDeleteView):
    queryset = PhoneDelivery.objects.all()
    table = PhoneDeliveryTable
    filterset = PhoneDeliveryFilterSet


class PhoneDeliveryDetailView(generic.ObjectView, PermissionRequiredMixin, GetRelatedModelsMixin):
    '''
    returns the Phone Delivery detail page with context
    '''
    queryset = PhoneDelivery.objects.all()

    def get_extra_context(self, request, instance) -> dict:
        context: dict = {}

        did = PhoneDID.objects.filter(delivery=instance)

        try:
            site_info = PhoneInfo.objects.filter(site=instance.site.id)
            context['maintainer'] = site_info.first().maintainer
        except:pass
        if instance.ndi:
            context['ndi'] = format_number(instance.ndi)
        if instance.dto:
            context['dto'] = format_number(instance.dto)
        context['did_range'] = PhoneDID
        context['num_range'] = did.count()
        context['num_did'] = count_all_did(did).__int__()
        context['related_models'] = self.get_related_models(
            request, instance,
        )
        return context


class PhoneDeliveryEditView(generic.ObjectEditView):
    '''
    creates anew Phone Delivery instance
    '''
    queryset = PhoneDelivery.objects.all()
    form = PhoneDeliveryForm


class PhoneDeliveryDeleteView(generic.ObjectDeleteView, PermissionRequiredMixin):
    '''
    deletes a Phone Delivery object
    '''
    queryset = PhoneDelivery.objects.all()


class PhoneDeliverySiteView(generic.ObjectEditView):
    '''
    adds a site automatically to the Phone Delivery
    '''
    queryset = PhoneDelivery.objects.all()
    form = PhoneDeliveryForm

    def get_object(self, **kwargs):
        return self.queryset.model(site=get_object_or_404(Site, pk=kwargs['pk']))

    def alter_object(self, obj, request, args, kwargs):
        pk = kwargs.get('pk')
        site = get_object_or_404(Site, pk=pk)
        obj = self.queryset.model
        return obj(site=site)

    def get(self, request, *args, **kwargs): 
        '''
        get request handler
        '''
        response = super().get(request, *args, **kwargs)
        return response
