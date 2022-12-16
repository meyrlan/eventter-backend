# Generated by Django 3.2.12 on 2022-09-15 15:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region='KZ', verbose_name='Phone Number')),
                ('password', models.CharField(max_length=30, verbose_name='Password')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Admin')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Name')),
                ('capacity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Capacity')),
                ('date_time', models.DateTimeField(verbose_name='Date time')),
                ('age_limit', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Age limit')),
                ('description', models.TextField(verbose_name='Description')),
                ('photo', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Interest',
                'verbose_name_plural': 'Interests',
                'db_table': 'interests',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('sex', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1, verbose_name='Sex')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth Date')),
                ('bio', models.TextField(verbose_name='Bio')),
                ('interests', models.ManyToManyField(db_table='interests_profiles', related_name='profiles', to='core.Interest', verbose_name='Interests')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Users')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'db_table': 'profile',
                'sensitive_fields': 'birth_date',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.event', verbose_name='Event')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
                'db_table': 'image',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(db_table='profiles_events', related_name='events', to='core.Profile', verbose_name='Attendees'),
        ),
        migrations.AddField(
            model_name='event',
            name='interests',
            field=models.ManyToManyField(db_table='interests_events', related_name='events', to='core.Interest', verbose_name='Interests'),
        ),
        migrations.AddField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_events', to='core.profile', verbose_name='Owner'),
        ),
    ]
