# Generated by Django 5.0.3 on 2024-10-22 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_admin_dashboard', '0003_alter_order_items_ordered_alter_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='staff_id',
            field=models.IntegerField(default='null'),
        ),
    ]
