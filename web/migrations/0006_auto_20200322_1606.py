# Generated by Django 3.0.4 on 2020-03-22 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_dashboardelement'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardelement',
            name='is_embed',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dashboardelement',
            name='is_link',
            field=models.BooleanField(default=False),
        ),
    ]
