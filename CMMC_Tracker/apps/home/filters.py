import django_filters
from .models import *

class ControlsFilter(django_filters.FilterSet):
    class Meta:
        model = Control
        fields = '__all__'
        exclude = ['organization']