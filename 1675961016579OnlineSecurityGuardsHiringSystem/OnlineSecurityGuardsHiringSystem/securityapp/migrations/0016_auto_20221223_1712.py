

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityapp', '0015_auto_20221223_1653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='mobilenum',
            new_name='mobile',
        ),
    ]
