# Generated by Django 3.2.4 on 2021-06-30 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Blog'},
        ),
    ]
