# Generated by Django 3.1.6 on 2021-02-16 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20210216_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.group'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='full name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='user_ava',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='User Photo'),
        ),
    ]
