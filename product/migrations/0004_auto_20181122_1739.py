# Generated by Django 2.1.3 on 2018-11-22 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20181122_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_data',
            name='category',
            field=models.CharField(choices=[('cloth', 'Cloth'), ('stationary', 'Stationary'), ('grocery', 'Grocery'), ('vegetables', 'Vegetables')], max_length=20),
        ),
    ]
