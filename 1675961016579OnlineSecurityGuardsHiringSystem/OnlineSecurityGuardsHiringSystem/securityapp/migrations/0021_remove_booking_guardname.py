

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityapp', '0020_auto_20221226_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='guardname',
        ),
    ]
