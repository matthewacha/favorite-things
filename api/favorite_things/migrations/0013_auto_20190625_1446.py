# Generated by Django 2.0.3 on 2019-06-25 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_things', '0012_auto_20190625_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='owner',
            new_name='customuser',
        ),
    ]
