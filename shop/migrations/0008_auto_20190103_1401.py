# Generated by Django 2.1.3 on 2019-01-03 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20190103_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='Shop_icon',
            field=models.ImageField(upload_to='', verbose_name='Shop Photo 1'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='Shop_icon_2',
            field=models.ImageField(null=True, upload_to='', verbose_name='Shop Photo 2'),
        ),
    ]
