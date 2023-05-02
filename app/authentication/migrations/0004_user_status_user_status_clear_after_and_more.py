# Generated by Django 4.1.2 on 2023-05-02 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_user_birth_date_remove_user_father_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='status_clear_after',
            field=models.CharField(blank=True, choices=[("don't clear", "don't clear"), ('30 min', '30 min'), ('1 hour', '1 hour'), ('24 hour', '24 hour'), ('this week', 'this week')], max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='status_set_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
