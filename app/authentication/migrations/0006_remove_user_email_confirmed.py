# Generated by Django 4.1.2 on 2023-05-02 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_city_rename_company_user_company_display_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email_confirmed',
        ),
    ]
