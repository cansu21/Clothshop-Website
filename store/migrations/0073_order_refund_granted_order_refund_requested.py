# Generated by Django 4.0.3 on 2022-05-18 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0072_remove_order_order_status_orderproduct_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='refund_granted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='refund_requested',
            field=models.BooleanField(default=False),
        ),
    ]