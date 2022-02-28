# Generated by Django 3.0.6 on 2020-12-13 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=250, null=True)),
                ('lastname', models.CharField(max_length=250, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_joined', models.DateField(null=True)),
                ('credit', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True)),
            ],
        ),
    ]
