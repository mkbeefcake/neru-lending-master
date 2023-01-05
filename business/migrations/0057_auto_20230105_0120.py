# Generated by Django 3.2.5 on 2023-01-05 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0056_alter_navigationlinks_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigationlinks',
            name='is_every_site',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='navigationlinks',
            name='is_main_site',
            field=models.BooleanField(default=False),
        ),
    ]
