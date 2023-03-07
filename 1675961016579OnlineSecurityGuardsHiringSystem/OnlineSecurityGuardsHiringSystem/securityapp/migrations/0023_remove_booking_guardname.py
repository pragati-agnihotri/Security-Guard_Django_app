

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityapp', '0022_booking_guardname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='guardname',
        ),
    ]
