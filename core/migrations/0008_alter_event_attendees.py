# Generated by Django 3.2.12 on 2022-10-18 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20221017_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(blank=True, db_table='profiles_events', related_name='events', to='core.Profile', verbose_name='Attendees'),
        ),
    ]