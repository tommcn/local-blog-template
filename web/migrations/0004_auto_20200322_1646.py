# Generated by Django 3.0.4 on 2020-03-22 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_blogpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(),
        ),
    ]