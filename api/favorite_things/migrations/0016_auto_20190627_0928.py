# Generated by Django 2.0.3 on 2019-06-27 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_things', '0015_auto_20190625_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
