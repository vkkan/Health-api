# Generated by Django 2.0.5 on 2018-07-11 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_auto_20180627_0657'),
    ]

    operations = [
        migrations.CreateModel(
            name='SnomedTerms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conceptID', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
