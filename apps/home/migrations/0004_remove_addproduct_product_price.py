# Generated by Django 4.0.3 on 2022-06-11 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addproduct',
            name='product_price',
        ),
    ]