from django.contrib.admin import ModelAdmin, register

from illallangi.data.fitness.models import Swim


@register(Swim)
class SwimModelAdmin(ModelAdmin):
    pass
