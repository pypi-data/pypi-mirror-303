from django.contrib.admin import ModelAdmin, register

from illallangi.data.residential.models import Residence


@register(Residence)
class ResidenceModelAdmin(ModelAdmin):
    pass
