from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:pk>', views.services_edit, name='edit'),
    path('services_view/<int:pk>', views.services_view, name='view'),
    path('get_nomenclature_data', views.json_nomenclature, name='get_nomenclature_data'),
    path('get_data/<str:model>/<str:field_type>', views.json_data, name='get_data'),
    path('upload_file/<int:pk>', views.upload_file, name='upload_file')
]
