# Generated by Django 4.1.5 on 2023-01-15 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_userdetail_accountnumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('accountNumber', models.BigIntegerField(primary_key=True, serialize=False)),
                ('accountCreationDate', models.DateField(default='1905-01-01')),
                ('accountStatus', models.CharField(default='ACTIVE', max_length=20)),
                ('accountBalance', models.DecimalField(decimal_places=2, max_digits=20)),
                ('accountUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.userdetail')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transactionId', models.BigIntegerField(primary_key=True, serialize=False)),
                ('toAccount', models.BigIntegerField(default=0)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('transactionDate', models.DateField(default='1905-01-01')),
                ('transactionStatus', models.CharField(default='PENDING', max_length=20)),
                ('fromAccount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.account')),
            ],
        ),
    ]
