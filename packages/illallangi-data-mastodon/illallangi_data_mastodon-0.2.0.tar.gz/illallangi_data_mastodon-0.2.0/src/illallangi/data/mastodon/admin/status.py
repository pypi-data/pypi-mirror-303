from django.contrib.admin import ModelAdmin, register

from illallangi.data.mastodon.models import Status


@register(Status)
class StatusModelAdmin(ModelAdmin):
    pass
