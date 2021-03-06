# Generated by Django 3.0.4 on 2020-03-22 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20200322_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=100)),
                ('posted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web.contact')),
            ],
        ),
    ]
