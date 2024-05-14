# Generated by Django 5.0.6 on 2024-05-14 13:40

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_cart_uuid_alter_cartitem_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='id',
        ),
        migrations.AlterField(
            model_name='cart',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]