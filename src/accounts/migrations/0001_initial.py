# Generated by Django 4.2 on 2024-09-24 16:34

import accounts.manager
from django.db import migrations, models
import django.utils.timezone
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=120, null=True, verbose_name="name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=120, null=True, verbose_name="surname"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        error_messages={
                            "unique": "A user with that email already exists."
                        },
                        max_length=254,
                        unique=True,
                        verbose_name="email address",
                    ),
                ),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True,
                        max_length=128,
                        null=True,
                        region=None,
                        verbose_name="phone number",
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        blank=True, null=True, verbose_name="date of birth"
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="country"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="city"
                    ),
                ),
                (
                    "registration_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="registration date"
                    ),
                ),
                (
                    "client_status",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, "Active"), (0, "Inactive"), (-1, "Blocked")],
                        default=1,
                        null=True,
                        verbose_name="client status",
                    ),
                ),
                (
                    "bonus_points",
                    models.PositiveSmallIntegerField(
                        blank=True, default=100, null=True, verbose_name="bonus points"
                    ),
                ),
                (
                    "notes_to_client",
                    models.TextField(
                        blank=True, null=True, verbose_name="notes to client"
                    ),
                ),
                (
                    "client_photo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="media/img/client",
                        verbose_name="client photo",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "client",
                "verbose_name_plural": "clients",
            },
            managers=[
                ("object", accounts.manager.ClientManager()),
            ],
        ),
    ]
