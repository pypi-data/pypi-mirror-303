import diffsync
from partial_date import PartialDate

from illallangi.data.education.models.course import (
    Course as ModelCourse,
)


class Course(diffsync.DiffSyncModel):
    pk: int

    label: str

    country: str
    finish: PartialDate | None
    institution: str
    locality: str
    olc: str
    postal_code: str
    region: str
    start: PartialDate | None
    street: str

    _modelname = "Course"
    _identifiers = ("label",)
    _attributes = (
        "country",
        "finish",
        "institution",
        "locality",
        "olc",
        "postal_code",
        "region",
        "start",
        "street",
    )

    @classmethod
    def create(
        cls,
        adapter: diffsync.Adapter,
        ids: dict,
        attrs: dict,
    ) -> "Course":
        obj = ModelCourse.objects.update_or_create(
            label=ids["label"],
            defaults={
                "country": attrs["country"],
                "finish": attrs["finish"],
                "institution": attrs["institution"],
                "locality": attrs["locality"],
                "olc": attrs["olc"],
                "postal_code": attrs["postal_code"],
                "region": attrs["region"],
                "start": attrs["start"],
                "street": attrs["street"],
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
    ) -> "Course":
        ModelCourse.objects.filter(
            pk=self.pk,
        ).update(
            **attrs,
        )

        return super().update(attrs)

    def delete(
        self,
    ) -> "Course":
        ModelCourse.objects.get(
            pk=self.pk,
        ).delete()

        return super().delete()
