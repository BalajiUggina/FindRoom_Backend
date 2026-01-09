from django.db import models
from apps.users.models import User

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('both', 'Both'),
)

class StandaloneRoom(models.Model):
    provider = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="standalone_rooms"
    )

    occupancy = models.CharField(max_length=20)  # "1 sharing", "2 sharing"
    rent_per_month = models.IntegerField()

    bills_included = models.BooleanField(default=False)
    extra_bills = models.JSONField(blank=True, null=True, default=list)

    facilities = models.JSONField(blank=True, null=True, default=list)

    rules = models.JSONField(blank=True, null=True, default=list)

    gender_allowed = models.CharField(max_length=20, choices=GENDER_CHOICES)
    availability_status = models.CharField(max_length=20, default='available')

    address = models.TextField()
    area = models.CharField(max_length=150)
    city = models.CharField(max_length=150)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Standalone Room - {self.area}, {self.city} ({self.availability_status})"




class StandaloneRoomImage(models.Model):
    room = models.ForeignKey(
        StandaloneRoom,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to="standalone_room_images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for Room {self.room.id}"
