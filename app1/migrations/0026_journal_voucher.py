# Generated by Django 4.1.4 on 2023-02-25 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0025_fmonths_stock_item_voucher_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='journal_voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jid', models.IntegerField(null=True)),
                ('account', models.CharField(max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('amount', models.IntegerField(null=True)),
                ('narration', models.CharField(max_length=255, null=True)),
                ('voucher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.voucher')),
            ],
        ),
    ]
