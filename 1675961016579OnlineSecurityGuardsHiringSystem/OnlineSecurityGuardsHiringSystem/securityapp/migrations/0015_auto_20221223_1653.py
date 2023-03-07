

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityapp', '0014_trackinghistory_mobilenum'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='mobile',
            new_name='mobilenum',
        ),
        migrations.RemoveField(
            model_name='trackinghistory',
            name='mobilenum',
        ),
    ]
