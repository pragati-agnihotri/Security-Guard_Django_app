

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('securityapp', '0008_auto_20221220_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(blank=True, default='Not Updated Yet', max_length=100, null=True),
        ),
    ]
