from rest_framework import  serializers
from api.models import company,Employee
# creating serialzers here``

class companySerializer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    
    class Meta:
         model=company
         fields="__all__"
    


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"


    












# class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
#      id = serializers.ReadOnlyField()

#      class Meta:
#           modol = Employee
#           fields = "__all__"