from django.apps import AppConfig
from django.conf import settings

from illallangi.django.data.models.models_manager import ModelsManager
from illallangi.rdf.adapters import EducationAdapter as RDFAdapter


class EducationalHistoryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "illallangi.data.education"

    def ready(self) -> None:
        ModelsManager().add_model(
            url="courses_html",
            singular="Course",
            plural="Courses",
            icon="education/courses.jpg",
            description="Each lesson unlocks new doors to knowledge, empowering you to shape your future.",
            model="illallangi.data.education.models.Course",
        )

        def synchronize() -> None:
            from illallangi.data.education.adapters import (
                EducationAdapter as DjangoAdapter,
            )

            src = RDFAdapter(
                **settings.RDF,
            )
            dst = DjangoAdapter()

            src.load(
                **settings.EDUCATION,
            )
            dst.load()

            src.sync_to(dst)

        ModelsManager().add_synchronize(
            name=__name__,
            synchronize=synchronize,
        )
