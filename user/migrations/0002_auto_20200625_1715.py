# Generated by Django 3.0.5 on 2020-06-25 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlist',
            name='Quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productlist',
            name='features',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='productlist',
            name='use',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.CreateModel(
            name='Order_Table',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=500)),
                ('amount', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=111)),
                ('address', models.CharField(max_length=1110)),
                ('city', models.CharField(max_length=110)),
                ('state', models.CharField(max_length=110)),
                ('zip_code', models.CharField(max_length=110)),
                ('phone', models.CharField(default='', max_length=110)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart_Data',
            fields=[
                ('quantity', models.PositiveIntegerField(default=0)),
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='user.ProductList')),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
