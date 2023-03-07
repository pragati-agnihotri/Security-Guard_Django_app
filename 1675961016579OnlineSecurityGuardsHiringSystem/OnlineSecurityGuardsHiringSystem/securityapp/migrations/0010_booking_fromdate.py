

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('securityapp', '0009_auto_20221221_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='fromdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
