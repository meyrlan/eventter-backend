# Generated by Django 3.2.12 on 2022-10-17 15:23

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_event_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='event/photos/', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='event/photos/', verbose_name='Photo'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]