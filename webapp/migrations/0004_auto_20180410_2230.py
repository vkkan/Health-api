# Generated by Django 2.0.4 on 2018-04-10 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20180410_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='formmodel',
            name='[10][PastHistory]',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='formmodel',
            name='[1][PastHistory]',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='formmodel',
            name='[2][PastHistory]',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='formmodel',
            name='[3][PastHistory]',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='formmodel',
            name='[4][PastHistory]',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='formmodel',
            name='[5][PastHistory]',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='formmodel',
            name='[6][PastHistory]',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='formmodel',
            name='[7][PastHistory]',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='formmodel',
            name='[8][PastHistory]',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='formmodel',
            name='[9][PastHistory]',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Kureid',
            field=models.CharField(default='cratIIZxt2bU9yN5YXfUNoRPi38HyjBC', max_length=120),
        ),
    ]
