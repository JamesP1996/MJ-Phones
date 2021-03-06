# Generated by Django 3.0.2 on 2020-04-20 14:44

import Phones.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Phones', '0010_addphone_cpu_cores'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('phoneProductID', models.IntegerField(blank=True, null=True)),
                ('phoneName', models.CharField(blank=True, max_length=40, null=True)),
                ('accessoryProductID', models.IntegerField(blank=True, null=True)),
                ('accessoryName', models.CharField(blank=True, max_length=40, null=True)),
                ('referrence', models.CharField(blank=True, default=Phones.models.random_string, editable=False, max_length=6, unique=True)),
                ('date_ordered', models.DateTimeField(default=datetime.datetime(2020, 4, 20, 15, 44, 43, 361688), editable=False)),
            ],
        ),
    ]
