# Generated by Django 2.1.3 on 2018-12-29 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_shop_shop_icon_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='address_State',
            field=models.CharField(choices=[('BR', 'Bihar'), ('JH', 'Jharkhand'), ('UT', 'Uttar Pradesh'), ('DH', 'Delhi')], max_length=20),
        ),
    ]
