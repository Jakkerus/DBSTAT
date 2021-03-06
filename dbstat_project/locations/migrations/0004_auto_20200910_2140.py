# Generated by Django 3.1.1 on 2020-09-10 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_auto_20200910_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations',
            name='number_cages',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='opened',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='sqft',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
