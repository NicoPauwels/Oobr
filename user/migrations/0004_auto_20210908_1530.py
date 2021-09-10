# Generated by Django 3.2.5 on 2021-09-08 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_customuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_business_user',
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_customer_user',
            field=models.BooleanField(default=False),
        ),
    ]
