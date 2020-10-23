from django.db import models
from datetime import date


CLIENT_GROUPS = [('ND', 'Not defined'),]


class Group(models.Model):
    number = models.CharField(verbose_name='Номер группы', max_length=3, unique=True)
    name = models.CharField(verbose_name='Название группы', max_length=256, unique=True)

    def __str__(self):
        return f'{self.number} - {self.name}'


class SubGroup(models.Model):
    number = models.CharField(verbose_name='Номер группы', max_length=3, unique=False)
    name = models.CharField(verbose_name='Название группы', max_length=256)
    group = models.ForeignKey(Group, models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.number} - {self.name}'


class ServiceType(models.Model):
    name = models.CharField(verbose_name='Наименование типа', max_length=50)

    def __str__(self):
        return self.name


class Service(models.Model):
    class Meta:
        verbose_name = 'Услуги'

    code = models.CharField(verbose_name='Код номенклатура', max_length=50, unique=True)
    tcle_code = models.CharField(verbose_name='Код услуги в TCLE', max_length=50, null=True, blank=True)
    tcle_abbreviation = models.CharField(verbose_name='Ключ (аббревиатура) услуги в TCLE', null= True, max_length=50, blank=True)
    kdl_service_key = models.CharField(verbose_name='Кдл. Услуга. Ключ', max_length=50, blank=True, null= True)
    kdl_service_perm_code = models.CharField(verbose_name='Кдл. Услуга. Пермь. Код', max_length=50, blank=True, null= True)
    name = models.CharField(verbose_name='Наименование', max_length=1200)
    blanks = models.CharField(verbose_name='Бланки', max_length=256, blank=True, null=True)
    container = models.CharField(verbose_name='контейнеры', max_length=256, blank=True, null=True)
    biomaterials = models.CharField(verbose_name='Биоматериалы', max_length=256, blank=True, null=True)
    result_type = models.CharField(verbose_name='тип результата', max_length=100, blank=True, null=True)
    due_date = models.CharField(verbose_name='срок выполнения', max_length=50, blank=True, null=True)
    subgroup = models.ForeignKey(SubGroup, models.SET_NULL, verbose_name='Группа тестов', null=True, blank=True, unique=False)
    salesability = models.BooleanField(verbose_name='Продаваемая', default=False)
    clients_group = models.CharField(verbose_name='Группа клиентов', max_length=50, blank=True, null=True)
    type = models.ForeignKey(ServiceType, models.SET_NULL, verbose_name='Тип услуги', null=True)
    classifier_1с = models.IntegerField(verbose_name='Классификатор 1С', blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.code} - {self.name}'


class Profile(Service):
    class Meta:
        verbose_name = 'Профили'

    services = models.ManyToManyField(Service, related_name = 'услуги')

# class MadicineData(models.Model):
#     service = models.ForeignKey(Service, models.SET_NULL, null=True, )


# class Client(models.Model):
#     code_laport = models.CharField()
#     code_portal = models.CharField()
#     name = models.CharField(verbose_name='')
#
# class TestSet(models.Model):
#     key_code = models.CharField()
#     name = models.CharField()
#     date_from = models.DateTimeField()
#     date_to = models.DateTimeField()
#     department = models.CharField()
#     start_turn = models.CharField()
#     addendum_file = models.BooleanField(default=False)
#     title_in_result = models.CharField()
#     number_pp = models.IntegerField()
#
#     tests = models.ManyToManyField(Test)
#     place_of_execution = models.ManyToManyField()
#     conteiners_and_biomaterial = models.ManyToManyField()
#     autovalidation_rules = models.ManyToManyField()
#
#     # outsourcing = models.ManyToManyField()
#     # protocols = models.ManyToManyField()
#
# class Test(models.Model):
#     keycode = models.CharField()
#     name = models.CharField()
#     kdl_test_code = models.CharField()
#     kdl_test_key = models.CharField()
#     result_type = models.CharField()
#     measure_unit = models.CharField(blank=True)
#     decimal_places = models.SmallIntegerField(blank=True)
#
#     coded_result = models.ManyToManyField()
#     reference = models.ManyToManyField()
#
# class PlaceOfExecution(models.Model):
#     city = models.CharField()
#     type = models.CharField()
