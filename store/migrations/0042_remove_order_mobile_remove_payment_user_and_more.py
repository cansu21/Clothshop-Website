# Generated by Django 4.0.4 on 2022-05-07 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0041_cart_cartproduct_remove_order_payment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.AddField(
            model_name='payment',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.customer'),
        ),
        migrations.AddField(
            model_name='payment',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('Cash On Delivery', 'Cash On Delivery'), ('CreditCard', 'CreditCard')], default='Cash On Delivery', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]