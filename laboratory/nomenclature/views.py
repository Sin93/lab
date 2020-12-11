from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, FileResponse
from nomenclature.forms import ServiceEditForm, ProfileEditForm, UploadFilesForm
from nomenclature.models import Service, Group, SubGroup, UploadFiles, Reference, Test, MadicineData

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
            new_file = UploadFiles(service=service, file=request.FILES['file'], filename=filename)
            new_file.save()
        return HttpResponseRedirect(f'/services_view/{pk}')
    else:
        service = get_object_or_404(Service, pk=pk)
        previous_service = Service.objects.filter(pk=pk-1).first()
        following_service = Service.objects.filter(pk=pk+1).first()
        med_data = MadicineData.objects.filter(service=service)[0] if MadicineData.objects.filter(service=service) else None
        files = UploadFiles.objects.filter(service=pk)
        references = []
        if service.test_set:
            for test in service.test_set.tests.all():
                ref = Reference.objects.filter(test=test)
                ref_list = []
                for itm in ref:
                    age_from = [int(i) for i in itm.age_from.split(':')] if itm.age_from else ''
                    age_to = [int(i) for i in itm.age_to.split(':')] if itm.age_to else ''
                    lower_normal_value = round(itm.lower_normal_value, test.decimal_places) if itm.lower_normal_value else ''
                    upper_normal_value = round(itm.upper_normal_value, test.decimal_places) if itm.upper_normal_value else ''
                    ref_list.append({
                        'position': itm.position,
                        'age_from': age_from,
                        'age_to': age_to,
                        'sex': itm.sex,
                        'lower_normal_value': lower_normal_value,
                        'upper_normal_value': upper_normal_value,
                        'normal_text': itm.normal_text,
                        'clinic_interpretation_key': itm.clinic_interpretation_key,
                        'clinic_interpretation_name': itm.clinic_interpretation_name,
                        'clinic_interpretation_text': itm.clinic_interpretation_text
                    })
                references.append(
                    {
                    'test_name': test.name,
                    'measure_unit': test.measure_unit,
                    'result_type': test.result_type,
                    'decimal_places': test.decimal_places,
                    'references': ref_list
                    }
                )

        if not files:
            files = False
        context = {
            'title': service.code,
            'previous_service': previous_service,
            'following_service': following_service,
            'service': service,
            'med_data': med_data,
            'files': files,
            'upload_file_form': UploadFilesForm,
            'tests': Test.objects.all(),
            'references': references,
        }

        context['test_set'] = service.test_set if service.test_set else None

        return render(request, 'nomenclature/service.html', context)


def add_test_in_test_set(request, pk):
    print(request.POST['test'])
    service = Service.objects.get(pk=pk)
    print(service.test_set.name)
    test = get_object_or_404(Test, pk=request.POST['test'])
    print(test.name)
    service.test_set.tests.add(test)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def upload_file(request, pk):
    if request.method == 'POST':
        file = request.FILES['file']
        print(request)
        print(type(file))
        service = Service.get_object_or_404(pk=pk)
        upload_file = UploadFiles(service=service, file=file)
        upload_file.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_file(request, pk):
    file = get_object_or_404(UploadFiles, pk=pk)
    file.delete()
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

        if len(subgroups) == 1 and subgroups[0].name == 'Нет':
            services = Service.objects.filter(subgroup=subgroups[0])
            if not services:
                result.pop(group.name)
                continue

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
