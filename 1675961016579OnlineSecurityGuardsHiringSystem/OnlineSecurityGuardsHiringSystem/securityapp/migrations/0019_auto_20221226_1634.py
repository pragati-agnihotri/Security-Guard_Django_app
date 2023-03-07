

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('securityapp', '0018_remove_trackinghistory_guard'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackinghistory',
            name='guard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='securityapp.guard'),
        ),
        migrations.AlterField(
            model_name='trackinghistory',
            name='remark',
            field=models.CharField(blank=True, default='Not Updated Yet', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trackinghistory',
            name='status',
            field=models.CharField(blank=True, default='Not Updated Yet', max_length=100, null=True),
        ),
    ]
