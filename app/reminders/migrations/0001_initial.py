# Generated by Django 4.1.2 on 2023-04-08 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('reminder_time', models.CharField(max_length=256)),
                ('remind_model', models.CharField(choices=[('یک روز قبل', 'یک روز قبل'), ('دو روز قبل', 'دو روز قبل'), ('سه روز قبل', 'سه روز قبل'), ('یک هفته قبل', 'یک هفته قبل')], default='یک روز قبل', max_length=256)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reminder_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]