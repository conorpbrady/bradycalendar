# Generated by Django 4.2.7 on 2023-12-02 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0002_rename_events_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='second_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]