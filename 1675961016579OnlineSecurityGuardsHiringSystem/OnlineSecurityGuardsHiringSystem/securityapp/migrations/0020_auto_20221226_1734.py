

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityapp', '0019_auto_20221226_1634'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='guard',
            new_name='guardname',
        ),
        migrations.RenameField(
            model_name='trackinghistory',
            old_name='guard',
            new_name='guardname',
        ),
    ]
