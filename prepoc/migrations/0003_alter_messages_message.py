# Generated by Django 4.1.7 on 2023-04-14 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prepoc', '0002_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='message',
            field=models.JSONField(),
        ),
    ]
