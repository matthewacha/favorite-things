# Generated by Django 2.0.3 on 2019-06-23 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_things', '0008_auto_20190623_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='ranking',
            field=models.IntegerField(),
        ),
    ]
