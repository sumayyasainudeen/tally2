# Generated by Django 4.1.4 on 2023-03-15 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0028_journal_voucher_voucher_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journal_voucher',
            old_name='voucher_name',
            new_name='jname',
        ),
    ]