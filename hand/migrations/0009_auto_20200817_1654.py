# Generated by Django 3.0.7 on 2020-08-17 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hand', '0008_auto_20200817_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='currently_a',
            field=models.CharField(choices=[('Hospital', 'Hospital'), ('Hotel', 'Hotel'), ('School', 'School')], default='Hospital', max_length=20),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='no_of_rooms',
            field=models.IntegerField(),
        ),
    ]
