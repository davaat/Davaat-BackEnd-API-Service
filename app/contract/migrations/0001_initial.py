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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='دسته بندی')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('status', models.CharField(blank=True, choices=[('تکمیل شده', 'تکمیل شده'), ('تدوین قرارداد', 'تدوین قرارداد'), ('منتظر تایید', 'منتظر تایید'), ('منتظر امضا', 'منتظر امضا'), ('پایان مهلت امضا', 'پایان مهلت امضا')], max_length=256, null=True)),
                ('body', models.TextField(max_length=1000)),
                ('conclusion_date', models.CharField(blank=True, max_length=256, null=True, verbose_name='تاریخ انعقاد')),
                ('end_date', models.CharField(blank=True, max_length=256, null=True, verbose_name='تاریخ پایان')),
                ('file', models.FileField(blank=True, null=True, upload_to='files', verbose_name='فایل های ضمیمه شده')),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='contract.category')),
                ('contracting_party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracting_party', to=settings.AUTH_USER_MODEL, verbose_name='طرف قرارداد')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]