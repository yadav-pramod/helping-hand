# Generated by Django 3.0.7 on 2020-08-17 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hand', '0009_auto_20200817_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='corona',
        ),
        migrations.AddField(
            model_name='hospital',
            name='corona_test_availability',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=0, max_length=20),
            preserve_default=False,
        ),
    ]
