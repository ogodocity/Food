# Generated by Django 3.1.13 on 2023-09-02 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('image2', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('image3', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('image4', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('image5', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('category', models.CharField(choices=[('Gadgets', 'Gadgets'), ('Drones', 'Drones'), ('Batteries', 'Batteries'), ('Panels', 'Panels'), ('Home Appliances', 'Home Appliances'), ('Electric Autos', 'Electric Autos')], max_length=30)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(default=None, max_length=300)),
                ('Address', models.CharField(default=None, max_length=300)),
                ('delivery_address', models.CharField(default=None, max_length=300)),
                ('delivery_port', models.CharField(default=None, max_length=300)),
                ('products', models.TextField()),
                ('email', models.CharField(default=None, max_length=300)),
                ('Phone', models.CharField(max_length=15)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order_number', models.PositiveIntegerField(default=None, editable=False, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
