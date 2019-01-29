# Generated by Django 2.1.5 on 2019-01-27 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_auto_20190103_1233'),
        ('order', '0007_auto_20190127_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_order_products',
            name='ordered_product',
        ),
        migrations.AddField(
            model_name='user_order_products',
            name='ordered_product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='product.product_data'),
            preserve_default=False,
        ),
    ]
