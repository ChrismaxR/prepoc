# Generated by Django 4.1.7 on 2023-04-18 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prepoc', '0010_alter_messages_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messagessummary',
            name='callMethods',
        ),
        migrations.RemoveField(
            model_name='messagessummary',
            name='callResponse',
        ),
        migrations.RemoveField(
            model_name='messagessummary',
            name='callResponseTimeMs',
        ),
        migrations.RemoveField(
            model_name='messagessummary',
            name='endpoint',
        ),
        migrations.RemoveField(
            model_name='messagessummary',
            name='generationDate',
        ),
        migrations.RemoveField(
            model_name='messagessummary',
            name='messageId',
        ),
        migrations.RemoveField(
            model_name='messagessummary',
            name='messageSize',
        ),
        migrations.RemoveField(
            model_name='messagessummary',
            name='recipientId',
        ),
        migrations.RemoveField(
            model_name='messagessummary',
            name='senderId',
        ),
        migrations.AddField(
            model_name='messagessummary',
            name='messagePriority',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='messagessummary',
            name='messageStatus',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='messagessummary',
            name='numberOfMessages',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
