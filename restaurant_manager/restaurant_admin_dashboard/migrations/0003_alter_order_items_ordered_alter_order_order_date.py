# Generated by Django 5.0.3 on 2024-10-22 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_admin_dashboard', '0002_staff_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items_ordered',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(),
        ),
    ]
