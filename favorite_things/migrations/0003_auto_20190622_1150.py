# Generated by Django 2.0.3 on 2019-06-22 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_things', '0002_auto_20190621_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='ranking',
            field=models.IntegerField(unique=True),
        ),
    ]
