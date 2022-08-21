# Generated by Django 4.0.4 on 2022-05-07 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0046_delete_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
