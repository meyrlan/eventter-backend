# Generated by Django 3.2.12 on 2022-09-15 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(db_table='interests_participants', related_name='participants', to='core.Profile', verbose_name='Participants'),
        ),
    ]
