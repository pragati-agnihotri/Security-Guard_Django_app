

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('securityapp', '0003_register'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Register',
            new_name='Profile',
        ),
    ]
