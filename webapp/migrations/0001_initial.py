# Generated by Django 2.0.3 on 2018-04-04 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=10)),
                ('emailAddress', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('comEmail', models.BooleanField(default=False)),
                ('comSms', models.BooleanField(default=False)),
                ('comPhone', models.BooleanField(default=False)),
                ('payCreditCard', models.BooleanField(default=False)),
                ('payBitCoin', models.BooleanField(default=False)),
                ('payCash', models.BooleanField(default=False)),
                ('amount', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='stepOneModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=10)),
                ('emailAddress', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('comEmail', models.BooleanField(default=False)),
                ('comSms', models.BooleanField(default=False)),
                ('comPhone', models.BooleanField(default=False)),
                ('payCreditCard', models.BooleanField(default=False)),
                ('payBitCoin', models.BooleanField(default=False)),
                ('payCash', models.BooleanField(default=False)),
                ('amount', models.CharField(max_length=10)),
            ],
        ),
    ]
