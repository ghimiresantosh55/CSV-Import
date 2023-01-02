import csv
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Customer
from rest_framework.views import APIView
from .serializers import CustomerSerializer

from . resources import CustomerResource
from django.contrib import messages
from tablib import Dataset
from rest_framework import viewsets

class CustomerViewSet(viewsets.ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

def simple_upload(request):
    if request.method=='POST':
        customer_resource = CustomerResource()
        dataset = Dataset()
        new_person = request.FILES['myfile']

        if not new_person.first_name.endswith('xlsx'):
            messages.info(request,' this is wrong format')
            return render(request,'upload.html')

        imported_data = dataset.load(new_person.read(), format='xlsx')
        for data in imported_data:
            value= Customer(
                data[0],
        		data[1],
        		data[2],
        		data[3]
                )
            value.save()  
            
    return render(request, 'upload.html')