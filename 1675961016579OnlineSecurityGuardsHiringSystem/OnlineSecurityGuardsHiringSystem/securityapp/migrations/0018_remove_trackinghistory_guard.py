

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityapp', '0017_booking_guard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trackinghistory',
            name='guard',
        ),
    ]
