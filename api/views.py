from django.shortcuts import render
from rest_framework import viewsets
from api.models import  company,Employee
from api.serializers import companySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
 

class companyViewSet(viewsets.ModelViewSet):
    queryset=company.objects.all()
    serializer_class=companySerializer
#   company/{id}/employees
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try: 
          company=company.objects.get(pk=pk)
          emps=Employee.objects.filter(company=company)
          emps_serializer=EmployeeSerializer(emps,many=True,contex={'request':request})
          return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'massage': "company might not exists !! Error"

            })





# Creating Employee views
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
