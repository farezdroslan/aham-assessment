from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Fund
from .serializer import FundSerializer

# Create your views here.

def say_hello(request):
    # return HttpResponse('Hello World')
    return render(request, 'hello.html', {'name': 'Fund'})

@api_view(['GET'])
def get_funds(request):
    """
    Retrieve all funds from the database and return them as JSON.
    """
    if request.method == 'GET':
        # Query all funds from the database
        funds = Fund.objects.all()

        # Serialize the queryset into JSON-compatible data
        serializer = FundSerializer(funds, many=True)

        # Return the serialized data as a JSON response
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_fund(request):
    """
    Create a new fund and return it as JSON.
    """
    if request.method == 'POST':
        # Deserialize the incoming data
        serializer = FundSerializer(data=request.data)
        
        # Validate and save the data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Return validation errors if the data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def fund_detail(request, pk):
    try:
        fund = Fund.objects.get(pk=pk)
    except Fund.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = FundSerializer(fund)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = FundSerializer(fund, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        fund.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

