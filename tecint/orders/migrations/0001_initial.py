# Generated by Django 4.0.1 on 2022-01-22 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderLines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Shipped', 'Shipped'), ('Pending', 'Pending'), ('Cancelled', 'Canceled')], default='Pending', max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='OrderNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Shipped', 'Shipped'), ('Pending', 'Pending'), ('Cancelled', 'Canceled')], default='Pending', max_length=9)),
                ('items', models.ManyToManyField(blank=True, null=True, to='orders.OrderLines')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.ordernumber')),
            ],
        ),
        migrations.AddField(
            model_name='orderlines',
            name='order_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.ordernumber'),
        ),
    ]
