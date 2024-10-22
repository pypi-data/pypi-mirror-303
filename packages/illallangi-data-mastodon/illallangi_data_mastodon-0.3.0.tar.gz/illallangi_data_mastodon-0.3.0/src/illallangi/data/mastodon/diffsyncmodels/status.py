from datetime import datetime

import diffsync

from illallangi.data.mastodon.models.status import Status as ModelStatus


class Status(
    diffsync.DiffSyncModel,
):
    pk: int
    url: str
    content: str
    datetime: datetime

    _modelname = "Status"
    _identifiers = ("url",)
    _attributes = (
        "content",
        "datetime",
    )

    @classmethod
    def create(
        cls,
        adapter: diffsync.Adapter,
        ids: dict,
        attrs: dict,
    ) -> "Status":
        obj = ModelStatus.objects.update_or_create(
            url=ids["url"],
            defaults={
                "content": attrs["content"],
                "datetime": attrs["datetime"],
            },
        )[0]

        return super().create(
            adapter,
            {
                "pk": obj.pk,
                **ids,
            },
            attrs,
        )

    def update(
        self,
        attrs: dict,
    ) -> "Status":
        ModelStatus.objects.filter(
            pk=self.pk,
        ).update(
            **attrs,
        )

        return super().update(attrs)

    def delete(
        self,
    ) -> "Status":
        ModelStatus.objects.get(
            pk=self.pk,
        ).delete()

        return super().delete()
