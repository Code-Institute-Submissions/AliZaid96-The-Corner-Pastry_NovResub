# Generated by Django 4.1.1 on 2022-10-30 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_orderproducts_alter_categories_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='order_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
