# Generated by Django 3.1.3 on 2020-11-23 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0005_auto_20201123_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='gpa',
            field=models.DecimalField(decimal_places=3, max_digits=3),
        ),
    ]
