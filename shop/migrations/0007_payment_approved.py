# Generated by Django 4.0.3 on 2022-12-21 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_payment_amount_alter_payment_due_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='approved',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
