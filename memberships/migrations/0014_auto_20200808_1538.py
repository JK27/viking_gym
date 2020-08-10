# Generated by Django 3.0.8 on 2020-08-08 15:38

from django.db import migrations, models
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0013_auto_20200808_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermembership',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usermembership',
            name='country',
            field=django_countries.fields.CountryField(default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermembership',
            name='county',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='usermembership',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermembership',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermembership',
            name='full_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermembership',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermembership',
            name='postcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='usermembership',
            name='street_address1',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermembership',
            name='street_address2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='usermembership',
            name='town_or_city',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]