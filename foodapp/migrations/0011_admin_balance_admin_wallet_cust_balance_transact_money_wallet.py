# Generated by Django 2.2.24 on 2023-02-28 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0010_auto_20200305_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('transactions', models.TextField(blank=True, default='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.Cust')),
            ],
        ),
        migrations.CreateModel(
            name='transact_money',
            fields=[
                ('transact_ID', models.AutoField(primary_key=True, serialize=False)),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('checksum', models.CharField(blank=True, max_length=100, null=True)),
                ('made_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='foodapp.Cust')),
                ('orders', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='order_id', to='foodapp.Order')),
            ],
        ),
        migrations.CreateModel(
            name='cust_balance',
            fields=[
                ('wallet_ID', models.AutoField(primary_key=True, serialize=False)),
                ('balance', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.Cust')),
            ],
        ),
        migrations.CreateModel(
            name='admin_wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.Admin')),
            ],
        ),
        migrations.CreateModel(
            name='admin_balance',
            fields=[
                ('wallet_ID', models.AutoField(primary_key=True, serialize=False)),
                ('balance', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.Admin')),
            ],
        ),
    ]