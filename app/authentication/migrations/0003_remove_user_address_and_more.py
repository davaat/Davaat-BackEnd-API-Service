# Generated by Django 4.1.2 on 2023-02-13 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_national_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='birth_certificate_file',
        ),
        migrations.RemoveField(
            model_name='user',
            name='car_insurance_file',
        ),
        migrations.RemoveField(
            model_name='user',
            name='car_technical_inspection_file',
        ),
        migrations.RemoveField(
            model_name='user',
            name='driver_rate',
        ),
        migrations.RemoveField(
            model_name='user',
            name='driving_license_file',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_driver',
        ),
        migrations.RemoveField(
            model_name='user',
            name='landline_phone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='location',
        ),
        migrations.RemoveField(
            model_name='user',
            name='national_card_file',
        ),
        migrations.RemoveField(
            model_name='user',
            name='post_code',
        ),
        migrations.RemoveField(
            model_name='user',
            name='wallet_inventory',
        ),
    ]