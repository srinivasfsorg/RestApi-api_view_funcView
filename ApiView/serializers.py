from rest_framework import serializers
from ApiView.models import Employs

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employs
        fields = ['id', 'empid', 'empname', 'salary', 'deptid']