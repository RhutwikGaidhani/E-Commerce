# Generated by Django 4.0.3 on 2022-06-21 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_addproduct_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='addproductid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='home.addproduct'),
            preserve_default=False,
        ),
    ]
