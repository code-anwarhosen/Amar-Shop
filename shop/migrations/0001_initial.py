# Generated by Django 4.0.5 on 2022-12-20 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shop.utails


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.CharField(blank=True, max_length=20, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('district', models.CharField(blank=True, choices=[('dhaka', 'Dhaka'), ('gazipur', 'Gazipur')], max_length=20, null=True)),
                ('city', models.CharField(blank=True, choices=[('cantonment-area', 'Cantonment Area'), ('abdullahpur', 'Abdullahpur'), ('uttara', 'Uttara'), ('mirpur', 'Mirpur'), ('pallabi', 'Pallabi'), ('kazipara', 'Kazipara'), ('kafrul', 'Kafrul'), ('agargaon', 'Agargaon'), ('sher-e-bangla', 'ShereBangla'), ('cantonment-area', 'Cantonment Area'), ('banani', 'Banani'), ('gulshan', 'Gulshan'), ('mohakhali', 'Mohakhali'), ('bashundhara', 'Bashundhara'), ('banasree', 'Banasree'), ('baridhara', 'Baridhara'), ('uttarkhan', 'Uttarkhan'), ('dakshinkhan', 'Dakshinkhan'), ('bawnia', 'Bawnia'), ('khilkhet', 'Khilkhet'), ('tejgaon', 'Tejgaon'), ('farmgate', 'Farmgate'), ('mohammadpur', 'Mohammadpur'), ('rampura', 'Rampura'), ('badda', 'Badda'), ('satarkul', 'Satarkul'), ('beraid', 'Beraid'), ('khilgaon', 'Khilgaon'), ('vatara', 'Vatara'), ('gabtali', 'Gabtali')], max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('address', models.TextField()),
                ('_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('total_amount', models.PositiveIntegerField(blank=True, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('packing', 'Packing Started'), ('packed', 'Packed'), ('on_the_way', 'On the way'), ('deliverd', 'Delivered')], default='pending', max_length=10)),
                ('ordered_at', models.DateTimeField(auto_now_add=True)),
                ('_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customer')),
                ('_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['ordered_at'],
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=shop.utails.get_upload_dir)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.CharField(blank=True, max_length=20, primary_key=True, serialize=False, unique=True)),
                ('category', models.CharField(blank=True, choices=[('electronics', 'Electronics'), ('domestic', 'Domestic')], max_length=50, null=True)),
                ('title', models.CharField(max_length=250)),
                ('model', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('normal', 'Normal'), ('lastest', 'Latest Product'), ('featured', 'Featured Product'), ('big_discount', 'Big Discount'), ('exclusive', 'Exclusive')], max_length=20, null=True)),
                ('quantity', models.PositiveIntegerField()),
                ('regular_price', models.PositiveIntegerField()),
                ('discount_price', models.PositiveIntegerField()),
                ('rating', models.FloatField(blank=True, default=5.0, null=True)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ManyToManyField(to='shop.productimage')),
            ],
            options={
                'ordering': ['added_at'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(blank=True, choices=[('cod', 'Cash on delivery'), ('bkash', 'Bkash'), ('nagad', 'Nagad')], max_length=10, null=True)),
                ('amount', models.PositiveIntegerField(blank=True, null=True)),
                ('paid', models.PositiveIntegerField(blank=True, null=True)),
                ('due', models.PositiveIntegerField(blank=True, null=True)),
                ('orders', models.ManyToManyField(to='shop.orderplaced')),
            ],
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.product'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
            options={
                'ordering': ['added_at'],
            },
        ),
    ]
