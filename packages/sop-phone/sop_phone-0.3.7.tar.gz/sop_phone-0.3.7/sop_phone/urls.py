from django.urls import path

from netbox.views.generic import ObjectChangeLogView, ObjectJournalView

from .views import phone_maintainer as vm
from .views import phone_delivery as vd
from .views import phone_did as did
from .views import phone_info as pi

'''🡣 DO NOT REMOVE 🡣'''
from .views import tab_view
'''🡩 DO NOT REMOVE 🡩'''

from .models import *


app_name = 'sop_phone'


urlpatterns = [

    # phone maintainer
    path('phone-maintainer/', vm.PhoneMaintainerListView.as_view(), name='phonemaintainer_list'),
    path('phone-maintainer/<int:pk>', vm.PhoneMaintainerView.as_view(), name='phonemaintainer_detail'),
    path('phone-maintainer/add', vm.PhoneMaintainerEditView.as_view(), name='phonemaintainer_add'),
    path('phone-maintainer/edit', vm.PhoneMaintainerBulkEditView.as_view(), name='phonemaintainer_bulk_edit'),
    path('phone-maintainer/import', vm.PhoneMaintainerBulkImportView.as_view(), name='phonemaintainer_import'),
    path('phone-maintainer/delete/', vm.PhoneMaintainerBulkDeleteView.as_view(), name='phonemaintainer_bulk_delete'),
    path('phone-maintainer/<int:pk>/contacts/', vm.PhoneMaintainerContactsView.as_view(), name='phonemaintainer_contacts'),
    path('phone-maintainer/edit/<int:pk>', vm.PhoneMaintainerEditView.as_view(), name='phonemaintainer_edit'),
    path('phone-maintainer/delete/<int:pk>', vm.PhoneMaintainerDeleteView.as_view(), name='phonemaintainer_delete'),
    path('phone-maintainer/changelog/<int:pk>', ObjectChangeLogView.as_view(), name='phonemaintainer_changelog', kwargs={'model': PhoneMaintainer}),
    path('phone-maintainer/journal/<int:pk>', ObjectJournalView.as_view(), name='phonemaintainer_journal', kwargs={'model': PhoneMaintainer}),

    # phone delivery
    path('phone-delivery/', vd.PhoneDeliveryListView.as_view(), name='phonedelivery_list'),
    path('phone-delivery/<int:pk>', vd.PhoneDeliveryDetailView.as_view(), name='phonedelivery_detail'),
    path('phone-delivery/add', vd.PhoneDeliveryEditView.as_view(), name='phonedelivery_add'),
    path('phone-delivery/add_site/<int:pk>', vd.PhoneDeliverySiteView.as_view(), name='phonedelivery_site_add'),
    path('phone-delivery/edit', vd.PhoneDeliveryBulkEditView.as_view(), name='phonedelivery_bulk_edit'),
    path('phone-delivery/delete', vd.PhoneDeliveryBulkDeleteView.as_view(), name='phonedelivery_bulk_delete'),
    path('phone-delivery/edit/<int:pk>', vd.PhoneDeliveryEditView.as_view(), name='phonedelivery_edit'),
    path('phone-delivery/delete/<int:pk>', vd.PhoneDeliveryDeleteView.as_view(), name='phonedelivery_delete'),
    path('phone-delivery/changelog/<int:pk>', ObjectChangeLogView.as_view(), name='phonedelivery_changelog', kwargs={'model': PhoneDelivery}),
    path('phone-delivery/journal/<int:pk>', ObjectJournalView.as_view(), name='phonedelivery_journal', kwargs={'model': PhoneDelivery}),

    # phone did
    path('phone-did/', did.PhoneDIDListView.as_view(), name='phonedid_list'),
    path('phone-did/<int:pk>', did.PhoneDIDDetailView.as_view(), name='phonedid_detail'),
    path('phone-did/add', did.PhoneDIDEditView.as_view(), name='phonedid_add'),
    path('phone-did/add_site/<int:pk>', did.PhoneDIDAddSiteView.as_view(), name='phonedid_site_add'),
    path('phone-did/edit/', did.PhoneDIDBulkEditView.as_view(),  name='phonedid_bulk_edit'),
    path('phone-did/import/', did.PhoneDIDBulkImportView.as_view(), name='phonedid_import'),
    path('phone-did/delete/', did.PhoneDIDBulkDeleteView.as_view(), name='phonedid_bulk_delete'),
    path('phone-did/edit/<int:pk>', did.PhoneDIDEditView.as_view(), name='phonedid_edit'),
    path('phone-did/delete/<int:pk>', did.PhoneDIDDeleteView.as_view(), name='phonedid_delete'),
    path('phone-did/changelog/<int:pk>', ObjectChangeLogView.as_view(), name='phonedid_changelog', kwargs={'model': PhoneDID}),
    path('phone-did/journal/<int:pk>', ObjectJournalView.as_view(), name='phonedid_journal', kwargs={'model': PhoneDID}),
 
    # phone info
    path('phone-info/', pi.PhoneInfoListView.as_view(), name='phoneinfo_list'),
    path('phone-info/<int:pk>', pi.PhoneInfoDetailView.as_view(), name='phoneinfo_detail'),
    path('phone-info/add/', pi.PhoneInfoAddView.as_view(), name='phoneinfo_add'),
    path('phone-info/add/<int:pk>', pi.PhoneInfoAddView.as_view(), name='phoneinfo_add'),
    path('phone-info/edit/', pi.PhoneInfoBulkEditView.as_view(), name='phoneinfo_bulk_edit'),
    path('phone-info/delete/', pi.PhoneInfoBulkDeleteView.as_view(), name='phoneinfo_bulk_delete'),
    path('phone-info/edit/<int:pk>', pi.PhoneInfoEditView.as_view(), name='phoneinfo_edit'),
    path('phone-info/delete/<int:pk>', pi.PhoneInfoDeleteView.as_view(), name='phoneinfo_delete'),
    path('phone-info/changelog/<int:pk>', ObjectChangeLogView.as_view(), name='phoneinfo_changelog', kwargs={'model': PhoneInfo}),
    path('phone-info/journal/<int:pk>', ObjectJournalView.as_view(), name='phoneinfo_journal', kwargs={'model': PhoneInfo}),

]
