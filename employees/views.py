from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee, Department


# Create your views here.
def api_employees(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        data = [
            {
                'name': employee.name,
                'email': employee.email,
                'department': employee.department.name
            }
            for employee in employees
        ]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        department_name = request.POST.get('department')

        try:
            department = Department.objects.get(name=department_name)
        except Department.DoesNotExist:
            return JsonResponse({'error': 'Department does not exist'},
                                status=400)

        employee = Employee(name=name, email=email, department=department)
        employee.save()

        return JsonResponse({'message': 'Employee added successfully'},
                            status=201)
    elif request.method == 'DELETE':
        employee_id = request.GET.get('id')

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
    return render(request, 'employees/employee_list.html',
                  {'employees': employees})
