from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backEnd.petAPI.models import Pet
from backEnd.petAPI.serializers import *

"""
GET: Get by ID, Name, Availability, Age
POST
PUT: Updated based off ID
DELETE: Delete based off ID

"""


@api_view(['GET'])
def get_pet_list(request):
    """
    List All of the Pets currently stored in the database.
    """

    if request.method == 'GET':
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)
    return "No Pets Found."

# Create your views here.
