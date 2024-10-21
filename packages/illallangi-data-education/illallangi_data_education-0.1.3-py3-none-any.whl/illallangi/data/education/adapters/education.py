from typing import ClassVar

import diffsync

from illallangi.data.education.diffsyncmodels import Course
from illallangi.data.education.models import Course as DjangoCourse


class EducationAdapter(diffsync.Adapter):
    Course = Course

    top_level: ClassVar = [
        "Course",
    ]

    type = "django_education"

    def load(
        self,
    ) -> None:
        if self.count() > 0:
            return

        for obj in DjangoCourse.objects.all():
            self.add(
                Course(
                    pk=obj.pk,
                    label=obj.label,
                    country=obj.country,
                    finish=obj.finish,
                    institution=obj.institution,
                    locality=obj.locality,
                    olc=obj.olc,
                    postal_code=obj.postal_code,
                    region=obj.region,
                    start=obj.start,
                    street=obj.street,
                ),
            )
