# Generated by Django 2.0.3 on 2019-06-25 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_things', '0011_auto_20190624_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
    ]
