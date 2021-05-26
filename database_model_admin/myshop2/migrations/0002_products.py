# Generated by Django 3.2.3 on 2021-05-18 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('Product_descriptions', models.TextField()),
                ('price', models.FloatField(default=0.0)),
            ],
        ),
    ]
