# Generated by Django 3.0.8 on 2020-08-10 13:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memberships', '0016_auto_20200810_1302'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserMembership',
            new_name='Subscriptions',
        ),
    ]
