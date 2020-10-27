from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from nomenclature.forms import ServiceEditForm, ProfileEditForm
from nomenclature.models import Service, Group, SubGroup

import json

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
                        f'/edit/{service.pk}'
                    ]
                    result[group.name][subgroup.name].append(serv_data)

    return JsonResponse(result)


def json_data(request, field_type):
    print(field_type)
    data = {}
    servises = Service.objects.all()
    for service in servises:
        data[service.code] = getattr(service, field_type)

    return JsonResponse({'data': 'Какой-то data'})
