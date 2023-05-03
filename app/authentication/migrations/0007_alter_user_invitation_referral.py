# Generated by Django 4.1.2 on 2023-05-02 13:39

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_remove_user_email_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='invitation_referral',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcdefg1234', length=8, max_length=15, prefix=''),
        ),
    ]