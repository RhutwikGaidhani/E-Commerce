# Generated by Django 4.0.3 on 2022-06-15 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/filepath'),
        ),
    ]