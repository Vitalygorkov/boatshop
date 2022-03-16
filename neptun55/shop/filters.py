from .models import Boat,Category
import django_filters
class BoatFilter(django_filters.FilterSet):
    # Category.objects.filter(url='lodki').get_descendants(include_self=False)
    keel = django_filters.BooleanFilter(field_name='keel', label='Киль')
    bulwark = django_filters.BooleanFilter(field_name='bulwark', label='Фальшборт')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.filter(url='lodki').get_descendants(include_self=False), label='Тип дна:')
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label='Цена(руб) от:')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt', label='Цена(руб) до:')
    # manufacturer = django_filters.MultipleChoiceFilter(field_name='manufacturer')
    # manufacturer = django_filters.ChoiceFilter(field_name='manufacturer')
    length__gt = django_filters.NumberFilter(field_name='length', lookup_expr='gt', label='Длинна(см) от:')
    length__lt = django_filters.NumberFilter(field_name='length', lookup_expr='lt', label='Длинна(см) до:')
    width__gt = django_filters.NumberFilter(field_name='width', lookup_expr='gt', label='Ширина(см) от:')
    width__lt = django_filters.NumberFilter(field_name='width', lookup_expr='lt', label='Ширина(см) до:')
    load_capacity__gt = django_filters.NumberFilter(field_name='load_capacity', lookup_expr='gt', label='Грузоподъемность(кг) от:')
    load_capacity__lt = django_filters.NumberFilter(field_name='load_capacity', lookup_expr='lt', label='Грузоподъемность(кг) до:')
    boat_weight__gt = django_filters.NumberFilter(field_name='boat_weight', lookup_expr='gt', label='Вес лодки(кг) от:')
    boat_weight__lt = django_filters.NumberFilter(field_name='boat_weight', lookup_expr='lt', label='Вес лодки(кг) до:')
    complete_set_weight__gt = django_filters.NumberFilter(field_name='complete_set_weight', lookup_expr='gt', label='Вес полного комплекта(кг) от:')
    complete_set_weight__lt = django_filters.NumberFilter(field_name='complete_set_weight', lookup_expr='lt', label='Вес полного комплекта(кг) до:')
    passenger_capacity__gt = django_filters.NumberFilter(field_name='passenger_capacity', lookup_expr='gt', label='Пассажировместимость(чел) от:')
    passenger_capacity__lt = django_filters.NumberFilter(field_name='passenger_capacity', lookup_expr='lt', label='Пассажировместимость(чел) до:')
    maximum_motor_power__gt = django_filters.NumberFilter(field_name='maximum_motor_power', lookup_expr='gt', label='Максимальная мощность мотора(лс) от:')
    maximum_motor_power__lt = django_filters.NumberFilter(field_name='maximum_motor_power', lookup_expr='lt', label='Максимальная Мощность мотора(лс) до:')

    cockpit_length__gt = django_filters.NumberFilter(field_name='cockpit_length', lookup_expr='gt', label='Длинна кокпита (см) от:')
    cockpit_length__lt = django_filters.NumberFilter(field_name='cockpit_length', lookup_expr='lt', label='Длинна кокпита (см) до:')
    cockpit_width__gt = django_filters.NumberFilter(field_name='cockpit_width', lookup_expr='gt', label='Длинна кокпита (см) от:')
    cockpit_width__lt = django_filters.NumberFilter(field_name='cockpit_width', lookup_expr='lt', label='Ширина кокпита (см) до:')
    fabric_thickness_side__gt = django_filters.NumberFilter(field_name='fabric_thickness_side', lookup_expr='gt', label='Плотность ткани борта (г/м²) от:')
    fabric_thickness_side__lt = django_filters.NumberFilter(field_name='fabric_thickness_side', lookup_expr='lt', label='Плотность ткани борта (г/м²) до:')
    fabric_thickness_bottom__gt = django_filters.NumberFilter(field_name='fabric_thickness_bottom', lookup_expr='gt', label='Плотность ткани дна (г/м²) от:')
    fabric_thickness_bottom__lt = django_filters.NumberFilter(field_name='fabric_thickness_bottom', lookup_expr='lt', label='Плотность ткани дна (г/м²) до:')
    inflatable_compartments__gt = django_filters.NumberFilter(field_name='inflatable_compartments', lookup_expr='gt', label='Количество надувных отсеков от:')
    inflatable_compartments__lt = django_filters.NumberFilter(field_name='inflatable_compartments', lookup_expr='lt', label='Количество надувных отсеков до:')

    class Meta:
        model = Boat

        fields = ['manufacturer',]

        # widgets = {
        #     "price__gt":
        #
        # }