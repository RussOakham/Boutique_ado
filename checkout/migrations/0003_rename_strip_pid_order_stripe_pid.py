# Generated by Django 3.2.3 on 2021-06-01 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20210601_1500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='strip_pid',
            new_name='stripe_pid',
        ),
    ]
