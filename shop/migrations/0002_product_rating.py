# Generated by Django 4.0.3 on 2022-12-11 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.FloatField(blank=True, default=5.0, null=True),
        ),
    ]