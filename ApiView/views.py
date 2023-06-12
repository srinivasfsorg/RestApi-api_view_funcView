from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ApiView.models import Employs
from ApiView.serializers import EmpSerializer
# Create your views here.

@api_view(['GET','POST', 'PUT', 'DELETE'])
def employ_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            emp = Employs.objects.get(id = id)
            serializer = EmpSerializer(emp)
            return Response(serializer.data)
        emp = Employs.objects.all()
        serializer = EmpSerializer(emp,many=True)
        return Response(serializer.data)