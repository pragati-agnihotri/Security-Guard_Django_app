

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('securityapp', '0012_trackinghistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackinghistory',
            name='remark',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trackinghistory',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
