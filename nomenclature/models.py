from django.db import models
from datetime import date


CLIENT_GROUPS = [('ND', 'Not defined'),]

SEX = [
    ('M', 'Муж.'),
    ('F', 'Жен.'),
    ('A', 'Любой')
]

TEST_RESULT_TYPE = [
    ('N', 'Numeric'),
    ('FT', 'Free Text'),
    ('TICR', 'Test Item Coded Result'),
    ('DTA', 'Display Text Area')
]

TYPE_PLACE_OF_EXECUTION = [
    ('Аутсорсинг', (
            ('MO', 'Москва'),
            ('PL', 'Местный')
        )
    ),
    ('Лаборатория', (
            ('INS', 'Прибор'),
            ('MAN', 'Ручная методика')
        )
    )
]


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


class Region(models.Model):
    name = models.CharField(verbose_name='Филиал', max_length=20, unique=True)


class PlaceOfExecution(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=100)
    region = models.ForeignKey(Region, models.CASCADE, verbose_name='Филиал')
    type = models.CharField(verbose_name='Тип места выполнения', max_length=20, choices=TYPE_PLACE_OF_EXECUTION)


class Test(models.Model):
    keycode = models.CharField(verbose_name='Ключ теста', max_length=50)
    name = models.CharField(verbose_name='Наименование теста', max_length=250)
    short_name = models.CharField(verbose_name='Наименование теста', max_length=50, blank=True, null=True)
    kdl_test_code = models.CharField(verbose_name='Внешний код (КДЛ.Тест.Код)', max_length=50, blank=True, null=True)
    kdl_test_key = models.CharField(verbose_name='Внешний код (КДЛ.Тест.Ключ)', max_length=50, blank=True, null=True)
    result_type = models.CharField(verbose_name='Тип результата', max_length=30, choices=TEST_RESULT_TYPE)
    measure_unit = models.CharField(verbose_name='Единицы измерения', max_length=50, blank=True, null=True)
    decimal_places = models.SmallIntegerField(verbose_name='Количество знаков после запятой', blank=True)


class Reference(models.Model):
    test = models.ForeignKey(Test, models.CASCADE, verbose_name='Тест', null=True, blank=True, unique=False)
    active = models.BooleanField(verbose_name='активность', default=True)
    position = models.SmallIntegerField(verbose_name='Позиция', null=True)
    age_from = models.CharField(verbose_name='Возраст с', max_length=10, blank=True, null=True)
    age_to = models.CharField(verbose_name='Возраст по', max_length=10, blank=True, null=True)
    sex = models.CharField(verbose_name='Пол', max_length=10, choices=SEX, default='Любой', null=True)
    lower_normal_value = models.DecimalField(verbose_name='Норма нижняя', max_digits=16, decimal_places=8, blank=True, null=True)
    upper_normal_value = models.DecimalField(verbose_name='Норма верхняя', max_digits=16, decimal_places=8, blank=True, null=True)
    normal_text = models.CharField(verbose_name='Норма текстом', max_length=50, blank=True, null=True)
    clinic_interpretation_key = models.CharField(verbose_name='Ключ клинической интерпретации', max_length=50, blank=True, null=True)
    clinic_interpretation_name = models.CharField(verbose_name='Наименование клинической интерпретации', max_length=50, blank=True, null=True)
    clinic_interpretation_text = models.CharField(verbose_name='Текс клинической интерпретации', max_length=1000, blank=True, null=True)


class Container(models.Model):
    code = models.CharField(verbose_name='Код контейнера', max_length=50, unique=True)
    name = models.CharField(verbose_name='Наименование контейнера', max_length=100, unique=True)


class Biomaterial(models.Model):
    code = models.CharField(verbose_name='Код биоматериала', max_length=20, unique=True)
    name = models.CharField(verbose_name='Название биоматериала', max_length=200, unique=True)
    type = models.SmallIntegerField(verbose_name='Тип биоматериала')


class BiomaterialContainer(models.Model):
    biomaterial = models.ForeignKey(Biomaterial, models.CASCADE, verbose_name='Биоматериал', unique=False)
    container = models.ForeignKey(Container, models.CASCADE, verbose_name='Контейнер', unique=False)


class BiomaterialContainerGroup(models.Model):
    biomaterial_container = models.ManyToManyField(BiomaterialContainer, related_name='Группы')


class TestSet(models.Model):
    key_code = models.CharField(verbose_name='Ключ набора тестов', max_length=50, unique=True)
    name = models.CharField(verbose_name='Наименование набора тестов', max_length=250, unique=True)
    date_from = models.DateTimeField(blank=True, null=True)
    date_to = models.DateTimeField(blank=True, null=True)
    department = models.CharField(verbose_name='Отдел', max_length=15, default='не определен')
    addendum_key = models.CharField(verbose_name='Код выгрузки приложения в портал', max_length=50, default=None, null=True)
    tests = models.ManyToManyField(Test, related_name='Тесты_в_наборе')
    place_of_execution = models.ManyToManyField(PlaceOfExecution, related_name='Места_выполнения')


class Service(models.Model):
    class Meta:
        verbose_name = 'Услуги'

    code = models.CharField(verbose_name='Код номенклатура', max_length=50, unique=True)
    tcle_code = models.CharField(verbose_name='Код услуги в TCLE', max_length=50, null=True, blank=True)
    tcle_abbreviation = models.CharField(verbose_name='Ключ (аббревиатура) услуги в TCLE', null= True, max_length=50, blank=True)
    kdl_service_key = models.CharField(verbose_name='Кдл. Услуга. Ключ', max_length=50, blank=True, null= True)
    kdl_service_perm_code = models.CharField(verbose_name='Кдл. Услуга. Пермь. Код', max_length=50, blank=True, null= True)
    name = models.CharField(verbose_name='Наименование', max_length=1200)
    test_set = models.ForeignKey(TestSet, models.SET_NULL, verbose_name='Набор тестов', null=True)
    blanks = models.CharField(verbose_name='Бланки', max_length=256, blank=True, null=True)
    container = models.CharField(verbose_name='контейнеры', max_length=256, blank=True, null=True)
    biomaterials = models.CharField(verbose_name='Биоматериалы', max_length=256, blank=True, null=True)
    bm_cont_groups = models.ManyToManyField(BiomaterialContainerGroup, related_name='биоматериалы')
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


class UploadFiles(models.Model):
    service = models.ForeignKey(Service, models.SET_NULL, verbose_name='Услуга', null=True)
    file = models.FileField(verbose_name='файл', blank=True, null=True, upload_to='files')
    filename = models.CharField(verbose_name='имя файла', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.filename


class Profile(Service):
    class Meta:
        verbose_name = 'Профили'

    services = models.ManyToManyField(Service, related_name = 'услуги')

class MadicineData(models.Model):
    service = models.ForeignKey(Service, models.SET_NULL, null=True)
    alter_name_KC = models.TextField(verbose_name='Альтернативные названия для КЦ', blank=True, null=True)
    alter_name = models.TextField(verbose_name='Альтернативные названия', blank=True, null=True)
    note = models.TextField(verbose_name='Примечание', blank=True, null=True)
    volume_pp = models.TextField(verbose_name='Объём ПП', blank=True, null=True)
    container_pp = models.TextField(verbose_name='Контейнер для ПП', blank=True, null=True)
    guide_pp = models.TextField(verbose_name='Инструкция по взятию ПП',  blank=True, null=True)
    transport_conditions = models.TextField(verbose_name='Условия транспортировки', blank=True, null=True)
    term_assign = models.TextField(verbose_name='Срок доназначения', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    method = models.TextField(verbose_name='Метод исследования', blank=True, null=True)
    factors = models.TextField(verbose_name='Влияние различных факторов на результат', blank=True, null=True)
    preparation = models.TextField(verbose_name='Подготовка к исследованию', blank=True, null=True)


# class Client(models.Model):
#     code_laport = models.CharField()
#     code_portal = models.CharField()
#     name = models.CharField(verbose_name='')
#

#
# class PlaceOfExecution(models.Model):
#     city = models.CharField()
#     type = models.CharField()
