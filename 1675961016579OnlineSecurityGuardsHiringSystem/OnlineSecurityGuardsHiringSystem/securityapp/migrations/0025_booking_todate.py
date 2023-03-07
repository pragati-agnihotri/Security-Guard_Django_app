from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('securityapp', '0024_booking_guardname'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='todate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
