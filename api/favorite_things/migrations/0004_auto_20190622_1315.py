# Generated by Django 2.0.3 on 2019-06-22 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_things', '0003_auto_20190622_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='audit_log',
        ),
        migrations.AlterField(
            model_name='favorite',
            name='description',
            field=models.CharField(choices=[('pe', 'person'), ('pl', 'place'), ('fo', 'food')], max_length=300),
        ),
    ]
