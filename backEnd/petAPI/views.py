from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from petAPI.models import *
from petAPI.serializers import *
from rest_framework import status

"""
TODO 
GET: Name, Availability, Age
PUT: Updated based off ID
DTO Design to filter out information that does not need to be send to front-end
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


@api_view(['GET', 'PUT', 'DELETE'])
def pet_by_ID(request, id):
    """
    Processes data about Pet with given ID - GET, PUT, DELETE
    """

    if request.method == 'GET':
        try:
            pets = Pet.objects.filter(id=id)
            serializer = PetSerializer(pets, many=True)
            return Response(serializer.data)
        except:
            return "No Pets Found this ID: " + id
    elif request.method == 'PUT':
        try:
            pet = pet.objects.filter(id = id).get()
            serializer = PetSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            serializer = PetSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response("Unable to precess request", status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            pet = Pet.objects.filter(id = id).get()
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
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return request


    
"""
@api_view(['PUT'])
def put_pet_by_id(request,id):
    
    Create or updates a pet and stores it in the database
    

    
    return 'Wrong Request Method used.'
    

# Create your views here.
"""