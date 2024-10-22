from dcim.models import Site
from netbox.views import generic
from tenancy.views import ObjectContactsView
from utilities.views import GetRelatedModelsMixin, register_model_view

from ..models import PhoneMaintainer, PhoneInfo, PhoneDID, PhoneDelivery
from ..filtersets import PhoneMaintainerFilterSet
from ..tables.phone_maintainer import *
from ..forms.phone_maintainer import *
from ..utils import count_all_did


__all__ = (
    'PhoneMaintainerView',
    'PhoneMaintainerEditView',
    'PhoneMaintainerDeleteView',
    'PhoneMaintainerBulkEditView',
    'PhoneMaintainerBulkDeleteView',
    'PhoneMaintainerBulkImportView',
    'PhoneMaintainerContactsView'
)


class PhoneMaintainerListView(generic.ObjectListView):
    queryset = PhoneMaintainer.objects.all()
    table = PhoneMaintainerTable
    filterset = PhoneMaintainerFilterSet
    filterset_form = PhoneMaintainerFilterForm


class PhoneMaintainerView(generic.ObjectView, GetRelatedModelsMixin):
    queryset = PhoneMaintainer.objects.all()

    def count_did(self, sites) -> tuple[int, int]:
        '''
        num_did = count of all numbers
        '''
        num_did: int = 0

        for instance in sites:
            temp = count_all_did(
                PhoneDID.objects.filter(delivery__site=instance.site),
                PhoneDelivery.objects.filter(site=instance.site)
            )
            num_did += temp.__int__()

        return num_did
    
    def get_format(self, values) -> str | None:
        qs = [str(item['site__id']) for item in values]
        if qs == []:
            return None
        return f'id=' + '&id='.join(qs)

    def get_extra_context(self, request, instance):
        '''
        additionnal context for the related models/objects
        as they are not directly related
        '''
        context: dict = {}

        sites = PhoneInfo.objects.filter(maintainer=instance)
        site_ids = (PhoneInfo.objects.filter(maintainer=instance).values('site__id'))

        context['num_did'] = self.count_did(sites)
        context['site_ids'] = site_ids
        context['related_models'] = self.get_related_models(
            request, 
            instance, 
            extra=(
                (Site.objects.filter(
                    pk__in=(PhoneInfo.objects.filter(maintainer=instance).values('site__id'))
                ), 'id'),
                (PhoneDID.objects.filter(
                    delivery__site__in=PhoneInfo.objects.filter(maintainer=instance).values('site_id')
                ), 'maintainer_id')
            )
        )
        context['site'] = Site
        context['restricted'] = self.get_format(site_ids)
        return context


class PhoneMaintainerEditView(generic.ObjectEditView):
    '''
    edits a maintainer instance
    '''
    queryset = PhoneMaintainer.objects.all()
    form = PhoneMaintainerForm


class PhoneMaintainerDeleteView(generic.ObjectDeleteView):
    '''
    deletes a maintainer instance
    '''
    queryset = PhoneMaintainer.objects.all()


class PhoneMaintainerBulkDeleteView(generic.BulkDeleteView):
    '''
    deletes multiple phone maintainers instances
    '''
    queryset = PhoneMaintainer.objects.all()
    table = PhoneMaintainerTable
    filterset = PhoneMaintainerFilterSet


class PhoneMaintainerBulkEditView(generic.BulkEditView):
    '''
    edits multiple phone maintainer instances
    '''
    queryset = PhoneMaintainer.objects.all()
    table = PhoneMaintainerTable
    form = PhoneMaintainerBulkEditForm
    filterset = PhoneMaintainerFilterSet


class PhoneMaintainerBulkImportView(generic.BulkImportView):
    queryset = PhoneMaintainer.objects.all()
    model_form = PhoneMaintainerBulkImportForm

    def save_object(self, object_form, request):
        instance = object_form.save()
        return instance

    def post(self, request):
        '''
        post request handler
        if additionnal changes is needed
        '''
        response = super().post(request)
        return response


@register_model_view(PhoneMaintainer, 'contacts')
class PhoneMaintainerContactsView(ObjectContactsView):
    queryset = PhoneMaintainer.objects.all()
