# Generated by Django 4.0.4 on 2022-05-02 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_product_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Secondimage',
            field=models.ImageField(default='', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Thirdimage',
            field=models.ImageField(default='', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='distributor',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='model',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='warrantyStatus',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
