# Generated by Django 4.2.3 on 2023-08-25 18:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0002_category_product_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
