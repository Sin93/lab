from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, FileResponse
from nomenclature.forms import ServiceEditForm, ProfileEditForm, UploadFilesForm
from nomenclature.models import Service, Group, SubGroup, UploadFiles

import json, os

DICT_OF_IMPORTED_CLASSES = globals()

def index(request):
    services = {}

    groups = Group.objects.all()

    for group in groups:
        if group.name not in services.keys():
            services[group.name] = {'name': group.name}

        subgroups = SubGroup.objects.filter(group=group)
        for subgroup in subgroups:
            if subgroup.name not in services[group.name].keys():
                services[group.name][subgroup.name] = {
                    'name': subgroup.name,
                    'services_list': Service.objects.filter(subgroup=subgroup)
                }

    context = {
        'title': 'Номенклатура',
        'services': services
    }

    return render(request, 'nomenclature/services.html', context)


def services_view(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = UploadFilesForm(request.POST, request.FILES)
        if form.is_valid():
            service = get_object_or_404(Service, pk=pk)
            filename = request.FILES['file'].name
            print()
            new_file = UploadFiles(service=service, file=request.FILES['file'], filename=filename)
            new_file.save()
        return HttpResponseRedirect(f'/services_view/{pk}')
    else:
        service = get_object_or_404(Service, pk=pk)
        files = UploadFiles.objects.filter(service=pk)
        if not files:
            files = False
        context = {
            'title': service.code,
            'service': service,
            'files': files,
            'upload_file_form': UploadFilesForm
        }

        return render(request, 'nomenclature/service.html', context)


def upload_file(request, pk):
    if request.method == 'POST':
        file = request.FILES['file']
        print(request)
        print(type(file))
        service = Service.get_object_or_404(pk=pk)
        upload_file = UploadFiles(service=service, file=file)
        upload_file.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def download_file(request, pk):
    response_file = UploadFiles.objects.get(pk=pk)
    print(dir(response_file.file))
    bynary_file = response_file.file.open()
    return FileResponse(bynary_file, as_attachment=True)


def services_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)

    if service.type.name == 'Коммерческий профиль':
        if request.method == 'POST':
            update_form = ProfileEditForm(request.POST, instance=service)
            if update_form.is_valid():
                update_form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            update_form = ProfileEditForm(instance=service)
    else:
        if request.method == 'POST':
            update_form = ServiceEditForm(request.POST, instance=service)
            if update_form.is_valid():
                update_form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            update_form = ServiceEditForm(instance=service)

    context = {
        'title': service.code,
        'update_form': update_form
    }

    return render(request, 'nomenclature/services_update.html', context)


def json_nomenclature(request):
    result = {}

    groups = Group.objects.all()

    for group in groups:
        if group.name not in result.keys():
            result[group.name] = {}

        subgroups = SubGroup.objects.filter(group=group)
        for subgroup in subgroups:
            if subgroup.name not in result[group.name].keys():
                result[group.name][subgroup.name] = []
                services = Service.objects.filter(subgroup=subgroup)
                for service in services:
                    serv_data = [
                        service.code,
                        service.name,
                        service.blanks,
                        service.biomaterials,
                        service.container,
                        service.due_date,
                        service.result_type,
                        service.pk
                    ]
                    result[group.name][subgroup.name].append(serv_data)

    return JsonResponse(result)


def json_data(request, model, field_type):
    print(model, field_type)
    model = DICT_OF_IMPORTED_CLASSES[model]
    data = {}
    services = model.objects.all()
    for service in services:
        attr = getattr(service, field_type)
        data[service.pk] = attr.name
    return JsonResponse(data)
