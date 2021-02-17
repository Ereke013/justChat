# Generated by Django 3.1.6 on 2021-02-17 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_remove_message_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.person'),
        ),
    ]