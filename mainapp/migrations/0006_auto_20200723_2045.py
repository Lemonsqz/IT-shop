

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20200722_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='sd',
            field=models.BooleanField(default=True, verbose_name='Наличие SD карты'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='sd_volume_max',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Максимальный объем встраивамой памяти'),
        ),
    ]
