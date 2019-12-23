# Generated by Django 2.1.4 on 2019-02-25 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_criminal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('complent_id', models.AutoField(primary_key=True, serialize=False)),
                ('complent_type', models.CharField(max_length=20)),
                ('complient_name', models.CharField(max_length=30)),
                ('date_of_complent', models.DateTimeField()),
                ('description', models.CharField(max_length=500)),
                ('proof', models.FileField(upload_to='Doucuments/proof')),
                ('station_id', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=30)),
            ],
        ),
    ]
