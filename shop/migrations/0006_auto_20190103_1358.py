# Generated by Django 2.1.3 on 2019-01-03 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20190103_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='Shop_icon',
            field=models.ImageField(upload_to='', verbose_name='Shop_Photo'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='Shop_icon_2',
            field=models.ImageField(null=True, upload_to='', verbose_name='Shop_Photo_2'),
        ),
    ]
