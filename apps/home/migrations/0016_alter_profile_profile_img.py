# Generated by Django 4.0.3 on 2022-06-26 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_merge_0011_alter_profile_phone_number_0014_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='filepath'),
        ),
    ]
