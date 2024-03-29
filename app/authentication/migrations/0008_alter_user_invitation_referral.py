# Generated by Django 4.1.2 on 2023-05-02 13:42

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_user_invitation_referral'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='invitation_referral',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcdefg1234', length=10, max_length=15, prefix='', unique=True),
        ),
    ]
