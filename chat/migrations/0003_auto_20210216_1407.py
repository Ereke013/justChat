# Generated by Django 3.1.6 on 2021-02-16 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_person'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'пользователь', 'verbose_name_plural': 'пользователи'},
        ),
        migrations.RenameField(
            model_name='person',
            old_name='users',
            new_name='user',
        ),
    ]