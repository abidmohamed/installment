# Generated by Django 3.0.6 on 2020-12-16 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
        ('customer', '0004_auto_20201212_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=0)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('pay_status', models.CharField(blank=True, choices=[('Cash', 'Cash'), ('Cheque', 'Cheque')], default='Cash', max_length=8)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='SupplierCheque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cheque_number', models.PositiveIntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.Supplier')),
                ('supplierpayment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.SupplierPayment')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=0)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('pay_status', models.CharField(blank=True, choices=[('Cash', 'Cash'), ('Cheque', 'Cheque')], default='Cash', max_length=8)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerCheque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cheque_number', models.PositiveIntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
                ('customerpayment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.CustomerPayment')),
            ],
        ),
    ]
