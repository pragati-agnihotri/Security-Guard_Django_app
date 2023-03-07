

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('securityapp', '0004_auto_20221217_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='adminname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
