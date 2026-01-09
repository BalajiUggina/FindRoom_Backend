from django.db import models
from apps.users.models import User

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('both', 'Both'),
)

class Hostel(models.Model):
    provider = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="hostels"
    )

    name = models.CharField(max_length=255)   # Example: "Sri Krishna Boys Hostel"
    address = models.TextField()
    area = models.CharField(max_length=150)
    city = models.CharField(max_length=150)

    facilities = models.JSONField(blank=True, null=True, default=list)

    rules = models.JSONField(blank=True, null=True, default=list)

    gender_allowed = models.CharField(max_length=20, choices=GENDER_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.area}, {self.city}"



class HostelRoom(models.Model):
    hostel = models.ForeignKey(
        Hostel,
        on_delete=models.CASCADE,
        related_name="rooms"
    )

    occupancy = models.CharField(max_length=20)     # "1 sharing", "2 sharing"
    rent_per_month = models.IntegerField()

    bills_included = models.BooleanField(default=False)
    extra_bills = models.JSONField(blank=True, null=True, default=list)

    availability_status = models.CharField(max_length=20, default="available")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.hostel.name} - {self.occupancy} ({self.availability_status})"


class HostelImage(models.Model):
    hostel = models.ForeignKey(
        Hostel,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to="hostel_images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.hostel.name}"
