# Generated by Django 4.0.4 on 2022-05-12 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0063_alter_product_distributor'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmanagersadmin',
            name='distributor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.distributor'),
        ),
    ]
