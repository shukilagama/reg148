# Generated by Django 4.1.9 on 2023-05-21 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crapi', '0002_order_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliedcoupon',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mechanic',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
