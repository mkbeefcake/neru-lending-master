# Generated by Django 3.2.5 on 2023-01-11 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0057_auto_20230105_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigationlinks',
            name='is_whitelabel_site',
            field=models.BooleanField(default=False),
        ),
    ]