# Generated by Django 3.2.5 on 2021-09-09 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business', '0002_alter_business_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='name',
        ),
        migrations.AddField(
            model_name='business',
            name='VAT_number',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='business',
            name='bankaccount_number',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='business',
            name='business_owner',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='business',
            name='contact_number',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='business',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
