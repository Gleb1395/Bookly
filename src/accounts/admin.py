from django.contrib import admin
from django.contrib.auth import get_user_model


@admin.register(get_user_model())
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'date_of_birth',
        'country',
        'city',
        "registration_date",
        'client_status',
        'bonus_points',
        'client_photo',
        'is_staff',
        'is_active',
        'date_joined',
    )
    exclude = ('groups', 'user_permissions')
