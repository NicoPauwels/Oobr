# Generated by Django 3.2.5 on 2021-09-14 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210912_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_customer_user',
        ),
    ]
