# Generated by Django 2.1.4 on 2019-02-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190221_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='police',
            name='station_id',
            field=models.IntegerField(),
        ),
    ]
