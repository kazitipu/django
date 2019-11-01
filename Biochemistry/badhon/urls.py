from django.urls import path
from .views import DonorListView,donor_detail_view,donor_create_view,donor_update_view,donor_delete_view


urlpatterns= [
    path('', DonorListView.as_view(), name='donor_list'),
    path('<str:slug>', donor_detail_view),
    path('<str:slug>/edit/', donor_update_view),
    path('<str:slug>/delete/', donor_delete_view),
]