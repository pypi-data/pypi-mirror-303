from django.contrib.admin import ModelAdmin, register

from illallangi.data.air_transport.models import Flight


@register(Flight)
class FlightModelAdmin(ModelAdmin):
    pass
