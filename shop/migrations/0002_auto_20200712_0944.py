# Generated by Django 3.0.8 on 2020-07-12 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='imageURL',
            new_name='image_url',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='productDisplayName',
            new_name='name',
        ),
    ]
