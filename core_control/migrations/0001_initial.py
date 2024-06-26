# Generated by Django 5.0.3 on 2024-03-31 10:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.SlugField(default='')),
                ('product_description', models.TextField(db_index=True, default='')),
                ('Date_created', models.DateField(auto_now_add=True)),
                ('orignal_price', models.PositiveIntegerField(db_index=True, default=0)),
                ('tax_price', models.PositiveIntegerField(db_index=True, default=0, null=True)),
                ('delivery_price', models.PositiveIntegerField(db_index=True, default=0, null=True)),
                ('tag', models.CharField(default='', max_length=50)),
                ('published', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(db_index=True, default=None, upload_to='product/images')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, default='', max_length=100)),
                ('last_name', models.CharField(db_index=True, default='', max_length=100)),
                ('phone_no', models.BigIntegerField(db_index=True)),
                ('state', models.CharField(db_index=True, default='', max_length=100)),
                ('city', models.CharField(db_index=True, default='', max_length=100)),
                ('street_no', models.CharField(db_index=True, default='', max_length=300)),
                ('postal_code', models.CharField(db_index=True, default='', max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='useraddress', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(db_index=True, default='', max_length=100)),
                ('status', models.CharField(choices=[('Cancel', 'Cancel'), ('Delivered', 'Delivered'), ('Return', 'Return')], db_index=True, default='', max_length=100)),
                ('total_price', models.PositiveIntegerField(db_index=True)),
                ('quatity', models.PositiveIntegerField(db_index=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_cancel', models.DateField(auto_now_add=True, null=True)),
                ('date_return', models.DateField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('products', models.ManyToManyField(db_index=True, default='', to='core_control.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(db_index=True, default=None, to='core_control.productimages'),
        ),
    ]
