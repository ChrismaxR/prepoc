# Generated by Django 4.1.7 on 2023-04-14 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prepoc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messageId', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]