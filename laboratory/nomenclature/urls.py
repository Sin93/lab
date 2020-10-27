from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:pk>', views.services_edit, name='edit'),
    path('get_nomenclature_data', views.json_nomenclature, name='get_nomenclature_data'),
    path('get_data/<str:field_type>', views.json_data, name='get_data'),
]
