# Generated by Django 4.1.4 on 2023-03-29 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0032_journal_particulars'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='no_of_vouchers',
            field=models.IntegerField(default=0),
        ),
    ]
