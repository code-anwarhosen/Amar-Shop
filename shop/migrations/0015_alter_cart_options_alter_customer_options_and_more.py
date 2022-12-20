# Generated by Django 4.0.5 on 2022-12-19 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0014_remove_orderplaced_is_deliverd'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['added_at']},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='orderplaced',
            options={'ordering': ['ordered_at']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['added_at']},
        ),
        migrations.AlterField(
            model_name='customer',
            name='_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customer',
            name='district',
            field=models.CharField(blank=True, choices=[('dhaka', 'Dhaka'), ('gazipur', 'Gazipur')], max_length=20, null=True),
        ),
    ]