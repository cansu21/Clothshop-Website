# Generated by Django 4.0.4 on 2022-05-04 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0032_order_items_alter_order_user_alter_orderitem_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
