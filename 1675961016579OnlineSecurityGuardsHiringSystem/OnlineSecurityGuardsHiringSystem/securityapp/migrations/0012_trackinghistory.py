

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('securityapp', '0011_auto_20221221_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trackinghistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.CharField(blank=True, default='Not Updated Yet', max_length=100, null=True)),
                ('status', models.CharField(blank=True, default='Not Updated Yet', max_length=100, null=True)),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
                ('booking', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='securityapp.booking')),
                ('guard', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='securityapp.guard')),
            ],
        ),
    ]
