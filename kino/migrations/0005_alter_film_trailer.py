# Generated by Django 3.2.9 on 2021-12-01 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0004_alter_film_trailer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='trailer',
            field=models.URLField(blank=True),
        ),
    ]
