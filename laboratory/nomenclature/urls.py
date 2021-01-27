from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:pk>', views.services_edit, name='edit'),
    path('services_view/<int:pk>', views.services_view, name='view'),
    path('get_nomenclature_data', views.json_nomenclature, name='get_nomenclature_data'),
    path('get_data/<str:model>/<str:field_type>', views.json_data, name='get_data'),
    path('upload_file/<int:pk>', views.upload_file, name='upload_file'),
    path('download_file/<int:pk>', views.download_file, name='download_file'),
    path('delete_file/<int:pk>', views.delete_file, name='delete_file'),
    path('add_test/<int:pk>', views.add_test_in_test_set, name='add_test'),
    path('add_bc_group/<int:pk>', views.add_biomaterial_container_group, name='add_bc_group'),
    path('add_bm_cont/<int:pk>', views.add_biomaterial_container_in_group, name='add_bm_cont'),
    path('delete_bc_group/<int:pk>', views.delete_biomaterial_container_group, name='delete_bc_group'),
]
