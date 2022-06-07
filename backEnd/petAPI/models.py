from uuid import uuid4
from django.db import models


AVAILABILITIES_OPTION = [
    ('Available', 'Available'),
    ('Adopted', 'Adopted'),
    ('Under Consideration','Under Consideration'),
]


class Pet(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    age = models.IntegerField()
    availability = models.CharField(max_length=100, choices=AVAILABILITIES_OPTION)
    photoUrl = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name

# Create your models here.
