from django.contrib.admin import ModelAdmin, register

from illallangi.data.aviation.models import Airline


@register(Airline)
class AirlineModelAdmin(ModelAdmin):
    pass
