from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

# GET all + POST
@api_view(['GET', 'POST'])
def employee_list(request):

    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# GET single + PUT + DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pk):

    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response({"error": "Not found"})

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == 'DELETE':
        employee.delete()
        return Response({"message": "Deleted successfully"})