# Generated by Django 4.0.4 on 2022-05-10 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0054_reviewitem_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewitem',
            name='review_status',
            field=models.CharField(blank=True, choices=[('Not Approved', 'Not Appoved'), ('Appoved', 'Appoved')], max_length=50, null=True),
        ),
    ]