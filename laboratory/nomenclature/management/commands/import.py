from openpyxl import load_workbook, Workbook
from django.core.management import BaseCommand
from django.db.utils import IntegrityError
from nomenclature.models import Group, SubGroup, Service, Profile, ServiceType


SERVICE_TYPES = [
    'Not defined',
    'ПРОФ',
    'Лабораторное исследование',
    'Коммерческий профиль',
    'Услуга'
]

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        ServiceType.objects.all().delete()

        for type in SERVICE_TYPES:
            new_type = ServiceType(name=type)
            new_type.save()

        Group.objects.all().delete()
        SubGroup.objects.all().delete()

        wb = load_workbook('nomenclature/data/Список групп и подгрупп.xlsx', read_only=True)
        first_sheet = wb.worksheets[0]
        groups = {}

        for row in first_sheet.rows:
            if str(row[0].value) not in groups.keys():
                groups[str(row[0].value)] = {'name':str(row[1].value), 'subgroups':[]}
                groups[str(row[0].value)]['subgroups'].append({'number':str(row[2].value), 'name':str(row[3].value)})
                continue

            groups[str(row[0].value)]['subgroups'].append({'number':str(row[2].value), 'name':str(row[3].value)})

        for group in groups.keys():
            new_group = Group(number=group, name=groups[group]['name'])
            new_group.save()
            for sg in groups[group]['subgroups']:
                new_sg = SubGroup(number=sg['number'], name=sg['name'], group=new_group)
                new_sg.save()

        new_group = Group(number='99', name='не определена!')
        new_group.save()
        new_sg = SubGroup(number='99', name='не определена!', group=new_group)
        new_sg.save()

        Service.objects.all().delete()
        wb = load_workbook('nomenclature/data/nomenclature.xlsx', read_only=True)
        first_sheet = wb.worksheets[0]

        for row in first_sheet:
            if row[0].value is not None:
                try:
                    gr = Group.objects.get(number=str(row[0].value))
                except:
                    print(f'группа {row[0].value} не найдена, для теста {row[7].value}')
            else:
                try:
                    gr = Group.objects.get(number='99')
                except:
                    print(f'группа 99 не найдена, для теста {row[7].value}')

            if row[1].value is not None:
                try:
                    sg = SubGroup.objects.get(number=str(row[1].value), group=gr)
                except:
                    print(f'подгруппа {row[1].value} не найдена, для теста {row[7].value}')
            else:
                try:
                    sg = SubGroup.objects.get(number='99')
                except:
                    print(f'подгруппа 99 не найдена, для теста {row[7].value}')

            if row[3].value is not None:
                type = ServiceType.objects.get(name=row[3].value)
            else:
                type = ServiceType.objects.get(name='Not defined')

            if type.name == 'Коммерческий профиль':
                new_record = Profile()
            else:
                new_record = Service()

            try:
                new_record.subgroup=sg
                new_record.salesability=True
                new_record.clients_group=row[2].value
                new_record.type=type
                new_record.classifier_1с=row[4].value
                new_record.tcle_code=row[5].value
                new_record.tcle_abbreviation=row[6].value
                new_record.code=row[7].value
                new_record.name=row[8].value
                new_record.blanks=row[9].value
                new_record.biomaterials=row[10].value
                new_record.container=row[11].value
                new_record.result_type=row[12].value
                new_recServiceType.objects.all().delete()

        for type in SERVICE_TYPES:
            new_type = ServiceType(name=type)
            new_type.save()

        Group.objects.all().delete()
        SubGroup.objects.all().delete()

        wb = load_workbook('nomenclature/data/Список групп и подгрупп.xlsx', read_only=True)
        first_sheet = wb.worksheets[0]
        groups = {}

        for row in first_sheet.rows:
            if str(row[0].value) not in groups.keys():
                groups[str(row[0].value)] = {'name':str(row[1].value), 'subgroups':[]}
                groups[str(row[0].value)]['subgroups'].append({'number':str(row[2].value), 'name':str(row[3].value)})
                continue

            groups[str(row[0].value)]['subgroups'].append({'number':str(row[2].value), 'name':str(row[3].value)})

        for group in groups.keys():
            new_group = Group(number=group, name=groups[group]['name'])
            new_group.save()
            for sg in groups[group]['subgroups']:
                new_sg = SubGroup(number=sg['number'], name=sg['name'], group=new_group)
                new_sg.save()

        new_group = Group(number='99', name='не определена!')
        new_group.save()
        new_sg = SubGroup(number='99', name='не определена!', group=new_group)
        new_sg.save()

        Service.objects.all().delete()
        wb = load_workbook('nomenclature/data/nomenclature.xlsx', read_only=True)
        first_sheet = wb.worksheets[0]

        for row in first_sheet:
            if row[0].value is not None:
                try:
                    gr = Group.objects.get(number=str(row[0].value))
                except:
                    print(f'группа {row[0].value} не найдена, для теста {row[7].value}')
            else:
                try:
                    gr = Group.objects.get(number='99')
                except:
                    print(f'группа 99 не найдена, для теста {row[7].value}')

            if row[1].value is not None:
                try:
                    sg = SubGroup.objects.get(number=str(row[1].value), group=gr)
                except:
                    print(f'подгруппа {row[1].value} не найдена, для теста {row[7].value}')
            else:
                try:
                    sg = SubGroup.objects.get(number='99')
                except:
                    print(f'подгруппа 99 не найдена, для теста {row[7].value}')

            if row[3].value is not None:
                type = ServiceType.objects.get(name=row[3].value)
            else:
                type = ServiceType.objects.get(name='Not defined')

            if type.name == 'Коммерческий профиль':
                new_record = Profile()
            else:
                new_record = Service()

            try:
                new_record.subgroup=sg
                new_record.salesability=True
                new_record.clients_group=row[2].value
                new_record.type=type
                new_record.classifier_1с=row[4].value
                new_record.tcle_code=row[5].value
                new_record.tcle_abbreviation=row[6].value
                new_record.code=row[7].value
                new_record.name=row[8].value
                new_record.blanks=row[9].value
                new_record.biomaterials=row[10].value
                new_record.container=row[11].value
                new_record.result_type=row[12].value
                new_record.due_date=row[13].value

                new_record.save()
            except IntegrityError:
                print(f'код {row[7].value} - не уникальный, второй раз не добавлен')


        profiles = Profile.objects.all()
        for profile in profiles:
            profile.services.clear()

        wb = load_workbook('nomenclature/data/profile.xlsx', read_only=True)
        first_sheet = wb.worksheets[0]

        for row in first_sheet.rows:
            try:
                profile = Profile.objects.get(code=row[0].value)
            except:
                print(f'Профиля {row[0].value} нет в номенклатуре')

            try:
                service = Service.objects.get(code=row[1].value)
            except:
                print(f'Услуги {row[1].value} нет в номенклатуре')
                continue

            profile.services.add(serviceord.due_date=row[13].value

                new_record.save()
            except IntegrityError:
                print(f'код {row[7].value} - не уникальный, второй раз не добавлен')


        profiles = Profile.objects.all()
        for profile in profiles:
            profile.services.clear()

        wb = load_workbook('nomenclature/data/profile.xlsx', read_only=True)
        first_sheet = wb.worksheets[0]

        for row in first_sheet.rows:
            try:
                profile = Profile.objects.get(code=row[0].value)
            except:
                print(f'Профиля {row[0].value} нет в номенклатуре')

            try:
                service = Service.objects.get(code=row[1].value)
            except:
                print(f'Услуги {row[1].value} нет в номенклатуре')
                continue

            profile.services.add(service)
