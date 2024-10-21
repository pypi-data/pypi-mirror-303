from django.db import migrations

from ..models import ESNSIClassifier


def forwards(apps, schema_editor):
    """Загрузка первоначальных данных справочников для передачи в ЕСНСИ"""

    ESNSIClassifier_model = apps.get_model('smev3_v321', 'ESNSIClassifier')

    for classifier in ESNSIClassifier.classifiers_classes:
        ESNSIClassifier_model.objects.get_or_create(
            name=classifier.__doc__,
            classifier_class=classifier.__name__
        )


class Migration(migrations.Migration):

    dependencies = [
        ('smev3_v321', '0003_esnsiclassifier_updateclassifierrequest'),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
