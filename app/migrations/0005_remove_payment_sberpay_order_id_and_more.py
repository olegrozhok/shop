# Generated by Django 4.1.4 on 2022-12-17 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_payment_orderplaced'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='sberpay_order_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='sberpay_payment_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='sberpay_payment_status',
        ),
        migrations.AddField(
            model_name='payment',
            name='razorpay_payment_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='razorpay_payment_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
