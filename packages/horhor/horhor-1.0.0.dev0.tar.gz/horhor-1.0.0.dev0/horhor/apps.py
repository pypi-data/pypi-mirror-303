from django.apps import AppConfig


class horhorConfig(AppConfig):
    name = "horhor"
    verbose_name = "Wagtail CRX"
    # TODO: At some point in the future, change this to BigAutoField and create
    # the corresponding migration for concrete models in horhor.
    default_auto_field = "django.db.models.AutoField"
