#

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('securityapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guard',
            name='pic',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
