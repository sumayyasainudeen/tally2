# Generated by Django 4.1.4 on 2023-03-23 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0030_bank_transcations_company_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank_transcations',
            name='cheque_printed',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]