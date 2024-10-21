from django.contrib.admin import ModelAdmin, register

from illallangi.data.aviation.models import Airport


@register(Airport)
class AirportModelAdmin(ModelAdmin):
    pass
