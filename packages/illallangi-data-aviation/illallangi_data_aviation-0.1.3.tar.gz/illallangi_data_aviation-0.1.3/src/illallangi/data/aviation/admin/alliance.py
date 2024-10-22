from django.contrib.admin import ModelAdmin, register

from illallangi.data.aviation.models import Alliance


@register(Alliance)
class AllianceModelAdmin(ModelAdmin):
    pass
