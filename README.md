```
# IGS Employee Manager

The "IGS Employee Manager" is a Django web application for managing employee information, such as name, email address, and department. It provides an administrative panel, an API for integration, and a public website for viewing employee details.

## Requirements

- Python 3.10
- Django 4.2

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/igs-employee-manager.git
   ```

2. Create and activate a virtual environment:

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Apply the database migrations:

   ```
   python manage.py migrate
   ```

5. Run the development server:

   ```
   python manage.py runserver
   ```

6. Access the application in your web browser at `http://localhost:8000`.

## Features

- Admin Panel: Access the Django admin panel to manage employee and department data.

- API Endpoints:
  - `GET /api/employees/`: Retrieve a list of employees.
  - `POST /api/employees/`: Add a new employee.
  - `DELETE /api/employees/{employee_id}/`: Remove an employee.
  - `GET /api/departments/`: Retrieve a list of departments.
  - `POST /api/departments/`: Add a new department.
  - `DELETE /api/departments/{department_id}/`: Remove a department.

- Public Website: View a simple table listing all employees and their departments.

## License

This project is licensed under the MIT License.
```