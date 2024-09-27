# Generated by Django 4.2 on 2024-09-26 13:41

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("hotels", "0002_amenity_alter_hotel_options_room_hotel_room"),
        ("bookings", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="hotel",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="hotel",
                to="hotels.hotel",
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="booking_status",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "active"), (0, "inactive")],
                default=0,
                null=True,
                verbose_name="booking status",
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="client",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="client",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="total_price",
            field=models.FloatField(
                blank=True,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
                verbose_name="total price",
            ),
        ),
    ]
