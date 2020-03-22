# Generated by Django 3.0.2 on 2020-03-22 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeadlineModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadline_PS2TS', models.DateTimeField(blank=True, null=True)),
                ('deadline_TS2PS', models.DateTimeField(blank=True, null=True)),
                ('is_active_PS2TS', models.BooleanField(default=False)),
                ('is_active_TS2PS', models.BooleanField(default=False)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('campus', models.IntegerField(blank=True, choices=[(0, 'Goa'), (1, 'Hyderabad'), (2, 'Pilani')], null=True)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('user_type', models.IntegerField(blank=True, choices=[(0, 'Student'), (1, 'Supervisor'), (2, 'Head of Department'), (3, 'Associate Dean'), (4, 'PS-Division')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PS2TSTransfer',
            fields=[
                ('applicant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='transfers.UserProfile')),
                ('supervisor_email', models.EmailField(max_length=254)),
                ('hod_email', models.EmailField(max_length=254)),
                ('sub_type', models.IntegerField(choices=[(0, 'PS to TS (Single Degree)'), (1, 'PS-TS/TS-PS to TS-TS (Dual Degree)')])),
                ('cgpa', models.DecimalField(decimal_places=2, max_digits=6)),
                ('thesis_locale', models.IntegerField(choices=[(0, 'On Campus'), (1, 'Off Campus (India)'), (2, 'Off Campus (Abroad)'), (3, 'Off Campus (Industry)')])),
                ('thesis_subject', models.CharField(help_text='Broad area/Title of Thesis', max_length=150)),
                ('name_of_org', models.CharField(help_text='Name of BITS Campus or Organization where thesis will be carried', max_length=100)),
                ('expected_deliverables', models.TextField(help_text='Expected outcome of thesis')),
                ('is_supervisor_approved', models.IntegerField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Rejected')], default=0)),
                ('is_hod_approved', models.IntegerField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Rejected')], default=0)),
                ('is_ad_approved', models.IntegerField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Rejected')], default=0)),
                ('comments_from_supervisor', models.TextField(blank=True, null=True)),
                ('comments_from_hod', models.TextField(blank=True, null=True)),
                ('comments_from_ad', models.TextField(blank=True, null=True)),
                ('application_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'PS to TS Application',
                'verbose_name_plural': 'PS to TS Applications',
            },
        ),
        migrations.CreateModel(
            name='TS2PSTransfer',
            fields=[
                ('applicant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='transfers.UserProfile')),
                ('hod_email', models.EmailField(max_length=254)),
                ('sub_type', models.IntegerField(choices=[(0, 'TS to PS (Single Degree)'), (1, 'PS-TS to PS-PS (Dual Degree)'), (2, 'TS-TS to TS-PS (Dual Degree)')])),
                ('cgpa', models.DecimalField(decimal_places=2, max_digits=6)),
                ('reason_for_transfer', models.TextField()),
                ('name_of_org', models.CharField(help_text='Name of BITS Campus or Organization where thesis was being carried', max_length=100)),
                ('is_hod_approved', models.IntegerField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Rejected')], default=0)),
                ('is_ad_approved', models.IntegerField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Rejected')], default=0)),
                ('comments_from_hod', models.TextField(blank=True, null=True)),
                ('comments_from_ad', models.TextField(blank=True, null=True)),
                ('application_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'TS to PS Application',
                'verbose_name_plural': 'TS to PS Applications',
            },
        ),
    ]
