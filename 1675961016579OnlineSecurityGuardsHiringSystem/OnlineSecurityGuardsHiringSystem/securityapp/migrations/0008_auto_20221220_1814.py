

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityapp', '0007_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='mobilenumber',
            new_name='mobileno',
        ),
    ]
