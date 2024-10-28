import os
import django

# Установить переменную окружения на файл настроек Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")

# Инициализация Django
django.setup()
import random

from faker import Faker

from hotels.models import Room, Hotel


def create_test_rooms(count):
    fake = Faker()
    rooms = []
    for _ in range(count):
        room = Room.objects.create(
            room_number=random.randint(1, 500),
            room_type=random.choice(["SGL", "DBL", "TWN", "STU", "APT", "DEL", "FAM", "OFF"]),
            room_status=random.choice(["AVAILABLE", "OCCUPIED", "RESERVED", "MAINTENANCE"]),
            price_per_night=round(random.uniform(100, 2000), 2),
            floor=random.randint(1, 10),
            room_description=fake.paragraph(nb_sentences=2),
        )
        room.save()
        rooms.append(room)
    return rooms


def create_test_hotels(count):
    fake = Faker()
    rooms = create_test_rooms(count)
    for i in range(count):
        hotel = Hotel.objects.create(
            country=fake.country(),
            city=fake.city(),
            hotel_name=fake.company(),
            hotel_star_rating=random.choice([1, 2, 3, 4, 5]),
            address=fake.address(),
            hotel_photo=None,
            number_of_rooms=random.randint(1, 500),
            phone_number=fake.phone_number(),
            email=fake.email(),
            website=fake.url(),
            description=fake.paragraph(nb_sentences=1),
            client_reviews=fake.paragraph(nb_sentences=1),
        )
        hotel.room.set([rooms[i]])
        hotel.save()


create_test_hotels(3)
