from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework import status

"""
TODO 
GET: Name, Availability, Age
PUT: Updated based off ID
"""


@api_view(['GET'])
def get_pet_list(request):
    """
    List All of the Pets currently stored in the database.
    """

    if request.method == 'GET':
        pets = models.Pet.objects.all()
        serializer = serializers.PetSerializer(pets, many=True)
        return Response(serializer.data)
    return "No Pets Found."


@api_view(['GET', 'PUT', 'DELETE'])
def pet_by_ID(request, id):
    """
    List The Pet with the given ID.
    """

    if request.method == 'GET':
        try:
            pets = models.Pet.objects.filter(id=request.data["id"]).get()
            serializer = serializers.PetSerializer(pets, many=True)
            return Response(serializer.data)
        except:
            return "No Pets Found this ID: " + id
    elif request.method == 'PUT':
        try:
            # Look for pet based on ID, if it does not exist you create the pet. 
            # If the pet is found you update it with the data provided in the request.
            pet = models.Pet.objects.update_or_create()
        except:
            return Response("Unable to process request", status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            pet = models.Pet.objects.filter(id = id).get()
            pet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response('No Pet found with such ID', status=status.HTTP_404_NOT_FOUND)
            
    return Response("Unable to process request", status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post_pet(request):
    """
    Creates a new Pet and stores it in the database.
    """

    if request.method == 'POST':
        serializer = serializers.PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return request


    

@api_view(['PUT'])
def put_pet(request,id):
    
    return 'Wrong Request Method used.'
    

# Create your views here.
