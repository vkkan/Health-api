# Generated by Django 2.0.4 on 2018-04-10 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20180410_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='formmodel',
            name='ProvisionalDiagnosis',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='formmodel',
            name='Kureid',
            field=models.CharField(default='SRNPTOmWlRpY4iUDAp9QEy23HEaB9s3m', max_length=120),
        ),
    ]
