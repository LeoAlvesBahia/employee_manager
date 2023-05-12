import json

from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee, Department
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def api_employees(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        data = [
            {
                'id': employee.id,
                'name': employee.name,
                'email': employee.email,
                'department': employee.department.name
            }
            for employee in employees
        ]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        department_id = data.get('department')

        try:
            department = Department.objects.get(id=department_id)
        except Department.DoesNotExist:
            return JsonResponse({'error': 'Department does not exist'},
                                status=400)

        employee = Employee(name=name, email=email, department=department)
        employee.save()

        return JsonResponse({'message': 'Employee added successfully'},
                            status=201)
    elif request.method == 'DELETE':
        data = json.loads(request.body)
        employee_id = data.get('id')

        try:
            employee = Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            return JsonResponse({'error': 'Employee does not exist'},
                                status=404)

        employee.delete()

        return JsonResponse({'message': 'Employee deleted successfully'},
                            status=204)


def public_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


@csrf_exempt
def api_department(request, department_name=None):
    if request.method == 'GET':
        departments = Department.objects.all()
        data = [
            {
                'id': department.id,
                'name': department.name
            }
            for department in departments
        ]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')

        if not name:
            return JsonResponse({'error': 'Department name is required'},
                                status=400)

        department = Department.objects.create(name=name)

        return JsonResponse({'message': 'Department created successfully',
                             'department_id': department.id})
    elif request.method == 'DELETE':
        try:
            department = Department.objects.get(id=department_name)
            department.delete()
            return JsonResponse({'message': 'Department deleted successfully'},
                                status=204)
        except Department.DoesNotExist:
            return JsonResponse({'error': 'Department does not exist'},
                                status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
