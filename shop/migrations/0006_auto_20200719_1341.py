# Generated by Django 3.0.8 on 2020-07-19 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200719_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='master_category',
            field=models.CharField(blank=True, choices=[('AC', 'Accessories'), ('CL', 'Clothing'), ('TR', 'Trainers'), ('SA', 'On sale')], default='', max_length=2, null=True),
        ),
    ]
