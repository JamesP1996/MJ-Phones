# Generated by Django 3.0.3 on 2020-03-01 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Phones', '0006_auto_20200301_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addphone',
            name='fourG',
            field=models.CharField(max_length=3),
        ),
    ]
