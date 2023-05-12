# Generated by Django 4.1.2 on 2023-05-11 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_alter_user_invitation_referral'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='invitation_referral',
        ),
        migrations.CreateModel(
            name='InvitationLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('invitation_referral', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefg1234', editable=False, length=10, max_length=15, prefix='', unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]