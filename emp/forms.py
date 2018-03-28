from django.forms import ModelForm
from emp.models import Employee


class EmployeeForm(ModelForm):
	class Meta:
		model = Employee
		fields = ['emp_id','emp_name','designation']

