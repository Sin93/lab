from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from nomenclature.forms import ServiceEditForm
from nomenclature.models import Service, Group, SubGroup


def index(request):
    # services = {}
    #
    # groups = Group.objects.all()
    #
    # for group in groups:
    #     if group.name not in services.keys():
    #         services[group.name] = {}
    #         print(group.name)
    #
    #     subgroups = SubGroup.objects.filter(group=group)
    #     for subgroup in subgroups:
    #         if subgroup.name not in services[group.name].keys():
    #             services[group.name][subgroup.name] = Service.objects.filter(subgroup=subgroup)
    #             print(subgroup.name)

    # services = []
    # groups = Group.objects.all()
    # for group in groups:
    #     services.append(group.name)
    #     subgroups = SubGroup.objects.filter(group=group)
    #     for subgroup in subgroups:
    #         services.append(subgroup.name)
    #         serv = Service.objects.filter(subgroup=subgroup)
    #         for s in serv:
    #             services.append(s)


    services = {
        'test1': {
            'test111': 'test112',
            'test121': 'test122'
        }, 'test2': {
            'test211': 'test212',
            'test221': 'test222'
        }

    }
    context = {
        'title': 'Номенклатура',
        'services': services
    }

    return render(request, 'nomenclature/services.html', context)

def services_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)

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
    result = {'name': 'Максим'}

    return JsonResponse({'result':result})
