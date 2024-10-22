from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.shortcuts import get_object_or_404

from netbox.views import generic
from dcim.models import Site

from ..forms.phone_did import *
from ..tables.phone_did import *
from ..filtersets import PhoneDIDFilterSet
from ..models import *
from ..utils import count_all_did, format_number


__all__ = (
    'PhoneDIDEditView',
    'PhoneDIDDeleteView',
    'PhoneDIDDetailView',
    'PhoneDIDBulkEditView',
    'PhoneDIDBulkDeleteView',
    'PhoneDIDListView',
    'PhoneDIDBulkImportView',
    'PhoneDIDAddSiteView'
)


class PhoneDIDListView(generic.ObjectListView):
    '''
    all DIDs list
    '''
    queryset = PhoneDID.objects.all()
    table = PhoneDIDTable
    filterset_form = PhoneDIDFilterForm
    filterset = PhoneDIDFilterSet


class PhoneDIDBulkEditView(generic.BulkEditView):
    '''
    for the "edit selected" view
    '''
    queryset = PhoneDID.objects.all()
    table = PhoneDIDTable
    form = PhoneDIDBulkEditForm
    filterset = PhoneDIDFilterSet


class PhoneDIDBulkDeleteView(generic.BulkDeleteView):
    '''
    for the "delete selected" view
    '''
    queryset = PhoneDID.objects.all()
    table = PhoneDIDTable
    filterset = PhoneDIDFilterSet


class PhoneDIDEditView(generic.ObjectEditView):
    '''
    edits a DID instance
    '''
    queryset = PhoneDID.objects.all()
    form = PhoneDIDForm
    

class PhoneDIDDeleteView(generic.ObjectDeleteView):
    '''
    deletes a DID instance
    '''
    queryset = PhoneDID.objects.all()


class PhoneDIDDetailView(generic.ObjectView, PermissionRequiredMixin):
    '''
    returns the DID detail page with context
    '''
    queryset = PhoneDID.objects.all()

    def get_extra_context(self, request, instance):
        context: dict = {}

        context['start'] = format_number(instance.start)
        context['end'] = format_number(instance.end)
        context['num_did'] = count_all_did(instance).__int__()
        try:
            context['maintainer'] = PhoneInfo.objects.filter(site=instance.delivery.site).first()
        except:
            pass
        return context


class PhoneDIDBulkImportView(generic.BulkImportView):
    queryset = PhoneDID.objects.all()
    model_form = PhoneDIDBulkImportForm

    def save_object(self, object_form, request):
        instance = object_form.save()
        
        if not instance.end or instance.end == 0:
            instance.end = instance.start
            instance.save()

        return instance

    def post(self, request):
        '''
        post request handler
        if additionnal changes is needed
        '''
        response = super().post(request)
        return response


class PhoneDIDAddSiteView(generic.ObjectEditView):
    '''
    adds a site automatically to the DID
    '''
    queryset = PhoneDID.objects.all()
    form = PhoneDIDForm

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
