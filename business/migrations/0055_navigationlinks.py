# Generated by Django 3.2.5 on 2022-11-15 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0054_auto_20210729_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavigationLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'navigation_links',
            },
        ),
    ]
